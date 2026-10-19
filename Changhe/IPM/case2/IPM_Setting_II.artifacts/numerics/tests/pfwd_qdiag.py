"""Lead's continuation diagnostics on saved states (code/pfwd_diag2.full_diag): Q, E_R, c_<R, sigma(lr), velocity minima, axis law fd1 both forms.
Usage: python3 tests/pfwd_qdiag.py state1.npz [state2.npz ...] [json=1]   (exit-map _fp.npz, bnewton iterate npz, or any (g, lr, th, args{p, par}))"""
import sys, json; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_batch import PFwdB
from pfwd_diag2 import full_diag, summary_line
torch.set_default_dtype(torch.float64)
want_json = any(a == 'json=1' for a in sys.argv[1:])
for fn in [a for a in sys.argv[1:] if not a.startswith('json=')]:
    d = np.load(fn, allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']; a = json.loads(str(d['args'])); p = float(a['p'])
    coef = np.array(a['par']) if 'par' in a else d['x'][:-1]
    K = int(a.get('K', len(coef)))
    if a.get('kind') == 'bnewton':
        coef = coef[:K]                                   # bnewton iterate files store par = x[:-1] (modes, bumps, [D], [q]); the Fourier modes are the first K
    Nr, Nth = g0.shape
    SB = PFwdB(Nr, Nth, float(lr[0]), float(lr[-1]), p)
    g = torch.tensor(g0, device='cuda')
    out = full_diag(SB, g, p, coef, qj=float(a.get('qj', 2.0)))
    print(summary_line(out, fn.split('/')[-1]))
    if want_json: print(json.dumps(dict(state=fn, **out)))
