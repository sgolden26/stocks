import streamlit as st
import openai
import json

class ChatBot():
    def get_openai_key(self): # Secret.

        # get my personal OpenAI API key
        with open('config.json') as config_file:
            config = json.load(config_file)

        openai_api_key = config['OPENAI_API_KEY']

        if not openai_api_key:
            raise ValueError("No OPENAI_API_KEY found in config.json")
        else:
            return openai_api_key

    def run(self):

        openai.api_key = self.get_openai_key()
      
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-4o-mini"

        # session state allows app to remember data bw user interactions
        # messages holds a dictionary of 
        # initialize chat history
        if "message" not in st.session_state:
            st.session_state.messages = []

        # Display chat msg from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # React to user input
        # := symbol assigns user's input to the 'prompt' variable
        # same as assigning prompt to the right of the := and checking if not none
        if prompt := st.chat_input("What is up?"):
            # Display user message in chat msg contianer
            with st.chat_message("user", avatar="👤"):
                st.markdown(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            response = f"Jane: {prompt}"
            # Display assistant response in chat message container
            with st.chat_message(name="assistant", avatar="👩🏻‍🦰"):
                message_placeholder = st.empty()
                full_response = ""
                # chat completion calls open ai's API
                for response in openai.ChatCompletion.create(
                    model=st.session_state["openai_model"], # pass in model, saved in session state
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True, #simulate typing effect
                ): # end of for loop header
                    full_response += response.choices[0].delta.get("content", "") # add chat gpt response to full response string
                    # show chat response so far
                    message_placeholder.markdown(full_response + "**|** ") # | to simulate blinking cursor
                message_placeholder.markdown(full_response) # after the loop, display full response one more time
            st.session_state.messages.append({"role": "assistant", "content": full_response}) # add chat gpt response to messages list
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
        
st.title("Hello")
st.write("Have a question? Jane can help you.")
chat = ChatBot()
chat.run()