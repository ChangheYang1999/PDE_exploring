"""Verifier check of lead analysis 13.16 (c): third x-derivative of H = log a across the source point P, on and off the axis.
Shape file only; H evaluated pointwise by the verifier's formula (code/gen_shape.py, re-coded here for scattered points).
Method (differs from the lead's axisjump.py, which fits H by degree 6/7 polynomials on each side):
  H_xxx(x, y) at fixed y by a 7-point central difference (h = 2e-3 physical) of H on a fine x-grid;
  jump estimate at a centre x_c: quadratic least-squares fits of H_xxx on [x_c + a, x_c + b] and [x_c - b, x_c - a],
  extrapolated to x_c, right minus left; windows (a, b) = (0.05, 0.30), (0.08, 0.50), (0.12, 0.80).
  Transition location at height y: the x of max |H_xxxx| (central difference of H_xxx) within |x - x*| < 0.4, and the
  midpoint of the H_xxx rise (half-way between the left and right extrapolated levels, located on the fine grid).
Usage: python3 pjump.py shape.npz x_star [y list]
"""
import sys
import numpy as np
from scipy.interpolate import BSpline
from numpy.polynomial.chebyshev import chebval


def H_pts(d, x, y):
    z = d['z']; k = float(z[0]); coef = z[1:]; L = float(d['L'])
    deg, ang, sing = int(d['degree']), int(d['angular']), int(d['singular'])
    order, r_or = int(d['spline_order']), float(d['origin_radius'])
    knots = np.asarray(d['spline_knots'], float)
    r = np.hypot(x, y); th = np.arctan2(y, x)
    rr = r / L
    s = rr ** 2 / (1 + rr ** 2)
    q = 1 - np.exp(-(1 - k) / 2 * np.log1p(rr ** 2))
    Bv = BSpline(knots, np.eye(deg + 1), order, extrapolate=False)(q)[:, 1:]
    C = coef[:(ang + 1) * deg].reshape(ang + 1, deg)
    prof = Bv @ C.T                                   # (N, ang+1)
    chi = rr ** 2 / (rr ** 2 + r_or ** 2)
    m = np.arange(ang + 1)
    fac = np.where(m > 1, 1.0, 0.0)[None, :] * (chi[:, None] ** np.maximum(m - 1, 0)[None, :]) + np.where(m > 1, 0.0, 1.0)[None, :]
    if r_or == 0:
        fac = np.ones_like(fac)
    H = (k - 3) / 2 * np.log1p(rr ** 2) + (prof * fac * np.cos(2 * np.outer(th, m))).sum(1)
    p3 = 6 + 2 * k / (2 - k)
    angs = np.abs(np.cos(th)) ** (p3 - 2) * np.sin(th) ** 2
    for j in range(sing):
        e = np.zeros(j + 1); e[j] = 1
        H += coef[(ang + 1) * deg + j] * s ** (p3 / 2) * chebval(2 * q - 1, e) * angs
    return H


def d3(f, h):
    # 7-point central third derivative, O(h^4) (sign fixed 08:4xZ: the first version returned -f''')
    return (f[:-6] - 8 * f[1:-5] + 13 * f[2:-4] - 13 * f[4:-2] + 8 * f[5:-1] - f[6:]) / (8 * h ** 3)


def jump(x, g, xc, a, b):
    R = (x >= xc + a) & (x <= xc + b); Lm = (x <= xc - a) & (x >= xc - b)
    pr = np.polyfit(x[R] - xc, g[R], 2); pl = np.polyfit(x[Lm] - xc, g[Lm], 2)
    return np.polyval(pr, 0) - np.polyval(pl, 0), np.polyval(pl, 0), np.polyval(pr, 0)


if __name__ == '__main__':
    d = np.load(sys.argv[1], allow_pickle=True)
    xs = float(sys.argv[2])
    ys = [float(v) for v in sys.argv[3].split(',')] if len(sys.argv) > 3 else [0.0]
    h = 2e-3
    W = [(0.05, 0.30), (0.08, 0.50), (0.12, 0.80)]
    for y in ys:
        x = xs + np.arange(-1.3, 1.3 + h / 2, h)
        H = np.concatenate([H_pts(d, x[i:i + 400], np.full(len(x[i:i + 400]), y)) for i in range(0, len(x), 400)])
        g = d3(H, h); xg = x[3:-3]
        out = []
        for c in (xs, xs - 0.8, xs + 0.8):
            out.append(' '.join('%+.4f' % jump(xg, g, c, a, b)[0] for a, b in W))
        # transition location: max |H_xxxx| near x*
        g4 = (g[2:] - g[:-2]) / (2 * h); x4 = xg[1:-1]
        sel = np.abs(x4 - xs) < 0.4
        j = np.argmax(np.abs(g4[sel])); xmax4 = x4[sel][j]
        J, lo, hi = jump(xg, g, xs, *W[1])
        mid = 0.5 * (lo + hi)
        near = np.abs(xg - xs) < 0.15
        cross = xg[near][np.argmin(np.abs(g[near] - mid))]
        print('y %.3f | jump at x* %s | ctrl x*-0.8 %s | x*+0.8 %s | max|H4| at xi %+.4f (%.1f) | mid-level crossing xi %+.4f'
              ' | circle xi %+.4f' % (y, out[0], out[1], out[2], xmax4 - xs, g4[sel][j], cross - xs, np.sqrt(xs ** 2 - y ** 2) - xs))
        sys.stdout.flush()
