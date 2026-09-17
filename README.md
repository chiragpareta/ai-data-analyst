# AI Data Analyst

AI-powered application for analyzing Google Sheets using natural language.

The application uses Gemini, LangChain, Pandas, FastAPI, and React to analyze data and generate text answers or charts.

## Tech Stack

**Backend:** Python, FastAPI, LangChain, Gemini, Pandas, gspread

**Frontend:** React 

## Project Structure

```text
ai_data_analyst/
├── main.py
├── agent.py
├── services/
│   ├── analytics_service.py
│   └── google_sheet.py
├── tools/
│   └── analytics_tool.py
├── frontend/
├── requirements.txt
├── .env
├── credentials.json
└── README.md
```

## Setup

### 1. Clone

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ai_data_analyst
```

### 2. Backend

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Add your Google service account file as:

```text
credentials.json
```

The service account must have access to the Google Sheet.

### 3. Start Backend

```bash
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

### 4. Start Frontend

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

## Usage

1. Open the frontend.
2. Enter a Google Sheet URL.
3. Enter a natural-language question.
4. Click **Ask AI**.

Example:

```text
Create a bar chart showing total sales for each product.
```

## Security

Do not commit sensitive files.

Add to `.gitignore`:

```gitignore
.env
credentials.json
venv/
__pycache__/
node_modules/
```

## Current Scope

- Google Sheets
- Dynamic Pandas analysis
- Natural-language questions
- Text answers
- Chart generation