import sys, json, warnings
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
print('c_l %.10f x* %.8f mu1 %.8f eps %.3e' % (cl, xs, mu1, ax['eps']))
be = 2 / A - 1; Nn = A ** (2 / A)
qd = ax['a2p'] / ax['G1'] ** 3 - 3 * ax['W1_2'] * ax['G1p'] / ax['G1'] ** 4
m = np.abs(w) / ax['G1']
q = qd * m ** be * x ** (p3 - 1) / (3 * Nn) * nat   # natural-unit scaled; f.p. int of x^{1-p3} q
for t in (1e-3, 1e-2, 0.05, 0.1, 0.3, 1, 2, 4):
    j = np.argmin(abs(x - t)); print('  t %.3g q %.12g' % (x[j], q[j]))
print('t_c   t_lo   K  B3nat(vb3 J-form)  B3nat(closed)  fit')
for tc in (0.005, 0.01, 0.02, 0.04, 0.08, 0.15, 0.3):
    for K in (2, 3, 4, 5, 6):
        for lo in (0.1, 0.25):
            try:
                o = b3(ax, t_lo_frac=tc * lo, t_c_frac=tc, K=K)
                cf = vb3w.closed_form(ax, cl, xs, t_lo_frac=tc * lo, t_c_frac=tc, K=K)
                print('%.3f  %.4f  %d  %9.4f  %9.4f  %.1e %.1e' % (tc, tc * lo, K, o['B3'] * nat, cf['B3'] * nat, o['fit_err'], cf['fit']))
            except Exception as e:
                print(tc, K, lo, 'fail', e)
