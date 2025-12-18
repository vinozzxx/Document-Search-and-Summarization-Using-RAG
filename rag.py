import os
from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq




def RAG_system(file_paths):
    # Load documents
    documents = []
    for path in file_paths:
        loader = PyPDFLoader(path)
        documents.extend(loader.load())

    # Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create vector store
    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    # Initialize Groq LLM
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.2
    )

    # Create prompt template
    prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context:

{context}

Question: {question}

Answer:""")

    # Format documents function
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Create RAG chain using LCEL (LangChain Expression Language)
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain, retriever


# Example usage:
if __name__ == "__main__":
    # Build the RAG system
    chain, retriever = RAG_system(["your_document.pdf"])
    
    # Ask a question
    question = "What is this document about?"
    answer = chain.invoke(question)
    
    # Print the answer
    print("Answer:", answer)
    
    # Get source documents (optional)
    source_docs = retriever.invoke(question)
    print("\nSource documents used:")
    for i, doc in enumerate(source_docs, 1):
        print(f"\n{i}. {doc.page_content[:200]}...")