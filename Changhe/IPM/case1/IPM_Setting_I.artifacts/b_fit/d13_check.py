"""D13 check (claim from external referee nobound1; equivalent to analysis 9.4 at x = x*):
  PV int_{R^2} rho(X) |Z|^{-3} sin(3 arg Z) dX = pi (1 - c_l + g(P)/4),  Z = X - P,  P = (x*, 0),
circular principal value about P. Uses rho = x^2 y e^H with H from the export (interpolated in (log r, theta)).
By oddness in y the integrand is even in y: integrate over y > 0 and double.
  smooth partition 1 = chi(|Z|) + (1 - chi), chi = 1 on |Z| < s1, 0 on |Z| > s2 (C^infinity transition);
  inner: chi * integrand, polar about P (the leading term g* eta sin 3phi / s integrates to zero in phi; by oddness in eta
         the O(1) term also does, so the cut at s0 costs O(s0^2));
  outer: (1 - chi) * integrand on the export grid (Q and its mirror x < 0), trapezoid in (log r, theta);
  tail: r > R_grid, rho ~ r^k Theta_limit(theta), kernel ~ r^{-3} sin(3 theta).
Usage: python d13_check.py fields.npz"""
import sys
import numpy as np
from scipy.interpolate import RectBivariateSpline, CubicSpline
from scipy.optimize import brentq
z = np.load(sys.argv[1])
r, th, H = z['r'], z['theta'], z['H']
cl = float(z['c_l']); k = 1 / cl
t = np.log(r)
Hs = RectBivariateSpline(t, th, H, kx=5, ky=5)
ax = z['axis_x']; sel = ax < 40
ws = CubicSpline(ax[sel], z['axis_w'][sel]); xs = brentq(ws, 1.0, 30.0)
gP = float(CubicSpline(ax[sel], z['axis_G1'][sel])(xs))
def rho(x, y):
    rr = np.hypot(x, y); tt = np.arctan2(y, np.abs(x))
    return x * x * y * np.exp(Hs.ev(np.log(rr), tt))
rhs = np.pi * (1 - cl + gP / 4)
def chi(s, s1, s2):
    u = np.clip((s - s1) / (s2 - s1), 0, 1)
    with np.errstate(divide='ignore', over='ignore'):
        a = np.where(u > 0, np.exp(-1 / np.maximum(u, 1e-300)), 0.0)
        b = np.where(u < 1, np.exp(-1 / np.maximum(1 - u, 1e-300)), 0.0)
    return b / (a + b)
for s1, s2 in ((0.5, 1.5), (1.0, 3.0), (2.0, 5.0), (0.3, 4.0)):
    # inner: s in (s0, s1), phi in (0, pi), Gauss-Legendre in both
    s0 = 1e-3
    ns, nph = 300, 600
    gs, gw = np.polynomial.legendre.leggauss(ns)
    u = np.log(s0) + (np.log(s2) - np.log(s0)) * (gs + 1) / 2; wu = gw * (np.log(s2) - np.log(s0)) / 2
    S = np.exp(u)
    gp, gpw = np.polynomial.legendre.leggauss(nph)
    ph = np.pi * (gp + 1) / 2; wph = gpw * np.pi / 2
    SS, PH = np.meshgrid(S, ph, indexing='ij')
    val = chi(SS, s1, s2) * rho(xs + SS * np.cos(PH), SS * np.sin(PH)) * np.sin(3 * PH) / SS ** 3 * SS * SS   # dX = s ds dphi = s^2 du dphi
    inner = 2 * np.sum(val * wu[:, None] * wph[None, :])
    # outer on the export grid (r, theta) in Q and mirror; integrand * r^2 dt dtheta
    TT = th[None, :]; RR = r[:, None]
    X, Y = RR * np.cos(TT), RR * np.sin(TT)
    rh = X * X * Y * np.exp(H)
    out = 0.0
    for sgn in (1, -1):
        Zx, Zy = sgn * X - xs, Y
        s = np.hypot(Zx, Zy)
        f = (1 - chi(s, s1, s2)) * rh * np.sin(3 * np.arctan2(Zy, Zx)) / np.maximum(s, 1e-300) ** 3 * RR ** 2
        wt = np.ones_like(t); wt[[0, -1]] = 0.5
        wth = np.ones_like(th); wth[[0, -1]] = 0.5
        out += 2 * np.sum(f * wt[:, None] * wth[None, :]) * (t[1] - t[0]) * (th[1] - th[0])
    # tail: rho ~ r^k Theta_limit, on x>0,y>0 and mirror: kernel -> r^-3 [sin 3theta + sin 3(pi - theta)]
    Th = np.asarray(z['Theta_limit'])
    Rg = r[-1]
    ang = np.sum(Th * (np.sin(3 * th) + np.sin(3 * (np.pi - th))) * wth) * (th[1] - th[0])
    tail = 2 * Rg ** (k - 1) / (1 - k) * ang
    lhs = inner + out + tail
    print(f's1, s2 = {s1}, {s2}: inner {inner:.6f}  outer {out:.6f}  tail {tail:.2e}  LHS {lhs:.6f}  RHS {rhs:.6f}  rel {lhs / rhs - 1:.2e}')
print(f'x* = {xs:.8f}, g(P) = {gP:.6f}, c_l = {cl:.8f}; grid ring spacing near P: dr = {np.interp(xs, r[1:], np.diff(r)):.4f}')
