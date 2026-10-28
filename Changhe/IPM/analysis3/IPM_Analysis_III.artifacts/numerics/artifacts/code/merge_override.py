"""Override-merge for margin refinement runs: start from runs/<base>/margin.npz, replace the per-cell entries of the refinement parts
(cells they computed), recompute the summary. Usage: python3 merge_override.py <tag_out> <base> <part1> <part2> ..."""
import sys, os, json
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial
from opimage import Cells
from run_section import HERE
import margin
tag_out, base = sys.argv[1], sys.argv[2]; parts = sys.argv[3:]
keys = ("M_lo", "Q", "BP_up", "GR_up", "DU_up", "MU", "MA_lo", "TANG", "VLO", "DV", "M_ref", "MA_ref", "NREF")
zb = np.load(os.path.join(HERE, "runs", base, "margin.npz")); arrays = {k: zb[k].copy() for k in keys}
meta = json.load(open(os.path.join(HERE, "runs", base, "margin.json"))); seconds = meta["seconds"]; replaced = 0
for p in parts:
    d = os.path.join(HERE, "runs", p); z = np.load(os.path.join(d, "margin.npz")); js = json.load(open(os.path.join(d, "margin.json")))
    mask = np.isfinite(z["M_lo"]).all(axis=1)
    for k in keys: arrays[k][mask] = z[k][mask]
    replaced += int(mask.sum()); seconds += js["seconds"]
prec = meta["prec"]; ntheta = meta["ntheta"]; ctx.prec = prec
T = ExactTrial(prec=prec); cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
th = [arb.pi() / 2 * i / ntheta for i in range(ntheta + 1)]
print("override-merge: %d cells replaced from %d parts" % (replaced, len(parts)))
margin.summarize(tag_out, arrays, cells, ntheta, prec, th, seconds)
