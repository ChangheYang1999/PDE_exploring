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
keys = ("M_lo", "Q", "BP_up", "GR_up", "DU_up", "MU", "MA_lo", "TANG", "VLO", "DV", "M_ref", "MA_ref")
arrays = None; seconds = 0.0; meta = None; nref = None; covered = None
for p in parts:
    d = os.path.join(HERE, "runs", p)
    z = np.load(os.path.join(d, "margin.npz")); js = json.load(open(os.path.join(d, "margin.json")))
    mask_cells = np.isfinite(z["M_lo"]).all(axis=1)           # fully computed cells of this part (V066/V068: all angular entries; mask also for integer arrays)
    if arrays is None:
        arrays = {k: z[k].copy() for k in keys}; meta = js; nref = z["NREF"].copy(); covered = mask_cells.copy()
    else:
        assert not (covered & mask_cells).any(), "overlapping cells between parts"
        for k in keys:
            a = z[k]; arrays[k][mask_cells] = a[mask_cells]
        nref[mask_cells] = z["NREF"][mask_cells]; covered |= mask_cells
    seconds += js["seconds"]
arrays["NREF"] = nref
prec = meta["prec"]; ntheta = meta["ntheta"]
ctx.prec = prec
T = ExactTrial(prec=prec)
cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
assert cells.n == arrays["M_lo"].shape[0]
th = [arb.pi() / 2 * i / ntheta for i in range(ntheta + 1)]
missing = int((~covered).sum())
print("merged %d parts; cells missing: %d of %d; refined leaves finite: %s" % (len(parts), missing, cells.n, bool(np.isfinite(arrays["M_ref"][covered]).all() and np.isfinite(arrays["MA_ref"][covered]).all())))
if missing: print("WARNING: incomplete coverage; the global infimum below is NOT a global certificate")
margin.summarize(tag_out, arrays, cells, ntheta, prec, th, seconds)
