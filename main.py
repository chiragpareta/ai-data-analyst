import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import agent


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    sheet_url: str
    question: str


def format_answer(content):
    if isinstance(content, str):
        return content

    return json.dumps(content, indent=2)


@app.get("/")
def home():
    return {
        "message": "AI Data Analyst is running"
    }


@app.post("/ask")
def ask(question: Question):

    prompt = f"""
    Google Sheet URL:
    {question.sheet_url}

    User question:
    {question.question}
    """

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })

    return {
        "answer": format_answer(result["messages"][-1].content)
    }
