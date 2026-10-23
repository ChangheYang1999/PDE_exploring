"""Multistart at one (c_l, beta) saving every distinct converged forced solution; then refinement test (48x24, 64x32,
96x48) of each saved solution whose smin exceeds a threshold."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); tag = sys.argv[3]; cl = float(sys.argv[4]); beta = float(sys.argv[5]); smin_thr = float(sys.argv[6]); L = 1.0
log = open(f'runs/{tag}.log', 'a'); log.write(f"# multistart_save N={N} M={M} cl={cl} beta={beta} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
r = mdl.rad.rR[:, None]; th = mdl.ang.theta[None, :]
found = []
for ratio in [0.5, 2.0, 4.0, 8.0, 16.0, 32.0]:
    for R in [0.03, 0.1, 0.3, 1.0, 3.0]:
        for kappa in [0.0, 0.5, -0.5]:
            bg = beta + (ratio*beta - beta)/(1 + (r/R)**2)*(1 + kappa*(r**2/(R**2 + r**2))*torch.cos(2*th))
            b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=60, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
            if info['nF'] < 1e-8:
                a0 = b[0,0].item(); mu = info['mu']; sv = torch.linalg.svdvals(info['J']); smin = sv[-1].item()
                if all(abs(mu - f[0]) > 1e-3 or abs(a0 - f[1]) > 1e-2 for f in found):
                    found.append((mu, a0, smin)); k = len(found)
                    torch.save(dict(b=b.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl.p, mu=mu, beta=beta, smin=smin), f'runs/{tag}_s{k}.pt')
                    m = f"sheet s{k}: mu={mu:+.8f} a0={a0:.6f} Delta={cl+mdl.psi_xy0(info['flds']).item()-1:+.5f} a0/4A={a0/(4*(2*cl-1)):.3f} smin={smin:.1e} (guess ratio={ratio} R={R} kappa={kappa})"
                    print(m, flush=True); log.write(m+"\n"); log.flush()
print(f"found {len(found)} sheets", flush=True)
# refinement of the better-conditioned ones
for k, (mu, a0, smin) in enumerate(found, 1):
    if smin < smin_thr: continue
    st = torch.load(f'runs/{tag}_s{k}.pt'); mdl_p = mdl; b_p = st['b'].to(dev); mu_p = mu
    for (N2, M2) in [(48, 24), (64, 32), (96, 48)]:
        mdl2 = ipm3.IPM3(N=N2, M=M2, L=L, gamma=1/cl, device=dev); mdl2.gauge = 'inf'
        bg = ipm3.regrid(mdl_p, b_p, mdl2); bg = bg*(beta/(mdl2.rad.ext1_R @ bg).mean().item())
        b2, _, info2 = ipm3.newton(mdl2, bg, cl, gauge_value=beta, maxit=120, tol=1e-12, verbose=False, log=log, mu=mu_p, forced=True)
        sv = torch.linalg.svdvals(info2['J'])
        m = f"  refine s{k} N={N2} M={M2}: |F|={info2['nF']:.1e} it={len(info2['hist'])} smin={sv[-1].item():.1e} mu={info2['mu']:+.8f} a0={b2[0,0].item():.6f}"
        print(m, flush=True); log.write(m+"\n"); log.flush()
        if info2['nF'] < 1e-8: mdl_p, b_p, mu_p = mdl2, b2, info2['mu']
