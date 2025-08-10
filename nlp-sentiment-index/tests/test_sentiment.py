import pandas as pd
from src.nlp_sentiment_index.sentiment import score_headlines, daily_index

def test_daily_index_mean():
    df = pd.DataFrame({"date": ["2025-01-01", "2025-01-01"], "title": ["good", "bad"]})
    scored = score_headlines(df)
    daily = daily_index(scored, agg="mean")
    assert "sentiment" in daily.columns
