"""Execute the notebooks that can run without a human, a webcam or a private dataset.

Nothing is written back to the repository: the notebooks are patched in memory only.
  * input()          -> scripted answers (INPUTS), so the games run to the end
  * time.sleep()     -> no-op
  * root.mainloop()  -> root.update(); root.destroy()   (the window is built, then closed; run under Xvfb)
  * %pip / !pip      -> removed (dependencies are installed by the workflow)
  * webcam loop      -> cells that open the camera are skipped (SKIP_CELLS)
"""
import os
import re
import sys
import time
import traceback

import nbformat
from nbclient import NotebookClient

INPUTS = {
    "04-movie-recommendation": ["abc", "-5", "7", "35", "-1"],
    "08-fortune-teller": ["blue", "5", "n"],
    "09-guessing-game": ["9", "1", "abc", "0", "exit"],
}
GUI = {"05-image-processing-app", "07-tic-tac-toe", "10-zodiac-sign-finder"}
SKIP_CELLS = {"06-opencv-realtime-effects": ["VideoCapture"]}
NOT_RUN = {
    "02-amazon-reviews-analysis": "the dataset amazon_alexa.tsv is not in the repository (Kaggle download)",
    "03-real-time-ai-detection": "needs a webcam, PyTorch and MediaPipe",
}

PRELUDE = """import time
_answers = iter({answers!r})
def _input(prompt=''):
    value = next(_answers)
    print(str(prompt) + str(value))
    return value
input = _input   # a global shadows the builtin (ipykernel re-installs builtins.input for every cell)
time.sleep = lambda *a, **k: None
"""

summary_path = os.environ.get("GITHUB_STEP_SUMMARY", os.devnull)
rows, failed = [], 0
folders = sorted(d for d in os.listdir(".") if re.match(r"^\d\d-", d) and os.path.isdir(d) and d != "00-quickstart")
folders = ["00-quickstart"] + folders
for folder in folders:
    nbs = [f for f in os.listdir(folder) if f.endswith(".ipynb")]
    if not nbs:
        continue
    if os.environ.get("NB_ONLY") and folder[:2] not in os.environ["NB_ONLY"].split(","):  # local debugging: NB_ONLY=04,08
        continue
    name = f"{folder}/{nbs[0]}"
    if folder in NOT_RUN:
        rows.append((name, "⏭️ not run", NOT_RUN[folder]))
        print(f"SKIPPED {name}: {NOT_RUN[folder]}")
        continue
    nb = nbformat.read(name, as_version=4)
    keep = []
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        if any(token in cell.source for token in SKIP_CELLS.get(folder, [])):
            continue
        cell.source = "\n".join(l for l in cell.source.splitlines() if not re.match(r"^\s*[%!]pip\b", l))
        if folder in GUI:
            cell.source = re.sub(r"\broot\.mainloop\(\)", "root.update(); root.destroy()", cell.source)
        keep.append(cell)
    nb.cells = keep
    answers = INPUTS.get(folder, [])
    nb.cells.insert(0, nbformat.v4.new_code_cell(PRELUDE.format(answers=answers)))
    start = time.time()
    try:
        NotebookClient(nb, timeout=600, kernel_name="python3", resources={"metadata": {"path": folder}}).execute()
        print(f"PASSED  {name} ({time.time() - start:.0f}s, {len(nb.cells) - 1} code cells)")
        rows.append((name, "✅ passed", f"{len(nb.cells) - 1} code cells, {time.time() - start:.0f}s"))
    except Exception as exc:  # noqa: BLE001
        failed += 1
        detail = str(exc).strip().splitlines()
        short = next((l for l in reversed(detail) if re.search(r"Error|Exception", l)), detail[-1] if detail else "error")
        print(f"FAILED  {name}: {short}")
        traceback.print_exc(limit=0)
        rows.append((name, "❌ failed", short[:140]))

with open(summary_path, "a", encoding="utf-8") as fh:
    fh.write("## Notebook run\n\n| Notebook | Result | Detail |\n|---|:-:|---|\n")
    for n, r, d in rows:
        fh.write(f"| `{n}` | {r} | {d.replace('|', '/')} |\n")
ran = sum(1 for _, r, _ in rows if "passed" in r)
print(f"\nSummary: {ran} passed, {failed} failed, {sum(1 for _, r, _ in rows if 'not run' in r)} not run")
sys.exit(1 if failed else 0)
