import sys, math, numpy as np, torch, sympy as sp
sys.path.insert(0, 'numerics/src')
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cpu'
gamma = 0.7; L = 1.1; a0 = 1.3; beta = 0.6; cl = 1.0/gamma
x, y = sp.symbols('x y', real=True)
r2 = x**2 + y**2
w_s = (1 + r2/L**2)**((gamma-1)/2)
s2 = r2/(L**2 + r2)
# b_m = a0 (1 + beta s^2 cos 2theta) = a0 (1 + beta (x^2-y^2)/(L^2+r^2))
b_s = a0*(1 + beta*(x**2 - y**2)/(L**2 + r2))
rho_s = y*w_s*b_s
f_s = sp.diff(rho_s, x)
rho_f = sp.lambdify((x, y), rho_s, 'numpy'); f_f = sp.lambdify((x, y), f_s, 'numpy')
rhox_f = sp.lambdify((x, y), sp.diff(rho_s, x), 'numpy'); rhoy_f = sp.lambdify((x, y), sp.diff(rho_s, y), 'numpy')
print("test 1: b = const -> c must be -a0/4 exactly (independent of L, gamma)")
for (N, M) in [(32, 8), (64, 12), (128, 16)]:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev)
    b = a0*torch.ones(N+1, M)
    flds = mdl.fields(b)
    c = mdl.psi_xy0(flds).item()
    E = mdl.residual(b, 1 - c, flds)
    print(f"  N={N} M={M}: c = {c:.14f}  (-a0/4 = {-a0/4:.14f}) diff {c + a0/4:.2e};  |E| at centre row {E[0].abs().max():.2e}  |E| max {E.abs().max():.3e} (nonzero: b=const is not a solution)")
print("test 2: manufactured b_m = a0 (1 + beta s^2 cos 2theta): Poisson source Fhat vs sympy, c vs quadrature formula, residual vs FD")
for (N, M) in [(32, 8), (64, 12), (128, 16), (192, 24)]:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev)
    rR = mdl.rad.rR; th = mdl.ang.theta
    b = a0*(1 + beta*mdl.rad.s2R[:, None]*torch.cos(2*th)[None, :])
    flds = mdl.fields(b)
    # Fhat on the Lobatto fine grid vs sympy (interior rows)
    tL = mdl.rad.tL_np.copy(); tL[-1] = 1 - 1e-12; tL[0] = -1 + 1e-12
    rL = mdl.rad.rmap(torch.tensor(tL)).numpy(); thf = mdl.angf.theta_np
    XL = rL[:, None]*np.cos(thf)[None, :]; YL = rL[:, None]*np.sin(thf)[None, :]
    wL = (1 + rL**2/L**2)**((gamma-1)/2)
    Fex = torch.tensor(f_f(XL, YL)/wL[:, None])
    eF = (flds['Fhat_L'] - Fex).abs()
    # c from the quadrature formula: c = -a0/4 + int_0^inf rho_3(r) r^-2 dr, rho_3 = sin 3theta coefficient of rho
    # rho = r w sin(th) b, sin th cos 2k th = [sin((2k+1)th) - sin((2k-1)th)]/2 -> rho_3 = r w (bhat_1 - bhat_2)/2
    bhat = mdl.ang.to_coef(b, 'EE')
    tg, wg = ipm3.gauss_legendre(400)
    Pg = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tg, mdl.rad.wR_np))
    bh = Pg @ bhat
    tgt = torch.tensor(tg); s2g = mdl.rad.s2_of_t(tgt); wgt = mdl.rad.w_of_t(tgt, gamma)
    Qg = (1 - tgt) + mdl.p*(1 + tgt)
    # int rho_3 r^-2 dr = int w (bhat1 - bhat2)/(2 r) dr = int w (bhat1-bhat2)/2 * Q/(1-t^2) dt
    integrand = wgt*(bh[:, 1] - bh[:, 2])/2*Qg/(1 - tgt**2)
    cq = -a0/4 + (integrand*torch.tensor(wg)).sum().item()
    c = mdl.psi_xy0(flds).item()
    # residual check at interior Radau points by central FD on rho (sympy rho), with U from the model evaluate()
    cl_t = 1 - c
    E = mdl.residual(b, cl_t, flds)
    rr = rR.numpy()[1:]; tt = th.numpy()
    RR, TT = np.meshgrid(rr, tt, indexing='ij')
    ev = mdl.evaluate(b, cl_t, flds, RR, TT)
    X = RR*np.cos(TT); Y = RR*np.sin(TT)
    rho_x = rhox_f(X, Y); rho_y = rhoy_f(X, Y); rho = rho_f(X, Y)
    R_ind = (cl_t*X + ev['U1'])*rho_x + (cl_t*Y + ev['U2'])*rho_y - rho
    wR = (1 + RR**2/L**2)**((gamma-1)/2)
    E_ind = R_ind/(Y*wR)
    eE = np.abs(E[1:].numpy() - E_ind)
    # evaluate() self-consistency: rho, grad rho vs sympy at off-grid points
    rq = np.array([0.01, 0.3, 1.0, 2.5, 7.0, 30.0, 300.0]); tq = np.array([0.1, 0.5, 1.0, 1.4])
    RQ, TQ = np.meshgrid(rq, tq, indexing='ij'); XQ = RQ*np.cos(TQ); YQ = RQ*np.sin(TQ)
    evq = mdl.evaluate(b, cl_t, flds, RQ, TQ)
    e_rho = np.abs(evq['rho'] - rho_f(XQ, YQ))/np.abs(rho_f(XQ, YQ))
    e_gx = np.abs(evq['rho_x'] - rhox_f(XQ, YQ))/(np.abs(rhox_f(XQ, YQ)) + np.abs(rhoy_f(XQ, YQ)))
    e_gy = np.abs(evq['rho_y'] - rhoy_f(XQ, YQ))/(np.abs(rhox_f(XQ, YQ)) + np.abs(rhoy_f(XQ, YQ)))
    print(f"  N={N:3d} M={M:2d}: |Fhat err| {eF.max():.2e} (t=-1 row {eF[0].max():.2e}, t=1 row {eF[-1].max():.2e});  c = {c:.12f}, quadrature formula {cq:.12f}, diff {c-cq:.2e};"
          f"  |E - E_ind| max {eE.max():.2e} (|E| max {np.abs(E_ind).max():.2e});  off-grid rho err {e_rho.max():.1e} grad err {max(e_gx.max(), e_gy.max()):.1e}")
