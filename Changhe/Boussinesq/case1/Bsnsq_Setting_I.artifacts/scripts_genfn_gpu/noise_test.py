"""Roundoff test of the residual rows: evaluate R/N and R/N2 on the solver grid (Nt Ns tmin) for the state and for the state with a
relative 1e-14 random perturbation of the coefficients; report max |delta| by radius band next to the max value. Usage: noise_test.py state Nt Ns tmin"""
import sys, numpy as np, torch
import jets; DEV = jets.DEV
from model import Model, fields, ts_to_xeta
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c'], device=DEV); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']); m_ = int(d['m']); mod = Model(J, Kw, m=m_, alpha=alpha, se=se); beta = mod.beta
if 'core' in d.files:
    from model_core import ModelCore
    mod = ModelCore(J, Kw, d['core'], m=m_, alpha=alpha, se=se); c = torch.tensor(np.concatenate([d['c'], d['cc']]), device=DEV)
Nt, Ns, tmin = int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
it = (np.arange(Nt) + 0.5) / Nt; is_ = (np.arange(Ns) + 0.5) / Ns; tau = 0.5 * (1 - np.cos(np.pi * it))
t = 1 - (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1); t = tmin + (1 - tmin) * t; s = 0.5 * (1 - np.cos(np.pi * is_))
T, S = np.meshgrid(t, s, indexing='ij'); x, eta = ts_to_xeta(T.ravel(), S.ravel(), m_, se); keep = (x > 1e-12) & (eta > 1e-12)
x = torch.tensor(x[keep], device=DEV); eta = torch.tensor(eta[keep], device=DEV)
def ev(cc):
    q = []; q2 = []; ys = []
    for ch in torch.split(torch.arange(x.shape[0], device=DEV), 4096):
        F = fields(mod.basis_matrix(x[ch], eta[ch]) @ cc, x[ch], eta[ch], a0, beta); y = F['y']; xc = x[ch]
        N2 = (F['U1'] * F['Ox']).abs() + (F['U2'] * F['Oy']).abs() + (beta * (xc * F['Ox'] + y * F['Oy']) + F['Om']).abs() + F['Thx'].abs()
        q.append((F['R'] / F['N']).detach()); q2.append((F['R'] / N2).detach()); ys.append(y.detach())
    return torch.cat(q).cpu().numpy(), torch.cat(q2).cpu().numpy(), torch.cat(ys).cpu().numpy()
torch.manual_seed(0)
q, q2, y = ev(c); cp = c * (1 + 1e-14 * torch.randn_like(c)); qp, q2p, _ = ev(cp)
r = np.hypot(x.cpu().numpy(), y)
print('grid %d x %d tmin %g: smallest t %.3e, largest r %.3e' % (Nt, Ns, tmin, t.min(), r.max()))
print('band            max|R/N2|   max|dR/N2| (1e-14 rel. perturbation)   max|R/N|    max|dR/N|')
for lo, hi in [(0, 1), (1, 1e2), (1e2, 1e4), (1e4, 1e6), (1e6, 1e8), (1e8, 1e10), (1e10, 1e14)]:
    m = (r >= lo) & (r < hi)
    if m.any(): print('[%g, %g):   %.2e     %.2e                               %.2e    %.2e' % (lo, hi, np.abs(q2[m]).max(), np.abs(q2[m] - q2p[m]).max(), np.abs(q[m]).max(), np.abs(q[m] - qp[m]).max()))
