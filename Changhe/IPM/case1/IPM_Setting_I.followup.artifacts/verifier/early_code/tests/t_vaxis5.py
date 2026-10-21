"""Which part of the w jet carries the origin-layer noise: direct jets_at vs panel interpolation; modes n >= 2 removed."""
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
Wi = ad.interp('w', x)
Wd = ad.jets_at(x)['w']
psi0 = ad.psi.copy()
ad.psi = psi0.copy(); ad.psi[:, 1:] = 0
W1 = ad.jets_at(x)['w']
ad.psi = psi0.copy(); ad.psi[:, 2:] = 0
W2 = ad.jets_at(x)['w']
ad.psi = psi0
def rough(arr):
    ch = Ch.Chebyshev.fit(s, arr, 20)
    return np.abs(arr - ch(s)).max() / np.abs(arr).max()
for k in range(5):
    sc = x if k % 2 == 0 else 1.0
    print('w%d: interp %.1e direct %.1e  mode1 only %.1e  modes 1-2 %.1e  | |n>=2 part|/|w_k| %.1e  |n>=3| %.1e' % (
        k, rough(Wi[k] / sc), rough(Wd[k] / sc), rough(W1[k] / sc), rough(W2[k] / sc),
        np.abs((Wd[k] - W1[k]) / Wd[k]).max(), np.abs((Wd[k] - W2[k]) / Wd[k]).max()))
