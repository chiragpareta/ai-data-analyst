from langchain_core.tools import tool

from services.analytics_service import analyze_data


@tool
def run_python_analysis(
    question: str,
    data: list,
    analysis_code: str
):
    """
    Run dynamically generated Python/Pandas code on loaded data.
    """

    return analyze_data(
        question=question,
        data=data,
        analysis_code=analysis_code
    )