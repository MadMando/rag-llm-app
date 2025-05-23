# 🧠 RAG LLM (Local)

A fully local **Retrieval-Augmented Generation (RAG)** application powered by **Langflow**, **ChromaDB**, and **Ollama**. This project allows you to load documents, generate embeddings, store them in a vector database, and query them using a local LLM — all within a visually interactive pipeline.

## 🚀 Features

- 🔍 Search across your own documents (`.pdf`, `.txt`)
- 🧠 Local LLM inference with quantized models (via Ollama)
- 🗃️ Vector storage and retrieval using ChromaDB
- 🖼️ Langflow UI for no-code visual pipelines

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Langflow-Orchestration-purple" alt="Langflow Badge"/>
  <img src="https://img.shields.io/badge/Ollama-LLM-green" alt="Ollama Badge"/>
  <img src="https://img.shields.io/badge/ChromaDB-VectorDB-orange" alt="ChromaDB Badge"/>
</p>

## 🛠️ Tech Stack

| Layer         | Tool               |
|---------------|--------------------|
| LLM           | Ollama (`llama3.2:1b`)  |
| Embeddings    | Ollama (`nomic-embed-text`) |
| Vector DB     | ChromaDB           |
| Orchestration | Langflow           |
| Environment   | Python 3.12 (Miniconda) |

## 🗂️ Project Structure

```
rag-llm-app/
├── data/                # Drop .pdf or .txt documents here
├── langflow/            # Langflow project files (optional)
├── requirements.txt     # Python dependencies (except langflow/uv)
├── Index.html           # Sample HTML index file with chat widget
├── .gitignore
└── README.md
```

## ⚙️ Quickstart Guide (via Miniconda)

### 1️⃣ Install Miniconda

Download Miniconda from:  
🔗 https://docs.conda.io/en/latest/miniconda.html

### 2️⃣ Install Ollama and Pull Models

Download and install Ollama for your OS:  
🔗 https://ollama.com/download

Then open a terminal or command prompt and run:

```bash
ollama pull llama3.2:1b             # LLM model
ollama pull nomic-embed-text   # Embedding model
```
You can explore other LLM models on the Ollama website—I chose the 1B model for its lightweight footprint and strong generalization capabilities.
Make sure Ollama is running after installation.

### 3️⃣ Set Up the Project Environment

```bash
# Clone the repo
git clone https://github.com/MadMando/rag-llm-app.git
cd rag-llm-app

# Create and activate your conda environment
conda create -n rag-env python=3.12 -y
conda activate rag-env

# Install uv - makes things easier!
pip install uv

# Install all other dependencies
uv pip install -r requirements.txt
```

### 4️⃣ Start the RAG Stack

```bash
# Start ChromaDB
chroma run --path ./data/chroma_data

# open a new cmd prompt, navigate to rag-llm-app folder and activate env again
cd rag-llm-app
conda activate rag-env

# Start Langflow using uv
uv run langflow run
```

Langflow will open at:  
👉 http://localhost:7860

### 🖼️ Example Langflow Diagram
Here's what a complete working flow looks like in Langflow:

![Langflow Example Setup](./img/langlfow_workflow_example.png)

### 📂 Document Ingestion

Drop your `.pdf` and `.txt` files into the `data/` folder.  
Langflow will use them during your flow execution with ChromaDB.

## 🧩 Langflow Project Setup (Step-by-Step)

### 📁 Step 1: Directory Tool
- Drag the **Directory** tool to the canvas.
- Configure it to point to the `data/` directory.

### ✂️ Step 2: Text Splitting
- Drag in a **Text Splitter** tool.
- Set `chunk size` to `500` and `chunk overlap` to `100`. This seems to work well for me.
- Connect the Directory output (Data) to the TextSplitter input (Data or Dataframe).

### 🧠 Step 3: Embeddings
- Drag in the **Ollama Embeddings** tool.
- Choose `nomic-embed-text` as the model.

### 📦 Step 4: Chroma Vector Store
- Drag in the **Chroma Vector Store** tool.
- Set the `Collection Name` to `CFR-1` (or your choice).
- Set the `Persist Directory` to the `data/` folder.
- Connect Chunks from the TextSplitter to Ingest Data in ChromaDB, and Embeddings to Embeddings.

### ▶️ Run the workflow by pressing the Play button next to the ChromaDB tool.
- This will create your embeddings and load them into the vector store.

### 💬 Chat-Ready Flow Setup

### 🧾 Step 5: Chat Input
- Drag in the **Chat Input** tool.
- Connect it to the **Search Query** input on **Chroma DB**.

### 🔍 Step 6: Chroma DB Search
- Already configured with collection name `CFR-1` and data path.
- It returns document chunks relevant to the query.

### 🧹 Step 7: Parser
- Add the **Parser** tool.
- Set it to `text({text})` mode to turn Chroma results into a usable string.
- Connect **Chroma DB → Parser**.

### 🧾 Step 8: Prompt Template
- Drag in a **Prompt** tool.
- Example template:
  ```
  You are an analyst. Your job is to review provided context and answer questions based on federal, state, or industry-specific compliance rules.

  Context: {context}
  Question: {question}
  ```
- You will need to adjust this to be specific to what you want your output to look like,  take your time creating the prompt message. 

### 🤖 Step 9: Ollama (LLM)
- Add the **Ollama** tool.
- Model: `llama3.2-1b`
- Connect **Prompt → Ollama** input.
  
⚠️ **Important Note for Langflow v1.4.1 Users:**
If you're running **Langflow version 1.4.1**, there's a known issue where the **model list does not populate** properly inside the Ollama component.

To work around this bug:
1. Click the **`</>` (Code)** icon on the Ollama tool.
2. Go to **line 289** and remove the word `await` from `await tags_response.json()` — make it just `tags_response.json()`.
3. Do the same for **line 301**: remove `await` from `show_response.json()`.

These changes bypass the async misuse and restore model visibility in the dropdown.
> This issue is expected to be fixed in a future version of Langflow.

### 💬 Step 10: Chat Output
- Add **Chat Output**.
- Connect **Ollama → Chat Output**.

### 🔗 Connections Overview
- Chat Input **Message** → ChromaDB **Search Query**
- Ollama Embeddings **Embeddings** → ChromaDB **Embeddings**
- ChromaDB **DataFrame** → Parser **Data or DataFrame**
- Parser **Parsed Text** → Prompt **context**
- Chat Input **Message** → Prompt **question**
- Prompt **Prompt Message** → Ollama **Input**
- Ollama **Message** → Chat Output **Text**

### ▶️ Click on Playground (upper right) to test your chat
Ask it specific questions based on your PDFs or text. For more accurate responses, set temperature to `0.1`. For more creative answers, increase it.

## 🌐 Sample Web Chat
You can embed the chat interface on a custom webpage using the `<langflow-chat>` component. See example `index.html` in this repo.
Remember to add your langflow flow id located on the address bar 
![Langflow flow id](./img/lanflow_id.png)

![Langflow Chat Demo](./img/ChatWidget.gif)

## ✅ Status

- ✅ Local LLMs via Ollama  
- ✅ Langflow integration  
- ✅ In-browser chat widget
- ⏳ Next: Shareable hosted demo + Langflow project exports

## 📄 License

MIT License

## ✍️ Author

Built by [Armando Medina](https://www.linkedin.com/in/armandomedina)  
Follow for more projects on GenAI, RAG, and LLM applications.

**Created with the help of local llm using langflow and ollama**
