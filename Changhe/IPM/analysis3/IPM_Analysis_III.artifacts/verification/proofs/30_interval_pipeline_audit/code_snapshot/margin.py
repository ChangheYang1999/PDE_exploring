"""Margin certificate for the lead's Theorem R (s2-num; lead note 4 of 02:14Z): rigorous lower bound of
    m(X) = b_0 + (1/2) mu~'(log r) q(X) - b_+(X)   on R^2 \\ {0},   b_0 = 1 + c_l,
    mu~' piecewise constant (lead note 5, 02:18Z): knots 3/2, 7/4, 3, 4, ..., 10; values (in 1/16) 4, 17, 28, 27, 25, 18, 4, -10, -17, -19, -20;
    on each box the hull of the mu~' values on the closed t-interval is used (a box touching a knot carries both values),
    q = V.X/|X|^2 = c_l - sum_n Pe_n(t) cos 2n theta,   b_+ = (|grad rho~| - d_y rho~)/2,
for the exact modal trial, on a cover of the first quadrant (parity: m even in x and y) by boxes [t_a, t_b] x [theta_i, theta_{i+1}]
(the trial's radial cells, the inner/outer sub-cells and the two half-lines, which give the asymptotic regions).
Also: sup |grad rho~| per box (grad rho~ -> 0 at 0 and infinity), sup |D U[rho~]| per box (global Lipschitz bound of V), both outward.
Radial enclosures: f(mid) +/- sup|f'| h/2 on finite cells (exponential polynomials); [-sup|f|, sup|f|] on half-lines, with the exact constant
parts kept (the inner half-line constants of Pe_1, Qe_1 (= c) and of Rhat_0, Rhat_1 (= 1/4) are the degree-0 exponent-0 terms).
Angular enclosures: arb trigonometric functions of the theta interval (balls).   D U: from the polar second derivatives of psi,
   psi = sum_n psi_n sin 2n theta, psi_n = (A_n + B_n)/(4n) (exponential polynomials in t on each cell):
   U_x = -psi_y, U_y = psi_x;  d_x U_x = -psi_xy, d_y U_x = -psi_yy, d_x U_y = psi_xx, d_y U_y = psi_xy; with
   psi_xx = psi_rr c^2 - 2 psi_rth s c / r + psi_th s^2 / r + psi_r s^2 / r + 2 psi_thth ... (standard polar formulas, see code).
Usage: python3 margin.py <tag> ntheta [prec]   (single process)
"""
import sys, os, time, json
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background
from tailbound import sup_bound
from run_section import HERE


def range_on_cell(ep, cl):
    if not ep.terms: return arb(0)
    if cl["kind"] in ("minf", "pinf"):
        # exact constant part (exponent 0, degree 0) plus a symmetric bound for the rest
        const = arb(0); rest = ExpPoly()
        for e, cs in ep.terms.items():
            if e == 0: const += cs[0]; assert all(x == 0 for x in cs[1:])
            else: rest.add(e, cs)
        s0 = sup_bound(rest, cl)[0] if rest.terms else arb(0)
        return const + arb(0, float(s0.upper()) * (1 + 1e-15) + 1e-300)
    h = cl["h"]; v = ep(h / 2); _, sd = sup_bound(ep, cl)
    return v + arb(0, float((sd * h / 2).upper()) * (1 + 1e-15) + 1e-300)


# lead note 5 (02:18Z): piecewise-linear weight mu~ with piecewise-constant mu~' (values in sixteenths on the intervals between the knots)
MU_KNOTS = [fmpq(3, 2), fmpq(7, 4), fmpq(3), fmpq(4), fmpq(5), fmpq(6), fmpq(7), fmpq(8), fmpq(9), fmpq(10)]
MU_VALS = [fmpq(v, 16) for v in (4, 17, 28, 27, 25, 18, 4, -10, -17, -19, -20)]     # on (-oo,3/2), [3/2,7/4), ..., [10, oo)


