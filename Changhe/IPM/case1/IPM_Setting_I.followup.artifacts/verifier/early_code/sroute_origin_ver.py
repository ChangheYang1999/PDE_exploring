"""verifier: origin-model dependence of the S route of hminus_ver.py (lead NOTES 06:09Z/06:15Z, D25 addendum), own code.
w-fit variants on [x0, xf] for y = w/x, z = (x/xf)^2 (all then use w'(0) = -A in the series, as hminus_ver.series_route):
  free     : y = c0 + sum_k c_k z^k, unweighted (hminus_ver.fit_w)
  forced   : c0 = -A fixed, unweighted (the first, faulty version)
  forced3  : c0 = -A fixed, residual weighted by x^3 (the lead's S-23 variant, as I read it)
  free3    : c0 free, weight x^3
  frac     : free + e x^(8+beta) (a w term x^(9+beta), the homogeneity heuristic of the lead's note)
  free.05  : free, x0 = 0.05;  free.1: free, x0 = 0.1
Printed: d3, d5, d7, the fitted e (frac), R_nat at u = 0.06, 0.1, 0.2, 0.3 (pointwise TraceAxis Q, m, Q*), B_3^nat by (8).
Usage: sroute_origin_ver.py name1,name2,..."""
import sys
import numpy as np
sys.path.insert(0, 'verifier/early_code')
from trace_axis import TraceAxis, _parts
from hminus_ver import series_route, b3_form8, D

US = (0.06, 0.1, 0.2, 0.3, 0.5, 0.9, 0.98, 0.995)


def fit(x, w, A, xf, deg, x0, forced, wpow, frac, be, fexp=8):
    s = (x >= x0) & (x <= xf)
    xx = x[s]
    y = w[s] / xx
    z = (xx / xf) ** 2
    cols = [z ** k for k in range(0 if not forced else 1, deg + 2)]
    if frac:
        cols.append((xx / xf) ** (fexp + be))
    M = np.array(cols).T
    rhs = y + A if forced else y.copy()
    wt = xx ** wpow
    c = np.linalg.lstsq(M * wt[:, None], rhs * wt, rcond=None)[0]
    res = float(np.abs(M @ c - rhs).max() / np.abs(y + A).max())
    if forced:
        c = np.concatenate([[-A], c])
    e = c[-1] / xf ** (fexp + be) if frac else 0.0
    cp = c[:deg + 2]
    wc = np.zeros(2 * deg + 4)
    wc[1] = -A
    wc[3::2] = cp[1:] / xf ** (2 * np.arange(1, deg + 2))
    return wc, e, res, c[0] + A


VARS = {'free': (0.02, False, 0, False), 'forced': (0.02, True, 0, False), 'forced3': (0.02, True, 3, False),
        'free3': (0.02, False, 3, False), 'frac': (0.02, False, 0, True), 'free.05': (0.05, False, 0, False),
        'free.1': (0.1, False, 0, False)}
if len(sys.argv) > 2:      # second run: same parameter count, extra polynomial degree vs fractional exponents 6, 8, 10 (+beta)
    VARS = {'free': (0.02, False, 0, False), 'free+1': (0.02, False, 0, False), 'frac6': (0.02, False, 0, 6),
            'frac8': (0.02, False, 0, 8), 'frac10': (0.02, False, 0, 10)}

for nm in sys.argv[1].split(','):
    path = D + nm + '_traces.npz'
    ad = TraceAxis(path, reg='Ag', near_frac=0.03, wppkey='wpp_ode')
    xs, mu1 = ad.xs, ad.mu1
    A = 2 * ad.c_l_file - 1
    be = 2 / A
    dAg = (mu1 - A) / xs ** 2
    zf = np.load(path, allow_pickle=True)
    xd, wd = np.asarray(zf['x']), np.asarray(zf['w'])
    Qs = float(_parts(ad, np.array([xs]))['Q'][0])
    pp = _parts(ad, np.array(US) * xs)
    print('%s: A %.6f beta %.6f x* %.5f' % (nm, A, be, xs), flush=True)
    for vn, (x0, forced, wpow, frac) in VARS.items():
        for xf, deg in [(2.0, 8), (2.6, 10)]:
            wc, e, res, c0 = fit(xd, wd, A, xf, deg + (vn == 'free+1'), x0, forced, wpow, bool(frac), be, 8 if frac is True else frac)
            S = series_route(wc, A, dAg, be)
            q5, q3, q1 = S['q']
            R = (pp['Q'] - (q5 * pp['m'] ** 5 + q3 * pp['m'] ** 3 + q1 * pp['m']) - Qs) * xs ** 5
            B = b3_form8(ad, S, S['q'], Qs, A, be, dAg, xs)['Bnat']
            print('  %-8s xf %.1f d%-2d c0+A %+.1e d3 %.10f d5 %+.6e d7 %+.6e%s fit res %.1e | R_nat(u=%s) %s | B3nat(8) %.5f' % (
                vn, xf, deg, c0, wc[3], wc[5], wc[7], (' e %+.2e' % e) if frac else '', res, US,
                ' '.join('%+.4f' % v for v in R), B), flush=True)
