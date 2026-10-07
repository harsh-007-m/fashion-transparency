from pathlib import Path 
import pandas as pd 

RAW = Path("data/raw")
FILES = sorted(RAW.glob("trends_*.csv"))
print("Found Files:",[f.name for f in FILES])

def find_header_row(path):
    with open(path, encoding="utf-8-sig") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines):
        if line.startswith(("Month","Week","Day","Time")):
            return i
    raise ValueError(f"No header row found in {path}")

for path in FILES:
    print("\n"+"="*60)
    print(path.name)
    print("="*60)

    with open(path, encoding="utf-8-sig") as f:
        print("".join(f.readlines()[:6]))
    df = pd.read_csv(path, skiprows=find_header_row(path), encoding="utf-8-sig")
    print(df.shape)
    print(df.columns.tolist())
    print(df.head())
    print(df.tail())
    print(df.dtypes)
    print((df == "<1").sum())