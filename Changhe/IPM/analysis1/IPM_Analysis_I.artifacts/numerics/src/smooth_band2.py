"""Mode-range smoothing diagnostic (floating): on the band t in [t1, t2], project the modes m in [m_lo, m_hi) onto the coarse spline
space whose knots are every `stride`-th original knot (a subspace of the original spline space), and re-express the result on the
ORIGINAL knot vector (exact up to roundoff). Other modes and the coefficients outside the band are unchanged.
Usage: python3 smooth_band2.py trial.npz t1 t2 stride m_lo m_hi out.npz
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import BSpline
from modal_fit import Trial

path, t1, t2, stride, m_lo, m_hi, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
d = dict(np.load(path)); T = Trial(d); p = T.p; kn = T.knots; kin = kn[p + 1:-(p + 1)]
inband = np.where((kin >= t1) & (kin <= t2))[0]
keep_idx = np.r_[np.arange(0, inband[0]), inband[::stride], np.arange(inband[-1] + 1, len(kin))]
if inband[-1] not in keep_idx: keep_idx = np.r_[keep_idx[keep_idx <= inband[-1]], inband[-1], keep_idx[keep_idx > inband[-1]]]
keep_idx = np.unique(keep_idx)
cknots = np.r_[np.full(p + 1, T.tmin), kin[keep_idx], np.full(p + 1, T.t0)]
lo, hi = kin[inband[0]], kin[inband[-1]]
print("band knots %d -> %d coarse (spacing ~%.4f in t); modes [%d, %d)" % (len(inband), len(inband[::stride]), (hi - lo) / max(len(inband[::stride]) - 1, 1), m_lo, m_hi), flush=True)
# fit grid over the affected region (coarse basis functions meeting (lo, hi))
nbc = len(cknots) - p - 1
csup = [(cknots[i], cknots[i + p + 1]) for i in range(nbc)]
cfree = [i for i in range(nbc) if not (csup[i][1] <= lo + 1e-12 or csup[i][0] >= hi - 1e-12)]
fa, fb = csup[cfree[0]][0], csup[cfree[-1]][1]
cells = np.unique(cknots); cells = cells[(cells >= fa) & (cells <= fb)]
tg = np.unique(np.concatenate([np.linspace(a, b, 16) for a, b in zip(cells[:-1], cells[1:])]))
Y = T.eval(tg, 0)[:, m_lo:m_hi]
Bc = np.nan_to_num(BSpline(cknots, np.eye(nbc), p, extrapolate=False)(tg))
# fixed part: coarse functions not free are exactly original fine functions? Not in general (knot removal changes functions near the
# band edges); so fit the whole coarse space on the fit grid for the affected region, then re-express on the fine knots.
sol = np.linalg.lstsq(Bc, Y, rcond=None)[0]
# preserve the strain functional c[rho] = int e^{2t} (a_0/4 + a_1/8 - a_2/8 - a_3/8) dt exactly (one linear constraint on modes 0-3):
# Lagrange correction S_m -> S_m + lam * w_m * N^{-1} g, g_i = int_{affected region} e^{2t} N_i(t) dt (quadrature on the fit grid)
wts = {0: 0.25, 1: 0.125, 2: -0.125, 3: -0.125}
modes_c = [m for m in range(m_lo, m_hi) if m in wts]
if modes_c:
    tq = np.linspace(tg.min(), tg.max(), 40001); dq = tq[1] - tq[0]
    Bq = np.nan_to_num(BSpline(cknots, np.eye(nbc), p, extrapolate=False)(tq))
    g = (np.exp(2 * tq)[:, None] * Bq).sum(0) * dq
    Yq = T.eval(tq, 0)
    c_old = sum(wts[m] * (np.exp(2 * tq) * Yq[:, m]).sum() * dq for m in modes_c)
    c_new = sum(wts[m] * (g @ sol[:, m - m_lo]) for m in modes_c)
    Bf = Bc[:, cfree]; gf = g[cfree]
    Ngf = np.linalg.solve(Bf.T @ Bf, gf)
    denom = sum(wts[m] ** 2 for m in modes_c) * (gf @ Ngf)
    lam = (c_old - c_new) / denom
    for m in modes_c: sol[cfree, m - m_lo] += lam * wts[m] * Ngf
    c_chk = sum(wts[m] * (g @ sol[:, m - m_lo]) for m in modes_c)
    print("strain functional on the affected region: original %.10e, unconstrained fit %.10e (change %.3e), constrained %.10e (change %.1e)" % (c_old, c_new, c_new - c_old, c_chk, c_chk - c_old), flush=True)
smooth_vals = Bc @ sol
dev = np.abs(smooth_vals - Y); print("coarse-fit deviation on the band: max %.3e (max_m|a_m| %.3e)" % (dev[(tg >= t1) & (tg <= t2)].max(), np.abs(Y).max()), flush=True)
# re-express on the original fine knot vector: fit the fine basis functions meeting [fa, fb] to the smoothed values (exact: subspace)
nb = len(kn) - p - 1
fsup = [(kn[i], kn[i + p + 1]) for i in range(nb)]
ffree = [i for i in range(nb) if fsup[i][0] >= fa - 1e-12 and fsup[i][1] <= fb + 1e-12]     # supports INSIDE [fa, fb]: the change vanishes outside
Bf = np.nan_to_num(BSpline(kn, np.eye(nb), p, extrapolate=False)(tg))
fixed = np.ones(nb, bool); fixed[ffree] = False
S = d["S"].copy()
rhs = smooth_vals - Bf[:, fixed] @ S[m_lo:m_hi][:, fixed].T
coef = np.linalg.lstsq(Bf[:, ffree], rhs, rcond=None)[0]
S[m_lo:m_hi, :][:, ffree] = coef.T
rep = Bf @ S[m_lo:m_hi].T
print("re-expression error on the fine knots: max %.2e" % np.abs(rep - smooth_vals).max())
d["S"] = S; np.savez_compressed(out, **d)
T2 = Trial(dict(np.load(out)))
chk = np.abs(T2.eval(tg, 0)[:, m_lo:m_hi] - smooth_vals).max()
tout = np.r_[np.linspace(T.tmin, fa, 400), np.linspace(fb, T.t0, 400)]
chk_out = np.abs(T2.eval(tout, 0) - T.eval(tout, 0)).max()
print("check: new trial vs smoothed values on the region max %.2e; change OUTSIDE [fa, fb] max %.2e; saved %s" % (chk, chk_out, out))
