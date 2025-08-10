import re
import pandas as pd

# Regex to capture ticker-like patterns (with optional $ sign)
TICKER_PATTERN = re.compile(r"\$?[A-Z]{1,5}(?=\b)")

# Simple sector map — expand with a CSV for production
SECTOR_MAP = {
    "AAPL": "Technology", "MSFT": "Technology", "GOOGL": "Communication Services",
    "AMZN": "Consumer Discretionary", "JPM": "Financials"
}

def extract_tickers(title: str) -> list[str]:
    cands = set(m.group(0).lstrip("$") for m in TICKER_PATTERN.finditer(title or ""))
    return [c for c in cands if 1 <= len(c) <= 5]

def add_tickers(df: pd.DataFrame, title_col: str = "title") -> pd.DataFrame:
    df = df.copy()
    df["tickers"] = df[title_col].map(extract_tickers)
    return df

def sector_from_tickers(tickers: list[str]) -> str | None:
    for t in tickers or []:
        if t in SECTOR_MAP:
            return SECTOR_MAP[t]
    return None

def daily_sector_sentiment(df_scored: pd.DataFrame, agg: str = "mean") -> pd.DataFrame:
    tmp = df_scored.copy()
    tmp["sector"] = tmp["tickers"].map(sector_from_tickers)
    tmp = tmp.dropna(subset=["sector"])
    if tmp.empty:
        return pd.DataFrame(columns=["date", "sector", "sentiment"])
    if agg == "median":
        out = tmp.groupby(["date", "sector"])["compound"].median().reset_index()
    else:
        out = tmp.groupby(["date", "sector"])["compound"].mean().reset_index()
    out = out.rename(columns={"compound": "sentiment"})
    return out