"""Prototype: how dense must the degree-7 B-spline knots in t = log r be to fit the cosine modes a_m(t) of e^H
to ~1e-13 relative? Knots: X3's q-knots mapped to t, plus uniform knots below X3's first knot, each interval
subdivided 'sub' times. Fit by least squares on the dense grid, validate on an independent shifted grid."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import BSpline
from scipy.fft import dct
from x3 import X3

X = X3(); L = X.L; k = X.k
d = np.load("data/x3_modes_N24000_q4096_M300.npz")
t = d["t"]; A = d["A"]; r = d["r"]
# X3 knots in t
qk = X.knots[X.order + 1:-(X.order + 1)]           # interior knots (strictly inside (0,1))
uk = np.sqrt((1 - qk) ** (-2 / (1 - k)) - 1); tk = np.log(L * uk)
print("X3 interior knots: %d, first r = %.4g, last r = %.4g (= %.1f L); median dt = %.4f, min dt = %.4f, max dt = %.4f" % (
    len(qk), L * uk[0], L * uk[-1], uk[-1], np.median(np.diff(tk)), np.diff(tk).min(), np.diff(tk).max()))
rmin = 1e-3 * L; R0 = L * uk[-1]
tmin, tmax = np.log(rmin), np.log(R0)
sel = (t >= tmin) & (t <= tmax)
ts, As = t[sel], A[sel]
# validation grid: midpoints between sample points
tv = 0.5 * (ts[:-1] + ts[1:]); rv = np.exp(tv)
th = np.linspace(0, np.pi / 2, 4097)
Hv = X.H(rv, th, derivs=False); cv = dct(np.exp(Hv), type=1, axis=1) / 4096; cv[:, 0] *= 0.5
modes = [0, 1, 2, 5, 20, 100, 200, 250]
base = (1 + (rv / L) ** 2) ** ((k - 3) / 2)            # weight for relative error
for sub in (1, 2, 4, 8):
    # knots: uniform from tmin to tk[0] with spacing ~ (tk[1]-tk[0])/sub ... use spacing 0.05/sub there
    inner = np.arange(tmin, tk[0], 0.05 / sub)[1:]
    mid = []
    for a, b in zip(tk[:-1], tk[1:]):
        mid.extend(np.linspace(a, b, sub + 1)[:-1])
    mid.append(tk[-1])
    knots_int = np.r_[inner, mid]
    knots_int = knots_int[(knots_int > tmin) & (knots_int < tmax)]
    kn = np.r_[np.full(8, tmin), knots_int, np.full(8, tmax)]
    nb = len(kn) - 8
    t0 = time.time()
    D = BSpline(kn, np.eye(nb), 7, extrapolate=False)(ts)      # (Ns, nb) dense
    D = np.nan_to_num(D)
    w = 1 / (1 + (np.exp(ts) / L) ** 2) ** ((k - 3) / 2)       # relative weighting
    Dw = D * w[:, None]
    Q, R = np.linalg.qr(Dw)
    coef = np.linalg.solve(R, Q.T @ (As[:, modes] * w[:, None]))
    Dv = np.nan_to_num(BSpline(kn, np.eye(nb), 7, extrapolate=False)(tv))
    fitv = Dv @ coef
    err = np.abs(fitv - cv[:, modes]) / base[:, None]
    errA0 = np.abs(fitv - cv[:, modes]) / np.abs(cv[:, [0]])
    print("sub=%d: %d basis functions, %d samples, %.1fs; max rel err (vs base) per mode %s ; max rel err vs a_0: %s" % (
        sub, nb, len(ts), time.time() - t0, " ".join("%.1e" % e for e in err.max(0)), " ".join("%.1e" % e for e in errA0.max(0))))
    i = np.argmax(err[:, 0]); print("     worst location mode 0: r = %.4g" % rv[i])
