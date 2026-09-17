import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import TOOLS
from services.google_sheet import get_sheet_data

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

model_with_tools = model.bind_tools(TOOLS)


def ask_agent(question: str, sheet_url: str):

    data = get_sheet_data(sheet_url)
    columns = list(data[0].keys()) if data else []

    prompt = f"""
You are an AI Data Analyst.

Available columns:
{columns}

User question:
{question}

Use the analysis tool.

The Google Sheet has ALREADY been loaded into a Pandas DataFrame named `df`.

Generate Python/Pandas code dynamically and assign the final output to `result`.

Rules:
- Use `df` for ALL analysis.
- NEVER use pd.read_csv().
- NEVER use pd.read_excel().
- NEVER download or read the Google Sheet yourself.
- NEVER use sheet_url to load data.
- Use ONLY the columns listed in Available columns.
- Do not invent column names.
- Do not assume fixed business logic.
- For charts, create the chart from `df` and assign it to `result`.
"""

    response = model_with_tools.invoke(prompt)

    if response.tool_calls:

        tool_call = response.tool_calls[0]

        args = tool_call["args"]

        result = TOOLS[0].invoke({
            "question": question,
            "data": data,
            "analysis_code": args["analysis_code"]
        })

        # Vega-Lite chart
        if isinstance(result, dict) and result.get("type") == "chart":
            return result

        # Old image-based chart
        if isinstance(result, dict) and "image_base64" in result:
            return {
                "type": "chart",
                "image_base64": result["image_base64"]
            }

        # Normal analysis result
        return {
            "type": "text",
            "result": result
        }

    # Normal Gemini text response
    content = response.content

    if isinstance(content, list):
        text_parts = [
            item.get("text", "")
            for item in content
            if isinstance(item, dict) and item.get("type") == "text"
        ]

        content = "\n".join(
            part for part in text_parts if part
        )

    return {
        "type": "text",
        "result": content
    }


# TEST
# if __name__ == "__main__":

#     sheet_url = "https://docs.google.com/spreadsheets/d/1rQvWqFS5ne40LluFPNMpuh3iy7DGtoKPwN9NOSFtSfA/edit?usp=sharing"

#     answer = ask_agent(
#         "Create a bar chart showing total sales for each product.",
#         sheet_url
#     )

#     print(answer)