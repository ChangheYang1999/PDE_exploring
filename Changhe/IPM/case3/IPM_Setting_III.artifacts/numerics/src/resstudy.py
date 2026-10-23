"""Resolution study of the coupled (gamma = 1/c_l) Newton solution at fixed p, starting from a saved state."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]; p = float(sys.argv[3])
pairs = [tuple(int(v) for v in s.split('x')) for s in sys.argv[4].split(',')]
st = torch.load(start)
log = open(f'runs/{tag}.log', 'a')
log.write(f"# resolution study from {start} at fixed p={p}; pairs {pairs}  {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
mdl_old = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
b_old = st['b'].to(dev); cl = st['cl']
for (N, M) in pairs:
    mdl = ipm3.IPM3(N=N, M=M, L=st['L'], gamma=1/cl, p=p, device=dev, couple_gamma=True)
    b = ipm3.regrid(mdl_old, b_old, mdl)
    t0 = time.time()
    b, cl_new, info = ipm3.newton(mdl, b, cl, gauge_value=1.0, maxit=60, tol=1e-12, verbose=False, log=log)
    c = mdl.psi_xy0(info['flds']).item()
    sv = torch.linalg.svdvals(info['J'])
    msg = (f"N={N} M={M} p={p}: cl={cl_new:.12f} gamma={mdl.gamma:.12f} c={c:.12f} a0={b[0,0].item():.10f} |F|={info['nF']:.2e} iters={len(info['hist'])} "
           f"smin(J)={sv[-1].item():.3e} s[-2]={sv[-2].item():.3e} b range [{b.min().item():.4f},{b.max().item():.4f}] time {time.time()-t0:.1f}s")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    torch.save(dict(b=b.cpu(), cl=cl_new, gamma=mdl.gamma, N=N, M=M, L=st['L'], p=p), f'runs/{tag}_N{N}M{M}.pt')
    if info['nF'] < 1e-8:
        mdl_old, b_old, cl = mdl, b, cl_new
