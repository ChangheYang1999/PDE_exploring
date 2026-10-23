"""Planted-solution refinement test with a FIXED continuum source (referee planted1, objection 1).
S_m(X) := (c_lm X + U_m).grad rho_m - rho_m is computed ONCE on a fine reference grid (N_ref x M_ref) and then
interpolated (spectrally, through the off-grid evaluator of the reference model) onto every test grid; the target in
E-units on a grid with weight w is S_m/(y w).  So b_m is an exact discrete solution only up to the reference and
interpolation errors, not by construction.  Then: forced solves at fixed c_l (planted c_lm and the valley root near 2.258)
over 48x16 -> 48x24 -> 64x32 -> 96x48, as in manufactured_refine.py."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'; a0m = 3.0; kap = -0.5; L = 1.0; tag = 'manuf3_fixed'; log = open(f'runs/{tag}.log', 'a')
def P(msg): print(msg, flush=True); log.write(msg + "\n"); log.flush()
def b_m(mdl, gm):
    r = mdl.rad.rR[:, None]; th = mdl.ang.theta[None, :]; x2 = (r*torch.cos(th))**2
    return a0m*(1 + r**2/L**2)**((gm-1)/2)*(1 + kap*x2/(L**2 + r**2))/mdl.wR[:, None]
# c_lm fixed point on the reference grid
Nref, Mref = 160, 64
gm = 0.5
for it in range(40):
    mref = ipm3.IPM3(N=Nref, M=Mref, L=L, gamma=gm, device=dev); c = mref.psi_xy0(mref.fields(b_m(mref, gm))).item(); clm = 1 - c
    if abs(1/clm - gm) < 1e-13: break
    gm = 1/clm
mref = ipm3.IPM3(N=Nref, M=Mref, L=L, gamma=1/clm, device=dev); bref = b_m(mref, 1/clm); fref = mref.fields(bref)
Eref = mref.residual(bref, clm, fref)                       # E_m on the reference grid = S_m/(y w_ref)
P(f"reference {Nref}x{Mref}: c_lm = {clm:.12f}")
# S_m as a function: interpolate E_ref (class EE) spectrally, multiply by y w_ref at the point
Ehat_ref = mref.ang.to_coef(Eref, 'EE'); kk = torch.tensor(mref.ang.n_EE, dtype=torch.float64, device=dev)
def S_m_at(r_np, th_np):
    t = mref.rad.t_of_r(r_np.ravel()); PR = torch.tensor(ipm3.interp_matrix(mref.rad.tR_np, t, mref.rad.wR_np), device=dev)
    th_t = torch.tensor(th_np.ravel(), device=dev); C = torch.cos(th_t[:, None]*kk[None, :])
    E = ((PR @ Ehat_ref)*C).sum(1); tt = torch.tensor(t, device=dev); w = mref.rad.w_of_t(tt, mref.gamma); rr = torch.tensor(r_np.ravel(), device=dev)
    return (E*rr*torch.sin(th_t)*w).reshape(r_np.shape)      # S_m = E * y * w_ref
def target_for(mdl):
    r = mdl.rad.rR.cpu().numpy(); th = mdl.ang.theta_np; RR, TT = np.meshgrid(r, th, indexing='ij')
    S = S_m_at(RR, TT); yw = (mdl.rad.rR*mdl.wR)[:, None]*mdl.ang.sin[None, :]
    tg = S/yw; tg[0, :] = 0.0                                 # centre row: S_m = O(r^3) there; E-target at r=0 is 0 (identity holds for rho_m)
    return tg
beta_m = 2.25
# check: how exactly is b_m a discrete solution of the FIXED-source problem on each grid?
for (N, M) in [(48, 16), (48, 24), (64, 32), (96, 48)]:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/clm, device=dev); mdl.gauge = 'inf'
    F0, _, _ = mdl.system(b_m(mdl, 1/clm), clm, gauge_value=beta_m, target=target_for(mdl))
    P(f"  |F(b_m)| with the fixed interpolated source at {N}x{M}: {F0.abs().max().item():.2e}")
for cl in [clm, 2.258, 2.30]:
    mdl_p = None
    for (N, M) in [(48, 16), (48, 24), (64, 32), (96, 48)]:
        mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'; tgt = target_for(mdl)
        if mdl_p is None: bg = beta_m*torch.ones(N+1, M, device=dev); mu0 = 0.0
        else: bg = ipm3.regrid(mdl_p, b_p, mdl); bg = bg*(beta_m/(mdl.rad.ext1_R @ bg).mean().item()); mu0 = mu_p
        b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta_m, target=tgt, maxit=100, tol=1e-12, verbose=False, log=log, mu=mu0, forced=True)
        sv = torch.linalg.svdvals(info['J'])
        P(f"  cl={cl:.6f} N={N} M={M}: |F|={info['nF']:.1e} it={len(info['hist'])} mu={info['mu']:+.8f} a0={b[0,0].item():.8f} smin={sv[-1].item():.1e}")
        if info['nF'] < 1e-8: mdl_p, b_p, mu_p = mdl, b, info['mu']
