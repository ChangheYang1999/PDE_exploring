"""profile the per-column image cost of fsec on one far cell"""
import sys, os, time, cProfile, pstats
sys.argv = ["fsec.py", "PROF", "4", "60", "1", "256", "19"]
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial
from opimage import Cells, Background, Operator
from basis import cutoff_chi
from section import Weights, Section
ctx.prec = 256
T = ExactTrial(prec=256); T.build_green(verbose=False)
CELLS = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
full = set(cutoff_chi(T, CELLS).keys()) | set(ic for ic, cl in enumerate(CELLS.cells) if cl["kind"] in ("outer", "pinf"))
bg = Background(T, CELLS, nmax=19 + 4 + 3, full_cells=full)
k = T.k_q; W = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
SEC = Section(T, CELLS, bg, W, Mh=4, stride=60, Mout=20, stride_test=30, verbose=False)
OP = SEC.op
for ic in (392, 1372):
    print("=== cell", ic, CELLS.cells[ic]["kind"], float(CELLS.cells[ic]["ta"]), flush=True)
    t0 = time.time(); insup = [cd["col"] for cd in SEC.cols if ic in cd["col"].pieces]; print("in-support columns:", len(insup), [cd["label"] for cd in SEC.cols if ic in cd["col"].pieces][:6])
    pr = cProfile.Profile(); pr.enable()
    for col in insup[:4]:
        t1 = time.time(); OP.image(col, ic, parts=True); print("  image(%s, m=%d): %.1fs" % (col.label, col.m, time.time() - t1), flush=True)
    pr.disable(); pstats.Stats(pr).sort_stats("cumulative").print_stats(12)
