import sys, warnings
warnings.simplefilter("ignore")
sys.path.insert(0, 'code')
import numpy as np
import vb3w
from vcand import load_modes
from vb3 import find_xstar, local_fit, axis_traces
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
be = 2 / A - 1; Nn = A ** (2 / A)
qd = ax['a2p'] / ax['G1'] ** 3 - 3 * ax['W1_2'] * ax['G1p'] / ax['G1'] ** 4
m = np.abs(w) / ax['G1']
q = qd * m ** be * x ** (p3 - 1) / (3 * Nn) * nat
print('r0 %.4g R %.4g N %d' % (x[0], x[-1], len(x)))
# reference even fit on [0.05, 0.5]
sel = (x > 0.05) & (x < 0.6)
cf = np.polyfit(x[sel] ** 2, q[sel], 4)
print('even fit [0.05,0.6] coeffs (high->low)', cf)
for t in np.geomspace(x[0], 3, 40):
    j = np.argmin(abs(x - t))
    print('  t %.4g  q %.10f  q-fit %.3e  w/x+A %.6e  a2/x %.8f  gw/x^2-1 %.3e' % (x[j], q[j], q[j] - np.polyval(cf, x[j] ** 2), w[j] / x[j] + A, ax['W1_2'][j] / x[j], ax['G1'][j] / x[j] ** 2 - 1))
