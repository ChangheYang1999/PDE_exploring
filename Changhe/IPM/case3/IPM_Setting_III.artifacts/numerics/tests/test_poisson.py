import sys, math, numpy as np, torch, sympy as sp
sys.path.insert(0, 'numerics/src')
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cpu'
gamma = 0.6; L = 1.3; alpha = 0.7
x, y = sp.symbols('x y', real=True)
r2 = x**2 + y**2
# manufactured psi: odd in x and y, ~ r^(gamma+1) at infinity, psi_xy(0) = 1 exactly
psi_s = x*y*(1 + r2/L**2)**sp.Rational(1,1)*0
psi_s = x*y*(1 + r2/L**2)**((gamma-1)/2)*(1 + alpha*(x**2 - y**2)/(1 + r2))
f_s = -(sp.diff(psi_s, x, 2) + sp.diff(psi_s, y, 2))
psi_f = sp.lambdify((x, y), psi_s, 'numpy'); f_f = sp.lambdify((x, y), f_s, 'numpy')
U1_f = sp.lambdify((x, y), -sp.diff(psi_s, y), 'numpy'); U2_f = sp.lambdify((x, y), sp.diff(psi_s, x), 'numpy')
for (N, M) in [(32, 8), (64, 12), (128, 16), (192, 24)]:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev)
    tL = mdl.rad.tL_np.copy(); tL[-1] = 1 - 1e-13; tL[0] = -1 + 1e-13
    rL = mdl.rad.rmap(torch.tensor(tL)).numpy()
    thf = mdl.angf.theta_np
    X = rL[:, None]*np.cos(thf)[None, :]; Y = rL[:, None]*np.sin(thf)[None, :]
    wL = (1 + rL**2/L**2)**((gamma-1)/2)
    Fhat = torch.tensor(f_f(X, Y)/wL[:, None])
    PsiC, I1, I2 = mdl.poisson_modes(Fhat)
    Psi_Lf = PsiC @ torch.sin(torch.tensor(thf)[:, None]*mdl.nf[None, :]).T
    Psi_ex = torch.tensor(psi_f(X, Y)/(rL[:, None]**2*wL[:, None]))
    err = (Psi_Lf - Psi_ex).abs()
    # velocity on the Radau grid through fields-like evaluation
    rad, ang = mdl.rad, mdl.ang
    cos, sin = ang.cos[None, :], ang.sin[None, :]
    PsiC_R = rad.P_LR @ PsiC
    Psi = PsiC_R @ mdl.S_OO_fc.T
    rPsi_r = (rad.gR[:, None]*(rad.DR @ PsiC_R)) @ mdl.S_OO_fc.T
    Psi_th = PsiC_R @ mdl.Sd_OO_fc.T
    G = (2 + mdl.omegaR)[:, None]*Psi + rPsi_r
    rv = (rad.rR*mdl.vR)[:, None]
    U1 = rv*(-(sin*G + cos*Psi_th)); U2 = rv*(cos*G - sin*Psi_th)
    rR = rad.rR.numpy(); th = ang.theta_np
    XR = rR[:, None]*np.cos(th)[None, :]; YR = rR[:, None]*np.sin(th)[None, :]
    U1ex = torch.tensor(U1_f(XR, YR)); U2ex = torch.tensor(U2_f(XR, YR))
    mask = torch.tensor(rR <= 5.0)
    e1 = ((U1 - U1ex).abs()/(1 + U1ex.abs()))[mask].max(); e2 = ((U2 - U2ex).abs()/(1 + U2ex.abs()))[mask].max()
    e1f = ((U1 - U1ex).abs()/(U1ex.abs())).max(); e2f = ((U2 - U2ex).abs()/(U2ex.abs())).max()
    print(f"N={N:4d} M={M:3d} |Psi~ err| max {err.max():.2e} (t=1 row {err[-1].max():.2e}, t=-1 row {err[0].max():.2e})"
          f"  rel U err r<=5: {e1:.2e} {e2:.2e}  rel U err all r (rmax {rR.max():.1e}): {e1f:.2e} {e2f:.2e}")
    print(f"      psi_xy(0): numeric {2*PsiC[0,0].item():.13f}  exact 1.0")
