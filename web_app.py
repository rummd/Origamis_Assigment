import streamlit as st
from src.agent import agent

st.title("AI-Powered Research Tool 📈")
st.sidebar.title("Enter URLs")

urls = []
for i in range(1):
    url = st.sidebar.text_input(f"URL {i+1}")
    if url:
        urls.append(url)

# Scrape and index articles
if st.sidebar.button("Process URLs"):
    for url in urls:
        # scraped_text = agent.run("Scrape Website", url)
        scraped_text = agent.invoke({"input": f"Scrape Website: {url}"})
        input_data = {"input": {"task": "Index Documents", "text": scraped_text}}
        indexing_status = agent.run(input_data)
        st.write(indexing_status)

# Query input for RAG pipeline
query = st.text_input("Ask a question:")
if query:
    #web_app.py line 25
    input_data = {"input": query, "task": "Retrieve Answer"} 
    result = agent.invoke(input_data)
    # print(result)
    answer = result["output"] 
    sources = "Sources not implemented in this example" 
    # answer, sources = agent.run("Retrieve Answer", query)

    st.header("Answer")
    st.write(answer)

    if sources:
        st.subheader("Sources:")
        st.write(sources)