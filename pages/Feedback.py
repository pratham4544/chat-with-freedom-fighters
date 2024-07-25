import streamlit as st
from pymongo import MongoClient
import os

# MongoDB connection setup
# Replace with your MongoDB server's connection string
MONGO_URI = os.environ['MONGO_URI']
client = MongoClient(MONGO_URI)
db = client["freedom_feedback_database"]
collection = db["freedom_feedback_collection"]

st.title("Feedback Form")

# Form fields
name = st.text_input("Name")
email = st.text_input("Email")
rating = st.slider("Rate our service", 1, 5)
comments = st.text_area("Comments")

# Submit button
if st.button("Submit"):
    if not name or not email:
        st.error("Please fill in all required fields.")
    else:
        # Prepare the data to be inserted
        feedback = {
            "name": name,
            "email": email,
            "rating": rating,
            "comments": comments
        }
        # Insert the feedback into MongoDB
        collection.insert_one(feedback)
        
        st.success("Thank you for your feedback!")
        # Optionally, you can display the submitted feedback
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Rating:", rating)
        st.write("Comments:", comments)
