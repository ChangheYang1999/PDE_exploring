"""Margin certificate for the lead's Theorem R (s2-num; lead note 4 of 02:14Z): rigorous lower bound of
    m(X) = b_0 + (1/2) mu~'(log r) q(X) - b_+(X)   on R^2 \\ {0},   b_0 = 1 + c_l,
    mu~' piecewise constant (lead note 5, 02:18Z): knots 3/2, 7/4, 3, 4, ..., 10; values (in 1/16) 4, 17, 28, 27, 25, 18, 4, -10, -17, -19, -20;
    on each box the hull of the mu~' values on the closed t-interval is used (a box touching a knot carries both values),
    q = V.X/|X|^2 = c_l - sum_n Pe_n(t) cos 2n theta,   b_+ = (|grad rho~| - d_y rho~)/2,
for the exact modal trial, on a cover of the first quadrant (parity: m even in x and y) by boxes [t_a, t_b] x [theta_i, theta_{i+1}]
(the trial's radial cells, the inner/outer sub-cells and the two half-lines, which give the asymptotic regions).
Also: sup |grad rho~| per box (grad rho~ -> 0 at 0 and infinity), sup |D U[rho~]| per box (global Lipschitz bound of V), both outward.
Radial enclosures: Taylor enclosure of order 8 with rigorous remainder on finite cells (encl.py; before 04:20Z: f(mid) +/- sup|f'| h/2, far too loose on the spline cells); [-sup|f|, sup|f|] on half-lines, with the exact constant
parts kept (the inner half-line constants of Pe_1, Qe_1 (= c) and of Rhat_0, Rhat_1 (= 1/4) are the degree-0 exponent-0 terms).
Angular enclosures: arb trigonometric functions of the theta interval (balls).   D U: from the polar second derivatives of psi,
   psi = sum_n psi_n sin 2n theta, psi_n = (A_n + B_n)/(4n) (exponential polynomials in t on each cell):
   U_x = -psi_y, U_y = psi_x;  d_x U_x = -psi_xy, d_y U_x = -psi_yy, d_x U_y = psi_xx, d_y U_y = psi_xy; with
   psi_xx = psi_rr c^2 - 2 psi_rth s c / r + psi_th s^2 / r + psi_r s^2 / r + 2 psi_thth ... (standard polar formulas, see code).
Usage: python3 margin.py <tag> ntheta [prec] [cells lo:hi or comma list]   (single process; parts merged by merge_margin.py)
"""
import sys, os, time, json, math
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background
from tailbound import sup_bound
from run_section import HERE
from outward import fup, flo, finite_or_raise
from encl import range_finite


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
    return range_finite(ep, cl)        # 04:20Z: Taylor enclosure with rigorous remainder (encl.py) instead of f(h/2) +/- sup|f'| h/2


# lead note 5 (02:18Z): piecewise-linear weight mu~ with piecewise-constant mu~' (values in sixteenths on the intervals between the knots)
HI_PREC = 512      # working precision on the inner/outer sub-cells and half-lines (V054 near-resonance)
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


