"""Smoke checks for the Studio K12 standalone lesson prototype.
Run: python3 tests/check_studio.py path/to/lesson.html
"""
from pathlib import Path
import re
import sys
import subprocess
import tempfile

path = Path(sys.argv[1] if len(sys.argv)>1 else "index.html")
html = path.read_text(encoding="utf-8")
assert re.search(r"<html\b", html, re.I), "Missing HTML root"
assert re.search(r"</html\s*>", html, re.I), "Missing closing HTML"
assert re.search(r"<body\b", html, re.I), "Missing body"
assert re.search(r"<style\b", html, re.I), "Missing CSS"
scripts = re.findall(r"<script\b[^>]*>(.*?)</script>", html, re.I | re.S)
inline = [s for s in scripts if s.strip()]
assert inline, "No inline JS detected"
for code in inline:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".js", encoding="utf-8", delete=False) as f:
        f.write(code)
        tmp = f.name
    try:
        subprocess.run(["node", "--check", tmp], check=True)
    finally:
        Path(tmp).unlink(missing_ok=True)
if "Prototype 3.5" in html or "3.5-prototype" in html:
    assert "aspect-ratio:16/9" in html or "aspect-ratio: 16 / 9" in html, "Missing 16:9 preview"
    assert "safeSVG" in html, "SVG handling missing"
    assert "scenes" in html, "Lesson scene data missing"
print(f"PASS: {path.name}; {len(inline)} inline JS blocks")
