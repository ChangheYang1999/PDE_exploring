"""V64f: where does one application of the own exact characteristic map T change the node strain of an imported state?
Band split of c = psi_xy(0) (own moment formula) for rho (import), T(rho), and an own reference state on the same grid.
Usage: python3 tests/v64_Tband.py IMPORT.npz a1:a2:...:a6 OWN.npz [LEAD_WITH_CWIN.npz]   (expf datum cos^2 exp(sum a_j phi_j), phi = sin t, cos 2t, ...)"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
d = np.load(sys.argv[1], allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
par = [float(s) for s in sys.argv[2].split(':')]
sys.path.insert(0, 'tests')
from cwin import cwin_fn
CW = cwin_fn(sys.argv[4]) if len(sys.argv) > 4 else None    # optional lead file carrying a winpic.py window factor
def Afun(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    return np.cos(t)**2*np.exp(f)*(1.0 if CW is None else CW(t))
F = FwdStat(p, Afun, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt, dti=0.01, nstep=800)
S = F.S; w = S.w; r = S.r; t = np.log(r.cpu().numpy())
rho = torch.tensor(d['rho'], dtype=DT, device='cuda'); rT, _ = F.T(rho)
ro = torch.tensor(np.load(sys.argv[3], allow_pickle=True)['rho'], dtype=DT, device='cuda')
bands = ((-12, -11), (-11, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10))
out = {}
for lab, x in (('import', rho), ('T(import)', rT), ('own', ro)):
    rm3 = S.rho_modes(x)[:, 3]; contrib = (-2*(w*rm3/r**2).imag).cpu().numpy(); nd = F.node(x)
    out[lab] = dict(m1=round(nd['m1'], 5), c=round(nd['c'], 5), b=round(nd['b'], 6),
                    c_by_band={'%g..%g' % (a_, b_): round(float(contrib[(t >= a_) & (t < b_)].sum()), 5) for a_, b_ in bands})
print(json.dumps(out, indent=1), flush=True)
