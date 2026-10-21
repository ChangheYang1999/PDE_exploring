"""Q = x^(5+beta) J_F2b on [1e-3, 2.6] from two inverse resolutions; deviation from the outer-window polynomial."""
import sys, math
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from numpy.polynomial import chebyshev as Ch
from vgen import Trial
from vaxis import AxisData, B3
tr = Trial('../IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz', 'cuda')
x = np.geomspace(1e-3, 2.6, 61)
Qs = {}
for tag, f, nth in [('p12', 'x3_p12_h25_n2048', 2048), ('p16', 'x3_p16_h20_n4096', 4096)]:
    ad = AxisData(tr, '../data/%s_eval.npz' % f, Nth=nth, K=4, mode1=sys.argv[1])
    print(tag, 'x*', ad.xs)
    b = B3(ad)
    I = b.integrands(x)
    Qs[tag] = I['F2b'] * x ** (5 + b.be)
    Qs[tag + 'w2'] = ad.interp('w', x)[2]
    Qs[tag + 'w3'] = ad.interp('w', x)[3]
m = x >= 0.34
for tag in ['p12', 'p16']:
    s = x[m] ** 2
    ch = Ch.Chebyshev.fit(s, Qs[tag][m], 12, domain=[0, 2.6 ** 2])
    Qs[tag + 'ext'] = ch(x ** 2)
print(' x          Q_p12            (Q_p16-Q_p12)/Q  (Q_p12-ext12)/Q (Q_p16-ext16)/Q  w2 p16-p12 rel  w3 rel')
for i in range(0, len(x), 3):
    q = Qs['p12'][i]
    print('%.4e %.12e %.2e %.2e %.2e %.2e %.2e' % (x[i], q, (Qs['p16'][i] - q) / q, (q - Qs['p12ext'][i]) / q,
          (Qs['p16'][i] - Qs['p16ext'][i]) / q, (Qs['p16w2'][i] - Qs['p12w2'][i]) / Qs['p12w2'][i],
          (Qs['p16w3'][i] - Qs['p12w3'][i]) / Qs['p12w3'][i]))
