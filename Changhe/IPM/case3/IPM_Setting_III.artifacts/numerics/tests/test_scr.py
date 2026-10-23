import sys, math, numpy as np, torch, sympy as sp
sys.path.insert(0, 'numerics/src')
import ipm3, ipm3s
torch.set_default_dtype(torch.float64)
dev = 'cpu'
print("== SCR test 1: Poisson inverse with manufactured psi (odd/odd, ~r^(gamma+1)); psi_xy(0)=1 exactly")
gamma = 0.6; L = 1.3; alpha = 0.7
x, y = sp.symbols('x y', real=True); r2 = x**2 + y**2
psi_s = x*y*(1 + r2/L**2)**((gamma-1)/2)*(1 + alpha*(x**2 - y**2)/(1 + r2))
f_f = sp.lambdify((x, y), -(sp.diff(psi_s, x, 2) + sp.diff(psi_s, y, 2)), 'numpy'); psi_f = sp.lambdify((x, y), psi_s, 'numpy')
U1_f = sp.lambdify((x, y), -sp.diff(psi_s, y), 'numpy'); U2_f = sp.lambdify((x, y), sp.diff(psi_s, x), 'numpy')
for (N, M) in [(32, 8), (64, 12), (128, 16)]:
    mdl = ipm3s.IPM3S(N=N, M=M, L=L, gamma=gamma, device=dev)
    tL = mdl.rad.tL_np.copy(); tL[-1] = 1 - 1e-13; tL[0] = -1 + 1e-13
    rL = mdl.rad.rmap_np(tL); wL = (1 - tL)/2; thf = mdl.angf.theta_np
    X = rL[:, None]*np.cos(thf)[None, :]; Y = rL[:, None]*np.sin(thf)[None, :]
    Fhat = torch.tensor(f_f(X, Y)/wL[:, None])
    PsiC, I1, I2 = mdl.poisson_modes(Fhat)
    Psi_Lf = PsiC @ torch.sin(torch.tensor(thf)[:, None]*mdl.nf[None, :]).T
    Psi_ex = torch.tensor(psi_f(X, Y)/(rL[:, None]**2*wL[:, None]))
    err = (Psi_Lf - Psi_ex).abs()
    # velocity via evaluate at off-grid points (uses PsiC only): compare U
    rq = np.array([0.01, 0.3, 1.0, 2.5, 7.0, 30.0]); tq = np.array([0.1, 0.5, 1.0, 1.4])
    RQ, TQ = np.meshgrid(rq, tq, indexing='ij'); XQ = RQ*np.cos(TQ); YQ = RQ*np.sin(TQ)
    beta0 = torch.zeros(N+1, M)
    ev = mdl.evaluate(beta0, 1.0, dict(PsiC=PsiC), RQ, TQ)
    eU = max(np.abs(ev['U1'] - U1_f(XQ, YQ)).max(), np.abs(ev['U2'] - U2_f(XQ, YQ)).max())/np.abs(U1_f(XQ,YQ)).max()
    print(f"  N={N} M={M}: |Psi~ err| max {err.max():.2e} (t=1 row {err[-1].max():.2e}); off-grid U rel err {eU:.2e}; psi_xy(0) = {2*PsiC[0,0].item():.13f}")
