# RAG-based Question Answering using Endee

## 📌 Project Overview
This project implements a **Retrieval-Augmented Generation (RAG)** style Question Answering system using **Endee** as a vector database.

The system allows users to:
- Ingest documents into a vector store
- Ask natural language questions
- Retrieve the most relevant content using semantic search

Endee is used to store and query vector embeddings efficiently, making it suitable for semantic search and RAG-based applications.

---

## 🧠 How It Works
1. Documents are loaded and converted into vector embeddings
2. Embeddings are stored in Endee’s vector database
3. User queries are embedded
4. Endee retrieves the most relevant documents based on similarity
5. Retrieved content is returned as an answer

---

## 🛠️ Tech Stack
- Python
- Endee (Vector Database)
- Sentence Transformers
- Torch

---

## 📂 Project Structure
rag-question-answering/
│
├── ingest.py          # Loads documents and stores embeddings in Endee
├── query.py           # Accepts user questions and retrieves relevant content
├── data/              # Sample documents for ingestion
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
