"""Sensitivity of the w-only B_3 (integrated-by-parts estimator, b3_ibp.py) to perturbations of the axis velocity w.
Base data: construct1 final_candidate.npz (axis_w, axis_w_prime). Perturbation w -> w + eps * W0 * phi(x), W0 = max |w| on
[0, x*], phi with phi(x) = O(x^3) at 0 (keeps w'(0) = -A), max |phi| = 1 on [0, 1.3 x*]. x* is recomputed (brentq),
c_l is held fixed. Prints dB_3 / eps in natural units for eps = 1e-6 and 1e-5 (linearity check), estimator settings
fixed (xc 0.4, xlo 0.05, K 9, n 80) and the 16-setting median.
Families: P_j(x) = (x/x*)^3 T_j(x/x*) (Chebyshev, smooth global), G(x0, s) = (x/x*)^3 exp(-((x - x0)/s)^2) normalized
(localized bumps), and dc_l: c_l -> c_l + eps with w fixed.
Usage: python3 sens.py [fields.npz]"""
import sys
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from b3_ibp import WOnly, b3_both

f = sys.argv[1] if len(sys.argv) > 1 else 'final_candidate.npz'
z = np.load(f)
cl0 = float(z['c_l'])
x = z['axis_x']; sel = x < 40; x = x[sel]
ws_ = CubicSpline(x ** 2, z['axis_w'][sel] / x)
wps = CubicSpline(x ** 2, z['axis_w_prime'][sel])
w0 = lambda t: np.asarray(t) * ws_(np.asarray(t) ** 2)
wp0 = lambda t: wps(np.asarray(t) ** 2)
wpp0 = lambda t: 2 * np.asarray(t) * wps(np.asarray(t) ** 2, 1)
xs0 = brentq(w0, 1.0, 30.0)
xx = np.linspace(0, xs0, 4001)
W0 = np.max(np.abs(w0(xx)))


def b3(w, wp, wpp, cl, grid=False):
    xs = brentq(w, 0.5 * xs0, 1.5 * xs0)
    d = WOnly(w, wp, wpp, cl, xs, Ag='mu1')
    nat = xs ** (d.p3 - 2)
    if not grid:
        return b3_both(d, 0.4 * xs, 0.05 * xs, 9, 80)[1] * nat
    v = [b3_both(d, xc * xs, xlo * xs, K, n)[1] * nat for xc in (0.3, 0.4) for xlo in (0.03, 0.05) for K in (7, 9)
         for n in (40, 80)]
    return float(np.median(v))


def family(phi, dphi, ddphi):
    # normalize max |phi| on [0, 1.3 x*]
    t = np.linspace(0, 1.3 * xs0, 6001)
    s = 1.0 / np.max(np.abs(phi(t)))
    return (lambda x: s * phi(x)), (lambda x: s * dphi(x)), (lambda x: s * ddphi(x))


def cheb(j):
    T = np.polynomial.chebyshev.Chebyshev.basis(j)
    P = np.polynomial.Polynomial([0, 0, 0, 1]) * T.convert(kind=np.polynomial.Polynomial)
    P = P(np.polynomial.Polynomial([0, 1 / xs0]))
    return P, P.deriv(), P.deriv(2)


def gauss(x0, sg):
    def phi(x):
        x = np.asarray(x); return (x / xs0) ** 3 * np.exp(-((x - x0) / sg) ** 2)
    def dphi(x):
        x = np.asarray(x); e = np.exp(-((x - x0) / sg) ** 2)
        return (3 * x ** 2 / xs0 ** 3 - (x / xs0) ** 3 * 2 * (x - x0) / sg ** 2) * e
    def ddphi(x, h=1e-5):
        return (dphi(np.asarray(x) + h) - dphi(np.asarray(x) - h)) / (2 * h)
    return phi, dphi, ddphi


B0 = b3(w0, wp0, wpp0, cl0); B0g = b3(w0, wp0, wpp0, cl0, grid=True)
print(f'{f}: c_l {cl0:.8f} x* {xs0:.6f} max|w| on [0,x*] {W0:.4f}; B_3 (fixed setting) {B0:.5f}, median {B0g:.5f}')
cases = [(f'cheb T{j}', cheb(j)) for j in range(0, 9)]
cases += [(f'bump x0={x0:.2f}x* s={sg:.2f}x*', gauss(x0 * xs0, sg * xs0)) for x0, sg in
          [(0.05, 0.03), (0.1, 0.05), (0.2, 0.05), (0.4, 0.1), (0.6, 0.1), (0.8, 0.05), (0.95, 0.03), (1.0, 0.05)]]
for name, (phi, dphi, ddphi) in cases:
    phi, dphi, ddphi = family(phi, dphi, ddphi)
    out = []
    for eps in (1e-6, 1e-5):
        a = eps * W0
        w = lambda t, a=a: w0(t) + a * phi(t)
        wp = lambda t, a=a: wp0(t) + a * dphi(t)
        wpp = lambda t, a=a: wpp0(t) + a * ddphi(t)
        out.append((b3(w, wp, wpp, cl0) - B0) / eps)
    a = 1e-5 * W0
    Bg = b3(lambda t: w0(t) + a * phi(t), lambda t: wp0(t) + a * dphi(t), lambda t: wpp0(t) + a * ddphi(t), cl0, grid=True)
    print(f'  {name:28s} dB3/eps: eps 1e-6 {out[0]: .4e}  eps 1e-5 {out[1]: .4e}  (median-setting, eps 1e-5: {(Bg - B0g) / 1e-5: .4e})')
for eps in (1e-6, 1e-5):
    print(f'  dc_l (w fixed)               eps {eps:.0e}: dB3/eps {(b3(w0, wp0, wpp0, cl0 + eps) - B0) / eps: .4e}')
