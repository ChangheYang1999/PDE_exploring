"""w-only finite-part B_3 (analysis.md 7.3) on an export (lead). Uses only c_l and w = W_1(x,0) on [0, x*]:
  g'/g = (w' - A)/w, g ~ x^2 (g0 = 1);  a2 = (g' - w'')/2;  b3 = -a2'/3;  then the b3_ls least-squares finite part.
Compares g_w with the exported G1 (the y^1 jet defect T1 integrated), and prints B_3 in natural units for
(i) w-only data, (ii) exported a2, b3, G1. Usage: python b3_wonly_export.py fields.npz"""
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
z, odd, even, fp_ls, cl, x = ns['z'], ns['odd'], ns['even'], ns['fp_ls'], ns['cl'], ns['x']
A = 2 * cl - 1
sel = z['axis_x'] < 40
w_s = CubicSpline(x ** 2, z['axis_w'][sel] / x)            # w = x S(x^2)
wp_s = CubicSpline(x ** 2, z['axis_w_prime'][sel])         # w' = T(x^2)
wf = lambda t: np.asarray(t) * w_s(np.asarray(t) ** 2)
wp = lambda t: wp_s(np.asarray(t) ** 2)
wpp = lambda t: 2 * np.asarray(t) * wp_s(np.asarray(t) ** 2, 1)
xs = brentq(wf, 1.0, 30.0)
# regular integrand e = (w' - A)/w - 2/x on a fine grid on (0, 1.3 x*), odd: e = x E(x^2)
xf = np.concatenate([np.geomspace(x[0], 0.05, 200), np.linspace(0.05, 1.3 * xs, 6000)[1:]])
xf = xf[np.abs(xf - xs) > 1e-3]
e = (wp(xf) - A) / wf(xf) - 2 / xf
Es = CubicSpline(xf ** 2, e / xf)
# log(g/x^2) = int_0^x t E(t^2) dt = (1/2) int_0^{x^2} E(s) ds
Ei = Es.antiderivative()
lg = lambda t: 0.5 * (Ei(np.asarray(t) ** 2) - Ei(0.0))
gw = lambda t: np.asarray(t) ** 2 * np.exp(lg(t))
gwp = lambda t: gw(t) * (wp(t) - A) / wf(t)
# avoid 0/0 at x*: build gp on the grid and spline (odd: gp = x G(x^2))
xg = xf[np.abs(xf - xs) > 2e-2]
gp_s = CubicSpline(xg ** 2, gwp(xg) / xg)
gwp_f = lambda t: np.asarray(t) * gp_s(np.asarray(t) ** 2)
a2w = lambda t: (gwp_f(t) - wpp(t)) / 2                  # odd
a2w_s = CubicSpline(xf ** 2, a2w(xf) / xf)
b3w = lambda t: -(a2w_s(np.asarray(t) ** 2) + 2 * np.asarray(t) ** 2 * a2w_s(np.asarray(t) ** 2, 1)) / 3
hw = lambda t: 2 * cl - wp(t)
G1 = z['axis_G1'][sel]
for t in (0.01, 1, 4, 8, 8.5):
    i = np.argmin(abs(x - t))
    print(f'x {x[i]:.4g}: g_w/G1 - 1 = {gw(x[i]) / G1[i] - 1: .3e}   a2_w {a2w(x[i]): .6f} a2_exp {z["axis_A2"][sel][i]: .6f}   b3_w {b3w(x[i]): .6f} b3_exp {z["axis_B3W"][sel][i]: .6f}')
print(f'x* = {xs:.8f}; natural unit x*^(2-p3) = {xs ** (-4 - 2 / A):.5e}')
d_w = AxisData(wf, hw, a2w, b3w, gw, gwp_f, cl, xs, ncheb=96)
d_e = AxisData(wf, hw, odd(z['axis_A2']), even(z['axis_B3W']), even(z['axis_G1'], 2), odd(z['axis_G1_prime']), cl, xs, ncheb=96)
for name, d in (('w-only', d_w), ('exported a2,b3,G1', d_e)):
    for delta in (0.3, 0.4, 0.5):
        row = [fp_ls(d, delta, deg) for deg in (8, 10, 12, 14, 16)]
        print(f'  {name:18s} delta {delta}: B3 natural (deg 8..16):', ' '.join(f'{v:.4f}' for v, _, _ in row),
              f' | fit {max(f for _, f, _ in row):.0e}')
