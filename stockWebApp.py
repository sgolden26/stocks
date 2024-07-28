"""
Description: This is a stock market dashboard to show some 
charts and data on some stock

# S & P Data: https://www.investing.com/indices/us-spx-500-historical-data
"""

# import the libraries
import streamlit as st
import pandas as pd
from PIL import Image

class StockWebApp:

    start = "2023-07-28"
    end =  "2024-07-26"
    sym = "AMZN"

    sym_available = ["AMZN", "GOOG", "META", "S&P500", "TSLA"]

    def setup(self):
        # Add a title and an image
        # ** bolds the text and # makes it the title
        st.write("""
        # Stock Market Web Application
        **Visually** show data on a stock! Date range from July 28, 2023 to July 26, 2024
        """)

        image = Image.open("/Users/sarahgolden/Desktop/SMWapp/stocks/stocks.png") #copy path by right clicking file on vs code

        st.image(image, use_column_width=True)

        # Create a sidebar header
        st.sidebar.header('User Input') # have user input start date, end date, and stock symbol

    # Create a function to get the users input
    def get_input(self):
        start_date = st.sidebar.text_input("Start Date", self.start)
        end_date = st.sidebar.text_input("End Date", self.end)
        stock_symbol = st.sidebar.text_input("Stock Symbol", self.sym)
        # self.valid returns an error if stock symbol is invalid, otherwise returns the stock symbol
        start_date, end_date, stock_symbol, passed = self.valid(start_date, end_date, stock_symbol)
        return start_date, end_date, stock_symbol, passed

            
    # Create a function to get the company name
    def get_company_name(self, symbol):
        if symbol == 'AMZN':
            return 'Amazon'
        elif symbol == 'GOOG':
            return 'Alphabet'
        elif symbol == 'META':
            return 'Meta'
        elif symbol == 'TSLA':
            return 'Tesla'
        else:
            return 'None'

    # Create a function to get the proper company data and the proper timeframe
    # From user start date to the user end date
    def get_data(self, symbol, start, end):

        # Load the data
        if symbol.upper() == 'AMZN':
            df = pd.read_csv("/Users/sarahgolden/Desktop/SMWapp/stocks/data/AMZN.csv")
        elif symbol.upper() == 'GOOG':
            df = pd.read_csv("/Users/sarahgolden/Desktop/SMWapp/stocks/data/GOOG.csv")
        elif symbol.upper() == 'META':
            df = pd.read_csv("/Users/sarahgolden/Desktop/SMWapp/stocks/data/META.csv")
        elif symbol.upper() == 'TSLA':
            df = pd.read_csv("/Users/sarahgolden/Desktop/SMWapp/stocks/data/TSLA.csv")
        else:
            df = pd.DataFrame(columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']) 

        # Get the date range
        # Convert dates to datetime data type
        new_start = pd.to_datetime(start)
        new_end = pd.to_datetime(end)

        # Set the start and end index rows both to 0
        start_row = 0
        end_row = 0

        # Start the date from the top of the data set and ggo down to see if the users start 
        # date is less than or equal to the dataset
            # sometimes stock market not open due to holidays

        # Find starting index
        for i in range(0, len(df)):
            if new_start <= pd.to_datetime(df['Date'][i]):
                start_row = i
                break

        # Start from the bottom of the dataset and look up to see if the users end date is
        # greater than or equal to the end date in the data set
        for i in range(0, len(df)):
            if new_end >= pd.to_datetime(df['Date'][len(df) - 1 - i]):
                end_row = len(df) - 1 - i
                break

        # Set the index to be the date
            # df['Date'].values extracts the values from the 'Date' column as a NumPy array
            # df.set_index replaces the current index of the df w the newly created DateTimeIndex
                # DateTimeIndex in Pandas Library does the following:
                    # Can slice data by date ranges. 
                        # Ex: df['2022-01-01':'2022-01-03']
                    # Resample date to diff frequencies, such as daily, monthly, or yearly
                        # Ex: df.resample('M').mean()
        df = df.set_index(pd.DatetimeIndex(df['Date']. values))

        # iloc is an indexer for pandas DataFrames and Series tha allows for integer location
        return df.iloc[start_row:end_row + 1, :]    #want only start-end rows, all of the columns

    """ SPECIAL FUNCS """
    # Check for valid inputs, stop program from outputting error if not valid and instead raise warning visual
    def valid(self, start_date, end_date, stock_symbol):
        old_values = [start_date, end_date, stock_symbol]
        # second return value so that we can prevent TypeError
        if pd.to_datetime(start_date) < pd.to_datetime(self.start):
            start_date = st.error(f'**Error:** Only data from {self.start} is available. Please try again.', icon="🚨"), False
        if pd.to_datetime(end_date) > pd.to_datetime(self.end):
            end_date = st.error(f'**Error:** Only data until {self.end} is available. Please try again.', icon="🚨"), False
        if stock_symbol not in self.sym_available:
            stock_symbol = st.error(f'**Error:** Stock data for {stock_symbol} is not available yet. Please try again.', icon="🚨"), False
        new_values = [start_date, end_date, stock_symbol]
        is_valid = old_values==new_values
        return start_date, end_date, stock_symbol, is_valid
      