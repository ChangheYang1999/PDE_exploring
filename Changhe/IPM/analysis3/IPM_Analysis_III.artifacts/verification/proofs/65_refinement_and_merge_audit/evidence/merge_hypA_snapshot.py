"""Merge hypA.py parts (disjoint cell ranges) into one run: python3 merge_hypA.py <tag_out> <tag_part1> <tag_part2> ...
Arrays are NaN where a part did not compute a cell; the merged arrays take the computed entries; summarize() recomputes the JSON."""
import sys, os, json
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial
from opimage import Cells
from run_section import HERE
import hypA

tag_out = sys.argv[1]; parts = sys.argv[2:]
keys = ("Dlo", "Dhi", "DPlo", "DPhi", "DD2", "DP2", "DCK", "DPK", "IDCHK", "A1", "A0", "A0W", "KWlo", "KWhi", "Qlo", "Qhi")
arrays = None; sel = set(); dropped = []; seconds = 0.0; meta = None
for p in parts:
    d = os.path.join(HERE, "runs", p)
    z = np.load(os.path.join(d, "hypA.npz")); js = json.load(open(os.path.join(d, "hypA.json")))
    if arrays is None:
        arrays = {k: z[k].copy() for k in keys}; meta = js; th_edges = z["theta_edges"]
    else:
        for k in keys:
            a = z[k]; m = ~np.isnan(a)
            assert np.isnan(arrays[k][m]).all(), "overlapping cells between parts in " + k
            arrays[k][m] = a[m]
    computed = [i for i in range(len(z["Dlo"])) if not np.isnan(z["Dlo"][i])]
    sel |= set(computed); seconds += js["seconds"]
    dp = os.path.join(d, "hypA_dropped.json")
    if os.path.exists(dp): dropped += [(x["cell"], x["what"], x["mid"], x["rad"]) for x in json.load(open(dp))]
prec = meta["prec"]; ntheta = meta["ntheta"]
ctx.prec = prec
T = ExactTrial(prec=prec)
cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
assert cells.n == len(arrays["Dlo"])
c_l = 1 / T.k; D = 4 * c_l - 1
th = [arb.pi() / 2 * i / ntheta for i in range(ntheta + 1)]
sel = sorted(sel)
print("merged %d parts, %d of %d cells computed" % (len(parts), len(sel), cells.n))
hypA.summarize(tag_out, arrays, cells, sel, ntheta, prec, th, c_l, D, T.k_q, seconds, dropped)
