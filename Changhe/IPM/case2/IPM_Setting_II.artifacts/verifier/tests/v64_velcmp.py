"""V64: own velocity (code/fwdstat.py, CharSolver) against the lead's velocity routine on the same density. The lead routine is
run only as the object under test (read-only import of ../analysis/explore/pforward2.py, or pforward.py with 'old').
Lead state: g, lr (uniform), th, p. Own: the density imported by tests/v52_import.py (OWN.npz). The lead fields
alpha_L = l + W_r/r, beta_L = W_th/r are splined in log r onto the own Gauss nodes (same angles required).
Usage: python3 tests/v64_velcmp.py LEAD.npz OWN.npz [old]"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
sys.path.insert(0, '../analysis/explore')
from fwdstat import FwdStat
old = len(sys.argv) > 3 and sys.argv[3] == 'old'
if old:
    import pforward as PFL
else:
    import pforward2 as PFL
DT = torch.float64
dl = np.load(sys.argv[1]); do = np.load(sys.argv[2], allow_pickle=True)
g, lr, thl, p = dl['g'], dl['lr'], dl['th'], float(dl['p']); l = 1.0/p
args = json.loads(str(do['args'])); nt = len(do['th'])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt,
            dti=0.01, nstep=800)
th = F.th.cpu().numpy(); assert len(thl) == nt and np.allclose(thl, th), 'angle grids differ'
rho = torch.tensor(do['rho'], dtype=DT, device='cuda')
al, be, _, _ = F.fields(rho); al = al.cpu().numpy(); be = be.cpu().numpy()
r = F.r.cpu().numpy(); t = np.log(r)
rl = np.exp(lr); wr, wt = PFL.velocity_p(rl[:, None]**p*g, lr, thl, p)
alL = CubicSpline(lr, l + wr/rl[:, None], axis=0)(np.clip(t, lr[0], lr[-1]))
beL = CubicSpline(lr, wt/rl[:, None], axis=0)(np.clip(t, lr[0], lr[-1]))
out = dict(lead=sys.argv[1].split('/')[-1], own=sys.argv[2].split('/')[-1], lead_routine='pforward' if old else 'pforward2', nt=nt)
out['min_alpha_own'] = round(float(al[(t > lr[0] + 0.5)].min()), 4); out['min_alpha_lead'] = round(float(alL[(t > lr[0] + 0.5)].min()), 4)
bands = {}
for a_, b_ in ((-11.5, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 3), (3, 6), (6, 9.5)):
    m = (t >= a_) & (t < b_)
    da = np.abs(al[m] - alL[m]); db = np.abs(be[m] - beL[m])
    i, j = np.unravel_index(np.argmax(da), da.shape)
    bands['%g..%g' % (a_, b_)] = dict(max_dalpha=float('%.3g' % da.max()), max_dbeta=float('%.3g' % db.max()),
                                     at_deg=round(float(np.degrees(th[j])), 1), max_alpha=float('%.3g' % np.abs(al[m]).max()))
out['bands'] = bands
for name, j in (('up', nt//4), ('down', 3*nt//4)):
    rows = []
    for lrv in (-10, -8, -6, -4, -2, 0, 2, 4, 9.5):
        i = int(np.argmin(np.abs(t - lrv)))
        rows.append([round(float(t[i]), 2), round(float(al[i, j]), 4), round(float(alL[i, j]), 4), round(float(be[i, j]), 4), round(float(beL[i, j]), 4)])
    out['axis_' + name + ' [t, alpha own, lead, beta own, lead]'] = rows
print(json.dumps(out, indent=1), flush=True)
