"""Second finite section in the lead's realization (lead notes 4 and 5, 02:14Z/02:18Z): the FIXED-EXPONENT operator
   L_fix h = (V.grad - 1) h + U[h].grad rho~      (no strain term)
on the plain spatial space L^2(e^{mu~(log r)} dX) for h and for L_fix h, with mu~ piecewise linear in t (mu~(0) = 0, mu~' piecewise
constant: knots 3/2, 7/4, 3, ..., 10; values 4, 17, 28, 27, 25, 18, 4, -10, -17, -19, -20 sixteenths).
Norms. h = x^2 y sum_m b_m(t) cos 2m theta:  ||h||^2 = sum_{m,m'} Aang_{mm'} int b_m b_{m'} e^{8t + mu~(t)} dt,
   Aang_{mm'} = int_0^{2pi} cos^4 th sin^2 th cos 2m th cos 2m' th dth = (I(m-m') + I(m+m'))/2 with
   I(d) = int (1 + cos 2th/2 - cos 4th - cos 6th/2)/16 cos 2d th dth = pi/8 [d=0] + pi/32 [|d|=1] - pi/16 [|d|=2] - pi/32 [|d|=3].
   g = e^{3t} sum_N G_N sin((2N+1) th):  ||g||^2 = pi sum_N int G_N^2 e^{8t + mu~} dt.   Rows: pi int G_N psi_i e^{8t+mu~} dt (L^2, no derivative).
Cells are split at the knots of mu~ so that the weight is a single exponential on every cell (partial Green recurrences on sub-cells).
Columns: the conforming basis of basis.py (inner powers, coarse splines, outer power laws, J); no tail columns (r^k Theta, KP are not in the space).
"""
import sys, os, time, json, math
from flint import arb, arb_mat, fmpq, fmpq_mat, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb, prim_S, moment_left, moment_right, integrate_ep
import opimage
from opimage import Cells, Background, Column, Operator, addsin, green_A_on_cell, green_B_on_cell, green_B_on_cell_minf
from basis import CoarseSplines, build_mode_columns
from section import MomentCache, TestSplines, arb_dyadic

MU_KNOTS = [fmpq(3, 2), fmpq(7, 4), fmpq(3), fmpq(4), fmpq(5), fmpq(6), fmpq(7), fmpq(8), fmpq(9), fmpq(10)]
MU_VALS = [fmpq(v, 16) for v in (4, 17, 28, 27, 25, 18, 4, -10, -17, -19, -20)]


def mu_prime_at(tq):
    """mu~'(t) on the interval containing tq (right-continuous)"""
    for i, kn in enumerate(MU_KNOTS):
        if tq < kn: return MU_VALS[i]
    return MU_VALS[-1]


def mu_at(tq):
    """mu~(t) = int_0^t mu~' (exact rational)"""
    t = fmpq(tq); s = fmpq(0)
    if t >= 0:
        cur = fmpq(0)
        for i, kn in enumerate(MU_KNOTS):
            if kn >= t: break
            s += (kn - cur) * MU_VALS[i]; cur = kn
        s += (t - cur) * mu_prime_at(cur if cur > 0 or t > 0 else t)
        # careful: value on [cur, t): the interval containing cur
        return s
    else:
        # t < 0: all knots are positive: mu' = 1/4 on (-oo, 3/2)
        return t * MU_VALS[0]


class CellsL2(Cells):
    """trial cells split at the mu~ knots inside [t_-, t_+]; the outer extras include the knots beyond t_+."""
    def __init__(self, T, inner_extra, outer_extra, split_at):
        super().__init__(T, inner_extra, outer_extra)
        new = []
        for cl in self.cells:
            if cl["kind"] != "mid":
                new.append(cl); continue
            lo = cl["tq"]; hi = cl["tq"] + cl["hq"]
            ks = sorted(set(k for k in split_at if lo < k < hi))
            if not ks:
                cl = dict(cl); cl["sub_lo"] = fmpq(0); new.append(cl); continue
            bounds = [lo] + ks + [hi]
            for a, b in zip(bounds[:-1], bounds[1:]):
                new.append(dict(kind="mid", tq=a, ta=q2arb(a), h=q2arb(b - a), hq=b - a, trial_cell=cl["trial_cell"], shift=fmpq(0), sub_lo=a - lo))
        self.cells = new; self.n = len(new); self.tq = [c["tq"] for c in new]
        self.first_mid = next(i for i, c in enumerate(new) if c["kind"] == "mid")


