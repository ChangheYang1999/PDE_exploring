# Usage: python3 slowcurve.py tag   (reads runs/audit/<tag>_resmap.npz; bisection for the slow curve leaving P)
import sys, numpy as np
from scipy.interpolate import RegularGridInterpolator as RGI
from scipy.integrate import solve_ivp
tag = sys.argv[1]
d = np.load('runs/audit/%s_resmap.npz' % tag)
r, th, W1, W2, R, Nf = d['r'], d['th'], d['W1'], d['W2'], d['R'], d['Nf']; xs = float(d['x_star'])
f1 = RGI((r, th), W1, bounds_error=False, fill_value=None); f2 = RGI((r, th), W2, bounds_error=False, fill_value=None)
def rhs(t, X):
    rr = np.hypot(X[0], X[1]); t_ = np.arctan2(X[1], X[0]); return [f1((rr, t_))[()], f2((rr, t_))[()]]
e1 = lambda t, X: abs(X[0] - xs) - 0.6; e1.terminal = True
e2 = lambda t, X: X[1] - 3.0; e2.terminal = True
y0 = 0.1
def run(xi0):
    return solve_ivp(rhs, [0, 20], [xs + xi0, y0], max_step=0.02, rtol=1e-11, atol=1e-13, events=[e1, e2])
lo, hi = -0.01, 0.01
slo, shi = run(lo), run(hi)
assert np.sign(slo.y[0, -1] - xs) != np.sign(shi.y[0, -1] - xs)
for it in range(60):
    mid = 0.5 * (lo + hi); s = run(mid)
    if s.t_events[1].size: break
    if np.sign(s.y[0, -1] - xs) == np.sign(slo.y[0, -1] - xs): lo, slo = mid, s
    else: hi, shi = mid, s
print('xi0 bracket at y0 %.2f: [%.6e, %.6e] (quadratic kappa y0^2 = %.6e)' % (y0, lo, hi, -0.0109474 * y0 ** 2))
# slow curve = where the two bracketing trajectories agree
yy = np.linspace(y0, 3.0, 300)
def xat(s, y):
    m = np.argsort(s.y[1]); return np.interp(y, s.y[1][m], s.y[0][m], right=np.nan)
xl, xh = xat(slo, yy), xat(shi, yy)
good = np.abs(xl - xh) < 0.01
ymax = yy[good].max() if good.any() else y0
print('slow curve resolved up to y %.2f' % ymax)
for y in [0.25, 0.5, 1.0, 1.5, 2.0, 2.5]:
    if y <= ymax: print('  y %.2f  x - x* %.4f  (kappa y^2 %.4f)' % (y, 0.5 * (np.interp(y, yy, xl) + np.interp(y, yy, xh)) - xs, -0.0109474 * y * y))
ok = (th > 1e-3) & (th < np.pi / 2 - 1e-3); q = np.abs(R[:, ok]) / Nf[:, ok]; tt = th[ok]
X = r[:, None] * np.cos(tt)[None, :]; Y = r[:, None] * np.sin(tt)[None, :]
i, j = np.unravel_index(np.argmax(q), q.shape)
print('residual max %.3e at x - x* %.4f, y %.3f' % (q[i, j], X[i, j] - xs, Y[i, j]))
for y in [1.0, 1.5, 2.0, 2.5]:
    if y > ymax: continue
    xc = 0.5 * (np.interp(y, yy, xl) + np.interp(y, yy, xh)); m = np.abs(Y - y) < 0.02
    row = []
    for off in [-0.3, -0.2, -0.1, -0.05, 0.0, 0.05, 0.1, 0.2, 0.3]:
        mm = m & (np.abs(X - (xc + off)) < 0.025)
        row.append('%+.2f:%.1e' % (off, q[mm].max() if mm.any() else np.nan))
    print('  y %.1f max residual vs offset from slow curve: %s' % (y, ' '.join(row)))
