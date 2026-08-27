from fastapi import FastAPI
from pydantic import BaseModel

from agent import agent


app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Data Analyst is running"
    }


@app.post("/ask")
def ask(question: Question):

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question.question
            }
        ]
    })

    return {
        "answer": result["messages"][-1].content
    }