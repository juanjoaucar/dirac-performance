from pathlib import Path
from .file_utils import rewrite_paths


def load_report_html(path: Path) -> str:
    raw_html = path.read_text(encoding="utf-8")
    return rewrite_paths(raw_html, path.parent)
