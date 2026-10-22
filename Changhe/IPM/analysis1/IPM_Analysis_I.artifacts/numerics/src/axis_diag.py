"""Lead's diagnostic (18:09Z addendum), floating point: d_x^j d_y rho~(x, 0) for j = 0..4 near x_*, from the exact representation
rho~_y(x, 0) = x^2 S(t), S = sum_m a_m(t), t = log x; d_x^j via d_x = e^{-t} d_t (Stirling numbers of the first kind).
Also finite-difference check of d_x^4 d_y rho on X3's own formula (src/x3.py) if available.
Usage: python3 axis_diag.py trial.npz
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
XS = 8.600063805157177
T = Trial(np.load(sys.argv[1]))
# d_x^j = e^{-jt} sum_i s(j,i) d_t^i  with signed Stirling numbers of the first kind
St = {1: {1: 1}, 2: {1: -1, 2: 1}, 3: {1: 2, 2: -3, 3: 1}, 4: {1: -6, 2: 11, 3: -6, 4: 1}}
def dxj_of(F, t, j):
    """F(t, nu) -> d_t^nu F; returns d_x^j F at t."""
    if j == 0: return F(t, 0)
    return np.exp(-j * t) * sum(c * F(t, i) for i, c in St[j].items())
def G(t, nu):
    # G(t) = e^{2t} S(t); d_t^nu by Leibniz
    from math import comb
    return sum(comb(nu, l) * 2.0 ** (nu - l) * np.exp(2 * t) * T.eval(t, l).sum(1) for l in range(nu + 1))
for side in [-1, 1]:
    print("side %+d: s = x - x_*" % side)
    ss = side * np.array([0.05, 0.03, 0.02, 0.01, 0.006, 0.003, 0.002, 0.001, 5e-4, 2e-4, 1e-4, 5e-5, 2e-5, 1e-5])
    x = XS + ss; t = np.log(x)
    vals = np.stack([dxj_of(G, t, j) for j in range(5)], 1)
    for i in range(len(ss)):
        print("  s=%+.1e  d_y rho=%.8f  d_x d_y=%.6f  d_x^2 d_y=%.6f  d_x^3 d_y=%.5f  d_x^4 d_y=%.4f" % (ss[i], *vals[i]))
    # log-log slopes of |d_x^3 d_y rho - value at s->0| etc. (layer prediction: d_x^3 d_y ~ |s|^{-0.07}, d_x^4 d_y ~ |s|^{-1.07})
    a3 = np.abs(vals[:, 3]); a4 = np.abs(vals[:, 4])
    sl3 = np.diff(np.log(a3)) / np.diff(np.log(np.abs(ss))); sl4 = np.diff(np.log(a4)) / np.diff(np.log(np.abs(ss)))
    print("  log-log slopes of |d_x^3 d_y| between consecutive s:", np.round(sl3, 3))
    print("  log-log slopes of |d_x^4 d_y| between consecutive s:", np.round(sl4, 3))
# knots near x_*
kn = np.exp(T.knots[T.p + 1:-(T.p + 1)]); kn = kn[(kn > XS - 0.1) & (kn < XS + 0.1)]
print("trial knots (r) within 0.1 of x_*:", np.round(kn - XS, 5))
# X3's own axis function by finite differences (its own spline in q): d_y rho_X3(x, 0) = x^2 e^{H(x,0)}
try:
    from x3 import X3
    X = X3()
    def gy(x):
        F = X.rho(np.atleast_1d(x), np.array([1e-9]))     # rho at tiny theta ~ y * d_y rho
        return F["rho"][:, 0] / (np.atleast_1d(x) * 1e-9)
    for h in [2e-3, 1e-3, 5e-4]:
        pts = np.arange(-3, 4) * h
        V = np.vander(pts, increasing=True).T
        import math
        for j in [3, 4]:
            w = np.linalg.solve(V, np.eye(7)[j] * math.factorial(j))
            for s in [0.05, 0.01, 0.003]:
                for side in [-1, 1]:
                    x0 = XS + side * s
                    fd = sum(wi * gy(x0 + pi)[0] for wi, pi in zip(w, pts))
                    tr = dxj_of(G, np.array([np.log(x0)]), j)[0]
                    print("  X3 FD(h=%.0e) d_x^%d d_y rho at s=%+.3f: %.5f   trial exact: %.5f" % (h, j, side * s, fd, tr))
except Exception as e:
    print("X3 comparison skipped:", e)
