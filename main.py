import os
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import ask_agent


app = FastAPI()


cors_origins = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000,http://127.0.0.1:3000",
).split(",")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in cors_origins if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    sheet_url: str
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Data Analyst is running"
    }


@app.post("/ask")
def ask(question: Question):

    result = ask_agent(
        question=question.question,
        sheet_url=question.sheet_url
    )

    return jsonable_encoder(result, custom_encoder={
    __import__("numpy").integer: int,
    __import__("numpy").floating: float,
})