"""fwdstat check: is the lead's forward state (pf_cos2_p05_deepB.npz) a near fixed point of my characteristic map T?"""
import sys, time, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
f = sys.argv[1] if len(sys.argv) > 1 else 'runs/pf_cos2_p05_deepB.npz'
p = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
ppu = int(sys.argv[3]) if len(sys.argv) > 3 else 3
nstep = int(sys.argv[4]) if len(sys.argv) > 4 else 400
d = np.load(f); g, lr, th = d['g'], d['lr'], d['th']
t0 = time.time()
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=-12, tmax=10, ppu=ppu, q=8, nt=len(th), dti=0.01, nstep=nstep)
rr = F.r.cpu().numpy(); lrr = np.log(rr)
G = CubicSpline(lr, g, axis=0)(np.clip(lrr, lr[0], lr[-1])); G[lrr < lr[0]] = 0.0
rho = torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda')
nd = F.node(rho); print('lead state node', json.dumps(nd), flush=True)
Tr, info = F.T(rho)
D = ((Tr - rho)/F.R**p).abs()
print('minalpha', info['minalpha'], 'max|T-rho|/r^p', float(D.max()), 't %.1f' % (time.time() - t0))
for a, b in [(-12, -8), (-8, -4), (-4, 0), (0, 4), (4, 8), (8, 10)]:
    sel = (F.t_nodes >= a) & (F.t_nodes < b)
    print('t in [%g,%g): max %.3e  mean %.3e  max g %.3e' % (a, b, float(D[sel].max()), float(D[sel].mean()), float((rho/F.R**p)[sel].abs().max())))
nd2 = F.node(Tr); print('T(state) node', json.dumps(nd2))
print(json.dumps(F.identities(rho, nd['m1'])))
if len(sys.argv) > 5 and sys.argv[5] == 'solve':
    rho2, hist = F.solve(rho, iters=int(sys.argv[6]) if len(sys.argv) > 6 else 30, tol=1e-10, m_and=6, beta_mix=float(sys.argv[7]) if len(sys.argv) > 7 else 1.0, verbose=True)
    nd = F.node(rho2); print('final node', json.dumps(nd))
    print(json.dumps(F.identities(rho2, nd['m1'])))
    out = sys.argv[8] if len(sys.argv) > 8 else None
    if out:
        np.savez(out, rho=rho2.cpu().numpy(), r=F.r.cpu().numpy(), th=F.th.cpu().numpy(), p=p, hist=json.dumps(hist))
    print('t %.1f' % (time.time() - t0))
