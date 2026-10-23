"""(T2) check of SPEC 4.3: H := q1 - q2 = int_0^inf s^-3 f_2(s) ds (f_2 = sin 4theta mode of d_x rho) must equal
(a0 - 4A) b/(3 a0) with b = rho_xxy(0)/2 for a smooth exact profile.  b is extracted from the cubic Taylor coefficients
of the modes (rho_1 = a0 r + ((b+3e)/4) r^3, rho_3 = ((b-e)/4) r^3) by a small-r fit; H from the modal integral with Gauss
quadrature in t.  Also validates on the planted manufactured solution (manufactured_test.py parameters) where the
identity holds for the manufactured problem only in modified form, so the real test is the valley states."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
def t2(mdl, b, cl, label):
    flds = mdl.fields(b); N, M = mdl.N, mdl.M; a0 = b[0,0].item(); A = 2*cl - 1
    # f_2 = sin(4 theta) mode of d_x rho = w * Fhat_4 ; Fhat_L: (N+1 Lobatto, M2 fine angular values) -> OO modes
    C = flds['Fhat_L'] @ mdl.angf.A['OO'].T          # (N+1, M2) coefficients of sin(2(k+1) theta): k=0 -> sin2, k=1 -> sin4
    F4_L = C[:, 1]                                    # Lobatto values of Fhat_4(t)
    tg, wg = ipm3.gauss_legendre(3000); tgt = torch.tensor(tg, device=dev); wgt = torch.tensor(wg, device=dev)
    PL = torch.tensor(ipm3.interp_matrix(mdl.rad.tL_np, tg, mdl.rad.wL_np), device=dev)
    F4 = PL @ F4_L
    w = mdl.rad.w_of_t(tgt, mdl.gamma); r = mdl.rad.rmap(tgt); Q = (1 - tgt) + mdl.p*(1 + tgt); dr_over_r = Q/(1 - tgt**2)
    # int s^-3 f_2 ds = int w Fhat_4 r^-3 dr = int w Fhat_4 r^-2 dr/r ; near 0 Fhat_4 ~ r^4 -> integrand ~ r^2 fine
    H = (w*F4/r**2*dr_over_r*wgt).sum().item()
    rn = r.cpu().numpy(); integ = (w*F4/r**2*dr_over_r*wgt).cpu().numpy()
    Heps = {eps: integ[rn > eps].sum() for eps in [1e-1, 1e-2, 1e-3, 1e-4]}
    ks = sorted(Heps); sl = [np.log(abs(Heps[ks[i]]-Heps[ks[i+1]]) + 1e-300)/1 for i in range(len(ks)-1)]
    print(f"   H(eps) = int_{{r>eps}} s^-3 f_2: " + ", ".join(f"eps={e:g}: {Heps[e]:+.4e}" for e in ks) + f";  local slopes of H(eps) vs eps (-> d-3 if H ~ eps^(d-3)): " + ", ".join(f"{(np.log(abs(Heps[ks[i]])) - np.log(abs(Heps[ks[i+1]])))/(np.log(ks[i]) - np.log(ks[i+1])):+.2f}" for i in range(len(ks)-1)))
    # cubic coefficients from small-r fit of the modes
    bhat = mdl.ang.to_coef(b, 'EE')
    rr = np.logspace(-3.5, -1.5, 40); tt = mdl.rad.t_of_r(rr); Pr = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev)
    bk = (Pr @ bhat).cpu().numpy(); wr = mdl.rad.w_of_t(torch.tensor(tt), mdl.gamma).numpy()
    rho1 = rr*wr*(bk[:,0] - bk[:,1]/2); rho3 = rr*wr*(bk[:,1] - bk[:,2])/2
    c1 = np.polyfit(rr**2, rho1/rr, 3); c3 = np.polyfit(rr**2, rho3/rr, 3)
    s13 = 4*c1[-2]; d13 = 4*c3[-2]; bb = (s13 + 3*d13)/4; ee = (s13 - d13)/4
    rhs = (a0 - 4*A)*bb/(3*a0)
    print(f"{label}: cl={cl:.8f} a0={a0:.6f} A={A:.4f}  b=rho_xxy/2={bb:+.6e} e=rho_yyy/6={ee:+.6e}  H=int s^-3 f_2={H:+.6e}  (a0-4A)b/(3a0)={rhs:+.6e}  T2 defect={H-rhs:+.3e} (rel {abs(H-rhs)/max(abs(H),abs(rhs),1e-300):.2e});  T1 defect e-(a0-2A)b/6={ee-(a0-2*A)*bb/6:+.3e}")
for f in sys.argv[1:]:
    st = torch.load(f)
    mdl = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
    t2(mdl, st['b'].to(dev), st['cl'], f)
# manufactured planted solution: not an exact unforced profile (source S_m), T1/T2 need not hold; printed for reference
