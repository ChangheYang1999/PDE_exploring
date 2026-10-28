"""NUMERICAL: piecewise-linear weight exponent mu~ (piecewise-constant mu~') for Theorem R, so that e^{mu~(log r)} is
piecewise exponential in t (exact integration in the numerics lane). Knots are dyadic; values multiples of 1/16.
On each t-interval the margin m = b0 + mu' q/2 - b_+ is evaluated with that interval's value; at each knot with both
neighbouring values (m is affine in mu', so the hull of the two values is covered)."""
import numpy as np, json
d = np.load('field.npz'); t = d['t']; th = d['th']; r = np.exp(t); cl = float(d['cl']); b0 = 1 + cl
bp = (np.hypot(d['rho_x'], d['rho_y']) - d['rho_y']) / 2
c, s = np.cos(th)[None, :], np.sin(th)[None, :]
q = (d['V1'] * c + d['V2'] * s) / r[:, None]
H = lambda z: 0.5 * (1 + np.tanh(z))
mup_cf = lambda tt: 0.25 + 1.5 * H((tt - 1.6) / 0.2) - 3 * H((tt - 6.5) / 1.5)
def build(knots):
    mids = np.concatenate([[knots[0] - 1], 0.5 * (knots[1:] + knots[:-1]), [knots[-1] + 1]])
    v = np.round(mup_cf(mids) * 16) / 16
    v[0] = 0.25; v[-1] = -1.25
    return v
def evalm(knots, v):
    idx = np.searchsorted(knots, t)              # interval index of each grid t
    m = b0 + 0.5 * v[idx][:, None] * q - bp
    mins = [m.min()]
    for j, tk in enumerate(knots):               # both values at each knot (nearest grid row)
        i = np.argmin(np.abs(t - tk))
        for vv in (v[j], v[j + 1]):
            mins.append((b0 + 0.5 * vv * q[i] - bp[i]).min())
    return m, min(mins)
best = None
for name, knots in [('quarter', np.arange(1.25, 11.01, 0.25)), ('half', np.concatenate([[1.5, 1.75], np.arange(2.5, 11.01, 0.5)])),
                    ('coarse', np.array([1.5, 1.75, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]))]:
    v = build(knots); m, mn = evalm(knots, v)
    i, j = np.unravel_index(m.argmin(), m.shape)
    print(name, len(knots), 'min margin incl knots %.4f' % mn, 'argmin r=%.3f th=%.3f' % (r[i], th[j]), 'sup|v| %.4f' % np.abs(v).max())
    print('  knots', knots.tolist()); print('  values', (v * 16).astype(int).tolist(), '/16')
    if name == 'coarse':
        json.dump(dict(knots=knots.tolist(), values_times_16=(v * 16).astype(int).tolist(), min_margin_grid=float(mn),
                       argmin_r=float(r[i]), argmin_theta=float(th[j]), sup_abs=float(np.abs(v).max())), open('mu_pwc.json', 'w'), indent=1)
