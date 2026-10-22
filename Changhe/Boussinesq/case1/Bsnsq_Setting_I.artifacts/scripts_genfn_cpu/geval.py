"""Off-grid evaluation of a generating-function state: R/N (prompt normalizer, no floor) on a shifted (t, sigma) grid,
by physical radius r = |(x, G_x)| and by angle; minimum of A; centre quantities. Usage: python3 geval.py state.npz [Nt Ns tmin shift]"""
import sys, math, json, numpy as np, torch
torch.set_num_threads(1)
from jets import Jet, monos, DT
from model import Model, fields, ts_to_xeta
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = d['c']; a0 = float(d['a0'])
Nt = int(sys.argv[2]) if len(sys.argv) > 2 else 3 * J + 11
Ns = int(sys.argv[3]) if len(sys.argv) > 3 else 3 * Kw + 11
tmin = float(sys.argv[4]) if len(sys.argv) > 4 else 0.005
shift = float(sys.argv[5]) if len(sys.argv) > 5 else 0.37
alpha = float(d['alpha']) if 'alpha' in d.files else 0.0
se = float(sys.argv[sys.argv.index('--se') + 1]) if '--se' in sys.argv else (float(d['se']) if 'se' in d.files else 1.0)
gam = float(sys.argv[sys.argv.index('--gam') + 1]) if '--gam' in sys.argv else (float(d['gam']) if 'gam' in d.files else 0.0)
m_ = int(d['m']) if 'm' in d.files else 3
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam)
it = (np.arange(Nt) + shift) / Nt; is_ = (np.arange(Ns) + shift) / Ns
tau = 0.5 * (1 - np.cos(np.pi * it)); t = tau if alpha <= 0 else 1 - (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1); t = tmin + (1 - tmin) * t; s = 0.5 * (1 - np.cos(np.pi * is_))
T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
S = S if gam <= 0 else (np.exp(gam * S) - 1) / (np.exp(gam) - 1)
x, eta = ts_to_xeta(T, S, m_, se)
k = (x > 1e-12) & (eta > 1e-12); x = torch.tensor(x[k]); eta = torch.tensor(eta[k])
res = []; chunks = torch.split(torch.arange(x.shape[0]), 2000)
F = {}
for ch in chunks:
    Bm = mod.basis_matrix(x[ch], eta[ch])
    Fc = fields(Bm @ torch.tensor(c), x[ch], eta[ch], a0, mod.beta)
    for kk, v in Fc.items(): F.setdefault(kk, []).append(v.detach().numpy())
F = {kk: np.concatenate(v) for kk, v in F.items()}
xx = x.numpy(); yy = F['y']; r = np.hypot(xx, yy); ph = np.degrees(np.arctan2(yy, xx))
q = np.abs(F['R']) / F['N']
print('state %s  J %d Kw %d a0 %.5f  points %d  min A %.6f  max A %.4e' % (sys.argv[1], J, Kw, a0, len(q), F['A'].min(), F['A'].max()))
for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 1e2), (1e2, 1e4), (1e4, 1e6), (1e6, 1e12)]:
    m = (r >= lo) & (r < hi)
    if m.any():
        i = np.argmax(np.where(m, q, -1))
        print('  r in [%g,%g): max |R|/N %.3e (at r %.3g, phi %.1f deg)  median %.2e  max |R| %.2e  (%d pts)' % (lo, hi, q[m].max(), r[i], ph[i], np.median(q[m]), np.abs(F['R'][m]).max(), m.sum()))
for lo, hi in [(0, 10), (10, 80), (80, 90)]:
    m = (ph >= lo) & (ph <= hi) & (r < 10)
    if m.any(): print('  r<10, phi in [%g,%g] deg: max |R|/N %.3e' % (lo, hi, q[m].max()))
# far-field growth exponents of U and Omega along phi = 45 deg-ish: fit log|U| vs log r at large r
m = (r > 1e3)
if m.sum() > 10:
    U = np.hypot(F['U1'], F['U2'])
    A_ = np.vstack([np.log(r[m]), np.ones(m.sum())]).T
    print('  far field: max |U|/r (r>1e3) %.3e ; max |Omega| r^(1/3) %.3e' % ((U[m] / r[m]).max(), (np.abs(F['Om'][m]) * r[m] ** (1 / 3)).max()))
U = np.hypot(F['U1'], F['U2'])
for lo in [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8]:
    m = (r >= lo) & (r < 10 * lo)
    if m.any(): print('  r in [%g,%g): max|U|/r %.3e  max|U|/r^(2/3) %.3e  max|Om| r^(1/3) %.3e  max Theta/r^(1/3) %.3e' % (lo, 10 * lo, (U[m] / r[m]).max(), (U[m] / r[m] ** (2 / 3)).max(), (np.abs(F['Om'][m]) * r[m] ** (1 / 3)).max(), (a0 * eta.numpy()[m] / r[m] ** (1 / 3)).max()))
