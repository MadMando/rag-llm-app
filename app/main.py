# app/main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/rag")
async def run_rag(request: QueryRequest):
    # Dummy logic for now
    return {"response": f"You asked: '{request.query}'. This is a placeholder response."}

@app.get("/")
def root():
    return {"status": "RAG API is running"}
