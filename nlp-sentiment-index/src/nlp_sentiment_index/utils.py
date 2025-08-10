from pathlib import Path
import yaml

def load_config(path: str | Path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def ensure_dirs(*paths: str | Path):
    for p in map(Path, paths):
        p.mkdir(parents=True, exist_ok=True)
