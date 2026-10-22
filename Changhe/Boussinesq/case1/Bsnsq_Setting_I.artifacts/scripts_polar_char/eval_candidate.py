"""Independent-point evaluation of a candidate: residual tables by region (absolute and normalized),
desingularized residuals with exact axis values, centre quantities, stagnation points, far-field checks."""
import argparse, json, math, os, sys
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from polarlib import *
from evalfields import *

ap = argparse.ArgumentParser()
ap.add_argument('npz')
ap.add_argument('--Nr', type=int, default=1500)
ap.add_argument('--Nth', type=int, default=97)
ap.add_argument('--umax', type=float, default=1e5, help='largest evaluation radius / L')
ap.add_argument('--json', type=str, default=None)
args = ap.parse_args()
device = dev()
P, cT, cO, NT, NO, K = load_coefs(args.npz)
beta = P.beta
# radii: midpoints of a uniform grid in q plus a geometric set near the origin
qmax = P.q_of_u(torch.tensor(args.umax, dtype=DT)).item()
q = (torch.arange(args.Nr, dtype=DT, device=device) + 0.5) / args.Nr * qmax
r = P.u_of_q(q) * P.L
r = torch.cat([torch.logspace(-3, math.log10(float(r[0]) * 0.9), 60, dtype=DT, device=device), r]); r, _ = torch.sort(r)   # r >= 1e-3: desingularized pieces lose < 1e-8 to cancellation
# angles: exact axes, near-axis, and uniform interior
th_in = (torch.arange(args.Nth, dtype=DT, device=device) + 0.5) / args.Nth * (math.pi / 2)
th = torch.cat([torch.tensor([0.0, 1e-4, 1e-3, 1e-2], dtype=DT, device=device), th_in,
                torch.tensor([math.pi / 2 - 1e-2, math.pi / 2 - 1e-3, math.pi / 2 - 1e-4, math.pi / 2], dtype=DT, device=device)])
th, _ = torch.sort(th)
prof = radial_profiles(P, cT, cO, r, NT, NO, K)
F = fields_at(prof, r, th, beta, NT, NO)
Rg = r[:, None].expand(-1, th.shape[0])
res = dict(file=args.npz, beta=beta, L=P.L, NT=NT, NO=NO, K=K, c=prof['c'])
# centre quantities from the radial profiles at tiny r
i0 = 0
res['a0'] = float(prof['f'][0][i0] / r[i0])
res['Omega_xy0'] = float(2 * prof['g'][0][i0] / r[i0] ** 2)
res['Psi_xy0_from_psi1'] = float(2 * prof['psi'][0][i0] / r[i0] ** 2)
# regions
edges = [0, 0.1, 1, 10, 100, 1e3, 1e4, 1e5, 1e7]
interior = ((th > 0) & (th < math.pi / 2))[None, :].expand(Rg.shape[0], -1)
def tab(Rk, Nk, label, colmask=None):
    rows = []
    for a, b in zip(edges[:-1], edges[1:]):
        mask = (Rg >= a * P.L) & (Rg < b * P.L)
        if colmask is not None: mask = mask & colmask
        if mask.sum() == 0: continue
        Rv = F[Rk][mask].abs(); Nv = F[Nk][mask]
        ok = Nv > 0
        rows.append(dict(rlo=a, rhi=b, max_abs=float(Rv.max()), max_norm=float((Rv[ok] / Nv[ok]).max()) if ok.any() else None,
                         frac_N_zero=float((~ok).float().mean())))
    res[label] = rows
