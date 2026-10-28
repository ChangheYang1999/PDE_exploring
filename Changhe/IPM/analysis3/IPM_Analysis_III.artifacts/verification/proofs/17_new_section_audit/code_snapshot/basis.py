"""Exactly conforming column basis for the finite section (s2-num).  All joins are exact rational identities.

Per angular mode m: radial functions b(t) (the factor of h = x^2 y b(t) cos 2m theta):
  (a) coarse degree-7 B-splines on every `stride`-th trial boundary (clamped at t_-, t_+) whose q-jets vanish at both ends
      (indices q+1 .. nb_c-q-2): zero outside [t_-, t_+];
  (b) the first q+1 B-splines, each extended on t < t_- by the unique combination of e^{2 j tau'} (j = 1..q+1) with the same q-jet;
  (c) inner powers e^{2 j tau'} (j = q+2..7) minus the combination of e^{2 j' tau'} (j' <= q+1) with the same q-jet (zero for t >= t_-);
  (d) the last q+1 B-splines extended on t > t_+ by the combination of e^{alpha_q' tau} (q' = 1..q+1) with the same q-jet;
  (e) outer power laws e^{alpha_q' tau} (q' = q+2..9) minus the matching combination (q'' <= q+1).
  For m = 0 also J = 1 on t < t_- plus the sum of the first `nJ` coarse B-splines (C^6 at t_-, zero near t_+).
Scalar multi-mode columns: TAU = chi(t) e^{(k-3)(t - t_+)} Theta_1 (modes B_m), KP = chi(t) (t - t_+) e^{(k-3)(t-t_+)} Theta_0~ (modes A_m0),
chi = sum of the last `ncut` fine B-splines of the trial (exactly 1 near t_+, C^6).
Every function is C^q at t_-, t_+ (exactly), C^6 at the coarse knots, smooth elsewhere; hence (q >= 2) L h has an H^1_loc image.
"""
import math, sys, os
from fractions import Fraction
from flint import arb, fmpq, fmpq_mat, fmpq_poly, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb, bspline_cell_polys
from opimage import Cells, Column


def poly_shift_q(coeffs, s):
    """fmpq coefficients of p(sigma + s) given those of p(sigma)"""
    d = len(coeffs); out = [fmpq(0)] * d
    for p in range(d):
        if coeffs[p] == 0: continue
        for q in range(p + 1):
            out[q] += coeffs[p] * math.comb(p, q) * s ** (p - q)
    return out


def poly_deriv_at0(coeffs, n):
    """n-th derivative at 0 of the polynomial with ascending fmpq coefficients"""
    return coeffs[n] * math.factorial(n) if n < len(coeffs) else fmpq(0)


class CoarseSplines:
    """degree-7 B-splines on the coarse knots; exact pieces on every integration cell of `cells`."""
    def __init__(self, T, cells, stride):
        self.T = T; self.cells = cells; p = T.p
        interior = T.tb_q[1:-1][::stride]
        self.knots_q = [T.t_lo_q] * (p + 1) + list(interior) + [T.t_hi_q] * (p + 1)
        self.nb = len(self.knots_q) - p - 1
        self.cbounds = [T.t_lo_q] + list(interior) + [T.t_hi_q]
        self.ncc = len(self.cbounds) - 1
        polys = bspline_cell_polys(self.knots_q, p, range(self.ncc))     # [coarse cell][active b] fmpq_poly in sigma_coarse
        # map every mid integration cell to its coarse cell and the exact pieces of the active splines there
        self.pieces = [dict() for _ in range(self.nb)]      # spline index -> {ic: [fmpq coeffs]}
        cc = 0
        for ic, cl in enumerate(cells.cells):
            if cl["kind"] != "mid": continue
            while cc + 1 < self.ncc and cl["tq"] >= self.cbounds[cc + 1]: cc += 1
            s = cl["tq"] - self.cbounds[cc]
            for b in range(p + 1):
                co = polys[cc][b].coeffs()
                co = [fmpq(x) for x in co] + [fmpq(0)] * (p + 1 - len(co))
                sh = poly_shift_q(co, s)
                if any(x != 0 for x in sh): self.pieces[cc + b][ic] = sh
        # jets at t_- (sigma = 0 of coarse cell 0) and at t_+ (end of the last coarse cell) for all splines
        self.jet_lo = [[poly_deriv_at0([fmpq(x) for x in polys[0][b].coeffs()] if b < p + 1 else [fmpq(0)], n) if b < p + 1 else fmpq(0) for n in range(p + 1)] for b in range(self.nb)]
        hl = self.cbounds[-1] - self.cbounds[-2]
        self.jet_hi = [[fmpq(0)] * (p + 1) for _ in range(self.nb)]
        for b in range(p + 1):
            co = [fmpq(x) for x in polys[self.ncc - 1][b].coeffs()]
            sh = poly_shift_q(co + [fmpq(0)] * (p + 1 - len(co)), hl)
            for n in range(p + 1): self.jet_hi[self.ncc - 1 + b][n] = poly_deriv_at0(sh, n)


