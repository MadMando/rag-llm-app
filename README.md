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

rag-llm-app/
├── app/
│ └── main.py # FastAPI app
├── data/ # Uploaded files or raw data
├── langflow/ # Langflow project files (optional)
├── Dockerfile # Build full stack container
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md


---

## ⚙️ Quickstart Guide (via Miniconda)

> Full instructions & setup scripts are available in the repository.  
> 👉 [github.com/yourusername/rag-llm-app](https://github.com/yourusername/rag-llm-app)

### 📥 1. Install Miniconda
If you don’t have Miniconda installed, download it from:  
🔗 https://docs.conda.io/en/latest/miniconda.html

### 🧪 2. Set Up the Environment
```bash
# Clone the repo
git clone https://github.com/yourusername/rag-llm-app.git
cd rag-llm-app

# Create and activate the conda environment
conda create -n rag-env python=3.12 -y
conda activate rag-env

# Install dependencies
pip install -r requirements.txt

# Start ChromaDB
chroma run --path ./data/chroma_data

# Start Langflow (optional)
langflow run

# Start FastAPI server
python app/main.py
