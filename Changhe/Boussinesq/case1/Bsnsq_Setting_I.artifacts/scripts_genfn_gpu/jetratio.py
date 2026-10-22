"""Centre Taylor jets of a generating-function state (beta-aware; CPU by default: run with CUDA_VISIBLE_DEVICES=).
Fields are evaluated with model.fields from the matrix-free jets (ModelFB / ModelCoreFB.g_jet) at points (x, eta) with physical
radius r = hypot(x, y) in [r1, r2]; least-squares fits in the physical monomials {1, x^2, y^2, x^4, x^2 y^2, y^4} of
  Psi/(x y) = d0 + d1 x^2 + d2 y^2 + ...,  Omega/(x y) = g + ...,  Theta_x/(x y) = 2 b1 + ...,  Theta_y = a0 + b1 x^2 + 3 b2 y^2 + ...
(Theta = a0 y + b1 x^2 y + b2 y^3 + ..., Psi = x y (d0 + d1 x^2 + d2 y^2) + ..., Omega = x y (g + ...)); d0 = Psi_xy(0) must be -2.
Prints the jet relations (derived from W.grad Theta = (beta-2) Theta at order 3 and the centre vorticity relations; b = beta - 2) as relative
defects: 2 (beta+2) b1 + 3 a0 d1 = 0, 2 b b2 + a0 d2 = 0, (2 beta+1) g = 2 b1,
g = -6 (d1 + d2), and the horizontal-curvature ratio -6 d1/g against C_beta/a0, C_beta = 2 (beta+2)(2 beta+1) (= 70 at beta 3).
Usage: python3 jetratio.py state.npz [--r1 2e-3] [--r2 4e-2] [--nr 24] [--nth 16]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from jets import DT
from model import fields
from model_fb import ModelFB
from model_core_fb import ModelCoreFB
d = np.load(sys.argv[1])
def opt(name, default, typ=float):
    return typ(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default
r1, r2, nr, nth = opt('--r1', 2e-3), opt('--r2', 4e-2), opt('--nr', 24, int), opt('--nth', 16, int)
J, Kw = int(d['J']), int(d['Kw']); beta = float(d['beta']) if 'beta' in d.files else 3.0; M = int(d['M']) if 'M' in d.files else 3
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0; a0 = float(d['a0'])
if 'core' in d.files:
    mod = ModelCoreFB(J, Kw, d['core'], beta=beta, M=M, alpha=alpha, se=se, gam=gam); c = np.concatenate([d['c'], d['cc']])
else:
    mod = ModelFB(J, Kw, beta=beta, M=M, alpha=alpha, se=se, gam=gam); c = d['c']
rho = np.exp(np.linspace(np.log(r1), np.log(r2), nr)); th = 0.5 * np.pi * (np.arange(nth) + 0.5) / nth
Rr, Th = np.meshgrid(rho, th, indexing='ij'); x = torch.tensor((Rr * np.cos(Th)).ravel(), dtype=DT); eta = torch.tensor((Rr * np.sin(Th)).ravel(), dtype=DT)
with torch.no_grad():
    F = fields(mod.g_jet(torch.as_tensor(c, dtype=DT), x, eta), x, eta, a0, beta)
x = x.numpy(); y = F['y'].numpy(); r = np.hypot(x, y); keep = (r >= r1) & (r <= r2)
x, y = x[keep], y[keep]; xy = x * y
A = np.stack([np.ones_like(x), x**2, y**2, x**4, x**2 * y**2, y**4], 1)
def fit(v): return np.linalg.lstsq(A, v, rcond=None)[0]
dp = fit(F['Psi'].numpy()[keep] / xy); go = fit(F['Om'].numpy()[keep] / xy); tx = fit(F['Thx'].numpy()[keep] / xy); ty = fit(F['Thy'].numpy()[keep])
d0, d1, d2 = dp[0], dp[1], dp[2]; g = go[0]; b1 = tx[0] / 2; b1y, b2 = ty[1], ty[2] / 3; a0fit = ty[0]
b = beta - 2; Cb = 2 * (beta + 2) * (2 * beta + 1)
print('state %s  beta %.6f  a0 %.6f  fit radii [%g, %g] (%d points)' % (sys.argv[1], beta, a0, r1, r2, int(keep.sum())))
print('  d0 = Psi_xy(0) = %.10f (must be -2; defect %.2e)   a0 (fit of Theta_y) = %.6f (rel defect %.2e)' % (d0, d0 + 2, a0fit, a0fit / a0 - 1))
print('  d1 %.8e  d2 %.8e  g %.8e  b1 %.8e (from Theta_x; from Theta_y: %.8e)  b2 %.8e' % (d1, d2, g, b1, b1y, b2))
print('  jet relations (relative defects): 2(beta+2) b1 + 3 a0 d1: %.2e | 2 b b2 + a0 d2: %.2e | (2beta+1) g - 2 b1: %.2e | g + 6 (d1 + d2): %.2e' % (
    (2 * (beta + 2) * b1 + 3 * a0 * d1) / abs(3 * a0 * d1), (2 * b * b2 + a0 * d2) / abs(a0 * d2), ((2 * beta + 1) * g - 2 * b1) / abs(2 * b1), (g + 6 * (d1 + d2)) / abs(g)))
print('  horizontal-curvature ratio -6 d1/g = %.8f   C_beta/a0 = %.8f (C_beta = %.1f)   rel diff %.2e' % (-6 * d1 / g, Cb / a0, Cb, (-6 * d1 / g) / (Cb / a0) - 1))