def vander_solve(exps, jets, q):
    """solve sum_j D_j exps[j]^n = jets[n], n = 0..q (len(exps) = q+1), exactly."""
    V = fmpq_mat(q + 1, q + 1); rhs = fmpq_mat(q + 1, 1)
    for n in range(q + 1):
        for j, e in enumerate(exps): V[n, j] = fmpq(e) ** n
        rhs[n, 0] = fmpq(jets[n])
    sol = V.solve(rhs)
    return [sol[j, 0] for j in range(q + 1)]


def build_mode_columns(T, cells, cs, m, q, nJ=8):
    """list of (label, pieces dict ic -> ExpPoly) for angular mode m"""
    p = T.p; cols = []
    mid_ics = [ic for ic, cl in enumerate(cells.cells) if cl["kind"] == "mid"]
    inner_ics = [ic for ic, cl in enumerate(cells.cells) if cl["kind"] in ("minf", "inner")]
    outer_ics = [ic for ic, cl in enumerate(cells.cells) if cl["kind"] in ("outer", "pinf")]
    def spline_pieces(b):
        return {ic: ExpPoly([(fmpq(0), [q2arb(x) for x in co])]) for ic, co in cs.pieces[b].items()}
    def inner_pieces(Dj):
        """sum_j Dj[j] e^{2 (j+1) tau'} on the inner cells (tau' = sigma + shift)"""
        out = {}
        for ic in inner_ics:
            s = cells.cells[ic]["shift"]; ep = ExpPoly()
            for j, Dq in enumerate(Dj):
                if Dq != 0: ep.add(fmpq(2 * (j + 1)), [q2arb(Dq) * (q2arb(fmpq(2 * (j + 1)) * s)).exp()])
            if ep.terms: out[ic] = ep
        return out
    def outer_pieces(Aq):
        """sum_{q'} Aq[q'-1] e^{alpha_q' tau} (q' = 1..) on the outer cells"""
        out = {}
        for ic in outer_ics:
            s = cells.cells[ic]["shift"]; ep = ExpPoly()
            for i, Av in enumerate(Aq):
                if Av != 0:
                    al = T.alpha_q[i + 1]
                    ep.add(al, [q2arb(Av) * (q2arb(al * s)).exp()])
            if ep.terms: out[ic] = ep
        return out
    def merge(*ds):
        out = {}
        for d in ds:
            for ic, ep in d.items(): out[ic] = out[ic] + ep if ic in out else ep
        return out
    exps_in = [2 * (j + 1) for j in range(q + 1)]
    exps_out = [T.alpha_q[i + 1] for i in range(q + 1)]
    # (b) first q+1 splines with inner extension
    for b in range(q + 1):
        D = vander_solve(exps_in, cs.jet_lo[b][:q + 1], q)
        cols.append(("sp%d+in" % b, merge(spline_pieces(b), inner_pieces(D))))
    # (c) inner powers with vanishing q-jet
    for j in range(q + 2, T.NIN + 1):
        jets = [fmpq(2 * j) ** n for n in range(q + 1)]
        D = vander_solve(exps_in, jets, q)
        Dfull = [fmpq(0)] * T.NIN; Dfull[j - 1] = fmpq(1)
        for i in range(q + 1): Dfull[i] -= D[i]
        cols.append(("in%d" % j, inner_pieces(Dfull)))
    # (a) interior splines
    for b in range(q + 1, cs.nb - q - 1):
        cols.append(("sp%d" % b, spline_pieces(b)))
    # (d) last q+1 splines with outer extension
    for b in range(cs.nb - q - 1, cs.nb):
        A = vander_solve(exps_out, cs.jet_hi[b][:q + 1], q)
        cols.append(("sp%d+out" % b, merge(spline_pieces(b), outer_pieces(A))))
    # (e) outer power laws with vanishing q-jet
    for qq in range(q + 2, T.NOUT):
        jets = [T.alpha_q[qq] ** n for n in range(q + 1)]
        A = vander_solve(exps_out, jets, q)
        Afull = [fmpq(0)] * (T.NOUT - 1); Afull[qq - 1] = fmpq(1)
        for i in range(q + 1): Afull[i] -= A[i]
        cols.append(("out%d" % qq, outer_pieces(Afull)))
    if m == 0:
        # J = 1 on the inner cells + sum of the first nJ coarse splines
        pj = {}
        for ic in inner_ics: pj[ic] = ExpPoly([(fmpq(0), [arb(1)])])
        for b in range(nJ): pj = merge(pj, spline_pieces(b))
        cols.append(("J", pj))
    return cols


