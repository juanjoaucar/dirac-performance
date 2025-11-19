import streamlit as st
import pandas as pd
import seaborn as sns
from st_aggrid import AgGrid, GridOptionsBuilder

def render_static_table(df):
    cpus = df["CPU"].unique()
    palette = sns.color_palette("pastel", len(cpus))
    color_map = {cpu: palette[i] for i, cpu in enumerate(cpus)}

    def highlight(row):
        c = color_map[row["CPU"]]
        return [f"background-color: rgba({int(c[0]*255)}, {int(c[1]*255)}, {int(c[2]*255)}, 0.35)"] * len(row)

    styled = df.style.apply(highlight, axis=1)
    styled = (
        df.style
        .apply(highlight, axis=1)
        .format({"Test": "{:.0f}","time [s]": "{:.2f}", "peak RAM [Mb]": "{:.1f}"})
        )
    st.write("### Static table")
    st.dataframe(styled, hide_index=True)


def render_selection_table(df):
    st.write("### Table to generate graphs")

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_pagination(enabled=True)
    opts = gb.build()

    grid = AgGrid(
        df,
        gridOptions=opts,
        update_mode="MODEL_CHANGED",
        theme="streamlit",
        height=400,
    )
    return grid["selected_rows"]
