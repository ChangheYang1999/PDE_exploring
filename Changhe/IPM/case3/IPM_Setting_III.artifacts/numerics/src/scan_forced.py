"""Forced continuation: for each fixed c_l (gamma = 1/c_l, p = 1/(1-gamma)), solve the smoothly forced problem
   (c_l X + U).grad rho - rho = mu y phi(r),  phi = (1 + r^2/L^2)^-2,  for (b, mu), with a gauge row.
True solutions are the zeros of mu(c_l)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); L = float(sys.argv[3]); tag = sys.argv[4]
cls = [float(v) for v in sys.argv[5].split(',')]
gauge = sys.argv[6] if len(sys.argv) > 6 else 'inf'
b0 = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
cont = (sys.argv[8] == 'cont') if len(sys.argv) > 8 else False
gv = float(sys.argv[9]) if len(sys.argv) > 9 else (1.0 if gauge == "inf" else 0.0)
log = open(f'runs/{tag}.log', 'a')
log.write(f"# forced scan N={N} M={M} L={L} gauge={gauge} cls={cls} start b={b0} cont={cont}  {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
b_prev = None; mdl_prev = None
for cl in cls:
    gamma = 1/cl
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev); mdl.gauge = gauge
    if cont and b_prev is not None:
        b = ipm3.regrid(mdl_prev, b_prev, mdl)
    else:
        b = b0*torch.ones(N+1, M, device=dev)
    t0 = time.time()
    b, _, info = ipm3.newton(mdl, b, cl, gauge_value=gv, maxit=80, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
    c = mdl.psi_xy0(info['flds']).item()
    sv = torch.linalg.svdvals(info['J'])
    binf = (mdl.rad.ext1_R @ b).mean().item()
    msg = (f"cl={cl:.6f}: mu={info['mu']:+.10f}  a0={b[0,0].item():.10f}  c={c:+.10f} (1-cl={1-cl:+.6f})  b(inf)={binf:.6f}  |F|={info['nF']:.2e} "
           f"iters={len(info['hist'])}  smin(J)={sv[-1].item():.3e} s[-2]={sv[-2].item():.3e}  b range [{b.min().item():.4f},{b.max().item():.4f}]  {time.time()-t0:.1f}s")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    torch.save(dict(b=b.cpu(), cl=cl, gamma=gamma, N=N, M=M, L=L, p=mdl.p, mu=info['mu'], gauge=gauge), f'runs/{tag}_cl{cl:.4f}.pt')
    if info['nF'] < 1e-8:
        b_prev, mdl_prev = b, mdl