class BackgroundL2(Background):
    """Background data on sub-cells of trial cells (partial Green recurrences from the trial cell's boundary values)."""
    def get(self, ic):
        if ic in self.cache: return self.cache[ic]
        cl = self.cells.cells[ic]
        if cl["kind"] != "mid" or cl.get("sub_lo", fmpq(0)) == 0 and (cl["tq"] + cl["hq"]) == self.T.tb_q[cl["trial_cell"] + 1]:
            return super().get(ic)
        T = self.T; Nf = T.Nf; ci = cl["trial_cell"]; s = cl["sub_lo"]; sa = q2arb(s)
        Rc = T.cell_a[ci] * T.P.transpose()
        Rhat0 = [ExpPoly([(fmpq(0), [Rc[r_, j] for r_ in range(T.p + 1)])]) for j in range(T.Mj)]
        fhat0 = [ExpPoly([(fmpq(0), T.cell_fhat[ci][n - 1])]) for n in range(1, Nf + 1)]
        Rhat = [ep.shift(sa) for ep in Rhat0]; fhat = [ep.shift(sa) for ep in fhat0]
        ta = cl["ta"]; h = cl["h"]; tcell_a = T.tb[ci]; e4c = (4 * tcell_a).exp()
        # A at the sub-cell's left end: A(t_a) = e^{-2n s} A(cell left) + e^{4 t_a} int_0^s e^{(2n+4)(sigma - s)} fhat0(sigma) dsigma
        Abd = []; Bbd = []
        hb = q2arb(T.tb_q[ci + 1] - (cl["tq"] + cl["hq"]))        # distance from the sub-cell's right end to the cell's right end
        tb_ = ta + h
        for n in range(1, Nf + 1):
            lam = arb(2 * n + 4); mom = arb(0)
            for e, cs in fhat0[n - 1].terms.items():
                for p_, cp in enumerate(cs):
                    if cp != 0 and sa != 0: mom += cp * moment_left(q2arb(e) + lam, p_, sa)
            Abd.append((-2 * n * sa).exp() * T.A[ci][n - 1] + (4 * ta).exp() * mom)
            # B at the sub-cell's right end: B(t_b) = e^{-2n hb} B(cell right) + e^{4 t_b} int_0^{hb} e^{(4-2n) sigma'} fhat_b(sigma') dsigma', fhat_b expanded at t_b
            mu = arb(4 - 2 * n); momb = arb(0)
            if hb != 0:
                fhb = fhat0[n - 1].shift(q2arb(cl["tq"] + cl["hq"] - T.tb_q[ci]))
                for e, cs in fhb.terms.items():
                    for p_, cp in enumerate(cs):
                        if cp != 0: momb += cp * moment_right(q2arb(e) + mu, p_, hb)
            Bbd.append((-2 * n * hb).exp() * T.B[ci + 1][n - 1] + (4 * tb_).exp() * momb)
        dR = [Rhat[j].scale(arb(3)) + Rhat[j].deriv() for j in range(T.Mj)]
        e4a = (4 * ta).exp(); em2a = (-2 * ta).exp()
        nmax = Nf if (self.nmax is None or ic in self.full_cells) else min(Nf, self.nmax)
        Pe = []; Qe = []
        for n in range(1, nmax + 1):
            An = green_A_on_cell(fhat[n - 1], n, Abd[n - 1], e4a, "mid")
            Bn = green_B_on_cell(fhat[n - 1], n, Bbd[n - 1], e4a, h, "mid")
            Pe.append((An + Bn).scale(em2a / 2).mul_exp(fmpq(-2))); Qe.append((Bn - An).scale(em2a / 2).mul_exp(fmpq(-2)))
        data = dict(Rhat=Rhat, dR=dR, Pe=Pe, Qe=Qe, fhat=fhat, ta=ta, h=h, kind="mid", e4a=e4a, Abd=Abd, Bbd=Bbd)
        if len(self.cache) > 4: self.cache.pop(next(iter(self.cache)))
        self.cache[ic] = data
        return data


