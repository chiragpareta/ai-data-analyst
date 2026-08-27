import gspread

from google.oauth2.service_account import Credentials
from langchain.tools import tool


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(credentials)

sheet = client.open("ai_analyst").sheet1


@tool
def analyze_sales_data(question: str) -> str:
    """
    Analyze the sales data from Google Sheets based on the user's question.
    Use this tool for sales calculations, filtering, comparisons,
    aggregations, trends, and other analytics.
    """

    data = sheet.get_all_records()

    # For our first version, return the data + question.
    # Gemini will perform the reasoning.
    return f"""
    User's analytics question:
    {question}

    Sales data:
    {data}
    """