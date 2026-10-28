"""Box enclosures for the lead's Theorem C' hypotheses (S2_L2_THEORY.md 5.2; lead notes 10 and 11), exact modal trial rho~ (s2-num).

Quantities (V = c_l X + U[rho~], polar modes of the background on each radial cell, exponential polynomials in sigma = t - t_a):
   U_r/r = -sum_n Pe_n(t) cos 2n theta,     U_theta/r = sum_n Qe_n(t) sin 2n theta,     q := V.X/r^2 = c_l + U_r/r.
 (A)  axis data  d(t) := V_2(0, e^t)/e^t = q(theta = pi/2) = c_l - sum_n (-1)^n Pe_n(t),  and d'(t);  D = 4 c_l - 1, c = 3 c_l - 1 = D - c_l.
      Reported per radial cell: enclosure of d and d'; sup |d - D| e^{-2t} and sup |d'| e^{-2t} on cells with t <= 0 (inner half-line
      included, where the exponent-0 constant of d - D is dropped as an exact cancellation, see below); sup |d - c_l| e^{(1-k)t} and
      sup |d'| e^{(1-k)t} on cells with t >= 0 (outer half-line included).
 (CB) p := 2 V_1/x + V_2/y - 1 = c + 3 U_r/r - 2 tan(theta) U_theta/r + cot(theta) U_theta/r.   On the axis p_axis = D - d - 2 d'.
      With u = pi/2 - theta, s = sin theta, U_m the Chebyshev polynomials of the second kind (U_{-1} = 0, U_0 = 1), exact identities:
        cos 2n theta - (-1)^n = -2 (-1)^n cos^2(theta) U_{n-1}(s)^2,
        tan(theta) sin 2n theta - (-1)^{n+1} 2n = cos^2(theta) g_n,   g_n := 2 (-1)^n sum_{k=1}^n [U_{k-2}(s)^2 + U_{k-1}(s)^2],
        cot(theta) sin 2n theta = cos^2(theta) 2 U_{n-1}(cos 2 theta),
      hence   a_1 := (q - d)/cos^2 theta = 2 sum_n (-1)^n Pe_n U_{n-1}(s)^2,
              a_0 := (p - p_axis)/cos^2 theta = 6 sum_n (-1)^n Pe_n U_{n-1}(s)^2 - 2 sum_n Qe_n g_n + 2 sum_n Qe_n U_{n-1}(cos 2 theta).
      The n = 1 part of a_0 is exactly 6 (Qe_1 - Pe_1) (U_0 = 1, g_1 = -2), computed as one exponential polynomial so that the
      origin constants cancel exactly.  Tails n > N0 use |U_{n-1}(s)| <= min(n, 1/min cos theta), |g_n| <= (4n^3 + 2n)/3 (or the
      min-form), |U_{n-1}(cos 2 theta)| <= min(n, 1/min |sin 2 theta|).   M_Q = sup |a_1|,  M_P = sup min(r^2, 1)^{-1} |a_0|.
 kappa_w for w_a = |cos theta|^{-2a} e^{mu_a(log r)}, a = 17/4, mu_a' = -17/2 (t < 0), -5/4 (t > 0), both at t = 0:
      kappa_w = b_0 + (mu_a'/2) q + a tan(theta) V.grad(theta),  tan(theta) V.grad(theta) = sin(theta) sum_n Qe_n sin(2n theta)/cos(theta),
      sin(2n theta)/cos(theta) = 2 sum_{k=1}^n (-1)^{n-k} sin((2k-1) theta) (exact, n <= N0), |.| <= min(2n, 1/min cos theta) beyond.
      kappa_* = ess inf kappa_w (lower bound), sup kappa_w (upper bound).
 Consistency check (Green data): n Qe_n = Pe_n + Pe_n'/2 on every cell and mode (sup of the difference reported).
Exact cancellations (dropped exponent-0 constants on the inner half-line, each asserted to be a ball containing 0 of radius < 1e-30):
   d - D -> 0 (exact normalization c[rho~] = 3 c_l - 1 of the repaired trial, V005);  6 (Qe_1 - Pe_1) = -6 e^{-2t} A_1 has no constant term.
Radial enclosures: f(h/2) +/- sup|f'| h/2 on finite cells; exact constant + symmetric sup bound of the rest on half-lines (tailbound.sup_bound).
Angular enclosures: arb balls of the theta boxes.  Final floats outward (outward.py).
Usage: python3 hypA.py <tag> ntheta [prec] [cells: comma list, for tests]     (single process)
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

N0 = 12            # exact angular identities up to this mode; bounds beyond
TINY = 1e-30       # maximal radius of a dropped exact-zero constant
DROPPED = []       # (cell, what, mid, rad) of every dropped constant


def split_const(ep):
    const = arb(0); rest = ExpPoly()
    for e, cs in ep.terms.items():
        if e == 0:
            assert all(x == 0 for x in cs[1:]), "polynomial constant term"
            const += cs[0]
        else: rest.add(e, cs)
    return const, rest


def range_on_cell(ep, cl):
    """arb ball enclosing the range of ep on the cell"""
    if not ep.terms: return arb(0)
    if cl["kind"] in ("minf", "pinf"):
        const, rest = split_const(ep)
        s0 = sup_bound(rest, cl)[0] if rest.terms else arb(0)
        return const + ball_rad(s0)
    return range_finite(ep, cl)          # Taylor enclosure with rigorous remainder (encl.py)


def ball_rad(x):
    """ball [-u, u] with u a float >= the exact upper end of the arb x (directed)"""
    return arb(0, fup(x))


def sup_abs(ep, cl):
    """arb upper bound of sup |ep| on the cell (half-lines: constants exact, rest by sup_bound; finite: range ball)"""
    if not ep.terms: return arb(0)
    if cl["kind"] in ("minf", "pinf"):
        return sup_bound(ep, cl)[0]
    r = range_on_cell(ep, cl); return arb(r.abs_upper())


def drop_const(ep, ic, what):
    """remove the exponent-0 constant of ep after checking that it is an exact-zero artifact (ball containing 0, radius < TINY)"""
    const, rest = split_const(ep)
    if not const.is_zero():
        ok = const.contains(arb(0)) and float(const.rad()) < TINY
        if not ok: raise ValueError("constant of %s on cell %d is not an exact zero: %s" % (what, ic, const.str(10)))
        DROPPED.append((ic, what, float(const.mid()), float(const.rad())))
    return rest


def const_ep(x):
    return ExpPoly([(fmpq(0), [arb(x)])])


def weighted(ep, beta_q, ta):
    """ep(sigma) e^{beta t} = e^{beta t_a} e^{beta sigma} ep(sigma) as an ExpPoly in sigma"""
    return ep.mul_exp(beta_q).scale((q2arb(beta_q) * ta).exp())


def main(tag, ntheta=64, prec=160, cells_sel=None):
    ctx.prec = prec; t0 = time.time()
    T = ExactTrial(prec=prec); T.build_green(verbose=False)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    bg = Background(T, cells, nmax=None)
    k_q = T.k_q; c_l = 1 / T.k; D = 4 * c_l - 1; c = 3 * c_l - 1; b0 = 1 + c_l; Nf = T.Nf; A_ANI = arb(17) / 4
    one_minus_k = fmpq(1) - k_q
    th = [arb.pi() / 2 * i / ntheta for i in range(ntheta + 1)]
    thbox = [(th[i] + th[i + 1]) / 2 + arb(0, float(((th[i + 1] - th[i]) / 2).upper()) * (1 + 1e-15)) for i in range(ntheta)]
    # angular data per box
    cos2n = [[(2 * n * tb).cos() for n in range(1, Nf + 1)] for tb in thbox]
    sinth = [tb.sin() for tb in thbox]
    cmin = [arb(th[i + 1].cos().lower()) for i in range(ntheta)]            # lower bound of cos theta on box i (cos decreasing)
    # (sin 2 theta is unimodal on [0, pi/2]: its minimum on a box is at an end, also for the box containing pi/4)
    s2min = [arb(min((2 * th[i]).sin().lower(), (2 * th[i + 1]).sin().lower())) for i in range(ntheta)]
    def inv_or(x, cap):
        """min(cap, 1/x) as a float upper bound (x a lower bound >= 0)"""
        xl = float(x.lower())
        return cap if xl <= 0 else min(cap, 1.0 / xl * (1 + 1e-12))
    U2s = []; GN = []; UC2 = []; RATIO = []
    for ib in range(ntheta):
        s = sinth[ib]; c2 = (2 * thbox[ib]).cos()
        Us = [arb(1), 2 * s]; Uc = [arb(1), 2 * c2]
        for m in range(2, N0 + 1):
            Us.append(2 * s * Us[-1] - Us[-2]); Uc.append(2 * c2 * Uc[-1] - Uc[-2])
        u2 = [Us[n - 1] * Us[n - 1] for n in range(1, N0 + 1)]               # U_{n-1}(s)^2, n = 1..N0
        gn = []; acc = arb(0)
        for n in range(1, N0 + 1):
            acc += (Us[n - 2] * Us[n - 2] if n >= 2 else arb(0)) + Us[n - 1] * Us[n - 1]
            gn.append(2 * (-1) ** n * acc)
        uc2 = [Uc[n - 1] for n in range(1, N0 + 1)]                           # U_{n-1}(cos 2 theta)
        sinodd = [((2 * kk - 1) * thbox[ib]).sin() for kk in range(1, N0 + 1)]
        ratio = [2 * sum(((-1) ** (n - kk) * sinodd[kk - 1] for kk in range(1, n + 1)), arb(0)) for n in range(1, N0 + 1)]
        U2s.append(u2); GN.append(gn); UC2.append(uc2); RATIO.append(ratio)
    nc = cells.n
    sel = list(range(nc)) if cells_sel is None else cells_sel
    # per-cell outputs
    Dlo = np.full(nc, np.nan); Dhi = np.full(nc, np.nan); DPlo = np.full(nc, np.nan); DPhi = np.full(nc, np.nan)
    DD2 = np.full(nc, np.nan); DP2 = np.full(nc, np.nan); DCK = np.full(nc, np.nan); DPK = np.full(nc, np.nan); IDCHK = np.full(nc, np.nan)
    # per-box outputs
    A1 = np.full((nc, ntheta), np.nan); A0 = np.full((nc, ntheta), np.nan); A0W = np.full((nc, ntheta), np.nan)
    KWlo = np.full((nc, ntheta), np.nan); KWhi = np.full((nc, ntheta), np.nan); Qlo = np.full((nc, ntheta), np.nan); Qhi = np.full((nc, ntheta), np.nan)
    for ic in sel:
        cl = cells.cells[ic]; d = bg.get(ic); kind = cl["kind"]; ta = cl["ta"]
        Pe = d["Pe"]; Qe = d["Qe"]
        # ---- axis data
        dEP = ExpPoly()
        for n in range(1, Nf + 1): dEP = dEP + Pe[n - 1].scale(arb((-1) ** (n + 1)))          # d - c_l
        dpEP = dEP.deriv()
        dr = c_l + range_on_cell(dEP, cl); dpr = range_on_cell(dpEP, cl)
        Dlo[ic] = flo(dr); Dhi[ic] = fup(dr); DPlo[ic] = flo(dpr); DPhi[ic] = fup(dpr)
        # identity check n Qe_n = Pe_n + Pe_n'/2
        idm = 0.0
        for n in range(1, Nf + 1):
            diff = Qe[n - 1].scale(arb(n)) - Pe[n - 1] - Pe[n - 1].deriv().scale(arb(1) / 2)
            idm = max(idm, fup(sup_abs(diff, cl)))
        IDCHK[ic] = idm
        t_lo = cl["tq"]; t_hi = None if kind == "pinf" else (cl["tq"] if kind == "minf" else cl["tq"] + cl["hq"])
        left_region = (kind == "minf") or (t_lo <= 0)                 # cell meets t <= 0
        right_region = (kind == "pinf") or (t_hi is None) or (t_hi >= 0)   # cell meets t >= 0
        if kind != "pinf" and left_region:
            try:
                dD = dEP + const_ep(c_l - D)                                # d - D
                if kind == "minf": dD = drop_const(dD, ic, "d - D")
                DD2[ic] = finite_or_raise(fup(sup_abs(weighted(dD, fmpq(-2), ta), cl)), "DD2")
                DP2[ic] = finite_or_raise(fup(sup_abs(weighted(dpEP, fmpq(-2), ta), cl)), "DP2")
            except (AssertionError, ValueError) as ex:
                print("cell %d: left asymptotic bound failed: %r" % (ic, ex), flush=True); DD2[ic] = np.inf; DP2[ic] = np.inf
        if kind != "minf" and right_region:
            try:
                DCK[ic] = finite_or_raise(fup(sup_abs(weighted(dEP, one_minus_k, ta), cl)), "DCK")
                DPK[ic] = finite_or_raise(fup(sup_abs(weighted(dpEP, one_minus_k, ta), cl)), "DPK")
            except (AssertionError, ValueError) as ex:
                print("cell %d: right asymptotic bound failed: %r" % (ic, ex), flush=True); DCK[ic] = np.inf; DPK[ic] = np.inf
        # ---- box quantities
        Pe_r = [range_on_cell(Pe[n - 1], cl) for n in range(1, Nf + 1)]
        Qe_r = [range_on_cell(Qe[n - 1], cl) for n in range(1, Nf + 1)]
        E1 = (Qe[0] - Pe[0]).scale(arb(6))                              # n = 1 part of a_0
        E1_r = range_on_cell(E1, cl)
        absPe = [arb(x.abs_upper()) for x in Pe_r]; absQe = [arb(x.abs_upper()) for x in Qe_r]
        # e^{-2t}-weighted versions for M_P on cells meeting t <= 0 (origin side)
        wgt = (kind != "pinf") and left_region
        if wgt:
            try:
              if kind == "minf":
                E1w_r = range_on_cell(weighted(drop_const(E1, ic, "6(Qe_1 - Pe_1)"), fmpq(-2), ta), cl)
                Pew = [None] + [range_on_cell(weighted(drop_const(Pe[n - 1], ic, "Pe_%d" % n), fmpq(-2), ta), cl) for n in range(2, Nf + 1)]
                Qew = [None] + [range_on_cell(weighted(drop_const(Qe[n - 1], ic, "Qe_%d" % n), fmpq(-2), ta), cl) for n in range(2, Nf + 1)]
              else:
                E1w_r = range_on_cell(weighted(E1, fmpq(-2), ta), cl)
                Pew = [None] + [range_on_cell(weighted(Pe[n - 1], fmpq(-2), ta), cl) for n in range(2, Nf + 1)]
                Qew = [None] + [range_on_cell(weighted(Qe[n - 1], fmpq(-2), ta), cl) for n in range(2, Nf + 1)]
              absPew = [None] + [arb(x.abs_upper()) for x in Pew[1:]]; absQew = [None] + [arb(x.abs_upper()) for x in Qew[1:]]
            except (AssertionError, ValueError) as ex:
                print("cell %d: weighted a_0 failed: %r" % (ic, ex), flush=True); wgt = False; A0W[ic, :] = np.inf
        # mu_a' hull on the cell (knot at t = 0, both values on cells touching 0)
        vals = []
        if kind == "minf": vals = [fmpq(-17, 2)] + ([fmpq(-5, 4)] if t_lo >= 0 else [])
        elif kind == "pinf": vals = [fmpq(-5, 4)] + ([fmpq(-17, 2)] if t_lo <= 0 else [])
        else: vals = ([fmpq(-17, 2)] if t_lo <= 0 else []) + ([fmpq(-5, 4)] if t_hi >= 0 else [])
        mua = q2arb((min(vals) + max(vals)) / 2) + arb(0, float(q2arb((max(vals) - min(vals)) / 2).upper()))
        for ib in range(ntheta):
            q = c_l - sum((Pe_r[n - 1] * cos2n[ib][n - 1] for n in range(1, Nf + 1)), arb(0))
            Qlo[ic, ib] = flo(q); Qhi[ic, ib] = fup(q)
            # caps: arb upper bounds of 1/min cos theta and 1/min |sin 2 theta| on the box (None when the minimum may vanish)
            capU_a = (1 / cmin[ib]) if float(cmin[ib].lower()) > 0 else None; capS_a = (1 / s2min[ib]) if float(s2min[ib].lower()) > 0 else None
            capU = fup(capU_a) if capU_a is not None else float("inf"); capS = fup(capS_a) if capS_a is not None else float("inf")
            def bU_of(n): return arb(n) if (capU_a is None or n <= capU) else capU_a          # upper bound of min(n, 1/cos) either way
            def bS_of(n): return arb(n) if (capS_a is None or n <= capS) else capS_a
            def gb_of(n):
                g1 = arb((4 * n ** 3 + 2 * n) // 3)
                if capU_a is None: return g1
                g2 = 4 * n * capU_a * capU_a
                return g2 if fup(g2) < fup(g1) else g1
            # a_1
            a1 = 2 * sum(((-1) ** n * Pe_r[n - 1] * U2s[ib][n - 1] for n in range(1, N0 + 1)), arb(0))
            tail = arb(0)
            for n in range(N0 + 1, Nf + 1):
                b = bU_of(n); tail += absPe[n - 1] * (b * b)
            a1 = a1 + ball_rad(2 * tail)
            A1[ic, ib] = finite_or_raise(fup(arb(a1.abs_upper())), "a1")
            # a_0 (n = 1 part exact; n = 2..N0 exact identities; tails)
            a0 = E1_r + sum((6 * (-1) ** n * Pe_r[n - 1] * U2s[ib][n - 1] - 2 * Qe_r[n - 1] * GN[ib][n - 1] + 2 * Qe_r[n - 1] * UC2[ib][n - 1] for n in range(2, N0 + 1)), arb(0))
            tail = arb(0)
            for n in range(N0 + 1, Nf + 1):
                bU = bU_of(n); bS = bS_of(n); gb = gb_of(n)
                tail += absPe[n - 1] * (6 * bU * bU) + absQe[n - 1] * (2 * gb + 2 * bS)
            a0 = a0 + ball_rad(tail)
            A0[ic, ib] = finite_or_raise(fup(arb(a0.abs_upper())), "a0")
            if wgt:
                a0w = E1w_r + sum((6 * (-1) ** n * Pew[n - 1] * U2s[ib][n - 1] - 2 * Qew[n - 1] * GN[ib][n - 1] + 2 * Qew[n - 1] * UC2[ib][n - 1] for n in range(2, N0 + 1)), arb(0))
                tail = arb(0)
                for n in range(N0 + 1, Nf + 1):
                    bU = bU_of(n); bS = bS_of(n); gb = gb_of(n)
                    tail += absPew[n - 1] * (6 * bU * bU) + absQew[n - 1] * (2 * gb + 2 * bS)
                a0w = a0w + ball_rad(tail)
                A0W[ic, ib] = finite_or_raise(fup(arb(a0w.abs_upper())), "a0w")
            # kappa_w
            tang = sum((Qe_r[n - 1] * RATIO[ib][n - 1] for n in range(1, N0 + 1)), arb(0))
            tail = arb(0)
            for n in range(N0 + 1, Nf + 1): tail += absQe[n - 1] * (arb(2 * n) if (capU_a is None or 2 * n <= capU) else capU_a)
            tang = (tang + ball_rad(tail)) * sinth[ib]
            kw = b0 + mua * q / 2 + A_ANI * tang
            KWlo[ic, ib] = finite_or_raise(flo(kw), "kw"); KWhi[ic, ib] = finite_or_raise(fup(kw), "kw")
        if ic % 100 == 0 or cells_sel is not None:
            print("cell %d/%d kind %s t_a %.3f: d in [%.6f, %.6f], kappa_w >= %.4f, max a1 %.3e, max a0 %.3e, idchk %.1e (%.0fs)" % (
                ic, nc, kind, float(ta), Dlo[ic], Dhi[ic], np.nanmin(KWlo[ic]), np.nanmax(A1[ic]), np.nanmax(A0[ic]), IDCHK[ic], time.time() - t0), flush=True)
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    cell_ta = np.array([float(cl["ta"]) for cl in cells.cells]); cell_h = np.array([float(cl["h"]) if cl["h"] is not None else np.nan for cl in cells.cells])
    cell_kind = np.array([cl["kind"] for cl in cells.cells])
    np.savez(os.path.join(outdir, "hypA.npz"), Dlo=Dlo, Dhi=Dhi, DPlo=DPlo, DPhi=DPhi, DD2=DD2, DP2=DP2, DCK=DCK, DPK=DPK, IDCHK=IDCHK, A1=A1, A0=A0, A0W=A0W,
             KWlo=KWlo, KWhi=KWhi, Qlo=Qlo, Qhi=Qhi, theta_edges=np.array([float(x) for x in th]), cell_ta=cell_ta, cell_h=cell_h, cell_kind=cell_kind)
    def nmax(a):
        a = np.asarray(a, dtype=float); a = a[~np.isnan(a)]; return float(np.max(a)) if a.size else None     # inf propagates
    def nmin(a):
        a = np.asarray(a, dtype=float); a = a[~np.isnan(a)]; return float(np.min(a)) if a.size else None
    def usum(a, b): return fup(arb(a) + arb(b)) if (a is not None and b is not None) else None
    isel = np.array(sel)
    # geometric selection (a failed bound is +inf and propagates): left = cells meeting t <= 0, right = cells meeting t >= 0
    def meets_left(i):
        cl = cells.cells[i]; return cl["kind"] == "minf" or (cl["kind"] != "pinf" and cl["tq"] <= 0)
    def meets_right(i):
        cl = cells.cells[i]; return cl["kind"] == "pinf" or (cl["kind"] != "minf" and cl["tq"] + cl["hq"] >= 0)
    left = [i for i in sel if meets_left(i)]; right = [i for i in sel if meets_right(i)]
    # M_P = sup max(e^{-2t}, 1) |a_0|: the e^{-2t}-weighted bound on every cell meeting t <= 0 and the plain bound on every cell meeting t >= 0
    MP_parts = [nmax(A0W[left]) if left else None, nmax(A0[right]) if right else None]
    res = dict(tag=tag, ntheta=ntheta, prec=prec, N0=N0, ncells=len(sel), background="exact modal trial modal_v2.json + z (V005 normalization)",
               c_l=str(c_l.str(30)), D=str(D.str(30)), k=str(k_q),
               d_inf=nmin(Dlo[isel]), d_sup=nmax(Dhi[isel]), d_inf_cell=int(isel[np.nanargmin(Dlo[isel])]), d_sup_cell=int(isel[np.nanargmax(Dhi[isel])]),
               dprime_abs_sup=max(abs(nmin(DPlo[isel])), abs(nmax(DPhi[isel]))),
               A_left=dict(desc="sup over cells meeting t <= 0 (inner half-line included) of |d - D| e^{-2t} and |d'| e^{-2t}",
                           sup_dD_e2=nmax(DD2[left]), sup_dp_e2=nmax(DP2[left]), minf_dD_e2=(float(DD2[0]) if 0 in sel else None), minf_dp_e2=(float(DP2[0]) if 0 in sel else None),
                           C_left=usum(nmax(DD2[left]), nmax(DP2[left])) if left else None),
               A_right=dict(desc="sup over cells meeting t >= 0 (outer half-line included) of |d - c_l| e^{(1-k)t} and |d'| e^{(1-k)t}",
                            sup_dcl_ek=nmax(DCK[right]), sup_dp_ek=nmax(DPK[right]), pinf_dcl_ek=(float(DCK[nc - 1]) if nc - 1 in sel else None), pinf_dp_ek=(float(DPK[nc - 1]) if nc - 1 in sel else None),
                            C_right=usum(nmax(DCK[right]), nmax(DPK[right])) if right else None),
               M_Q=nmax(A1[isel]), M_Q_argmax=[int(x) for x in np.unravel_index(np.nanargmax(np.where(np.isfinite(A1), A1, -np.inf)), A1.shape)],
               M_P=(None if any(x is None for x in MP_parts) else max(MP_parts)), M_P_parts=MP_parts,
               conditional_on="exact normalization c[rho~] = 3 c_l - 1 of the repaired trial (V005; z = (3/k - 1 - c_0)/s) for the dropped exponent-0 constant of d - D on the inner half-line; kappa_w identity holds a.e. (knot t = 0, axes)",
               enclosure="encl.range_finite: Taylor order 8 about the cell midpoint with rigorous remainder; sub-intervals when |e|_max h > 1; half-lines: exact constant + coefficient-sum bound (tailbound.sup_bound)",
               sup_a0_unweighted=nmax(A0[isel]),
               kappa_star_lower=nmin(KWlo[isel]), kappa_star_argmin=[int(x) for x in np.unravel_index(np.nanargmin(np.where(np.isfinite(KWlo), KWlo, np.inf)), KWlo.shape)],
               kappa_w_sup=nmax(KWhi[isel]), q_range=[nmin(Qlo[isel]), nmax(Qhi[isel])],
               identity_check_max=nmax(IDCHK[isel]), dropped_constants=len(DROPPED), dropped_max_rad=(max(x[3] for x in DROPPED) if DROPPED else 0.0),
               seconds=time.time() - t0)
    json.dump(res, open(os.path.join(outdir, "hypA.json"), "w"), indent=1)
    json.dump([dict(cell=a, what=b, mid=cm, rad=r) for a, b, cm, r in DROPPED], open(os.path.join(outdir, "hypA_dropped.json"), "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    a = sys.argv
    sel = [int(x) for x in a[4].split(",")] if len(a) > 4 else None
    main(a[1], int(a[2]) if len(a) > 2 else 64, int(a[3]) if len(a) > 3 else 160, sel)
