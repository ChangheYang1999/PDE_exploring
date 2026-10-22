"""Map of |R|/N over the (t, sigma) grid (off-grid shift) for a generating-function state."""
import sys, numpy as np, torch
torch.set_num_threads(1)
from model import Model, fields, ts_to_xeta
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = d['c']; a0 = float(d['a0'])
alpha = float(d['alpha']) if 'alpha' in d.files else 0.0
se = float(sys.argv[sys.argv.index('--se') + 1]) if '--se' in sys.argv else (float(d['se']) if 'se' in d.files else 1.0)
gam = float(sys.argv[sys.argv.index('--gam') + 1]) if '--gam' in sys.argv else (float(d['gam']) if 'gam' in d.files else 0.0)
m_ = int(d['m']) if 'm' in d.files else 3
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam)
nt, ns = 24, 12
tb = np.linspace(0.005, 1, nt + 1); sb = np.linspace(0, 1, ns + 1)
t = np.linspace(0.005, 0.9995, 200); s = np.linspace(0.002, 0.998, 60)
T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
S = S if gam <= 0 else (np.exp(gam * S) - 1) / (np.exp(gam) - 1)
x, eta = ts_to_xeta(T, S, m_, se); x = torch.tensor(x); eta = torch.tensor(eta)
q = []; y = []
for ch in torch.split(torch.arange(x.shape[0]), 3000):
    F = fields(mod.basis_matrix(x[ch], eta[ch]) @ torch.tensor(c), x[ch], eta[ch], a0, mod.beta)
    q.append((F['R'].abs() / F['N']).detach().numpy()); y.append(F['y'].detach().numpy())
q = np.concatenate(q); y = np.concatenate(y); r = np.hypot(x.numpy(), y)
print('rows: t bins (t, median physical r); columns: sigma bins 0 (x-axis) .. 1 (y-axis); entries log10 max |R|/N')
for i in range(nt):
    m = (T >= tb[i]) & (T < tb[i + 1])
    row = []
    for j in range(ns):
        mm = m & (S >= sb[j]) & (S < sb[j + 1])
        row.append('%5.1f' % np.log10(q[mm].max()) if mm.any() else '  .  ')
    print('t %.3f r %8.2e |' % (0.5 * (tb[i] + tb[i + 1]), np.median(r[m])) + ' '.join(row))
