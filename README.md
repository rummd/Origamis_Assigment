# Origamis_Assigment

# AI-Powered Research Tool

## Overview

This project is a web-based AI-powered research tool that allows users to:

1. **Scrape** text from web pages
2. **Index** the scraped content into a FAISS vector database
3. **Retrieve** relevant answers using a Retrieval-Augmented Generation (RAG) pipeline powered by Google's Gemini model
4. **Query the system** via a Streamlit web interface

## Installation

To set up the project locally, follow these steps:

### **1. Clone the Repository**

```sh
 git clone https://github.com/your-username/your-repo-name.git
 cd your-repo-name
```

### **2. Create a Virtual Environment (Optional but Recommended)**

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**

```sh
pip install -r requirements.txt
```

## Running the Pipeline

### **1. Running the Scraper**

The scraper extracts text from a given URL.

```python
from src.scraper import scrape_website
scraped_text = scrape_website("https://example.com")
print(scraped_text)
```

### **2. Indexing the Data**

The indexer tokenizes and embeds the scraped text into FAISS for efficient retrieval.

```python
from src.indexer import index_documents
index_documents(scraped_text)
```

### **3. Querying the RAG Pipeline**

Retrieve answers using the indexed knowledge.

```python
from src.retriever import retrieve_answer
response = retrieve_answer("What is the article about?")
print(response)
```

## Running the Streamlit Web App

Launch the Streamlit app to use the AI-powered tool through a user-friendly interface.

```sh
streamlit run web_app.py
```

## **Example Usage**

1. Enter a **URL** in the Streamlit app.
2. Click **Process URLs** to scrape and index the content.
3. Type a **query** in the search box and get relevant answers from the indexed data.

## **License**

This project is open-source and available under the MIT License.

