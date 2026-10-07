import sys
from dotenv import load_dotenv
from turtle import goto
from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_anthropic import ChatAnthropic

app = FastAPI()
load_dotenv()

DOCS = [
    "BEON.tech mission is to place the brightest tech talent in the mostdisruptive and innovative U.S. companies.",
    "BEON.tech offer IT staff augmentation services for every modern tech need,from backend and frontend to AI, machine learning, DevOps and QA.",
    "At BEON.tech, building software means far more than just filling roles — it'sabout creating strong relationships, empowering careers and helping peoplegrow."
]

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
vectorstore = InMemoryVectorStore.from_texts(DOCS, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

@tool
def search_docs(query: str) -> str:
    """Search the BEON.tech docs for the answer to the question."""
    print(f"Searching for {query}")
    docs = retriever.invoke(query)
    if not docs:
        return "No documents found"
    return docs

system_prompt = """
You are a helpful assistant that can search the BEON.tech docs for the answer to the question.
just answer the question with the information from the docs, do not make up any information.
"""

model = ChatAnthropic(model="claude-haiku-4-5")
agent = create_agent(
    model, 
    tools=[search_docs],
    system_prompt=system_prompt,
    )


class ChatResponse(BaseModel):
    message: str

class ChatRequest(BaseModel):
    message: str

@app.post("/chat" , response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    result = agent.invoke({"messages":[{"role": "user", "content": request.message}]})
    reply = result["messages"][-1].text
    return ChatResponse(message=reply)