from pathlib import Path
import pandas as pd

def load_csvs(root: Path):
    paths = list(root.rglob("benchmark_summary.csv"))
    info = []
    for p in paths:
        rel = p.relative_to(root)
        cpu = rel.parts[0]
        build = rel.parts[1]
        info.append((cpu, build, p))
    return info


def load_and_normalize(path, cpu, build_name):
    df = pd.read_csv(path).ffill()
    df["CPU"] = cpu
    df["Test"] = pd.to_numeric(df["Test"], errors="coerce")
    df["cores"] = pd.to_numeric(df["cores"], errors="coerce")
    df["build"] = build_name

    return df

