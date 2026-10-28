"""Finite-section assembly with exact integration (s2-num): Gram matrices, operator rows, image norms.

Norms (parameters in `Weights`):
  X (domain, factor cosine modes b_m): ||h||_X^2 = sum_m wX_m^2 int (b_m^2 + b_m'^2) W_X(t) dt,
      W_X = e^{-2 eps0 (t-t_-)} (t < t_-), 1 (t_- <= t <= t_+), e^{2 (3 - gammaX)(t - t_+)} (t > t_+);  wX_m^2 = (1 + (2m)^2)^{sX}
  Y (forcing, image factor sine modes G_N = e^{-3t} (Lh)_N): ||g||_Y^2 = sum_N wY_N^2 int (G_N^2 + G_N'^2) W_Y dt, same form with eps0Y, gammaY, sY,
      wY_N^2 = (1 + (2N+1)^2)^{sY}.
Scalar coordinates (J, dk, dtau) carry their own weights (direct sum).
Rows: test functions psi_i(t) = degree-7 B-splines on the test knots (clamped at the outermost finite cell boundaries);
  row (N, i) of column c:  wY_N^2 sum_cells int (G_N psi_i + G_N' psi_i') W_Y dt.
"""
import math, sys, os, time, json
from flint import arb, arb_mat, fmpq, fmpq_mat, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb, moment_left, moment_right, moment_minf, moment_pinf, bspline_cell_polys
from opimage import Cells, Background, Column, Operator
from basis import CoarseSplines, build_mode_columns, tail_columns, poly_shift_q


class Weights:
    def __init__(self, T, eps0X, gammaX, sX, eps0Y, gammaY, sY):
        self.T = T
        self.eps0X = fmpq(eps0X); self.gammaX = fmpq(gammaX); self.sX = sX
        self.eps0Y = fmpq(eps0Y); self.gammaY = fmpq(gammaY); self.sY = sY

    def cell_weight(self, cl, which):
        """(W0 (arb), slope w (fmpq)) with W(t_a + sigma) = W0 e^{w sigma} on the cell"""
        T = self.T
        eps0, gamma = (self.eps0X, self.gammaX) if which == "X" else (self.eps0Y, self.gammaY)
        tq = cl["tq"]
        if tq < T.t_lo_q:
            w = 2 * eps0 * (-1) * (-1)   # W = e^{-2 eps0 (t - t_-)}: slope in t is -2 eps0
            w = -2 * eps0
            W0 = (q2arb(-2 * eps0 * (tq - T.t_lo_q))).exp()
        elif tq < T.t_hi_q:
            w = fmpq(0); W0 = arb(1)
        else:
            w = 2 * (3 - gamma); W0 = (q2arb(w * (tq - T.t_hi_q))).exp()
        return W0, w

    def wX2(self, m): return arb(1 + (2 * m) ** 2) ** self.sX
    def wY2(self, N): return arb(1 + (2 * N + 1) ** 2) ** self.sY


