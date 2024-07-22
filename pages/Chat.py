import streamlit as st
from src.helper import *


llm = ResponseLLM()

# Ensure a character is selected before displaying the chat
if 'selected_fighter' not in st.session_state:
    st.warning("Please select a character from the home page.")
    st.stop()

st.header(f"Chat with {st.session_state.selected_fighter}")

# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # Display previous messages
# for message in st.session_state.messages:
#     st.write(message)

# Input for new message
user_input = st.text_input("You: ", "")
name = st.session_state.selected_fighter
print(f"first name{name}")
name = name.split()
print(f'after convert into lower{name}')
name = name[0].lower()
print(f'first word after split{name}')


if st.button("Send"):
    if user_input:
        # st.session_state.messages.append(f"You: {user_input}")
        response = llm.response(user_input,name)
        st.write(response)
        
        

if st.button("Back"):
    st.switch_page("Home.py")
