from langchain.tools import tool

from services.analytics_service import analyze_sales


@tool
def analyze_sales_data(question: str, sheet_url: str) -> dict:
    """
    Analyze sales data from the user's Google Sheet
    based on their question.
    """

    return analyze_sales(question, sheet_url)