import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.analytics_tool import analyze_sales_data


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")
)


agent = create_agent(
    model=llm,
    tools=[analyze_sales_data],
    system_prompt="""
    You are an AI Data Analyst.

    Use the analyze_sales_data tool
    whenever the user asks about sales.

    Answer clearly and briefly.
    Never invent data.
    """
)