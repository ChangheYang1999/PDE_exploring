"""B_3 of a stored trial with the Green-quadrature axis inverse (vgaxis.GreenAxis): forms F1, F2a, F2b, own coefficient.
usage: python3 b3_green.py trial.npz Nth hmax qf tag"""
import sys, math, time, json
sys.path.insert(0, 'verifier/early_code')
import numpy as np, torch
from numpy.polynomial import chebyshev as Ch
from vgen import Trial
from vaxis import B3
from vgaxis import GreenAxis
trial, Nth, hmax, qf, tag = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
t0 = time.time()
tr = Trial(trial, 'cuda')
kw = dict(K=4, Nth=Nth, hmax=hmax, qf=qf)
ad0 = GreenAxis(tr, **kw)
c_lint = (1 + ad0.info['M_n'][0] / 2) / 3
c_lP, adP = ad0.c_l, ad0
for it in range(3):
    c_lP = 1 - c_lP + float(adP.interp('w', [adP.xs])[1][0])
    adP = GreenAxis(tr, c_l=c_lP, xguess=adP.xs, **kw)
A0 = 2 * ad0.c_l - 1
xf = np.geomspace(2e-3, 0.05, 200)
cf = np.polynomial.polynomial.polyfit(xf ** 2, ad0.interp('w', xf)[0] / xf, 6)
print("%s green: x* %.13f c_l(1/k) %.12f  w'(0)+A %.3e  c_lint %.12f  c_lP %.12f  w'(x*)-A at c_lP %.2e" %
      (tag, ad0.xs, ad0.c_l, cf[0] + A0, c_lint, c_lP, adP.interp('w', [adP.xs])[1][0] - (2 * c_lP - 1)))
own = Ch.chebval(-1.0, tr.tcoef) * tr.L ** (-tr.p3)
print('own coefficient T(-1) L^-p3 = %.6e natural %.5f' % (own, own * ad0.xs ** (tr.p3 - 2)))
wins = [(0.002, 0.03), (0.002, 0.05), (0.003, 0.1), (0.005, 0.06), (0.005, 0.2), (0.01, 0.1), (0.01, 0.15), (0.01, 0.3),
        (0.02, 0.35), (0.34, 2.6)]
for lab, cl in [('cl_1/k', ad0.c_l), ('cl_0', c_lint), ('cl_P', c_lP)]:
    ad = ad0 if cl == ad0.c_l else (adP if cl == c_lP else GreenAxis(tr, c_l=cl, **kw))
    b = B3(ad)
    for key in ['F1', 'F2a', 'F2b']:
        row = []
        for (xlo, xc) in wins:
            for deg in [8, 12, 16]:
                r = b.fp(key, xlo, xc, deg=deg)
                row.append((xlo, xc, deg, r['Bnat'], r['fitres']))
        print('%-7s %-5s x* %.10f ' % (lab, key, ad.xs) + ' | '.join('[%.3g,%.3g]d%d %.6f (fit %.0e)' %
              (a, bb, dg, v, fr) for a, bb, dg, v, fr in row), flush=True)
print('time %.1f s' % (time.time() - t0))
