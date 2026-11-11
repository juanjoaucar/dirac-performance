from pathlib import Path
from datetime import datetime
import re
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


def cpu_model(build_dir: Path):
    """ CPU model from setup_info/lscpu.txt (same CPU across report folders), else the report folder name. """
    lscpu = build_dir / "setup_info" / "lscpu.txt"
    if lscpu.exists():
        m = re.search(r"^Model name:\s*(.+)$", lscpu.read_text(), re.M)
        if m:
            return m.group(1).strip()
    return build_dir.parent.name


def dirac_version(build_dir: Path):
    """ Label like '26.1 (2026-11-11, 6f3ae3fb3)' from setup_info/VERSION and git_info.h. """
    info = build_dir / "setup_info"
    version = (info / "VERSION").read_text().strip() if (info / "VERSION").exists() else "unknown"
    if not (info / "git_info.h").exists():
        return version

    git = dict(re.findall(r'#define (\w+) "(.*)"', (info / "git_info.h").read_text()))
    date = git.get("GIT_COMMIT_DATE", "unknown")
    try:
        # git's default date format, e.g. 'Wed Nov 11 16:53:24 2026 +0100'
        date = datetime.strptime(date, "%a %b %d %H:%M:%S %Y %z").date()
    except ValueError:
        pass
    return f"{version} ({date}, {git.get('GIT_COMMIT_HASH', 'unknown')})"


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


