"""Vertical-axis traces of a generating-function state (beta = 3 states; a0 = Theta_y(0)).
On x = 0, for heights y on a log grid, report  z(y) = Omega_x(0, y),  s(y) = Theta_xx(0, y),  C(y) = U2_xx(0, y)  and the first heights with
C < 0, s > 0, z > 0 (the authors' 2026-10-21T23:03Z question; Proposition 37(d) of the authors' report: order 0 < y_C < y_s < y_z when g < 0).
Method: physical-space root inversion (gphys_local.py: solve G_x(x, eta) = y for eta) at x = 0, h, 2h with h = hrel * max(y, 0.1);
z from the model's exact Omega_x at x = 0 (cross-check: (8 Om(h) - Om(2h)) / (6h)); s from the odd function Theta_x: (8 Thx(h) - Thx(2h)) / (6h)
(cross-check: second difference of a0 eta); C from the even function U2: (16 (U2(h) - U2(0)) - (U2(2h) - U2(0))) / (6 h^2). Richardson-corrected
differences, truncation O(h^4). Usage: python3 vaxis.py state.npz [ymin ymax ny] [--hrel 1e-3]"""
import sys, math, numpy as np, torch
torch.set_num_threads(1)
import jets
DEV = jets.DEV
from jets import monos, DT
from model import Model, fields
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c'], device=DEV); a0 = float(d['a0'])
alpha = float(d['alpha']) if 'alpha' in d.files else 0.0
se = float(d['se']) if 'se' in d.files else 1.0
gam = float(d['gam']) if 'gam' in d.files else 0.0
m_ = int(d['m']) if 'm' in d.files else 3
assert int(d['fb']) == 0 if 'fb' in d.files else True, 'beta-3 (fixed-m) states only'
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam)
if 'core' in d.files:
    from model_core import ModelCore; mod = ModelCore(J, Kw, d['core'], m=m_, alpha=alpha, se=se, gam=gam)
    c = torch.tensor(np.concatenate([d['c'], d['cc']]), device=DEV)
args = [a for a in sys.argv[2:] if not a.startswith('--')]
ymin = float(args[0]) if len(args) > 0 else 1e-3; ymax = float(args[1]) if len(args) > 1 else 1e6; ny = int(args[2]) if len(args) > 2 else 181
hrel = float(sys.argv[sys.argv.index('--hrel') + 1]) if '--hrel' in sys.argv else 1e-3
L1, ix1 = monos(1); L2, ix2 = monos(2)
def Gx_of(x, e): return (mod.basis_matrix(x, e, p=1)[ix1[(1, 0)]] @ c)
def eta_of(x, y):
    lo = torch.zeros_like(y); hi = torch.maximum(y, torch.ones_like(y)) * 1e-3
    for _ in range(200):
        g = Gx_of(x, hi); m = g < y
        if not m.any(): break
        lo = torch.where(m, hi, lo); hi = torch.where(m, hi * 4, hi)
    for _ in range(80):
        mid = 0.5 * (lo + hi); g = Gx_of(x, mid); m = g < y
        lo = torch.where(m, mid, lo); hi = torch.where(m, hi, mid)
    e = 0.5 * (lo + hi)
    for _ in range(4):
        B = mod.basis_matrix(x, e, p=2) @ c
        e = e - (B[ix2[(1, 0)]] - y) / B[ix2[(1, 1)]]
    return e
def phys(x, y):
    e = eta_of(x, y); F = fields(mod.basis_matrix(x, e) @ c, x, e, a0, mod.beta); F['eta'] = e; return F
yv = torch.tensor(np.logspace(math.log10(ymin), math.log10(ymax), ny), dtype=DT, device=DEV)
h = hrel * torch.clamp(yv, min=0.1)
F0 = phys(torch.zeros_like(yv), yv); F1 = phys(h, yv); F2 = phys(2 * h, yv)
yerr = max(float(((F['y'] - yv).abs() / yv).max()) for F in (F0, F1, F2))
z = F0['Ox']; z_fd = (8 * F1['Om'] - F2['Om']) / (6 * h)
s = (8 * F1['Thx'] - F2['Thx']) / (6 * h); s_fd = a0 * (16 * (F1['eta'] - F0['eta']) - (F2['eta'] - F0['eta'])) / (6 * h ** 2)
C = (16 * (F1['U2'] - F0['U2']) - (F2['U2'] - F0['U2'])) / (6 * h ** 2)
cpu = lambda t: t.detach().cpu().numpy()
yv, z, z_fd, s, s_fd, C = map(cpu, (yv, z, z_fd, s, s_fd, C))
print('state %s  a0 %.4f  beta %.3f  heights %d in [%g, %g]  hrel %g  max rel |G_x - y|/y %.1e' % (sys.argv[1], a0, mod.beta, ny, ymin, ymax, hrel, yerr))
iz = np.argmax(np.abs(z - z_fd) / np.abs(z)); is_ = np.argmax(np.abs(s - s_fd) / np.abs(s))
print('  cross-checks (pointwise relative): max rel |z - z_fd| %.1e at y %.3e (z %.4e z_fd %.4e)   max rel |s - s_fd| %.1e at y %.3e (s %.4e s_fd %.4e); medians %.1e / %.1e' % (
      np.abs(z - z_fd)[iz] / np.abs(z)[iz], yv[iz], z[iz], z_fd[iz], np.abs(s - s_fd)[is_] / np.abs(s)[is_], yv[is_], s[is_], s_fd[is_],
      np.median(np.abs(z - z_fd) / np.abs(z)), np.median(np.abs(s - s_fd) / np.abs(s))))
print('  centre values (smallest height y = %.1e): z = %.6e (z1 = Omega_xy(0) ~ z/y: %.6e)  s = %.6e (s/y: %.6e)  C = %.6e (C/y: %.6e)' % (yv[0], z[0], z[0] / yv[0], s[0], s[0] / yv[0], C[0], C[0] / yv[0]))
def runs(name, v, want):
    sg = np.sign(v); out = []; start = 0
    for i in range(1, len(v) + 1):
        if i == len(v) or sg[i] != sg[start]:
            out.append('%s on [%.3e, %.3e]' % ({1: '+', -1: '-', 0: '0'}[int(sg[start])], yv[start], yv[i - 1])); start = i
    first = np.where(want(v))[0]
    fy = ('first height with the asked sign: %.4e' % yv[first[0]]) if len(first) else 'asked sign NOT found on the grid'
    print('  %s: sign runs: %s;  %s' % (name, ' | '.join(out), fy))
    return yv[first[0]] if len(first) else np.inf
yC = runs('C = U2_xx(0, y)   (asked: C < 0)', C, lambda v: v < 0)
ys = runs('s = Theta_xx(0, y) (asked: s > 0)', s, lambda v: v > 0)
yz = runs('z = Omega_x(0, y)  (asked: z > 0)', z, lambda v: v > 0)
print('  order of the first heights: y_C %.4e  y_s %.4e  y_z %.4e  ->  %s' % (yC, ys, yz, 'y_C < y_s < y_z' if yC < ys < yz else 'NOT y_C < y_s < y_z'))
print('  table (y, z, s, C, rel |z - z_fd|, rel |s - s_fd|; the finite differences lose accuracy where |Om(h)|, |Thx(h)| are small against the evaluation error, far field):')
for i in range(0, ny, max(1, ny // 30)):
    print('    %.3e  %+.6e  %+.6e  %+.6e   %.1e  %.1e' % (yv[i], z[i], s[i], C[i], abs(z[i] - z_fd[i]) / abs(z[i]), abs(s[i] - s_fd[i]) / abs(s[i])))
