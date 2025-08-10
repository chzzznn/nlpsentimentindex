import argparse
from pathlib import Path
from src.nlp_sentiment_index.utils import load_config, ensure_dirs
from src.nlp_sentiment_index.data_fetch import fetch_news_newsapi, save_csv

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()

cfg = load_config(args.config)
raw_dir = Path(cfg["io"]["raw_dir"]); ensure_dirs(raw_dir)
news_cfg = cfg["news"]

print("Fetching headlines…")
df = fetch_news_newsapi(
    query=news_cfg["query"],
    from_date=str(news_cfg["from_date"]),
    to_date=str(news_cfg["to_date"]),
    sources=news_cfg.get("sources"),
    language=news_cfg.get("language", "en"),
    page_size=int(news_cfg.get("page_size", 100)),
)
save_csv(df, raw_dir / "headlines.csv")
print(f"Saved {len(df)} headlines → {raw_dir / 'headlines.csv'}")