tab('RT', 'NT', 'R_Theta', interior); tab('RO', 'NO', 'R_Omega', interior)
tab('RT_y', 'NT_y', 'R_Theta_over_y'); tab('RO_xy', 'NO_xy', 'R_Omega_over_xy')
xax = (th == 0)[None, :].expand(Rg.shape[0], -1); yax = (th == math.pi / 2)[None, :].expand(Rg.shape[0], -1)
tab('RT_y', 'NT_y', 'xaxis_R_Theta_over_y', xax); tab('RO_xy', 'NO_xy', 'xaxis_R_Omega_over_xy', xax)
tab('RT_y', 'NT_y', 'yaxis_R_Theta_over_y', yax); tab('RO_xy', 'NO_xy', 'yaxis_R_Omega_over_xy', yax)
# axis values of desingularized residuals
jx = 0; jy = th.shape[0] - 1
# stagnation points: zeros of W1/x on x-axis and W2/y on y-axis
w1x = F['W1_x'][:, jx].cpu().numpy(); w2y = F['W2_y'][:, jy].cpu().numpy(); rr = r.cpu().numpy()
res['xaxis_W1_over_x_min'] = float(w1x.min()); res['xaxis_W1_over_x_argmin_r'] = float(rr[w1x.argmin()])
res['yaxis_W2_over_y_min'] = float(w2y.min()); res['yaxis_W2_over_y_argmin_r'] = float(rr[w2y.argmin()])
res['xaxis_W1_sign_changes'] = int((np.sign(w1x[1:]) != np.sign(w1x[:-1])).sum())
res['yaxis_W2_sign_changes'] = int((np.sign(w2y[1:]) != np.sign(w2y[:-1])).sum())
# Taylor coefficients at the origin from the radial profiles on small radii (fit in r^2 on 1e-3 < r < 2e-2)
import numpy.polynomial.polynomial as npoly
rr_t = r.cpu().numpy(); msk = (rr_t > 1e-3) & (rr_t < 2e-2)
def fitpoly(vals, powers):
    # least squares fit vals = sum_k coef_k r^powers[k]
    A = np.stack([rr_t[msk] ** pw for pw in powers], 1); return np.linalg.lstsq(A, vals[msk], rcond=None)[0]
f0 = prof['f'][0].cpu().numpy(); f1 = prof['f'][1].cpu().numpy() if NT > 1 else 0 * f0
g1 = prof['g'][0].cpu().numpy(); psi1 = prof['psi'][0].cpu().numpy(); psi2 = prof['psi'][1].cpu().numpy() if NO > 1 else 0 * psi1
a0_, a02 = fitpoly(f0, (1, 3, 5))[:2]; bcoef = fitpoly(f1, (3, 5))[0]
b1 = a02 + 3 * bcoef; b2 = a02 - bcoef                       # Theta = a0 y + b1 x^2 y + b2 y^3 + ...
g00 = 2 * fitpoly(g1, (2, 4))[0]                            # Omega = g00 x y + ...
cfit, p1 = fitpoly(psi1, (2, 4, 6))[:2]; p2 = fitpoly(psi2, (4, 6))[0]
d1 = 2 * p1 + 4 * p2; d2 = 2 * p1 - 4 * p2                   # Psi = c x y + d1 x^3 y + d2 x y^3 + ...
# exact linear functionals of the coefficients (no fitting): a0 = P_0(0)/L, b1 = a02 + 3 b, b2 = a02 - b with
#   a02 = [(gamma_T-1)/2 P_0(0) + mu/2 P_0'(0)]/L^3, b = P_1(0)/L^3 ; g = 2 Q_1(0)/L^2 ; d1 = -G2/6 + M2/2, d2 = -G2/6 - M2/2,
#   G2 = Q_1(0)/L^2, M2 = int_0^inf g_2 s^-3 ds = (1/(2L^2))(2/mu) int_0^1 (1-q)^(-(gamma_O-4)/mu-2/mu-1) T_k dq . Q_2 coefficients
sgnk = np.array([(-1.0) ** k for k in range(K)]); dsgnk = np.array([(-1.0) ** (k + 1) * k * k * 2.0 for k in range(K)])
cTn = cT.cpu().numpy(); cOn = cO.cpu().numpy()
a0_ex = cTn[0] @ sgnk / P.L; a02_ex = ((P.gamma_T - 1) / 2 * (cTn[0] @ sgnk) + P.mu / 2 * (cTn[0] @ dsgnk)) / P.L ** 3
b_ex = (cTn[1] @ sgnk) / P.L ** 3 if NT > 1 else 0.0
b1_ex = a02_ex + 3 * b_ex; b2_ex = a02_ex - b_ex; G2_ex = (cOn[0] @ sgnk) / P.L ** 2; g_ex = 2 * G2_ex
xq_, wq_ = np.polynomial.legendre.leggauss(256); qq_ = 0.5 * (xq_ + 1); ww_ = 0.5 * wq_
Tq_, _ = cheb_T_and_dT(torch.tensor(qq_, dtype=DT), K); Tq_ = Tq_.numpy()
expo_ = -(P.gamma_O - 4) / P.mu - 2.0 / P.mu - 1.0
M2_ex = (1.0 / (2 * P.L ** 2)) * (2.0 / P.mu) * ((ww_ * (1 - qq_) ** expo_) @ Tq_) @ cOn[1] if NO > 1 else 0.0
d1_ex = -G2_ex / 6 + M2_ex / 2; d2_ex = -G2_ex / 6 - M2_ex / 2
res['taylor_exact'] = dict(a0=a0_ex, b1=b1_ex, b2=b2_ex, g=g_ex, d1=d1_ex, d2=d2_ex,
    T1_defect=(2 * beta + 4) * b1_ex + 3 * a0_ex * d1_ex, T2_defect=2 * (beta - 2) * b2_ex + a0_ex * d2_ex, T3_defect=(2 * beta + 1) * g_ex - 2 * b1_ex,
    Poisson_xy_defect=g_ex + 6 * (d1_ex + d2_ex), T1_scale=abs((2 * beta + 4) * b1_ex) + abs(3 * a0_ex * d1_ex), T2_scale=abs(2 * (beta - 2) * b2_ex) + abs(a0_ex * d2_ex), T3_scale=abs((2 * beta + 1) * g_ex) + abs(2 * b1_ex))
