"""Residual-independent exact identities (external review betadet answer, checked against the divergence computation):
 (I)  weighted temperature identity, for 4 - 4/beta < k < 4:  [beta(4-k) - 4] int Theta^2 r^-k = k int Theta^2 (U.X) r^-k-2
      => beta_k = [4 I_k + k J_k] / ((4-k) I_k),   I_k = int Theta^2 r^-k, J_k = int Theta^2 (U.X) r^-(k+2)
 (II) vorticity production, m > 2 beta: (1 - 2 beta/m) int |Omega|^m = int Theta_x Omega |Omega|^(m-2)
      => beta_m = (m/2) (1 - int Theta_x Omega|Omega|^(m-2) / int |Omega|^m)
 (III) critical power m = 2 beta: int Theta_x Omega |Omega|^(2beta-2) = (1/2) int_0^2pi |A(phi)|^(2 beta) dphi, A = lim r^(1/beta) Omega.
Integrals over R^2 by Gauss quadrature in q (radial, mapped) and angle, using the four-fold parity (4 x first quadrant)."""
import sys, math, torch, numpy as np
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *; from evalfields import load_coefs, radial_profiles, fields_at
device = dev()
P, cT, cO, NT, NO, K = load_coefs(sys.argv[1]); beta = P.beta
Nq = int(sys.argv[2]) if len(sys.argv) > 2 else 3000; Nth = int(sys.argv[3]) if len(sys.argv) > 3 else 128
# radial quadrature: Gauss-Legendre in q on [0, qmax], r = u_of_q; dr = (dr/dq) dq
qmax = P.q_of_u(torch.tensor(1e9, dtype=DT)).item()
xg, wg = np.polynomial.legendre.leggauss(Nq); q = torch.tensor(0.5 * (xg + 1) * qmax, dtype=DT, device=device); wq = torch.tensor(0.5 * wg * qmax, dtype=DT, device=device)
r = P.u_of_q(q) * P.L
# dr/dq = L * d/dq sqrt((1-q)^(-2/mu) - 1) = L * (1/mu) (1-q)^(-2/mu-1) / u
u = r / P.L; drdq = P.L * (1.0 / P.mu) * (1 - q) ** (-2.0 / P.mu - 1) / u
xa, wa = np.polynomial.legendre.leggauss(Nth); th = torch.tensor(0.25 * math.pi * (xa + 1), dtype=DT, device=device); wth = torch.tensor(0.25 * math.pi * wa, dtype=DT, device=device)
prof = radial_profiles(P, cT, cO, r, NT, NO, K)
F = fields_at(prof, r, th, beta, NT, NO)
R = r[:, None]; W2d = 4.0 * (wq * r * drdq)[:, None] * wth[None, :]          # area element r dr dphi, four quadrants
def integ(f): return float((f * W2d).sum())
out = {}
UX = F['U1'] * F['X'] + F['U2'] * F['Y']
for k in (2.8, 3.0, 3.2, 3.5):
    if not (4 - 4 / beta < k < 4): continue
    Ik = integ(F['Th'] ** 2 * R ** (-k)); Jk = integ(F['Th'] ** 2 * UX * R ** (-(k + 2)))
    out['beta_from_I_k=%g' % k] = (4 * Ik + k * Jk) / ((4 - k) * Ik)
for m in (8, 10):
    if m <= 2 * beta: continue
    num = integ(F['Thx'] * F['Om'] * F['Om'].abs() ** (m - 2)); den = integ(F['Om'].abs() ** m)
    out['beta_from_II_m=%d' % m] = (m / 2) * (1 - num / den)
# (III): LHS volume integral; RHS from A(phi) = r^(1/beta) Omega at the largest radii
m = 2 * beta
lhs = integ(F['Thx'] * F['Om'] * F['Om'].abs() ** (m - 2))
for rA in (1e6, 1e8):
    i = int((r - rA).abs().argmin()); A = (F['Om'][i] * r[i] ** (1 / beta))
    out['III_lhs'] = lhs; out['III_rhs_A_at_r=%.0e' % rA] = float(0.5 * 4 * (A.abs() ** m * wth).sum())
# convergence check: halve resolution
print('beta =', beta, ' Nq =', Nq, ' Nth =', Nth)
for k_, v in out.items(): print('  %s = %.6f' % (k_, v))
