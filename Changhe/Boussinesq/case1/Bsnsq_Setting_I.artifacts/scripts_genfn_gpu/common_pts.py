"""Absolute field values of several generating-function states at COMMON physical points (authors' G3 requirement: absolute values at common points, not
only functionals). For each physical (x, y) of the quadrant the chart is inverted (G_x(x, eta) = y, bisection + Newton, as in gphys_local.py) and the fields
of model.fields are evaluated: eta (Theta = a0 eta h-normalized as stored), Om (Omega), Psi, W1, W2 (beta X + U), A (= G_x,eta). Prints the values for the
first state and the absolute and relative differences of every other state from it. CPU is enough (run with CUDA_VISIBLE_DEVICES=).
Usage: common_pts.py STATE1 STATE2 ... [--pts x1,y1;x2,y2;...]"""
import sys, math, numpy as np, torch
torch.set_num_threads(1)
import jets
DEV = jets.DEV
from jets import monos, DT
from model import Model, fields
L1, ix1 = monos(1); L2, ix2 = monos(2)
PTS = [(1e-3, 1e-2), (1e-2, 1e-2), (1e-2, 0.1), (0.1, 0.1), (0.1, 1.0), (1.0, 0.1), (1.0, 1.0), (1.0, 10.0), (10.0, 1.0), (10.0, 10.0), (100.0, 100.0), (1e3, 1e3), (1e4, 1e4), (1e3, 10.0), (10.0, 1e3)]
if '--pts' in sys.argv:
    PTS = [tuple(float(v) for v in p.split(',')) for p in sys.argv[sys.argv.index('--pts') + 1].split(';')]
files = [a for a in sys.argv[1:] if a.endswith('.npz')]

def load(f):
    d = np.load(f); J, Kw = int(d['J']), int(d['Kw']); a0 = float(d['a0'])
    alpha = float(d['alpha']) if 'alpha' in d.files else 0.0; se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
    m_ = int(d['m']) if 'm' in d.files else 3
    beta = float(d['beta']) if 'beta' in d.files else 3.0
    if 'fb' in d.files and int(d['fb']) == 1:    # free-exponent basis (gsolve_fbg states): use the FB models with the stored beta (fix 2026-10-21T18:2xZ, review s329review item 15)
        M = int(d['M']) if 'M' in d.files else 3
        if 'core' in d.files:
            from model_core_fb import ModelCoreFB; mod = ModelCoreFB(J, Kw, d['core'], beta=beta, M=M, alpha=alpha, se=se, gam=gam); c = torch.tensor(np.concatenate([d['c'], d['cc']]), device=DEV)
        else:
            from model_fb import ModelFB; mod = ModelFB(J, Kw, beta=beta, M=M, alpha=alpha, se=se, gam=gam); c = torch.tensor(d['c'], device=DEV)
        print('%s: fb = 1 basis (beta %.6f, M %d)' % (f.split('/')[-1], beta, M))
    elif 'core' in d.files:
        from model_core import ModelCore; mod = ModelCore(J, Kw, d['core'], m=m_, alpha=alpha, se=se, gam=gam); c = torch.tensor(np.concatenate([d['c'], d['cc']]), device=DEV)
    else:
        mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam); c = torch.tensor(d['c'], device=DEV)
    return mod, c, a0, beta

def eta_of(mod, c, x, y):
    Gx = lambda e: (mod.basis_matrix(x, e, p=1)[ix1[(1, 0)]] @ c)
    lo = torch.zeros_like(y); hi = torch.maximum(y, torch.ones_like(y)) * 1e-3
    for _ in range(200):
        g = Gx(hi); m = g < y
        if not m.any(): break
        lo = torch.where(m, hi, lo); hi = torch.where(m, hi * 4, hi)
    for _ in range(80):
        mid = 0.5 * (lo + hi); g = Gx(mid); m = g < y
        lo = torch.where(m, mid, lo); hi = torch.where(m, hi, mid)
    e = 0.5 * (lo + hi)
    for _ in range(4):
        B = mod.basis_matrix(x, e, p=2) @ c
        e = e - (B[ix2[(1, 0)]] - y) / B[ix2[(1, 1)]]
    return e

KEYS = ['eta', 'Om', 'Psi', 'W1', 'W2', 'A']
vals = {}
for f in files:
    mod, c, a0, beta = load(f)
    x = torch.tensor([p[0] for p in PTS], dtype=DT, device=DEV); y = torch.tensor([p[1] for p in PTS], dtype=DT, device=DEV)
    e = eta_of(mod, c, x, y)
    F = fields(mod.basis_matrix(x, e) @ c, x, e, a0, beta); F['eta'] = e
    vals[f] = {k: F[k].detach().cpu().numpy() for k in KEYS if k in F}
    print('%s: beta %.6f a0 %.4f; chart inversion residual max |G_x - y|/y %.2e' % (f.split('/')[-1], beta, a0, float(((F['y'] - y).abs() / y).max())))
ref = files[0]
print('\nreference %s (eta = Theta / a0 up to the stored normalization; W = beta X + U):' % ref.split('/')[-1])
print('%12s %12s | ' % ('x', 'y') + ' '.join('%14s' % k for k in KEYS))
for i, p in enumerate(PTS):
    print('%12.4g %12.4g | ' % p + ' '.join('%+14.7e' % vals[ref][k][i] for k in KEYS))
for f in files[1:]:
    print('\n%s minus reference: max |diff| and max |diff|/|ref| over the %d points, per field:' % (f.split('/')[-1], len(PTS)))
    for k in KEYS:
        d = vals[f][k] - vals[ref][k]; r = np.abs(d) / np.maximum(np.abs(vals[ref][k]), 1e-300)
        i = int(np.argmax(np.abs(d))); j = int(np.argmax(r))
        print('   %4s: max |diff| %.3e at (%.3g, %.3g); max rel %.3e at (%.3g, %.3g)' % (k, abs(d[i]), PTS[i][0], PTS[i][1], r[j], PTS[j][0], PTS[j][1]))
    print('   per point rel diff (eta, Om, Psi): ' + ' '.join('(%.1e,%.1e,%.1e)' % tuple(abs(vals[f][k][i] - vals[ref][k][i]) / max(abs(vals[ref][k][i]), 1e-300) for k in ('eta', 'Om', 'Psi')) for i in range(len(PTS))))
