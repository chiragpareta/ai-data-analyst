import React, { useEffect, useRef, useState } from "react";
import embed from "vega-embed";

const API_URL = "/ask";

function App() {
  const [sheetUrl, setSheetUrl] = useState("");
  const [question, setQuestion] = useState("");

  const [answer, setAnswer] = useState("");
  const [chart, setChart] = useState(null);
  const [image, setImage] = useState(null);

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const chartRef = useRef(null);

  useEffect(() => {
    if (!chart || !chartRef.current) {
      return;
    }

    chartRef.current.innerHTML = "";

    embed(chartRef.current, chart, {
      actions: false,
    }).catch((err) => {
      setError(`Chart rendering failed: ${err.message}`);
    });
  }, [chart]);

  async function handleSubmit(event) {
    event.preventDefault();

    setAnswer("");
    setChart(null);
    setImage(null);
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
          question: question,
        }),
      });

      const text = await response.text();

      let data;

      try {
        data = JSON.parse(text);
      } catch {
        throw new Error(text || "Backend returned an invalid response.");
      }

      if (!response.ok) {
        throw new Error(
          data.detail || "Something went wrong."
        );
      }

      // Vega-Lite chart
      if (data.type === "chart" && data.chart) {
        setChart(data.chart);
        return;
      }

      // Base64 PNG chart
      if (data.type === "chart" && data.image_base64) {
        setImage(data.image_base64);
        return;
      }

      // Text answer
      if (data.type === "text") {
        setAnswer(
          typeof data.result === "string"
            ? data.result
            : JSON.stringify(data.result, null, 2)
        );
        return;
      }

      setAnswer(JSON.stringify(data, null, 2));

    } catch (err) {
      setError(
        err.message || "Unable to contact the backend."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page">
      <section className="app-shell">

        <h1>AI Data Analyst</h1>

        <form onSubmit={handleSubmit} className="form">

          <label htmlFor="sheet-url">
            Google Sheet URL
          </label>

          <input
            id="sheet-url"
            type="url"
            value={sheetUrl}
            onChange={(event) =>
              setSheetUrl(event.target.value)
            }
            placeholder="https://docs.google.com/spreadsheets/d/..."
            required
          />

          <label htmlFor="question">
            Ask your question
          </label>

          <textarea
            id="question"
            value={question}
            onChange={(event) =>
              setQuestion(event.target.value)
            }
            placeholder="Create a bar chart showing total sales for each product."
            rows={4}
            required
          />

          <button
            type="submit"
            disabled={loading}
          >
            {loading ? "Asking AI..." : "Ask AI"}
          </button>

        </form>

        {error && (
          <div className="message error">
            {error}
          </div>
        )}

        {answer && (
          <div className="message answer">
            <h2>Answer</h2>
            <pre>{answer}</pre>
          </div>
        )}

        {chart && (
          <div className="message answer">
            <h2>Chart</h2>
            <div ref={chartRef} />
          </div>
        )}

        {image && (
          <div className="message answer">
            <h2>Chart</h2>

            <img
              src={`data:image/png;base64,${image}`}
              alt="Generated chart"
              style={{
                maxWidth: "100%",
                height: "auto",
              }}
            />
          </div>
        )}

      </section>
    </main>
  );
}

export default App;