class MomentCache:
    def __init__(self, cl):
        self.cl = cl; self.cache = {}
        self.kind = cl["kind"]; self.h = cl["h"]

    def mom(self, e, p):
        key = (e, p)
        v = self.cache.get(key)
        if v is None:
            ea = q2arb(e)
            if self.kind == "minf": v = moment_minf(ea, p)
            elif self.kind == "pinf": v = moment_pinf(ea, p)
            elif ea <= 0: v = moment_right(ea, p, self.h)
            else: v = (ea * self.h).exp() * moment_left(ea, p, self.h)
            self.cache[key] = v
        return v

    def integ(self, ep, w, W0):
        """int e^{w sigma} W0 ep(sigma) over the cell"""
        tot = arb(0)
        for e, cs in ep.terms.items():
            for p, c in enumerate(cs):
                if c != 0: tot += c * self.mom(e + w, p)
        return W0 * tot

    def Tmats(self, e, degmax, tp, tdp):
        """(Tv, Td): arb_mat (degmax+1) x ntest with Tv[a, i] = sum_b psi_{i,b} mom(e, a+b), Td[a, i] = sum_b psi'_{i,b} mom(e, a+b)"""
        key = ("T", e, degmax)
        v = self.cache.get(key)
        if v is None:
            nt = len(tp)
            Tv = arb_mat(degmax + 1, nt); Td = arb_mat(degmax + 1, nt)
            for i in range(nt):
                pv = tp[i][1]; pd = tdp[i][1]
                for a in range(degmax + 1):
                    sv = arb(0); sd = arb(0)
                    for b, d in enumerate(pv):
                        if d != 0: sv += d * self.mom(e, a + b)
                    for b, d in enumerate(pd):
                        if d != 0: sd += d * self.mom(e, a + b)
                    Tv[a, i] = sv; Td[a, i] = sd
            v = (Tv, Td); self.cache[key] = v
        return v

    def rows_vec(self, ep, dep, w, W0, tp, tdp):
        """arb_mat 1 x ntest of int (ep psi_i + dep psi_i') e^{w sigma} W0 over the cell"""
        nt = len(tp); out = arb_mat(1, nt)
        for e, cs in ep.terms.items():
            Tv, Td = self.Tmats(e + w, max(len(cs) - 1, len(dep.terms.get(e, [arb(0)])) - 1), tp, tdp)
            row = arb_mat(1, Tv.nrows(), [cs[a] if a < len(cs) else arb(0) for a in range(Tv.nrows())])
            out = out + row * Tv
        for e, cs in dep.terms.items():
            Tv, Td = self.Tmats(e + w, max(len(cs) - 1, len(ep.terms.get(e, [arb(0)])) - 1), tp, tdp)
            row = arb_mat(1, Td.nrows(), [cs[a] if a < len(cs) else arb(0) for a in range(Td.nrows())])
            out = out + row * Td
        return out * W0

    def integ_poly(self, ep, poly, w, W0):
        """int e^{w sigma} W0 ep(sigma) poly(sigma)  (poly: list of arb, ascending)"""
        tot = arb(0)
        for e, cs in ep.terms.items():
            for a, c in enumerate(cs):
                if c == 0: continue
                for b, d in enumerate(poly):
                    if d != 0: tot += c * d * self.mom(e + w, a + b)
        return W0 * tot


class TestSplines:
    """degree-7 B-splines on the test knots; pieces on every finite integration cell: dict ic -> list of (i, coeffs arb)"""
    def __init__(self, T, cells, stride_test):
        p = T.p
        fin = [cl["tq"] for cl in cells.cells if cl["kind"] not in ("minf", "pinf")] + [cells.cells[-1]["tq"]]
        # knots: all inner/outer extra boundaries + every stride_test-th mid boundary (+ t_-, t_+)
        ks = set()
        for cl in cells.cells:
            if cl["kind"] in ("inner", "outer"): ks.add(cl["tq"])
        ks.add(T.t_lo_q); ks.add(T.t_hi_q); ks.add(cells.cells[-1]["tq"])
        for b in T.tb_q[1:-1][::stride_test]: ks.add(b)
        ks = sorted(ks)
        self.lo_q, self.hi_q = ks[0], ks[-1]
        self.knots_q = [ks[0]] * (p + 1) + ks[1:-1] + [ks[-1]] * (p + 1)
        self.nb = len(self.knots_q) - p - 1
        self.bounds = ks; self.nk = len(ks) - 1
        polys = bspline_cell_polys(self.knots_q, p, range(self.nk))
        self.pieces = {}
        self.dpieces = {}
        kc = 0
        for ic, cl in enumerate(cells.cells):
            if cl["kind"] in ("minf", "pinf"): continue
            while kc + 1 < self.nk and cl["tq"] >= ks[kc + 1]: kc += 1
            s = cl["tq"] - ks[kc]
            lst = []; dl = []
            for b in range(p + 1):
                co = [fmpq(x) for x in polys[kc][b].coeffs()]
                co = co + [fmpq(0)] * (p + 1 - len(co))
                sh = poly_shift_q(co, s)
                if any(x != 0 for x in sh):
                    lst.append((kc + b, [q2arb(x) for x in sh]))
                    dl.append((kc + b, [q2arb(sh[r_] * r_) for r_ in range(1, p + 1)]))
            self.pieces[ic] = lst; self.dpieces[ic] = dl


