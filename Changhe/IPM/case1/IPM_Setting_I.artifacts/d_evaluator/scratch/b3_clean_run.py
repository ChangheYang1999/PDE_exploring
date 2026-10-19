import sys, io, contextlib, warnings, json
warnings.simplefilter("ignore")
import numpy as np
sys.path.insert(0, 'code')
from scipy.interpolate import CubicSpline
import vb3w
from vb3c import fp_clean
from vcand import load_modes
from vb3 import find_xstar, local_fit
L = 'b3_wonly_export.py'
field, Mmax, lf = sys.argv[1], int(sys.argv[2]), sys.argv[3]
argv0 = sys.argv; sys.argv = ['x', lf]
ns = {'__file__': L, '__name__': 'lead'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(L).read(), ns)
sys.argv = argv0
d = ns['d_w']
dd, g, ms, F = load_modes(field, Mmax)
c, cl, k, p, dp, ns2 = vb3w.inverse(g, F, Mmax)
A = 2 * cl - 1; p3 = 6 + 2 / A
tr = vb3w.w_traces(g, F, ms, p, dp, ns2, cl)
x, w = tr['x'], tr['w']
xs = find_xstar(x, w)
mu1 = float(local_fit(x, w, xs, 0.1 * xs).deriv()(0.0))
ax = vb3w.wonly(g, tr, cl, xs, mu1, 'wpp_fd')
be = 2 / A - 1; Nn = A ** (2 / A)
qd = ax['a2p'] / ax['G1'] ** 3 - 3 * ax['W1_2'] * ax['G1p'] / ax['G1'] ** 4
m = np.abs(w) / ax['G1']
q_cf = qd * m ** be * x ** (p3 - 1) / (3 * Nn)
sel = x < 1.2 * xs
cs = CubicSpline(np.log(x[sel]), q_cf[sel])
q_my = lambda t: cs(np.log(t))
q_ld = lambda t: (1 - t / d.xs) ** (d.beta - 1) * d.phi_x(t)
print('c_l %.10f x* %.8f eps %.2e (lead x* %.8f)' % (cl, xs, ax['eps'], d.xs))
res = {}
for name, qf, xx in (('mine', q_my, xs), ('lead_pipeline', q_ld, d.xs)):
    rows = []
    for u_lo, uc, K in ((0.03, 0.3, 5), (0.03, 0.3, 6), (0.04, 0.3, 6), (0.04, 0.4, 6), (0.06, 0.4, 6), (0.04, 0.4, 8),
                        (0.06, 0.5, 7), (0.02, 0.3, 6), (0.01, 0.3, 6), (0.005, 0.3, 8)):
        for ue, uf, ux, dE in ((0.8, 0.6, 0.97, 6), (0.8, 0.6, 0.95, 5), (0.9, 0.7, 0.98, 6), (0.7, 0.5, 0.93, 6)):
            o = fp_clean(qf, xx, p3, 2 / A, u_lo, uc, K, ue, uf, ux, dE)
            rows.append(dict(u_lo=u_lo, uc=uc, K=K, ue=ue, uf=uf, ux=ux, dE=dE, **o))
    res[name] = rows
    B = np.array([r['B'] for r in rows])
    outer = np.array([r['B'] for r in rows if r['u_lo'] >= 0.03])
    print(name, 'all: %.4f .. %.4f (median %.4f); u_lo >= 0.03: %.4f .. %.4f' % (B.min(), B.max(), np.median(B), outer.min(), outer.max()))
    for r in rows[::4]:
        print('   u_lo %.3f uc %.1f K %d | B %.4f (fp0 %.3f mid %.3f endp %.4f) fit0 %.0e fitE %.0e' % (r['u_lo'], r['uc'], r['K'], r['B'], r['fp0'], r['mid'], r['endp'], r['fit0'], r['fitE']))
    print('   end variants for (0.04,0.3,6):', ' '.join('%.4f' % r['B'] for r in rows[8:12]))
json.dump(res, open(sys.argv[4], 'w'), indent=0)
