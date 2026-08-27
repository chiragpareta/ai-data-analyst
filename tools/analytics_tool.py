from langchain.tools import tool

from services.analytics_service import analyze_sales


@tool
def analyze_sales_data(question: str) -> dict:
    """
    Analyze sales data based on the user's question.
    Use this for sales calculations, comparisons,
    trends, filtering, and other sales analytics.
    """

    return analyze_sales(question)