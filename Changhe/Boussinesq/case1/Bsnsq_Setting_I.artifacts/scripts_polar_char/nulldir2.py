"""Reduced beta sensitivity on the SOLVER's own grid, weights and rows (fixes the referee's objection to nulldir.py):
rows = weighted R_Theta, R_Omega (weights 1/max(N, 0.03 S) as in solve_gn), the c-row (w_c = 1e3), the Taylor rows T1/|a0|, T2/|a0|;
J = exact Jacobian (same blocks as solve_gn), column-equilibrated; b = central-difference beta column (basis exponents move with beta).
s_beta = |(I - P_Ran Jg) b| / |b| with Jg = J with the scaling direction projected out (gauge fixed)."""
import sys, math, numpy as np, torch
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *; from evalfields import load_coefs
device = dev()
npz = sys.argv[1]; qmax = float(sys.argv[2]) if len(sys.argv) > 2 else 0.99
P, cT2, cO2, NT, NO, K = load_coefs(npz); beta = P.beta
d = np.load(npz, allow_pickle=True); Nr, Nth = int(d['Nr']), int(d['Nth'])
cT = cT2.reshape(-1).to(device); cO = cO2.reshape(-1).to(device); nT, nO = NT * K, NO * K
j = torch.arange(Nr, dtype=DT, device=device); q = qmax * 0.5 * (1 - torch.cos(math.pi * (j + 0.5) / Nr)); r, _ = torch.sort(P.u_of_q(q) * P.L)
xg, wg = np.polynomial.legendre.leggauss(Nth); th = torch.tensor((xg + 1) * 0.25 * math.pi, dtype=DT, device=device)
grid = Grid(r, th)
sgn = torch.tensor([(-1.0) ** k for k in range(K)], dtype=DT, device=device); dsgn = torch.tensor([(-1.0) ** (k + 1) * k * k * 2.0 for k in range(K)], dtype=DT, device=device)
def centre_vecs(Pb):
    va0 = torch.zeros(nT, dtype=DT, device=device); va0[:K] = sgn / Pb.L
    va02 = torch.zeros(nT, dtype=DT, device=device); va02[:K] = ((Pb.gamma_T - 1) / 2 * sgn + Pb.mu / 2 * dsgn) / Pb.L ** 3
    vb = torch.zeros(nT, dtype=DT, device=device); vb[K:2 * K] = sgn / Pb.L ** 3
    vG2 = torch.zeros(nO, dtype=DT, device=device); vG2[:K] = sgn / Pb.L ** 2
    xq, wq = gl_nodes(256, device); qq = 0.5 * (xq + 1); ww = 0.5 * wq; T2, _ = cheb_T_and_dT(qq, K)
    expo = -(Pb.gamma_O - 4) / Pb.mu - 2.0 / Pb.mu - 1.0
    vM2 = torch.zeros(nO, dtype=DT, device=device); vM2[K:2 * K] = (1.0 / (2 * Pb.L ** 2)) * (2.0 / Pb.mu) * torch.einsum('g,gk->k', ww * (1 - qq) ** expo, T2)
    return va0, va02 + 3 * vb, va02 - vb, vG2, vM2
def rows_and_J(Pb, beta_, wT, wO, a0norm, want_J):
    Mx = field_matrices(Pb, grid, NT, NO, K); Rs = residuals(Mx, grid, cT, cO, beta_)
    va0, vb1, vb2, vG2, vM2 = centre_vecs(Pb)
    a0 = float(va0 @ cT); b1 = float(vb1 @ cT); b2 = float(vb2 @ cT); G2 = float(vG2 @ cO); M2 = float(vM2 @ cO)
    d1 = -G2 / 6 + M2 / 2; d2 = -G2 / 6 - M2 / 2; vd1 = -vG2 / 6 + vM2 / 2; vd2 = -vG2 / 6 - vM2 / 2
    T1 = (2 * beta_ + 4) * b1 + 3 * a0 * d1; T2 = 2 * (beta_ - 2) * b2 + a0 * d2
    rows = torch.cat([wT * Rs['RT'], wO * Rs['RO'], torch.tensor([1e3 * (float(Mx['crow'] @ cO) + 2.0), T1 / a0norm, T2 / a0norm], dtype=DT, device=device)])
    J = None
    if want_J:
        U1, U2 = Rs['U1'][:, None], Rs['U2'][:, None]; x, y = grid.x[:, None], grid.y[:, None]
        JT_T = wT[:, None] * (beta_ * (x * Mx['THx'] + y * Mx['THy']) - (beta_ - 2) * Mx['TH'] + U1 * Mx['THx'] + U2 * Mx['THy'])
        JT_O = wT[:, None] * (Rs['Thx'][:, None] * Mx['U1'] + Rs['Thy'][:, None] * Mx['U2'])
        JO_T = wO[:, None] * (-Mx['THx'])
        JO_O = wO[:, None] * (beta_ * (x * Mx['OMx'] + y * Mx['OMy']) + Mx['OM'] + U1 * Mx['OMx'] + U2 * Mx['OMy'] + Rs['Omx'][:, None] * Mx['U1'] + Rs['Omy'][:, None] * Mx['U2'])
        Jc = torch.cat([torch.zeros(1, nT, dtype=DT, device=device), 1e3 * Mx['crow'][None, :]], 1)
        J1 = torch.cat([(2 * beta_ + 4) * vb1 + 3 * d1 * va0, 3 * a0 * vd1]) / a0norm; J2 = torch.cat([2 * (beta_ - 2) * vb2 + d2 * va0, a0 * vd2]) / a0norm
        J = torch.cat([torch.cat([JT_T, JT_O], 1), torch.cat([JO_T, JO_O], 1), Jc, J1[None, :], J2[None, :]], 0)
    return rows, J, Rs, a0
