# 📄 RAG Document Query System (PDF Q&A using LLMs)

A **Retrieval-Augmented Generation (RAG)** based application that allows users to upload PDF documents and ask natural language questions. The system retrieves the most relevant document chunks using embeddings and generates accurate answers using a Large Language Model.

This project was built as part of a **Junior AI/ML / GenAI Engineer interview assignment** focused on **document search and summarization using LLMs**.

---

## 🚀 Features

* 📂 Upload PDF documents
* 🔍 Semantic search using vector embeddings
* 🤖 Context-aware answers using LLM
* 🧠 Retrieval-Augmented Generation (RAG) architecture
* 🖥️ Simple and clean API-based backend

---

## 🏗️ Project Architecture

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

## 📁 Project File Structure

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

## 🧠 Core Components Explained

### 🔹 `app.py`

* Handles user interaction and API endpoints
* Accepts queries and PDF uploads
* Calls RAG pipeline for answer generation

### 🔹 `rag.py`

* Loads and chunks PDF documents
* Creates embeddings using LLM embeddings
* Performs similarity search
* Sends retrieved context to LLM

### 🔹 `uploads/`

* Stores uploaded PDF files
* Acts as the document corpus

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rag-document-query.git
cd rag-document-query
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

### 5️⃣ Run the Application

```bash
python app.py
```

---

## 🖼️ Application Screenshot

> Below is the current project structure as seen in VS Code:

![Project Structure Screenshot](Screenshot_2025-12-18_145557.png)

---

## 🧪 Example Use Case

**Question:**

> What is the function of a stepper motor in Delta PLC?

**Answer:**

> A stepper motor in Delta PLC is used for precise position and speed control by converting electrical pulses into discrete mechanical movements.

---

## 📊 Evaluation (Optional Extension)

* Retrieval Accuracy: Semantic similarity matching
* Answer Quality: Context relevance and coherence
* Scalable to multiple PDFs and large documents

---

## 🛠️ Tech Stack

* Python 🐍
* LangChain / LLM APIs
* Vector Embeddings
* PDF Parsing
* Retrieval-Augmented Generation (RAG)

---

## 🎯 Future Improvements

* Web UI (Streamlit / React)
* Support for multiple documents
* Summary length control
* ROUGE-based evaluation
* Query auto-suggestions

---

## 👤 Author

**Vinod Kumar**
GenAI / Data Science Enthusiast
📍 India

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork and improve it!
