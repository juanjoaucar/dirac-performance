from pathlib import Path
import io
import zipfile
import streamlit as st


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