# weights from the current state (as the solver does at the start of an iteration)
Mx0 = field_matrices(P, grid, NT, NO, K); Rs0 = residuals(Mx0, grid, cT, cO, beta); del Mx0
va0, vb1, vb2, vG2, vM2 = centre_vecs(P); a0 = float(va0 @ cT); g0 = 2 * float(vG2 @ cO) / P.L ** 2
u = grid.R / P.L; E = 1 + u * u
ST = abs(a0) * grid.R * E ** (-1.0 / beta) * (grid.sin + 0.05); SO = abs(g0) * grid.R ** 2 * E ** (-1.0 - 0.5 / beta) * (0.5 * torch.sin(2 * grid.TH) + 0.05)
wT = 1.0 / torch.maximum(Rs0['NT'], 0.03 * ST); wO = 1.0 / torch.maximum(Rs0['NO'], 0.03 * SO)
rows, J, Rs, _ = rows_and_J(P, beta, wT, wO, abs(a0), True)
db = 1e-4
rp, _, _, _ = rows_and_J(Params(beta + db, L=P.L), beta + db, wT, wO, abs(a0), False); rm, _, _, _ = rows_and_J(Params(beta - db, L=P.L), beta - db, wT, wO, abs(a0), False)
b = (rp - rm) / (2 * db)
cn = torch.sqrt((J * J).sum(0)); cn = torch.where(cn > 0, cn, torch.ones_like(cn)); Js = J / cn
# scaling generator in coefficient space (projected on the basis), in scaled coordinates
Mx = field_matrices(P, grid, NT, NO, K)
dTh = Rs['Th'] - (grid.x * Rs['Thx'] + grid.y * Rs['Thy']); dOm = -(grid.x * Rs['Omx'] + grid.y * Rs['Omy'])
vT = torch.linalg.lstsq(Mx['TH'], dTh[:, None]).solution[:, 0]; vO = torch.linalg.lstsq(Mx['OM'], dOm[:, None]).solution[:, 0]
v = torch.cat([vT, vO]) * cn; v = v / v.norm()
print('state: beta %.6f a0 %.4f objective %.4e (rows incl. c, T1, T2)' % (beta, a0, float(rows @ rows)))
print('|J v_scale| (scaled coords) = %.3e ; |b| = %.3e' % (float((Js @ v).norm()), float(b.norm())))
Jg = Js - (Js @ v)[:, None] * v[None, :]
Ug, Sg, Vgh = torch.linalg.svd(Jg, full_matrices=False)
for thr in (1e-8, 1e-10, 1e-12):
    keep = Sg > thr * Sg[0]; Pb = Ug[:, keep] @ (Ug[:, keep].T @ b)
    print('rank threshold %.0e: kept %d of %d; s_beta = |(I-P)b|/|b| = %.3e ; uncompensated |.| = %.3e vs residual norm %.3e' % (thr, int(keep.sum()), Jg.shape[1], float((b - Pb).norm() / b.norm()), float((b - Pb).norm()), float(rows.norm())))
# also: without gauge projection (pure range of J)
Uj, Sj, _ = torch.linalg.svd(Js, full_matrices=False); keep = Sj > 1e-10 * Sj[0]; Pb = Uj[:, keep] @ (Uj[:, keep].T @ b)
print('without gauge projection: s_beta = %.3e' % float((b - Pb).norm() / b.norm()))
