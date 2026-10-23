"""Refinement test at fixed (c_l, beta) on a forced sheet: regrid the start state to each (N, M) and re-solve the forced
problem; record mu, a0, c, K, Lcan, between-node residual of the forced equation, Chebyshev tails.  Convergence of mu
and a0 with (N, M) means the sheet is a resolved smooth object at this c_l."""
import sys, math, time, numpy as np, torch
sys.path.insert(0, 'numerics/src'); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]; pairs = [tuple(int(v) for v in s.split('x')) for s in sys.argv[3].split(',')]
beta = float(sys.argv[4]); L = 1.0
log = open(f'runs/{tag}.log', 'a'); log.write(f"# refine fixed from {start} pairs {pairs} beta={beta} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
def cheb_coeffs(mdl, f):
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(mdl.N + 1))); return np.linalg.lstsq(V, f, rcond=None)[0]
st = torch.load(start); cl = st['cl']
mdl_p = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev); b_p = st['b'].to(dev); mu_p = st.get('mu', 0.0)
for (N, M) in pairs:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
    bg = ipm3.regrid(mdl_p, b_p, mdl); bg = bg*(beta/(mdl.rad.ext1_R @ bg).mean().item())
    F0, _, _ = mdl.system(bg, cl, gauge_value=beta, mu=mu_p, forced=True)
    t0 = time.time()
    b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=120, tol=1e-12, verbose=False, log=log, mu=mu_p, forced=True)
    c = mdl.psi_xy0(info['flds']).item(); a0 = b[0,0].item(); mu = info['mu']
    bhat = mdl.ang.to_coef(b, 'EE'); bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = L**(1-1/cl)*bK; Lcan = (K/a0)**(cl/(cl-1)) if K/a0 > 0 else float('nan')
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np; thm = 0.5*(th[:-1]+th[1:])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, info['flds'], RR, TT)
    tt = mdl.rad.t_of_r(RR); phi = mdl.rad.one_minus_s2_of_t(torch.tensor(tt)).numpy()**2
    q = np.abs(ev['R'] - mu*ev['y']*phi)/ev['Nf']
    og = [q[(RR>=lo)&(RR<hi)].max() if ((RR>=lo)&(RR<hi)).any() else float('nan') for lo,hi in [(0,0.1),(0.1,1),(1,100),(100,1e30)]]
    ck0 = cheb_coeffs(mdl, bhat[:,0].cpu().numpy()); far = bhat[-1].abs().cpu().numpy()
    sv = torch.linalg.svdvals(info['J'])
    msg = (f"cl={cl:.6f} beta={beta} N={N} M={M}: |F0|={F0.abs().max().item():.1e} -> |F|={info['nF']:.1e} it={len(info['hist'])} smin={sv[-1].item():.1e}  mu={mu:+.8f} a0={a0:.8f} c={c:+.8f} K={K:.6f} Lcan={Lcan:.5f} a0/4A={a0/(4*(2*cl-1)):.4f} "
           f"forced-eq offgrid|R|/Nf [<.1,.1-1,1-100,>100]= {og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}  cheb b0 |c_N/2|={abs(ck0[N//2]):.1e} |c_N-3|={abs(ck0[N-3]):.1e}  far |b_k| k=4,8,16,M-1: {far[4]:.2e} {far[8]:.2e} {far[min(16,M-1)]:.2e} {far[M-1]:.2e}  {time.time()-t0:.1f}s")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    torch.save(dict(b=b.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl.p, mu=mu, beta=beta), f'runs/{tag}_N{N}M{M}.pt')
    if info['nF'] < 1e-8: mdl_p, b_p, mu_p = mdl, b, mu
