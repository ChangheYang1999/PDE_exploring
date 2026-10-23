"""Continuation of a forced sheet in c_l at fixed resolution and beta from a saved state (small steps), logging
mu, Delta, a0, K, Lcan, and the between-node residual of the forced equation."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]; N = int(sys.argv[3]); M = int(sys.argv[4]); beta = float(sys.argv[5])
cls = [float(v) for v in sys.argv[6].split(',')]; L = 1.0
log = open(f'runs/{tag}.log', 'a'); log.write(f"# sheet continuation from {start} N={N} M={M} beta={beta} cls={cls} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
st = torch.load(start)
mdl_p = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
b_p = st['b'].to(dev); mu_p = st.get('mu', 0.0)
for cl in cls:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
    bg = ipm3.regrid(mdl_p, b_p, mdl); bg = bg*(beta/(mdl.rad.ext1_R @ bg).mean().item())
    b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=120, tol=1e-12, verbose=False, log=log, mu=mu_p, forced=True)
    c = mdl.psi_xy0(info['flds']).item(); a0 = b[0,0].item()
    bhat = mdl.ang.to_coef(b, 'EE'); bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = L**(1-1/cl)*bK; Lcan = (K/a0)**(cl/(cl-1)) if K/a0 > 0 else float('nan')
    msg = f"cl={cl:.5f}: mu={info['mu']:+.8f} Delta={cl+c-1:+.6f} a0={a0:.8f} c={c:+.8f} K={K:.6f} Lcan={Lcan:.5f} |F|={info['nF']:.1e} it={len(info['hist'])} b range [{b.min().item():.3f},{b.max().item():.3f}]"
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    if info['nF'] < 1e-8:
        torch.save(dict(b=b.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl.p, mu=info['mu'], beta=beta), f'runs/{tag}_cl{cl:.4f}.pt')
        mdl_p, b_p, mu_p = mdl, b, info['mu']
