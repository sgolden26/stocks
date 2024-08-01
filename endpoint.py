import streamlit as st
# --- Page Setup ---
home_page = st.Page(
    page="views/Home.py",
    title="Home Page",
    icon="🏠",
    default=True,
)

stocks_page = st.Page(
    page="views/Stock_Data.py", # 2_📈_Stock_Data
    title="Stock Data and Visualization",
    icon="📈",
)

chat_page = st.Page(
    page="views/Chat_Bot.py",
    title="Any Questions? Talk to Jane!",
    icon="💬",
)

# -- Navigation setup [without sections] ---
pg = st.navigation(
    pages=[home_page, stocks_page, chat_page]
)

# --- Run navigation ---
pg.run()

# --- Shared on all pages ---
st.logo("assets/logo.png")