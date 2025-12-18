#  RAG Document Query System (PDF Q&A using LLMs)

A **Retrieval-Augmented Generation (RAG)** based application that allows users to upload PDF documents and ask natural language questions. The system retrieves the most relevant document chunks using embeddings and generates accurate answers using a Large Language Model.

This project was built as part of a **Junior AI/ML / GenAI Engineer interview assignment** focused on **document search and summarization using LLMs**.

---

##  Screenshots

![image 1](https://github.com/vinozzxx/Document-Search-and-Summarization-Using-RAG/blob/d230d6cf0b0ec753fb0da8cbd4c7070f3389cc98/image%201.png)

![image 2 ](https://github.com/vinozzxx/Document-Search-and-Summarization-Using-RAG/blob/d230d6cf0b0ec753fb0da8cbd4c7070f3389cc98/image%202%20.png)


---


##  Features

*  Upload PDF documents
*  Semantic search using vector embeddings
*  Context-aware answers using LLM
*  Retrieval-Augmented Generation (RAG) architecture
*  Simple and clean API-based backend

---

##  Project Architecture

**Flow:**

```
User Query
   ↓
Embed Query
   ↓
Vector Similarity Search
   ↓
Retrieve Relevant Chunks
   ↓
LLM (Answer Generation)
   ↓
Final Answer
```

---

##  Project File Structure

```
RAG_EVER_QUENT/
│
├── uploads/
│   └── STEPPER MOTOR USING DELTA PLC.pdf
│
├── __pycache__/
├── .venv/
│
├── app.py              # Main application entry point
├── rag.py              # RAG logic: embedding, retrieval, generation
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API keys)
├── .gitignore          # Git ignored files
└── README.md           # Project documentation
```

---

##  Core Components Explained

###  `app.py`

* Handles user interaction and API endpoints
* Accepts queries and PDF uploads
* Calls RAG pipeline for answer generation

###  `rag.py`

* Loads and chunks PDF documents
* Creates embeddings using LLM embeddings
* Performs similarity search
* Sends retrieved context to LLM

###  `uploads/`

* Stores uploaded PDF files
* Acts as the document corpus

---

##  Installation & Setup

### 1️ Clone the Repository

```bash
git clone https://github.com/your-username/rag-document-query.git
cd rag-document-query
```

### 2️ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️ Configure Environment Variables

Create a `.env` file:

```env
Groq_API_KEY=my_api_key_here
```

### 5️ Run the Application

```bash
python app.py
```

## Example Use Case

**Question:**

> What is the function of a stepper motor in Delta PLC?

**Answer:**

> A stepper motor in Delta PLC is used for precise position and speed control by converting electrical pulses into discrete mechanical movements.

---

## Evaluation (Optional Extension)

* Retrieval Accuracy: Semantic similarity matching
* Answer Quality: Context relevance and coherence
* Scalable to multiple PDFs and large documents

---

##  Tech Stack

* Python 
* LangChain / LLM APIs
* Vector Embeddings
* PDF Parsing
* Retrieval-Augmented Generation (RAG)

---

##  Future Improvements

* Web UI (Streamlit / React)
* Support for multiple documents
* Summary length control
* ROUGE-based evaluation
* Query auto-suggestions

---

##  Author

**VinothKumar**
GenAI / Data Science Enthusiast

