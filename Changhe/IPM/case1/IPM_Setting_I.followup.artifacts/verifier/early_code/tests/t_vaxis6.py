"""Consistency of the w jet (mode 1 only, integral representation): d/dx of the order-k coefficient = (k+1) x coef k+1."""
import sys, math
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from numpy.polynomial import polynomial as Pn
from vgen import Trial
from vaxis import AxisData
tr = Trial('../IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz', 'cuda')
ad = AxisData(tr, '../data/x3_p12_h25_n2048_eval.npz', Nth=2048, K=4)
#ad.psi = ad.psi.copy(); ad.psi[:, 1:] = 0
x0 = np.array([0.005, 0.01, 0.02, 0.05, 0.1, 0.2])
for h in [1e-4]:
    W0 = ad.jets_at(x0)['w']
    Wp = ad.jets_at(x0 * (1 + h))['w']
    Wm = ad.jets_at(x0 * (1 - h))['w']
    for k in range(4):
        fd = (Wp[k] - Wm[k]) / (2 * h * x0)
        print('h %.0e k %d: coef_k+1 (k+1) %s  fd %s' % (h, k, np.array2string((k + 1) * W0[k + 1], precision=10),
                                                    np.array2string(fd, precision=10)))
