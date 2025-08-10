import argparse
from pathlib import Path
from src.nlp_sentiment_index.utils import load_config, ensure_dirs
from src.nlp_sentiment_index.market_data import fetch_index

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()

cfg = load_config(args.config)
processed_dir = Path(cfg["io"]["processed_dir"]); ensure_dirs(processed_dir)
mk = cfg["market"]

print("Fetching market data…")
df = fetch_index(mk["ticker"], str(mk["start"]), str(mk["end"]))
df.to_csv(processed_dir / "market_daily.csv", index=False)
print("Saved market data →", processed_dir / "market_daily.csv")
