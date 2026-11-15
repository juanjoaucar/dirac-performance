import plotly.express as px
import streamlit as st
import pandas as pd

def plot_selected_rows(selected, color_by="CPU"):
    df = pd.DataFrame(selected)
    tests = df["Test"].unique()

    # Check if all selected rows belong to the same Test number
    if len(tests) > 1:
        st.error("Selected rows must belong to the same **Test number**.")
        return

    # cores as category for the x-axis: these are grouped bars to compare one at a
    # time, not a numeric axis, so they shouldn't spread apart by the actual
    # core-count gaps. Keep the numeric column too, needed for the efficiency math.
    cores_order = [str(c) for c in sorted(df["cores"].unique())]
    df["cores_label"] = df["cores"].astype(str)

    # Create the bar chart
    fig = px.bar(
        df,
        x="cores_label",
        y="time [s]",
        color=color_by,
        barmode="group",
        title="Times for selected rows",
        category_orders={"cores_label": cores_order},
        labels={"cores_label": "cores"},
    )

    st.plotly_chart(fig)

    # Efficiency = speedup / cores: 1 at 1 core, 1 if N cores make it N times faster.
    # Needs each series' own 1-core time, so only series with a 1-core row selected show up.
    one_core = df[df["cores"] == 1][[color_by, "time [s]"]].rename(columns={"time [s]": "time_1core"})
    df_eff = df.merge(one_core, on=color_by)
    df_eff["efficiency"] = df_eff["time_1core"] / (df_eff["time [s]"] * df_eff["cores"])

    fig_eff = px.bar(
        df_eff,
        x="cores_label",
        y="efficiency",
        color=color_by,
        barmode="group",
        title="Time efficiency for selected rows (x 1 core)",
        category_orders={"cores_label": cores_order},
        labels={"cores_label": "cores"},
    )
    st.plotly_chart(fig_eff)
