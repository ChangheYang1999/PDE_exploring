"""V42: weak-stationarity check of a state with the exact identities (referee result 13 S1, S2) on my CharSolver grid (code/fwdstat.py).
S1: (1 - l) I + Q - flux_L = -int phi R (phi = r^-3 sin 3th, R = V.grad rho - rho), I = pi c. For an exact state the defect is 0;
m1_Q := l - (Q - flux_L)/(pi (l - 1)) is the strain value implied by the transport identity, to be compared with m1_c = l - c.
Usage: python3 tests/v42_ident.py FILE p [nt]  (FILE: lead/num format g, lr, th or own format rho, r, th, p)."""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
f = sys.argv[1]; p = float(sys.argv[2]); l = 1/p
d = np.load(f, allow_pickle=True)
if 'g' in d.files:
    g0, lr0, th0 = d['g'], d['lr'], d['th']
else:
    p0 = float(d['p']); r0 = d['r']; th0 = d['th']; g0 = d['rho']/r0[:, None]**p0; lr0 = np.log(r0)
nt = int(sys.argv[3]) if len(sys.argv) > 3 else len(th0)
for ppu in (3, 5):
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=ppu, q=8, nt=nt, dti=0.01, nstep=400)
    rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
    G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
    if len(th0) != len(thn) or not np.allclose(th0, thn):
        th_ext = np.concatenate([th0, [2*math.pi]]); G_ext = np.concatenate([G, G[:, :1]], 1)
        G = CubicSpline(th_ext, G_ext, axis=1, bc_type='periodic')(thn)
    G[lrr < lr0[0]] = 0.0
    rho = torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda')
    nd = F.node(rho); m1 = nd['m1']
    I = F.identities(rho, m1)
    m1_Q = l - (I['Q'] - I['flux1'])/(math.pi*(l - 1))
    print(json.dumps(dict(file=f.split('/')[-1], ppu=ppu, nt=nt, c=round(nd['c'], 6), m1_c=round(m1, 6), m1_Q=round(m1_Q, 6),
                          S1_defect=I['S1_defect'], S1_rel=I['S1_defect']/(math.pi*(l - 1)*nd['c']),
                          S2=I['S2'], S2_defect=I['S2_defect'], S2_rel=I['S2_defect']/I['flux2'])), flush=True)
