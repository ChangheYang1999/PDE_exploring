"""Regional absolute residuals of a beta-3 generating-function state on the dense where2 grid (Nt x Ns Chebyshev rows + axis/centre edges), in
the format of the authors' FINAL_REPORT regional table: 20 bands of log radius from 1e-8 to 1e8, sampled maxima (not suprema) of |R_Omega|,
|R_Omega/(x y)| (desingularized), R/N_Omega and R/N2 per band. R_Theta vanishes identically in this representation (Theta is transported
exactly in the chart). Usage: python3 regtab.py state.npz [Nt Ns tmin] [--edges]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
import jets; DEV = jets.DEV
from model import Model, fields, ts_to_xeta
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c'], device=DEV); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
args = [a for a in sys.argv[2:] if not a.startswith('--')]
Nt = int(args[0]) if len(args) > 0 else 241; Ns = int(args[1]) if len(args) > 1 else 300; tmin = float(args[2]) if len(args) > 2 else 1e-4
m_ = int(d['m']) if 'm' in d.files else 3
if abs((float(d['beta']) if 'beta' in d.files else 3.0) - 3.0) > 1e-12: raise SystemExit('beta-3 states only (model.Model)')
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam); beta = mod.beta
if 'core' in d.files:
    from model_core import ModelCore; mod = ModelCore(J, Kw, d['core'], m=m_, alpha=alpha, se=se, gam=gam); c = torch.tensor(np.concatenate([d['c'], d['cc']]), device=DEV)
it = (np.arange(Nt) + 0.5) / Nt; is_ = (np.arange(Ns) + 0.5) / Ns
tau = 0.5 * (1 - np.cos(np.pi * it)); t = 1 - (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1) if alpha > 0 else tau
t = tmin + (1 - tmin) * t; s = 0.5 * (1 - np.cos(np.pi * is_))
if '--edges' in sys.argv:
    s = np.concatenate([s, [1e-10, 1e-7, 1e-5, 1e-4, 1e-3, 3e-3, 1 - 3e-3, 1 - 1e-3, 1 - 1e-4, 1 - 1e-5, 1 - 1e-7, 1 - 1e-10]])
    t = np.concatenate([t, 1 - np.array([1e-12, 1e-10, 1e-8, 1e-6, 1e-5, 1e-4])])
T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
x, eta = ts_to_xeta(T, S, m_, se); keep = (x > 1e-12) & (eta > 1e-12)
x = torch.tensor(x[keep], device=DEV); eta = torch.tensor(eta[keep], device=DEV)
R = []; N = []; N2 = []; Y = []
with torch.no_grad():
    for ch in torch.split(torch.arange(x.shape[0], device=DEV), 4096):
        F = fields(mod.basis_matrix(x[ch], eta[ch]) @ c, x[ch], eta[ch], a0, beta); y = F['y']; xc = x[ch]
        n2 = (F['U1'] * F['Ox']).abs() + (F['U2'] * F['Oy']).abs() + (beta * (xc * F['Ox'] + y * F['Oy']) + F['Om']).abs() + F['Thx'].abs()
        R.append(F['R'].cpu().numpy()); N.append(F['N'].cpu().numpy()); N2.append(n2.cpu().numpy()); Y.append(y.cpu().numpy())
R = np.concatenate(R); N = np.concatenate(N); N2 = np.concatenate(N2); y = np.concatenate(Y); x = x.cpu().numpy(); r = np.hypot(x, y)
print('state %s a0 %.4f: %d dense points%s; sampled maxima per band of r (binary64 direct evaluation; beyond r ~ 1e8 the direct rows are rounding noise and are omitted)' % (sys.argv[1], a0, len(R), ' (with edges)' if '--edges' in sys.argv else ''))
print('| r band | max abs R_Omega | max abs R_Omega/(xy) | max R/N_Omega | max R/N2 | points |')
print('|---|---|---|---|---|---|')
edges = np.logspace(-8, 8, 21); rows = []
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (r >= lo) & (r < hi)
    if not m.any(): print('| %.1e to %.1e | - | - | - | - | 0 |' % (lo, hi)); continue
    vals = (np.abs(R[m]).max(), np.abs(R[m] / (x[m] * y[m])).max(), np.abs(R[m] / N[m]).max(), np.abs(R[m] / N2[m]).max()); rows.append(vals)
    print('| %.1e to %.1e | %.2e | %.2e | %.2e | %.2e | %d |' % (lo, hi, *vals, int(m.sum())))
m = (r >= 1e-8) & (r < 1e8); print('| all (1e-8 <= r < 1e8) | %.2e | %.2e | %.2e | %.2e | %d |' % (np.abs(R[m]).max(), np.abs(R[m] / (x[m] * y[m])).max(), np.abs(R[m] / N[m]).max(), np.abs(R[m] / N2[m]).max(), int(m.sum())))
i = np.argmax(np.where(m, np.abs(R / N2), 0)); j = np.argmax(np.where(m, np.abs(R / N), 0))
print('max R/N2 at (x, y) = (%.3e, %.3e), max R/N at (%.3e, %.3e); points with r < 1e-8: %d (smallest r %.1e)' % (x[i], y[i], x[j], y[j], int((r < 1e-8).sum()), r.min()))