class ColumnFix(Column):
    """column for L_fix: plain Green data (no strain convention)."""
    def green_on_cell(self, ic):
        cells = self.cells; cl = cells.cells[ic]; ta = cl["ta"]; e4a = (4 * ta).exp(); kind = cl["kind"]; h = cl["h"]
        out_A = {}; out_B = {}; in_support = ic in self.pieces
        for n in self.hmodes:
            if in_support:
                fh = self.fh[ic].get(n, ExpPoly())
                if kind == "minf":
                    An = green_A_on_cell(fh, n, self._A_at_right_of(ic, n), e4a, kind)
                    Bn = green_B_on_cell_minf(fh, n, self.B_right[ic][n], e4a)
                elif kind == "pinf":
                    An = green_A_on_cell(fh, n, self.A_left[ic][n], e4a, kind); Bn = green_B_on_cell(fh, n, None, e4a, None, kind)
                else:
                    An = green_A_on_cell(fh, n, self.A_left[ic][n], e4a, kind); Bn = green_B_on_cell(fh, n, self.B_right[ic][n], e4a, h, kind)
            else:
                An = ExpPoly(); Bn = ExpPoly(); tq = cl["tq"]
                if tq >= self.t_end_q: An.add(fmpq(-2 * n), [(-2 * n * (ta - q2arb(self.t_end_q))).exp() * self.A_end[n]])
                else: Bn.add(fmpq(2 * n), [(2 * n * (ta - q2arb(self.t_start_q))).exp() * self.B_start[n]])
            out_A[n] = An; out_B[n] = Bn
        return out_A, out_B


class OperatorFix(Operator):
    """L_fix: no strain term; plain velocity of h."""
    def __init__(self, T, cells, bg, Nmax=None):
        super().__init__(T, cells, bg, Nmax); self.exact_normalized = False

    def far_coefficients(self, col, ic):
        cl = self.cells.cells[ic]; ta = cl["ta"]; out = {}
        for n in col.hmodes:
            if cl["tq"] >= col.t_end_q: out[n] = ((-2 * n * (ta - q2arb(col.t_end_q))).exp() * col.A_end[n], arb(0))
            else: out[n] = (arb(0), (2 * n * (ta - q2arb(col.t_start_q))).exp() * col.B_start[n])
        return out

    def image(self, col, ic, Nmax=None, parts=False):
        Nmax = self.Nmax if Nmax is None else Nmax
        d = self.bg.get(ic); T = self.T; m = col.m; acc = {}
        if ic in col.pieces:
            b = col.pieces[ic]
            for N, ep in self.transport_self(b, m, col.Pcol).items(): addsin(acc, 2 * N + 1, ep)
            Rh = col.Rhat_h(b); Rht = {j: Rh[j].scale(arb(3)) + Rh[j].deriv() for j in Rh}; jmax = max(Rh) if Rh else -1
            for ni in range(len(d["Pe"])):
                n = ni + 1
                if Nmax is not None and n > Nmax + jmax + 2: break
                Pe = d["Pe"][ni]; Qe = d["Qe"][ni]
                for j in Rh:
                    if Nmax is not None and min(abs(2 * j + 1 - 2 * n), 2 * j + 1 + 2 * n) > 2 * Nmax + 1: continue
                    co = (Pe * Rht[j]).scale(arb(-1) / 2); addsin(acc, 2 * j + 1 + 2 * n, co); addsin(acc, 2 * j + 1 - 2 * n, co)
                    co2 = (Qe * Rh[j]).scale(arb(2 * j + 1) / 2); addsin(acc, 2 * n + 2 * j + 1, co2); addsin(acc, 2 * n - 2 * j - 1, co2)
        Ah, Bh = col.green_on_cell(ic); em2a = (-2 * d["ta"]).exp()
        for n in col.hmodes:
            Peh = (Ah[n] + Bh[n]).scale(em2a / 2).mul_exp(fmpq(-2)); Qeh = (Bh[n] - Ah[n]).scale(em2a / 2).mul_exp(fmpq(-2))
            if not Peh.terms and not Qeh.terms: continue
            for j in range(T.Mj):
                if Nmax is not None and min(abs(2 * j + 1 - 2 * n), 2 * j + 1 + 2 * n) > 2 * Nmax + 1: continue
                co = (Peh * d["dR"][j]).scale(arb(-1) / 2); addsin(acc, 2 * j + 1 + 2 * n, co); addsin(acc, 2 * j + 1 - 2 * n, co)
                co2 = (Qeh * d["Rhat"][j]).scale(arb(2 * j + 1) / 2); addsin(acc, 2 * n + 2 * j + 1, co2); addsin(acc, 2 * n - 2 * j - 1, co2)
        if Nmax is not None: acc = {N: ep for N, ep in acc.items() if N <= Nmax}
        return acc


def angular_matrix(Mmax):
    """Aang_{mm'} for m, m' < Mmax as exact multiples of pi (fmpq), per the docstring"""
    def I(d):
        d = abs(d)
        return {0: fmpq(1, 8), 1: fmpq(1, 32), 2: fmpq(-1, 16), 3: fmpq(-1, 32)}.get(d, fmpq(0))
    return [[(I(m - mp) + I(m + mp)) / 2 for mp in range(Mmax)] for m in range(Mmax)]


