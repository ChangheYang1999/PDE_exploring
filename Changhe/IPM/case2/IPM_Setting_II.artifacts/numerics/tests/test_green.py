"""Compare the Green-function (product-integration) inverse with the collocation inverse and with exact
manufactured solutions (decaying data, exact psi), and with each other on growing class-S-type data."""
import sys, time; sys.path.insert(0, 'code'); sys.path.insert(0, 'tests')
import numpy as np, torch
from ipm2polar import Disc
from green_inverse import GreenInverse
from test_poisson import make_case, eval_np, taylor_coeffs, x, y, CASES
torch.set_default_dtype(torch.float64)
dev = 'cuda'
for Nr, Nth, R in ((48, 32, 10.0), (64, 32, 10.0), (96, 32, 10.0)):
    d = Disc(Nr, Nth, R, K=2, device=dev)
    t0 = time.time(); G = GreenInverse(d, nq=48); tsetup = time.time() - t0
    th = d.theta_p.cpu().numpy(); r = d.r_np
    TH, RR = np.meshgrid(th, r, indexing="ij"); X, Y = RR*np.cos(TH), RR*np.sin(TH)
    rho_e, psi_e, U1_e, U2_e = make_case(CASES["T4_asym"])
    rho_g = eval_np(rho_e, X, Y); U1_g = eval_np(U1_e, X, Y); U2_g = eval_np(U2_e, X, Y)
    tp = taylor_coeffs(psi_e, 1); U0 = (-tp[(0,1)], tp[(1,0)])
    V1_g, V2_g = U1_g - U0[0], U2_g - U0[1]
    rho_m = d.to_modes(torch.tensor(rho_g, device=dev)); q = rho_m / d.rk
    rho_m2, drho_m, tth_m = d.rho_modes(q); f_m = d.dx_modes(drho_m, tth_m)
    # collocation inverse
    p = d.poisson(f_m, rho_m2, None); psiC, UrC, UtC = d.velocity_modes(p)
    # Green inverse
    psiG, UrG, UtG = G.apply(f_m, rho_m2, None)
    def cart(Ur_m, Ut_m):
        Ur = d.to_phys(Ur_m).cpu().numpy(); Ut = d.to_phys(Ut_m).cpu().numpy()
        return Ur*np.cos(TH) - Ut*np.sin(TH), Ur*np.sin(TH) + Ut*np.cos(TH)
    V1C, V2C = cart(UrC, UtC); V1G, V2G = cart(UrG, UtG)
    nrm = max(np.abs(V1_g).max(), np.abs(V2_g).max())
    eC = max(np.abs(V1C-V1_g).max(), np.abs(V2C-V2_g).max())/nrm
    eG = max(np.abs(V1G-V1_g).max(), np.abs(V2G-V2_g).max())/nrm
    eCG = max(np.abs(V1C-V1G).max(), np.abs(V2C-V2G).max())/nrm
    # psi modes n>=1 compare (collocation psi has modes 0 with p_0(0)=0 convention; Green psi_0 = 0)
    epsi = float((psiC[1:]-psiG[1:]).abs().max() / psiC[1:].abs().max())
    print("T4 decaying Nr=%3d: |V_coll - exact| %.1e  |V_green - exact| %.1e  |V_coll - V_green| %.1e  |psi_C-psi_G| %.1e  (green setup %.1fs)" % (Nr, eC, eG, eCG, epsi, tsetup), flush=True)
# growing class-S-type data: compare the two inverses (no exact solution), several R and tails
print("--- growing data rho = x^2 (1 + 1.5 y/sqrt(1+r^2))^2 (1+r^2)^{(p-2)/2}, p = 0.5 ---")
for Nr, Nth, R in ((48, 32, 100.0), (64, 32, 100.0), (96, 48, 1000.0)):
    d = Disc(Nr, Nth, R, K=2, tail='power2', device=dev)
    G = GreenInverse(d, nq=48)
    th = d.theta_p[:, None]; r = d.r[None, :]
    X, Y = r*torch.cos(th), r*torch.sin(th)
    rho = X**2 * (1 + 1.5*Y/(1+r**2)**0.5)**2 * (1+r**2)**((0.5-2)/2)
    rho_m = d.to_modes(rho); q = rho_m/d.rk
    rho_m2, drho_m, tth_m = d.rho_modes(q); f_m = d.dx_modes(drho_m, tth_m)
    cl = torch.tensor(2.0, device=dev)
    p = d.poisson(f_m, rho_m2, cl); psiC, UrC, UtC = d.velocity_modes(p)
    psiG, UrG, UtG = G.apply(f_m, rho_m2, cl)
    sc = max(float(UrC.abs().max()), float(UtC.abs().max()))
    eU = max(float((UrC-UrG).abs().max()), float((UtC-UtG).abs().max()))/sc
    # relative error per radius region
    dU = torch.sqrt((UrC-UrG).abs()**2 + (UtC-UtG).abs()**2).max(dim=0).values
    U_ = torch.sqrt(UrC.abs()**2 + UtC.abs()**2).max(dim=0).values
    rr = d.r
    def reg(msk): return float((dU[msk]/U_[msk]).max()) if msk.any() else float('nan')
    # strain at the origin from both: psi_xy(0) via taylor_psi needs p; from Green: p2 = psi_2 / r^2 extrapolated
    U0, pxx, pxy, pyy = d.taylor_psi(p)
    pG2 = (psiG[2] / d.rk[2]) @ d.ell0c
    print("Nr=%3d Nth=%2d R=%6g: max|U_C-U_G|/max|U| = %.1e ; relative by region r<1: %.1e, 1<r<10: %.1e, r>10: %.1e | psi_xy0 coll %.6f green %.6f  psi_yy0 coll %.1e green %.1e" %
          (Nr, Nth, R, eU, reg(rr<1), reg((rr>=1)&(rr<10)), reg(rr>=10), float(pxy), float(-4*pG2.imag), float(pyy), float(-4*pG2.real + 0)), flush=True)
