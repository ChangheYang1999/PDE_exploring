"""NUMERICAL: anisotropic weight w = |cos th|^{-2a} e^{mu(t)} (b = 0) with piecewise-constant mu' (multiples of 1/16),
mu' = -2a on (-oo, t_1) (the product weight of Theorem O with b = 0 near 0) and mu' = -5/4 on [t_last, oo).
Margin m = b0 + (mu'/2) q + a tan(th) V.grad(th) - b_+ (kappa_w - b_+ for this weight). For each grid row t the
feasible mu' interval for m >= m0 is computed; knots are chosen and checked with both neighbouring values at each knot."""
import numpy as np, json, sys
d = np.load('field.npz'); t = d['t']; th = d['th']; r = np.exp(t)
cl = float(d['cl']); b0 = 1 + cl
bp = (np.hypot(d['rho_x'], d['rho_y']) - d['rho_y']) / 2
C, S = np.cos(th)[None, :], np.sin(th)[None, :]
q = (d['V1']*C + d['V2']*S) / r[:, None]; vth = (-d['V1']*S + d['V2']*C) / r[:, None]
J = slice(1, -1)
a = float(sys.argv[1]) if len(sys.argv) > 1 else 4.25
alpha = b0 + a*np.tan(th[J])[None, :]*vth[:, J] - bp[:, J]; beta = 0.5*q[:, J]
def window(m0):
    lo = np.full(len(t), -np.inf); hi = np.full(len(t), np.inf)
    for i in range(len(t)):
        pos, neg = beta[i] > 1e-14, beta[i] < -1e-14
        if pos.any(): lo[i] = ((m0 - alpha[i, pos]) / beta[i, pos]).max()
        if neg.any(): hi[i] = ((m0 - alpha[i, neg]) / beta[i, neg]).min()
        if (~pos & ~neg).any() and (alpha[i, ~pos & ~neg] < m0).any(): lo[i], hi[i] = np.inf, -np.inf
    return lo, hi
def margin(knots, v):
    idx = np.searchsorted(knots, t); m = alpha + v[idx][:, None]*beta; mins = [m.min()]
    for j, tk in enumerate(knots):
        i = np.argmin(np.abs(t - tk))
        for vv in (v[j], v[j+1]): mins.append((alpha[i] + vv*beta[i]).min())
    return m, min(mins)
for m0 in (0.5, 1.0, 1.5, 2.0):
    lo, hi = window(m0); bad = lo > hi
    print('m0 %.1f: infeasible rows %d; lo(-oo end) %.2f hi %.2f; lo(+oo end) %.2f hi %.2f' % (m0, bad.sum(), lo[0], hi[0], lo[-1], hi[-1]))
    if bad.any(): print('   infeasible r range %.3g..%.3g' % (r[bad].min(), r[bad].max()))
np.savez('aniso_pwc_window_a%.2f.npz' % a, t=t, **{('lo%.1f' % m0): window(m0)[0] for m0 in (1.0,)}, hi1=window(1.0)[1])
lo, hi = window(1.0)
for tt in np.arange(-6.5, 11.6, 0.5):
    i = np.argmin(np.abs(t - tt)); print('t %5.2f r %9.3g  window for m>=1: [%7.2f, %7.2f]' % (t[i], r[i], lo[i], hi[i]))

# piecewise-constant design: on each interval pick the multiple of 1/16 maximizing the minimum margin over the rows of
# the closed interval (rows nearest to each knot count for both neighbours), with the end values fixed.
def design(knots, vfirst, vlast):
    grid16 = np.arange(-160, 33) / 16.0
    edges = np.concatenate([[-np.inf], knots, [np.inf]]); v = np.zeros(len(knots) + 1)
    for j in range(len(knots) + 1):
        rows = np.where((t >= edges[j]) & (t < edges[j+1]))[0].tolist()
        for tk in (edges[j], edges[j+1]):
            if np.isfinite(tk): rows.append(int(np.argmin(np.abs(t - tk))))
        rows = sorted(set(rows))
        if j == 0: v[j] = vfirst; continue
        if j == len(knots): v[j] = vlast; continue
        mins = [(alpha[rows] + g*beta[rows]).min() for g in grid16]; v[j] = grid16[int(np.argmax(mins))]
    return v
best = None
for name, knots in [('k1', np.array([2.0, 2.25, 2.5, 3.0, 4.0])), ('k2', np.array([1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0])),
                    ('k3', np.array([2.0, 2.5, 3.0])), ('k4', np.array([2.0, 2.25, 2.5, 2.75, 3.0, 3.5]))]:
    v = design(knots, -2*a, -1.25); m, mn = margin(knots, v); i, j = np.unravel_index(m.argmin(), m.shape)
    print(name, 'knots', knots.tolist(), 'values*16', (v*16).astype(int).tolist(), 'min margin incl knots %.4f at r=%.3g th=%.3f' % (mn, r[i], th[J][j]))
    if best is None or mn > best[2]: best = (name, knots, mn, v)
name, knots, mn, v = best
m, mn = margin(knots, v)
for lab, sl in [('r<0.1', r < 0.1), ('0.1<r<5', (r > 0.1) & (r < 5)), ('5<r<60', (r > 5) & (r < 60)), ('r>60', r > 60)]:
    print('%10s min margin %.4f' % (lab, m[sl].min()))
print('near y-axis (last interior angle) min %.4f; near x-axis (first interior) min %.4f' % (m[:, -1].min(), m[:, 0].min()))
json.dump(dict(a=a, b=0, knots=knots.tolist(), values_times_16=(v*16).astype(int).tolist(), min_margin_grid=float(mn)),
          open('aniso_pwc_a%.2f.json' % a, 'w'), indent=1)
