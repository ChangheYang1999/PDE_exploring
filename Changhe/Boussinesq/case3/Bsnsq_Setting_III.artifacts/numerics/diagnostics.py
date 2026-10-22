"""SPEC sec. 7 diagnostics for a state: centre identities, far-field exponents, v0(R), W.X on circles, stagnation
points of W, sign of Theta. Uses the collocation Geometry on a finer node set (not the fit nodes)."""
import sys, os, json, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, Problem, DT
from evalstate import load_state, basis_from_meta
torch.set_default_dtype(DT)

def main(path, ngc=9, nphimult=2):
    dev = 'cuda'
    cF, cG, meta = load_state(path, dev)
    beta, L = meta['beta'], meta['L']; beta_b = meta.get('beta_basis', beta)
    b = basis_from_meta(meta, dev, ngc=ngc, Nphi=int(meta['Nphi']) * nphimult)
    g = Geometry(b, beta_b, L, rmap=str(meta.get('rmap', 'r'))); p = Problem(g, beta_dyn=beta); f = p.fields(cF, cG)
    out = dict(file=path, beta=beta, c=(g.c_op @ cG).item(), c_target=1 + beta / 2, G0=cG[0].item(), G0_target=4 / beta)
    Nc, Nphi = b.Nc, b.Nphi
    r = g.r.cpu().numpy(); x = g.x.reshape(Nc, Nphi).cpu().numpy(); y = g.y.reshape(Nc, Nphi).cpu().numpy()
    F = f['F'].reshape(Nc, Nphi).cpu().numpy(); G = f['G'].reshape(Nc, Nphi).cpu().numpy()
    Theta = x ** 2 * F; Omega = x * G
    U1 = (g.M_U1 @ cG).reshape(Nc, Nphi).cpu().numpy(); U2 = (g.M_U2 @ cG).reshape(Nc, Nphi).cpu().numpy()
    W1 = beta * x + U1; W2 = beta * y + U2
    # far-field exponents: fit log max_phi|field| vs log r on decades
    def expo(field, lo, hi):
        m = (r >= lo) & (r <= hi)
        v = np.abs(field[m]).max(1); rr = r[m]
        good = v > 0
        return np.polyfit(np.log(rr[good]), np.log(v[good]), 1)[0] if good.sum() > 3 else float('nan')
    out['exponents'] = {}
    for lo, hi in [(10, 100), (100, 1e3), (1e3, 1e4), (1e4, 1e6)]:
        out['exponents'][f'{lo:g}-{hi:g}'] = dict(Theta=expo(Theta, lo, hi), Theta_pred=1 - 2 / beta, Omega=expo(Omega, lo, hi),
                                                 Omega_pred=-1 / beta, U=expo(np.sqrt(U1 ** 2 + U2 ** 2), lo, hi), U_pred=1 - 1 / beta)
    # W.X on circles, min over phi
    WX = (W1 * x + W2 * y) / (beta * r[:, None] ** 2)
    out['WX_over_beta_r2_min_by_radius'] = {f'{r[i]:.3g}': float(WX[i].min()) for i in range(0, Nc, max(1, Nc // 12))}
    # stagnation points: local minima of |W|/(1+r) below a threshold
    Wn = np.sqrt(W1 ** 2 + W2 ** 2) / (1 + r[:, None])
    thr = 0.02
    cand = []
    for i in range(1, Nc - 1):
        for j in range(1, Nphi - 1):
            if Wn[i, j] < thr and Wn[i, j] <= Wn[i-1:i+2, j-1:j+2].min() and r[i] > 0.05:
                cand.append(dict(x=float(x[i, j]), y=float(y[i, j]), Wn=float(Wn[i, j]), W1=float(W1[i, j]), W2=float(W2[i, j])))
    out['stagnation_candidates_off_centre'] = cand[:20]
    # Theta sign
    out['Theta_min'] = float(Theta.min()); out['Theta_max'] = float(Theta.max()); out['Omega_min'] = float(Omega.min()); out['Omega_max'] = float(Omega.max())
    # v0(R): (1/2) int_0^R Omega_1 dr with Omega_1 = r (g_0 - g_2/2) on the quadrature grid
    wq = (b.w_quad_t * g.drdtq).cpu().numpy(); rq = g.rq.cpu().numpy(); Nb = b.Nb
    gq0 = (g.Wq_k[0] @ cG[:Nb]).cpu().numpy() / rq
    gq2 = (g.Wq_k[2] @ cG[2 * Nb:3 * Nb]).cpu().numpy() / rq if b.K > 2 else 0 * gq0
    Om1 = rq * (gq0 - 0.5 * gq2)
    cum = np.cumsum(0.5 * wq * Om1)
    out['v0_R'] = {f'{R:g}': float(cum[np.searchsorted(rq, R)]) for R in [1, 10, 100, 1e3, 1e4, 1e5, 1e6] if R < rq.max()}
    # strain shells (astra fold1): c = -(1/2) int Omega_2(r) dr/r; signed cumulative contributions, tail fraction C_>(R)/c,
    # cancellation measure Cc = int |Omega_2|/(2r) dr / |c|
    Om2 = rq * (0.5 * (g.Wq_k[1] @ cG[Nb:2 * Nb]).cpu().numpy() / rq - (0.5 * (g.Wq_k[3] @ cG[3 * Nb:4 * Nb]).cpu().numpy() / rq if b.K > 3 else 0))
    kap = -0.5 * Om2 / rq
    cum_c = np.cumsum(wq * kap); c_tot = cum_c[-1]
    out['strain_shells'] = dict(c_from_shells=float(c_tot), tail_fraction_C_gt_R_over_c={f'{R:g}': float((c_tot - cum_c[np.searchsorted(rq, R)]) / c_tot) for R in [1, 3, 10, 30, 100, 1e3, 1e4] if R < rq.max()},
                                cancellation_Cc=float(np.sum(wq * np.abs(kap)) / abs(c_tot)),
                                shell_signed={f'{lo:g}-{hi:g}': float(np.sum(wq[(rq >= lo) & (rq < hi)] * kap[(rq >= lo) & (rq < hi)])) for lo, hi in [(0, 1), (1, 3), (3, 10), (10, 100), (100, 1e3), (1e3, 1e5), (1e5, 1e99)]})
    # odd-power-of-r content of each angular mode near the centre: fit f_k(r), g_k(r) on r < rmax to sum_{n=0..5} a_n r^n
    # and report the odd/even coefficient ratios relative to the leading r^k term (smoothness requires f_k = r^k * even(r))
    K, Nb = b.K, b.Nb
    fk = torch.einsum('kia,ka->ki', g.R0kF, cF.reshape(K, Nb)).cpu().numpy(); gk = torch.einsum('kia,ka->ki', g.R0kG, cG.reshape(K, Nb)).cpu().numpy()
    rmax = 0.2 * L
    m = r < rmax
    odd = {}
    for k in range(min(K, 4)):
        for name, arr in [('F', fk), ('G', gk)]:
            co = np.polynomial.polynomial.polyfit(r[m], arr[k][m], 5)
            lead = co[k] if abs(co[k]) > 1e-14 else 1.0
            odd[f'{name}_k{k}'] = dict(coeffs_r0_to_r5=[float(v) for v in co], **{f'ratio_r{k+1}_over_r{k}': float(co[k + 1] / lead) if k + 1 <= 5 else None})
    out['odd_power_content_near_centre'] = odd
    # angular tail convergence (lead note 16:13Z): max_theta | r^{1/beta} Omega(r,.) - r'^{1/beta} Omega(r',.) | for r, r' in {10,100,1000}
    def ang_profile(R):
        i = int(np.argmin(np.abs(r - R)))
        return (r[i] ** (1 / beta)) * Omega[i], r[i]
    tail = {}
    for R1, R2 in [(10, 100), (100, 1000), (1000, 10000)]:
        p1, ra = ang_profile(R1); p2, rb = ang_profile(R2)
        tail[f'{ra:.3g}_vs_{rb:.3g}'] = dict(max_abs_diff=float(np.abs(p1 - p2).max()), max_abs_profile=float(np.abs(p2).max()))
    out['angular_tail_convergence_r1beta_Omega'] = tail
    # axis zeros of b(y) = W_2(0,y) (SPEC sec. 7 item 7; lead note 15:31Z): U_2(0,y) from the modal Psi_k at the radii
    Psi_k = torch.einsum('kia,a->ki', g.Psi_op, cG).cpu().numpy()          # (K, Nc)
    kk = np.arange(1, b.K + 1)[:, None]
    U2_minus = (kk * Psi_k).sum(0) / r                                      # at phi = 0: y = -r
    U2_plus = -(kk * ((-1.0) ** kk) * Psi_k).sum(0) / r                     # at phi = pi: y = +r
    b_minus = beta * (-r) + U2_minus; b_plus = beta * r + U2_plus
    def zeros(yv, bv):
        s = np.sign(bv); ch = np.nonzero(s[1:] != s[:-1])[0]
        return [float(yv[i] - bv[i] * (yv[i + 1] - yv[i]) / (bv[i + 1] - bv[i])) for i in ch]
    out['axis_b_zeros_y_pos'] = zeros(r, b_plus); out['axis_b_zeros_y_neg'] = zeros(-r, b_minus)
    out['axis_b_samples'] = {f'{yv:.3g}': float(bv) for yv, bv in list(zip(r, b_plus))[::max(1, Nc // 10)]}
    out['axis_b_samples_neg'] = {f'{-yv:.3g}': float(bv) for yv, bv in list(zip(r, b_minus))[::max(1, Nc // 10)]}
    # third-order centre defects (SPEC sec. 7 item 7; our derivation, see NOTES_FOR_LEAD sec. 12):
    #   a(y) = F(0,y), q(y) = G(0,y), b(y) = W_2(0,y) = Lam y + h02 y^2 + ..., Lam = beta + c;
    #   D1 = a'(0) - 4 h02 a0 / Lam,   D2 = (2 beta + 1) q'(0) - 2 h02 (q(0) + 4 a0 / Lam)
    fk_ax = fk; gk_ax = gk          # (K, Nc) radial mode functions
    sgn = ((-1.0) ** np.arange(K))[:, None]
    a_plus = (fk_ax * sgn).sum(0); a_minus = fk_ax.sum(0)          # F(0, +r), F(0, -r)
    q_plus = (gk_ax * sgn).sum(0); q_minus = gk_ax.sum(0)
    msm = r < 0.15 * L
    yy = np.concatenate([-r[msm][::-1], r[msm]])
    def fit(vals_minus, vals_plus, deg):
        v = np.concatenate([vals_minus[msm][::-1], vals_plus[msm]])
        return np.polynomial.polynomial.polyfit(yy, v, deg)
    ca = fit(a_minus, a_plus, 4); cq = fit(q_minus, q_plus, 4); cb = fit(b_minus, b_plus, 4)
    Lam = beta + out['c']
    h02 = cb[2]
    out['centre_third_order'] = dict(a0=float(ca[0]), a1=float(ca[1]), q0=float(cq[0]), q1=float(cq[1]), b1=float(cb[1]), Lam_target=Lam,
                                     h02_from_b=float(h02), D1=float(ca[1] - 4 * h02 * ca[0] / Lam),
                                     D2=float((2 * beta + 1) * cq[1] - 2 * h02 * (cq[0] + 4 * ca[0] / Lam)))
    # lead FINAL_REPORT 4.17 identities (beta > 2), half plane x > 0: I1 = int (1+v) P^2 dA = 0,
    # I2: int (1+v) Q^2 dA = int Q (2P + x P_x) dA, with P = F, Q = G, v = U_1/x = -H_y, 2P + x P_x = 2 (F + s F_s).
    wA = ((b.w_coll_t * g.drdt * g.r)[:, None].expand(b.Nc, b.Nphi) * (np.pi / b.Nphi)).reshape(-1)   # area element on the half plane
    onev = 1.0 - f['Hy']
    I1 = (onev * f['F'] ** 2 * wA).sum().item()
    I1_scale = (onev.abs() * f['F'] ** 2 * wA).sum().item()
    I2l = (onev * f['G'] ** 2 * wA).sum().item(); I2r = (f['G'] * 2 * f['F1'] * wA).sum().item()
    out['identities_4_17'] = dict(I1=I1, I1_abs_scale=I1_scale, I1_normalized_defect=abs(I1) / (I1_scale + 1e-300),
                                  I2_lhs=I2l, I2_rhs=I2r, I2_normalized_defect=abs(I2l - I2r) / (abs(I2l) + abs(I2r) + 1e-300),
                                  note='quadrature on the evaluation grid (Gauss in t, midpoint in phi); tails r^{-2-4/beta}, r^{-2-2/beta} are integrated to infinity on the compactified grid')
    # lead 19:40Z axis-tail diagnostic: y^{1+2/beta} Theta_xx(0,y) = 2 y^{1+2/beta} F(0,y) and y^{1+1/beta} Omega_x(0,y) = y^{1+1/beta} G(0,y)
    # on both half-axes for y in [10, 1e4]; angular tail ratio r^{1/beta} Omega/cos(theta) = r^{1+1/beta} G at the nodes nearest the axis.
    sel = [i for i in range(Nc) if 10 <= r[i] <= 1e4][::max(1, Nc // 25)]
    out['axis_tail_scaled'] = {f'{r[i]:.4g}': dict(Txx_up=float(2 * a_plus[i] * r[i] ** (1 + 2 / beta)), Txx_down=float(2 * a_minus[i] * r[i] ** (1 + 2 / beta)),
                                                 Omx_up=float(q_plus[i] * r[i] ** (1 + 1 / beta)), Omx_down=float(q_minus[i] * r[i] ** (1 + 1 / beta))) for i in sel}
    G2 = G; ang = {}
    for R in [100, 1000, 1e4]:
        i = int(np.argmin(np.abs(r - R)))
        ang[f'{r[i]:.4g}'] = dict(up_node=float(r[i] ** (1 + 1 / beta) * G2[i, -1]), down_node=float(r[i] ** (1 + 1 / beta) * G2[i, 0]),
                                  axis_up=float(r[i] ** (1 + 1 / beta) * q_plus[i]), axis_down=float(r[i] ** (1 + 1 / beta) * q_minus[i]))
    out['angular_tail_ratio_near_axis'] = ang
    # core length scale: radius where max_phi G drops to G(0,0)/2
    Gmax = np.abs(G).max(1); G0 = abs(cG[0].item())
    idx = np.nonzero(Gmax < 0.5 * G0)[0]
    out['core_half_radius_G'] = float(r[idx[0]]) if len(idx) else float('nan')
    # DW(0) eigenvalues from c
    out['DW0_eigs'] = [beta - out['c'], beta + out['c']]
    out['DW0_eigs_target'] = [(beta - 2) / 2, 1 + 3 * beta / 2]
    # constant far-field velocity C = (0, C2) (FINAL_REPORT 4.26(b), lead 00:08Z): defined for 2 < beta_basis < 3; a retied
    # candidate (beta_basis = beta) must have C2 = 0 (4.26(c)). Cross-checked with the verifier's packet-93 formula (shift 3).
    try:
        from constvel import const_velocity
        bq = basis_from_meta(meta, dev, ngc=int(meta.get('ngc', 7)), Nphi=int(meta['Nphi']))
        gq = Geometry(bq, beta_b, L, rmap=str(meta.get('rmap', 'r')))
        cv = const_velocity(bq, gq, cG)
        out['const_velocity_C2'] = dict(C2=cv['C2'], A0_omega0_mode1=cv['A0'], A1_omega1_mode1=cv['A1'], defined=bool(2 < beta_b < 3),
                                        retied=bool(abs(beta_b - beta) < 1e-9), note='candidate requires C2 = 0 for 2 < beta < 3 (4.26(c)); meaningful only if retied')
    except Exception as e:
        out['const_velocity_C2'] = dict(error=str(e))
    return out

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--ngc', type=int, default=9); ap.add_argument('--nphimult', type=int, default=2)
    a = ap.parse_args()
    print(json.dumps(main(a.state, a.ngc, a.nphimult), indent=1))
