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

    # Create the bar chart
    fig = px.bar(
        df,
        x="cores",
        y="time [s]",
        color=color_by,
        barmode="group",
        title="Times for selected rows",
    )

    # --- Show only the tics corresponding to the selected numbers of cores ---
    fig.update_xaxes(
        tickmode="array",
        tickvals=sorted(df["cores"].unique()),
    )

    st.plotly_chart(fig, use_container_width=True)