# exact far-field limits of the basis: B_n = P_n(1) = sum_k cT[n,k] (Theta ~ r^gamma_T sum B_n sin((2n+1)phi)), A_n = Q_n(1) = sum_k cO[n,k]
res['farfield_exact_limits'] = dict(B=[float(cTn[n].sum()) for n in range(min(NT, 6))], A=[float(cOn[n].sum()) for n in range(min(NO, 6))],
    C=[float(-2 * (np.arange(K) ** 2 * cTn[n]).sum()) for n in range(min(NT, 6))])
res['taylor'] = dict(a0=a0_, b1=b1, b2=b2, g=g00, c_fit=2 * cfit, d1=d1, d2=d2,
                     T1_defect=(2 * beta + 4) * b1 + 3 * a0_ * d1, T2_defect=2 * (beta - 2) * b2 + a0_ * d2,
                     T3_defect=(2 * beta + 1) * g00 - 2 * b1, Poisson_xy_defect=g00 + 6 * (d1 + d2),
                     T1_scale=abs((2 * beta + 4) * b1) + abs(3 * a0_ * d1), T2_scale=abs(2 * (beta - 2) * b2) + abs(a0_ * d2),
                     T3_scale=abs((2 * beta + 1) * g00) + abs(2 * b1))
# next-order centre identities (verifier A5): Theta = a00 y + a10 x^2 y + a01 y^3 + a20 x^4 y + a11 x^2 y^3 + a02 y^5 + ...,
# Omega = g00 xy + g10 x^3 y + g01 x y^3 + ..., Psi = -2xy + h10 x^3 y + h01 x y^3 + ... (h10 = d1, h01 = d2):
#   x^3 y of Omega-eq: (4 beta + 5) g10 + 2 g00 h10 - 4 a20 = 0 ;  x y^3: (4 beta - 3) g01 - 2 g00 h01 - 2 a11 = 0.
# r^5 terms: f_0 = a0 r + a02r r^3 + a04r r^5, f_1 = b r^3 + b5 r^5, f_2 = e r^5 ; with r^5 sin(th) = y r^4 = x^4 y + 2 x^2 y^3 + y^5,
#   r^5 sin(3 th) = r^2 (3 x^2 y - y^3) = 3 x^4 y + 2 x^2 y^3 - y^5, r^5 sin(5 th) = 5 x^4 y - 10 x^2 y^3 + y^5:
#   a20 = a04r + 3 b5 + 5 e ; a11 = 2 a04r + 2 b5 - 10 e ; a02 = a04r - b5 + e.
# Omega r^4 terms: g_1 = G2 r^2 + G4 r^4, g_2 = H4 r^4 ; r^4 sin 2th = 2 x^3 y + 2 x y^3, r^4 sin 4th = 4 x^3 y - 4 x y^3:
#   g10 = 2 G4 + 4 H4 ; g01 = 2 G4 - 4 H4.
a04r = fitpoly(f0, (1, 3, 5, 7))[2]; b5 = fitpoly(f1, (3, 5, 7))[1]
f2 = prof['f'][2].cpu().numpy() if NT > 2 else 0 * f0; e5 = fitpoly(f2, (5, 7))[0]
a20 = a04r + 3 * b5 + 5 * e5; a11 = 2 * a04r + 2 * b5 - 10 * e5
G4 = fitpoly(g1, (2, 4, 6))[1]; g2 = prof['g'][1].cpu().numpy() if NO > 1 else 0 * g1; H4 = fitpoly(g2, (4, 6))[0]
g10 = 2 * G4 + 4 * H4; g01 = 2 * G4 - 4 * H4
res['taylor4'] = dict(a20=a20, a11=a11, g10=g10, g01=g01,
                      T4a_defect=(4 * beta + 5) * g10 + 2 * g00 * d1 - 4 * a20, T4a_scale=abs((4 * beta + 5) * g10) + abs(2 * g00 * d1) + abs(4 * a20),
                      T4b_defect=(4 * beta - 3) * g01 - 2 * g00 * d2 - 2 * a11, T4b_scale=abs((4 * beta - 3) * g01) + abs(2 * g00 * d2) + abs(2 * a11))
