"""Recompute diagnostics (incl. kappa_axis) of saved forward states: python3 tests/pfwd_rediag.py state.npz ..."""
import sys, json; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd import PFwd
torch.set_default_dtype(torch.float64)
for fn in sys.argv[1:]:
    d = np.load(fn); g = torch.tensor(d['g'], device='cuda'); lr = d['lr']; th = d['th']; a = json.loads(str(d['args'])); p = a['p']
    Nr, Nth = g.shape; shift = float(th[0]) / (2 * np.pi / Nth)
    S = PFwd(Nr, Nth, float(lr[0]), float(lr[-1]), p, dev='cuda', thshift=shift)
    o = S.diagnostics(g, krings=(8, 20, 40))
    print("%s: p=%g shift=%.2f m1(rings)=%s c_mom=%.5f (c_l - c_mom = %.5f) kappa_axis=%s Rrel=%s" % (fn.split('/')[-1], p, shift,
          [o['ring%d' % k]['m1'] for k in (8, 20, 40)], o['c_moment'], 1 / p - o['c_moment'], {k: round(v, 4) for k, v in o['kappa_axis'].items()},
          {k: '%.1e' % v for k, v in o['R_rel_bands'].items()}))
