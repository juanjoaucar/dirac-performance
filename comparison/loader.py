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


#def load_and_normalize(path, cpu, build_name):
#    df = pd.read_csv(path).ffill()
#    df["CPU"] = cpu
#    df["Test"] = pd.to_numeric(df["Test"], errors="coerce")
#    df["cores"] = pd.to_numeric(df["cores"], errors="coerce")
#    df["build"] = build_name

#    return df

def load_and_normalize(path, cpu, build_name):
    import pandas as pd

    def safe_string(x):
        """Convierte distintos tipos en un string estable y legible."""
        # Si ya es string → todo bien
        if isinstance(x, str):
            return x

        # Caso típico: dicts de Streamlit / AgGrid
        if isinstance(x, dict):
            # Si tiene un label, úsalo
            if "label" in x:
                return str(x["label"])
            # Si tiene 'value', úsalo
            if "value" in x:
                return str(x["value"])
            # Caso general: el dict completo
            return str(x)

        # Tuplas: típicas de selectbox mal armado
        if isinstance(x, (tuple, list)):
            return "-".join(safe_string(i) for i in x)

        # Último recurso: conversión genérica
        return str(x)

    # Normalizaciones seguras
    cpu_str = safe_string(cpu)
    build_str = safe_string(build_name)

    df = pd.read_csv(path).ffill()
    df["CPU"] = cpu_str
    df["build"] = build_str
    df["Test"] = pd.to_numeric(df["Test"], errors="coerce")
    df["cores"] = pd.to_numeric(df["cores"], errors="coerce")

    return df


