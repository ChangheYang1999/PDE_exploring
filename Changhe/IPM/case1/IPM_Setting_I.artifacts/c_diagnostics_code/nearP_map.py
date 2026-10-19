"""Map of R/rho near P (lead): table over xi = x - x* in [-3, 3], y in [0.05, 4] for one export."""
import sys, numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.optimize import brentq
f = sys.argv[1]
d = np.load(f); r, th = d['r'], d['theta']; sel = (r > 3) & (r < 16); r = r[sel]
rho, R = d['rho'][sel], d['residual'][sel]
q = np.where(np.abs(rho) > 0, R / np.where(rho == 0, 1, rho), 0.0); q[:, 0] = q[:, 1]
den = d['denominator'][sel]; nr = R / den
sq = RectBivariateSpline(np.log(r), th, q); sn = RectBivariateSpline(np.log(r), th, nr)
xs = brentq(lambda t: np.interp(t, d['axis_x'], d['axis_w']), 1.0, 30.0)
xis = [-3, -2, -1.5, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 1.5, 2, 3]
print(f'{f.split("/")[-1]}: R/rho x 1e5 (rows y, columns xi)')
print('   y\\xi ' + ''.join(f'{v:7.2f}' for v in xis))
for y in [4, 3, 2, 1.5, 1, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05]:
    row = []
    for xi in xis:
        x = xs + xi; rr = np.hypot(x, y); t = np.arctan2(y, x)
        row.append(float(sq.ev(np.log(rr), t)) * 1e5)
    print(f'{y:7.2f} ' + ''.join(f'{v:7.1f}' for v in row))
