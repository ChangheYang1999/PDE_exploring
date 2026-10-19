"""V42 diagnostic: apply my exact characteristic map T (code/fwdstat.py) ONCE to a published state rho_pub and compare the strain
c[T rho_pub] with c[rho_pub], for several trace step counts / interpolation spacings / angle counts. If rho_pub were an exact
stationary state, T rho_pub = rho_pub. Also the radial distribution of the strain difference (cumulative in t).
Usage: python3 tests/v42_Tdiag.py FILE p [configs nt,ppu,nstep,dti;...]"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
f = sys.argv[1]; p = float(sys.argv[2]); l = 1/p
d = np.load(f, allow_pickle=True); g0, lr0, th0 = d['g'], d['lr'], d['th']
CF = ((128, 3, 1000, 0.01), (128, 3, 2000, 0.01), (128, 3, 1000, 0.005), (128, 5, 1000, 0.01), (256, 3, 1000, 0.01))
if len(sys.argv) > 3:
    CF = [tuple(int(v) if i < 3 else float(v) for i, v in enumerate(c.split(','))) for c in sys.argv[3].split(';')]
for (nt, ppu, nstep, dti) in CF:
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=ppu, q=8, nt=nt, dti=dti, nstep=nstep)
    rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
    G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
    if len(th0) != len(thn):
        th_ext = np.concatenate([th0, [2*math.pi]]); G_ext = np.concatenate([G, G[:, :1]], 1)
        G = CubicSpline(th_ext, G_ext, axis=1, bc_type='periodic')(thn)
    G[lrr < lr0[0]] = 0.0
    rho = torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda')
    Tr, info = F.T(rho)
    c0 = F.node(rho)['c']; c1 = F.node(Tr)['c']
    # cumulative strain difference by radius: (1/pi) int (T rho - rho) r^-3 sin3th dX over r < e^t
    wA = (F.S.w*F.S.r)[:, None]*(2*math.pi/nt)
    dens = (wA*(Tr - rho)*F.R**-3*torch.sin(3*F.TH)).sum(1)/math.pi
    cum = torch.cumsum(dens, 0).cpu().numpy(); t = np.log(rr)
    cs = {('%g' % tt): round(float(np.interp(tt, t, cum)), 5) for tt in (-10, -8, -6, -4, -2, 0, 2, 5, 10)}
    D = ((Tr - rho)/F.R**p).abs()
    print(json.dumps(dict(file=f.split('/')[-1], nt=nt, ppu=ppu, nstep=nstep, dti=dti, c_pub=round(c0, 6), c_T=round(c1, 6),
                          m1_pub=round(l - c0, 5), m1_T=round(l - c1, 5), cum_dc_by_t=cs, sup_dg=float(D.max()))), flush=True)