# lead relations (SPEC v4 (l6)): b1 = (2beta+1) g/2 ; b2 = g (a0 - 2(beta+2)(2beta+1)) / (12 (beta-2))
res['taylor']['b1_pred_l6'] = (2 * beta + 1) * g00 / 2
res['taylor']['b2_pred_l6'] = g00 * (a0_ - 2 * (beta + 2) * (2 * beta + 1)) / (12 * (beta - 2))
res['taylor']['a0_threshold_l6'] = 2 * (beta + 2) * (2 * beta + 1)
# strain from the inverse with the vorticity truncated at R: c_R = c - J_out(R)/(2 R^2) (J_out(R) = R^2 int_R^inf g_1/s ds)
cR = {}
for Rt in (1e2, 1e3, 1e4, 1e5, 1e6):
    i = int(np.abs(rr - Rt).argmin())
    # J_out(r) = 4 psi_1 - J_in ; psi_1' = (J_out - J_in)/(2r) => J_out = 2 psi_1 + r psi_1'
    Jout = 2 * prof['psi'][0][i].item() + rr[i] * prof['dpsi'][0][i].item()
    cR['%g' % Rt] = prof['c'] - Jout / (2 * rr[i] ** 2)
res['c_truncated_at_R'] = cR
res['g1_r2pow_at_decades'] = decades(prof['g'][0].cpu().numpy() * rr ** (2 / beta)) if False else None
# origin disc: (R_Theta/y - a0 delta)/r^2 with delta = c + 2, normalized by the cubic scale S3 = |2beta+4||b1| + 3|a0||d1| + 2|beta-2||b2| + |a0||d2|
delta_c = prof['c'] + 2.0
S3 = abs(2 * beta + 4) * abs(b1_ex) + 3 * abs(a0_ex) * abs(d1_ex) + 2 * abs(beta - 2) * abs(b2_ex) + abs(a0_ex) * abs(d2_ex)
disc = (Rg < 0.1 * P.L) & (Rg >= 1e-3 * P.L)
red = ((F['RT_y'] - a0_ex * delta_c) / Rg ** 2)
res['origin_disc'] = dict(strain_defect_a0_delta=a0_ex * delta_c, cubic_scale_S3=S3, max_abs_reduced_RT_y_over_r2=float(red[disc].abs().max()),
    max_norm_reduced_RT_y_over_r2=float(red[disc].abs().max() / S3), note='(R_Theta/y - a0 (c+2))/r^2 on 1e-3 <= r < 0.1, all angles incl. axes')
