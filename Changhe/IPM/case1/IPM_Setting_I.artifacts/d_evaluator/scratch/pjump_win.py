"""Window dependence of the extrapolated [H_xxx] at P on the axis (verifier, check of lead analysis 13.16 (c), (d)).
E2(a): quadratic fits of H_xxx (7-point difference of the verifier's H, h = 1e-3) on a < |xi| < a + 0.4 on each side,
right minus left at xi = 0. E1(a): the lead's form, degree-6 polynomial fit of H itself on the same windows, third
derivative at 0. A |xi|^lam mode (lam = 2.93) gives H_xxx = J/2 sign(xi) (|xi|/0.1)^(lam - 3) up to a smooth part, so
E(a) would stay within about 15 percent of J for a in [0.02, 0.25]. Manufactured control: the same estimators applied to
H + C (xi_+^lam + xi_-^lam) with C set so that J = 0.12 at |xi| = 0.1, and to H + 0.12 xi_+^3 / 6 (an exact cubic jump).
Usage: python3 pjump_win.py x_star shape.npz [shape.npz ...]"""
import sys
import numpy as np
from pjump import H_pts, d3
xs = float(sys.argv[1])
lam = 2.9306
A = (0.02, 0.03, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25)
h = 1e-3


def est(x, H):
    g = d3(H, h); xg = x[3:-3]
    e1, e2 = [], []
    for a in A:
        b = a + 0.4
        v1, v2 = [], []
        for sgn in (-1, 1):
            m = (sgn * (x - xs) > a) & (sgn * (x - xs) < b)
            v1.append(np.poly1d(np.polyfit(x[m] - xs, H[m], 6)).deriv(3)(0.))
            m = (sgn * (xg - xs) > a) & (sgn * (xg - xs) < b)
            v2.append(np.polyval(np.polyfit(xg[m] - xs, g[m], 2), 0.))
        e1.append(v1[1] - v1[0]); e2.append(v2[1] - v2[0])
    return e1, e2


print('inner edge a       ' + ' '.join('%7.2f' % a for a in A))
for p in sys.argv[2:]:
    d = np.load(p, allow_pickle=True)
    x = xs + np.arange(-0.8, 0.8 + h / 2, h); H = H_pts(d, x, 0 * x)
    xi = x - xs
    e1, e2 = est(x, H)
    print('%-12s E1 ' % p.split('/')[-1][:12] + ' '.join('%+7.3f' % v for v in e1))
    print('%-12s E2 ' % '' + ' '.join('%+7.3f' % v for v in e2))
    if p == sys.argv[2]:
        # manufactured: lam mode, both sides, H_xxx jump 0.12 at |xi| = 0.1 (even mode: H_xxx = +-C lam(lam-1)(lam-2)|xi|^(lam-3))
        C = 0.06 / (lam * (lam - 1) * (lam - 2) * 0.1 ** (lam - 3))
        for lab, add in (('+lam mode', C * np.abs(xi) ** lam), ('+cubic jump', 0.12 * np.where(xi > 0, xi, 0) ** 3 / 6)):
            f1, f2 = est(x, H + add)
            print('%-12s E1 ' % lab + ' '.join('%+7.3f' % (u - v) for u, v in zip(f1, e1)) + '   (added part only)')
            print('%-12s E2 ' % '' + ' '.join('%+7.3f' % (u - v) for u, v in zip(f2, e2)))
