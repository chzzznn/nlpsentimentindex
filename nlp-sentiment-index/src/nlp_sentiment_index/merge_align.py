import pandas as pd

def inner_merge(sentiment_daily: pd.DataFrame, market_daily: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(sentiment_daily, market_daily, on="date", how="inner")
    return df.dropna(subset=["sentiment", "log_return"]).reset_index(drop=True)