class WeightsL2:
    def cell_weight(self, cl):
        """W(t) = e^{8t + mu~(t)} = W0 e^{w sigma} on the cell (slope w = 8 + mu~' constant on the cell by construction)"""
        tq = cl["tq"]
        if cl["kind"] == "minf": w = 8 + MU_VALS[0]; W0 = (q2arb(8 * tq + mu_at(tq))).exp()
        else:
            w = 8 + mu_prime_at(tq); W0 = (q2arb(8 * tq + mu_at(tq))).exp()
            if cl["kind"] != "pinf":
                # the cell must not straddle a knot
                hi = tq + cl["hq"]
                assert all(not (tq < k < hi) for k in MU_KNOTS), ("cell straddles a mu knot", str(tq), str(hi))
        return W0, fmpq(w)


class SectionL2:
    def __init__(self, T, cells, bg, Mh, stride, Mout, stride_test, q=3, nJ=8, verbose=True):
        self.T = T; self.cells = cells; self.bg = bg; self.Mh = Mh; self.Mout = Mout; self.q = q
        self.op = OperatorFix(T, cells, bg, Nmax=Mout - 1); self.W = WeightsL2()
        t0 = time.time(); self.cs = CoarseSplines(T, cells, stride); self.cols = []
        for m in range(Mh):
            for lab, pieces in build_mode_columns(T, cells, self.cs, m, q, nJ):
                self.cols.append(dict(m=m, label=lab, col=ColumnFix(m, pieces, T, cells, label=lab)))
        self.ts = TestSplines(T, cells, stride_test); self.ncol = len(self.cols); self.ntest = self.ts.nb
        self.Aang = angular_matrix(Mh)
        if verbose: print("L2 section: %d columns, %d test splines per mode, Mout %d (%.0fs)" % (self.ncol, self.ntest, Mout, time.time() - t0), flush=True)

    def cell_contrib(self, ic):
        cl = self.cells.cells[ic]; mc = MomentCache(cl); W0, w = self.W.cell_weight(cl)
        out = dict(GX={}, GY={}, rows={})
        # X Gram: all column pairs with |m - m'| <= 3 (Aang), radial integral of b_i b_j
        here = [(ci_, cd) for ci_, cd in enumerate(self.cols) if ic in cd["col"].pieces]
        for a_ in range(len(here)):
            ia, cda = here[a_]; ba = cda["col"].pieces[ic]
            for b_ in range(a_, len(here)):
                ib, cdb = here[b_]
                aq = self.Aang[cda["m"]][cdb["m"]]
                if aq == 0: continue
                v = mc.integ(ba * cdb["col"].pieces[ic], w, W0) * q2arb(aq) * arb.pi()
                out["GX"][(ia, ib)] = v
        tp = self.ts.pieces.get(ic, [])
        if not tp: return out
        pi = arb.pi()
        for a_ in range(len(tp)):
            ia, pa = tp[a_]
            for b_ in range(a_, len(tp)):
                ib, pb = tp[b_]
                out["GY"][(ia, ib)] = mc.integ_poly(ExpPoly([(fmpq(0), pa)]), pb, w, W0) * pi
        def rows_of_img(img):
            res = {}
            for N, ep in img.items():
                Tv, Td = mc.Tmats(None, 0, tp, [(i, []) for i, _ in tp]) if False else (None, None)
                row = arb_mat(1, len(tp))
                for e, cs in ep.terms.items():
                    Tv, _ = mc.Tmats(e + w, len(cs) - 1, tp, [(i, []) for i, _ in tp])
                    rv = arb_mat(1, len(cs), list(cs))
                    row = row + rv * Tv
                res[N] = row * (W0 * pi)
            return res
        far = {}
        for ci_, cd in enumerate(self.cols):
            c = cd["col"]
            if ic in c.pieces:
                for N, rv in rows_of_img(self.op.image(c, ic)).items():
                    for a_, (it, _) in enumerate(tp): out["rows"][(N, it, ci_)] = out["rows"].get((N, it, ci_), arb(0)) + rv[0, a_]
            else:
                for n, (al, be) in self.op.far_coefficients(c, ic).items():
                    if al != 0: far.setdefault((n, "A"), {})[ci_] = al
                    if be != 0: far.setdefault((n, "B"), {})[ci_] = be
        nset = sorted(set(n for (n, _) in far))
        if nset:
            unit = self.op.far_unit_images(ic, nset)
            for (n, which), coefs in far.items():
                urows = rows_of_img(unit[n][0 if which == "A" else 1])
                for ci_, co in coefs.items():
                    for N, rv in urows.items():
                        for a_, (it, _) in enumerate(tp): out["rows"][(N, it, ci_)] = out["rows"].get((N, it, ci_), arb(0)) + co * rv[0, a_]
        return out
