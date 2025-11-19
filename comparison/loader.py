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
    import pandas as pd

    def safe_string(x):
        """ Convert various types into a stable and readable string. """
        # If string already, return as is
        if isinstance(x, str):
            return x

        # Typical case: dicts from Streamlit / AgGrid
        if isinstance(x, dict):
            # If it has a label, use it
            if "label" in x:
                return str(x["label"])
            # If it has 'value', use it
            if "value" in x:
                return str(x["value"])
            # General case: the whole dict
            return str(x)

        # Tuples or lists: join elements with '-'
        if isinstance(x, (tuple, list)):
            return "-".join(safe_string(i) for i in x)

        # Last resort: generic conversion
        return str(x)

    # Safe conversions
    cpu_str = safe_string(cpu)
    build_str = safe_string(build_name)

    df = pd.read_csv(path).ffill()
    df["CPU"] = cpu_str
    df["build"] = build_str
    df["Test"] = pd.to_numeric(df["Test"], errors="coerce")
    df["cores"] = pd.to_numeric(df["cores"], errors="coerce")

    return df


