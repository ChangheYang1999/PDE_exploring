"""Checks on a saved (unforced) state: (I1) c_l + c - 1 with c from the solver and from the modal strain formula
c = -a0/4 + int rho_3 r^-2 dr (quadrature in r of the sin 3theta mode); (I5') J := int rho U.grad(r^-3 sin 3th) dX
(angular integration first, radial Gauss quadrature in t) against -pi (c_l - 1)(c_l - 1 + a0/4); Chebyshev tail of b_0
with sign pattern and algebraic slope; (T1) cubic Taylor relation e = (a0 - 2A) b/6 from the radial Taylor coefficients
of the modes (b = rho_xxy(0)/2, e = rho_yyy(0)/6: rho_1 = a0 r + ((b+3e)/4) r^3, rho_3 = ((b-e)/4) r^3)."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
for f in sys.argv[1:]:
    st = torch.load(f); N, M, L = st['N'], st['M'], st['L']; cl = st['cl']; gamma = 1/cl
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=st['gamma'], p=st['p'], device=dev); b = st['b'].to(dev); flds = mdl.fields(b)
    c_solver = mdl.psi_xy0(flds).item(); a0 = b[0,0].item(); A = 2*cl - 1
    bhat = mdl.ang.to_coef(b, 'EE')
    # radial Gauss quadrature in t
    tg, wg = ipm3.gauss_legendre(2000); tgt = torch.tensor(tg, device=dev); wgt = torch.tensor(wg, device=dev)
    P = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tg, mdl.rad.wR_np), device=dev)
    bh = P @ bhat                                       # mode coefficients of b at Gauss points
    w = mdl.rad.w_of_t(tgt, mdl.gamma); Q = (1 - tgt) + mdl.p*(1 + tgt); r = mdl.rad.rmap(tgt)
    dr_over_r = Q/(1 - tgt**2)                          # dr/r = (Q/(1-t^2)) dt
    # rho_3(r) = r w (bhat1 - bhat2)/2 ;  int rho_3 r^-2 dr = int w (bhat1 - bhat2)/2 dr/r
    I3 = (w*(bh[:,1] - bh[:,2])/2*dr_over_r*wgt).sum().item()
    c_formula = -a0/4 + I3
    # (I5'): J = int rho U.grad(phi) dX, phi = r^-3 sin 3th. grad phi = e_r (-3 r^-4 sin3th) + e_th (3 r^-4 cos 3th).
    # U.grad phi = 3 r^-4 (U_th cos3th - U_r sin3th) with U_r = r Ur_r, U_th = r Uth_r (grid values).  Angular quadrature
    # on the fine quadrant grid is exact for trigonometric polynomials up to the dealiasing degree; use the coarse grid
    # pointwise products with the M-point midpoint rule times 4 quadrants (exact for the parity class up to degree 2M-1).
    th = mdl.ang.theta; dth = math.pi/(2*M)
    rho = mdl.rho_from_b(b)                             # (N+1, M) Radau grid
    Ur = mdl.rad.rR[:,None]*flds['Ur_r']; Uth = mdl.rad.rR[:,None]*flds['Uth_r']
    integrand_ang = (rho*3/mdl.rad.rR[:,None]**4*(Uth*torch.cos(3*th)[None,:] - Ur*torch.sin(3*th)[None,:])).sum(1)*dth*4   # (N+1,)
    integrand_ang[0] = 0.0
    # radial: int ... r dr = int (...) r^2 dr/r ; interpolate the angular integral (times r^2) from Radau to Gauss nodes
    g_rad = integrand_ang*mdl.rad.rR**2                # finite at 0 (rho ~ r, U ~ r, r^-4 -> r^-2, times r^2 -> O(1)... check)
    g_gauss = P @ g_rad
    J = (g_gauss*dr_over_r*wgt).sum().item()
    J_pred = -math.pi*(cl - 1)*(cl - 1 + a0/4)
    # Chebyshev tail of beta_0 = bhat[:,0]
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(N+1))); ck = np.linalg.lstsq(V, bhat[:,0].cpu().numpy(), rcond=None)[0]
    n = np.arange(N+1); tail = slice(N//2, N-2); s = ((-1.0)**n*ck)[tail]
    sl = np.polyfit(np.log(n[tail]), np.log(np.abs(s)+1e-300), 1)[0]
    # Taylor coefficients at the centre from the modes: fit bhat_k(r) on small r: b0 = a0 + b0_2 r^2 + ..., b1 = b1_2 r^2 + ...
    rr = np.logspace(-3.5, -1.5, 30); tt = mdl.rad.t_of_r(rr); Pr = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev)
    bk = (Pr @ bhat).cpu().numpy(); wr = mdl.rad.w_of_t(torch.tensor(tt), mdl.gamma).numpy()
    # rho_1 = r w (b0 - b1/2) [sin th cos 2th = (sin3th - sin th)/2 -> sin th coefficient: b0 - b1/2], rho_3 = r w (b1 - b2)/2
    rho1 = rr*wr*(bk[:,0] - bk[:,1]/2); rho3 = rr*wr*(bk[:,1] - bk[:,2])/2
    c1 = np.polyfit(rr**2, rho1/rr, 2); c3 = np.polyfit(rr**2, rho3/rr, 2)        # rho1/r = a0 + ((b+3e)/4) r^2 + ..., rho3/r = ((b-e)/4) r^2 + ...
    s13 = 4*c1[1]; d13 = 4*c3[1]           # b + 3e, b - e
    bb = (s13 + 3*d13)/4; ee = (s13 - d13)/4
    T1_lhs, T1_rhs = ee, (a0 - 2*A)*bb/6
    print(f"{f}: N={N} M={M} cl={cl:.8f} a0={a0:.6f} A={A:.4f}")
    print(f"   (I1) c_solver={c_solver:+.10f}  c_formula(-a0/4 + int rho_3 r^-2)={c_formula:+.10f}  diff={c_solver-c_formula:+.2e}   cl+c-1={cl+c_solver-1:+.2e}")
    print(f"   (I5') J=int rho U.grad(r^-3 sin3th) = {J:+.8f}   predicted -pi(cl-1)(cl-1+a0/4) = {J_pred:+.8f}   rel diff {abs(J-J_pred)/abs(J_pred):.2e}")
    print(f"   cheb tail beta0 (n = N/2..N-3): sign fraction(+) {(s>0).mean():.2f}, slope {sl:+.2f} -> alpha = d-1 ~ {(-sl-1)/2:.2f}; |c_N/2| {abs(ck[N//2]):.1e} |c_N-3| {abs(ck[N-3]):.1e}")
    print(f"   (T1) cubic: b=rho_xxy/2={bb:+.5e} e=rho_yyy/6={ee:+.5e}; e - (a0-2A)b/6 = {T1_lhs-T1_rhs:+.3e} (rel {abs(T1_lhs-T1_rhs)/max(abs(T1_rhs),1e-300):.2e}); rho3 fit residual {np.abs(np.polyval(c3, rr**2) - rho3/rr).max():.1e}")
