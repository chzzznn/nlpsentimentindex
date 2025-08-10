import os
from pathlib import Path
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

def fetch_news_newsapi(query: str, from_date: str, to_date: str, sources: list[str] | None, language: str,
                        page_size: int = 100) -> pd.DataFrame:
    base = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "language": language,
        "pageSize": page_size,
        "sortBy": "publishedAt",
        "apiKey": NEWSAPI_KEY,
    }
    if sources:
        params["domains"] = ",".join(sources)

    r = requests.get(base, params=params, timeout=30)
    r.raise_for_status()
    data = r.json().get("articles", [])
    rows = []
    for a in data:
        rows.append({
            "publishedAt": a.get("publishedAt"),
            "title": a.get("title"),
            "source": a.get("source", {}).get("name"),
            "url": a.get("url"),
        })
    df = pd.DataFrame(rows)
    if not df.empty:
        df["date"] = pd.to_datetime(df["publishedAt"]).dt.date
    return df

def save_csv(df: pd.DataFrame, path: str | Path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
