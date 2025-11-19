from pathlib import Path
import base64
import re
import io
import zipfile
import streamlit as st

def file_to_data_url(path: Path) -> str:
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
    # Regex pattern to find href and src attributes
    pattern = r'(href|src)=["\']([^"\']+)["\']'

    def repl(match):
        attr = match.group(1)
        href = match.group(2)

        # Ignore absolute URLs (http, https)
        if href.startswith("http://") or href.startswith("https://"):
            return match.group(0)

        # Resolve the target file path
        target = (parent_dir / href).resolve()
        if target.exists():
            try:
                from .file_utils import file_to_data_url
                return f'{attr}="{file_to_data_url(target)}"'
            except:
                pass

        return match.group(0)

    return re.sub(pattern, repl, html)



def zip_integrity(zip_bytes: io.BytesIO, ROOT: Path) -> bool:
    try:
        with zipfile.ZipFile(zip_bytes, "r") as zip_ref:
            # Test integrity of the ZIP file
            bad_file = zip_ref.testzip()
            if bad_file:
                st.error(f"The ZIP file is corrupted. Problem at {bad_file}")
            else:
                zip_ref.extractall(ROOT)
                st.success(f"Report uploaded and extracted to {ROOT}")

                    # Guardar en session_state para limpieza
                uploaded_tmp_dirs = st.session_state.get("uploaded_tmp_dirs", [])
                entries = zip_ref.namelist()
                top_level_dirs = sorted({p.split("/")[0] for p in entries if "/" in p})
                for d in top_level_dirs:
                    if d not in uploaded_tmp_dirs:
                        uploaded_tmp_dirs.append(d)
                st.session_state["uploaded_tmp_dirs"] = uploaded_tmp_dirs


    except zipfile.BadZipFile:
        st.error("The uploaded file is not a valid ZIP.")
    except EOFError:
        st.error("The ZIP file is incomplete or corrupted.")