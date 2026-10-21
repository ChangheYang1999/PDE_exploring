"""B_3 of a numerics-lane state (vnum.NumTrial) from this lane's own inverse: forms F1, F2a, F2b, defect identity.
Variant of b3_x3.py without the published-trial coefficient line.
usage: python3 b3_num.py state.npz eval.npz Nth tag"""
import sys, math, time, json
sys.path.insert(0, 'verifier/early_code')
import numpy as np, torch
from numpy.polynomial import chebyshev as Ch
from vnum import NumTrial
from vaxis import AxisData, B3
trial, evnpz, Nth, tag = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
t0 = time.time()
tr = NumTrial(trial, 'cuda')
mode1 = sys.argv[5] if len(sys.argv) > 5 else 'integral'
ad0 = AxisData(tr, evnpz, Nth=Nth, K=4, mode1=mode1)
d = np.load(evnpz, allow_pickle=True)
summ = json.loads(str(d['summary']))
c_lint = summ['cl_identity_int']
# c_l with h(P) = 1 exactly for the w used: c_l -> 1 - P_1'(x*) = 1 - c_l + w'(x*), iterated
c_lP, adP = ad0.c_l, ad0
for it in range(3):
    c_lP = 1 - c_lP + float(adP.interp('w', [adP.xs])[1][0])
    adP = AxisData(tr, evnpz, c_l=c_lP, Nth=Nth, K=4, mode1=mode1)
A0 = 2 * ad0.c_l - 1
xf = np.geomspace(2e-3, 0.05, 200)
cf = np.polynomial.polynomial.polyfit(xf ** 2, ad0.interp('w', xf)[0] / xf, 6)
print("%s (mode1 %s): c_l(1/k) %.12f  w'(0)+A %.3e  c_lint %.12f  c_lP %.12f  w'(x*)-A at c_lP %.2e" %
      (tag, mode1, ad0.c_l, cf[0] + A0, c_lint, c_lP, adP.interp('w', [adP.xs])[1][0] - (2 * c_lP - 1)))
wins = [(0.002, 0.02), (0.003, 0.03), (0.005, 0.06), (0.01, 0.1), (0.02, 0.12), (0.01, 0.15), (0.34, 2.6)]
res = {}
for lab, cl in [('cl_1/k', ad0.c_l), ('cl_0', c_lint), ('cl_P', c_lP)]:
    ad = ad0 if cl == ad0.c_l else (adP if cl == c_lP else AxisData(tr, evnpz, c_l=cl, Nth=Nth, K=4, mode1=mode1))
    b = B3(ad)
    for key in ['F1', 'F2a', 'F2b', 'ident']:
        if key == 'ident' and lab != 'cl_1/k':
            continue
        row = []
        for (xlo, xc) in wins:
            for deg in [8, 12]:
                r = b.fp(key, xlo, xc, deg=deg)
                row.append((xlo, xc, deg, r['Bnat'], r['fitres'], r['k0']))
        res[(lab, key)] = row
        print('%-7s %-5s x* %.10f ' % (lab, key, ad.xs) + ' | '.join('[%.3g,%.3g]d%d %.5f (fit %.0e)' %
              (a, bb, dg, v, fr) for a, bb, dg, v, fr, k0 in row), flush=True)
print('time %.1f s' % (time.time() - t0))
