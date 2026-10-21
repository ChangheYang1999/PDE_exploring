import sys
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from vnum import NumTrial
from vaxis import AxisData, B3
st, ev = sys.argv[1], sys.argv[2]
tr = NumTrial(st, 'cuda')
ad = AxisData(tr, ev, Nth=4096, K=4)
b = B3(ad); be = b.be
t = np.linspace(np.log(0.02), np.log(0.1), 4001)
x = np.exp(t)
J = b.integrands(x)['F2b']
num = np.trapz(J * x, t)
print('int_0.02^0.1 J (trapz, 4001 pts in log x) = %.8e' % num)
c = np.polyfit(x ** 2, J * x ** (5 + be), 8)
print('x^(5+b) J over [0.02, 0.1]: min %.6e max %.6e' % ((J * x ** (5 + be)).min(), (J * x ** (5 + be)).max()))
print('c0 x^(-4-b)/(-4-b) difference: %.8e' % (-0.04934764 * (0.1 ** (-4 - be) - 0.02 ** (-4 - be)) / (4 + be)))
print('panel breaks of ad.b in [log .02, log .1]:', np.exp(ad.b[(ad.b > np.log(0.02)) & (ad.b < np.log(0.1))]))
print('ad.b first values', np.exp(ad.b[:5]), 'ad.q', ad.q, 'P', ad.P)
