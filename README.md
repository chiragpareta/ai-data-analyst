# AI Data Analyst

An AI-powered data analyst that lets users connect their Google Sheet and ask questions about their data using natural language.

## Features

- Connect Google Sheet using its URL
- Natural-language data analysis
- Gemini LLM
- LangChain Agent & Tool Calling
- Pandas for data analysis
- FastAPI backend
- React frontend

## Tech Stack

**Frontend:** React, JavaScript, Vite  
**Backend:** Python, FastAPI  
**AI:** Gemini, LangChain  
**Data:** Google Sheets, Pandas

## Architecture

```text
React
  ↓
FastAPI
  ↓
LangChain Agent
  ↓
Gemini
  ↓
Analytics Tool
  ↓
Google Sheets
  ↓
Pandas
  ↓
Analysis Result
  ↓
Gemini
  ↓
Final Answer
```

## Setup

### Backend

Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
GEMINI_API_KEY=your_api_key
```

Add your Google service-account file:

```text
credentials.json
```

Share your Google Sheet with the service-account email.

Run the backend:

```bash
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

## Docker Setup

Make sure Docker Desktop is installed and running.

Create `.env` in the project root:

```env
GEMINI_API_KEY=your_api_key
```

Add your Google service-account file in the project root:

```text
credentials.json
```

Run both backend and frontend:

```bash
docker compose up --build
```

Open the app:

```text
http://localhost:3000
```

Backend API:

```text
http://localhost:8000
```

Stop containers:

```bash
docker compose down
```

### Docker Files

```text
Dockerfile                  FastAPI backend image
frontend/Dockerfile         React build + Nginx frontend image
frontend/nginx.conf         Sends /ask requests to the backend container
docker-compose.yml          Runs backend and frontend together
.dockerignore               Keeps secrets and local files out of Docker images
.env.example                Shows required environment variables
```

Secrets are not copied into Docker images. `GEMINI_API_KEY` is loaded from `.env`, and `credentials.json` is mounted into the backend container.

## Usage

1. Open the React application.
2. Enter your Google Sheet URL.
3. Ask a question about your data.
4. Click **Ask AI**.
5. The agent analyzes the data and returns the answer.

Example:

```text
Which product has the highest sales?
```

## Security

Never commit these files to GitHub:

```text
.env
credentials.json
```

Add them to `.gitignore`.

## Project Structure

```text
ai_data_analyst/
├── main.py
├── agent.py
├── tools/
├── services/
├── frontend/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Status

Working prototype.

Future improvements:

- Cloud deployment
- Google OAuth
- Data visualization
- Support for different data schemas
