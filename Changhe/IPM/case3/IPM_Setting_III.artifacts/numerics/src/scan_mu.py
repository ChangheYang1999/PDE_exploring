"""Fixed-c_l defect scan: for each c_l (gamma = 1/c_l, p = 1/(1-gamma) exact), solve for (b, mu) with the gauge
mean b(inf) = 1 and the centre row c_l - 1 + c[b] = mu.  True solutions are zeros of mu(c_l)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); L = float(sys.argv[3]); tag = sys.argv[4]
cls = [float(v) for v in sys.argv[5].split(',')]
b0 = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
log = open(f'runs/{tag}.log', 'a')
log.write(f"# defect scan N={N} M={M} L={L} cls={cls} start b={b0}  {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
b = None
for cl in cls:
    gamma = 1/cl
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev)
    if b is None:
        b = b0*torch.ones(N+1, M, device=dev)
    else:
        b = ipm3.regrid(mdl_prev, b, mdl)
    t0 = time.time()
    b, _, info = ipm3.newton(mdl, b, cl, gauge_value=1.0, maxit=60, tol=1e-12, verbose=False, log=log, mu=0.0)
    c = mdl.psi_xy0(info['flds']).item()
    sv = torch.linalg.svdvals(info['J'])
    msg = (f"cl={cl:.6f} gamma={gamma:.6f}: mu={info['mu']:.10f}  c={c:.10f}  a0=b0={b[0,0].item():.10f}  |F|={info['nF']:.2e} "
           f"iters={len(info['hist'])}  smin(J)={sv[-1].item():.3e} s[-2]={sv[-2].item():.3e} smax={sv[0].item():.3e}  "
           f"b range [{b.min().item():.4f},{b.max().item():.4f}]  time {time.time()-t0:.1f}s")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    torch.save(dict(b=b.cpu(), cl=cl, gamma=gamma, N=N, M=M, L=L, p=mdl.p, mu=info['mu']), f'runs/{tag}_cl{cl:.4f}.pt')
    mdl_prev = mdl
