"""Characteristic defect of a trial (lead, analysis section 13.4).
Every characteristic of the open quadrant leaves the source P. Along a characteristic, an exact solution satisfies
d log rho / dt = 1; a trial has d log rho / dt = 1 + R/rho, R = W.grad rho - rho. So
  J(X0) = int_{-inf}^0 (R/rho)(X(s)) ds   (X(0) = X0, backward to P)
is the relative difference log rho_trial(X0) - log rho_transport(X0), where rho_transport is the solution of the transport
equation with the trial's own velocity W that agrees with the trial at P (to first order). Spread of J over the
characteristics = inconsistency of the trial with smoothness at P plus accumulated residual (no nonlocal feedback).
Start points X0 on the circle r = r0 at angles theta0; backward integration (dX/dtau = -W) until |X - P| < eps_P.
Usage: python3 char_defect.py fields.npz r0 [n_theta]"""
import sys
import numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

f = sys.argv[1]; r0 = float(sys.argv[2]); nth = int(sys.argv[3]) if len(sys.argv) > 3 else 24
d = np.load(f)
r, th = d['r'], d['theta']
sel = (r < 3 * r0 + 20)
r = r[sel]
lr = np.log(r)
W1, W2, rho, R = d['W1'][sel], d['W2'][sel], d['rho'][sel], d['residual'][sel]
q = np.empty_like(rho)
inner = np.abs(rho) > 0
q[inner] = R[inner] / rho[inner]
# axis rows (rho = 0): copy the neighbour row
q[:, 0] = q[:, 1]; q[:, -1] = q[:, -2]
iz = np.where(~np.isfinite(q))
q[iz] = 0.0
sW1 = RectBivariateSpline(lr, th, W1, kx=3, ky=3)
sW2 = RectBivariateSpline(lr, th, W2, kx=3, ky=3)
sq = RectBivariateSpline(lr, th, q, kx=3, ky=3)
# x* from the axis trace
ax, aw = d['axis_x'], d['axis_w']
xs = brentq(lambda t: np.interp(t, ax, aw), 1.0, 30.0)
hP = None
if 'axis_h' in d.files:
    # local cubic interpolation of the sampled trace (2026-10-18 about 06:45Z; linear interpolation over the axis spacing
    # 6.4e-3 gave h(P) - 1 = +2.8e-6 on c6d/c6f exports where the trial value is -1.3e-8; x* and J unchanged)
    from scipy.interpolate import CubicSpline
    _i = int(np.searchsorted(ax, xs)); _sl = slice(max(_i - 8, 0), _i + 8)
    hP = float(CubicSpline(ax[_sl], d['axis_h'][_sl])(xs))


def polar(X):
    x, y = X
    rr = np.hypot(x, y); t = np.arctan2(y, x)
    return np.log(rr), t


def rhs(tau, Z):
    x, y = Z[0], Z[1]
    l, t = polar((x, y))
    a = float(sW1.ev(l, t)); b = float(sW2.ev(l, t))
    return [-a, -b, float(sq.ev(l, t))]


def near_P(tau, Z):
    return np.hypot(Z[0] - xs, Z[1]) - epsP


near_P.terminal = True
print(f'{f}: x* {xs:.6f} h(P) {hP}; start circle r0 = {r0}')
print(' theta0     tau_end    J(eps_P=0.1)   J(eps_P=0.03)  end point (x - x*, y)')
out = []
for t0 in np.linspace(0.02, np.pi / 2 - 0.02, nth):
    X0 = [r0 * np.cos(t0), r0 * np.sin(t0), 0.0]
    res = []
    for epsP in (0.1, 0.03):
        sol = solve_ivp(rhs, (0, 200), X0, events=near_P, rtol=1e-10, atol=1e-12, max_step=0.05)
        res.append((sol.t[-1], sol.y[2, -1], sol.y[0, -1] - xs, sol.y[1, -1]))
    out.append((t0, res[1][0], res[0][1], res[1][1]))
    print(f' {t0:.4f}  {res[1][0]:9.3f}  {res[0][1]: .4e}  {res[1][1]: .4e}  ({res[1][2]: .2e}, {res[1][3]:.2e})')
J = np.array([o[3] for o in out])
print(f'SUMMARY r0 {r0}: J (eps_P 0.03) min {J.min():.3e} max {J.max():.3e} spread {J.max() - J.min():.3e}')
