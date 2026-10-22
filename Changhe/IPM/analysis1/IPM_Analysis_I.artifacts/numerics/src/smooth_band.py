"""Smoothing experiment (floating, evidence only): replace the trial's fine spline knots on a band t in [t1, t2] by coarse knots of
spacing hc, and refit every mode a_m(t) by least squares on a fine t grid (global fit; outside the band the original spline is
reproduced to roundoff since the knots are unchanged there). Writes a new trial npz with the same keys (knots, S replaced).
The dependent coefficients (Ei, Eo, A00) are kept: the joins at tmin, t0 are far from the band (changes ~1e-14).
Usage: python3 smooth_band.py trial.npz t1 t2 hc out.npz
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import BSpline
from modal_fit import Trial

path, t1, t2, hc, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
d = dict(np.load(path)); T = Trial(d); p = T.p
kn = T.knots; kin = kn[p + 1:-(p + 1)]
keep = kin[(kin < t1) | (kin > t2)]
lo = kin[kin < t1].max(); hi = kin[kin > t2].min()
ncoarse = max(int(round((hi - lo) / hc)), 1); coarse = lo + (hi - lo) * np.arange(1, ncoarse) / ncoarse
new_int = np.sort(np.r_[keep, coarse]); new_knots = np.r_[np.full(p + 1, T.tmin), new_int, np.full(p + 1, T.t0)]
nb = len(new_knots) - p - 1
print("band [%.4f, %.4f]: original interior knots %d, new %d (coarse spacing %.4f over [%.4f, %.4f], %d intervals)" % (
    t1, t2, len(kin), len(new_int), (hi - lo) / ncoarse, lo, hi, ncoarse), flush=True)
# coefficients of basis functions whose support does not meet (lo, hi) are COPIED from the original (same local knots);
# only the others are refitted by least squares on a fine grid over the union of their supports (data minus the fixed part).
def supports(knots):
    return [(knots[i], knots[i + p + 1]) for i in range(len(knots) - p - 1)]
old_sup = supports(kn); new_sup = supports(new_knots)
old_by_knots = {}
for j, (a, b) in enumerate(old_sup): old_by_knots.setdefault((round(a, 12), round(b, 12)), j)
S_new = np.zeros((nb, T.M)); free = []
for i, (a, b) in enumerate(new_sup):
    if b <= lo + 1e-12 or a >= hi - 1e-12:
        j = old_by_knots[(round(a, 12), round(b, 12))]; S_new[i] = T.S[:, j]
    else:
        free.append(i)
free = np.array(free); fa, fb = new_sup[free[0]][0], new_sup[free[-1]][1]
tg = [np.linspace(fa, fb, 6000)]
for a, b in zip(new_knots[p:-p - 1], new_knots[p + 1:-p]):
    if b > a and b > fa and a < fb: tg.append(np.linspace(a, b, 14)[1:-1])
tg = np.unique(np.concatenate(tg)); tg = tg[(tg >= fa) & (tg <= fb)]
Y = T.eval(tg, 0)
Bfull = np.nan_to_num(BSpline(new_knots, np.eye(nb), p, extrapolate=False)(tg))
fixed = np.ones(nb, bool); fixed[free] = False
Yres = Y - Bfull[:, fixed] @ S_new[fixed]
t0 = time.time()
sol, res, rk, sv = np.linalg.lstsq(Bfull[:, free], Yres, rcond=None); S_new[free] = sol
print("free coefficients %d (supports within [%.4f, %.4f]); lstsq %d x %d with %d rhs: %.0fs, rank %d" % (len(free), fa, fb, Bfull.shape[0], len(free), Y.shape[1], time.time() - t0, rk), flush=True)
fit = Bfull @ S_new; dev = np.abs(fit - Y); base = np.abs(Y).max(1, keepdims=True)
inb = (tg >= t1) & (tg <= t2)
print("fit deviation / max_m|a_m(t)|: inside band max %.2e, outside band (within the free support) max %.2e" % ((dev[inb] / base[inb]).max(), (dev[~inb] / base[~inb]).max()))
print("mode 0 deviation inside band: max %.2e (a_0 ~ %.3e)" % (dev[inb, 0].max(), np.abs(Y[inb, 0]).max()))
d["knots"] = new_knots; d["S"] = S_new.T.copy()
np.savez_compressed(out, **d)
# check the joins at tmin and t0 (the new spline value and 6 derivatives vs the inner/outer representations)
T2 = Trial(dict(np.load(out)))
for tj in [T.tmin, T.t0]:
    e = 1e-9
    vin = np.array([T2.eval(np.array([tj - e if tj == T.tmin else tj + e]), nu)[0] for nu in range(7)])
    vmid = np.array([T2.eval(np.array([tj + e if tj == T.tmin else tj - e]), nu)[0] for nu in range(7)])
    print("join at t = %.4f: |jump| per order 0..6: %s" % (tj, " ".join("%.1e" % np.abs(vin[o] - vmid[o]).max() for o in range(7))))
