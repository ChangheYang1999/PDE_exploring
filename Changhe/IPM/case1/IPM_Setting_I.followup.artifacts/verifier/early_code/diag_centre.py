# Centre diagnostic for a numerics-lane state: x^(5+beta) J (forms F2b, ident) and the axis traces near 0.
import sys
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from vnum import NumTrial
from vaxis import AxisData, B3
st, ev = sys.argv[1], sys.argv[2]
tr = NumTrial(st, 'cuda')
ad = AxisData(tr, ev, Nth=4096, K=4)
b = B3(ad)
be = b.be
x = np.geomspace(2e-4, 0.3, 14)
I = b.integrands(x)
W = ad.interp('w', x); G = ad.interp('g', x); G3 = ad.interp('G3', x)
A = 2 * ad.c_l - 1
print('A %.10f beta %.6f x* %.8f' % (A, be, ad.xs))
print('   x          x^(5+b) F2b      x^(5+b) ident    (w/x + A)/x^2     g/x^2         (g/x^2 - g0)/x^2   G3/x^2')
g0 = G[0][0] / x[0] ** 2
for i, xi in enumerate(x):
    print('%.3e  %+.6e  %+.6e  %+.6e  %+.8e  %+.4e  %+.6e' % (xi, I['F2b'][i] * xi ** (5 + be), I['ident'][i] * xi ** (5 + be),
          (W[0][i] / xi + A) / xi ** 2, G[0][i] / xi ** 2, (G[0][i] / xi ** 2 - g0) / xi ** 2, G3[0][i] / xi ** 2))
