import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")
st.title("Visor de reportes DIRAC")

HTML_ROOT = Path("static/html")

# Listar solo archivos .html directamente dentro de static/html/
html_files = [f for f in HTML_ROOT.glob("*.html")]

# Sidebar
choices = [str(f.name) for f in html_files]
sel = st.sidebar.selectbox("Reportes disponibles:", choices)

# URL universal (funciona en local y en la Cloud)
url = f"/static/html/{sel}"

# Mostrar en iframe
st.markdown(
    f"""
    <iframe src="{url}"
            style="width:100%; height:2000px; border:none;">
    </iframe>
    """,
    unsafe_allow_html=True
)

