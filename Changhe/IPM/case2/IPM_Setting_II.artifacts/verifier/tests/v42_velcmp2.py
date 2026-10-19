"""V42: velocity of one density by four routes: mine (code/fwdstat.py -> charsolve, exact radial Green per mode on Gauss
bands, ppu 5), the lead's velocity_p (trapezoid recursion) at 1x and 2x radial resampling, and the numerics' PFwd.velocity
(exact exponential product weights, 6th-order FD) at 1x and 2x (both imported read-only as external comparators).
Reports max |d alpha|, |d beta| against mine per log-r band. Usage: python3 tests/v42_velcmp2.py FILE p"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
sys.path.insert(0, '../analysis/explore')
from fwdstat import FwdStat
import pforward as LP
import importlib.util
spec = importlib.util.spec_from_file_location('npfwd', 'code/pfwd.py')
NP = importlib.util.module_from_spec(spec); spec.loader.exec_module(NP)
f = sys.argv[1]; p = float(sys.argv[2]); l = 1/p
d = np.load(f, allow_pickle=True); g0, lr0, th0 = d['g'], d['lr'], d['th']
Nr, Nth = g0.shape; r0 = np.exp(lr0)
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=5, q=8, nt=Nth, dti=0.01, nstep=10)
rr = F.r.cpu().numpy(); lrr = np.log(rr)
G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1])); G[lrr < lr0[0]] = 0.0
am, bm, _, _ = F.fields(torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda'))
a_me = CubicSpline(lrr, am.cpu().numpy(), axis=0)(lr0); b_me = CubicSpline(lrr, bm.cpu().numpy(), axis=0)(lr0)
lr2 = np.linspace(lr0[0], lr0[-1], 2*Nr - 1); g2 = CubicSpline(lr0, g0, axis=0)(lr2); r2 = np.exp(lr2)
routes = {}
Wr, Wt = LP.velocity_p(r0[:, None]**p*g0, lr0, th0, p); routes['lead_1x'] = (l + Wr/r0[:, None], Wt/r0[:, None])
Wr, Wt = LP.velocity_p(r2[:, None]**p*g2, lr2, th0, p); routes['lead_2x'] = ((l + Wr/r2[:, None])[::2], (Wt/r2[:, None])[::2])
for name, (lrg, gg) in (('num_1x', (lr0, g0)), ('num_2x', (lr2, g2))):
    S = NP.PFwd(len(lrg), Nth, float(lrg[0]), float(lrg[-1]), p, dev='cuda')
    rg = np.exp(lrg)
    Wr, Wt = S.velocity(torch.tensor(rg[:, None]**p*gg, dtype=torch.float64, device='cuda'))
    Wr = Wr.cpu().numpy(); Wt = Wt.cpu().numpy()
    a = l + Wr/rg[:, None]; b = Wt/rg[:, None]
    routes[name] = (a[::2], b[::2]) if name.endswith('2x') else (a, b)
    del S; torch.cuda.empty_cache()
out = dict(file=f.split('/')[-1], p=p, Nr=Nr, Nth=Nth)
for name, (a, b) in routes.items():
    bands = {}
    for lo_, hi_ in ((-11.5, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 3), (3, 9.5)):
        k = (lr0 >= lo_) & (lr0 < hi_)
        bands['%g..%g' % (lo_, hi_)] = '%.1e/%.1e' % (np.abs(a - a_me)[k].max(), np.abs(b - b_me)[k].max())
    out[name] = bands
print(json.dumps(out), flush=True)
