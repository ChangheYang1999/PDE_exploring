"""Homotopy from several starting shapes/amplitudes; report the maximal eps reached by natural continuation (fine steps)."""
import sys, time, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
dev = 'cuda'
N, M, L = 48, 10, 1.0
res_all = []
def run(name, bfun, cl0):
    gamma = 1/cl0
    m = ipm1.IPM1(N=N, M=M, L=L, gamma=gamma, device=dev)
    nw = solve.Newton(m, verbose=False)
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
    b0 = bfun(r, th, m); b0[0, :] = 1.0
    eps_list = np.linspace(0, 1, 81)[1:]
    b, cl, res, ok = solve.continuation(nw, b0, cl0, eps_list, tol=1e-10, maxit=30, verbose=False)
    emax = max([e for (e, c, conv, nr) in res if conv], default=0.0)
    last = [x for x in res if x[2]][-1] if any(x[2] for x in res) else None
    print(f"{name:40s} cl0={cl0:4.2f}: reached eps={emax:.4f} ok={ok} c_l_end={last[1] if last else float('nan'):.6f} max|b|={b.abs().max().item():.3g}", flush=True)
    res_all.append((name, cl0, emax, ok))
s2 = lambda r, m: r**2/(m.L**2 + r**2)
shapes = {
  'b=1': lambda r, th, m: torch.ones_like(r*th),
  'b=1+10 s2': lambda r, th, m: 1 + 10*s2(r, m) + 0*th,
  'b=1+100 s2': lambda r, th, m: 1 + 100*s2(r, m) + 0*th,
  'b=1+1000 s2': lambda r, th, m: 1 + 1000*s2(r, m) + 0*th,
  'b=1+ s2 cos2th': lambda r, th, m: 1 + s2(r, m)*torch.cos(2*th),
  'b=1- s2 cos2th': lambda r, th, m: 1 - s2(r, m)*torch.cos(2*th),
  'b=1+ 30 s2 (1-cos2th)': lambda r, th, m: 1 + 30*s2(r, m)*(1 - torch.cos(2*th)),
  'b=1+ 30 s2 (1+cos2th)': lambda r, th, m: 1 + 30*s2(r, m)*(1 + torch.cos(2*th)),
  'b=1-0.9 s2': lambda r, th, m: 1 - 0.9*s2(r, m) + 0*th,
}
for cl0 in [1.3, 2.0, 3.0]:
    for name, f in shapes.items():
        try:
            run(name, f, cl0)
        except Exception as ex:
            print(name, cl0, "failed:", ex)
