"""Manufactured test for vresid.evaluate: rho = x^2 y exp(-r^2) with the exact psi
psi = p2(r) sin 2t + p4(r) sin 4t, s = r^2,
p2 = (e^{-s}(s^2+s+1) - 1)/(8 s),  p4 = (e^{-s}(s^3+3s^2+6s+6) - 6)/(16 s^2),
so R_exact = (c_l X + U_exact).grad rho - rho is known in closed form for any c_l."""
import numpy as np
import sympy as sp
from vpolar import LogGrid
from vresid import evaluate, region_stats

rs = sp.symbols('r', positive=True)
s = rs ** 2
p2 = (sp.exp(-s) * (s ** 2 + s + 1) - 1) / (8 * s)
p4 = (sp.exp(-s) * (s ** 3 + 3 * s ** 2 + 6 * s + 6) - 6) / (16 * s ** 2)
fp = {n: (sp.lambdify(rs, p, 'mpmath'), sp.lambdify(rs, sp.diff(p, rs), 'mpmath')) for n, p in ((2, p2), (4, p4))}
import mpmath as mp
mp.mp.dps = 40


def pex(n, r):
    f, df = fp[n]
    return (np.array([float(f(mp.mpf(x))) for x in r]), np.array([float(df(mp.mpf(x))) for x in r]))


for N, Nt in ((400, 32), (800, 64), (1600, 64)):
    g = LogGrid(N, 1e-3, 12.0)
    th = 2 * np.pi * np.arange(Nt) / Nt
    r = g.r
    X = r[:, None] * np.cos(th)[None, :]
    Y = r[:, None] * np.sin(th)[None, :]
    rho = X ** 2 * Y * np.exp(-(X ** 2 + Y ** 2))
    cl = 1.3
    ev = evaluate(rho, g, th, c_l=cl, k_far=None)
    # exact
    P2, dP2 = pex(2, r)
    P4, dP4 = pex(4, r)
    psr = dP2[:, None] * np.sin(2 * th) + dP4[:, None] * np.sin(4 * th)
    pst = 2 * P2[:, None] * np.cos(2 * th) + 4 * P4[:, None] * np.cos(4 * th)
    R2 = r[:, None]
    Ur, Ut = -pst / R2, psr
    e = np.exp(-(X ** 2 + Y ** 2))
    rx = (2 * X * Y - 2 * X ** 3 * Y) * e
    ry = (X ** 2 - 2 * X ** 2 * Y ** 2) * e
    ct, st = np.cos(th)[None, :], np.sin(th)[None, :]
    rr_ = ct * rx + st * ry
    rt_ = R2 * (-st * rx + ct * ry)
    Rex = cl * R2 * rr_ + Ur * rr_ + Ut * rt_ / R2 - rho
    sel = slice(8, -8)
    dR = np.abs(ev.R - Rex)[sel].max()
    print(f"N={N} Nt={Nt}: c={ev.c:.15f} (exact 1/8, err {ev.c-0.125:.1e}); max|R-Rexact|={dR:.2e}, "
          f"max|Rexact|={np.abs(Rex).max():.2e}; max|E|={np.abs(ev.E[sel]).max():.2e}; "
          f"max|Ur-Urex|={np.abs(ev.Ur-Ur)[sel].max():.1e} parity_bad={ev.parity_bad:.1e}")
    print('   region stats r in [0.01,3]:', {k: f"{v:.2e}" for k, v in region_stats(ev, g, th, 0.01, 3).items()})
