"""Far-field angular structure of a genfn state: at fixed t (radial variable), H = G/(x eta E^(1/3)), physical angle phi
and Omega r^(1/3), Theta r^(-1/3) as functions of w. Usage: python3 hfar.py state.npz [t]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from model import Model, fields
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c']); a0 = float(d['a0'])
alpha = float(d['alpha']) if 'alpha' in d.files else 0.0
se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
mod = Model(J, Kw, alpha=alpha, se=se, gam=gam)
tt = float(sys.argv[2]) if len(sys.argv) > 2 else 0.03
S = np.array([1e-3, 0.01, 0.03, 0.06, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 0.999])
E = tt ** -6.0; wmax = (1 - tt ** 6) ** (1 / 3); w = wmax * S; u = np.maximum(1 - tt ** 6 - w ** 3, 0)
x = torch.tensor(np.sqrt(E * u)); eta = torch.tensor(se * np.sqrt(w) * E ** (1 / 6))
F = fields(mod.basis_matrix(x, eta) @ c, x, eta, a0, mod.beta)
G = (mod.basis_matrix(x, eta, p=0)[0] @ c).numpy()
H = G / (x.numpy() * eta.numpy() * E ** (1 / 3))
y = F['y'].numpy(); r = np.hypot(x.numpy(), y); ph = np.degrees(np.arctan2(y, x.numpy()))
print('t %.3f (E^(1/2) %.3g)  a0 %.3f' % (tt, E ** 0.5, a0))
print('     w        phi(deg)      r         H        Omega r^(1/3)   Theta r^(-1/3)   R/N')
for i in range(len(S)):
    print('  %7.4f  %12.6f  %9.3e  %10.4f  %12.4e  %12.4e  %9.2e' % (w[i], ph[i], r[i], H[i], float(F['Om'][i]) * r[i] ** (1 / 3),
          a0 * float(eta[i]) / r[i] ** (1 / 3), abs(float(F['R'][i])) / float(F['N'][i])))
