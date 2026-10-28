"""Merge margin.py parts (disjoint cell ranges): python3 merge_margin.py <tag_out> <tag_part1> <tag_part2> ...
Arrays are NaN where a part did not compute a cell; summarize() recomputes margin.json over the merged arrays."""
import sys, os, json
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial
from opimage import Cells
from run_section import HERE
import margin

tag_out = sys.argv[1]; parts = sys.argv[2:]
keys = ("M_lo", "Q", "BP_up", "GR_up", "DU_up", "MU", "MA_lo", "TANG")
arrays = None; seconds = 0.0; meta = None
for p in parts:
    d = os.path.join(HERE, "runs", p)
    z = np.load(os.path.join(d, "margin.npz")); js = json.load(open(os.path.join(d, "margin.json")))
    if arrays is None: arrays = {k: z[k].copy() for k in keys}; meta = js
    else:
        for k in keys:
            a = z[k]; m = ~np.isnan(a)
            assert np.isnan(arrays[k][m]).all(), "overlapping cells between parts in " + k
            arrays[k][m] = a[m]
    seconds += js["seconds"]
prec = meta["prec"]; ntheta = meta["ntheta"]
ctx.prec = prec
T = ExactTrial(prec=prec)
cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
assert cells.n == arrays["M_lo"].shape[0]
th = [arb.pi() / 2 * i / ntheta for i in range(ntheta + 1)]
missing = int(np.isnan(arrays["M_lo"][:, 0]).sum())
print("merged %d parts; cells missing: %d of %d" % (len(parts), missing, cells.n))
margin.summarize(tag_out, arrays, cells, ntheta, prec, th, seconds)
