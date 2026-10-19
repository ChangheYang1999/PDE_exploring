"""Sensitivity of the w-only finite-part B_3 (b3_wonly_export.py) to a localized relative perturbation of w (lead).
w -> w (1 + eps phi(x/l)), phi(s) = s^2 exp(-s^2) (even, so w stays odd; w' perturbed consistently).
Compares the change of B_3 (natural units) with the estimate eps (l/x*)^(2-p3)/A of analysis.md 3.5(b).
Usage: python b3_wonly_perturb.py fields.npz"""
import sys
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
here = __file__.rsplit('/', 1)[0]
sys.path.insert(0, here)
from b3_diag import AxisData
src = open(here + '/b3_ls.py').read().split("wf = odd(z['axis_w'])")[0]
ns = {'__file__': here + '/b3_ls.py'}
exec(src, ns)
z, fp_ls, cl, x = ns['z'], ns['fp_ls'], ns['cl'], ns['x']
A = 2 * cl - 1
sel = z['axis_x'] < 40
W0, WP0 = z['axis_w'][sel], z['axis_w_prime'][sel]


def b3_w(Wv, WPv):
    w_s = CubicSpline(x ** 2, Wv / x)
    wp_s = CubicSpline(x ** 2, WPv)
    wf = lambda t: np.asarray(t) * w_s(np.asarray(t) ** 2)
    wp = lambda t: wp_s(np.asarray(t) ** 2)
    wpp = lambda t: 2 * np.asarray(t) * wp_s(np.asarray(t) ** 2, 1)
    xs = brentq(wf, 1.0, 30.0)
    xf = np.concatenate([np.geomspace(x[0], 0.05, 200), np.linspace(0.05, 1.3 * xs, 6000)[1:]])
    xf = xf[np.abs(xf - xs) > 1e-3]
    e = (wp(xf) - A) / wf(xf) - 2 / xf
    Ei = CubicSpline(xf ** 2, e / xf).antiderivative()
    lg = lambda t: 0.5 * (Ei(np.asarray(t) ** 2) - Ei(0.0))
    gw = lambda t: np.asarray(t) ** 2 * np.exp(lg(t))
    gwp = lambda t: gw(t) * (wp(t) - A) / wf(t)
    xg = xf[np.abs(xf - xs) > 2e-2]
    gp_s = CubicSpline(xg ** 2, gwp(xg) / xg)
    gwp_f = lambda t: np.asarray(t) * gp_s(np.asarray(t) ** 2)
    a2w = lambda t: (gwp_f(t) - wpp(t)) / 2
    a2w_s = CubicSpline(xf ** 2, a2w(xf) / xf)
    b3w = lambda t: -(a2w_s(np.asarray(t) ** 2) + 2 * np.asarray(t) ** 2 * a2w_s(np.asarray(t) ** 2, 1)) / 3
    hw = lambda t: 2 * cl - wp(t)
    d = AxisData(wf, hw, a2w, b3w, gw, gwp_f, cl, xs, ncheb=96)
    return xs, {(dl, dg): fp_ls(d, dl, dg)[0] for dl in (0.4, 0.5) for dg in (10, 12, 14)}


xs, base = b3_w(W0, WP0)
p3 = 6 + 2 / A
print(f'x* = {xs:.6f}; base B3 natural:', ' '.join(f'{k}:{v:.4f}' for k, v in base.items()))
for l in (0.15, 0.5, 1.5, 4.0):
    for eps in (1e-8, 1e-6):
        s = x / l
        phi, dphi = s ** 2 * np.exp(-s ** 2), (2 * s - 2 * s ** 3) * np.exp(-s ** 2) / l
        Wv = W0 * (1 + eps * phi)
        WPv = WP0 * (1 + eps * phi) + W0 * eps * dphi
        _, b = b3_w(Wv, WPv)
        dB = {k: b[k] - base[k] for k in b}
        est = eps * (l / xs) ** (2 - p3) / A
        print(f'l {l:5.2f} eps {eps:.0e}: dB3 natural', ' '.join(f'{v: .2e}' for v in dB.values()), f' | estimate {est:.1e}')
