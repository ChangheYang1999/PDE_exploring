"""h - 1 for stored states: h = G_x,eta(0, 0) (= A(0, 0) of model.fields, = the heavy gauge row H(0,0) of the solver), evaluated in binary64 on the CPU from the
stored coefficients (outer P(1, 0) plus the core patch contribution), and compared with the solver's final 'H00' history field. Usage: h_check.py STATE..."""
import sys, json, numpy as np, torch
from jets import DT
from model import fields
from model_core_fb import ModelCoreFB
from model_core import as_patches
for f in sys.argv[1:]:
    d = np.load(f, allow_pickle=True); J, Kw = int(d['J']), int(d['Kw']); beta = float(d['beta']); a0 = float(d['a0'])
    core = as_patches(d['core']) if 'core' in d.files else []
    mod = ModelCoreFB(J, Kw, core, beta=beta, M=int(d['M']) if 'M' in d.files else 3, alpha=float(d['alpha']), se=float(d['se']) if 'se' in d.files else 1.0)
    c = np.concatenate([d['c'], d['cc']]) if core else d['c']
    x0 = torch.tensor([0.0], dtype=DT); e0 = torch.tensor([0.0], dtype=DT)
    h = float(fields(mod.g_jet(c, x0, e0), x0, e0, torch.tensor(a0, dtype=DT), beta)['A'][0])
    # outer part alone: P(1,0) = sum over the outer Chebyshev coefficients of the basis derivative at the origin
    cz = np.concatenate([d['c'], 0 * d['cc']]) if core else d['c']
    h_out = float(fields(mod.g_jet(cz, x0, e0), x0, e0, torch.tensor(a0, dtype=DT), beta)['A'][0])
    H00 = None
    try:
        hist = json.loads(str(d['hist'])); H00 = [r.get('H00') for r in hist if 'H00' in r][-1]
    except Exception: pass
    print('%s: h - 1 = %r (outer part P(1,0) - 1 = %r, core contribution %r); solver final H00 - 1 = %r' % (f.split('/')[-1], h - 1, h_out - 1, h - h_out, (H00 - 1) if H00 is not None else None))
