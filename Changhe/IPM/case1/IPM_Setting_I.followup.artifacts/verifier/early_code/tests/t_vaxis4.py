"""Noise structure of Q = x^(5+beta) J_F2b and of the w jets in the origin layer (p12 and p16 inverses)."""
import sys, math
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from numpy.polynomial import chebyshev as Ch
from vgen import Trial
from vaxis import AxisData, B3
tr = Trial('../IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz', 'cuda')
x = np.geomspace(5e-3, 0.3, 1500)
s = (x / 0.3) ** 2
for tag, f, nth in [('p12', 'x3_p12_h25_n2048', 2048), ('p16', 'x3_p16_h20_n4096', 4096)]:
    ad = AxisData(tr, '../data/%s_eval.npz' % f, Nth=nth, K=4)
    b = B3(ad)
    Q = b.integrands(x)['F2b'] * x ** (5 + b.be)
    W = ad.interp('w', x)
    for nm, arr in [('Q', Q), ('w/x', W[0] / x), ('w1', W[1]), ('w2/x', W[2] / x), ('w3', W[3]), ('w4/x', W[4] / x)]:
        ch = Ch.Chebyshev.fit(s, arr, 20)
        r = (arr - ch(s)) / np.abs(arr).max()
        # roughness: second differences in log x relative
        print('%s %-5s max|resid deg20| %.1e  at x %.3g; resid rms %.1e; resid in x<0.02 %.1e, 0.02-0.1 %.1e, >0.1 %.1e' %
              (tag, nm, np.abs(r).max(), x[np.argmax(np.abs(r))], np.sqrt(np.mean(r ** 2)), np.abs(r[x < 0.02]).max(),
               np.abs(r[(x >= 0.02) & (x < 0.1)]).max(), np.abs(r[x >= 0.1]).max()))
