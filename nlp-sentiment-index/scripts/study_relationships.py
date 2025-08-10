import argparse
from pathlib import Path
import pandas as pd
from src.nlp_sentiment_index.utils import load_config, ensure_dirs
from src.nlp_sentiment_index.merge_align import inner_merge
from src.nlp_sentiment_index.analysis import rolling_corr, lag_regression

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()

cfg = load_config(args.config)
processed_dir = Path(cfg["io"]["processed_dir"]); ensure_dirs(processed_dir)

sent = pd.read_csv(processed_dir / "sentiment_daily.csv")
mk = pd.read_csv(processed_dir / "market_daily.csv")

merged = inner_merge(sent, mk)
merged["rolling_corr"] = rolling_corr(merged, window=int(cfg["analysis"]["rolling_window"]))
merged.to_csv(processed_dir / "merged.csv", index=False)

model = lag_regression(merged)
print(model.summary())
