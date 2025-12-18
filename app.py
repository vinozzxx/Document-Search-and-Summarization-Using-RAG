import streamlit as st
import os
from rag import build_rag_from_files

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="Groq RAG System", layout="wide")
st.title("Upload Documents & Query Them ")

uploaded_files = st.file_uploader(
    "Upload PDF documents",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    file_paths = []

    for file in uploaded_files:
        file_path = os.path.join(UPLOAD_DIR, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        file_paths.append(file_path)

    st.success("Documents uploaded successfully.")

    with st.spinner("Building knowledge base..."):
        # Unpack the tuple - chain and retriever
        qa_chain, retriever = build_rag_from_files(file_paths)

    st.success("RAG system is ready.")

    query = st.text_input("Enter your query")
    summary_length = ("Summary Length (words)", 300)

    if st.button("Search"):
        if query.strip():
            with st.spinner("Generating response..."):
                # Invoke the chain with the query
                answer = qa_chain.invoke(query)
                
                # Get source documents
                source_docs = retriever.invoke(query)

                #Generate summary using the chain
                summary_prompt = f"""Summarize the following content in approximately {summary_length} words:

{answer}

Summary:"""
                summary = qa_chain.invoke(summary_prompt)

            st.subheader("🔍 Answer")
            st.write(answer)

            st.subheader("📝 Summary")
            st.write(summary)

            st.subheader("📚 Source Chunks")
            for i, doc in enumerate(source_docs, 1):
                with st.expander(f"Source {i}"):
                    st.write(doc.page_content)
        else:
            st.warning("Please enter a query.")


# Custom CSS for background
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/8294598/pexels-photo-8294598.jpeg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
