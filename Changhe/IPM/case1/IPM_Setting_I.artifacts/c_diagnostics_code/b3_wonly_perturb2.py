"""Companion to b3_wonly_perturb.py (lead): (1) w-only B_3 for each construct1 export (radial degree 80, 120, 160, 200) and
the change of w between exports after removing the uniform factor (w scales with A = 2 c_l - 1); (2) response of the
w-only B_3 to a relative perturbation of w localized near P: w -> w (1 + eps exp(-((x - x*)/sigma)^2)), sigma = 0.5, 1.
Usage: python b3_wonly_perturb2.py"""
import sys
import numpy as np
from scipy.interpolate import CubicSpline
here = __file__.rsplit('/', 1)[0]
C1 = here + '/../astra/construct1/'
src = open(here + '/b3_wonly_perturb.py').read().split("xs, base = b3_w(W0, WP0)")[0]
res = {}
for f in ('spline80_preliminary_fields.npz', 'spline120_preliminary_fields.npz', 'spline160_refined_fields.npz',
          'final_candidate.npz'):
    sys.argv = ['x', C1 + f]
    ns = {'__file__': here + '/b3_wonly_perturb.py'}
    exec(src, ns)
    xs, b = ns['b3_w'](ns['W0'], ns['WP0'])
    res[f] = (ns['x'], ns['W0'], ns['A'], xs, b)
    print(f'{f:34s} c_l {ns["cl"]:.7f} x* {xs:.6f} B3 natural:', ' '.join(f'{v:.4f}' for v in b.values()))
xr, wr, Ar, _, _ = res['final_candidate.npz']
S = CubicSpline(xr ** 2, wr / xr / Ar)
for f, (x, w, A, xs, b) in res.items():
    if f == 'final_candidate.npz':
        continue
    Sf = CubicSpline(x ** 2, w / x / A)
    d = np.array([Sf(t * t) / S(t * t) - 1 for t in (0.01, 0.05, 0.15, 0.5, 1.5, 4, 8)])
    print(f'  (w/A) change vs final, {f}: ' + ' '.join(f'{v: .1e}' for v in d), ' at x = 0.01 0.05 0.15 0.5 1.5 4 8')
ns_last = ns
x, W0, WP0, xs = ns_last['x'], ns_last['W0'], ns_last['WP0'], res['final_candidate.npz'][3]
base = res['final_candidate.npz'][4]
for sig in (0.5, 1.0):
    eps = 1e-6
    ph = np.exp(-((x - xs) / sig) ** 2)
    dph = -2 * (x - xs) / sig ** 2 * ph
    _, b = ns_last['b3_w'](W0 * (1 + eps * ph), WP0 * (1 + eps * ph) + W0 * eps * dph)
    print(f'near-P perturbation sigma {sig}, eps 1e-6: dB3 natural', ' '.join(f'{b[k] - base[k]: .2e}' for k in b))
