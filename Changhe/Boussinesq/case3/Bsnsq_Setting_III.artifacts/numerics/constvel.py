"""constvel.py -- constant far-field velocity C = (0, C2) of a stored state (FINAL_REPORT 4.26(b), lead 00:08Z), 2 < beta < 3.
eta = Omega - omega0 - omega1 (the two leading homogeneous far-field terms r^{-s} a(theta), r^{-2s} b(theta), s = 1/beta
removed); then C2 = -(1/(2 pi)) int (y1/|y|^2) eta(y) dy = -(1/2) int_0^inf eta_1(r) dr, eta_1 the first sine mode
(Omega = sum_k Omega_k(r) sin(k phi), x = r sin phi; only k = 1 contributes), absolutely convergent since eta_1 = O(r^{-3s}) at
infinity (3s > 1) and O(r^{-2s}) at 0 (2s < 1).  A retied candidate (basis exponent b = beta) must have C2 = 0 (4.26(c)).
Representation: Omega_1(r) = r (g_0 - g_2/2), g_k = (1-t)^{b+1} sum_j c_kj B_j(t) (even modes carry no rho_odd factor), z = 1 - t,
r2 map: r = L sqrt(z^{-2b} - 1);  r map: r = L (z^{-b} - 1).  On the last knot interval P(z) = sum_j (c_0j - c_2j/2) B_j(1 - z) is a
polynomial; Omega_1 = L z P(z) (1 + O(z^b)) so the homogeneous terms are A0 r^{-s} with A0 = L^{1+s} P(0) and A1 r^{-2s} with
A1 = L^{1+2s} P'(0).  Evaluation: int_0^R0 Omega_1 dr by the basis quadrature (t < t_last_knot) minus the analytic integrals of the
homogeneous terms over [0, R0]; int_{R0}^inf eta_1 dr by the geometrically refined quadrature of the last interval, with the
analytic integral of the leading terms b L^2 sum_{j>=2} P^(j)(0)/j! z^{j-b} over the innermost cell [0, z_min] (integrand ~ z^{2-b}).
Usage: python3 code/constvel.py state.npz [more.npz ...]"""
import sys, os, math, numpy as np, torch
from numpy.polynomial.legendre import leggauss
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scipy.interpolate import BSpline
from bq3core import Basis, Geometry, DT
from fixedsrc import omega_modes_at


def last_piece_derivs(b, csum):
    """Exact derivatives d^j P/dz^j at z = 0 (t = 1) of the last polynomial piece of the clamped spline sum_j csum_j B_j(t):
    PPoly.from_spline evaluates the last piece at its right endpoint exactly (no 1 - 1e-13 shift; astra fixedsrc1 item 3)."""
    from scipy.interpolate import PPoly
    spl = BSpline(b.knots, csum, b.deg, extrapolate=True)
    pp = PPoly.from_spline(spl, extrapolate=True)
    Pd = [float(pp.derivative(j)(1.0)) * (-1) ** j if j > 0 else float(pp(1.0)) for j in range(b.deg + 1)]
    assert abs(Pd[0] - csum[-1]) < 1e-12 * (1 + abs(csum[-1])), (Pd[0], csum[-1])      # clamped: B_last(1) = 1
    return Pd


