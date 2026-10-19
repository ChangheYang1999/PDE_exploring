import sys, warnings
warnings.simplefilter("ignore")
sys.path.insert(0, 'code')
import numpy as np
import vb3w
from vcand import load_modes
from vb3 import find_xstar, local_fit, b3
path, Mmax = sys.argv[1], int(sys.argv[2])
d, g, ms, F = load_modes(path, Mmax)
c, cl, k, p, dp, ns = vb3w.inverse(g, F, Mmax)
A = 2 * cl - 1; p3 = 6 + 2 / A
tr = vb3w.w_traces(g, F, ms, p, dp, ns, cl)
x, w = tr['x'], tr['w']
xs = find_xstar(x, w)
mu1 = float(local_fit(x, w, xs, 0.1 * xs).deriv()(0.0))
nat = xs ** (p3 - 2)
ax = vb3w.wonly(g, tr, cl, xs, mu1, 'wpp_fd')
print('c_l %.10f x* %.8f' % (cl, xs))
print('windows with t_lo outside the origin layer (0.153 physical = 0.0178 x*)')
for lo in (0.03, 0.04, 0.06, 0.08):
    for tc in (0.3, 0.4, 0.5):
        row = []
        for K in (5, 6, 7, 8, 10, 12):
            try:
                cf = vb3w.closed_form(ax, cl, xs, t_lo_frac=lo, t_c_frac=tc, K=K)
                row.append('%8.3f(%.0e)' % (cf['B3'] * nat, cf['fit']))
            except Exception as e:
                row.append('fail')
        print('lo %.2f tc %.1f K5..12:' % (lo, tc), ' '.join(row))