class Section:
    def __init__(self, T, cells, bg, weights, Mh, stride, Mout, stride_test, q=3, nJ=8, verbose=True):
        self.T = T; self.cells = cells; self.bg = bg; self.W = weights
        self.Mh = Mh; self.Mout = Mout; self.q = q
        self.op = Operator(T, cells, bg, Nmax=Mout - 1)
        t0 = time.time()
        self.cs = CoarseSplines(T, cells, stride)
        self.cols = []        # list of dict(m, label, col: Column)
        for m in range(Mh):
            for lab, pieces in build_mode_columns(T, cells, self.cs, m, q, nJ):
                self.cols.append(dict(m=m, label=lab, col=Column(m, pieces, T, cells, label=lab)))
        if verbose: print("columns: %d (%.0fs)" % (len(self.cols), time.time() - t0), flush=True)
        TAU, KP, Bm, A0 = tail_columns(T, cells)
        self.TAU = [Column(m, pieces, T, cells, label="TAU_m%d" % m) for m, pieces in TAU]
        self.KP = [Column(m, pieces, T, cells, label="KP_m%d" % m) for m, pieces in KP]
        self.cTAU = sum((c.c for c in self.TAU), arb(0)); self.cKP = sum((c.c for c in self.KP), arb(0))
        if verbose: print("tail columns: TAU %d modes (c = %s), KP %d modes (c = %s) (%.0fs)" % (len(self.TAU), self.cTAU.str(10), len(self.KP), self.cKP.str(10), time.time() - t0), flush=True)
        self.ts = TestSplines(T, cells, stride_test)
        self.ncol = len(self.cols); self.ntest = self.ts.nb
        if verbose: print("test splines per mode: %d; rows %d x %d" % (self.ntest, Mout, self.ntest), flush=True)

    # ---- per-cell contributions ----
    def cell_contrib(self, ic, want_norms=True):
        """returns dict with: GX (per m: dict (i,j)->arb), rows: dict (N, itest, colindex)->arb, rows_tau, rows_kp, imgnorm2 per col, imgnorm2 tau/kp,
        GY diag: test Gram per cell (dict (i,j) -> arb) [mode-independent]"""
        cl = self.cells.cells[ic]; mc = MomentCache(cl)
        W0X, wX = self.W.cell_weight(cl, "X"); W0Y, wY = self.W.cell_weight(cl, "Y")
        out = dict(GX={}, rows={}, rows_tau={}, rows_kp={}, img2={}, GY={})
        # X Gram: columns of the same mode overlapping this cell
        by_mode = {}
        for ci_, cd in enumerate(self.cols):
            if cd["label"] == "J": continue        # scalar coordinate: no remainder Gram entries
            if ic in cd["col"].pieces: by_mode.setdefault(cd["m"], []).append(ci_)
        for m, lst in by_mode.items():
            for a_ in range(len(lst)):
                ia = lst[a_]; ba = self.cols[ia]["col"].pieces[ic]; dba = ba.deriv()
                for b_ in range(a_, len(lst)):
                    ib = lst[b_]; bb = self.cols[ib]["col"].pieces[ic]
                    v = mc.integ(ba * bb + dba * bb.deriv(), wX, W0X)
                    out["GX"][(ia, ib)] = v
        # Y Gram of the test splines on this cell (mode independent; multiplied by wY2 later)
        tp = self.ts.pieces.get(ic, []); tdp = self.ts.dpieces.get(ic, [])
        for a_ in range(len(tp)):
            ia, pa = tp[a_]; dpa = tdp[a_][1]
            for b_ in range(a_, len(tp)):
                ib, pb = tp[b_]; dpb = tdp[b_][1]
                epa = ExpPoly([(fmpq(0), pa)]); epda = ExpPoly([(fmpq(0), dpa)])
                v = mc.integ_poly(epa, pb, wY, W0Y) + (mc.integ_poly(epda, dpb, wY, W0Y) if dpa and dpb else arb(0))
                out["GY"][(ia, ib)] = v
        # operator rows. In-support columns: full image, rows by batched moment matrices. Far columns: unit far images per
        # velocity mode n (UA_n, UB_n) and the strain image M; TAU and KP (260 single-mode pieces each) are aggregated per n.
        Nmax = self.Mout - 1
        nt_here = len(tp)
        if nt_here == 0:
            return out
        def rows_of_img(img):
            """dict N -> arb_mat(1, nt_here)"""
            res = {}
            for N, ep in img.items():
                res[N] = mc.rows_vec(ep, ep.deriv(), wY, W0Y, tp, tdp) * self.W.wY2(N)
            return res
        def store_rows(key_store, cidx, rows):
            for N, rv in rows.items():
                for a_, (it, _) in enumerate(tp):
                    key = (N, it, cidx); key_store[key] = key_store.get(key, arb(0)) + rv[0, a_]
        groups = [("rows", [(ci_, cd["col"]) for ci_, cd in enumerate(self.cols)]), ("rows_tau", [("TAU", c) for c in self.TAU]), ("rows_kp", [("KP", c) for c in self.KP])]
        far_needed = {}      # (n, which) -> dict cidx_store -> coefficient (aggregated)
        need_M = {}          # (store, cidx) -> c
        for store, lst in groups:
            for cidx, c in lst:
                if ic in c.pieces:
                    store_rows(out[store], cidx, rows_of_img(self.op.image(c, ic)))
                else:
                    fc = self.op.far_coefficients(c, ic)
                    for n, (al, be) in fc.items():
                        if al != 0:
                            d = far_needed.setdefault((n, "A"), {}); d[(store, cidx)] = d.get((store, cidx), arb(0)) + al
                        if be != 0:
                            d = far_needed.setdefault((n, "B"), {}); d[(store, cidx)] = d.get((store, cidx), arb(0)) + be
                    if c.c != 0: need_M[(store, cidx)] = need_M.get((store, cidx), arb(0)) + c.c
        nset = sorted(set(n for (n, w_) in far_needed))
        if nset:
            unit = self.op.far_unit_images(ic, nset)
            for (n, which), coefs in far_needed.items():
                U = unit[n][0 if which == "A" else 1]
                urows = rows_of_img(U)
                for (store, cidx), co in coefs.items():
                    for N, rv in urows.items():
                        for a_, (it, _) in enumerate(tp):
                            key = (N, it, cidx); out[store][key] = out[store].get(key, arb(0)) + co * rv[0, a_]
        if need_M:
            Mrows = rows_of_img({N: ep for N, ep in self.op.M_cached(ic).items() if N <= Nmax})
            for (store, cidx), co in need_M.items():
                for N, rv in Mrows.items():
                    for a_, (it, _) in enumerate(tp):
                        key = (N, it, cidx); out[store][key] = out[store].get(key, arb(0)) + co * rv[0, a_]
        return out


