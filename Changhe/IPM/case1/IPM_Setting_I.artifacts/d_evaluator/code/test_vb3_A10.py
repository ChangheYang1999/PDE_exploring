"""Accuracy of vb3.b3 at large A (c_l about 5.58, A about 10.15, p3 about 6.197), on the compatible axis family of
analysis.md 9.3 (w = -A x (1-u^2)/(1+u^2), g = x^2/(1+u^2), u = x/L), sampled on the log grid of the construct1 export.
Reference value: high-precision quadrature (mpmath) of the finite part, q(t) = J t^{p3-1} = F3/(A t^2 omega^{1-beta}
gamma^{3+beta}), omega = (1-u^2)/(1+u^2), gamma = 1/(1+u^2), beta = 2/A (H = t^{p3} gamma^{3+beta} omega^{-beta}, g0 = 1)."""
import numpy as np, sympy as sp, mpmath as mp, warnings
warnings.simplefilter("ignore")
from vb3 import b3
mp.mp.dps = 50
t, Ls, As = sp.symbols('t L A', positive=True)
u = t / Ls
w = -As * t * (1 - u ** 2) / (1 + u ** 2)
g = t ** 2 / (1 + u ** 2)
h = (As + 1) - sp.diff(w, t)
a2 = (sp.diff(g, t) - sp.diff(w, t, 2)) / 2
b3s = -sp.diff(a2, t) / 3
F3 = sp.cancel(sp.together(-a2 * sp.diff(g, t) - b3s * g))
F3t2 = sp.cancel(F3 / t ** 2)
fw, fh, fF = (sp.lambdify((t, As, Ls), e, 'numpy') for e in (w, h, F3))
qF = sp.lambdify((t, As, Ls), F3t2, 'mpmath')


def reference(A, L, tc_frac=0.3):
    A, L = mp.mpf(A), mp.mpf(L)
    be = 2 / A
    p3 = 6 + be
    def q(tt):
        uu = tt / L
        om = (1 - uu ** 2) / (1 + uu ** 2)
        ga = 1 / (1 + uu ** 2)
        return qF(tt, A, L) / (A * om ** (1 - be) * ga ** (3 + be))
    c = mp.taylor(q, 0, 12)
    tc = tc_frac * L
    s0 = L / 50
    # on [0, s0]: the remainder q - q0 - q2 s^2 - q4 s^4 by its Taylor series (orders 6 to 12), integrated exactly
    I0 = sum(c[k] * s0 ** (k + 2 - p3) / (k + 2 - p3) for k in range(6, 13, 2))
    I0 += mp.quad(lambda s: s ** (1 - p3) * (q(s) - c[0] - c[2] * s ** 2 - c[4] * s ** 4), [s0, tc])
    I0 += sum(c[k] * tc ** (k + 2 - p3) / (k + 2 - p3) for k in (0, 2, 4))
    tail_err = abs(c[12] * s0 ** (14 - p3))
    I1 = mp.quad(lambda s: s ** (1 - p3) * q(s), [tc, L * 0.9, L])
    return float(I0 + I1), float(p3)


h_grid = np.log(7652.0 / 7.652e-4) / 1535
for A in (10.15, 3.4):
    for L in (8.6, 3.0, 20.0):
        B_ref, p3 = reference(A, L)
        n = int(np.log(1.5 * L / 7.652e-4) / h_grid) + 1
        x = 7.652e-4 * np.exp(h_grid * np.arange(n))
        ax = dict(x=x, w=fw(x, A, L), h=fh(x, A, L), F3=fF(x, A, L), G3=np.full_like(x, 1e-300))
        res = []
        for tl, tc in ((0.01, 0.3), (0.02, 0.3), (0.01, 0.2), (0.005, 0.4)):
            o = b3(ax, t_lo_frac=tl, t_c_frac=tc)
            res.append(o['B3'])
        res = np.array(res)
        print('A %.2f L %5.1f  B3_ref %.10e  vb3 (4 windows) %s  max rel err %.2e' %
              (A, L, B_ref, np.array2string(res, precision=6), np.abs(res / B_ref - 1).max()))
