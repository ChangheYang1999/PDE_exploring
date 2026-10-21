"""Fit an exactly compatible analytic reference w_0(u) = -A u (1 - u^2)/(1 + u^2) + u^3 (1 - u^2)^2 q(u^2) to a stored
axis trace (normalized u = x/x*, w~ = w/x*), q a polynomial of degree K in u^2 (least squares on w, w' and w'' with
weights), and evaluate B(A, e, w_0) with bref.py. Usage: python3 fitref.py trace_name K[,K2,...] [wfit]
Writes src/xref/ref_<name>_K<K>.json (A, x*, e, exact decimal coefficients of q, fit errors, B)."""
import sys, json
import numpy as np
import mpmath as mp
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bref

D = os.environ.get('TRACE_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'traces')) + os.sep
name = sys.argv[1]
Ks = [int(k) for k in sys.argv[2].split(',')]
z = np.load(D + name + '_traces.npz', allow_pickle=True)
x, w, wp, wpp = z['x'], z['w'], z['wp'], z['wpp_ode']
cl = float(z['c_l']); A = 2 * cl - 1
k = np.where((w[:-1] < 0) & (w[1:] >= 0))[0][0]
xs = brentq(CubicSpline(x, w), x[k], x[k + 1])
u = x / xs; sel = (u > 0) & (u < 1)
u, wt, wtp, wtpp = u[sel], w[sel] / xs, wp[sel], wpp[sel] * xs
w1 = -A * u * (1 - u ** 2) / (1 + u ** 2)
# derivatives of the R12 part
w1p = -A * (1 - 4 * u ** 2 - u ** 4) / (1 + u ** 2) ** 2
w1pp = -A * (4 * u * (u ** 2 - 3)) / (1 + u ** 2) ** 3
r0, r1, r2 = wt - w1, wtp - w1p, wtpp - w1pp


def basis(u, K):
    """phi_k = u^3 (1 - u^2)^2 T_k(2 u^2 - 1) and its first two derivatives (numerical, via polynomial algebra)."""
    P = np.polynomial.Polynomial
    cols = []
    for kk in range(K + 1):
        Tk = np.polynomial.Chebyshev.basis(kk).convert(kind=P)          # in s
        # q(s) with s = 2u^2 - 1 -> polynomial in u
        Tu = Tk(P([-1, 0, 2]))
        ph = P([0, 0, 0, 1]) * P([1, 0, -1]) ** 2 * Tu
        cols.append((ph(u), ph.deriv(1)(u), ph.deriv(2)(u), ph))
    return cols


out = []
for K in Ks:
    cols = basis(u, K)
    # weights: relative error in w (|w| ~ A u (1 - u)), absolute in w', w'' scaled; exclude u < 0.003 (origin layer noise)
    m = u > 3e-3
    s0 = 1 / (A * u * (1 - u) + 1e-3)
    M = np.vstack([np.column_stack([c[0] * s0 for c in cols])[m],
                   np.column_stack([c[1] / A for c in cols])[m],
                   0.1 * np.column_stack([c[2] / A for c in cols])[m]])
    rhs = np.concatenate([(r0 * s0)[m], (r1 / A)[m], 0.1 * (r2 / A)[m]])
    c, *_ = np.linalg.lstsq(M, rhs, rcond=None)
    # monomial coefficients of q in s' = u^2 (exact decimal strings via mpmath at 40 digits)
    mp.mp.dps = 40
    qs = [mp.mpf(0)] * (K + 1)
    for kk in range(K + 1):
        Tk = np.polynomial.chebyshev.cheb2poly([0] * kk + [1])               # in s = 2 v - 1, v = u^2
        for j, tj in enumerate(Tk):
            # (2 v - 1)^j
            for i in range(j + 1):
                qs[i] += mp.mpf(float(c[kk])) * int(tj) * mp.binomial(j, i) * mp.mpf(2) ** i * (-1) ** (j - i)
    qstr = [mp.nstr(v, 30) for v in qs]
    ph = sum(float(c[kk]) * cols[kk][3] for kk in range(K + 1))
    e0, e1, e2 = r0 - ph(u), r1 - ph.deriv(1)(u), r2 - ph.deriv(2)(u)
    bands = [(0, 0.01), (0.01, 0.1), (0.1, 0.5), (0.5, 0.9), (0.9, 1.0)]
    errs = {'%g-%g' % b: [float(np.abs(e[(u >= b[0]) & (u < b[1])]).max()) for e in (e0 / u, e1, e2)] for b in bands}
    r = bref.Ref(A, 1 / mp.mpf(xs) ** 2, qstr, dps=30)
    uu = np.linspace(1e-4, 1 - 1e-4, 20001)
    w0 = -A * uu * (1 - uu ** 2) / (1 + uu ** 2) + ph(uu)
    neg = bool((w0 < 0).all()); mu0 = float((-w0 / (uu * (1 - uu))).min())
    r.setup()
    B = r.B()
    row = dict(trace=name, K=K, A=A, x_star=xs, e=1 / xs ** 2, q_monomial=qstr, max_err_w_over_u_wp_wpp_by_band=errs,
               w0_negative=neg, mu0=mu0, B=mp.nstr(B, 20), I0=mp.nstr(r.I0, 12), Imid=mp.nstr(r.Imid, 12),
               I1=mp.nstr(r.I1, 12), Q1=mp.nstr(r.Q1, 15), tails=[mp.nstr(v, 3) for v in r.F0tail[-2:] + r.F1tail[-2:]],
               jet=[mp.nstr(r.ser0['W'][j], 15) for j in (1, 3, 5, 7, 9)])
    print(json.dumps({k_: row[k_] for k_ in ('K', 'B', 'w0_negative', 'mu0', 'max_err_w_over_u_wp_wpp_by_band', 'tails',
                                              'jet')}), flush=True)
    json.dump(row, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ref_%s_K%d.json' % (name, K)), 'w'),
              indent=1)
    out.append(row)
