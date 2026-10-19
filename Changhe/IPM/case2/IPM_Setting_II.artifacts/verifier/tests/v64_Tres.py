"""V64e: fixed-point defect of an imported (lead) state in my discretisation: T = exact characteristic map of code/fwdstat.py
(rho_new = e^{-s} L^p A(th_exit) along the own velocity of rho). Reports max |g_T - g| / max |g| (g = rho / r^p) by t band, the
node m1 of rho and of T(rho), and min V_r/r. Needs V_r > 0. Usage: python3 tests/v64_Tres.py OWN.npz a1:a2:...  (expf datum)"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
d = np.load(sys.argv[1], allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
par = [float(v) for v in sys.argv[2].split(':')]
def Afun(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    return np.cos(t)**2*np.exp(f)
F = FwdStat(p, Afun, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt, dti=0.01, nstep=800)
rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
rT, info = F.T(rho)
g = (rho/F.R**p).cpu().numpy(); gT = (rT/F.R**p).cpu().numpy(); t = np.log(F.r.cpu().numpy())
out = dict(state=sys.argv[1].split('/')[-1], minalpha=round(info['minalpha'], 4), m1_rho=round(F.node(rho)['m1'], 5),
           m1_Trho=round(F.node(rT)['m1'], 5), gmax=float('%.4g' % np.abs(g).max()))
bands = {}
for a_, b_ in ((-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10)):
    m = (t >= a_) & (t < b_)
    e = np.abs(gT[m] - g[m]); i, j = np.unravel_index(np.argmax(e), e.shape)
    bands['%g..%g' % (a_, b_)] = dict(max_rel=float('%.3g' % (e.max()/np.abs(g[m]).max())), at_deg=round(float(np.degrees(F.th[j].item())), 1))
out['defect_by_band'] = bands
print(json.dumps(out, indent=1), flush=True)
