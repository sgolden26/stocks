import pandas as pd
import datetime
import yfinance as yf
#from StockWebApp import StockWebApp


# Data Readers can show us how to read this
class StockAnalysis:
  
   # starting values
   start = datetime.datetime(2023, 7, 28)
   end = datetime.datetime(2024, 7, 26)
   sym = "AMZN"


   def __init__(self, symbol, start, end):   #start, end, symbol passed in as a string in main class
    # can convert to_datetime?
       year = lambda s: int(s[:4])
       month = lambda s: int(s[5:7])
       day = lambda s: int(s[8:])
      
       self.start = datetime.datetime(year(start), month(start), day(start))
       self.end = datetime.datetime(year(end), month(start), day(start))
       self.sym = symbol


   def get_data(self, symbol, start, end):
       df = yf.Ticker('GOOGL').history(start, end)
       return df


   def get_date(self, type_of_date):
       return type_of_date


   def get_symbol(self):
       return self.sym

    """
    s = StockAnalysis("AMZN", "2023-07-28", "2024-07-26")
    print(s.get_date(s.start))  #returns 2023-07-28 00:00:00
    print(s.get_date(s.end))    # returns 2024-07-28 00:00:00
    print(s.get_symbol())   # returns MZN
    """