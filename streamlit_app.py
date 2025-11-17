import streamlit as st
from pathlib import Path
import threading
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import socket


st.set_page_config(layout="wide")
st.title("Visor de reportes DIRAC")

HTML_ROOT = Path("static/html")


def get_free_port():
    """Devuelve un puerto libre."""
    s = socket.socket()
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port


@st.cache_resource
def start_static_server():
    app = FastAPI()
    app.mount("/static/html", StaticFiles(directory=HTML_ROOT), name="static-html")

    # elegir puerto dinámicamente
    port = get_free_port()

    def run():
        uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")

    thread = threading.Thread(target=run, daemon=True)
    thread.start()

    return port  # retornamos el puerto elegido


# iniciar servidor estático → devuelve puerto real
STATIC_PORT = start_static_server()


# =========================================================
# UI
# =========================================================
#html_files = list(HTML_ROOT.rglob("*.html")) #de manera recursiva
html_files = [f for f in HTML_ROOT.glob("*.html")] #de manera no recursiva

choices = [str(f.relative_to(HTML_ROOT)) for f in html_files]

sel = st.sidebar.selectbox("Reportes disponibles:", choices)

url = f"http://localhost:{STATIC_PORT}/static/html/{sel}"

st.markdown(
    f'<iframe src="{url}" style="width:100%; height:2000px; border:none;"></iframe>',
    unsafe_allow_html=True
)
