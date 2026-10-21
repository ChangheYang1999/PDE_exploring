"""verifier: mu_0 of the amplitude split (hminus_split_ver.py) under the x^(7+beta) and x^(9+beta) origin models of the
D25 addendum: hminus_split_ver.fit_w replaced by a free-constant fit with one extra term e x^(k-1+beta) in w/x (the
fractional term is fitted and then dropped from the series, as in sroute_origin_ver.py). Usage: split_origin_ver.py k names"""
import sys
import numpy as np
sys.path.insert(0, 'verifier/early_code')
import hminus_split_ver as H

KF = int(sys.argv[1])


def fit_frac(x, w, A, xf, deg, x0=0.02):
    be = 2 / A
    s = (x >= x0) & (x <= xf)
    xx = x[s]
    y = w[s] / xx
    z = (xx / xf) ** 2
    M = np.array([z ** k for k in range(deg + 2)] + [(xx / xf) ** (KF - 1 + be)]).T
    c = np.linalg.lstsq(M, y, rcond=None)[0]
    res = float(np.abs(M @ c - y).max() / np.abs(y + A).max())
    wc = np.zeros(2 * deg + 4)
    wc[1] = -A
    wc[3::2] = c[1:deg + 2] / xf ** (2 * np.arange(1, deg + 2))
    return wc, res


H.fit_w = fit_frac
for nm in sys.argv[2].split(','):
    r = H.analyse(H.D + nm + '_traces.npz', nm, dict(near_frac=0.03, wppkey='wpp_ode'))
    for row in r['rows']:
        print('k = %d %-7s xf %.1f deg %d: b0 %.5f b1 %.5f B3 %.5f mu_0 %.4f (H_-) for mu >= %.4f' % (
            KF, nm, row['xf'], row['deg'], row['b0'], row['b1'], row['B3'], row['mu0'], row['mu_H']), flush=True)
