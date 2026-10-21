"""B_3 estimator (code/vaxis.py B3, forms F1, F2a, F2b) on manufactured exact axis data:
S2 (h) pair (expected 0) and the R12 family (expected C_A (1 - S_A/L^2) natural units; lead: C_A = 0.530667,
sqrt(S_A) = 5.343575 at A = 10.150725)."""
import sys, math
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from manual_axis import ManualAxis, s2h_pair, r12_family
from vaxis import B3
A = 10.150725
wins = [(0.01, 0.15, 8), (0.02, 0.35, 8), (0.05, 0.6, 12), (0.34, 2.6, 12)]
f, cl, xs = s2h_pair(A)
ad = ManualAxis(f, cl, xs, K=6, xmin=1e-3)
b3 = B3(ad, cl)
x = np.geomspace(0.01, xs * 0.999, 7)
it = b3.integrands(x)
print('S2(h): x* %.10f; max |F2b|, |F2a| integrands' % xs, np.abs(it['F2b']).max(), np.abs(it['F2a']).max(), ' T1', np.abs(it['T1']).max())
for key in ['F1', 'F2a', 'F2b']:
    print('  %s ' % key + ' | '.join('[%g,%g]d%d %.3e' % (a, c, d, b3.fp(key, a, c, deg=d)['Bnat']) for a, c, d in wins))
res = {}
for L in [4.0, 5.0, 5.343575, 6.0, 7.0, 8.6, 10.0]:
    f, cl, xs = r12_family(A, L)
    ad = ManualAxis(f, cl, xs, K=6, xmin=1e-3)
    b3 = B3(ad, cl)
    row = {}
    for key in ['F1', 'F2a', 'F2b']:
        row[key] = [b3.fp(key, a, c, deg=d)['Bnat'] for a, c, d in wins]
    res[L] = row
    fac = 1 - 5.343575 ** 2 / L ** 2
    print('R12 L %.6f: ' % L + ' || '.join('%s ' % k + ' '.join('%.7f' % v for v in row[k]) for k in row),
          ' | F2b/(1 - S_A/L^2) = %s' % (' '.join('%.6f' % (v / fac) for v in row['F2b']) if abs(fac) > 1e-6 else 'n/a'))
