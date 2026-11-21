"""Static quality gates for isolated Prototype 3.5 QA (10-scene lesson).

Usage: python3 tests/check_prototype35.py [path/to/prototype.html]
Only validates source structure and JavaScript syntax. It does not certify
mathematical correctness, visual layout, audio, video export, or deployment.
"""
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

DEFAULT = "prototypes/NguyenTrang_Studio_K12_Prototype_3_5_QA_Layout.html"
path = Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT)
html = path.read_text(encoding="utf-8")

assert re.search(r"<html\b[^>]*lang=[\"']vi[\"']", html, re.I), "Missing Vietnamese HTML root"
assert re.search(r"<body\b", html, re.I), "Missing body"
assert re.search(r"<style\b", html, re.I), "Missing styles"
assert "aspect-ratio:16/9" in html or "aspect-ratio: 16/9" in html, "Missing 16:9 stage"
assert "safeSVG" in html, "SVG sanitizer hook missing"
assert "mathjax" in html.lower(), "MathJax reference missing"
assert "Prototype 3.5 QA" in html, "Wrong version label"

match = re.search(
    r'<script\s+id=["\']lesson-data["\']\s+type=["\']application/json["\']>(.*?)</script\s*>',
    html, re.I | re.S
)
assert match, "Embedded lesson-data JSON missing"
lesson = json.loads(match.group(1))
assert lesson.get("title") == "Bài 1. Phép biến hình", "Unexpected lesson"
scenes = lesson.get("scenes")
assert isinstance(scenes, list) and len(scenes) == 10, "Expected exactly 10 lesson scenes"
ids = [scene.get("id") for scene in scenes]
assert all(isinstance(i, str) and i.strip() for i in ids), "Scene id missing"
assert len(ids) == len(set(ids)), "Duplicate scene ids"

for number, scene in enumerate(scenes, start=1):
    assert isinstance(scene.get("heading"), str) and scene["heading"].strip(), f"Scene {number}: missing heading"
    assert isinstance(scene.get("bullets"), list), f"Scene {number}: bullets must be an array"
    assert isinstance(scene.get("narration"), str) and scene["narration"].strip(), f"Scene {number}: missing narration"
    assert isinstance(scene.get("source"), str) and scene["source"].strip(), f"Scene {number}: missing source"
    for key in ("quiz", "check"):
        q = scene.get(key)
        if q and q.get("type", "mcq") == "mcq":
            options = q.get("options")
            answer = q.get("answer")
            assert isinstance(options, list) and len(options) >= 2, f"Scene {number}: invalid {key} options"
            assert isinstance(answer, int) and 0 <= answer < len(options), f"Scene {number}: invalid {key} answer"

# Deterministic mathematical spot check for scene 9:
# f(x,y)=(x,3y) maps B(2,-1) to (2,-3), answer C (zero-based index 2).
review = scenes[8].get("quiz")
assert review and review.get("answer") == 2, "Scene 9: expected answer C"
assert "3y" in review.get("question", ""), "Scene 9: expected coordinate transformation"
assert "(2;-3)" in review["options"][2], "Scene 9: incorrect image of B"

# Script tags containing lesson-data JSON are data, NOT JavaScript.
script_tags = re.findall(r"<script\b([^>]*)>(.*?)</script\s*>", html, re.I | re.S)
inline_js = []
for attrs, code in script_tags:
    if re.search(r'\bsrc\s*=', attrs, re.I):
        continue
    if re.search(r'\btype\s*=\s*["\'](?:application/json|application/ld\+json)["\']', attrs, re.I):
        continue
    if code.strip():
        inline_js.append(code)
assert inline_js, "Missing executable inline JavaScript"
for script in inline_js:
    with tempfile.TemporaryDirectory() as folder:
        js = Path(folder) / "inline.js"
        js.write_text(script, encoding="utf-8")
        subprocess.run(["node", "--check", str(js)], check=True)

print(f"PASS: Prototype 3.5 QA source: {len(scenes)} scenes, {len(inline_js)} JS block(s), 16:9, scene-9 answer C")
