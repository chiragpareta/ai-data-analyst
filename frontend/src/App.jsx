import React, { useState } from "react";

const API_URL = "/ask";

function formatMessage(value) {
  if (!value) {
    return "";
  }

  if (typeof value === "string") {
    return value;
  }

  return JSON.stringify(value, null, 2);
}

async function readResponse(response) {
  const contentType = response.headers.get("content-type") || "";

  if (contentType.includes("application/json")) {
    return response.json();
  }

  return {
    detail: await response.text(),
  };
}

function App() {
  const [sheetUrl, setSheetUrl] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();
    setAnswer("");
    setError("");
    setLoading(true);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          sheet_url: sheetUrl,
          question,
        }),
      });

      const data = await readResponse(response);

      if (!response.ok) {
        throw new Error(formatMessage(data.detail) || "Something went wrong.");
      }

      setAnswer(formatMessage(data.answer) || "No answer returned.");
    } catch (err) {
      setError(err.message || "Unable to contact the backend.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page">
      <section className="app-shell" aria-labelledby="app-title">
        <h1 id="app-title">AI Data Analyst</h1>

        <form onSubmit={handleSubmit} className="form">
          <label htmlFor="sheet-url">Google Sheet URL</label>
          <input
            id="sheet-url"
            type="url"
            value={sheetUrl}
            onChange={(event) => setSheetUrl(event.target.value)}
            placeholder="https://docs.google.com/spreadsheets/d/..."
            required
          />

          <label htmlFor="question">Ask your question</label>
          <textarea
            id="question"
            value={question}
            onChange={(event) => setQuestion(event.target.value)}
            placeholder="Which product has the highest sales?"
            rows="4"
            required
          />

          <button type="submit" disabled={loading}>
            {loading ? "Asking AI..." : "Ask AI"}
          </button>
        </form>

        {error && (
          <div className="message error" role="alert">
            {error}
          </div>
        )}

        {answer && (
          <div className="message answer">
            <h2>Answer</h2>
            <pre>{answer}</pre>
          </div>
        )}
      </section>
    </main>
  );
}

export default App;
