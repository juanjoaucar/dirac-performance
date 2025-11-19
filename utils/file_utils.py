from pathlib import Path
import base64
import re

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
