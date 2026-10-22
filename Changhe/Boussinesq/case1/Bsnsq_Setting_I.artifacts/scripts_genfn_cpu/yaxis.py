"""Profiles along the y-axis (x -> 0+) of a genfn state: y, V/y = W2/y, W1/x, Theta/(a0 y) = eta/y, Omega/(x y), R/N.
Usage: python3 yaxis.py state.npz [x0]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from model import Model, fields
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c']); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
mod = Model(J, Kw, m=int(d['m']) if 'm' in d.files else 3, alpha=alpha, se=se, gam=gam)
if 'core' in d.files:    # core patch (model_core.py)
    from model_core import ModelCore; q_ = d['core']
    mod = ModelCore(J, Kw, q_, m=(int(d['m']) if 'm' in d.files else 3), alpha=alpha, se=se, gam=gam)
    c = torch.tensor(np.concatenate([d['c'], d['cc']]))
xs = float(sys.argv[2]) if len(sys.argv) > 2 else 1e-6
eta = torch.tensor(np.logspace(-3, 4.5, 76)); x = torch.full_like(eta, xs)
F = fields(mod.basis_matrix(x, eta) @ c, x, eta, a0, mod.beta)
y = F['y'].detach().numpy(); e = eta.numpy()
print('  eta        y          W2/y      W1/x      eta/y      Om/(xy)    Thx/(x)    R/N')
for i in range(len(e)):
    print('  %.3e  %.3e  %.5f  %.5f  %.4e  %+.4e  %+.4e  %.2e' % (e[i], y[i], F['W2'][i] / y[i], F['W1'][i] / xs, e[i] / y[i],
          F['Om'][i] / (xs * y[i]), F['Thx'][i] / xs, abs(F['R'][i] / F['N'][i])))
