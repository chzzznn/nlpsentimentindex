import argparse
from pathlib import Path
import pandas as pd
from src.nlp_sentiment_index.utils import load_config, ensure_dirs
from src.nlp_sentiment_index.sentiment import score_headlines, daily_index

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()

cfg = load_config(args.config)
raw_dir = Path(cfg["io"]["raw_dir"]); processed_dir = Path(cfg["io"]["processed_dir"]); ensure_dirs(processed_dir)

headlines_path = raw_dir / "headlines.csv"
df = pd.read_csv(headlines_path)
scored = score_headlines(df)
daily = daily_index(scored, agg=cfg["sentiment"].get("agg", "mean"))
daily.to_csv(processed_dir / "sentiment_daily.csv", index=False)
print("Saved daily sentiment →", processed_dir / "sentiment_daily.csv")
