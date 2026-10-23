"""Resolution study: coupled (gamma = 1/c_l) unforced Newton from a saved state, far-field gauge at that state's b(inf);
p re-set to 1/(1-gamma) at each level; between-node residual summary after each level."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]
pairs = [tuple(int(v) for v in s.split('x')) for s in sys.argv[3].split(',')]
st = torch.load(start)
log = open(f'runs/{tag}.log', 'a')
log.write(f"# resolution study from {start}; pairs {pairs}  {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
mdl_old = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
b_old = st['b'].to(dev); cl = st['cl']
beta = (mdl_old.rad.ext1_R @ b_old).mean().item()
def offgrid(mdl, b, cl, flds):
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1] + tR[1:]); th = mdl.ang.theta_np; thm = 0.5*(th[:-1] + th[1:])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, flds, RR, TT); q = np.abs(ev['R'])/ev['Nf']
    out = []
    for lo, hi in [(0, 1), (1, 100), (100, 1e4), (1e4, 1e30)]:
        m = (RR >= lo) & (RR < hi); out.append(q[m].max() if m.sum() else float('nan'))
    return out
for (N, M) in pairs:
    mdl = ipm3.IPM3(N=N, M=M, L=st['L'], gamma=1/cl, device=dev, couple_gamma=True); mdl.gauge = 'inf'
    b = ipm3.regrid(mdl_old, b_old, mdl)
    t0 = time.time()
    b, cl_new, info = ipm3.newton(mdl, b, cl, gauge_value=beta, maxit=80, tol=1e-12, verbose=False, log=log)
    c = mdl.psi_xy0(info['flds']).item()
    og = offgrid(mdl, b, cl_new, info['flds'])
    bhat = mdl.ang.to_coef(b, 'EE'); far = bhat[-1].abs().cpu().numpy()
    msg = (f"N={N} M={M}: cl={cl_new:.12f} c={c:.12f} cl+c-1={cl_new+c-1:.1e} a0={b[0,0].item():.10f} |F|={info['nF']:.2e} iters={len(info['hist'])} "
           f"offgrid max|R|/Nf by region [r<1, 1-100, 100-1e4, >1e4] = {og[0]:.2e} {og[1]:.2e} {og[2]:.2e} {og[3]:.2e}  "
           f"far-field angular coefs (row N, k=0..7): {np.array2string(far[:8], precision=3, max_line_width=200)}  time {time.time()-t0:.1f}s")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    torch.save(dict(b=b.cpu(), cl=cl_new, gamma=mdl.gamma, N=N, M=M, L=st['L'], p=mdl.p), f'runs/{tag}_N{N}M{M}.pt')
    if info['nF'] < 1e-8:
        mdl_old, b_old, cl = mdl, b, cl_new
    else:
        print("  not converged; next level starts from the last converged state", flush=True)
