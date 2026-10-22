# Dilation-invariant aspect ratio of a stored profile (Proposition 29 escape diagnostic). With h = G_x_eta(0, 0) and physical a0 = a/h:
# vertical scale y_f: Theta(0, y)/y = f a0, i.e. G_x(0, eta) = eta h/f, y_f = G_x(0, eta); horizontal scale x_f: Theta_y(x, 0) = f a0,
# i.e. G_x_eta(x, 0) = h/f. Under D_mu both scale by mu; under the vertical compression of Proposition 29 (a0 -> lambda^2 a0) y_f -> y_f/lambda,
# x_f unchanged, so y_f/x_f ~ a0^(-1/2) would signal escape. Bisection in log scale; binary64 sampled values. Usage: aspect.py STATE [...]
import sys, numpy as np, torch
from jets import DT
from model import fields
from model_core_fb import ModelCoreFB
from model_core import as_patches
def load(f):
    d = np.load(f); J, Kw = int(d['J']), int(d['Kw']); beta = float(d['beta']); a0 = float(d['a0'])
    core = as_patches(d['core']) if 'core' in d.files else []
    mod = ModelCoreFB(J, Kw, core, beta=beta, M=int(d['M']) if 'M' in d.files else 3, alpha=float(d['alpha']), se=float(d['se']) if 'se' in d.files else 1.0)
    c = np.concatenate([d['c'], d['cc']]) if core else d['c']
    return mod, c, a0, beta
def F(mod, c, a0, beta, x, e):
    x0 = torch.tensor(np.asarray(x, float), dtype=DT); e0 = torch.tensor(np.asarray(e, float), dtype=DT)
    return fields(mod.g_jet(c, x0, e0), x0, e0, torch.tensor(a0, dtype=DT), beta)
def bis(fun, lo, hi, n=80):
    flo = fun(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi); fm = fun(mid)
        if (fm > 0) == (flo > 0): lo, flo = mid, fm
        else: hi = mid
    return 0.5 * (lo + hi)
for f in sys.argv[1:]:
    mod, c, a, beta = load(f)
    h = F(mod, c, a, beta, [0.0], [0.0])['A'].numpy()[0]
    out = []
    for fr in (0.5, 0.25):
        le = bis(lambda L: F(mod, c, a, beta, [0.0], [10 ** L])['y'].numpy()[0] / 10 ** L - h / fr, -8.0, 12.0)
        yv = F(mod, c, a, beta, [0.0], [10 ** le])['y'].numpy()[0]
        lx = bis(lambda L: F(mod, c, a, beta, [10 ** L], [0.0])['A'].numpy()[0] - h / fr, -8.0, 12.0)
        out.append((fr, yv, 10 ** lx, yv / 10 ** lx))
    print('%s: beta %.6f a(stored) %.5f h %.10f a0 = a/h %.5f  ' % (f.split('/')[-1], beta, a, h, a / h) +
          '  '.join('f %.2f: y_f %.6e x_f %.6e y_f/x_f %.7f' % o for o in out), flush=True)