# interior stagnation search: cells of the (r, th) grid where W1 changes sign across theta or r AND W2 changes sign, and min |W|/(beta r)
W1 = F['W1']; W2 = F['W2']; Wn = torch.sqrt(W1 ** 2 + W2 ** 2) / (beta * Rg)
inner_mask = interior & (Rg < 1e6 * P.L)
i_min = torch.nonzero(Wn == Wn[inner_mask].min())[0]
res['interior_min_|W|/(beta r)'] = dict(value=float(Wn[inner_mask].min()), r=float(r[i_min[0]]), deg=float(th[i_min[1]] * 180 / math.pi))
s1 = torch.sign(W1); s2 = torch.sign(W2)
both = ((s1[:-1, :-1] != s1[1:, :-1]) | (s1[:-1, :-1] != s1[:-1, 1:])) & ((s2[:-1, :-1] != s2[1:, :-1]) | (s2[:-1, :-1] != s2[:-1, 1:]))
both = both & interior[:-1, :-1] & interior[1:, 1:]
res['interior_cells_with_both_W_components_changing_sign'] = int(both.sum())
# next-order far-field balance (referee): Theta = r^(1-2/beta) B(phi) + C(phi) r^(1-3/beta) + ..., U = r^(1-1/beta) V + ...:
#   C_n balance: C = p V_r B + V_phi B' with p = 1-2/beta, V_r = -p_psi', V_phi = (2-1/beta) p_psi, p_psi = sum A_n/((2n)^2-(2-1/beta)^2) sin(2n phi)
phi = torch.linspace(0, 2 * math.pi, 721, dtype=DT)[:-1]
Bp = sum(cTn[n].sum() * torch.sin((2 * n + 1) * phi) for n in range(NT)); Bpp = sum(cTn[n].sum() * (2 * n + 1) * torch.cos((2 * n + 1) * phi) for n in range(NT))
Cp = sum(-2 * (np.arange(K) ** 2 * cTn[n]).sum() * torch.sin((2 * n + 1) * phi) for n in range(NT))
qb = 1.0 / beta; pexp = 1 - 2 * qb
ppsi = sum(cOn[n - 1].sum() / ((2 * n) ** 2 - (2 - qb) ** 2) * torch.sin(2 * n * phi) for n in range(1, NO + 1))
dppsi = sum(cOn[n - 1].sum() * 2 * n / ((2 * n) ** 2 - (2 - qb) ** 2) * torch.cos(2 * n * phi) for n in range(1, NO + 1))
Vr = -dppsi; Vphi = (2 - qb) * ppsi
Cpred = pexp * Vr * Bp + Vphi * Bpp
res['farfield_nextorder_balance'] = dict(max_abs_C=float(Cp.abs().max()), max_abs_Cpred=float(Cpred.abs().max()), max_abs_mismatch=float((Cp - Cpred).abs().max()),
    note='C (next-order Theta coefficient of the stored basis, exact) vs p V_r B + V_phi B\' predicted from the exact basis limits B, A')
# near-axis bands (interior points within 10 degrees of an axis)
nearx = ((th > 0) & (th < math.pi / 18))[None, :].expand(Rg.shape[0], -1); neary = ((th > 4 * math.pi / 9) & (th < math.pi / 2))[None, :].expand(Rg.shape[0], -1)
tab('RT', 'NT', 'nearxaxis_R_Theta', nearx); tab('RO', 'NO', 'nearxaxis_R_Omega', nearx)
tab('RT', 'NT', 'nearyaxis_R_Theta', neary); tab('RO', 'NO', 'nearyaxis_R_Omega', neary)
# far field: fitted exponents of f_0 and g_1 between 1e3 L and 1e5 L
def slope(v, lo, hi):
    m = (rr > lo) & (rr < hi)
    if (np.sign(v[m]) != np.sign(v[m][0])).any():
        return None   # sign change inside the window: slope undefined
    lv = np.log(np.abs(v[m])); lr = np.log(rr[m])
    return float(np.polyfit(lr, lv, 1)[0])
def decades(v):
    out = {}
    for dec in (1, 10, 100, 1e3, 1e4, 1e5, 1e6):
        i = int(np.abs(rr - dec).argmin()); out['%g' % dec] = float(v[i])
    return out
res['f0_at_decades'] = decades(prof['f'][0].cpu().numpy()); res['g1_at_decades'] = decades(prof['g'][0].cpu().numpy())
res['psi1_at_decades'] = decades(prof['psi'][0].cpu().numpy())
res['f0_rpow_at_decades'] = decades(prof['f'][0].cpu().numpy() * rr ** (-(1 - 2 / beta)))
res['g1_rpow_at_decades'] = decades(prof['g'][0].cpu().numpy() * rr ** (1 / beta))
res['g1_r2pow_at_decades'] = decades(prof['g'][0].cpu().numpy() * rr ** (2 / beta))
res['farfield_slope_f0_1e3_1e5'] = slope(prof['f'][0].cpu().numpy(), 1e3, 1e5)
res['farfield_slope_g1_1e3_1e5'] = slope(prof['g'][0].cpu().numpy(), 1e3, 1e5)
res['farfield_slope_psi1_1e3_1e5'] = slope(prof['psi'][0].cpu().numpy(), 1e3, 1e5)
res['predicted_slopes'] = dict(f=1 - 2 / beta, g=-1 / beta, psi=2 - 1 / beta)
# velocity sublinearity: max |U|/(beta r) in far field
Umag = torch.sqrt(F['U1'] ** 2 + F['U2'] ** 2)
for a, b in ((1e2, 1e3), (1e3, 1e4), (1e4, 1e5)):
    mask = (Rg >= a) & (Rg < b)
    res[f'max_U_over_beta_r_{a:.0e}_{b:.0e}'] = float((Umag[mask] / (beta * Rg[mask])).max())
print(json.dumps(res, indent=1))
if args.json:
    json.dump(res, open(args.json, 'w'), indent=1)
