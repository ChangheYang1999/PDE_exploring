"""V190: compare the numerics slaved b1 responses PLS1e6 (eps_rel 3e-6) and PLS1e7 (eps_rel 1e-6), read only:
relative difference of v = dg/scale by log-radius band, and of the 37 column values."""
import numpy as np, json
P = '../numerics/'
b = np.load(P + 'runs/pfwd/bn/DR512_a2-1.000_it0.npz'); lr = b['lr']; r = np.exp(lr)
p = 0.337335
scale = (r**2 / (1 + r**2))**(1 - p / 2)
V = {}; C = {}
for t in ('PLS1e6', 'PLS1e7'):
    d = np.load(P + 'runs/pfwd/par/%s_resp_b1.npz' % t)
    V[t] = d['dg'].astype(float) / scale[:, None]
    C[t] = np.array([json.loads(l)['col_values'] for l in open(P + 'runs/pfwd/par/%s.out' % t) if '"col_values"' in l][0])
a, c = V['PLS1e6'], V['PLS1e7']
print('global |v6 - v7|/|v7| = %.3f, cos = %.4f' % (np.linalg.norm(a - c) / np.linalg.norm(c), (a * c).sum() / np.linalg.norm(a) / np.linalg.norm(c)))
for lo, hi in [(-14, -12), (-12, -10), (-10, -8), (-8, -4), (-4, 0), (0, 4), (4, 10)]:
    m = (lr >= lo) & (lr < hi)
    na, nc = np.linalg.norm(a[m]), np.linalg.norm(c[m])
    print('lr [%5.1f,%5.1f): |v6| %.3e |v7| %.3e |v6-v7|/|v7| %.3f cos %.4f' % (lo, hi, na, nc, np.linalg.norm(a[m] - c[m]) / nc,
          (a[m] * c[m]).sum() / na / nc))
x, y = C['PLS1e6'], C['PLS1e7']
print('column values (37): |c6 - c7|/|c7| = %.3f, cos = %.4f, |c6| %.4f |c7| %.4f' % (np.linalg.norm(x - y) / np.linalg.norm(y),
      x @ y / np.linalg.norm(x) / np.linalg.norm(y), np.linalg.norm(x), np.linalg.norm(y)))
print('entries 0-7 c6', np.round(x[:8], 4)); print('entries 0-7 c7', np.round(y[:8], 4))
for lo, hi, nm in [(0, 17, 'rows 0-16'), (17, 37, 'rows 17-36'), (17, 19, 'rows 17-18 (b_1, b_2 per notes of the numerical researcher 19:12Z)')]:
    print('%s: |c6 - c7|/|c7| = %.3f, cos = %.4f' % (nm, np.linalg.norm(x[lo:hi] - y[lo:hi]) / np.linalg.norm(y[lo:hi]),
          (x[lo:hi] * y[lo:hi]).sum() / np.linalg.norm(x[lo:hi]) / np.linalg.norm(y[lo:hi])))
for i in (17, 18, 34, 36):
    print('row %d: c6 %.4f c7 %.4f' % (i, x[i], y[i]))
