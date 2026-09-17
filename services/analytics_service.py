import matplotlib
matplotlib.use("Agg")

import pandas as pd


def analyze_data(question: str, data, analysis_code: str):

    df = pd.DataFrame(data)

    local_vars = {
        "df": df,
        "pd": pd,
        "question": question,
    }

    exec(
        analysis_code,
        {"__builtins__": __builtins__},
        local_vars
    )

    result = local_vars["result"]

    if hasattr(result, "to_dict"):
        return {
            "type": "chart",
            "chart": result.to_dict()
        }

    return result


# TEST
# question = "Show me the total sales"
# sheet_url = "https://docs.google.com/spreadsheets/d/1rQvWqFS5ne40LluFPNMpuh3iy7DGtoKPwN9NOSFtSfA/edit?usp=sharing"

# result = analyze_data(question, sheet_url)

# print(result)