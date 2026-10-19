import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
import importlib.util
spec = importlib.util.spec_from_file_location('npfwd', 'code/pfwd.py')
NP = importlib.util.module_from_spec(spec); spec.loader.exec_module(NP)
f = sys.argv[1]; p = float(sys.argv[2]); l = 1/p
d = np.load(f, allow_pickle=True); g0, lr0, th0 = d['g'], d['lr'], d['th']
Nr, Nth = g0.shape; r0 = np.exp(lr0)
S = NP.PFwd(Nr, Nth, float(lr0[0]), float(lr0[-1]), p, dev='cuda')
Wr, Wt = S.velocity(torch.tensor(r0[:, None]**p*g0, dtype=torch.float64, device='cuda'))
aN = l + Wr.cpu().numpy()/r0[:, None]; bN = Wt.cpu().numpy()/r0[:, None]
del S; torch.cuda.empty_cache()
prev = None
for ppu in (3, 5, 8, 12):
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=ppu, q=8, nt=Nth, dti=0.01, nstep=10)
    rr = F.r.cpu().numpy(); lrr = np.log(rr)
    G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1])); G[lrr < lr0[0]] = 0.0
    am, bm, _, _ = F.fields(torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda'))
    a_me = CubicSpline(lrr, am.cpu().numpy(), axis=0)(lr0); b_me = CubicSpline(lrr, bm.cpu().numpy(), axis=0)(lr0)
    row = {}
    for lo_, hi_ in ((-11.5, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0)):
        k = (lr0 >= lo_) & (lr0 < hi_)
        row['%g..%g' % (lo_, hi_)] = 'num %.1e/%.1e' % (np.abs(aN - a_me)[k].max(), np.abs(bN - b_me)[k].max()) + \
            ('' if prev is None else ' prev %.1e/%.1e' % (np.abs(prev[0] - a_me)[k].max(), np.abs(prev[1] - b_me)[k].max()))
    prev = (a_me, b_me)
    print(ppu, F.S.Nr, json.dumps(row), flush=True)
    del F; torch.cuda.empty_cache()
