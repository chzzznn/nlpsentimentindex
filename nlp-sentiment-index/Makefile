.PHONY: fetch sentiment market analyze plots pipeline lint test

fetch:
	python scripts/fetch_news.py --config configs/config.yaml
	python scripts/fetch_market.py --config configs/config.yaml

sentiment:
	python scripts/build_sentiment.py --config configs/config.yaml

analyze:
	python scripts/study_relationships.py --config configs/config.yaml

plots:
	python -c "from src.nlp_sentiment_index.visualize import plot_all; plot_all('configs/config.yaml')"

pipeline: fetch sentiment analyze plots

lint:
	flake8 src scripts

test:
	pytest -q
