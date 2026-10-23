"""Track the second forced sheet: start at (c_l0, beta) from the H1 guess b = beta + (a0g - beta)/(1 + (r/R)^2),
then continue in c_l (list), regridding; report mu, a0, c, Delta = c_l + c - 1, off-grid residual, Chebyshev tail."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); tag = sys.argv[3]; beta = float(sys.argv[4])
cl0 = float(sys.argv[5]); a0g = float(sys.argv[6]); R = float(sys.argv[7]); cls = [float(v) for v in sys.argv[8].split(',')]
L = 1.0
log = open(f'runs/{tag}.log', 'a'); log.write(f"# sheet2 N={N} M={M} beta={beta} start cl0={cl0} a0g={a0g} R={R} cls={cls} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
def cheb_coeffs(mdl, f):
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(mdl.N + 1))); return np.linalg.lstsq(V, f, rcond=None)[0]
def diag(mdl, b, cl, flds, mu, label):
    c = mdl.psi_xy0(flds).item(); a0 = b[0,0].item(); gamma = 1/cl
    bhat = mdl.ang.to_coef(b, 'EE')
    bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = L**(1-gamma)*bK; Lcan = (K/a0)**(cl/(cl-1)) if K/a0 > 0 else float('nan')
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np; thm = 0.5*(th[:-1]+th[1:])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, flds, RR, TT)
    tt = mdl.rad.t_of_r(RR); one_m_s2 = mdl.rad.one_minus_s2_of_t(torch.tensor(tt)).numpy(); phi = one_m_s2**2
    Rf = ev['R'] - mu*ev['y']*phi                      # residual of the FORCED equation between nodes
    q = np.abs(Rf)/ev['Nf']
    og = [q[(RR>=lo)&(RR<hi)].max() if ((RR>=lo)&(RR<hi)).any() else float('nan') for lo,hi in [(0,1),(1,100),(100,1e4),(1e4,1e30)]]
    ck0 = cheb_coeffs(mdl, bhat[:,0].cpu().numpy()); n = np.arange(N+1); tail = slice(N//2, N-2); s0 = ((-1.0)**n*ck0)[tail]
    msg = (f"{label} cl={cl:.6f} beta={beta} mu={mu:+.8f} a0={a0:.8f} c={c:+.8f} Delta=cl+c-1={cl+c-1:+.6f} K={K:.5f} Lcan={Lcan:.4g} "
           f"forced-eq offgrid|R|/Nf={og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e} tail beta0: frac(+)={(s0>0).mean():.2f} |c_N/2|={abs(ck0[N//2]):.1e} |c_N-3|={abs(ck0[N-3]):.1e} b range [{b.min().item():.3f},{b.max().item():.3f}]")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl0, device=dev); mdl.gauge = 'inf'
startfile = sys.argv[9] if len(sys.argv) > 9 else None
if startfile is None:
    r = mdl.rad.rR[:, None]
    bg = beta + (a0g - beta)/(1 + (r/R)**2) * torch.ones(1, M, device=dev); mu0 = 0.0
else:
    st = torch.load(startfile); mo = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
    bg = ipm3.regrid(mo, st['b'].to(dev), mdl); mu0 = st['mu']
    bg = bg * (beta/(mdl.rad.ext1_R @ bg).mean().item())
b, _, info = ipm3.newton(mdl, bg, cl0, gauge_value=beta, maxit=80, tol=1e-12, verbose=False, log=log, mu=mu0, forced=True)
print(f"start solve |F|={info['nF']:.1e} it={len(info['hist'])}")
mu = info['mu']; diag(mdl, b, cl0, info['flds'], mu, "SHEET2 start")
torch.save(dict(b=b.cpu(), cl=cl0, gamma=1/cl0, N=N, M=M, L=L, p=mdl.p, mu=mu, beta=beta), f'runs/{tag}_cl{cl0:.4f}.pt')
mdl_prev, b_prev, mu_prev = mdl, b, mu
for cl in cls:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
    bg = ipm3.regrid(mdl_prev, b_prev, mdl)
    b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=80, tol=1e-12, verbose=False, log=log, mu=mu_prev, forced=True)
    if info['nF'] > 1e-8:
        m = f"  cl={cl}: NOT converged |F|={info['nF']:.1e}"; print(m, flush=True); log.write(m+"\n"); continue
    diag(mdl, b, cl, info['flds'], info['mu'], f"SHEET2 it={len(info['hist'])}")
    torch.save(dict(b=b.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl.p, mu=info['mu'], beta=beta), f'runs/{tag}_cl{cl:.4f}.pt')
    mdl_prev, b_prev, mu_prev = mdl, b, info['mu']
