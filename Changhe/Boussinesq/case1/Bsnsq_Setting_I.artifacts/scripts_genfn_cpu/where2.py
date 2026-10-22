"""Like where.py, but also reports the residual relative to the non-cancelling normalizer
N2 = |U1 Om_x| + |U2 Om_y| + |beta X.grad Om + Om| + |Theta_x| (U = W - beta X). In the far field
beta X.grad Om + Om cancels to O(r^(-2/3)) for the leading homogeneous term, so R/N ~ r^(-1/3) C while R/N2 ~ C
(C = next-order far-field coefficient of the vorticity equation). Usage: python3 where2.py state.npz [Nt Ns tmin]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from model import Model, fields, ts_to_xeta
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c']); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
Nt = int(sys.argv[2]) if len(sys.argv) > 2 else int(d['Nt']); Ns = int(sys.argv[3]) if len(sys.argv) > 3 else int(d['Ns'])
tmin = float(sys.argv[4]) if len(sys.argv) > 4 else float(d['tmin'])
m_ = int(d['m']) if 'm' in d.files else 3
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam); beta = mod.beta
if 'core' in d.files:    # core patch (model_core.py)
    from model_core import ModelCore; q_ = d['core']
    mod = ModelCore(J, Kw, q_, m=m_, alpha=alpha, se=se, gam=gam)
    c = torch.tensor(np.concatenate([d['c'], d['cc']]))
it = (np.arange(Nt) + 0.5) / Nt; is_ = (np.arange(Ns) + 0.5) / Ns
tau = 0.5 * (1 - np.cos(np.pi * it))
t = 1 - (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1) if alpha > 0 else tau
t = tmin + (1 - tmin) * t
s = 0.5 * (1 - np.cos(np.pi * is_))
if '--edges' in sys.argv:    # rows next to both axes (s -> 0: eta -> 0; s -> 1: x -> 0) and next to the centre (t -> 1)
    s = np.concatenate([s, [1e-10, 1e-7, 1e-5, 1e-4, 1e-3, 3e-3, 1 - 3e-3, 1 - 1e-3, 1 - 1e-4, 1 - 1e-5, 1 - 1e-7, 1 - 1e-10]])
    t = np.concatenate([t, 1 - np.array([1e-12, 1e-10, 1e-8, 1e-6, 1e-5, 1e-4])])
T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
x, eta = ts_to_xeta(T, S, m_, se)
keep = (x > 1e-12) & (eta > 1e-12)
x = torch.tensor(x[keep]); eta = torch.tensor(eta[keep])
q = []; q2 = []; ys = []
for ch in torch.split(torch.arange(x.shape[0]), 1500):
    F = fields(mod.basis_matrix(x[ch], eta[ch]) @ c, x[ch], eta[ch], a0, beta)
    y = F['y']; xc = x[ch]
    N2 = (F['U1'] * F['Ox']).abs() + (F['U2'] * F['Oy']).abs() + (beta * (xc * F['Ox'] + y * F['Oy']) + F['Om']).abs() + F['Thx'].abs()
    q.append((F['R'].abs() / F['N']).detach().numpy()); q2.append((F['R'].abs() / N2).detach().numpy()); ys.append(y.detach().numpy())
q = np.concatenate(q); q2 = np.concatenate(q2); y = np.concatenate(ys); r = np.hypot(x.numpy(), y); ph = np.degrees(np.arctan2(y, x.numpy()))
print('state %s a0 %.4f grid max R/N %.3e  R/N2 %.3e' % (sys.argv[1], a0, q.max(), q2.max()))
print('  max R/N2 [R/N] by band and physical angle:')
for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e6), (1e6, 1e13)]:
    row = []
    for plo, phi_ in [(0, 10), (10, 45), (45, 80), (80, 88), (88, 90.1)]:
        m = (r >= lo) & (r < hi) & (ph >= plo) & (ph < phi_)
        row.append('%.1e[%.1e]' % (q2[m].max(), q[m].max()) if m.any() else '        -         ')
    print('  r [%g, %g): ' % (lo, hi) + ' '.join(row))
