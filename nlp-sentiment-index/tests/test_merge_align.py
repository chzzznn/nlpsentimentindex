import pandas as pd
from src.nlp_sentiment_index.merge_align import inner_merge

def test_inner_merge_basic():
    s = pd.DataFrame({"date": ["2025-01-01"], "sentiment": [0.1]})
    m = pd.DataFrame({"date": ["2025-01-01"], "log_return": [0.02]})
    out = inner_merge(s, m)
    assert len(out) == 1 and set(out.columns) >= {"sentiment", "log_return"}
