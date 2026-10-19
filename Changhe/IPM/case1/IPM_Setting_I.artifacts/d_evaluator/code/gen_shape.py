"""Verifier's re-implementation of the construct1 global trial formula (final_shape.npz), verifier.

From the stored parameters only (z = [k, coefficients], L, degree, angular, singular, spline_order, origin_radius):
  rr = r/L, s = rr^2/(1+rr^2), q = 1 - (1+rr^2)^(-(1-k)/2),
  H = (k-3)/2 log(1+rr^2) + sum_{m=0}^{angular} sum_j z[1+m*degree+j] B_{j+1}(q) chi^(m-1)[m>1] cos(2 m t)
      + sum_{j<singular} z[1+(angular+1)*degree+j] s^(p3/2) T_j(2q-1) |cos t|^(p3-2) sin^2 t,
  chi = rr^2/(rr^2+origin_radius^2), p3 = 6 + 2k/(2-k), B_i the order-7 B-splines on knots
  [0]*8 + linspace(0,1,degree-6)[1:-1]^1.3 + [1]*8 (the first one omitted),
  rho = L^3 rr^3 cos^2 t sin t e^H.
The formula is defined for every r > 0 (no exterior closure is involved). Output: closed-first-quadrant export in the
format read by vcand.py (r uniform in log r, theta uniform on [0, pi/2]).
Usage: python3 gen_shape.py shape.npz r0 R N nq out.npz [closure]
With the 7th argument 'closure' (or 'closure=<Rs>', closure radius Rs L) the field for r > Rc = R_shape L is replaced by the lead's two-term exterior
extension (construct5 REPORT, tail_control.py; re-implemented here from its definition):
  rho(r, t) = (rho_c - S)(r/Rc)^k + S (r/Rc)^(2k-1),  S = (r rho_r|_c - k rho_c)/(k - 1),
which matches rho and r rho_r at Rc (C^1, not C^2). r rho_r at Rc by a 5-point stencil in log r (h = 1e-3).
"""
import sys
import numpy as np
from scipy.interpolate import BSpline
from numpy.polynomial.chebyshev import chebval


def shape_rho(d, r, th):
    z = d['z']
    k = float(z[0])
    coef = z[1:]
    L = float(d['L'])
    deg, ang, sing = int(d['degree']), int(d['angular']), int(d['singular'])
    order, r_or = int(d['spline_order']), float(d['origin_radius'])
    assert str(d['compact']) == 'matched' and str(d['radial_basis']) == 'spline' and int(d['angular_cap']) == 0
    assert len(coef) == (ang + 1) * deg + sing
    rr = r / L
    s = rr ** 2 / (1 + rr ** 2)
    q = 1 - np.exp(-(1 - k) / 2 * np.log1p(rr ** 2))
    if 'spline_knots' in d.files:                     # construct4 and later: explicit (possibly refined) knots
        knots = np.asarray(d['spline_knots'], float)
        assert len(knots) == deg + order + 2
    else:
        knots = np.r_[np.zeros(order + 1), np.linspace(0, 1, deg - order + 2)[1:-1] ** 1.3, np.ones(order + 1)]
    Bv = BSpline(knots, np.eye(deg + 1), order, extrapolate=False)(q)[:, 1:]       # (N, deg)
    H = (k - 3) / 2 * np.log1p(rr ** 2)[:, None] * np.ones((1, len(th)))
    chi = rr ** 2 / (rr ** 2 + r_or ** 2)
    for m in range(ang + 1):
        prof = Bv @ coef[m * deg:(m + 1) * deg]
        if r_or > 0 and m > 1:
            prof = prof * chi ** (m - 1)
        H += prof[:, None] * np.cos(2 * m * th)[None, :]
    p3 = 6 + 2 * k / (2 - k)
    ct, st = np.abs(np.cos(th)), np.sin(th)
    angs = ct ** (p3 - 2) * st ** 2
    for j in range(sing):
        e = np.zeros(j + 1)
        e[j] = 1
        prof = coef[(ang + 1) * deg + j] * s ** (p3 / 2) * chebval(2 * q - 1, e)
        H += prof[:, None] * angs[None, :]
    rho = L ** 3 * (rr ** 3)[:, None] * (np.cos(th) ** 2 * np.sin(th))[None, :] * np.exp(H)
    return rho, H, dict(k=k, L=L, p3=p3, c_l=1 / k, c=3 / k - 1)


if __name__ == '__main__':
    path, r0, R, N, nq, outp = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    d = np.load(path, allow_pickle=True)
    r = np.exp(np.linspace(np.log(r0), np.log(R), N))
    th = np.linspace(0, np.pi / 2, nq + 1)
    rho, H, info = shape_rho(d, r, th)
    if len(sys.argv) > 7 and sys.argv[7].startswith('closure'):
        # 'closure' closes at R_shape L (the fit's inverse domain); 'closure=<Rs>' closes at Rs L instead (Rs in shape units,
        # e.g. 10000 for the lead's export_fit.py convention, G64)
        Rc = (float(sys.argv[7].split('=')[1]) if '=' in sys.argv[7] else float(d['R_shape'])) * float(d['L'])
        h = 1e-3
        f = [shape_rho(d, np.array([Rc * np.exp(j * h)]), th)[0][0] for j in (-2, -1, 0, 1, 2)]
        rc, rrc = f[2], (f[0] - 8 * f[1] + 8 * f[3] - f[4]) / (12 * h)
        k = info['k']
        S = (rrc - k * rc) / (k - 1)
        out = r > Rc
        u = (r[out] / Rc)[:, None]
        rho[out] = (rc - S)[None, :] * u ** k + S[None, :] * u ** (2 * k - 1)
        print('closure at Rc = %.6g (R_shape %.6g), %d radii replaced, max |S|/max|rho_c| %.3e' % (
            Rc, float(d['R_shape']), int(out.sum()), np.abs(S).max() / np.abs(rc).max()))
    rho[:, 0] = 0.0
    np.savez(outp, r=r, theta=th, rho=rho, c=info['c'], c_l=info['c_l'], k=info['k'], L=info['L'])
    print(info, 'rho max', np.abs(rho).max(), 'finite', np.isfinite(rho).all())