def cutoff_chi(T, cells, ncut=10):
    """chi = sum of the last ncut fine B-splines of the trial: exact polynomial pieces on the mid cells (dict ic -> [fmpq])"""
    out = {}
    for ic, cl in enumerate(cells.cells):
        if cl["kind"] != "mid": continue
        ci = cl["trial_cell"]; Tm = T.cell_T[ci]
        co = [fmpq(0)] * (T.p + 1); nz = False
        for b in range(T.p + 1):
            if ci + b >= T.nb - ncut:
                nz = True
                for r_ in range(T.p + 1): co[r_] += Tm[r_, b]
        if nz and any(x != 0 for x in co): out[ic] = co
    return out


def tail_columns(T, cells, ncut=10):
    """TAU and KP as lists of single-mode Column objects (and the mode coefficient vectors)."""
    chi = cutoff_chi(T, cells, ncut)
    A0 = [q2arb(T.Aout_q[m][0]) + (T.z if m == 0 else arb(0)) for m in range(T.M)]
    Bm = [arb(0)] * T.M
    Bm[0] = A0[1] / 2; Bm[1] = A0[0] + A0[2] / 2
    for j in range(2, T.M): Bm[j] = (A0[j - 1] + A0[j + 1]) / 2 if j + 1 < T.M else A0[j - 1] / 2
    al0 = T.alpha_q[0]
    outer_ics = [ic for ic, cl in enumerate(cells.cells) if cl["kind"] in ("outer", "pinf")]
    def pieces(tfactor):
        out = {}
        for ic, co in chi.items():
            cl = cells.cells[ic]; s = cl["tq"] - T.t_hi_q            # tau = sigma + s  (s <= 0)
            poly = [q2arb(x) for x in co]
            if tfactor:   # multiply by (sigma + s)
                poly = [arb(0)] + poly if False else None
                base = [q2arb(x) for x in co]
                poly = [arb(0)] * (len(base) + 1)
                for i, v in enumerate(base): poly[i] += v * q2arb(s); poly[i + 1] += v
            out[ic] = ExpPoly([(al0, [v * (q2arb(al0 * s)).exp() for v in poly])])
        for ic in outer_ics:
            s = cells.cells[ic]["shift"]
            poly = [q2arb(s), arb(1)] if tfactor else [arb(1)]
            out[ic] = ExpPoly([(al0, [v * (q2arb(al0 * s)).exp() for v in poly])])
        return out
    p_tau = pieces(False); p_kp = pieces(True)
    TAU = [(m, {ic: ep.scale(Bm[m]) for ic, ep in p_tau.items()}) for m in range(T.M) if Bm[m] != 0]
    KP = [(m, {ic: ep.scale(A0[m]) for ic, ep in p_kp.items()}) for m in range(T.M) if A0[m] != 0]
    return TAU, KP, Bm, A0


def check_conformity(T, cells, cols, q):
    """numerical check (floating evaluation) that every column is C^q at t_- and t_+: compares one-sided jets."""
    worst = 0.0
    for lab, pieces in cols:
        for tq in (T.t_lo_q, T.t_hi_q):
            icR = cells.find(tq); icL = icR - 1
            epL = pieces.get(icL); epR = pieces.get(icR)
            for n in range(q + 1):
                vL = arb(0); vR = arb(0)
                if epL is not None:
                    e = epL
                    for _ in range(n): e = e.deriv()
                    clL = cells.cells[icL]; vL = e(clL["h"] if clL["h"] is not None else arb(0))
                if epR is not None:
                    e = epR
                    for _ in range(n): e = e.deriv()
                    vR = e(arb(0))
                d = vL - vR
                worst = max(worst, abs(float(d.mid())) + float(d.rad()))
    return worst


if __name__ == "__main__":
    import time
    FIX = os.path.join(os.path.dirname(__file__), "..", "research_copy", "analysis1", "IPM_Analysis_I.artifacts", "numerics", "data", "trial_small_M20.npz")
    T = ExactTrial.from_npz(FIX, prec=200)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    t0 = time.time(); cs = CoarseSplines(T, cells, 60); print("coarse splines: nb =", cs.nb, "coarse cells", cs.ncc, "%.1fs" % (time.time() - t0))
    q = 3
    cols = build_mode_columns(T, cells, cs, 0, q)
    print("mode-0 columns:", len(cols), [lab for lab, _ in cols][:12], "...")
    print("conformity (one-sided jets to order %d) max mismatch: %.2e" % (q, check_conformity(T, cells, cols, q)))
    # the J column: jets to order 6 at t_- (should match the constant 1 exactly)
    J = dict(cols)["J"]
    print("J conformity to order 6: %.2e" % check_conformity(T, cells, [("J", J)], 6))
    TAU, KP, Bm, A0 = tail_columns(T, cells)
    print("TAU modes:", len(TAU), " KP modes:", len(KP), " Bm[0:3] =", [b.str(8) for b in Bm[:3]])
    # chi = 1 near t_+ exactly?
    chi = cutoff_chi(T, cells); last = max(chi); print("chi on last fine cell:", chi[last][:2], "nonzero cells:", len(chi))
