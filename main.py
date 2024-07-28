# import the libraries
import streamlit as st
import pandas as pd
from PIL import Image
from StockWebApp import StockWebApp

web = StockWebApp()

web.setup()

# Get the users input
start, end, symbol = web.get_input()

# Get the data
df = web.get_data(symbol, start, end)

# Get company name
company_name = web.get_company_name(symbol.upper())

# Display the close price
st.header(company_name + " Close Price\n")
st.line_chart(df['Close'])

# Display the volume
st.header(company_name + " Volume\n")
st.line_chart(df['Volume'])

# Get stats on data
st.header('Data Statistics')
st.write(df.describe())