def mu_prime_values_on(tq_lo, tq_hi):
    """set of mu~' values attained on the CLOSED interval [tq_lo, tq_hi] (both neighbours at a knot), exact rationals; half-lines: tq = None"""
    vals = set()
    for i in range(len(MU_VALS)):
        lo = MU_KNOTS[i - 1] if i >= 1 else None; hi = MU_KNOTS[i] if i < len(MU_KNOTS) else None
        # interval i = [lo, hi) meets the closed [tq_lo, tq_hi] (closure counts: a box touching a knot carries both values)
        if (hi is not None and tq_lo is not None and tq_lo > hi): continue
        if (lo is not None and tq_hi is not None and tq_hi < lo): continue
        vals.add(MU_VALS[i])
    return vals


def mu_prime_range(cl):
    """ball enclosing (the hull of) mu~' on the cell"""
    if cl["kind"] == "minf": vals = mu_prime_values_on(None, cl["tq"])
    elif cl["kind"] == "pinf": vals = mu_prime_values_on(cl["tq"], None)
    else: vals = mu_prime_values_on(cl["tq"], cl["tq"] + cl["hq"])
    lo = min(vals); hi = max(vals)
    mid = q2arb((lo + hi) / 2); rad = q2arb((hi - lo) / 2)
    return mid + arb(0, float(rad.upper()))


