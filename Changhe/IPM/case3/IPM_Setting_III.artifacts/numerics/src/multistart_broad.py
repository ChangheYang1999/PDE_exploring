"""Broad multistart search for forced-sheet solutions at several (c_l, beta): H1-type guesses with varying centre
amplitude, core radius and angular shape.  Report every converged distinct (mu, a0) with the Jacobian's smin."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); tag = sys.argv[3]
cls = [float(v) for v in sys.argv[4].split(',')]; betas = [float(v) for v in sys.argv[5].split(',')]; L = 1.0
log = open(f'runs/{tag}.log', 'a'); log.write(f"# broad multistart N={N} M={M} cls={cls} betas={betas} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
for cl in cls:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
    r = mdl.rad.rR[:, None]; th = mdl.ang.theta[None, :]
    for beta in betas:
        found = []
        for ratio in [0.5, 2.0, 4.0, 8.0, 16.0]:
            for R in [0.03, 0.3, 3.0]:
                for kappa in [0.0, 0.5, -0.5]:
                    a0g = ratio*beta
                    bg = beta + (a0g - beta)/(1 + (r/R)**2)*(1 + kappa*(r**2/(R**2 + r**2))*torch.cos(2*th))
                    b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=60, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
                    if info['nF'] < 1e-8:
                        c = mdl.psi_xy0(info['flds']).item(); a0 = b[0,0].item(); sv = torch.linalg.svdvals(info['J'])
                        key = (round(info['mu'], 4), round(a0, 3))
                        new = all(abs(key[0]-f[0]) > 1e-3 or abs(key[1]-f[1]) > 1e-2 for f in found)
                        if new: found.append(key)
                        m = f"cl={cl:.3f} beta={beta:6.2f} guess ratio={ratio:5.1f} R={R:5.2f} kappa={kappa:+.1f}: CONVERGED mu={info['mu']:+.8f} a0={a0:.6f} c={c:+.6f} Delta={cl+c-1:+.5f} a0/4A={a0/(4*(2*cl-1)):.3f} smin={sv[-1].item():.1e} it={len(info['hist'])}{' NEW' if new else ''}"
                    else:
                        m = f"cl={cl:.3f} beta={beta:6.2f} guess ratio={ratio:5.1f} R={R:5.2f} kappa={kappa:+.1f}: not converged |F|={info['nF']:.1e}"
                    log.write(m+"\n"); log.flush()
                    if info['nF'] < 1e-8 and new: print(m, flush=True)
        m = f"SUMMARY cl={cl} beta={beta}: distinct converged solutions (mu, a0): {found}"; print(m, flush=True); log.write(m+"\n"); log.flush()