print("test 3: Jacobian vs finite differences (random directions)")
for (N, M) in [(24, 6), (48, 10)]:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev)
    th = mdl.ang.theta
    b = a0*(1 + beta*mdl.rad.s2R[:, None]*torch.cos(2*th)[None, :]) + 0.1*mdl.rad.s2R[:, None]**2*torch.cos(4*th)[None, :]
    flds = mdl.fields(b); c = mdl.psi_xy0(flds).item(); cl_t = 1 - c + 0.05
    J = mdl.jacobian(b, cl_t, flds)
    nb = (N+1)*M
    torch.manual_seed(0)
    for trial in range(3):
        du = torch.randn(nb + 1); du[-1] *= 0.3
        eps = 1e-6
        Fp, _, _ = mdl.system(b + eps*du[:nb].reshape(N+1, M), cl_t + eps*du[-1].item())
        Fm, _, _ = mdl.system(b - eps*du[:nb].reshape(N+1, M), cl_t - eps*du[-1].item())
        fd = (Fp - Fm)/(2*eps)
        Jd = J @ du
        print(f"  N={N} M={M} trial {trial}: |J du - FD| / |J du| = {(Jd - fd).abs().max().item()/Jd.abs().max().item():.2e}")
    # exact: the system is quadratic in b, so with eps = 1 the central difference is exact in b; check that too
    du = torch.randn(nb + 1); du[-1] = 0.0
    Fp, _, _ = mdl.system(b + du[:nb].reshape(N+1, M), cl_t); Fm, _, _ = mdl.system(b - du[:nb].reshape(N+1, M), cl_t)
    print(f"  quadratic structure check (eps=1, b only): {((Fp - Fm)/2 - J @ du).abs().max().item():.2e}")
    print(f"  Jacobian size {J.shape}, cond estimate (2-norm, small case) {torch.linalg.cond(J).item():.3e}, smallest singular values {torch.linalg.svdvals(J)[-4:].numpy()}")
