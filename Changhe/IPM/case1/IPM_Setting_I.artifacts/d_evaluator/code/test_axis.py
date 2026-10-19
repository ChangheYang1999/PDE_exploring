"""Check vb3.axis_traces against analytic fields: rho = x^2 y e^{-x^2-2y^2} (G1 = x^2 e^{-x^2}, G3 = -2 x^2 e^{-x^2}),
psi = x y e^{-x^2-2y^2} (Psi1 = x e^{-x^2}, Psi3 = -2 x e^{-x^2})."""
import numpy as np
from vpolar import LogGrid
from vb3 import axis_traces

for M in (31, 63):
    g = LogGrid(800, 1e-3, 6.0)
    r = g.r
    Nt = 4 * (M + 1)
    th = 2 * np.pi * np.arange(Nt) / Nt
    X = r[:, None] * np.cos(th)[None, :]
    Y = r[:, None] * np.sin(th)[None, :]
    E = np.exp(-X ** 2 - 2 * Y ** 2)
    rho, psi = X ** 2 * Y * E, X * Y * E
    ms = np.arange(1, M + 1, 2)
    ns = np.arange(2, M + 2, 2)
    S = lambda k: np.sin(np.outer(th, k)) * (2.0 / Nt)
    F = (rho @ S(ms)).T
    P = (psi @ S(ns)).T
    dP = g.du(P.T).T / r
    ax = axis_traces(F, ms, P, dP, ns, r, 1.4, g.du)
    x = r
    ex = dict(G1=x ** 2 * np.exp(-x ** 2), G3=-2 * x ** 2 * np.exp(-x ** 2))
    Psi1 = x * np.exp(-x ** 2)
    Psi3 = -2 * x * np.exp(-x ** 2)
    Psi1p = (1 - 2 * x ** 2) * np.exp(-x ** 2)
    Psi3p = -2 * Psi1p
    G1p = (2 * x - 2 * x ** 3) * np.exp(-x ** 2)
    ex.update(w=1.4 * x - Psi1, h=1.4 + Psi1p, W1_2=-3 * Psi3, W2_3=Psi3p, G1p=G1p,
              F3=3 * Psi3 * G1p - Psi3p * ex['G1'])
    for sel_name, sel in (('r in [0.01,0.1]', (x > 0.01) & (x < 0.1)), ('r in [0.1,3]', (x > 0.1) & (x < 3))):
        errs = {k: float(np.abs(ax[k][sel] - v[sel]).max() / np.abs(v[sel]).max()) for k, v in ex.items()}
        print(M, sel_name, ' '.join(f'{k}={e:.1e}' for k, e in errs.items()))
