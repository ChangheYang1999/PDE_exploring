"""Reproduce a forced solution from a specific H1 guess (c_l, beta, ratio, R, kappa) at (N0, M0), save it, then run the
refinement test over pairs (regrid + forced solve at fixed c_l, beta)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N0 = int(sys.argv[1]); M0 = int(sys.argv[2]); tag = sys.argv[3]; cl = float(sys.argv[4]); beta = float(sys.argv[5])
ratio = float(sys.argv[6]); R = float(sys.argv[7]); kappa = float(sys.argv[8]); pairs = [tuple(int(v) for v in s.split('x')) for s in sys.argv[9].split(',')]
L = 1.0; log = open(f'runs/{tag}.log', 'a'); log.write(f"# sheet from guess cl={cl} beta={beta} ratio={ratio} R={R} kappa={kappa} N0={N0} M0={M0} pairs={pairs} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
mdl = ipm3.IPM3(N=N0, M=M0, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
r = mdl.rad.rR[:, None]; th = mdl.ang.theta[None, :]
bg = beta + (ratio*beta - beta)/(1 + (r/R)**2)*(1 + kappa*(r**2/(R**2 + r**2))*torch.cos(2*th))
b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=80, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
def rep(mdl, b, info, label):
    c = mdl.psi_xy0(info['flds']).item(); a0 = b[0,0].item(); sv = torch.linalg.svdvals(info['J']); M = mdl.M
    bhat = mdl.ang.to_coef(b, 'EE'); far = bhat[-1].abs().cpu().numpy()
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(mdl.N+1))); ck = np.linalg.lstsq(V, bhat[:,0].cpu().numpy(), rcond=None)[0]
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); thg = mdl.ang.theta_np; thm = 0.5*(thg[:-1]+thg[1:])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, info['flds'], RR, TT); tt = mdl.rad.t_of_r(RR); phi = mdl.rad.one_minus_s2_of_t(torch.tensor(tt)).numpy()**2
    q = (np.abs(ev['R'] - info['mu']*ev['y']*phi)/ev['Nf']).max()
    msg = (f"{label} N={mdl.N} M={M}: |F|={info['nF']:.1e} it={len(info['hist'])} smin={sv[-1].item():.1e} mu={info['mu']:+.8f} a0={a0:.8f} c={c:+.8f} Delta={cl+c-1:+.6f} a0/4A={a0/(4*(2*cl-1)):.3f} "
           f"offgrid|R_f|/Nf={q:.1e} cheb b0 |c_N/2|={abs(ck[mdl.N//2]):.1e} |c_N-3|={abs(ck[mdl.N-3]):.1e} far|b_k| k=4,8,M-1: {far[4]:.1e} {far[8]:.1e} {far[M-1]:.1e}")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
rep(mdl, b, info, f"[{tag} start]")
if info['nF'] > 1e-8: print("start not converged; stop"); sys.exit()
torch.save(dict(b=b.cpu(), cl=cl, gamma=1/cl, N=N0, M=M0, L=L, p=mdl.p, mu=info['mu'], beta=beta), f'runs/{tag}_N{N0}M{M0}.pt')
mdl_p, b_p, mu_p = mdl, b, info['mu']
for (N, M) in pairs:
    mdl2 = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl2.gauge = 'inf'
    bg2 = ipm3.regrid(mdl_p, b_p, mdl2); bg2 = bg2*(beta/(mdl2.rad.ext1_R @ bg2).mean().item())
    b2, _, info2 = ipm3.newton(mdl2, bg2, cl, gauge_value=beta, maxit=120, tol=1e-12, verbose=False, log=log, mu=mu_p, forced=True)
    rep(mdl2, b2, info2, f"[{tag} refine]")
    torch.save(dict(b=b2.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl2.p, mu=info2['mu'], beta=beta), f'runs/{tag}_N{N}M{M}.pt')
    if info2['nF'] < 1e-8: mdl_p, b_p, mu_p = mdl2, b2, info2['mu']
