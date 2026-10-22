"""Knot refinement of the trial on a band (exact knot insertion; the function is unchanged): insert the midpoints of the original knot
intervals inside [t1, t2] and re-express all modes on the refined knot vector (least squares on a dense grid; exact up to roundoff since
the old spline space is a subspace of the new one). Output: a Trial npz with the refined knots. Then src/resid_smooth.py with stride-1
coarse_space on the refined trial performs the Gauss-Newton step on the refined space.
Usage: python3 refine_knots.py trial.npz t1 t2 out.npz
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import BSpline
from modal_fit import Trial

path, t1, t2, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
d = dict(np.load(path)); T = Trial(d); p = T.p; kn = T.knots; kin = kn[p + 1:-(p + 1)]
inb = np.where((kin >= t1) & (kin <= t2))[0]
mids = 0.5 * (kin[inb[:-1]] + kin[inb[1:]])
new_int = np.sort(np.r_[kin, mids]); new_knots = np.r_[np.full(p + 1, T.tmin), new_int, np.full(p + 1, T.t0)]
nb = len(new_knots) - p - 1
print("band [%.4f, %.4f]: %d original interior knots in the band, %d midpoints inserted; total interior knots %d -> %d" % (t1, t2, len(inb), len(mids), len(kin), len(new_int)), flush=True)
# re-expression: fit all modes on the new knot vector on a dense grid (>= 16 points per new cell); exact (subspace) up to roundoff
cells = np.unique(new_knots)
tg = np.unique(np.concatenate([np.linspace(a, b, 18) for a, b in zip(cells[:-1], cells[1:])]))
B = np.nan_to_num(BSpline(new_knots, np.eye(nb), p, extrapolate=False)(tg))
Y = T.eval(tg, 0)
S_new = np.linalg.lstsq(B, Y, rcond=None)[0]
err = np.abs(B @ S_new - Y).max(); print("re-expression error on the dense grid: %.2e (max |a_m| %.3e)" % (err, np.abs(Y).max()), flush=True)
d["knots"] = new_knots; d["S"] = S_new.T.copy()
np.savez_compressed(out, **d)
T2 = Trial(dict(np.load(out))); tt = np.linspace(T.tmin + 1e-9, T.t0 - 1e-9, 20001)
for nu in range(3):
    print("check derivative order %d: max |new - old| = %.2e (max |old| %.3e)" % (nu, np.abs(T2.eval(tt, nu) - T.eval(tt, nu)).max(), np.abs(T.eval(tt, nu)).max()))
print("saved", out)
