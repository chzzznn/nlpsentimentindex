from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .utils import load_config

def plot_all(config_path: str):
    cfg = load_config(config_path)
    plots_dir = Path(cfg["io"]["plots_dir"])
    plots_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(Path(cfg["io"]["processed_dir"]) / "merged.csv", parse_dates=["date"]).sort_values("date")

    ax = df.set_index("date")[["sentiment", "log_return"]].plot(figsize=(10,4), title="Sentiment vs Log Returns")
    fig = ax.get_figure(); fig.tight_layout(); fig.savefig(plots_dir / "sentiment_vs_returns.png")
    plt.close(fig)

    if "rolling_corr" in df.columns:
        ax = df.set_index("date")["rolling_corr"].plot(figsize=(10,4), title="Rolling Correlation (Sentiment vs Returns)")
        fig = ax.get_figure(); fig.tight_layout(); fig.savefig(plots_dir / "rolling_corr.png")
        plt.close(fig)
