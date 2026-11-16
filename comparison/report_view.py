from pathlib import Path
import html
import re
import pandas as pd
import streamlit as st

from .loader import build_setup


def embedded_inputs(report_html: Path):
    """ {N: [("Test-N.mol", content), ("Test-N.inp", content)]}: the inputs that html_report.py embedded in each
    plot card of benchmark_report.html (the report folders have no other copy of them). Named after the test
    number N: older reports embed them as Test-<N+2>, from before input_files/ was renumbered to match. """
    inputs = {}
    if not report_html.exists():
        return inputs
    for card in report_html.read_text().split('<div class="card my-4')[1:]:
        position = re.search(r'src="(\d+)\.png"', card)  # the card's test number N, from its N.png plot
        if position:
            n = int(position[1])
            inputs[n] = [(f"Test-{n}.{ext}", html.unescape(text)) for ext, text in
                         re.findall(r'<summary><strong>Test-[^<]+\.(\w+)</strong></summary>\s*<pre[^>]*>(.*?)</pre>',
                                    card, re.S)]
    return inputs


def input_expanders(inputs):
    """ One expander per (file name, content), e.g. from embedded_inputs(). """
    for name, text in inputs:
        with st.expander(name):
            st.code(text, language=None)


def render_report_native(build_dir: Path):
    """ Native Streamlit rendering of one build's report, using Streamlit widgets."""
    setup = build_setup(build_dir)
    with st.expander("How it was built", expanded=False):
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

    df = pd.read_csv(build_dir / "benchmark_summary.csv")
    text_cols = ["Test", "Description", "Property", "N. of Atoms", "Method",
                 "Basis Functions", "Extra Information"]
    df[text_cols] = df[text_cols].ffill()
    df["Test"] = df["Test"].astype(int)
    df["N. of Atoms"] = df["N. of Atoms"].astype(int)
    # reset_index
    df = df.sort_values(["Test", "cores"]).reset_index(drop=True)

    st.subheader("Summary table")
    # Dark-blue top border on each new Test's first row.
    new_test = df["Test"].ne(df["Test"].shift())
    new_test.iloc[0] = False
    border_style = lambda row: ["border-top: 3px solid #0d47a1" if new_test.loc[row.name] else ""
                                 for _ in row]
    styled = (df.style.apply(border_style, axis=1)
              .format({"time [s]": "{:.1f}", "peak RAM [Mb]": "{:.1f}"})
              .hide(axis="index"))
    st.table(styled)

    st.subheader("Plots")
    inputs = embedded_inputs(build_dir / "benchmark_report.html")
    for position in sorted(df["Test"].unique()):
        row = df[df["Test"] == position].iloc[0]
        st.markdown(f"**Test {position}**")
        st.caption(row["Description"])
        input_expanders(inputs.get(position, []))

        for suffixes in [["", "_efficiency"], ["_ram_vs_time", "_ram_vs_time_factor"]]:
            imgs = [build_dir / f"{position}{s}.png" for s in suffixes]
            imgs = [img for img in imgs if img.exists()]
            if not imgs:
                continue
            if len(imgs) == 1:
                # Keep a lone image (e.g. RAM-vs-time) at the same
                # half-width size as a pair, centered, instead of stretched across the row.
                _, mid, _ = st.columns([1, 2, 1])
                mid.image(str(imgs[0]), width="stretch")
            else:
                for col, img in zip(st.columns(len(imgs)), imgs):
                    col.image(str(img), width="stretch")

        st.divider()
