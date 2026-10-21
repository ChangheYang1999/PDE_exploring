import sys
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from vnum import NumTrial
from vaxis import AxisData, B3
st, ev = sys.argv[1], sys.argv[2]
tr = NumTrial(st, 'cuda')
ad = AxisData(tr, ev, Nth=4096, K=4)
b = B3(ad)
for key in ['F1', 'F2b']:
    for (xlo, xc) in [(0.002, 0.02), (0.01, 0.1), (0.34, 2.6)]:
        r = b.fp(key, xlo, xc, deg=8)
        print(key, xlo, xc, 'fp0 %.6e mid %.6e endp %.6e Bnat %.6e k0 %.6e fit %.1e' % (r['fp0'], r['mid'], r['endp'], r['Bnat'], r['k0'], r['fitres']))
xs = ad.xs
x = xs - np.geomspace(1e-6, 1, 13)
I = b.integrands(x)
for key in ['F1', 'F2b']:
    print(key, 'near P: (x*-x)^(1-beta) J:', ' '.join('%.3e' % v for v in I[key] * (xs - x) ** (1 - b.be)))
x = np.linspace(0.3, xs - 0.3, 12)
I = b.integrands(x)
print('middle J F2b:', ' '.join('%.2e' % v for v in I['F2b']))
