"""Manufactured test of vb3.b3: x* = 1, w = A x (x^2-1)/(1+x^2), h = A + 1 - w' (so w' + h = 2c_l, mu1 = A, mu2 = 1),
H = x^p3 (1-x^2)^(-2/A) (1+x^2)^(-3) exactly, G3 = x^2 e^{-x^2} + B chi(x) H with chi = 1 on [0,0.3], 0 on [0.9,inf),
F3 := w G3' + (3h-1) G3. The bounded solution is G3 itself and its |x|^p3 coefficient is B exactly."""
import sys, json
import numpy as np
KW = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
from vpolar import LogGrid
from vb3 import b3

def step(t):
    f = lambda s: np.where(s > 0, np.exp(-1 / np.maximum(s, 1e-300)), 0.0)
    return f(1 - t) / (f(1 - t) + f(t))      # 1 for t<=0, 0 for t>=1

for cl in (1.3, 1.5, 2.2):
    A = 2 * cl - 1
    p3 = 6 + 2 / A
    for N in (1200, 2400):
        g = LogGrid(N, 1e-5, 10.0)
        x = g.r
        w = A * x * (x ** 2 - 1) / (1 + x ** 2)
        wp = A * ((3 * x ** 2 - 1) * (1 + x ** 2) - 2 * x ** 2 * (x ** 2 - 1)) / (1 + x ** 2) ** 2
        h = A + 1 - wp
        with np.errstate(all='ignore'):
            H = x ** p3 * np.abs(1 - x ** 2) ** (-2 / A) * (1 + x ** 2) ** (-3)
            Hp = H * (1 - 3 * h) / w
        t = (x - 0.32) / 0.46
        chi = step(t)
        f = lambda s: np.where(s > 0, np.exp(-1 / np.maximum(s, 1e-300)), 0.0)
        # chi' by complex-step-free finite difference in t (analytic enough at 1e-7 step)
        dt = 1e-6
        chip = (step(t + dt) - step(t - dt)) / (2 * dt) / 0.46
        B = 0.7
        gs = x ** 2 * np.exp(-x ** 2)
        gsp = (2 * x - 2 * x ** 3) * np.exp(-x ** 2)
        with np.errstate(all='ignore'):
            G3 = gs + B * np.where(chi > 0, chi * H, 0.0)
            F3 = w * gsp + (3 * h - 1) * gs + B * np.where(np.abs(chip) > 0, H * w * chip, 0.0)
        ax = dict(x=x, w=w, h=h, F3=F3, G3=G3)
        o = b3(ax, **KW)
        print(f"c_l={cl} N={N}: x*={o['x_star']:.12f} mu1={o['mu1']:.8f} (A={A}) mu2={o['mu2']:.10f} p3={o['p3']:.8f} "
              f"(exact {p3:.8f}) B3={o['B3']:.10f} (exact {B}) err={o['B3']-B:.1e}; pieces fp0={o['fp0']:.4e} "
              f"mid={o['mid']:.4e} end={o['endp']:.4e}; hybrid={[round(v, 9) for v in o['hybrid']]} fit_err={o['fit_err']:.1e}")
