from services.google_sheet import get_sheet_data


def analyze_sales(question: str):
    data = get_sheet_data()

    return {
        "question": question,
        "data": data
    }