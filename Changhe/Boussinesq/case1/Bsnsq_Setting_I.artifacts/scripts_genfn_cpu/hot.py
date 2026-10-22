"""Locate the residual maximum of a genfn state (outer or core) on a box in (x, eta): log-spaced x, linear eta.
Prints the top points (x, eta, physical y, r, angle, R/N, R/N2) and the maxima per eta row.
Usage: python3 hot.py state.npz xmin xmax nx emin emax ne [top]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from model import Model, fields
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c']); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
m_ = int(d['m']) if 'm' in d.files else 3
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam); beta = mod.beta
if 'core' in d.files:
    from model_core import ModelCore
    mod = ModelCore(J, Kw, d['core'], m=m_, alpha=alpha, se=se, gam=gam); c = torch.tensor(np.concatenate([d['c'], d['cc']]))
xmin, xmax, nx, emin, emax, ne = float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), int(sys.argv[7])
top = int(sys.argv[8]) if len(sys.argv) > 8 else 12
xs = np.logspace(np.log10(xmin), np.log10(xmax), nx); es = np.linspace(emin, emax, ne)
X, H = np.meshgrid(xs, es, indexing='ij'); x = torch.tensor(X.ravel()); eta = torch.tensor(H.ravel())
q = []; q2 = []; ys = []
for ch in torch.split(torch.arange(x.shape[0]), 1500):
    F = fields(mod.basis_matrix(x[ch], eta[ch]) @ c, x[ch], eta[ch], a0, beta)
    y = F['y']; xc = x[ch]
    N2 = (F['U1'] * F['Ox']).abs() + (F['U2'] * F['Oy']).abs() + (beta * (xc * F['Ox'] + y * F['Oy']) + F['Om']).abs() + F['Thx'].abs()
    q.append((F['R'].abs() / F['N']).detach().numpy()); q2.append((F['R'].abs() / N2).detach().numpy()); ys.append(y.detach().numpy())
q = np.concatenate(q); q2 = np.concatenate(q2); y = np.concatenate(ys); xn = x.numpy(); en = eta.numpy()
r = np.hypot(xn, y); ph = np.degrees(np.arctan2(y, xn)); mx = np.maximum(q, q2)
print('state %s a0 %.4f box x [%g, %g] eta [%g, %g]: max R/N %.3e R/N2 %.3e' % (sys.argv[1], a0, xmin, xmax, emin, emax, q.max(), q2.max()))
for i in np.argsort(-mx)[:top]:
    print('  x %.4e eta %.4f y %.4e r %.4e phi %.3f  R/N %.3e R/N2 %.3e' % (xn[i], en[i], y[i], r[i], ph[i], q[i], q2[i]))
M = mx.reshape(nx, ne)
print('  max over x by eta:', ' '.join('%.2f:%.1e' % (es[j], M[:, j].max()) for j in range(0, ne, max(1, ne // 16))))
print('  max over eta by x:', ' '.join('%.0e:%.1e' % (xs[i], M[i, :].max()) for i in range(0, nx, max(1, nx // 16))))
