from pathlib import Path
from collections import defaultdict
import pandas as pd
import streamlit as st

from comparison.loader import build_setup, cpu_model, dirac_version

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

    # Another report may not have the build selected before ("Open report" buttons set it)
    if st.session_state.get("builds_sel") not in archivo_map:
        st.session_state.pop("builds_sel", None)
    archivo_sel = st.sidebar.selectbox("Builds:", archivo_nombres, key="builds_sel")
    return root / archivo_map[archivo_sel]


def builds_index(report_dir: Path):
    """ Index of a report: one expander per build with how it was built, and a button to open its report. """
    st.write(f"### Builds of {report_dir.name}")
    build_dirs = sorted(p.parent for p in report_dir.glob("*/benchmark_report.html"))
    for build_dir in build_dirs:
        setup = build_setup(build_dir)
        with st.expander(build_dir.name):
            st.caption(f"DIRAC {dirac_version(build_dir)} · {cpu_model(build_dir)}")
            st.button("Open report", key=f"open-{build_dir.name}",
                      on_click=st.session_state.update, kwargs={"builds_sel": build_dir.name})

            st.markdown("**How to build it**")
            st.code(setup["setup_command"] or "(not recorded)", language="bash")
            if not setup["modules"]:
                st.caption("Older report: the environment (Docker image or modules) was not recorded, "
                           "only the setup command above and the compilers below.")
            else:
                st.markdown("**All loaded modules**")
                st.code("\n".join(setup["modules"]), language=None)

            if setup["build_info"]:
                st.markdown("**Compilers and libraries** (build_info.h)")
                st.dataframe(pd.DataFrame(setup["build_info"].items(), columns=["", "value"]),
                             hide_index=True)
