import streamlit as st

class ChatBot():

    def run(self):
        with st.chat_message(name="assistant", avatar="👩🏻‍🦰"):   # chat message feature is like a container, can add anything
            st.write("Hey there! 👋🏻")
            st.write("I'm Jane, your personal assistant. How may I help you today?")
