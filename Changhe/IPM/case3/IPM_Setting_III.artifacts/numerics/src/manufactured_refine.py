"""Refinement discrimination on the manufactured problem: forced solves at fixed c_l (planted c_lm vs the valley root
c_l ~ 2.254 on the same sheet) over resolutions; a smooth exact solution keeps mu = 0 and stable smin, a valley root drifts."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'; a0m = 3.0; kap = -0.5; L = 1.0; tag = 'manuf2_refine'; log = open(f'runs/{tag}.log', 'a')
def P(msg): print(msg, flush=True); log.write(msg + "\n"); log.flush()
def b_m(mdl, gm):
    r = mdl.rad.rR[:, None]; th = mdl.ang.theta[None, :]; x2 = (r*torch.cos(th))**2
    return a0m*(1 + r**2/L**2)**((gm-1)/2)*(1 + kap*x2/(L**2 + r**2))/mdl.wR[:, None]
def clm_at(N, M):
    gm = 0.5
    for it in range(40):
        mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gm, device=dev); c = mdl.psi_xy0(mdl.fields(b_m(mdl, gm))).item(); clm = 1 - c
        if abs(1/clm - gm) < 1e-13: break
        gm = 1/clm
    return clm
clm = clm_at(48, 16); beta_m = 2.25
P(f"c_lm(48x16) = {clm:.12f}; c_lm(96x48) = {clm_at(96, 48):.12f}")
for cl in [clm, 2.254, 2.30]:
    mdl_p = None
    for (N, M) in [(48, 16), (48, 24), (64, 32), (96, 48)]:
        mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
        tgt = mdl.residual(b_m(mdl, 1/clm), clm)
        if mdl_p is None: bg = beta_m*torch.ones(N+1, M, device=dev); mu0 = 0.0
        else: bg = ipm3.regrid(mdl_p, b_p, mdl); bg = bg*(beta_m/(mdl.rad.ext1_R @ bg).mean().item()); mu0 = mu_p
        b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta_m, target=tgt, maxit=100, tol=1e-12, verbose=False, log=log, mu=mu0, forced=True)
        sv = torch.linalg.svdvals(info['J'])
        P(f"  cl={cl:.6f} N={N} M={M}: |F|={info['nF']:.1e} it={len(info['hist'])} mu={info['mu']:+.8f} a0={b[0,0].item():.8f} smin={sv[-1].item():.1e}")
        if info['nF'] < 1e-8: mdl_p, b_p, mu_p = mdl, b, info['mu']
