import streamlit as st
import zipfile
import os
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient(os.environ['MONGO_URI'])
db = client.freedom_fighters
collection = db.contributors

# Function to save uploaded files to a directory
def save_uploaded_file(uploaded_file, directory):
    with open(os.path.join(directory, uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())

# Function to create a zip file of a directory
def create_zip(zip_name, directory):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)

# Streamlit UI
st.title("Contributor Page for Freedom Fighters")

# Input fields for user details
name = st.text_input("Your Name")
email = st.text_input("Your Email")

# File upload widgets
st.subheader("Upload Documents and Images about Freedom Fighters")
st.write("Please upload documents and images in .pdf,.jpg,.png or .zip format.")
f_name = st.text_input('Enter Name of Freedom Fighter')
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

if uploaded_files and f_name and email:
    # Create a directory to save uploaded files
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Save each uploaded file
    for uploaded_file in uploaded_files:
        save_uploaded_file(uploaded_file, upload_dir)
    
    st.success("Files successfully uploaded.")
    
    # Create a zip file of the uploaded files
    zip_name = "freedom_fighter_documents.zip"
    create_zip(zip_name, upload_dir)
    
    # Store contributor details in MongoDB
    contributor_data = {
        "name": name,
        "email": email,
        "files": [file.name for file in uploaded_files],
        'f_name': f_name
    }
    collection.insert_one(contributor_data)
    
    st.success("Contributor details successfully saved to MongoDB.")
    
    # Provide a download link for the zip file
    with open(zip_name, "rb") as zip_file:
        btn = st.download_button(
            label="Download Zip",
            data=zip_file,
            file_name=zip_name,
            mime="application/zip"
        )
