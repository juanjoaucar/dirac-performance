import base64
from pathlib import Path
from .file_utils import rewrite_paths

DISABLE_LINKS_CSS = """
<style>
a {
    pointer-events: none; /* deshabilita clics */
    color: gray !important;          /* opcional: cambiar color para indicar que está deshabilitado */
    text-decoration: none;
    cursor: default;
}
</style>
"""

def load_html_as_data_url(path: Path, is_index: bool, extra_header=None):
    parent = path.parent
    raw_html = path.read_text(encoding="utf-8")

    if is_index:
        # Mostrar el Index.html tal cual, pero deshabilitar los links visualmente. Se inyecta un estilo CSS
        html = (extra_header or "") + DISABLE_LINKS_CSS + raw_html
    else:
        html = rewrite_paths(raw_html, parent)

    encoded = base64.b64encode(html.encode()).decode()
    return f"data:text/html;base64,{encoded}"
