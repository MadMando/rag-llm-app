# RAG LLM App (Local & Multi-User)

A fully local, multi-user **Retrieval-Augmented Generation (RAG)** application powered by **Langflow**, **ChromaDB**, **Ollama**, and **FastAPI**. This project allows you to load documents, generate embeddings, store in a vector database, and query them using a local LLM — all served via an API for concurrent access.

---

## Features

- 🔍 **Document Search** with embeddings (PDF, TXT)
- 🧠 **Local LLM Inference** using [Ollama](https://ollama.com/)
- 🗃️ **ChromaDB** vector store for fast similarity search
- ⚡ **FastAPI Backend** with support for multiple users
- 🖼️ **Langflow UI** for building and testing LLM chains
- 🐳 **Dockerized** for easy deployment

---

## 🛠️ Tech Stack

| Layer            | Tool/Library         |
|------------------|----------------------|
| LLM              | [Ollama](https://ollama.com) (`llama3.2-1b`) |
| Vector DB        | [ChromaDB](https://www.trychroma.com/)     |
| Orchestration    | [Langflow](https://github.com/logspace-ai/langflow) |
| API Layer        | [FastAPI](https://fastapi.tiangolo.com/)   |
| Containerization | Docker               |
| Language         | Python 3.12          |

---

## 🗂️ Project Structure






