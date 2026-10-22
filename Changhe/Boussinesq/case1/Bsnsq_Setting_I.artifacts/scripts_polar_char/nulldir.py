"""Is the smallest singular direction of the (weighted, column-scaled) Jacobian the scaling generator?
Scaling: Theta_l = l Theta(X/l): d/dl at l=1 gives dTheta = Theta - X.grad Theta, dOmega = -X.grad Omega.
Project these fields onto the basis (least squares on the grid) to get the coefficient direction v_scale, and report
cosines with the right singular vectors of the smallest singular values."""
import sys, math, json, numpy as np, torch
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *; from evalfields import load_coefs
P, cT, cO, NT, NO, K = load_coefs(sys.argv[1]); beta = P.beta; device = dev()
cT = cT.reshape(-1).to(device); cO = cO.reshape(-1).to(device)
Nr, Nth, qmax = 300, 48, 0.99
j = torch.arange(Nr, dtype=DT, device=device); q = qmax * 0.5 * (1 - torch.cos(math.pi * (j + 0.5) / Nr)); r, _ = torch.sort(P.u_of_q(q) * P.L)
xg, wg = np.polynomial.legendre.leggauss(Nth); th = torch.tensor((xg + 1) * 0.25 * math.pi, dtype=DT, device=device)
grid = Grid(r, th); Mx = field_matrices(P, grid, NT, NO, K)
Rs = residuals(Mx, grid, cT, cO, beta)
x, y = grid.x[:, None], grid.y[:, None]; U1, U2 = Rs['U1'][:, None], Rs['U2'][:, None]
JT_T = beta * (x * Mx['THx'] + y * Mx['THy']) - (beta - 2) * Mx['TH'] + U1 * Mx['THx'] + U2 * Mx['THy']
JT_O = Rs['Thx'][:, None] * Mx['U1'] + Rs['Thy'][:, None] * Mx['U2']
JO_T = -Mx['THx']
JO_O = beta * (x * Mx['OMx'] + y * Mx['OMy']) + Mx['OM'] + U1 * Mx['OMx'] + U2 * Mx['OMy'] + Rs['Omx'][:, None] * Mx['U1'] + Rs['Omy'][:, None] * Mx['U2']
u = grid.R / P.L; E = 1 + u * u
ST = Rs['NT'].clamp(min=1e-12); SO = Rs['NO'].clamp(min=1e-12)
wT = 1 / torch.maximum(Rs['NT'], 0.03 * abs(float(cT[0])) * grid.R * E ** (-1 / beta) * (grid.sin + 0.05))
wO = 1 / torch.maximum(Rs['NO'], 0.03 * max(abs(float(Rs['Om'].abs().max())), 1e-12) * grid.R ** 2 * E ** (-1 - 0.5 / beta) * (0.5 * torch.sin(2 * grid.TH) + 0.05))
J = torch.cat([torch.cat([wT[:, None] * JT_T, wT[:, None] * JT_O], 1), torch.cat([wO[:, None] * JO_T, wO[:, None] * JO_O], 1)], 0)
cn = torch.sqrt((J * J).sum(0)); J = J / cn
U_, S, Vh = torch.linalg.svd(J, full_matrices=False)
# scaling generator in coefficient space
dTh = Rs['Th'] - (grid.x * Rs['Thx'] + grid.y * Rs['Thy']); dOm = -(grid.x * Rs['Omx'] + grid.y * Rs['Omy'])
vT = torch.linalg.lstsq(Mx['TH'], dTh[:, None]).solution[:, 0]; vO = torch.linalg.lstsq(Mx['OM'], dOm[:, None]).solution[:, 0]
fitT = float(((Mx['TH'] @ vT - dTh).norm() / dTh.norm())); fitO = float(((Mx['OM'] @ vO - dOm).norm() / dOm.norm()))
v = torch.cat([vT, vO]) * cn           # in column-scaled coordinates
v = v / v.norm()
cos = (Vh @ v).abs()
print('scaling generator representable in basis: rel. projection error Theta %.2e, Omega %.2e' % (fitT, fitO))
print('singular values (smallest 8 / largest):', [float(s) for s in S[-8:]], float(S[0]))
print('|cos| of scaling direction with the right singular vectors of the 8 smallest sigmas:', [round(float(c), 4) for c in cos[-8:]])
print('|J v_scale| / |J| for the scaling direction: %.3e (sigma_min = %.3e)' % (float((J @ v).norm()), float(S[-1])))
top = torch.topk(cos, 5)
print('largest |cos| overall: values', [round(float(c), 4) for c in top.values], 'at singular values', [float(S[i]) for i in top.indices])

# ---- reduced beta sensitivity (external review betadet): s_beta = |(I - P_Ran J) b| / |b| with b the beta column (basis exponents move with beta),
#      after removing the scaling direction from the admissible profile changes (gauge fixed).
def rows_at(beta_, Pb):
    Mxb = field_matrices(Pb, grid, NT, NO, K)
    Rsb = residuals(Mxb, grid, cT, cO, beta_)
    return torch.cat([wT * Rsb['RT'], wO * Rsb['RO']])
db = 1e-4
b = (rows_at(beta + db, Params(beta + db, L=P.L)) - rows_at(beta - db, Params(beta - db, L=P.L))) / (2 * db)
# project out the scaling direction from J's column space: J_g = J restricted to the complement of v (column-scaled coordinates)
vhat = v / v.norm()
Jg = J - (J @ vhat)[:, None] * vhat[None, :]          # columns orthogonal to the scaling direction
Ug, Sg, Vgh = torch.linalg.svd(Jg, full_matrices=False)
keep = Sg > 1e-10 * Sg[0]
Pb = Ug[:, keep] @ (Ug[:, keep].T @ b)
s_beta = float((b - Pb).norm() / b.norm())
print('reduced beta sensitivity s_beta = |(I-P)b|/|b| = %.3e  (|b| = %.3e, rank kept %d of %d; 1 = fully determined, 0 = undetermined)' % (s_beta, float(b.norm()), int(keep.sum()), Jg.shape[1]))
# where does the unexplained beta-residual live?  by radial decade
resid = (b - Pb)
nrow = grid.N * grid.M
rT = resid[:nrow].reshape(grid.N, grid.M); rO = resid[nrow:2 * nrow].reshape(grid.N, grid.M)
for lo in (1e-2, 1e-1, 1, 10, 100, 1e3, 1e4, 1e5):
    m = (grid.r >= lo) & (grid.r < 10 * lo)
    if m.any(): print('   r in [%g, %g): |unexplained beta-residual| Theta rows %.3e  Omega rows %.3e' % (lo, 10 * lo, float(rT[m].norm()), float(rO[m].norm())))
