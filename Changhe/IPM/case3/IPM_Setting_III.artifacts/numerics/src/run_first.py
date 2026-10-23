import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]) if len(sys.argv) > 1 else 48
M = int(sys.argv[2]) if len(sys.argv) > 2 else 12
a0 = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
L = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
tag = sys.argv[5] if len(sys.argv) > 5 else 'first'
cl = 1 + a0/4; gamma = 1/cl
log = open(f'runs/{tag}.log', 'a')
log.write(f"# N={N} M={M} a0={a0} L={L} start cl={cl} gamma={gamma}  {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev)
b = a0*torch.ones(N+1, M, device=dev)
for outer in range(12):
    t0 = time.time()
    b, cl, info = ipm3.newton(mdl, b, cl, gauge_value=1.0, maxit=25, tol=1e-12, verbose=True, log=log)
    c = mdl.psi_xy0(info['flds']).item()
    msg = f"outer {outer}: gamma_frozen={mdl.gamma:.10f} -> cl={cl:.10f} 1/cl={1/cl:.10f} c={c:.10f} cl+c-1={cl+c-1:.2e} b0={b[0,0].item():.8f} |F|={info['nF']:.2e} |E|int max={info['E'][1:].abs().max().item():.2e} time {time.time()-t0:.1f}s"
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    if abs(1/cl - mdl.gamma) < 1e-11 and info['nF'] < 1e-10:
        break
    mdl_new = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev)
    b = ipm3.regrid(mdl, b, mdl_new)
    mdl = mdl_new
torch.save(dict(b=b.cpu(), cl=cl, gamma=mdl.gamma, N=N, M=M, L=L, p=mdl.p), f'runs/{tag}.pt')
print("saved", f'runs/{tag}.pt')
