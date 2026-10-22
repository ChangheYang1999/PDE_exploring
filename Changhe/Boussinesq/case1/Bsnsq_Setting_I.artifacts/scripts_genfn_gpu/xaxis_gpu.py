"""Amplitude test along the horizontal axis (eta -> 0+) of a genfn state (float version of the centre/far-axis comparison).
R = S1 + a0 S2 with S2 = B0/A (= -Theta_x/a0) and S1 = W1 Omega_x + b eta Omega_eta + Omega; both are odd in eta, so
a0*(x) = -S1/S2 is the amplitude that would make the eta-desingularized residual vanish at (x, 0+) with G fixed.
x -> 0: the centre (order-xy) identity; x -> infinity: the far-axis next-order condition C = 0. Also R/N and R/N2.
Usage: python3 xaxis.py state.npz [eps]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
import jets
DEV = jets.DEV
from model import Model, fields
# [numerics GPU version of the authors' xaxis.py]
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c'], device=DEV); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
mod = Model(J, Kw, m=int(d['m']) if 'm' in d.files else 3, alpha=alpha, se=se, gam=gam)
if 'core' in d.files:
    from model_core import ModelCore
    mod = ModelCore(J, Kw, d['core'], m=(int(d['m']) if 'm' in d.files else 3), alpha=alpha, se=se, gam=gam)
    c = torch.tensor(np.concatenate([d['c'], d['cc']]), device=DEV)
es = float(sys.argv[2]) if len(sys.argv) > 2 else 1e-6
x = torch.tensor(np.logspace(-4, 10, 57), device=DEV); eta = torch.full_like(x, es)
F = fields(mod.basis_matrix(x, eta) @ c, x, eta, a0, mod.beta)
F = {k: v.detach().cpu() for k, v in F.items()}; x = x.cpu()
S2 = -F['Thx'] / a0; S1 = F['R'] - a0 * S2
N2 = (F['U1'] * F['Ox']).abs() + (F['U2'] * F['Oy']).abs() + (mod.beta * (x * F['Ox'] + F['y'] * F['Oy']) + F['Om']).abs() + F['Thx'].abs()
print('state a0 %.6f' % a0)
print('  x          a0*(x)        R/N        R/N2       R/(eta x^(1/3))')
for i in range(len(x)):
    print('  %.3e  %+.6e  %.2e  %.2e  %+.4e' % (x[i], -S1[i] / S2[i], abs(F['R'][i] / F['N'][i]), abs(F['R'][i] / N2[i]),
          F['R'][i] / es * float(x[i]) ** (1 / 3)))
