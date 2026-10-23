"""farfield_check.py -- numerical check of the far-field expansion rho = r^p Theta0 + r^(2p-1) Theta1 + O(r^(3p-2)), p = 1/c_l (SPEC v9 (G4),
FINAL_REPORT 3.32), on a saved state.  Theta0 is read off at t = 1; u0 (canonical velocity of r^p Theta0) is computed ANALYTICALLY mode by mode:
with Theta0 = sum_{k odd} T_k sin k th, d_x(r^p Theta0) = r^(p-1) sum_n f_n sin 2n th, f_n = (p - (2n-1)) T_{2n-1}/2 + (p + 2n+1) T_{2n+1}/2,
psi0 = r^(p+1) sum_n P_n sin 2n th, P_n = f_n/((2n+1+p)(2n-1-p)) (the two Green-function integrals of the homogeneous source; no resonance for
0 < p < 1), u0r = -r^p sum 2n P_n cos 2n th, u0th = (p+1) r^p sum P_n sin 2n th, and Theta1 = (p u0r_hat Theta0 + u0th_hat Theta0')/(c_l - 1).
Theta1 from the formula is compared with (rho(r, th) - r^p Theta0(th))/r^(2p-1) evaluated from the state at several large radii (between nodes).
usage: python3 src/farfield_check.py state.pt"""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
S = qdiag.State(sys.argv[1]); p = S.gamma; cl = S.cl
Mq = 128; thq = (np.arange(Mq) + 0.5) * np.pi / (2 * Mq)
T0, T0p, _ = S.theta0(thq)
kmax = 2 * len(S.bk_inf) + 3
ks = np.arange(1, kmax + 1, 2)
Tk = np.array([(2.0 / Mq) * (T0 * np.sin(k * thq)).sum() for k in ks])                     # sin k th coefficients (k odd) of Theta0
def Tof(k): return Tk[(k - 1) // 2] if 1 <= k <= kmax else 0.0
ns = np.arange(1, (kmax + 1) // 2 + 1)
fn = np.array([0.5 * (p - (2 * n - 1)) * Tof(2 * n - 1) + 0.5 * (p + 2 * n + 1) * Tof(2 * n + 1) for n in ns])
Pn = fn / ((2 * ns + 1 + p) * (2 * ns - 1 - p))
def th1(th):
    T0_, T0p_, _ = S.theta0(th)
    u0r = -(2 * ns[None, :] * Pn[None, :] * np.cos(2 * np.outer(th, ns))).sum(1)
    u0th = (p + 1) * (Pn[None, :] * np.sin(2 * np.outer(th, ns))).sum(1)
    return (p * u0r * T0_ + u0th * T0p_) / (cl - 1), u0r, u0th
thc = np.linspace(0.05, np.pi / 2, 64)
T1f, u0r, u0th = th1(thc); T0c, _, _ = S.theta0(thc)
print(f"FARFIELD {sys.argv[1]} c_l={cl} p={p:.6f}: |T_k| of Theta0 = {np.array2string(np.abs(Tk[:6]), precision=4)}; max|Theta1(formula)| = {np.abs(T1f).max():.4g}, "
      f"max|u0r_hat| = {np.abs(u0r).max():.4g}, max|u0th_hat| = {np.abs(u0th).max():.4g}")
# check the canonical velocity of the state against u0 r^p at large r (U should approach r^p u0_hat)
rmax = S.rad.rmap_np(S.rad.tR_np[-1])
for r in [1e2, 1e4, 1e6, 1e8, 1e12, 1e16]:
    if r > rmax / 10: break
    ev = S.ev(np.full_like(thc, r), thc)
    ur = (ev['U1'] * np.cos(thc) + ev['U2'] * np.sin(thc)) / r ** p; uth = (-ev['U1'] * np.sin(thc) + ev['U2'] * np.cos(thc)) / r ** p
    T1n = (ev['rho'] - r ** p * T0c) / r ** (2 * p - 1)
    print(f"  r={r:.0e}: max|U_r/r^p - u0r_hat| = {np.abs(ur - u0r).max():.2e} (|u0r| {np.abs(u0r).max():.3g}), max|U_th/r^p - u0th_hat| = {np.abs(uth - u0th).max():.2e}; "
          f"Theta1_num vs formula: max|diff| = {np.abs(T1n - T1f).max():.2e} (max|Theta1| {np.abs(T1f).max():.3g}; relative {np.abs(T1n - T1f).max()/max(np.abs(T1f).max(),1e-300):.2e}); "
          f"expected next-order size r^(p-1) = {r**(p-1):.1e}")

# Referee's direct extraction of the REPRESENTED second coefficient (referee/fixedcl1/answer.md): for the Q map r = L sqrt((1+t)/2) (1-t)^(-1/(1-p)),
# rho = y (1-t) b/2, expansion at t = 1 gives Theta1_rep = -(1/2) L^(2(1-p)) sin th [ b_t(1, th) + (1-p) b(1, th)/4 ],
# b_t(1, th) = sum_k [beta_k'(1) + (k/2) beta_k(1)] cos 2k th.  Compared with the PDE formula Theta1 (no subtraction at large radii).
if S.rep == 'Q':
    beta_t = (S.rad.DR @ S.coef); bt1 = (S.rad.ext1_R @ beta_t).reshape(-1).cpu().numpy(); b1 = S.bk_inf
    k = np.arange(len(b1)); coef_t = bt1 + 0.5 * k * b1
    bt_th = (coef_t[None, :] * np.cos(2 * np.outer(thc, k))).sum(1); b_th = (b1[None, :] * np.cos(2 * np.outer(thc, k))).sum(1)
    T1rep = -0.5 * S.L ** (2 * (1 - p)) * np.sin(thc) * (bt_th + (1 - p) * b_th / 4)
    print(f"  represented second coefficient (Q basis, t = 1 expansion): max|Theta1_rep - Theta1(PDE)| = {np.abs(T1rep - T1f).max():.3e} "
          f"(max|Theta1| {np.abs(T1f).max():.4g}; relative {np.abs(T1rep - T1f).max()/max(np.abs(T1f).max(),1e-300):.2e})")