print("== SCR test 2: beta = const -> c = -a0/4 exactly; manufactured beta -> residual vs FD on rho, off-grid consistency")
gamma = 0.7; L = 1.1; a0 = 1.3; cl = 1/gamma
for (N, M) in [(32, 8), (64, 12), (128, 16)]:
    mdl = ipm3s.IPM3S(N=N, M=M, L=L, gamma=gamma, device=dev)
    beta = torch.zeros(N+1, M); beta[:, 0] = a0
    flds = mdl.fields(beta); c = mdl.psi_xy0(flds).item()
    E = mdl.residual(beta, 1 - c, flds)
    print(f"  N={N} M={M}: const beta: c + a0/4 = {c + a0/4:.2e}; centre row |E| {E[0].abs().max():.1e}", end='')
    # manufactured: beta_0 = a0 (1 + 0.3 sigma), beta_1 = 0.6 a0 (1 - 0.5 sigma), beta_2 = 0.2 a0  -> b = sum sigma^k beta_k cos 2k th
    sig = mdl.rad.sigR
    beta = torch.zeros(N+1, M); beta[:, 0] = a0*(1 + 0.3*sig); beta[:, 1] = 0.6*a0*(1 - 0.5*sig); beta[:, 2] = 0.2*a0
    flds = mdl.fields(beta); c = mdl.psi_xy0(flds).item(); clt = 1 - c
    E = mdl.residual(beta, clt, flds)
    # independent: rho(x,y) exactly from the formula (t from r by bisection), FD gradient, U from evaluate
    def rho_exact(X, Y):
        R = np.sqrt(X**2 + Y**2); TH = np.arctan2(Y, X); t = mdl.rad.t_of_r(R); s = (1+t)/2; w = (1-t)/2
        b = a0*(1 + 0.3*s) + s*0.6*a0*(1 - 0.5*s)*np.cos(2*TH) + s**2*0.2*a0*np.cos(4*TH)
        return Y*w*b
    rr = mdl.rad.rR.numpy()[1:]; th = mdl.ang.theta_np
    RR, TT = np.meshgrid(rr, th, indexing='ij'); X = RR*np.cos(TT); Y = RR*np.sin(TT)
    h = 1e-5*np.maximum(RR, 1e-3)
    rho_x = (rho_exact(X+h, Y) - rho_exact(X-h, Y))/(2*h); rho_y = (rho_exact(X, Y+h) - rho_exact(X, Y-h))/(2*h)
    ev = mdl.evaluate(beta, clt, flds, RR, TT)
    R_ind = (clt*X + ev['U1'])*rho_x + (clt*Y + ev['U2'])*rho_y - rho_exact(X, Y)
    t = mdl.rad.t_of_r(RR); w = (1-t)/2
    E_ind = R_ind/(Y*w)
    print(f";  manufactured: |E - E_FD| max {np.abs(E[1:].numpy() - E_ind).max():.2e} (|E| max {np.abs(E_ind).max():.2e});"
          f" evaluate rho err {np.abs(ev['rho'] - rho_exact(X,Y)).max():.1e}, grad err {max(np.abs(ev['rho_x']-rho_x).max(), np.abs(ev['rho_y']-rho_y).max()):.1e} (FD-limited)")
print("== SCR test 3: Jacobian vs FD (plain, forced), gauge K; regrid round trip")
for (N, M) in [(24, 6), (48, 10)]:
    mdl = ipm3s.IPM3S(N=N, M=M, L=L, gamma=gamma, device=dev)
    sig = mdl.rad.sigR
    beta = torch.zeros(N+1, M); beta[:, 0] = a0*(1 + 0.3*sig); beta[:, 1] = 0.6*a0*(1 - 0.5*sig); beta[:, 2] = 0.2*a0 + 0.1*sig**2
    beta[0, 1:] = (mdl.rad.extm1_int @ beta[1:, 1:]).reshape(-1)
    nb = (N+1)*M; clt = 1/gamma + 0.1; torch.manual_seed(0)
    flds = mdl.fields(beta)
    J = mdl.jacobian(beta, clt, flds)
    for trial in range(2):
        du = torch.randn(nb+1); eps = 1e-6
        Fp,_,_ = mdl.system(beta + eps*du[:nb].reshape(N+1, M), clt + eps*du[-1].item()); Fm,_,_ = mdl.system(beta - eps*du[:nb].reshape(N+1, M), clt - eps*du[-1].item())
        print(f"  N={N} M={M} plain: |J du - FD|/|J du| = {(J@du - (Fp-Fm)/(2*eps)).abs().max().item()/(J@du).abs().max().item():.2e}")
    mu = 0.37; J = mdl.jacobian(beta, clt, flds, forced=True)
    du = torch.randn(nb+1); eps = 1e-6
    Fp,_,_ = mdl.system(beta + eps*du[:nb].reshape(N+1, M), clt, mu=mu + eps*du[-1].item(), forced=True); Fm,_,_ = mdl.system(beta - eps*du[:nb].reshape(N+1, M), clt, mu=mu - eps*du[-1].item(), forced=True)
    print(f"  N={N} M={M} forced: |J du - FD|/|J du| = {(J@du - (Fp-Fm)/(2*eps)).abs().max().item()/(J@du).abs().max().item():.2e}")
    mdl2 = ipm3s.IPM3S(N=N+16, M=M+2, L=L*1.5, gamma=gamma+0.05, device=dev)
    beta2 = ipm3s.regrid_s(mdl, beta, mdl2)
    rq = np.array([0.01, 0.3, 1.0, 2.5, 7.0, 30.0, 1000.]); tq = np.array([0.1, 0.5, 1.0, 1.4]); RQ, TQ = np.meshgrid(rq, tq, indexing='ij')
    e1 = mdl.evaluate(beta, clt, flds, RQ, TQ); e2 = mdl2.evaluate(beta2, clt, mdl2.fields(beta2), RQ, TQ)
    print(f"  regrid (N,M,L,gamma changed): rho err {np.abs(e1['rho']-e2['rho']).max()/np.abs(e1['rho']).max():.2e}, grad err {np.abs(e1['rho_y']-e2['rho_y']).max()/np.abs(e1['rho_y']).max():.2e}, U err {np.abs(e1['U2']-e2['U2']).max()/np.abs(e1['U2']).max():.2e}")
