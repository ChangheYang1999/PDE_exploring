"""Compare jump estimators for [H_xxx] at P on the axis (verifier H evaluator, scratch/pjump.py H_pts):
 E1 (lead's form, re-coded): degree-D polynomial fit of H on lo < |xi| < hi on each side, third derivative at xi = 0;
 E2 (verifier): quadratic fit of the 7-point-difference H_xxx on the same windows, value at xi = 0.
Usage: python3 pjump_cmp.py shape.npz x_star"""
import sys
import numpy as np
from pjump import H_pts, d3
d = np.load(sys.argv[1], allow_pickle=True); xs = float(sys.argv[2])
h = 1e-3
x = xs + np.arange(-1.6, 1.6 + h / 2, h); H = H_pts(d, x, 0 * x); g = d3(H, h); xg = x[3:-3]
for x0 in (xs, xs - 0.8, xs + 0.8):
    row = []
    for lo, hi, D in ((0.05, 0.5, 6), (0.1, 0.8, 6), (0.2, 1.2, 7), (0.03, 0.3, 4), (0.05, 0.3, 3)):
        e1, e2 = [], []
        for sgn in (-1, 1):
            m = (sgn * (x - x0) > lo) & (sgn * (x - x0) < hi)
            e1.append(np.poly1d(np.polyfit(x[m] - x0, H[m], D)).deriv(3)(0.))
            m = (sgn * (xg - x0) > lo) & (sgn * (xg - x0) < hi)
            e2.append(np.polyval(np.polyfit(xg[m] - x0, g[m], 2), 0.))
        row.append('(%.2f,%.2f,%d) E1 %+.4f E2 %+.4f' % (lo, hi, D, e1[1] - e1[0], e2[1] - e2[0]))
    print('x0-x* %+.1f | ' % (x0 - xs) + ' | '.join(row))
