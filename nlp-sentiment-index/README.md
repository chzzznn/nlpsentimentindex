# NLP-Based Sentiment Index

A daily sentiment factor built from financial headlines and tested against market returns (S&P 500 by default).

## Setup
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
cp .env.example .env  # fill in API keys
```

## Usage
```bash
# 1) Fetch headlines and market data
make fetch

# 2) Build daily sentiment index
make sentiment

# 3) Merge with returns & run analysis (rolling corr, OLS)
make analyze

# 4) Generate plots
make plots

# Or one shot
make pipeline
```

## Config
Edit `configs/config.yaml` to set date ranges, sources, tickers, and parameters.
