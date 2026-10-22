"""Locate the largest |R|/N of a genfn state on its own collocation grid (same grid as gsolve.py) and print the top
points in physical coordinates. Usage: python3 where.py state.npz [Nt Ns tmin ntop]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from model import Model, fields, ts_to_xeta
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c']); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
Nt = int(sys.argv[2]) if len(sys.argv) > 2 else int(d['Nt']); Ns = int(sys.argv[3]) if len(sys.argv) > 3 else int(d['Ns'])
tmin = float(sys.argv[4]) if len(sys.argv) > 4 else float(d['tmin']); ntop = int(sys.argv[5]) if len(sys.argv) > 5 else 12
m_ = int(d['m']) if 'm' in d.files else 3
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam)
it = (np.arange(Nt) + 0.5) / Nt; is_ = (np.arange(Ns) + 0.5) / Ns
tau = 0.5 * (1 - np.cos(np.pi * it))
t = 1 - (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1) if alpha > 0 else tau
t = tmin + (1 - tmin) * t
s = 0.5 * (1 - np.cos(np.pi * is_))
T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
S = S if gam <= 0 else (np.exp(gam * S) - 1) / (np.exp(gam) - 1)
x, eta = ts_to_xeta(T, S, m_, se)
keep = (x > 1e-12) & (eta > 1e-12)
x = torch.tensor(x[keep]); eta = torch.tensor(eta[keep]); T = T[keep]; S = S[keep]
q = []; ys = []
for ch in torch.split(torch.arange(x.shape[0]), 1500):
    F = fields(mod.basis_matrix(x[ch], eta[ch]) @ c, x[ch], eta[ch], a0, mod.beta)
    q.append((F['R'].abs() / F['N']).detach().numpy()); ys.append(F['y'].detach().numpy())
q = np.concatenate(q); y = np.concatenate(ys); r = np.hypot(x.numpy(), y); ph = np.degrees(np.arctan2(y, x.numpy()))
o = np.argsort(-q)[:ntop]
print('state %s a0 %.4f grid max %.3e' % (sys.argv[1], a0, q.max()))
print('   R/N        t          s        x          eta        r          phi(deg)')
for i in o: print('  %.3e  %.6f  %.6f  %.3e  %.3e  %.3e  %.4f' % (q[i], T[i], S[i], x[i], eta[i], r[i], ph[i]))
for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 1e3), (1e3, 1e6), (1e6, 1e13)]:
    m = (r >= lo) & (r < hi)
    if m.any(): print('  r [%g, %g): max %.3e  (%d pts)' % (lo, hi, q[m].max(), m.sum()))
print('  by band and physical angle (max R/N):')
for lo, hi in [(0, 0.03), (0.03, 0.1), (0.1, 0.3), (0.3, 1), (1, 3), (3, 10), (10, 100), (100, 1e4), (1e4, 1e13)]:
    row = []
    for plo, phi_ in [(0, 30), (30, 60), (60, 80), (80, 88), (88, 89.5), (89.5, 90.1)]:
        m = (r >= lo) & (r < hi) & (ph >= plo) & (ph < phi_)
        row.append('%.1e(%d)' % (q[m].max(), m.sum()) if m.any() else '   -    ')
    print('  r [%g, %g): ' % (lo, hi) + ' '.join(row))
