"""Print the indices of the kind 'outer' cells of the margin.py cell cover with the 24-offset finer outer cover (shift 4), for the
MARGIN_OUTER_EXTRA run OUTER_F8 (cells from t_+ + 1/2 to t_+ + 8; the first eight (t_+ .. t_+ + 1/2) were done by OUTER_F403)."""
import os, sys, json
os.environ["MARGIN_OUTER_EXTRA"] = "1/16,1/8,3/16,1/4,5/16,3/8,7/16,1/2,5/8,3/4,7/8,1,5/4,3/2,7/4,2,5/2,3,7/2,4,5,6,7,8"
sys.argv = ["margin.py"]
import margin
from flint import fmpq, ctx
ctx.prec = 160
T = margin.ExactTrial(prec=160)
cells = margin.Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(x) for x in os.environ["MARGIN_OUTER_EXTRA"].split(",")])
for i, cl in enumerate(cells.cells):
    if cl["kind"] in ("outer", "pinf"): print(i, cl["kind"], str(cl["shift"]), float(cl["ta"]), (float(cl["h"]) if cl["h"] is not None else None))
sel = [i for i, cl in enumerate(cells.cells) if cl["kind"] == "outer" and cl["shift"] >= fmpq(1, 2)]
print("n cells", cells.n, "selected", sel); json.dump(sel, open("runs/outer_cells_f8.json", "w"))
