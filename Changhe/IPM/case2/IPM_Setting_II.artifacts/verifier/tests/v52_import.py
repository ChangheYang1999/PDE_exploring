"""V52: import an external forward state (lead / numerics format g, lr, th) onto the code/fwdstat.py grid (cubic spline in log r,
periodic cubic in theta if the angles differ, rho = 0 inside the external inner radius, as tests/v43_gfix.py), save it in the own
format (rho, r, th, p, args) so that tests/v50_axis.py and tests/v51_qprof.py run on it unchanged. Prints the own node data.
Usage: python3 tests/v52_import.py EXT.npz p OUT.npz [nt]"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn, p, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
d = np.load(fn, allow_pickle=True)
g0, lr0, th0 = d['g'], d['lr'], d['th']
nt = int(sys.argv[4]) if len(sys.argv) > 4 else len(th0)
tmin, tmax = -12.0, float(lr0[-1])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=tmax, ppu=3, q=8, nt=nt, dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
if len(th0) != len(thn) or not np.allclose(th0, thn):
    th_ext = np.concatenate([th0, [th0[0] + 2*math.pi]]); G_ext = np.concatenate([G, G[:, :1]], 1)
    G = CubicSpline(th_ext, G_ext, axis=1, bc_type='periodic')(np.remainder(thn - th0[0], 2*math.pi) + th0[0])
G[lrr < lr0[0]] = 0.0
rho = rr[:, None]**p*G
nd = F.node(torch.tensor(rho, dtype=DT, device='cuda'))
np.savez(out, rho=rho, r=rr, th=thn, p=p, args=json.dumps(dict(tmin=tmin, tmax=tmax, ppu=3, nt=nt, source=fn)))
print(json.dumps(dict(source=fn, p=p, nt=nt, m1=round(nd['m1'], 6), m2=round(nd['m2'], 6), e1_deg=round(nd['e1_deg'], 4))), flush=True)
