import streamlit as st
import os

st.title("Visor de HTMLs")

# ---- Descripción editable ----
st.markdown("""
### Descripción
Acá podés escribir una explicación o resumen de lo que muestran los reportes HTML.
(Colocá el texto que quieras en este bloque.)
""")



HTML_DIR = "html"

# listar archivos html
html_files = [f for f in os.listdir(HTML_DIR) if f.endswith(".html")]

opcion = st.selectbox("Reportes generados por los distintos tipos de procesadores:", html_files)

if opcion:
    archivo_path = os.path.join(HTML_DIR, opcion)

    with open(archivo_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    st.components.v1.html(html_content, height=800, scrolling=True)
