
# 🧠 RAG LLM App (Local & Multi-User)

A fully local, multi-user **Retrieval-Augmented Generation (RAG)** application powered by **Langflow**, **ChromaDB**, **Ollama**, and **FastAPI**. This project allows you to load documents, generate embeddings, store in a vector database, and query them using a local LLM — all served via an API for concurrent access.

## 🚀 Features

- 🔍 Search across your own documents (`.pdf`, `.txt`)
- 🧠 Local LLM inference with quantized models (via Ollama)
- 🗃️ Vector storage and retrieval using ChromaDB
- ⚡ FastAPI backend with multi-user support
- 🖼️ Langflow UI for no-code visual pipelines

## 🛠️ Tech Stack

| Layer         | Tool               |
|---------------|--------------------|
| LLM           | Ollama (`llama3`)  |
| Embeddings    | Ollama (`nomic-embed-text`) |
| Vector DB     | ChromaDB           |
| Orchestration | Langflow           |
| API Server    | FastAPI            |
| Environment   | Python 3.12 (Miniconda) |

## 🗂️ Project Structure

```
rag-llm-app/
├── app/
│   └── main.py          # FastAPI app
├── data/                # Drop .pdf or .txt documents here
├── langflow/            # Langflow project files (optional)
├── requirements.txt     # Python dependencies (except langflow/uv)
├── .gitignore
└── README.md
```

## ⚙️ Quickstart Guide (via Miniconda)

> Full setup instructions and Langflow flows are available in the repo:  
> 👉 [https://github.com/MadMando/rag-llm-app](https://github.com/MadMando/rag-llm-app)

### 1️⃣ Install Miniconda

Download Miniconda from:  
🔗 https://docs.conda.io/en/latest/miniconda.html

### 2️⃣ Install Ollama and Pull Models

Download Ollama for your OS:  
🔗 https://ollama.com/download

Then open a terminal or command prompt and run:

```bash
ollama pull llama3             # LLM model
ollama pull nomic-embed-text   # Embedding model
```

Make sure Ollama is running after installation.

### 3️⃣ Set Up the Project Environment

```bash
# Clone the repo
git clone https://github.com/MadMando/rag-llm-app.git
cd rag-llm-app

# Create and activate your conda environment
conda create -n rag-env python=3.12 -y
conda activate rag-env

# Install uv and langflow
pip install uv
uv pip install langflow

# Install all other dependencies
uv pip install -r requirements.txt
```

### 4️⃣ Start the RAG Stack

```bash
# Start ChromaDB
chroma run --path ./data/chroma_data

# Start Langflow
langflow run
```

Langflow will open at:  
👉 http://localhost:7860

### 5️⃣ (Optional) Run FastAPI App

```bash
uvicorn app.main:app --reload
```

Visit the docs:  
👉 http://localhost:8000/docs

### 📂 Document Ingestion

Drop your `.pdf` and `.txt` files into the `data/` folder.  
Langflow will use them during your flow execution with ChromaDB.

## ✅ Status

- ✅ Local LLMs via Ollama  
- ✅ Langflow integration  
- ✅ Multi-user query support via FastAPI  
- ⏳ Next: Add UI chat interface + advanced chunking logic

## 📄 License

MIT License

## ✍️ Author

Built by [Armando Medina](https://www.linkedin.com/in/armandomedina)  
Follow for more projects on GenAI, RAG, and LLM applications.
