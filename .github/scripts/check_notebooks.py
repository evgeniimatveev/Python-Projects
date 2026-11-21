"""Static checks for every project folder (nothing is executed).

* no spaces or emoji in tracked file names
* every notebook is valid nbformat and every code cell parses (IPython magics are ignored)
* no personal absolute paths (Windows user folders)
* every data / image file a notebook reads exists next to it (or is listed in EXTERNAL below)
* relative links in every README point to files that exist
"""
import ast
import glob
import json
import os
import re
import subprocess
import sys

import nbformat

BS = chr(92)
# files the notebooks read but that are deliberately not in the repo (see the project README)
EXTERNAL = {"02-amazon-reviews-analysis": {"amazon_alexa.tsv"}}

problems = []
tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.splitlines()
for f in tracked:
    base = os.path.basename(f)
    if " " in base or any(ord(ch) > 127 for ch in f):
        problems.append(f"{f}: file name has a space or a non-ASCII character")

notebooks = sorted(glob.glob("*/*.ipynb"))
n_cells = 0
for f in notebooks:
    folder = os.path.dirname(f)
    try:
        nb = nbformat.read(f, as_version=4)
        nbformat.validate(nb)
    except Exception as exc:  # noqa: BLE001
        problems.append(f"{f}: invalid notebook: {str(exc).splitlines()[0][:120]}")
        continue
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        n_cells += 1
        src = "\n".join(l for l in cell.source.splitlines() if not l.lstrip().startswith(("%", "!")))
        try:
            ast.parse(src)
        except SyntaxError as exc:
            problems.append(f"{f}: code cell {i} does not parse: {exc.msg} (line {exc.lineno})")
        if (":" + BS + "Users") in cell.source or "/Users/" in cell.source:
            problems.append(f"{f}: code cell {i} contains a personal absolute path")
        for name in re.findall(r"""["']([\w\-./]+\.(?:csv|tsv|jpg|jpeg|png))["']""", cell.source):
            if not os.path.exists(os.path.join(folder, name)) and name not in EXTERNAL.get(folder, set()):
                problems.append(f"{f}: code cell {i} reads '{name}', which is not in {folder}/")

readmes = sorted(glob.glob("*/README.md")) + ["README.md"]
for r in readmes:
    base = os.path.dirname(r)
    text = open(r, encoding="utf-8").read()
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"^(https?:|#|mailto:)", target):
            continue
        path = os.path.normpath(os.path.join(base, target.split("#")[0]))
        if not os.path.exists(path):
            problems.append(f"{r}: broken relative link '{target}'")

print(f"Checked {len(notebooks)} notebooks ({n_cells} code cells), {len(readmes)} READMEs, {len(problems)} problem(s)")
for p in problems:
    print("FAIL ", p)
sys.exit(1 if problems else 0)