def const_velocity(b, g, cG, verbose=False, ng_far=24):
    """Returns dict(C2, A0, A1, I1, hom_int, I2, tail, R0, zmin, P_derivs, defined). C2 is defined (absolutely convergent) only for
    2 < beta_basis < 3; outside that range C2 = nan is returned (the integrals diverge; at beta = 3 the resonance of 4.27 applies)."""
    bb = g.beta; L = g.L; s = 1.0 / bb; K, Nb = b.K, b.Nb
    dev = cG.device
    # number of homogeneous ladder terms r^{-(j+1)s} with (j+1)s < 1 to subtract: J = 2 for 2 < b < 3 (4.26(b)), J = 3 for 3 < b < 4
    # (noninteger-beta analogue, FINAL_REPORT 4.26(d)); integer b is resonant (log terms, 4.27): undefined
    J = 2 if 2.0 < bb < 3.0 else (3 if 3.0 < bb < 4.0 else 0)
    defined = J > 0 and abs(bb - round(bb)) > 1e-9
    csum = (cG[0:Nb] * g.mask_k[0]).cpu().numpy().copy()
    if K > 2:
        csum -= 0.5 * (cG[2 * Nb:3 * Nb] * g.mask_k[2]).cpu().numpy()
    Pd = last_piece_derivs(b, csum)
    pj = [Pd[j] / math.factorial(j) for j in range(b.deg + 1)]                    # P(z) = sum_j pj z^j on the last interval
    A0 = L ** (1 + s) * pj[0]; A1 = L ** (1 + 2 * s) * pj[1]; A2 = L ** (1 + 3 * s) * pj[2]
    Aj = [A0, A1, A2][:J]
    # (i) core: int_0^R0 Omega_1 dr by the basis quadrature (t < t_split), minus the analytic integrals of the homogeneous terms
    tq = b.t_quad; t_split = b.edges[-2]
    tq_t = b.t_quad_t; rq, drq = g.rq, g.drdtq
    Om1 = omega_modes_at(g, cG, tq_t, rq)[0]
    wq_t = b.w_quad_t
    low = torch.tensor(tq < t_split, device=dev)
    I1 = float((wq_t * drq * Om1)[low].sum())
    R0 = float(g.r_of_t(torch.tensor(t_split, dtype=DT, device=dev))[0])
    hom_int = sum(Aj[j] * R0 ** (1 - (j + 1) * s) / (1 - (j + 1) * s) for j in range(J)) if R0 > 0 else 0.0
    # (ii) far: int_{R0}^inf eta_1 dr on the last knot interval, quadrature built DIRECTLY in z = 1 - t (geometric panels from
    # zmin to z_split, Gauss nodes in z, closed-form Jacobian |dr/dz|; astra fixedsrc1 item 4), eta_1 in closed form:
    #   r2 map: eta_1 |dr/dz| = b L^2 z^{-b} [P(z) - p0 (1-w)^{-(1+b)/(2b)} - p1 z (1-w)^{-(2+b)/(2b)}],  w = z^{2b}
    #   r  map: eta_1 |dr/dz| = b L^2 z^{-b} [(1-w) P(z) - p0 (1-w)^{-1/b} - p1 z (1-w)^{-2/b}],          w = z^{b}
    # written with Prem = P - p0 - p1 z and expm1/log1p so that no cancellation occurs on the far cells.
    z_split = 1.0 - t_split
    zmin = 1.0 - b.edges_q[-2]
    # panel edges in z: zmin, 2 zmin, ..., up to z_split (mirror the geometric refinement of edges_q)
    zedges = [zmin]
    while zedges[-1] * 2 < z_split:
        zedges.append(zedges[-1] * 2)
    zedges.append(z_split)
    xg, wg = leggauss(ng_far)
    za = np.array(zedges[:-1]); zb_ = np.array(zedges[1:])
    zq = (0.5 * (zb_ - za)[:, None] * xg[None, :] + 0.5 * (zb_ + za)[:, None]).ravel()
    wz = (0.5 * (zb_ - za)[:, None] * wg[None, :]).ravel()
    zq_t = torch.tensor(zq, dtype=DT, device=dev); wz_t = torch.tensor(wz, dtype=DT, device=dev)
    Pz = sum(pj[j] * zq_t ** j for j in range(b.deg + 1))
    Prem = sum(pj[j] * zq_t ** j for j in range(J, b.deg + 1))
    if g.rmap == 'r2':
        # eta_1 |dr/dz| = b L^2 z^{-b} (1-w)^{-1/2} [sqrt(1-w) P - sum_{j<J} pj z^j (1-w)^{-(j+1)/(2b)}]
        #               = b L^2 z^{-b} [P - sum_{j<J} pj z^j (1-w)^{-(j+1+b)/(2b)}]          (the sqrt cancels against the Jacobian)
        w = zq_t ** (2 * bb); lg = torch.log1p(-w)
        bracket = Prem - sum(pj[j] * zq_t ** j * torch.expm1(-(j + 1 + bb) / (2 * bb) * lg) for j in range(J))
        integrand = bb * L ** 2 * zq_t ** (-bb) * bracket
    else:
        w = zq_t ** bb; lg = torch.log1p(-w)
        bracket = Prem + Pz * torch.expm1(lg) - sum(pj[j] * zq_t ** j * torch.expm1(-(j + 1) * lg / bb) for j in range(J))
        integrand = bb * L ** 2 * zq_t ** (-bb) * bracket
    I2 = float((wz_t * integrand).sum())
    # (iii) innermost cell [0, zmin]: leading asymptotics of the integrand b L^2 sum_{j>=2} pj z^{j-b} (+ O(z^b))
    tail = sum(bb * L ** 2 * pj[j] * zmin ** (j + 1 - bb) / (j + 1 - bb) for j in range(J, b.deg + 1)) if defined else float('nan')
    tail_next_order = bb * L ** 2 * abs(pj[0]) * zmin ** (bb + 1) / (bb + 1)          # size of the omitted O(z^b) term integral (error proxy)
    C2 = -0.5 * (I1 - hom_int + I2 + tail) if defined else float('nan')
    out_res = (bb * L ** 2 / 2 * pj[2] / (3 - bb)) if J == 3 else 0.0
    out = dict(C2=C2, A0=A0, A1=A1, A2=A2, J_subtracted=J, I1=I1, hom_int=hom_int, I2=I2, tail=tail, tail_next_order=tail_next_order, R0=R0, zmin=zmin, v0_R0=0.5 * I1,
               beta_basis=bb, P_derivs=Pd, p_coeffs=pj, defined=defined, n_far_nodes=int(len(zq)),
               resonant_term=(-bb * L ** 2 / 2 * pj[2] / (3 - bb) if J == 3 else 0.0))   # the near-resonant j = 2 CONTRIBUTION to C2 (pole part), b near 3
    if verbose:
        if defined:
            print(f"   beta_basis {bb:.6f}: C2 = {C2:+.10f}  [J = {J} terms subtracted; A0 = {A0:+.6e}, A1 = {A1:+.6e}, A2 = {A2:+.6e}; int_0^R0 Omega_1 = {I1:+.6e}, hom {hom_int:+.6e}, "
                  f"int_R0^inf eta_1 = {I2:+.6e}, tail {tail:+.3e} (omitted next order <= {tail_next_order:.1e}); R0 = {R0:.4g}, zmin = {zmin:.2e}" + (f"; near-resonant j=2 part -(b L^2/2) p2/(3-b) = {-out_res:+.4e}" if J == 3 else "") + "]")
        else:
            print(f"   beta_basis {bb:.6f}: C2 undefined (requires noninteger beta_basis in (2, 4)); A0 = {A0:+.6e}, A1 = {A1:+.6e}, A2 = {A2:+.6e}")
    return out


