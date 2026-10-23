"""Methodology validation on a planted smooth solution.
rho_m = a0m y (1 + r^2/L^2)^((gm-1)/2) (1 + kap x^2/(L^2 + r^2)) is smooth, has rho_y(0) = a0m and far field r^gm.
Define c_lm := 1 - c[rho_m] (so the centre identity holds exactly) and gm := 1/c_lm (fixed point in gm); the
manufactured problem is  (c_l X + U).grad rho - rho = S_m := (c_lm X + U_m).grad rho_m - rho_m.
Tests: (A) unforced Newton with c_l free from a perturbation of rho_m -> returns (rho_m, c_lm)?
       (B) unforced Newton from b = const -> lands on rho_m or on a valley state at another c_l?
       (C) forced continuation mu(c_l) at fixed gauge: does mu cross zero at c_lm on a well-conditioned sheet?"""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'; N = int(sys.argv[1]); M = int(sys.argv[2]); a0m = float(sys.argv[3]); kap = float(sys.argv[4]); tag = sys.argv[5]
L = 1.0; log = open(f'runs/{tag}.log', 'a'); log.write(f"# manufactured test N={N} M={M} a0m={a0m} kap={kap} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
def P(msg): print(msg, flush=True); log.write(msg + "\n"); log.flush()
def b_m(mdl, gm):
    r = mdl.rad.rR[:, None]; th = mdl.ang.theta[None, :]; x2 = (r*torch.cos(th))**2
    wm = (1 + r**2/L**2)**((gm-1)/2); rho_over_y = a0m*wm*(1 + kap*x2/(L**2 + r**2))
    return rho_over_y/mdl.wR[:, None]
# fixed point for gm = 1/c_lm with c_lm = 1 - c[rho_m]
gm = 0.5
for it in range(30):
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gm, device=dev); mdl.gauge = 'inf'
    bm = b_m(mdl, gm); c = mdl.psi_xy0(mdl.fields(bm)).item(); clm = 1 - c; gnew = 1/clm
    if abs(gnew - gm) < 1e-13: break
    gm = gnew
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gm, device=dev, couple_gamma=True); mdl.gauge = 'inf'
bm = b_m(mdl, gm); flds_m = mdl.fields(bm); c = mdl.psi_xy0(flds_m).item(); clm = 1 - c
P(f"planted solution: a0m={a0m} kap={kap} c_lm={clm:.12f} (gamma_m={gm:.12f}) c={c:+.12f} b_m range [{bm.min().item():.4f},{bm.max().item():.4f}] beta_m = mean b_m(inf) = {(mdl.rad.ext1_R @ bm).mean().item():.6f}")
def target_for(mdl):
    """manufactured source expressed as E-target on the model's grid: E[b_m(grid), c_lm] with the model's own w."""
    bmg = b_m(mdl, 1/clm)*0 + (lambda r, th: a0m*(1 + r**2/L**2)**((1/clm-1)/2)*(1 + kap*(r*torch.cos(th))**2/(L**2 + r**2))/mdl.wR[:, None])(mdl.rad.rR[:, None], mdl.ang.theta[None, :])
    return mdl.residual(bmg, clm)
Em = target_for(mdl); beta_m = (mdl.rad.ext1_R @ bm).mean().item()
F0, _, _ = mdl.system(bm, clm, gauge_value=beta_m, target=Em)
P(f"check: |F(b_m, c_lm)| with target = {F0.abs().max().item():.2e} (should be ~1e-15)")
# (A) perturbed start
torch.manual_seed(1)
bp = bm*(1 + 0.05*torch.randn_like(bm)*mdl.rad.s2R[:, None]) ; bp[0, :] = bm[0, 0]
bA, clA, infoA = ipm3.newton(mdl, bp, clm + 0.05, gauge_value=beta_m, target=Em, maxit=60, tol=1e-12, verbose=False, log=log)
P(f"(A) from 5% perturbation and c_l + 0.05: |F|={infoA['nF']:.1e} it={len(infoA['hist'])} -> cl={clA:.12f} (c_lm={clm:.12f}, diff {clA-clm:+.1e}) a0={bA[0,0].item():.8f} max|b - b_m|={(bA-bm).abs().max().item():.1e}")
# (B) from const
bc = beta_m*torch.ones(N+1, M, device=dev)
mdlB = ipm3.IPM3(N=N, M=M, L=L, gamma=gm, device=dev, couple_gamma=True); mdlB.gauge = 'inf'
bB, clB, infoB = ipm3.newton(mdlB, bc, clm, gauge_value=beta_m, target=target_for(mdlB), maxit=80, tol=1e-12, verbose=False, log=log)
P(f"(B) from b = const, c_l = c_lm: |F|={infoB['nF']:.1e} it={len(infoB['hist'])} -> cl={clB:.12f} a0={bB[0,0].item():.8f} max|b - b_m|={(bB-bm).abs().max().item():.1e}")
for cl0 in [1.3, 2.0, 3.0]:
    mdlB = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl0, device=dev, couple_gamma=True); mdlB.gauge = 'inf'
    bB, clB, infoB = ipm3.newton(mdlB, bc, cl0, gauge_value=beta_m, target=target_for(mdlB), maxit=80, tol=1e-12, verbose=False, log=log)
    sv = torch.linalg.svdvals(infoB['J'])
    P(f"(B) from b = const, c_l0 = {cl0}: |F|={infoB['nF']:.1e} it={len(infoB['hist'])} -> cl={clB:.12f} a0={bB[0,0].item():.8f} smin={sv[-1].item():.1e}")
# (C) forced scan in c_l
P("(C) forced continuation mu(c_l) at gauge beta_m, from b = const at each c_l (fresh starts) and continued:")
b_prev = None; mdl_prev = None; mu_prev = 0.0
for cl in [1.3, 1.5, 1.7, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.2, 3.5, 4.0]:
    mdlC = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdlC.gauge = 'inf'
    tgt = target_for(mdlC)
    bg = beta_m*torch.ones(N+1, M, device=dev)
    bC, _, infoC = ipm3.newton(mdlC, bg, cl, gauge_value=beta_m, target=tgt, maxit=80, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
    sv = torch.linalg.svdvals(infoC['J'])
    line = f"   cl={cl:.3f} fresh: mu={infoC['mu']:+.8f} a0={bC[0,0].item():.6f} |F|={infoC['nF']:.1e} smin={sv[-1].item():.1e}"
    if b_prev is not None:
        bg2 = ipm3.regrid(mdl_prev, b_prev, mdlC)
        bC2, _, infoC2 = ipm3.newton(mdlC, bg2, cl, gauge_value=beta_m, target=tgt, maxit=80, tol=1e-12, verbose=False, log=log, mu=mu_prev, forced=True)
        sv2 = torch.linalg.svdvals(infoC2['J'])
        line += f" | continued: mu={infoC2['mu']:+.8f} a0={bC2[0,0].item():.6f} |F|={infoC2['nF']:.1e} smin={sv2[-1].item():.1e}"
        if infoC2['nF'] < 1e-8: b_prev, mdl_prev, mu_prev = bC2, mdlC, infoC2['mu']
    elif infoC['nF'] < 1e-8:
        b_prev, mdl_prev, mu_prev = bC, mdlC, infoC['mu']
    P(line)
