"""Residual table for the planted solution of the fixed-source manufactured problem (NUM_REPORT 4C(D')):
R_m = (c_lm X + U[rho]).grad rho - rho - S_m at between-node points, S_m interpolated from the 160x64 reference."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'; a0m = 3.0; kap = -0.5; L = 1.0
def b_m(mdl, gm):
    r = mdl.rad.rR[:, None]; th = mdl.ang.theta[None, :]; x2 = (r*torch.cos(th))**2
    return a0m*(1 + r**2/L**2)**((gm-1)/2)*(1 + kap*x2/(L**2 + r**2))/mdl.wR[:, None]
Nref, Mref = 160, 64; gm = 0.5
for it in range(40):
    mref = ipm3.IPM3(N=Nref, M=Mref, L=L, gamma=gm, device=dev); c = mref.psi_xy0(mref.fields(b_m(mref, gm))).item(); clm = 1 - c
    if abs(1/clm - gm) < 1e-13: break
    gm = 1/clm
mref = ipm3.IPM3(N=Nref, M=Mref, L=L, gamma=1/clm, device=dev); bref = b_m(mref, 1/clm); fref = mref.fields(bref)
Eref = mref.residual(bref, clm, fref); Ehat = mref.ang.to_coef(Eref, 'EE'); kk = torch.tensor(mref.ang.n_EE, dtype=torch.float64, device=dev)
def S_m_at(r_np, th_np):
    t = mref.rad.t_of_r(r_np.ravel()); PR = torch.tensor(ipm3.interp_matrix(mref.rad.tR_np, t, mref.rad.wR_np), device=dev)
    th_t = torch.tensor(th_np.ravel(), device=dev); C = torch.cos(th_t[:, None]*kk[None, :])
    E = ((PR @ Ehat)*C).sum(1); tt = torch.tensor(t, device=dev); w = mref.rad.w_of_t(tt, mref.gamma); rr = torch.tensor(r_np.ravel(), device=dev)
    return (E*rr*torch.sin(th_t)*w).reshape(r_np.shape).cpu().numpy()
for (N, M) in [(48, 16), (96, 48)]:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/clm, device=dev); b = b_m(mdl, 1/clm); flds = mdl.fields(b)
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np
    thm = np.concatenate([[0.25*th[0], 0.5*th[0]], 0.5*(th[:-1]+th[1:]), [0.5*(th[-1]+np.pi/2), np.pi/2 - 0.25*(np.pi/2-th[-1])]])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, clm, flds, RR, TT); Rm = ev['R'] - S_m_at(RR, TT)
    print(f"planted solution rho_m (a0 = {a0m}, kappa = {kap}), c_lm = {clm:.12f}, grid {N}x{M}; residual of the manufactured problem R_m = R - S_m")
    print("   region r          points   max|R_m|     max|R_m|/N_f   max|R_m|/N_v   min N_f     max|S_m|")
    for lo, hi in [(0, 0.01), (0.01, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e8), (1e8, 1e30)]:
        m = (RR >= lo) & (RR < hi)
        if not m.any(): continue
        print(f"   [{lo:8.0e},{hi:8.0e}) {m.sum():6d}   {np.abs(Rm[m]).max():.2e}     {(np.abs(Rm[m])/ev['Nf'][m]).max():.2e}       {(np.abs(Rm[m])/ev['Nv'][m]).max():.2e}       {ev['Nf'][m].min():.2e}    {np.abs(S_m_at(RR, TT)[m]).max():.2e}")
