import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Stock Visualization Web App",
    page_icon="📈",
)
image = Image.open("/Users/sarahgolden/Desktop/SMWapp/stocks/assets/logo.png") #copy path by right clicking file on vs code

st.image(image, width=150)

st.title("Stock Market Web Application")
st.write("""
        **Welcome!**

        Click on the menu on the left to begin.
        
        """)
