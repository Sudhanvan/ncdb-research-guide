"""Render Quarto and update the directory published by GitHub Pages."""
from pathlib import Path
import shutil
import subprocess
root = Path(__file__).resolve().parent
subprocess.run(["quarto", "render", str(root / "website")], check=True)
rendered = root / "website" / "_site"
assert (rendered / "index.html").is_file()
published = root / "docs"
if published.exists():
    shutil.rmtree(published)
shutil.copytree(rendered, published)
(published / ".nojekyll").write_text("")
print("Rebuilt docs/. Review, commit, and push to publish.")
