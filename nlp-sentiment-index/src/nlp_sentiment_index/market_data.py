import pandas as pd
import numpy as np
import yfinance as yf

def fetch_index(ticker: str, start: str, end: str) -> pd.DataFrame:
    df = yf.download(ticker, start=start, end=end, progress=False)
    df = df.rename_axis("datetime").reset_index()
    # yfinance may use 'Date' or index; handle both
    df["date"] = pd.to_datetime(df["Date"]).dt.date if "Date" in df else pd.to_datetime(df["datetime"]).dt.date
    df = df.sort_values("date")
    df["log_return"] = np.log(df["Close"]).diff()
    return df[["date", "Close", "log_return"]]
