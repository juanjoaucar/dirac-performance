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

    # cores as category: these are grouped bars to compare one at a time, not a
    # numeric axis, so they shouldn't spread apart by the actual core-count gaps.
    # Plotly infers axis type from the values themselves, not the column dtype, so
    # numeric-looking labels (1, 2, 4...) get treated as linear unless forced here.
    cores_order = sorted(df["cores"].unique())

    # Create the bar chart
    fig = px.bar(
        df,
        x="cores",
        y="time [s]",
        color=color_by,
        barmode="group",
        title="Times for selected rows",
        category_orders={"cores": cores_order},
    )
    fig.update_xaxes(type="category")

    st.plotly_chart(fig)

    # Efficiency = speedup / cores: 1 at 1 core, 1 if N cores make it N times faster.
    # Needs each series' own 1-core time, so only series with a 1-core row selected show up.
    one_core = df[df["cores"] == 1][[color_by, "time [s]"]].rename(columns={"time [s]": "time_1core"})
    df_eff = df.merge(one_core, on=color_by)
    df_eff["efficiency"] = df_eff["time_1core"] / (df_eff["time [s]"] * df_eff["cores"])

    fig_eff = px.bar(
        df_eff,
        x="cores",
        y="efficiency",
        color=color_by,
        barmode="group",
        title="Time efficiency for selected rows (x 1 core)",
        category_orders={"cores": cores_order},
    )
    fig_eff.update_xaxes(type="category")
    st.plotly_chart(fig_eff)

    fig_ram = px.bar(
        df,
        x="cores",
        y="peak RAM [Mb]",
        color=color_by,
        barmode="group",
        title="Peak RAM for selected rows",
        category_orders={"cores": cores_order},
    )
    fig_ram.update_xaxes(type="category")
    st.plotly_chart(fig_ram)


@st.fragment
def quick_test_picker(df, color_by="CPU", key=None):
    """ Quick way to compare one whole test (all its cores) without manually
    checking rows in the selection table. """
    st.write("#### Quick pick: compare one test across all cores")
    tests = sorted(df["Test"].unique().astype(int))  # Test is float64 upstream (pd.to_numeric)
    test_sel = st.segmented_control("Test:", tests, key=key)
    if test_sel is not None:
        rows = df[df["Test"] == test_sel]
        # Joined in case a test number means different tests in the compared reports
        st.markdown(f"**Test {test_sel}:** " + " / ".join(rows["Description"].dropna().unique()))
        plot_selected_rows(rows.to_dict("records"), color_by=color_by)
