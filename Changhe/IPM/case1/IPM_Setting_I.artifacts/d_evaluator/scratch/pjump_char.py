"""Third-x-derivative step of H across the characteristic leaving P (xi_c(y) = c y^2, c = -a_2/(A-2) from the shape via
the axis identities h'(x*) = -A q'(x*)/g*, a_2 = (h' + q')/2), at fixed heights y (verifier; check of lead 13.16 (a), (d)).
Estimators centred at x* + xi_c(y): E1 (lead's form; degree-6 fits of H on a < |xi - xi_c| < a + 0.4, a = 0.05, 0.1, 0.2)
and the joint model S of pjump_joint.py (D = 10, W = 0.8, gap a = 0.05, 0.15). Same sign convention as the axis value
(right minus left). Usage: python3 pjump_char.py shape.npz x_star c y1,y2,..."""
import sys
import numpy as np
from numpy.polynomial import legendre as Lg
from pjump import H_pts
d = np.load(sys.argv[1], allow_pickle=True); xs = float(sys.argv[2]); c = float(sys.argv[3])
for y in [float(v) for v in sys.argv[4].split(',')]:
    x0 = xs + c * y * y
    x = x0 + np.linspace(-0.8, 0.8, 3201); xi = x - x0
    H = H_pts(d, x, np.full(len(x), y))
    e1 = []
    for a in (0.05, 0.1, 0.2):
        v = []
        for sgn in (-1, 1):
            m = (sgn * xi > a) & (sgn * xi < a + 0.4)
            v.append(np.poly1d(np.polyfit(xi[m], H[m], 6)).deriv(3)(0.))
        e1.append(v[1] - v[0])
    js = []
    for a in (0.05, 0.15):
        m = np.abs(xi) >= a
        M = np.c_[Lg.legvander(xi[m] / 0.8, 10), np.where(xi[m] > 0, xi[m], 0) ** 3 / 6]
        cc, *_ = np.linalg.lstsq(M, H[m], rcond=None); js.append(cc[-1])
    print('y %.2f xi_c %+.4f | E1 %s | joint D10 %s' % (y, c * y * y, ' '.join('%+.3f' % v for v in e1), ' '.join('%+.3f' % v for v in js)))
