import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # project root

def load_raw():
    raw_dir = ROOT / "data" / "raw"
    train = pd.read_csv(raw_dir / "train.csv", parse_dates=["Date"])
    stores = pd.read_csv(raw_dir / "store.csv")
    test = pd.read_csv(raw_dir / "test.csv", parse_dates=["Date"])
    return train, stores, test

if __name__ == "__main__":
    train, stores, test = load_raw()
    print("Train shape:", train.shape)
    print("Stores shape:", stores.shape)
    print(train.head())
