import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); a0 = float(sys.argv[3]); L = float(sys.argv[4]); tag = sys.argv[5]
cl0 = float(sys.argv[6]) if len(sys.argv) > 6 else 1 + a0/4
start = sys.argv[7] if len(sys.argv) > 7 else None
cl = cl0; gamma = 1/cl
log = open(f'runs/{tag}.log', 'a')
log.write(f"# coupled gamma=1/cl. N={N} M={M} a0={a0} L={L} start cl={cl}  {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev, couple_gamma=True)
if start is None:
    b = a0*torch.ones(N+1, M, device=dev)
else:
    st = torch.load(start)
    mdl_old = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
    b = ipm3.regrid(mdl_old, st['b'].to(dev), mdl); cl = st['cl']; mdl.set_gamma(1/cl)
for outer in range(6):
    t0 = time.time()
    b, cl, info = ipm3.newton(mdl, b, cl, gauge_value=1.0, maxit=40, tol=1e-12, verbose=True, log=log)
    c = mdl.psi_xy0(info['flds']).item()
    msg = f"outer {outer}: p={mdl.p:.8f} (1/(1-gamma)={1/(1-mdl.gamma):.8f}) cl={cl:.12f} gamma={mdl.gamma:.12f} c={c:.12f} cl+c-1={cl+c-1:.2e} a0=b0={b[0,0].item():.10f} |F|={info['nF']:.2e} time {time.time()-t0:.1f}s"
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    if info['nF'] > 1e-8:
        print("not converged; stop"); break
    if abs(mdl.p - 1/(1-mdl.gamma)) < 1e-9:
        break
    mdl_new = ipm3.IPM3(N=N, M=M, L=L, gamma=mdl.gamma, device=dev, couple_gamma=True)   # p = 1/(1-gamma)
    b = ipm3.regrid(mdl, b, mdl_new); mdl = mdl_new
torch.save(dict(b=b.cpu(), cl=cl, gamma=mdl.gamma, N=N, M=M, L=L, p=mdl.p), f'runs/{tag}.pt')
print("saved", f'runs/{tag}.pt')