def load_state(path, dev='cuda'):
    d = np.load(path)
    b = Basis(int(d['Nt']), int(d['deg']), int(d['K']), int(d['Nphi']), ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=float(d['grade']))
    g = Geometry(b, float(d['beta_basis']), float(d['L']), rmap=str(d['rmap']))
    cG = torch.tensor(d['cG'], dtype=DT, device=dev)
    return d, b, g, cG


if __name__ == '__main__':
    torch.set_default_dtype(DT)
    dev = 'cuda' if torch.cuda.is_available() else 'cpu'
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        # exact test (r2 map): g_0 = (1-t)^{b+1} P(1-t) with P a GLOBAL degree-5 polynomial in z = 1 - t (a polynomial lies in every
        # degree-5 spline space, so cG_0 is obtained exactly by least squares on the collocation nodes); then
        # C2 = -(b L^2/2) sum_j p_j/(j+1-b) exactly (astra fixedsrc1 item 4; the Beta-function terms of the analytic continuation of the
        # j = 0, 1 integrals vanish because B(c, -c) = 0 for the r2 exponents). Nt 40 / grade 1.5 as in production; b incl. near 3.
        pj_true = [0.2, -0.3, 0.7, -0.5, 0.4, 0.1]
        for bb in [2.3, 2.6, 2.9, 2.99, 3.005, 3.3, 3.9]:
            b = Basis(40, 5, 4, 8, ng_coll=7, m_reg=2, device=dev, grade=1.5)
            g = Geometry(b, bb, 1.5, rmap='r2')
            tcol = b.t_coll_t; target = sum(pj_true[j] * (1 - tcol) ** j for j in range(6))
            c0 = torch.linalg.lstsq(b.B_coll_t, target[:, None], driver='gels').solution[:, 0]
            cG = torch.zeros(b.K * b.Nb, dtype=DT, device=dev); cG[0:b.Nb] = c0
            fit_err = (b.B_coll_t @ c0 - target).abs().max().item()
            out = const_velocity(b, g, cG, verbose=True)
            exact = -(bb * 1.5 ** 2 / 2) * sum(pj_true[j] / (j + 1 - bb) for j in range(6))
            print(f"      polynomial fit error {fit_err:.1e}; p_j recovered {[round(v, 12) for v in out['p_coeffs']]}; exact C2 {exact:+.12f}; difference {out['C2'] - exact:+.3e} (relative {(out['C2'] - exact) / abs(exact):+.1e})")
        g3 = Geometry(Basis(40, 5, 4, 8, ng_coll=7, m_reg=2, device=dev, grade=1.5), 3.2, 1.5, rmap='r2')
        print('   b = 3.2 ->', const_velocity(g3.b, g3, cG)['C2'])
        sys.exit(0)
    for path in sys.argv[1:]:
        d, b, g, cG = load_state(path, dev)
        print(f"{path}: beta = {float(d['beta']) if 'beta' in d.files else float('nan'):.6f}, beta_basis = {g.beta:.6f}, rmap = {g.rmap}")
        const_velocity(b, g, cG, verbose=True)
