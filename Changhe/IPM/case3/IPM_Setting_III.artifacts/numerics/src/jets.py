"""jets.py -- origin jets and strain/gradient suprema of a Q-representation state (lead 20:08Z).  Q basis: b = sum_k sigma^k beta_k cos 2k th,
w = (1-t)/2 = 1 - sigma, sigma = (1+t)/2 = kappa r^2 (1 + O(r^2)), kappa = 2^(2p)/L^2 (map r = L sqrt(sigma) (1-t)^-p).  With d0 = 2 beta_0'(-1),
d1 = beta_1(-1):  rho = a0 y + b x^2 y + e y^3 + ..., b = kappa (d0 - a0 + d1), e = kappa (d0 - a0 - d1).  psi = r^2 w Psi, Psi = sum_n Psi_n(t) sin 2n th
(PsiC on the Lobatto grid): c = 2 Psi_1(-1), q1 + q2 = 4 kappa (2 Psi_1'(-1) - Psi_1(-1)), q1 - q2 = 16 kappa Psi_2'(-1)
(psi_2 = (c/2) r^2 + ((q1+q2)/4) r^4, psi_4 = ((q1-q2)/8) r^4; the first version had both factors halved, caught by the Poisson check on a forced state).  Checks: Poisson q1 + q2 = -b/3;
exact-profile relations 2 A b + 3 a0 q1 = 0, 2 e + a0 q2 = 0, 6 e - (a0 - 2A) b = 0 (SPEC 4.3, FINAL_REPORT 3.3).  Then on a dense set (log-spaced
r in [1e-4, 1e6], 256 angles + both axes): sup |grad rho|/|a0| with location and n.S n + D there (n = grad rho/|grad rho|, S = sym DU by central
differences), and max_th |S|_op as a function of r (first r where it exceeds D = c_l - 1, and the maximum).  usage: python3 src/jets.py state.pt"""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
S = qdiag.State(sys.argv[1]); q = S.mdl; st = S.st; D = S.cl - 1; A = 2 * S.cl - 1
beta = S.coef; kappa = 2.0 ** (2 * q.p) / S.L ** 2
dbeta = (q.rad.DR @ beta); d0 = 2 * dbeta[0, 0].item(); d1 = beta[0, 1].item(); a0 = beta[0, 0].item()
b = kappa * (d0 - a0 + d1); e = kappa * (d0 - a0 - d1)
PsiC = S.flds['PsiC']; dPsi = q.rad.DL @ PsiC
Psi1, dPsi1, dPsi2 = PsiC[0, 0].item(), dPsi[0, 0].item(), dPsi[0, 1].item()
c = 2 * Psi1; qsum = 4 * kappa * (2 * dPsi1 - Psi1); qdif = 16 * kappa * dPsi2; q1 = (qsum + qdif) / 2; q2 = (qsum - qdif) / 2   # x^3y + xy^3 = r^4 sin2th/2, x^3y - xy^3 = r^4 sin4th/4
print(f"JETS {sys.argv[1]}: c_l={S.cl:.8f} a0={a0:.8f} A={A:.6f} kappa=2^(2p)/L^2={kappa:.6g}; c={c:+.8f} (c_l + c - 1 = {S.cl + c - 1:+.3e})")
print(f"  b = rho_xxy(0)/2 = {b:+.6g}, e = rho_yyy(0)/6 = {e:+.6g}, q1 = {q1:+.6g}, q2 = {q2:+.6g}; signs: a0 b {np.sign(a0*b):+.0f}, a0 e {np.sign(a0*e):+.0f}, q1 {np.sign(q1):+.0f}, q2 {np.sign(q2):+.0f}")
print(f"  defects: Poisson q1 + q2 + b/3 = {q1 + q2 + b/3:+.3e} (relative to |b|/3: {(q1 + q2 + b/3)/max(abs(b)/3,1e-300):+.2e});  2Ab + 3 a0 q1 = {2*A*b + 3*a0*q1:+.3e} (rel {(2*A*b + 3*a0*q1)/max(abs(2*A*b),1e-300):+.2e});  "
      f"2e + a0 q2 = {2*e + a0*q2:+.3e} (rel {(2*e + a0*q2)/max(abs(2*e),1e-300):+.2e});  6e - (a0 - 2A) b = {6*e - (a0 - 2*A)*b:+.3e} (rel {(6*e - (a0-2*A)*b)/max(abs(6*e),1e-300):+.2e}); a0 - 2A = {a0 - 2*A:+.4f}")
# dense set
rr = np.exp(np.linspace(np.log(1e-4), np.log(1e6), 161)); th = np.concatenate([[1e-9], (np.arange(256) + 0.5) * np.pi / 512, [np.pi / 2 - 1e-9]])
RR, TT = np.meshgrid(rr, th, indexing='ij'); out = S.ev(RR, TT); x, y = out['x'], out['y']; h = 1e-5 * RR
ep = S.ev_xy(x + h, y); em = S.ev_xy(x - h, y); fp = S.ev_xy(x, y + h); fm = S.ev_xy(x, y - h)
U1x = (ep['U1'] - em['U1']) / (2 * h); U2x = (ep['U2'] - em['U2']) / (2 * h); U1y = (fp['U1'] - fm['U1']) / (2 * h); U2y = (fp['U2'] - fm['U2']) / (2 * h)
Sa, Sd, Sb = U1x, U2y, 0.5 * (U1y + U2x); Sop = np.abs((Sa + Sd) / 2) + np.sqrt(((Sa - Sd) / 2) ** 2 + Sb ** 2)
G = np.hypot(out['rho_x'], out['rho_y']); iG = np.unravel_index(np.argmax(G), G.shape)
nx, ny = out['rho_x'][iG] / G[iG], out['rho_y'][iG] / G[iG]; nSn = Sa[iG] * nx * nx + 2 * Sb[iG] * nx * ny + Sd[iG] * ny * ny
print(f"  sup|grad rho|/|a0| on the dense set = {G[iG]/abs(a0):.8f} at (r={RR[iG]:.3g}, th={TT[iG]:.4f}); |grad rho(0)| = |a0| analytically; n.S n + D at the sampled maximum = {nSn + D:+.4e} (D = {D:.6f})")
Smax_r = Sop.max(axis=1); iSm = np.argmax(Smax_r); jth = np.argmax(Sop[iSm])
exceed = np.where(Smax_r > D)[0]
print(f"  max_th |S|_op: at r = 1e-4: {Smax_r[0]:.6f} (|c| = {abs(c):.6f}); first sampled r where it exceeds D = {D:.6f}: " + (f"r = {rr[exceed[0]]:.3g} (value {Smax_r[exceed[0]]:.6f}, excess {Smax_r[exceed[0]] - D:+.2e})" if len(exceed) else "never on [1e-4, 1e6]") +
      f"; maximum {Smax_r[iSm]:.6f} at (r={rr[iSm]:.3g}, th={th[jth]:.4f}); sigma - D = {Smax_r[iSm] - D:+.3e}; values at r = 1, 1e2, 1e4, 1e6: {Smax_r[np.searchsorted(rr, 1.0)]:.5f}, {Smax_r[np.searchsorted(rr, 1e2)]:.5f}, {Smax_r[np.searchsorted(rr, 1e4)]:.5f}, {Smax_r[-1]:.5f}")