def main(tag, ntheta=64, prec=160, cells_sel=None):
    ctx.prec = prec; t0 = time.time()
    T = ExactTrial(prec=prec); T.build_green(verbose=False)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    ctx.prec = HI_PREC; bg = Background(T, cells, nmax=None); ctx.prec = prec     # half-line expansions at high precision (V054)
    c_l = 1 / T.k; b0 = 1 + c_l; Nf = T.Nf; Mj = T.Mj
    th = [arb.pi() / 2 * i / ntheta for i in range(ntheta + 1)]
    thbox = [(th[i] + th[i + 1]) / 2 + arb(0, float(((th[i + 1] - th[i]) / 2).upper()) * (1 + 1e-15)) for i in range(ntheta)]
    cos2n = [[(2 * n * tb).cos() for n in range(1, Nf + 1)] for tb in thbox]
    sin2n = [[(2 * n * tb).sin() for n in range(1, Nf + 1)] for tb in thbox]
    sinj = [[((2 * j + 1) * tb).sin() for j in range(Mj)] for tb in thbox]
    cosj = [[((2 * j + 1) * tb).cos() for j in range(Mj)] for tb in thbox]
    sinth = [tb.sin() for tb in thbox]; costh = [tb.cos() for tb in thbox]
    nc = cells.n
    M_lo = np.full((nc, ntheta), np.nan); Q = np.full((nc, ntheta, 2), np.nan); BP_up = np.full((nc, ntheta), np.nan); GR_up = np.full((nc, ntheta), np.nan); DU_up = np.full((nc, ntheta), np.nan); MU = np.full((nc, 2), np.nan)
    sel = list(range(nc)) if cells_sel is None else cells_sel
    # anisotropic margin of lead note 7 (02:41Z): a = 17/4, mu_a' = -17/2 (t < 0), -5/4 (t >= 0), knot at t = 0 (boxes touching 0 carry both)
    MA_lo = np.full((nc, ntheta), np.nan); TANG = np.full((nc, ntheta, 2), np.nan); A_ANI = arb(17) / 4; N0_EXACT = 8
    # hypothesis (Z) of the lead's note 12 (04:28Z): lower bound of |V|/r per box and enclosures of the four entries of DV = c_l I + DU
    # (DU from the polar second derivatives of psi: d_x U_x = -psi_xy, d_y U_x = -psi_yy, d_x U_y = psi_xx, d_y U_y = psi_xy; formulas in the code)
    VLO = np.full((nc, ntheta), np.nan); DV = np.full((nc, ntheta, 4, 2), np.nan)
    # sin(2n theta)/cos theta = 2 sum_{k=1}^{n} (-1)^{n-k} sin((2k-1) theta) for n <= N0_EXACT (exact identity); |.| <= 2n beyond
    sinodd = [[((2 * k - 1) * tb).sin() for k in range(1, N0_EXACT + 1)] for tb in thbox]
    ratio = [[2 * sum(((-1) ** (n - k) * sinodd[ib][k - 1] for k in range(1, n + 1)), arb(0)) for n in range(1, N0_EXACT + 1)] for ib in range(ntheta)]
    # adaptive angular refinement (04:55Z): a standard box whose lower bound of m or m_a is below REF_THR is split in two (recursively,
    # depth <= REF_DEPTH); the refined minima M_ref, MA_ref (min over the leaves, each a rigorous lower bound on its sub-box) are the certified values.
    REF_THR = 0.5; REF_DEPTH = 4
    M_ref = np.full((nc, ntheta), np.nan); MA_ref = np.full((nc, ntheta), np.nan); NREF = np.zeros((nc, ntheta), dtype=np.int32)
    N0_EXACT_ = N0_EXACT
    def theta_ball(lo, hi):
        return (lo + hi) / 2 + arb(0, fup((hi - lo) / 2))
    for ic in sel:
        cl = cells.cells[ic]
        ctx.prec = HI_PREC if cl["kind"] != "mid" else prec      # near-resonant Green data on the non-mid cells (V054): all arithmetic at 512 bits there
        d = bg.get(ic)
        mu = mu_prime_range(cl); MU[ic] = [flo(mu), fup(mu)]
        Pe_r = [range_on_cell(d["Pe"][ni], cl) for ni in range(Nf)]
        Qe_r = [range_on_cell(d["Qe"][ni], cl) for ni in range(Nf)]
        # density gradient: rho_r = sum_j [e^{2t} dR_j] sin((2j+1)th), rho_th/r = sum_j (2j+1) [e^{2t} Rhat_j] cos((2j+1)th): exp-polys with exponent shifted by 2
        e2a = (2 * cl["ta"]).exp()
        dR2 = [range_on_cell(d["dR"][j].mul_exp(fmpq(2)).scale(e2a), cl) for j in range(Mj)]
        R2 = [range_on_cell(d["Rhat"][j].mul_exp(fmpq(2)).scale(e2a), cl) for j in range(Mj)]
        # second derivatives of psi for D U: psi_n = (A_n + B_n)/(4n) = e^{2t} Pe_n/(2n);  d_t psi_n = (B-A)/2 = e^{2t} Qe_n;  d_t^2 psi_n from the ExpPoly derivative
        # with  psi_r/r = e^{-2t} d_t psi,  psi_rr = e^{-2t}(d_t^2 psi - d_t psi),  psi_rth/r = e^{-2t} d_t d_th psi,  psi_thth/r^2 = e^{-2t} d_th^2 psi,  psi_th/r^2 = e^{-2t} d_th psi.
        # In modes: e^{-2t} d_t psi_n = Qe_n; e^{-2t} psi_n = Pe_n/(2n); e^{-2t} d_t^2 psi_n = (d/dt)(e^{2t} Qe_n) e^{-2t} = Qe_n' + 2 Qe_n.
        dQe_r = [range_on_cell(d["Qe"][ni].deriv(), cl) for ni in range(Nf)]
        # mu_a' hull (anisotropic weight, lead note 7): -17/2 for t < 0, -5/4 for t > 0, both on cells touching 0
        tq = cl["tq"]; hi_q = None if cl["kind"] == "pinf" else (tq + cl["hq"] if cl["kind"] != "minf" else tq)
        if cl["kind"] == "minf": mua_vals = [fmpq(-17, 2)] + ([fmpq(-5, 4)] if tq >= 0 else [])
        elif cl["kind"] == "pinf": mua_vals = [fmpq(-5, 4)] + ([fmpq(-17, 2)] if tq <= 0 else [])
        else: mua_vals = ([fmpq(-17, 2)] if tq < 0 else []) + ([fmpq(-5, 4)] if hi_q > 0 else []) + ([fmpq(-17, 2), fmpq(-5, 4)] if (tq <= 0 <= hi_q) else [])
        lo_ = min(mua_vals); hi_ = max(mua_vals); mua = q2arb((lo_ + hi_) / 2) + arb(0, fup(q2arb((hi_ - lo_) / 2)))

        def eval_box(tb, full=True):
            """all box quantities for the theta ball tb; returns a dict of arb balls (m_lo, q, bp_up, gr_up, ma, tang; and if full: du, vlo, dv)"""
            c2n = [(2 * n * tb).cos() for n in range(1, Nf + 1)]; s2n = [(2 * n * tb).sin() for n in range(1, Nf + 1)]
            sj = [((2 * j + 1) * tb).sin() for j in range(Mj)]; cj = [((2 * j + 1) * tb).cos() for j in range(Mj)]
            s_ = tb.sin(); c_ = tb.cos()
            q = c_l - sum((Pe_r[ni] * c2n[ni] for ni in range(Nf)), arb(0))
            rr = sum((dR2[j] * sj[j] for j in range(Mj)), arb(0))
            rt = sum((R2[j] * (2 * j + 1) * cj[j] for j in range(Mj)), arb(0))
            R_ = arb(rr.abs_upper()); T_ = arb(rt.abs_upper()); gr_up = (R_ * R_ + T_ * T_).sqrt()     # V033: no correlated interval squares
            dy = rr * s_ + rt * c_
            bp_up = (gr_up - arb(dy.lower())) / 2          # b_+ = (|grad rho| - d_y rho)/2 <= (gr_up - dy_lo)/2
            m_lo = b0 + (mu * q / 2) - bp_up               # ball whose lower end bounds m from below
            # anisotropic: tan(theta) V.grad(theta) = sin(theta) sum_n Qe_n sin(2n theta)/cos(theta); exact ratio for n <= N0_EXACT, |.| <= 2n beyond
            sinodd_ = [((2 * k - 1) * tb).sin() for k in range(1, N0_EXACT_ + 1)]
            tang = arb(0)
            for ni in range(Nf):
                n = ni + 1
                fac = 2 * sum(((-1) ** (n - k) * sinodd_[k - 1] for k in range(1, n + 1)), arb(0)) if n <= N0_EXACT_ else arb(0, 2 * n)
                tang += Qe_r[ni] * fac
            tang = tang * s_
            ma = b0 + mua * q / 2 + A_ANI * tang - bp_up
            out = dict(m_lo=m_lo, q=q, bp_up=bp_up, gr_up=gr_up, ma=ma, tang=tang)
            if full:
                s_tt = arb(0); s_t = arb(0); s_tth = arb(0); s_thth = arb(0); s_th = arb(0)
                p_rr = arb(0); p_rt = arb(0); p_tt = arb(0); p_r = arb(0); p_t = arb(0)
                for ni in range(Nf):
                    n = ni + 1; S = s2n[ni]; C = c2n[ni]
                    s_tt += abs((dQe_r[ni] + 2 * Qe_r[ni]) * S); s_t += abs(Qe_r[ni] * S)
                    s_tth += abs(Qe_r[ni] * 2 * n * C); s_thth += abs(Pe_r[ni] * 2 * n * S); s_th += abs(Pe_r[ni] * C)
                    # polar second derivatives (scaled by e^{-2t}): psi_rr = sum (Qe' + Qe) S, psi_rth/r = sum 2n Qe C, psi_thth/r^2 = -sum 2n Pe S, psi_r/r = sum Qe S, psi_th/r^2 = sum Pe C
                    p_rr += (dQe_r[ni] + Qe_r[ni]) * S; p_rt += 2 * n * Qe_r[ni] * C; p_tt += -2 * n * Pe_r[ni] * S; p_r += Qe_r[ni] * S; p_t += Pe_r[ni] * C
                out["du"] = (s_tt + s_t) + 2 * s_tth + s_thth + s_t + s_th
                # (Z): |V|/r >= sqrt(min|q|^2 + min|u_theta|^2), u_theta = V_theta/r = psi_r/r = sum Qe_n sin 2n theta
                def minabs(b): return 0.0 if b.contains(arb(0)) else min(abs(flo(b)), abs(fup(b)))
                mq = minabs(q); mu_ = minabs(p_r)
                out["vlo"] = (arb(mq) * mq + arb(mu_) * mu_).sqrt()
                sc = s_ * c_; c2 = c_ * c_; s2 = s_ * s_
                p_xx = c2 * p_rr - 2 * sc * p_rt + s2 * p_tt + s2 * p_r + 2 * sc * p_t
                p_yy = s2 * p_rr + 2 * sc * p_rt + c2 * p_tt + c2 * p_r - 2 * sc * p_t
                p_xy = sc * p_rr + (c2 - s2) * p_rt - sc * p_tt - sc * p_r - (c2 - s2) * p_t
                out["dv"] = [c_l - p_xy, -p_yy, p_xx, c_l + p_xy]          # DV_xx, DV_xy, DV_yx, DV_yy  (DV = c_l I + DU, U = (-psi_y, psi_x))
            return out

        def refine(lo, hi, depth):
            r = eval_box(theta_ball(lo, hi), full=False)
            ml = flo(r["m_lo"]); al = flo(r["ma"])
            if depth >= REF_DEPTH or (ml >= REF_THR and al >= REF_THR): return ml, al, 1
            mid = (lo + hi) / 2
            a = refine(lo, mid, depth + 1); b = refine(mid, hi, depth + 1)
            return min(a[0], b[0]), min(a[1], b[1]), a[2] + b[2]

        for ib in range(ntheta):
            r = eval_box(thbox[ib])
            M_lo[ic, ib] = finite_or_raise(flo(r["m_lo"]), "m_lo"); Q[ic, ib] = [flo(r["q"]), fup(r["q"])]
            BP_up[ic, ib] = finite_or_raise(fup(r["bp_up"]), "b_+"); GR_up[ic, ib] = finite_or_raise(fup(r["gr_up"]), "grad")
            MA_lo[ic, ib] = finite_or_raise(flo(r["ma"]), "m_a"); TANG[ic, ib] = [flo(r["tang"]), fup(r["tang"])]
            DU_up[ic, ib] = finite_or_raise(fup(r["du"]), "DU")
            VLO[ic, ib] = flo(r["vlo"])
            for jj, e_ in enumerate(r["dv"]): DV[ic, ib, jj] = [flo(e_), fup(e_)]
            if M_lo[ic, ib] < REF_THR or MA_lo[ic, ib] < REF_THR:
                ml, al, nleaves = refine(th[ib], th[ib + 1], 0)
                M_ref[ic, ib] = max(ml, M_lo[ic, ib]); MA_ref[ic, ib] = max(al, MA_lo[ic, ib]); NREF[ic, ib] = nleaves
            else:
                M_ref[ic, ib] = M_lo[ic, ib]; MA_ref[ic, ib] = MA_lo[ic, ib]; NREF[ic, ib] = 1
        if ic % 100 == 0 or (cells_sel is not None and len(cells_sel) <= 20):
            print("cell %d/%d: min m_lo so far %.4f (refined %.4f), min m_a %.4f (refined %.4f), leaves this cell %d (%.0fs)" % (
                ic, nc, np.nanmin(M_lo), np.nanmin(M_ref), np.nanmin(MA_lo), np.nanmin(MA_ref), int(NREF[ic].sum()), time.time() - t0), flush=True)
    ctx.prec = prec
    arrays = dict(M_lo=M_lo, Q=Q, BP_up=BP_up, GR_up=GR_up, DU_up=DU_up, MU=MU, MA_lo=MA_lo, TANG=TANG, VLO=VLO, DV=DV, M_ref=M_ref, MA_ref=MA_ref, NREF=NREF)
    summarize(tag, arrays, cells, ntheta, prec, th, time.time() - t0)


