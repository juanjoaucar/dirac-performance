import streamlit as st
from pathlib import Path
import base64
import re
from collections import defaultdict

# Configuración de la página
st.set_page_config(layout="wide")
st.title("Visor de reportes DIRAC — Versión completa")

# Carpeta raíz con los reportes
ROOT = Path("static/html")

# =============================================================================
# UTILIDADES
# =============================================================================

def file_to_data_url(path: Path) -> str:
    """Convierte cualquier archivo (HTML, imagen, CSS, etc.) en un data URL."""
    mime = {
        ".html": "text/html",
        ".css": "text/css",
        ".js": "text/javascript",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".svg": "image/svg+xml",
    }.get(path.suffix.lower(), "application/octet-stream")
    
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode()
    return f"data:{mime};base64,{b64}"

def rewrite_paths(html: str, parent_dir: Path) -> str:
    """Reescribe rutas relativas (href, src, link rel='stylesheet') a data-URLs."""
    pattern = r'(href|src)=["\']([^"\']+)["\']'
    
    def repl(match):
        attr = match.group(1)
        href = match.group(2)
        
        # Ignorar rutas absolutas HTTP/HTTPS
        if href.startswith("http://") or href.startswith("https://"):
            return match.group(0)
        
        # Ruta relativa al archivo actual
        target = (parent_dir / href).resolve()
        if target.exists():
            try:
                return f'{attr}="{file_to_data_url(target)}"'
            except Exception:
                pass
        return match.group(0)
    
    return re.sub(pattern, repl, html)

# =============================================================================
# EXPLORADOR CON SUBCATEGORÍAS POR CARPETA
# =============================================================================

# Construimos un dict: categoria → lista de archivos
categorias = defaultdict(list)
for f in ROOT.rglob("*.html"):
    rel = f.relative_to(ROOT)
    categoria = rel.parts[0] if len(rel.parts) > 1 else "(root)"
    categorias[categoria].append(rel)

# Ordenar categorías alfabéticamente
categorias_ordenadas = dict(sorted(categorias.items()))

# Sidebar
st.sidebar.write("### Reportes disponibles")

# Selección de categoría
cat_sel = st.sidebar.selectbox(
    "Categoría:",
    list(categorias_ordenadas.keys())
)

# Archivos de la categoría seleccionada
archivos = categorias_ordenadas[cat_sel]

# Mostrar solo el primer nivel de subdirectorio dentro de la categoría
# Incluye el primer html, cuyos links no funcionan correctamente (no se muestran las imagenes)
archivo_nombres = []
for a in archivos:
    parts = a.parts
    if len(parts) > 1:
        # Solo tomar la carpeta que contiene el archivo, no el archivo en sí
        nombre_mostrar = parts[1]
    else:
        nombre_mostrar = a.name
    archivo_nombres.append(str(nombre_mostrar))


# Mapear lo que se muestra → path real
archivo_map = dict(zip(archivo_nombres, archivos))



# Selección de archivo
archivo_sel = st.sidebar.selectbox(
    "Archivo:",
    archivo_nombres
)

# Path real del archivo seleccionado
sel_path = ROOT / archivo_map[archivo_sel]

# =============================================================================
# CARGAR Y PROCESAR HTML SELECCIONADO
# =============================================================================

parent_dir = sel_path.parent
raw_html = sel_path.read_text(encoding="utf-8")

# Reescribir rutas relativas internas
html_rewritten = rewrite_paths(raw_html, parent_dir)

# Convertir a data URL
encoded = base64.b64encode(html_rewritten.encode()).decode()
data_url = f"data:text/html;base64,{encoded}"

# =============================================================================
# MOSTRAR EN IFRAME
# =============================================================================

st.markdown(
    f'<iframe src="{data_url}" style="width:100%; height:2000px; border:none;"></iframe>',
    unsafe_allow_html=True
)

