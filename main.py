# import the libraries
import streamlit as st
import pandas as pd
from PIL import Image
from StockWebApp import StockWebApp
from ChatBot import ChatBot
import json



# Now set up
web = StockWebApp()
chat = ChatBot()

web.setup()

# Get the users input
start, end, symbol, passed = web.get_input()

#analysis = StockAnalysis(symbol, start, end)

if passed:

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
   
    # Chat for questions
    st.header('Any questions? Talk to Jane!')
    chat.run()



    #analysis
   
    #df2 = analysis.get_data(symbol, start, end)
    #st.header('Stock Analysis')
    #st.write(df2.describe())
    