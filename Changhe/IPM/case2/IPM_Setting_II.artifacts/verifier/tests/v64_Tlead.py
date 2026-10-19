"""V64h: split the T-defect of an imported lead state into a velocity part and a transport part. The own exact characteristic map
(code/fwdstat.py trace, RK4 in t, inflow datum at tmax) is applied to the lead density with (i) the own velocity of that density and
(ii) the lead velocity routine (../analysis/explore/pforward2.velocity_p, run read-only as the object under test, splined in log r
onto the own Gauss nodes). If (ii) reproduces the lead density, the lead transport is consistent with its velocity and the defect
is a velocity difference; otherwise the lead transport itself is off.  Usage: python3 tests/v64_Tlead.py LEAD.npz IMPORT.npz a1:..:a6"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
sys.path.insert(0, '../analysis/explore')
from fwdstat import FwdStat
import pforward2 as PFL
DT = torch.float64
dl = np.load(sys.argv[1]); do = np.load(sys.argv[2], allow_pickle=True)
g, lr, thl, p = dl['g'], dl['lr'], dl['th'], float(dl['p']); l = 1.0/p
par = [float(s) for s in sys.argv[3].split(':')]
sys.path.insert(0, 'tests')
from cwin import cwin_fn
CW = cwin_fn(sys.argv[1])                       # lead winpic.py window factor, if the lead file carries one
def Afun(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    return np.cos(t)**2*np.exp(f)*(1.0 if CW is None else CW(t))
args = json.loads(str(do['args'])); nt = len(do['th'])
F = FwdStat(p, Afun, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt, dti=0.01, nstep=800)
th = F.th.cpu().numpy(); assert np.allclose(thl, th)
rho = torch.tensor(do['rho'], dtype=DT, device='cuda')
r = F.r.cpu().numpy(); t = np.log(r)
rl = np.exp(lr); wr, wt = PFL.velocity_p(rl[:, None]**p*g, lr, thl, p)
alL = torch.tensor(CubicSpline(lr, l + wr/rl[:, None], axis=0)(np.clip(t, lr[0], lr[-1])), dtype=DT, device='cuda')
beL = torch.tensor(CubicSpline(lr, wt/rl[:, None], axis=0)(np.clip(t, lr[0], lr[-1])), dtype=DT, device='cuda')
alO, beO, _, _ = F.fields(rho)
t0 = F.t_nodes[:, None].expand_as(F.R).reshape(-1); th0 = F.TH.reshape(-1)
gI = (rho/F.R**p).cpu().numpy(); gmax = np.abs(gI).max()
out = dict(lead=sys.argv[1].split('/')[-1], nt=nt, m1_import=round(F.node(rho)['m1'], 5), window_factor=CW is not None)
for lab, a, b in (('own_velocity', alO, beO), ('lead_velocity', alL, beL)):
    the, s = F.trace(a, b, t0, th0)
    Ae = torch.tensor(Afun(the.cpu().numpy()), dtype=DT, device='cuda')
    rT = (torch.exp(-s)*F.L**p*Ae).reshape(F.R.shape)
    gT = (rT/F.R**p).cpu().numpy(); res = {}
    for a_, b_ in ((-12, -11), (-11, -10), (-10, -9), (-9, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10)):
        m = (t >= a_) & (t < b_); e = np.abs(gT[m] - gI[m])
        rm = e.max(1)/np.abs(gI[m]).max(1)
        res['%g..%g' % (a_, b_)] = dict(max_rel_to_gmax=float('%.3g' % (e.max()/gmax)), max_ringwise_rel=float('%.3g' % rm.max()))
    out[lab] = dict(m1_T=round(F.node(rT)['m1'], 5), defect=res)
print(json.dumps(out, indent=1), flush=True)
