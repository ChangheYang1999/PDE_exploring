"""V42 decomposition: apply my exact characteristic map T once to a lead state rho_pub, (i) with my velocity of rho_pub,
(ii) with the LEAD's velocity of rho_pub (analysis/explore/pforward.py velocity_p on the lead grid, imported read-only,
cubic-spline interpolated in log r to my nodes; same angles). If (ii) reproduces rho_pub but (i) does not, the lead/verifier
discrepancy is in the velocity; if neither, it is in the transport. Also: the lead velocity on the same density resampled to
2x radial points (kernel-quadrature convergence of the lead's velocity).
Usage: python3 tests/v42_Tdiag2.py FILE p [ppu] [nstep]"""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
sys.path.insert(0, '../analysis/explore')
from fwdstat import FwdStat
import pforward as LP
f = sys.argv[1]; p = float(sys.argv[2]); l = 1/p
ppu = int(sys.argv[3]) if len(sys.argv) > 3 else 5; nstep = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
d = np.load(f, allow_pickle=True); g0, lr0, th0 = d['g'], d['lr'], d['th']
Nr, Nth = g0.shape; r0 = np.exp(lr0)
Wr_L, Wt_L = LP.velocity_p(r0[:, None]**p*g0, lr0, th0, p)
aL = l + Wr_L/r0[:, None]; bL = Wt_L/r0[:, None]
# lead velocity on 2x radial resampling of the same density
lr2 = np.linspace(lr0[0], lr0[-1], 2*Nr - 1); g2 = CubicSpline(lr0, g0, axis=0)(lr2); r2 = np.exp(lr2)
Wr2, Wt2 = LP.velocity_p(r2[:, None]**p*g2, lr2, th0, p)
aL2 = (l + Wr2/r2[:, None])[::2]; bL2 = (Wt2/r2[:, None])[::2]
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=ppu, q=8, nt=Nth, dti=0.01, nstep=nstep)
rr = F.r.cpu().numpy(); lrr = np.log(rr)
G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1])); G[lrr < lr0[0]] = 0.0
rho = torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda')
c0 = F.node(rho)['c']
am, bm, _, _ = F.fields(rho)
def ext(X):   # lead-grid field -> my nodes (clamped below the lead's inner edge: those nodes are in my panel 0)
    return torch.tensor(CubicSpline(lr0, X, axis=0)(np.clip(lrr, lr0[0], lr0[-1])), dtype=torch.float64, device='cuda')
res = dict(file=f.split('/')[-1], p=p, Nr=Nr, Nth=Nth, ppu=ppu, nstep=nstep, c_pub=c0, m1_pub=l - c0)
k = (lr0 > -11.5) & (lr0 < 9.5)
res['lead_vel_1x_vs_2x'] = dict(dalpha=float(np.abs(aL - aL2)[k].max()), dbeta=float(np.abs(bL - bL2)[k].max()))
for name, (a, b) in (('my_vel', (am, bm)), ('lead_vel', (ext(aL), ext(bL))), ('lead_vel_2x', (ext(aL2), ext(bL2)))):
    the, s = F.trace(a, b, F.t_nodes[:, None].expand_as(F.R).reshape(-1), F.TH.reshape(-1))
    Ae = torch.tensor(F.Afun(the.cpu().numpy()), dtype=torch.float64, device='cuda')
    Tr = (torch.exp(-s)*F.L**p*Ae).reshape(F.R.shape)
    c1 = F.node(Tr)['c']
    D = ((Tr - rho)/F.R**p).abs()
    sup_in = float(D[(F.t_nodes > -11.5) & (F.t_nodes < -2)].max()); sup_out = float(D[F.t_nodes >= -2].max())
    res[name] = dict(c_T=round(c1, 6), m1_T=round(l - c1, 5), sup_dg_inner=round(sup_in, 4), sup_dg_outer=round(sup_out, 4))
print(json.dumps(res), flush=True)
