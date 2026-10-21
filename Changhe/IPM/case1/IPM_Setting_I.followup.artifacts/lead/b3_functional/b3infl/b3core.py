"""B_3 (natural units) from (c_l, w) on [0, x*]: original form of R10 by the run-1 verifier machinery (vb3ibp.py, copied
into ../dcode), one fixed evaluation configuration (for derivatives) and the 32-variant median (for values)."""
import sys, time
import numpy as np
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dcode'))
from vb3ibp import build, fp0, mid, endp, b3_variants

CFG = dict(xc=0.35, xlo=0.02, K=8, xe=0.92, mode='poly')


def b3_one(x, w, wp, wpp, cl, cfg=CFG, both=False):
    d = build(x, w, wp, wpp, cl)
    xs, be = d['xs'], d['be']
    nat = xs ** (d['p3'] - 2)
    xc, xlo, xe = cfg['xc'] * xs, cfg['xlo'] * xs, cfg['xe'] * xs
    o0, _ = fp0(d['x'], d['Jo'], -5 - be, xlo, xc, cfg['K'])
    mo = mid(d, d['Jo'], xc, xe)
    eo, _ = endp(d, d['Jo'], xe, be - 1, cfg['mode'])
    Bo = (o0 + mo + eo) / (3 * d['N']) * nat
    if not both:
        return Bo, d
    J = d['J1'] - d['kappa'] * d['J2']
    a1, _ = fp0(d['x'], d['J1'], -5 - be, xlo, xc, cfg['K'])
    a2, _ = fp0(d['x'], d['J2'], -be, xlo, xc, cfg['K'])
    mi = mid(d, J, xc, xe)
    en, _ = endp(d, J, xe, be - 1, cfg['mode'])
    Bi = -(1 - be) / (3 * d['N']) * (a1 - d['kappa'] * a2 + mi + en) * nat
    return Bo, Bi, d


def b3_median(x, w, wp, wpp, cl):
    d = build(x, w, wp, wpp, cl)
    s, _ = b3_variants(d)
    return s


def load(path):
    z = np.load(path, allow_pickle=True)
    return z['x'], z['w'], z['wp'], z['wpp_ode'], float(z['c_l'])


if __name__ == '__main__':
    x, w, wp, wpp, cl = load(sys.argv[1])
    t = time.time()
    Bo, Bi, d = b3_one(x, w, wp, wpp, cl, both=True)
    print('one cfg: orig %.6f ibp %.6f  (%.3f s)  x* %.8f g* %.6f' % (Bo, Bi, time.time() - t, d['xs'],
          np.interp(d['xs'], d['x'], d['g'])))
    t = time.time()
    s = b3_median(x, w, wp, wpp, cl)
    print('median: orig %.6f [%.6f, %.6f] ibp %.6f [%.6f, %.6f] (%.2f s)' % (s['orig_median'], s['orig_min'], s['orig_max'],
          s['ibp_median'], s['ibp_min'], s['ibp_max'], time.time() - t))