def arb_dyadic(x):
    man, ex = x.mid().man_exp(); rman, rex = x.rad().man_exp()
    return [str(man), str(ex), str(rman), str(rex)]


if __name__ == "__main__":
    FIX = os.path.join(os.path.dirname(__file__), "..", "research_copy", "analysis1", "IPM_Analysis_I.artifacts", "numerics", "data", "trial_small_M20.npz")
    T = ExactTrial.from_npz(FIX, prec=200); T.build_green(verbose=False)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    from basis import cutoff_chi
    full = set(cutoff_chi(T, cells).keys()) | set(ic for ic, cl in enumerate(cells.cells) if cl["kind"] in ("outer", "pinf"))
    bg = Background(T, cells, nmax=6 + 2 + 3, full_cells=full)
    k = T.k_q
    Wt = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
    S = Section(T, cells, bg, Wt, Mh=2, stride=60, Mout=6, stride_test=30)
    for ic in [1, cells.first_mid + 5, cells.first_mid + 700, cells.n - 3]:
        t0 = time.time(); out = S.cell_contrib(ic, want_norms=False)
        print("cell %d (%s): GX %d, GY %d, rows %d, img2 %d  (%.1fs)" % (ic, cells.cells[ic]["kind"], len(out["GX"]), len(out["GY"]), len(out["rows"]), len(out["img2"]), time.time() - t0), flush=True)


