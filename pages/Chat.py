import streamlit as st
from pymongo import MongoClient
from src.helper import *
import os

# Initialize your language model
llm = ResponseLLM()

# MongoDB connection setup
MONGO_URI = os.environ['MONGO_URI'] # Replace with your MongoDB server's connection string
client = MongoClient(MONGO_URI)
db = client["freedom_chat_database"]
collection = db["freedom_chat_collection"]

# Ensure a character is selected before displaying the chat
if 'selected_fighter' not in st.session_state:
    st.warning("Please select a character from the home page.")
    st.stop()

st.header(f"Chat with {st.session_state.selected_fighter}")

user_input = st.text_input("You: ", "")
name = st.session_state.selected_fighter
print(f"first name{name}")
name = name.split()
print(f'after convert into lower{name}')
name = name[0].lower()
print(f'first word after split{name}')

if st.button("Send"):
    if user_input:
        # Generate the response from the language model
        response = llm.response(user_input, name)
        st.write(response)

        # Prepare the data to be inserted into MongoDB
        chat_entry = {
            "character": st.session_state.selected_fighter,
            "user_input": user_input,
            "response": response
        }

        # Insert the chat entry into MongoDB
        collection.insert_one(chat_entry)
        
        # st.success("Your question and the response have been stored.")

if st.button("Back"):
    st.switch_page("Home.py")
