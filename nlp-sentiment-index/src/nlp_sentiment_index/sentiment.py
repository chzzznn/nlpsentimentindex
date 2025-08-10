import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

_sia = None

def _get_sia():
    global _sia
    if _sia is None:
        _sia = SentimentIntensityAnalyzer()
    return _sia

def score_headlines(df: pd.DataFrame) -> pd.DataFrame:
    sia = _get_sia()
    df = df.copy()
    df["compound"] = df["title"].fillna("").map(lambda t: sia.polarity_scores(t)["compound"])
    return df

def daily_index(df_scored: pd.DataFrame, agg: str = "mean") -> pd.DataFrame:
    if df_scored.empty:
        return pd.DataFrame(columns=["date", "sentiment"])
    grp = df_scored.groupby("date")["compound"]
    out = grp.median() if agg == "median" else grp.mean()
    return out.rename("sentiment").reset_index()