# ---------------------------------------------------------------------------------------------------------------
# Phase 2a: exact image norms within the retained modes N <= Nmax (for the within-mode part of (I - Q_M) L P_N).
# For every cell: in-support columns -> exact sum_N wY2 int (G_N^2 + G_N'^2) W_Y and cross inner products with the unit far images;
# far columns -> quadratic form in their coefficients (alpha_n, beta_n, c) with the unit Gram of (UA_n, UB_n, M) on the cell.
def cell_norms(self, ic):
    cl = self.cells.cells[ic]; mc = MomentCache(cl)
    W0Y, wY = self.W.cell_weight(cl, "Y")
    Nmax = self.Mout - 1
    allcols = [(ci_, cd["col"]) for ci_, cd in enumerate(self.cols)] + [("TAU", c) for c in self.TAU]
    def ipN(e1, de1, e2, de2):
        return mc.integ(e1 * e2 + de1 * de2, wY, W0Y)
    # unit functions on this cell: dict key -> {N: (ep, dep)}
    nset = sorted(set(n for _, c in allcols if ic not in c.pieces for n in c.hmodes))
    units = {}
    if nset:
        for n, (UA, UB) in self.op.far_unit_images(ic, nset).items():
            units[("A", n)] = {N: (ep, ep.deriv()) for N, ep in UA.items()}
            units[("B", n)] = {N: (ep, ep.deriv()) for N, ep in UB.items()}
    units[("M", 0)] = {N: (ep, ep.deriv()) for N, ep in self.op.M_cached(ic).items() if N <= Nmax}
    keys = sorted(units.keys(), key=str)
    def gram_pair(f, g):
        tot = arb(0)
        for N in set(f) & set(g):
            tot += self.W.wY2(N) * ipN(f[N][0], f[N][1], g[N][0], g[N][1])
        return tot
    UG = {}
    for a_ in range(len(keys)):
        for b_ in range(a_, len(keys)):
            UG[(keys[a_], keys[b_])] = gram_pair(units[keys[a_]], units[keys[b_]])
    # in-support images
    imgs = {}
    for cidx, c in allcols:
        if ic in c.pieces:
            img = self.op.image(c, ic)
            key = cidx
            cur = imgs.get(key, {})
            for N, ep in img.items():
                if N in cur: cur[N] = (cur[N][0] + ep, None)
                else: cur[N] = (ep, None)
            imgs[key] = cur
    for key in imgs: imgs[key] = {N: (ep, ep.deriv()) for N, (ep, _) in imgs[key].items()}
    out = dict(norm2={}, cross={}, UG={}, coef={})
    for key, f in imgs.items(): out["norm2"][key] = gram_pair(f, f)
    # in-support x in-support cross terms (same cell)
    ks = sorted(imgs.keys(), key=str)
    for a_ in range(len(ks)):
        for b_ in range(a_ + 1, len(ks)): out["cross"][(ks[a_], ks[b_])] = gram_pair(imgs[ks[a_]], imgs[ks[b_]])
    # in-support x unit cross terms
    for key, f in imgs.items():
        for uk in keys: out["cross"][(key, uk)] = gram_pair(f, units[uk])
    out["UG"] = UG
    # far coefficients of every far column on this cell: cidx -> {unit key: arb}
    for cidx, c in allcols:
        if ic in c.pieces: continue
        fc = self.op.far_coefficients(c, ic); co = {}
        for n, (al, be) in fc.items():
            if al != 0: co[("A", n)] = co.get(("A", n), arb(0)) + al
            if be != 0: co[("B", n)] = co.get(("B", n), arb(0)) + be
        if c.c != 0: co[("M", 0)] = co.get(("M", 0), arb(0)) + c.c
        if co: out["coef"][cidx] = co
    return out
Section.cell_norms = cell_norms
