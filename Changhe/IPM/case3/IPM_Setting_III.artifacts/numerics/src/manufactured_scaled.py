"""Referee P6: scaled planted family.  S_{m,lam}(X) = lam S_m(X/lam) has the exact solution rho_{m,lam} = lam rho_m(X/lam)
with the same c_lm and a0 and gauge beta_lam = lam^(1-g) beta_m.  Test: forced solve at (c_lm, beta_lam) with the scaled
source from b = const; the result must have mu = 0, a0 = 3, and the rescaled-back field must match rho_m."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'; a0m = 3.0; kap = -0.5; L = 1.0; log = open('runs/manuf4_scaled.log', 'a')
def P(msg): print(msg, flush=True); log.write(msg + "\n"); log.flush()
def rho_m_over_y(r, th, gm):   # rho_m / y as a function (torch), scale lam applied outside
    x2 = (r*torch.cos(th))**2
    return a0m*(1 + r**2/L**2)**((gm-1)/2)*(1 + kap*x2/(L**2 + r**2))
Nref, Mref = 160, 64; gm = 0.5
for it in range(40):
    mref = ipm3.IPM3(N=Nref, M=Mref, L=L, gamma=gm, device=dev)
    bref = rho_m_over_y(mref.rad.rR[:, None], mref.ang.theta[None, :], gm)/mref.wR[:, None]
    c = mref.psi_xy0(mref.fields(bref)).item(); clm = 1 - c
    if abs(1/clm - gm) < 1e-13: break
    gm = 1/clm
mref = ipm3.IPM3(N=Nref, M=Mref, L=L, gamma=1/clm, device=dev)
bref = rho_m_over_y(mref.rad.rR[:, None], mref.ang.theta[None, :], 1/clm)/mref.wR[:, None]
Eref = mref.residual(bref, clm, mref.fields(bref)); Ehat = mref.ang.to_coef(Eref, 'EE'); kk = torch.tensor(mref.ang.n_EE, dtype=torch.float64, device=dev)
def S_m_at(r_np, th_np):
    t = mref.rad.t_of_r(r_np.ravel()); PR = torch.tensor(ipm3.interp_matrix(mref.rad.tR_np, t, mref.rad.wR_np), device=dev)
    th_t = torch.tensor(th_np.ravel(), device=dev); C = torch.cos(th_t[:, None]*kk[None, :])
    E = ((PR @ Ehat)*C).sum(1); tt = torch.tensor(t, device=dev); w = mref.rad.w_of_t(tt, mref.gamma); rr = torch.tensor(r_np.ravel(), device=dev)
    return (E*rr*torch.sin(th_t)*w).reshape(r_np.shape)
beta_m = 2.25; gam = 1/clm
P(f"c_lm = {clm:.12f}")
for lam in [0.5, 1.0, 2.0, 5.0]:
    N, M = 64, 32
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gam, device=dev); mdl.gauge = 'inf'
    r = mdl.rad.rR.cpu().numpy(); th = mdl.ang.theta_np; RR, TT = np.meshgrid(r, th, indexing='ij')
    S = lam*S_m_at(RR/lam, TT); yw = (mdl.rad.rR*mdl.wR)[:, None]*mdl.ang.sin[None, :]
    tgt = S/yw; tgt[0, :] = 0.0
    beta_lam = lam**(1-gam)*beta_m
    # exact scaled planted field on this grid: rho_lam/y = rho_m(X/lam)/(y/lam) = (rho_m/y)(r/lam) ; b = that / w
    b_exact = rho_m_over_y(mdl.rad.rR[:, None]/lam, mdl.ang.theta[None, :], gam)/mdl.wR[:, None]
    F0, _, _ = mdl.system(b_exact, clm, gauge_value=beta_lam, target=tgt)
    bg = beta_lam*torch.ones(N+1, M, device=dev)
    b, _, info = ipm3.newton(mdl, bg, clm, gauge_value=beta_lam, target=tgt, maxit=100, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
    P(f"lam={lam}: beta_lam={beta_lam:.6f} |F(exact scaled planted)|={F0.abs().max().item():.1e}; forced solve from const: |F|={info['nF']:.1e} it={len(info['hist'])} mu={info['mu']:+.3e} a0={b[0,0].item():.8f} max|b - b_exact|={(b-b_exact).abs().max().item():.1e}")