def summarize(tag, arrays, cells, ntheta, prec, th, seconds):
    """write runs/<tag>/margin.npz and margin.json from the per-box arrays (NaN = not computed); used by main and merge_margin.py"""
    M_lo, Q, BP_up, GR_up, DU_up, MU, MA_lo, TANG = (arrays[k] for k in ("M_lo", "Q", "BP_up", "GR_up", "DU_up", "MU", "MA_lo", "TANG"))
    VLO = arrays.get("VLO"); DV = arrays.get("DV"); M_ref = arrays.get("M_ref", M_lo); MA_ref = arrays.get("MA_ref", MA_lo); NREF = arrays.get("NREF")
    nc = cells.n
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    np.savez(os.path.join(outdir, "margin.npz"), M_lo=M_lo, Q=Q, BP_up=BP_up, GR_up=GR_up, DU_up=DU_up, MU=MU, MA_lo=MA_lo, TANG=TANG, VLO=VLO, DV=DV, M_ref=M_ref, MA_ref=MA_ref, NREF=NREF, theta_edges=np.array([float(x) for x in th]),
             cell_ta=np.array([float(cl["ta"]) for cl in cells.cells]), cell_h=np.array([float(cl["h"]) if cl["h"] is not None else np.nan for cl in cells.cells]), cell_kind=np.array([cl["kind"] for cl in cells.cells]))
    imin = np.unravel_index(np.nanargmin(M_ref), M_ref.shape)
    res = dict(tag=tag, ntheta=ntheta, prec=prec, inf_m_lower_bound=float(np.nanmin(M_ref)), inf_m_lower_bound_unrefined=float(np.nanmin(M_lo)),
               refined_boxes=int((NREF > 1).sum()) if NREF is not None else None, refinement_leaves=int(NREF.sum()) if NREF is not None else None,
               negative_boxes_refined=int((M_ref < 0).sum()), cells_computed=int(np.isfinite(M_lo[:, 0]).sum()), cells_total=int(nc), argmin_cell=int(imin[0]), argmin_cell_ta=float(cells.cells[imin[0]]["ta"]), argmin_theta_box=int(imin[1]),
               min_over_minf=float(np.nanmin(M_lo[0])), min_over_pinf=float(np.nanmin(M_lo[-1])), sup_grad_rho_finite=float(np.nanmax(GR_up)), sup_DU=float(np.nanmax(DU_up)),
               sup_bplus=float(np.nanmax(BP_up)), q_range=[float(np.nanmin(Q[:, :, 0])), float(np.nanmax(Q[:, :, 1]))], mu_range=[float(np.nanmin(MU[:, 0])), float(np.nanmax(MU[:, 1]))],
               aniso_inf_ma_lower_bound=(float(np.nanmin(MA_ref)) if np.isfinite(MA_ref).any() else None), aniso_inf_ma_unrefined=(float(np.nanmin(MA_lo)) if np.isfinite(MA_lo).any() else None),
               aniso_nan_boxes_computed_cells=int(np.isnan(MA_lo[np.isfinite(M_lo[:, 0])]).sum()), aniso_negative_boxes_refined=int((MA_ref < 0).sum()),
               aniso_argmin=[int(x) for x in np.unravel_index(np.nanargmin(MA_ref), MA_ref.shape)] if np.isfinite(MA_ref).any() else None,
               tang_range=[float(np.nanmin(TANG[:, :, 0])), float(np.nanmax(TANG[:, :, 1]))],
               seconds=seconds, background="exact modal trial modal_v2.json + z", method="box enclosures (see docstring)")
    # (Z) summary: P = (8.600064, 0) lies in the cell containing t_P = log 8.600064 and the theta box 0; report |V|/r lower bounds
    # excluding that cell's theta-box 0 and its neighbours, and DV on the P box; the inner half-line and the origin side are reported separately
    try:
        tP = math.log(8.600064); icP = max(i for i in range(nc) if float(cells.cells[i]["ta"]) <= tP)
        maskZ = np.isfinite(VLO).copy()
        for i in range(max(0, icP - 1), min(nc, icP + 2)):
            maskZ[i, 0:2] = False
        res["Z"] = dict(P_cell=int(icP), P_cell_ta=float(cells.cells[icP]["ta"]), P_theta_box=0,
                        DV_on_P_box=[[float(x) for x in DV[icP, 0, jj]] for jj in range(4)] if DV is not None else None,
                        DV_labels=["DV_xx", "DV_xy", "DV_yx", "DV_yy"],
                        min_V_over_r_excluding_P_boxes=(float(np.nanmin(np.where(maskZ, VLO, np.nan))) if maskZ.any() else None),
                        argmin=[int(x) for x in np.unravel_index(np.nanargmin(np.where(maskZ, VLO, np.nan)), VLO.shape)] if maskZ.any() else None,
                        min_V_over_r_on_P_cell_boxes=[float(x) for x in VLO[icP, :4]],
                        note="|V|/r lower bound per box; P = (8.600064, 0) (prompt 3.4) sits in theta box 0 of cell P_cell; boxes 0 and 1 of cells P_cell-1..P_cell+1 excluded from the minimum")
    except Exception as ex:
        res["Z"] = dict(error=repr(ex))
    json.dump(res, open(os.path.join(outdir, "margin.json"), "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    a = sys.argv
    sel = None
    if len(a) > 4:
        if ":" in a[4]: lo, hi = a[4].split(":"); sel = list(range(int(lo), int(hi)))
        else: sel = [int(x) for x in a[4].split(",")]
    main(a[1], int(a[2]) if len(a) > 2 else 64, int(a[3]) if len(a) > 3 else 160, sel)
