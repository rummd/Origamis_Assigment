import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
import google.generativeai as genai

FILE_PATH = "faiss_index"  # Change to a directory or filename without .pkl

APIKEY = "AIzaSyBasYdrvaYNGk9IQpjFof-lx6xv_szUVyE"
print(f"API Key = {APIKEY}")
genai.configure(api_key=APIKEY)

def index_documents(docs):
    """Indexes scraped documents into FAISS and saves the index."""
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=500
    )
    chunks = text_splitter.split_text(docs)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=APIKEY)
    vectorstore = FAISS.from_texts(chunks, embeddings)

    # Save the FAISS index to disk
    vectorstore.save_local(FILE_PATH)

    return "Documents successfully indexed! ✅"

def load_vectorstore():
    """Loads the FAISS index from disk."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=APIKEY)
    vectorstore = FAISS.load_local(FILE_PATH, embeddings)
    return vectorstore