def main(tag, ntheta=64, prec=160):
    ctx.prec = prec; t0 = time.time()
    T = ExactTrial(prec=prec); T.build_green(verbose=False)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    bg = Background(T, cells, nmax=None)
    c_l = 1 / T.k; b0 = 1 + c_l; Nf = T.Nf; Mj = T.Mj
    th = [arb.pi() / 2 * i / ntheta for i in range(ntheta + 1)]
    thbox = [(th[i] + th[i + 1]) / 2 + arb(0, float(((th[i + 1] - th[i]) / 2).upper()) * (1 + 1e-15)) for i in range(ntheta)]
    cos2n = [[(2 * n * tb).cos() for n in range(1, Nf + 1)] for tb in thbox]
    sin2n = [[(2 * n * tb).sin() for n in range(1, Nf + 1)] for tb in thbox]
    sinj = [[((2 * j + 1) * tb).sin() for j in range(Mj)] for tb in thbox]
    cosj = [[((2 * j + 1) * tb).cos() for j in range(Mj)] for tb in thbox]
    sinth = [tb.sin() for tb in thbox]; costh = [tb.cos() for tb in thbox]
    nc = cells.n
    M_lo = np.zeros((nc, ntheta)); Q = np.zeros((nc, ntheta, 2)); BP_up = np.zeros((nc, ntheta)); GR_up = np.zeros((nc, ntheta)); DU_up = np.zeros((nc, ntheta)); MU = np.zeros((nc, 2))
    for ic in range(nc):
        cl = cells.cells[ic]; d = bg.get(ic)
        mu = mu_prime_range(cl); MU[ic] = [float(mu.lower()), float(mu.upper())]
        Pe_r = [range_on_cell(d["Pe"][ni], cl) for ni in range(Nf)]
        Qe_r = [range_on_cell(d["Qe"][ni], cl) for ni in range(Nf)]
        # density gradient: rho_r = sum_j [e^{2t} dR_j] sin((2j+1)th), rho_th/r = sum_j (2j+1) [e^{2t} Rhat_j] cos((2j+1)th): exp-polys with exponent shifted by 2
        e2a = (2 * cl["ta"]).exp()
        dR2 = [range_on_cell(d["dR"][j].mul_exp(fmpq(2)).scale(e2a), cl) for j in range(Mj)]
        R2 = [range_on_cell(d["Rhat"][j].mul_exp(fmpq(2)).scale(e2a), cl) for j in range(Mj)]
        # second derivatives of psi for D U: psi_n = (A_n + B_n)/(4n) = e^{2t} Pe_n/(2n);  d_t psi_n = (B-A)/2 = e^{2t} Qe_n;  d_t^2 psi_n from the ExpPoly derivative
        # |D U| <= |psi_rr| + 2|psi_rth|/r + |psi_thth|/r^2 + |psi_r|/r + |psi_th|/r^2 (crude Frobenius-type bound of the polar second-derivative formulas)
        # with  psi_r/r = e^{-2t} d_t psi,  psi_rr = e^{-2t}(d_t^2 psi - d_t psi),  psi_rth/r = e^{-2t} d_t d_th psi,  psi_thth/r^2 = e^{-2t} d_th^2 psi,  psi_th/r^2 = e^{-2t} d_th psi.
        # In modes: e^{-2t} d_t psi_n = Qe_n; e^{-2t} psi_n = Pe_n/(2n); e^{-2t} d_t^2 psi_n = (d/dt)(e^{2t} Qe_n) e^{-2t} = Qe_n' + 2 Qe_n.
        dQe_r = [range_on_cell(d["Qe"][ni].deriv(), cl) for ni in range(Nf)]
        for ib in range(ntheta):
            q = c_l - sum((Pe_r[ni] * cos2n[ib][ni] for ni in range(Nf)), arb(0))
            rr = sum((dR2[j] * sinj[ib][j] for j in range(Mj)), arb(0))
            rt = sum((R2[j] * (2 * j + 1) * cosj[ib][j] for j in range(Mj)), arb(0))
            gr = (rr * rr + rt * rt).sqrt(); dy = rr * sinth[ib] + rt * costh[ib]
            bp = (gr - dy) / 2
            m = b0 + mu * q / 2 - bp
            M_lo[ic, ib] = float(m.lower()); Q[ic, ib] = [float(q.lower()), float(q.upper())]
            BP_up[ic, ib] = float(bp.upper()); GR_up[ic, ib] = float(gr.upper())
            # D U bound
            s_tt = arb(0); s_t = arb(0); s_tth = arb(0); s_thth = arb(0); s_th = arb(0)
            for ni in range(Nf):
                n = ni + 1; S = sin2n[ib][ni]; C = cos2n[ib][ni]
                s_tt += abs((dQe_r[ni] + 2 * Qe_r[ni]) * S); s_t += abs(Qe_r[ni] * S)
                s_tth += abs(Qe_r[ni] * 2 * n * C); s_thth += abs(Pe_r[ni] * 2 * n * S); s_th += abs(Pe_r[ni] * C)
            du = (s_tt + s_t) + 2 * s_tth + s_thth + s_t + s_th
            DU_up[ic, ib] = float(du.upper())
        if ic % 100 == 0: print("cell %d/%d: min m_lo so far %.4f (%.0fs)" % (ic, nc, M_lo[:ic + 1].min(), time.time() - t0), flush=True)
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    np.savez(os.path.join(outdir, "margin.npz"), M_lo=M_lo, Q=Q, BP_up=BP_up, GR_up=GR_up, DU_up=DU_up, MU=MU, theta_edges=np.array([float(x) for x in th]),
             cell_ta=np.array([float(cl["ta"]) for cl in cells.cells]), cell_h=np.array([float(cl["h"]) if cl["h"] is not None else np.nan for cl in cells.cells]), cell_kind=np.array([cl["kind"] for cl in cells.cells]))
    imin = np.unravel_index(np.argmin(M_lo), M_lo.shape)
    res = dict(tag=tag, ntheta=ntheta, prec=prec, inf_m_lower_bound=float(M_lo.min()), argmin_cell=int(imin[0]), argmin_cell_ta=float(cells.cells[imin[0]]["ta"]), argmin_theta_box=int(imin[1]),
               min_over_minf=float(M_lo[0].min()), min_over_pinf=float(M_lo[-1].min()), sup_grad_rho_finite=float(np.nanmax(GR_up)), sup_DU=float(DU_up.max()),
               sup_bplus=float(BP_up.max()), q_range=[float(Q[:, :, 0].min()), float(Q[:, :, 1].max())], mu_range=[float(MU[:, 0].min()), float(MU[:, 1].max())],
               seconds=time.time() - t0, background="exact modal trial modal_v2.json + z", method="box enclosures (see docstring)")
    json.dump(res, open(os.path.join(outdir, "margin.json"), "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    a = sys.argv
    main(a[1], int(a[2]) if len(a) > 2 else 64, int(a[3]) if len(a) > 3 else 160)
