from pathlib import Path
from collections import defaultdict
import streamlit as st

def build_categories(root: Path):
    categorias = defaultdict(list)
    for f in root.rglob("*.html"):
        rel = f.relative_to(root)
        categoria = rel.parts[0] if len(rel.parts) > 1 else "(root)"
        categorias[categoria].append(rel)
    return dict(sorted(categorias.items()))


def sidebar_selector(categorias, root):
    st.sidebar.write("### Explorer for specific CPU and build-type")

    cat_sel = st.sidebar.selectbox("Reports:", list(categorias.keys()))
    archivos = categorias[cat_sel]

    # Mostrar sólo primer nivel
    archivo_nombres = []
    for a in archivos:
        parts = a.parts
        archivo_nombres.append(parts[1] if len(parts) > 1 else a.name)

    archivo_map = dict(zip(archivo_nombres, archivos))

    archivo_sel = st.sidebar.selectbox("Builds:", archivo_nombres)
    return root / archivo_map[archivo_sel]
