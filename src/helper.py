import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from src.prompt import *
import streamlit as st



# Load environment variables
load_dotenv()

def get_prompt(person_name):
    variable_name = f"{person_name.lower()}"
    print(variable_name)
    return globals().get(variable_name, None)


class ResponseLLM:
    def __init__(self, model=None, embeddings=None):
        # Initialize the model and embeddings, using defaults if none provided
        self.model = model or ChatGroq(temperature=0.7, model="llama3-70b-8192", api_key=os.environ['GORQ_API_KEY'])
        self.embeddings = embeddings or GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    def load_ebooks(self, ebooks):
        # Load documents from a directory of PDF files
        loader = PyPDFDirectoryLoader(ebooks)
        documents = loader.load()
        return documents

    def split_text(self, documents):
        # Split documents into smaller chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        split_text = text_splitter.split_documents(documents)
        return split_text

    def create_embeddings(self, split_text, persona_name):
        # Create embeddings for the text chunks and save them to a local FAISS index
        vector_store = FAISS.from_documents(split_text, embedding=self.embeddings)
        vector_store.save_local(f"data/{persona_name}/faiss_index_{persona_name}")
        return vector_store
    

    def response(self, user_question, persona_name):
        # Generate a response to the user's question
        prompt_template = get_prompt(persona_name)
        
        if not prompt_template:
            raise ValueError(f"No prompt found for {persona_name}")
        # Load the FAISS index based on the persona name
        new_db = FAISS.load_local(f"data/{persona_name}/faiss_index_{persona_name}", self.embeddings, allow_dangerous_deserialization=True)
        # Perform a similarity search with the user's question
        docs = new_db.similarity_search(user_question)
        # Create the prompt with context
        prompt = PromptTemplate(template=prompt_template, input_variables=["user_question", 'context'])
        print(prompt)
        # Chain the prompt with the model and output parser
        chain = prompt | self.model | StrOutputParser()
        # Generate the response
        response = chain.invoke({"context": docs, "user_question": user_question})
        return response

    def translate_output(self, response, language):
        prompt_template = '''translate following text english to {language} 
        convert text : {response}'''
        prompt = PromptTemplate(template=prompt_template, input_variables=["language",'response'])
        chain = prompt | self.model | StrOutputParser()
        translation= chain.invoke({"language": language, 'response':response})
        return translation