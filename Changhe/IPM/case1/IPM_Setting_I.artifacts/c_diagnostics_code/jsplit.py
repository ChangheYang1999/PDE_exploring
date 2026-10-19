"""Where along the characteristics does the characteristic defect J accumulate? (lead diagnostic, analysis 13.4)
For start points on r = r0, integrate backward (dX/dtau = -W) to |X - P| = eps_P, accumulating q = R/rho split by region:
  stem: |X - P| < d1 ; mid: d1 <= |X - P| < d2 ; outer: |X - P| >= d2 (with r < r0).
Usage: python3 jsplit.py fields.npz r0 n_theta"""
import sys
import numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

f = sys.argv[1]; r0 = float(sys.argv[2]); nth = int(sys.argv[3])
d = np.load(f)
r, th = d['r'], d['theta']
sel = (r < 3 * r0 + 20)
r = r[sel]; lr = np.log(r)
W1, W2, rho, R = d['W1'][sel], d['W2'][sel], d['rho'][sel], d['residual'][sel]
q = np.zeros_like(rho)
inner = np.abs(rho) > 0
q[inner] = R[inner] / rho[inner]
q[:, 0] = q[:, 1]; q[:, -1] = q[:, -2]
q[~np.isfinite(q)] = 0.0
sW1 = RectBivariateSpline(lr, th, W1, kx=3, ky=3)
sW2 = RectBivariateSpline(lr, th, W2, kx=3, ky=3)
sq = RectBivariateSpline(lr, th, q, kx=3, ky=3)
xs = brentq(lambda t: np.interp(t, d['axis_x'], d['axis_w']), 1.0, 30.0)
bounds = [0.03, 0.3, 1.0, 2.0, 4.0, 1e9]
epsP = bounds[0]


def rhs(tau, Z):
    x, y = Z[0], Z[1]
    l, t = np.log(np.hypot(x, y)), np.arctan2(y, x)
    a = float(sW1.ev(l, t)); b = float(sW2.ev(l, t)); qq = float(sq.ev(l, t))
    dist = np.hypot(x - xs, y)
    out = [-a, -b]
    for k in range(len(bounds) - 1):
        out.append(qq if bounds[k] <= dist < bounds[k + 1] else 0.0)
    return out


def near_P(tau, Z):
    return np.hypot(Z[0] - xs, Z[1]) - epsP


near_P.terminal = True
labels = [f'[{bounds[k]},{bounds[k+1]})' for k in range(len(bounds) - 1)]
print(f'{f}: x* {xs:.6f}; r0 {r0}; J split by distance from P')
print(' theta0   total     ' + '  '.join(f'{s:>12s}' for s in labels))
rows = []
for t0 in np.linspace(0.02, np.pi / 2 - 0.02, nth):
    X0 = [r0 * np.cos(t0), r0 * np.sin(t0)] + [0.0] * (len(bounds) - 1)
    sol = solve_ivp(rhs, (0, 200), X0, events=near_P, rtol=1e-9, atol=1e-12, max_step=0.05)
    parts = sol.y[2:, -1]
    rows.append(parts)
    print(f' {t0:.4f} {parts.sum(): .3e} ' + '  '.join(f'{v: .3e}' for v in parts))
rows = np.array(rows)
print('spread by region (max - min over labels): total {:.3e}; '.format(np.ptp(rows.sum(1))) +
      ', '.join(f'{s} {np.ptp(rows[:, k]):.3e}' for k, s in enumerate(labels)))
