"""Noise of the w jets by mode: drop single modes consistently (all t-derivatives) and measure roughness of w3."""
import sys, math
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from numpy.polynomial import chebyshev as Ch
from vgen import Trial
from vaxis import AxisData
tr = Trial('../IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz', 'cuda')
x = np.geomspace(5e-3, 0.3, 600)
s = (x / 0.3) ** 2
ad = AxisData(tr, '../data/x3_p12_h25_n2048_eval.npz', Nth=2048, K=4)
nm = len(ad.ns)
def rough(arr, lo, hi):
    ch = Ch.Chebyshev.fit(s, arr, 20)
    m = (x >= lo) & (x < hi)
    return np.abs(arr - ch(s))[m].max()
for lab, keep in [('all', None), ('all notol', 'notol'), ('drop n>=2', lambda n: n == 1), ('drop n>=3', lambda n: n <= 2), ('drop n>=4', lambda n: n <= 3),
                  ('drop n>=5', lambda n: n <= 4), ('drop n=3 only', lambda n: n != 3), ('drop n>=8', lambda n: n <= 7),
                  ('drop n>=30', lambda n: n <= 29)]:
    ad.mode_tol = None if keep == 'notol' else 1e-12
    ad.mode_mask = None if keep is None or keep == 'notol' else np.array([1.0 if keep(n) else 0.0 for n in ad.ns])
    W = ad.jets_at(x)['w']
    print('%-14s abs noise w3: x<0.02 %.1e  0.02-0.1 %.1e  >0.1 %.1e | w2/x %.1e %.1e %.1e' % (
        lab, rough(W[3], 0, .02), rough(W[3], .02, .1), rough(W[3], .1, 1), rough(W[2] / x, 0, .02), rough(W[2] / x, .02, .1),
        rough(W[2] / x, .1, 1)))
