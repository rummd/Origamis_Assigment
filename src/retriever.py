import os
import pickle
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
# from langchain import OpenAI # Removed
from langchain_google_genai import GoogleGenerativeAI  # Added
APIKEY = ""
FILE_PATH = "faiss_store.pkl"
# llm = OpenAI(temperature=0.7, max_tokens=500) # Removed
llm = GoogleGenerativeAI(model="models/gemini-2.0-flash-lite", google_api_key=APIKEY)  # Added

def retrieve_answer(query):
    """Retrieves an answer from indexed documents based on the query."""
    if not os.path.exists(FILE_PATH):
        return "No data indexed yet! Please scrape website first."

    with open(FILE_PATH, "rb") as f:
        vectorstore = pickle.load(f)

    retriever = vectorstore.as_retriever()
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=retriever)
    result = chain({"question": query}, return_only_outputs=True)

    return result["answer"], result.get("sources", "")