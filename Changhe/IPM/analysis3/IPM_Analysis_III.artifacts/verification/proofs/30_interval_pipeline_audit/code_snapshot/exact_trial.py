"""Exact (ball-arithmetic) representation of the exactly normalized modal trial rho~ of Analysis I (s2-num, 2026-10-28).

Definition (verifier topic modal_repair of Analysis I, CONFIRMED there): rho~ = x^2 y sum_{m<M} a_m(t) cos(2 m theta), t = log r,
  t < t_-:        a_m = delta_{m0} + sum_{j=1}^{7} D_mj e^{2 j tau} + e^{bi tau} sum_{i<7} Ei_mi tau^i,      tau = t - t_-
  t_- <= t <= t_+: a_m = degree-7 clamped B-spline in t with the exact dyadic knots and coefficients S_mi
  t > t_+:        a_m = sum_q A_mq e^{alpha_q tau} + e^{-bo tau} sum_{i<7} Eo_mi tau^i,                    tau = t - t_+
with t_- = knots[0], t_+ = knots[-1] (exact dyadics), alpha_q = (k-3) - j_q (1-k) - 2 l_q, Ei and Eo the UNIQUE C^6 join coefficients
(computed here exactly in rationals), A_00 replaced by A_00 + z, z the exact real number making c[rho~] = 3/k - 1 (enclosed below, with
the whole computation uniform over the enclosure of z).  All stored doubles (hex) are exact rationals.

Exponential polynomials on a cell with local variable sigma = t - t_a (left end; for the inner cell sigma = t - t_- <= 0):
  dict {exponent (fmpq): [c_0, ..., c_d] (arb)}  meaning  sum_e e^{e sigma} sum_p c_p sigma^p.

Green data (canonical inverse, -Lap psi = d_x rho, psi = sum_n psi_n(t) sin(2 n theta)):
  f_n = sine-2n mode of d_x rho~,  A_n(t) = e^{-2nt} int_{-oo}^t e^{(2n+2)s} f_n ds,  B_n(t) = e^{2nt} int_t^oo e^{(2-2n)s} f_n ds,
  psi_n = (A_n + B_n)/(4n),  d psi_n/dt = (B_n - A_n)/2,  c[rho~] = psi_xy(0) = (1/2) int_R f_1 dt.
"""
import json, lzma, math, os, sys, time
from fractions import Fraction
from flint import arb, arb_mat, fmpq, fmpq_poly, fmpq_mat, ctx

HERE = os.path.dirname(os.path.abspath(__file__))
EXACT_JSON = os.path.join(HERE, "..", "research_copy", "analysis1", "IPM_Analysis_I.artifacts", "verification", "data_exact", "modal_v2.json.xz")
# z enclosure from analysis1 verification/research/modal_repair/PROOF.md (both independent interval calculations):
Z_LO = "-1.198605236453734890460334164888e-20"
Z_HI = "-1.198605236453734890460334164887e-20"
PREC = 320


def hexq(s):
    """exact rational of a hex-float string"""
    f = Fraction(float.fromhex(s)); return fmpq(f.numerator, f.denominator)


def q2arb(q):
    return arb(q.p) / arb(q.q) if isinstance(q, fmpq) else arb(q)


class ExpPoly:
    """sum_e e^{e sigma} p_e(sigma); exponents fmpq, coefficients arb (ascending)."""
    __slots__ = ("terms",)

    def __init__(self, terms=None):
        self.terms = {}
        if terms:
            for e, c in terms:
                self.add(e, c)

    def add(self, e, c):
        e = fmpq(e); c = list(c)
        while len(c) > 1 and c[-1] == 0: c.pop()
        if e in self.terms:
            old = self.terms[e]; n = max(len(old), len(c)); new = [arb(0)] * n
            for i, v in enumerate(old): new[i] += v
            for i, v in enumerate(c): new[i] += v
            self.terms[e] = new
        else:
            self.terms[e] = [arb(x) for x in c]
        return self

    def scale(self, s):
        return ExpPoly([(e, [s * x for x in c]) for e, c in self.terms.items()])

    def __add__(self, o):
        r = ExpPoly([(e, c) for e, c in self.terms.items()])
        for e, c in o.terms.items(): r.add(e, c)
        return r

    def __sub__(self, o):
        return self + o.scale(arb(-1))

    def mul_exp(self, beta):
        """multiply by e^{beta sigma}"""
        return ExpPoly([(e + fmpq(beta), c) for e, c in self.terms.items()])

    def deriv(self):
        r = ExpPoly()
        for e, c in self.terms.items():
            ea = q2arb(e); d = [ea * x for x in c]
            for p in range(1, len(c)): d[p - 1] += p * c[p]
            r.add(e, d)
        return r

    def __mul__(self, o):
        r = ExpPoly()
        for e1, c1 in self.terms.items():
            for e2, c2 in o.terms.items():
                prod = [arb(0)] * (len(c1) + len(c2) - 1)
                for i, a in enumerate(c1):
                    if a == 0: continue
                    for j, b in enumerate(c2): prod[i + j] += a * b
                r.add(e1 + e2, prod)
        return r

    def shift(self, s):
        """re-expand around sigma' = sigma - s (i.e. return q with q(sigma') = self(sigma' + s))"""
        r = ExpPoly(); s = arb(s)
        for e, c in self.terms.items():
            d = len(c); new = [arb(0)] * d
            # p(sigma' + s) = sum_p c_p (sigma'+s)^p
            for p in range(d):
                if c[p] == 0: continue
                for q in range(p + 1):
                    new[q] += c[p] * arb.bin_uiui(p, q) * s ** (p - q)
            r.add(e, [x * (q2arb(e) * s).exp() for x in new])
        return r

    def __call__(self, sigma):
        sigma = arb(sigma); out = arb(0)
        for e, c in self.terms.items():
            pv = arb(0)
            for p in range(len(c) - 1, -1, -1): pv = pv * sigma + c[p]
            out += (q2arb(e) * sigma).exp() * pv
        return out

    def maxdeg(self):
        return max(len(c) for c in self.terms.values()) - 1


# ---------- exact exponential-polynomial moments ----------
def prim_S(lam, p):
    """polynomial coefficients (ascending, arb) of S with int e^{lam sigma} sigma^p dsigma = e^{lam sigma} S(sigma), lam != 0 (arb)."""
    S = [arb(0)] * (p + 1)
    for l in range(p + 1):
        S[p - l] = arb((-1) ** l) * arb.fac_ui(p) / arb.fac_ui(p - l) / lam ** (l + 1)
    return S


def _polyval(c, x):
    v = arb(0)
    for p in range(len(c) - 1, -1, -1): v = v * x + c[p]
    return v


def moment_left(lam, p, h):
    """int_0^h e^{lam (sigma - h)} sigma^p dsigma  (any sign of lam; the exponential is normalized at the RIGHT end: use for lam > 0)."""
    lam = arb(lam); h = arb(h)
    if lam == 0: return h ** (p + 1) / (p + 1)
    S = prim_S(lam, p)
    return _polyval(S, h) - (-lam * h).exp() * S[0]


def moment_right(mu, p, h):
    """int_0^h e^{mu sigma} sigma^p dsigma (exponential normalized at the LEFT end: use for mu <= 0; for small positive mu also fine)."""
    mu = arb(mu); h = arb(h)
    if mu == 0: return h ** (p + 1) / (p + 1)
    S = prim_S(mu, p)
    return (mu * h).exp() * _polyval(S, h) - S[0]


def moment_minf(lam, p):
    """int_{-oo}^0 e^{lam sigma} sigma^p dsigma, lam > 0"""
    lam = arb(lam); assert lam > 0
    return arb((-1) ** p) * arb.fac_ui(p) / lam ** (p + 1)


def moment_pinf(mu, p):
    """int_0^oo e^{mu sigma} sigma^p dsigma, mu < 0"""
    mu = arb(mu); assert mu < 0
    return arb.fac_ui(p) / (-mu) ** (p + 1)


def integrate_ep(ep, kind, h=None):
    """int of an ExpPoly: kind 'cell' over [0, h] (returns exact value), 'minf' over (-oo, 0], 'pinf' over [0, oo)."""
    tot = arb(0)
    for e, c in ep.terms.items():
        ea = q2arb(e)
        for p, cp in enumerate(c):
            if cp == 0: continue
            if kind == "cell":
                m = moment_right(ea, p, h) if ea <= 0 else (ea * arb(h)).exp() * moment_left(ea, p, h)
            elif kind == "minf": m = moment_minf(ea, p)
            else: m = moment_pinf(ea, p)
            tot += cp * m
    return tot


# ---------- exact B-spline cell polynomials ----------
def bspline_cell_polys(knots_q, p, cells_idx):
    """For each cell index ci (interval [knots[ci+p], knots[ci+p+1]] in the clamped knot vector), the degree-p polynomials (fmpq_poly in
    the LOCAL variable sigma = t - t_a) of the p+1 active B-splines B_{ci}, ..., B_{ci+p}. Returns list of lists of fmpq_poly."""
    out = []
    x = fmpq_poly([0, 1])
    for ci in cells_idx:
        a = knots_q[ci + p]; b = knots_q[ci + p + 1]
        assert b > a
        # Cox-de Boor in the local variable: t = a + sigma; B_{i,0} = 1 on this cell for i = ci+p, else 0
        # level q polynomials for i = ci+p-q .. ci+p
        cur = {ci + p: fmpq_poly([1])}
        for q in range(1, p + 1):
            new = {}
            for i in range(ci + p - q, ci + p + 1):
                poly = fmpq_poly([0])
                d1 = knots_q[i + q] - knots_q[i]
                if d1 != 0 and i in cur: poly += cur[i] * (fmpq_poly([a - knots_q[i]]) + x) / d1
                d2 = knots_q[i + q + 1] - knots_q[i + 1]
                if d2 != 0 and (i + 1) in cur: poly += cur[i + 1] * (fmpq_poly([knots_q[i + q + 1] - a]) - x) / d2
                new[i] = poly
            cur = new
        out.append([cur[i] for i in range(ci, ci + p + 1)])
    return out


class ExactTrial:
    def __init__(self, path=EXACT_JSON, prec=PREC, verbose=True):
        ctx.prec = prec; self.prec = prec
        t0 = time.time()
        d = json.load(lzma.open(path))
        self.sha = d["source_npz_sha256"]
        sc = d["scalars_hex"]
        self.k_q = hexq(sc["k"]); self.L_q = hexq(sc["L"]); self.bi_q = hexq(sc["bi"]); self.bo_q = hexq(sc["bo"])
        self.k = q2arb(self.k_q); self.L = q2arb(self.L_q); self.bi = q2arb(self.bi_q); self.bo = q2arb(self.bo_q)
        self.p = int(d["degree"]); assert self.p == 7
        self.outer_jl = [tuple(x) for x in d["outer_jl"]]
        A = d["arrays"]
        M, nb = A["S"]["shape"]; self.M = M; self.nb = nb
        self.knots_q = [hexq(s) for s in A["knots"]["hex"]]
        assert len(self.knots_q) == nb + self.p + 1
        self.t_lo_q = self.knots_q[0]; self.t_hi_q = self.knots_q[-1]
        assert all(self.knots_q[i] == self.t_lo_q for i in range(self.p + 1)) and all(self.knots_q[-1 - i] == self.t_hi_q for i in range(self.p + 1))
        self.t_lo = q2arb(self.t_lo_q); self.t_hi = q2arb(self.t_hi_q)
        S_hex = A["S"]["hex"]; self.S_q = [[hexq(S_hex[m * nb + i]) for i in range(nb)] for m in range(M)]
        D_hex = A["D"]["hex"]; nD = A["D"]["shape"][1]; self.D_q = [[hexq(D_hex[m * nD + j]) for j in range(nD)] for m in range(M)]
        Ao_hex = A["Aout"]["hex"]; nA = A["Aout"]["shape"][1]; self.Aout_q = [[hexq(Ao_hex[m * nA + q]) for q in range(nA)] for m in range(M)]
        self.NIN = nD; self.NOUT = nA; self.NCOR = 7
        self.alpha_q = [(self.k_q - 3) - j * (1 - self.k_q) - 2 * l for (j, l) in self.outer_jl]
        assert all(a < -2 for a in self.alpha_q) and self.alpha_q[0] + self.bo_q > 0 and self.bi_q > 4
        # cells: interior distinct knots (simple) -> boundaries tb_q
        inner_knots = self.knots_q[self.p + 1:-(self.p + 1)]
        assert all(inner_knots[i] < inner_knots[i + 1] for i in range(len(inner_knots) - 1))
        self.tb_q = [self.t_lo_q] + inner_knots + [self.t_hi_q]
        self.nc = len(self.tb_q) - 1
        self.tb = [q2arb(q) for q in self.tb_q]
        self.h_q = [self.tb_q[i + 1] - self.tb_q[i] for i in range(self.nc)]
        # z enclosure (uniform): arb from the two decimal bounds
        zlo = arb(Z_LO); zhi = arb(Z_HI)
        mid = (zlo + zhi) / 2; rad = (zhi - zlo) / 2
        self.z = arb(mid.mid(), float(rad.upper()) * 1.01 + float(mid.rad()) * 2 + 1e-60)
        assert self.z.contains(zlo) and self.z.contains(zhi)
        if verbose: print("loaded exact trial: M=%d nb=%d cells=%d  t_-=%s t_+=%s  (%.1fs)" % (M, nb, self.nc, self.t_lo.str(20), self.t_hi.str(20), time.time() - t0), flush=True)
        # exact cell polynomials of the B-splines (local variable), then a_m per cell as arb coefficient rows
        t0 = time.time()
        cellpolys = bspline_cell_polys(self.knots_q, self.p, range(self.nc))
        self.cell_T = []        # per cell: fmpq_mat (p+1) x (p+1): Taylor coeff (row) of active spline (col)
        for ci in range(self.nc):
            T = fmpq_mat(self.p + 1, self.p + 1)
            for b, poly in enumerate(cellpolys[ci]):
                cs = poly.coeffs()
                for r_, cq in enumerate(cs): T[r_, b] = cq
            self.cell_T.append(T)
        if verbose: print("exact B-spline cell polynomials: %.1fs" % (time.time() - t0), flush=True)
        # a_m on each cell: coefficient arb_mat (p+1) x M = T (p+1 x p+1) * Sblock (p+1 x M); exact in fmpq then converted
        t0 = time.time()
        self.cell_a = []        # list of (p+1) x M arb_mat
        for ci in range(self.nc):
            Sblk = fmpq_mat(self.p + 1, M)
            for b in range(self.p + 1):
                for m in range(M): Sblk[b, m] = self.S_q[m][ci + b]
            C = self.cell_T[ci] * Sblk
            self.cell_a.append(arb_mat(self.p + 1, M, [q2arb(C[r_, c_]) for r_ in range(self.p + 1) for c_ in range(M)]))
        if verbose: print("a_m cell coefficients (exact -> arb): %.1fs" % (time.time() - t0), flush=True)
        # exact join coefficients Ei, Eo (6-jet matching) and the scalar repair
        self._joins()
        # sine projection matrix P (M+1 x M), exact rationals: R_j = sum_m P_jm a_m
        self.Mj = M + 1; self.Nf = M + 1
        P = fmpq_mat(self.Mj, M)
        for m in range(M):
            for f, sg in ((1 + 2 * m, 1), (1 - 2 * m, 1), (3 + 2 * m, 1), (3 - 2 * m, 1)):
                if f < 0: f, sg = -f, -sg
                if f == 0: continue
                j = (f - 1) // 2
                if j < self.Mj: P[j, m] += fmpq(sg, 8)
        self.P_q = P
        self.P = arb_mat(self.Mj, M, [q2arb(P[r_, c_]) for r_ in range(self.Mj) for c_ in range(M)])

    @classmethod
    def from_npz(cls, path, prec=PREC, verbose=True):
        """Fixture loader: all stored doubles exact, stored Ei/Eo/Aout used literally (no exact joins), z = 0."""
        import numpy as np
        d = np.load(path)
        obj = cls.__new__(cls); ctx.prec = prec; obj.prec = prec
        def fq(x):
            f = Fraction(float(x)); return fmpq(f.numerator, f.denominator)
        obj.sha = "npz:" + os.path.basename(path)
        obj.k_q = fq(d["k"]); obj.L_q = fq(d["L"]); obj.bi_q = fq(d["bi"]); obj.bo_q = fq(d["bo"])
        obj.k = q2arb(obj.k_q); obj.L = q2arb(obj.L_q); obj.bi = q2arb(obj.bi_q); obj.bo = q2arb(obj.bo_q)
        obj.p = int(d["p"]); obj.outer_jl = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (0, 1), (1, 1), (2, 1), (0, 2)]
        S = d["S"]; M, nb = S.shape; obj.M = M; obj.nb = nb
        obj.knots_q = [fq(x) for x in d["knots"]]
        obj.t_lo_q = obj.knots_q[0]; obj.t_hi_q = obj.knots_q[-1]; obj.t_lo = q2arb(obj.t_lo_q); obj.t_hi = q2arb(obj.t_hi_q)
        obj.S_q = [[fq(x) for x in row] for row in S]; obj.D_q = [[fq(x) for x in row] for row in d["D"]]
        obj.Aout_q = [[fq(x) for x in row] for row in d["Aout"]]
        obj.Ei_q = [[fq(x) for x in row] for row in d["Ei"]]; obj.Eo_q = [[fq(x) for x in row] for row in d["Eo"]]
        obj.NIN = d["D"].shape[1]; obj.NOUT = d["Aout"].shape[1]; obj.NCOR = d["Ei"].shape[1]
        obj.alpha_q = [(obj.k_q - 3) - j * (1 - obj.k_q) - 2 * l for (j, l) in obj.outer_jl]
        inner_knots = obj.knots_q[obj.p + 1:-(obj.p + 1)]
        obj.tb_q = [obj.t_lo_q] + inner_knots + [obj.t_hi_q]; obj.nc = len(obj.tb_q) - 1
        obj.tb = [q2arb(q) for q in obj.tb_q]; obj.h_q = [obj.tb_q[i + 1] - obj.tb_q[i] for i in range(obj.nc)]
        obj.z = arb(0); obj.zB_coef = [fmpq(0)] * obj.NCOR
        cellpolys = bspline_cell_polys(obj.knots_q, obj.p, range(obj.nc))
        obj.cell_T = []
        for ci in range(obj.nc):
            T = fmpq_mat(obj.p + 1, obj.p + 1)
            for b, poly in enumerate(cellpolys[ci]):
                for r_, cq in enumerate(poly.coeffs()): T[r_, b] = cq
            obj.cell_T.append(T)
        obj.cell_a = []
        for ci in range(obj.nc):
            Sblk = fmpq_mat(obj.p + 1, M)
            for b in range(obj.p + 1):
                for m in range(M): Sblk[b, m] = obj.S_q[m][ci + b]
            C = obj.cell_T[ci] * Sblk
            obj.cell_a.append(arb_mat(obj.p + 1, M, [q2arb(C[r_, c_]) for r_ in range(obj.p + 1) for c_ in range(M)]))
        obj.Mj = M + 1; obj.Nf = M + 1
        P = fmpq_mat(obj.Mj, M)
        for m in range(M):
            for f, sg in ((1 + 2 * m, 1), (1 - 2 * m, 1), (3 + 2 * m, 1), (3 - 2 * m, 1)):
                if f < 0: f, sg = -f, -sg
                if f == 0: continue
                j = (f - 1) // 2
                if j < obj.Mj: P[j, m] += fmpq(sg, 8)
        obj.P_q = P; obj.P = arb_mat(obj.Mj, M, [q2arb(P[r_, c_]) for r_ in range(obj.Mj) for c_ in range(M)])
        if verbose: print("loaded npz fixture: M=%d nb=%d cells=%d" % (M, nb, obj.nc), flush=True)
        return obj

    # ---- joins ----
    def _spline_jet(self, ci, side):
        """exact jet (derivatives 0..p in t) of all a_m at the left (side=0) or right (side=1) end of cell ci: fmpq_mat (p+1) x M"""
        Sblk = fmpq_mat(self.p + 1, self.M)
        for b in range(self.p + 1):
            for m in range(self.M): Sblk[b, m] = self.S_q[m][ci + b]
        C = self.cell_T[ci] * Sblk            # Taylor coefficients in sigma
        J = fmpq_mat(self.p + 1, self.M)
        if side == 0:
            for n in range(self.p + 1):
                for m in range(self.M): J[n, m] = C[n, m] * math.factorial(n)
        else:
            h = self.h_q[ci]
            for n in range(self.p + 1):
                for m in range(self.M):
                    s = fmpq(0)
                    for q in range(n, self.p + 1):
                        s += C[q, m] * (math.factorial(q) // math.factorial(q - n)) * h ** (q - n)
                    J[n, m] = s
        return J

    def _joins(self):
        """Ei (inner) and Eo (outer) exact: E_i = sum_{j<=i} (-b)^(i-j) (J_j - P_j)/((i-j)! j!), b = bi (inner), b = -bo (outer)."""
        t0 = time.time()
        Jin = self._spline_jet(0, 0); Jout = self._spline_jet(self.nc - 1, 1)
        M = self.M; NC = self.NCOR
        self.Ei_q = [[fmpq(0)] * NC for _ in range(M)]; self.Eo_q = [[fmpq(0)] * NC for _ in range(M)]
        for m in range(M):
            # non-correction inner jets: delta_m0 + sum_j D_mj e^{2j tau}: derivative n at tau=0: delta_m0 [n=0] + sum_j D_mj (2j)^n
            Pin = [(fmpq(1) if (m == 0 and n == 0) else fmpq(0)) + sum((self.D_q[m][j - 1] * fmpq(2 * j) ** n for j in range(1, self.NIN + 1)), fmpq(0)) for n in range(NC)]
            Pout = [sum((self.Aout_q[m][q] * self.alpha_q[q] ** n for q in range(self.NOUT)), fmpq(0)) for n in range(NC)]
            for i in range(NC):
                si = fmpq(0); so = fmpq(0)
                for j in range(i + 1):
                    den = math.factorial(i - j) * math.factorial(j)
                    si += (-self.bi_q) ** (i - j) * (Jin[j, m] - Pin[j]) / den
                    so += (self.bo_q) ** (i - j) * (Jout[j, m] - Pout[j]) / den      # b = -bo: (-b)^(i-j) = bo^(i-j)
                self.Ei_q[m][i] = si; self.Eo_q[m][i] = so
        # scalar repair: A_00 -> A_00 + z changes mode 0 outer by z * B(tau), B = e^{alpha_0 tau} - e^{-bo tau} sum_i ((alpha_0+bo) tau)^i / i!
        # i.e. Eo_0i -> Eo_0i - z (alpha_0 + bo)^i / i!   (exact consequence of the jet formula, since the jets of z e^{alpha_0 tau} are z alpha_0^n)
        self.zB_coef = [(self.alpha_q[0] + self.bo_q) ** i / math.factorial(i) for i in range(NC)]
        print("exact joins Ei, Eo computed (%.1fs); max |Ei| %.3e, max |Eo| %.3e" % (time.time() - t0, max(abs(float(x)) for r in self.Ei_q for x in r), max(abs(float(x)) for r in self.Eo_q for x in r)), flush=True)

    # ---- exp-poly representation of a_m on the three kinds of cells ----
    def a_inner(self):
        """list over m of ExpPoly in tau = t - t_- <= 0"""
        out = []
        for m in range(self.M):
            ep = ExpPoly()
            if m == 0: ep.add(fmpq(0), [arb(1)])
            for j in range(1, self.NIN + 1): ep.add(fmpq(2 * j), [q2arb(self.D_q[m][j - 1])])
            ep.add(self.bi_q, [q2arb(x) for x in self.Ei_q[m]])
            out.append(ep)
        return out

    def a_outer(self):
        """list over m of ExpPoly in tau = t - t_+ >= 0 (with the exact scalar repair z in mode 0)"""
        out = []
        for m in range(self.M):
            ep = ExpPoly()
            for q in range(self.NOUT):
                coef = q2arb(self.Aout_q[m][q])
                if m == 0 and q == 0: coef = coef + self.z
                ep.add(self.alpha_q[q], [coef])
            eo = [q2arb(x) for x in self.Eo_q[m]]
            if m == 0: eo = [eo[i] - self.z * q2arb(self.zB_coef[i]) for i in range(self.NCOR)]
            ep.add(-self.bo_q, eo)
            out.append(ep)
        return out

    def a_cell(self, ci):
        """list over m of ExpPoly (pure polynomials) on cell ci"""
        C = self.cell_a[ci]
        return [ExpPoly([(fmpq(0), [C[r_, m] for r_ in range(self.p + 1)])]) for m in range(self.M)]

    # ---- sine modes: R_j (without the e^{3t} factor): Rhat_j = sum_m P_jm a_m ; f_n = e^{2t} * fhat_n ----
    def Rhat_from_a(self, a_list):
        """a_list: list over m of ExpPoly -> list over j of ExpPoly (Rhat_j = sum_m P_jm a_m)"""
        out = []
        for j in range(self.Mj):
            ep = ExpPoly()
            for m in range(self.M):
                pq = self.P_q[j, m]
                if pq != 0: ep = ep + a_list[m].scale(q2arb(pq))
            out.append(ep)
        return out

    def fhat_from_Rhat(self, Rhat):
        """f_n(t) = e^{2 t_a} e^{2 sigma} fhat_n(sigma), fhat_n = (1/2)[(3 + d/dsigma) Rhat_{n-1} - (2n-1) Rhat_{n-1} + (3 + d/dsigma) Rhat_n + (2n+1) Rhat_n]
        (R_j = e^{3t} Rhat_j, dR_j/dt = e^{3t}(3 Rhat_j + Rhat_j')). Returns list over n = 1..Nf (index n-1)."""
        out = []
        for n in range(1, self.Nf + 1):
            jl = n - 1; ju = n
            ep = ExpPoly()
            Rl = Rhat[jl]; ep = ep + Rl.scale(arb(3 - (2 * n - 1))) + Rl.deriv()
            if ju < self.Mj:
                Ru = Rhat[ju]; ep = ep + Ru.scale(arb(3 + (2 * n + 1))) + Ru.deriv()
            out.append(ep.scale(arb(1) / 2))
        return out

    # ---- Green boundary values ----
    def build_green(self, verbose=True):
        """A_n(tb_i), B_n(tb_i) for n = 1..Nf at all nc+1 boundaries (lists of arb lists), and the strain c."""
        t0 = time.time()
        Nf = self.Nf; nc = self.nc
        # inner start: A_n(t_-) = e^{4 t_-} int_{-oo}^0 e^{(2n+4) tau} fhat_n^in(tau) dtau
        fin = self.fhat_from_Rhat(self.Rhat_from_a(self.a_inner()))
        e4lo = (4 * self.t_lo).exp(); e4hi = (4 * self.t_hi).exp()
        A = [[None] * Nf for _ in range(nc + 1)]; B = [[None] * Nf for _ in range(nc + 1)]
        for n in range(1, Nf + 1):
            A[0][n - 1] = e4lo * integrate_ep(fin[n - 1].mul_exp(fmpq(2 * n + 4)), "minf")
        fout = self.fhat_from_Rhat(self.Rhat_from_a(self.a_outer()))
        for n in range(1, Nf + 1):
            B[nc][n - 1] = e4hi * integrate_ep(fout[n - 1].mul_exp(fmpq(4 - 2 * n)), "pinf")
        # head of the strain integral: (1/2) int_{-oo}^{t_-} f_1 dt = (1/2) e^{2 t_-} int_{-oo}^0 e^{2 tau} fhat_1 dtau
        head = (2 * self.t_lo).exp() * integrate_ep(fin[0].mul_exp(fmpq(2)), "minf") / 2
        tail = (2 * self.t_hi).exp() * integrate_ep(fout[0].mul_exp(fmpq(2)), "pinf") / 2
        if verbose: print("inner/outer starts: %.1fs" % (time.time() - t0), flush=True)
        # cells: need per cell the polynomial fhat_n (degree <= 7) for all n: build via arb_mat algebra for speed
        # Rhat coefficients: (p+1) x Mj = cell_a (p+1 x M) * P^T  -> then fhat_n coefficients by the formula
        self.cell_fhat = []
        mid_int = arb(0)
        for ci in range(nc):
            Rc = self.cell_a[ci] * self.P.transpose()          # (p+1) x Mj ; Rhat_j(sigma) = sum_r Rc[r,j] sigma^r
            pp = self.p
            # derivative coefficients: dRc[r, j] = (r+1) Rc[r+1, j]
            F = [[arb(0)] * (pp + 1) for _ in range(Nf)]        # F[n-1][r]
            for n in range(1, Nf + 1):
                jl, ju = n - 1, n
                for r_ in range(pp + 1):
                    v = (3 - (2 * n - 1)) * Rc[r_, jl]
                    if r_ + 1 <= pp: v += (r_ + 1) * Rc[r_ + 1, jl]
                    if ju < self.Mj:
                        v += (3 + (2 * n + 1)) * Rc[r_, ju]
                        if r_ + 1 <= pp: v += (r_ + 1) * Rc[r_ + 1, ju]
                    F[n - 1][r_] = v / 2
            self.cell_fhat.append(F)
            h = q2arb(self.h_q[ci]); ta = self.tb[ci]; tbb = self.tb[ci + 1]
            e4a = (4 * ta).exp(); e4b = (4 * tbb).exp()
            # A_n(t_b) = e^{-2nh} A_n(t_a) + e^{4 t_b} int_0^h e^{(2n+4)(sigma-h)} fhat_n ; B done in a second backward pass
            for n in range(1, Nf + 1):
                lam = arb(2 * n + 4)
                mom = arb(0)
                for r_ in range(pp + 1):
                    if F[n - 1][r_] != 0: mom += F[n - 1][r_] * moment_left(lam, r_, h)
                A[ci + 1][n - 1] = (-2 * n * h).exp() * A[ci][n - 1] + e4b * mom
            # strain middle part: (1/2) int_{t_a}^{t_b} f_1 dt = (1/2) e^{2 t_a} int_0^h e^{2 sigma} fhat_1
            mom1 = arb(0)
            for r_ in range(pp + 1):
                if F[0][r_] != 0: mom1 += F[0][r_] * moment_right(arb(2), r_, h)
            mid_int += (2 * ta).exp() * mom1 / 2
            if verbose and (ci + 1) % 200 == 0: print("  forward cells %d/%d (%.0fs)" % (ci + 1, nc, time.time() - t0), flush=True)
        for ci in range(nc - 1, -1, -1):
            F = self.cell_fhat[ci]; h = q2arb(self.h_q[ci]); ta = self.tb[ci]; e4a = (4 * ta).exp(); pp = self.p
            for n in range(1, Nf + 1):
                mu = arb(4 - 2 * n)
                mom = arb(0)
                for r_ in range(pp + 1):
                    if F[n - 1][r_] != 0: mom += F[n - 1][r_] * moment_right(mu, r_, h)
                B[ci][n - 1] = (-2 * n * h).exp() * B[ci + 1][n - 1] + e4a * mom
        self.A, self.B = A, B
        self.c_head, self.c_mid, self.c_tail = head, mid_int, tail
        self.c = head + mid_int + tail
        # consistency: c = (1/2)[head*2 + e^{-2 t_-} B_1(t_-)]  (B_1(t_-) = e^{2 t_-} int_{t_-}^oo f_1 dt)
        self.c_alt = head + (-2 * self.t_lo).exp() * B[0][0] / 2
        if verbose: print("Green boundary values done: %.1fs; c = %s ; alt %s" % (time.time() - t0, self.c.str(40, radius=True), self.c_alt.str(40, radius=True)), flush=True)
        return A, B

    def c_from_cosine_modes(self):
        """normalization identity c = int_0^oo r (a_0/4 + a_1/8 - a_2/8 - a_3/8) dr = int e^{2t} (...) dt"""
        w = [fmpq(1, 4), fmpq(1, 8), fmpq(-1, 8), fmpq(-1, 8)]
        ain = self.a_inner(); aout = self.a_outer()
        tot = arb(0)
        for m in range(4):
            tot += q2arb(w[m]) * ((2 * self.t_lo).exp() * integrate_ep(ain[m].mul_exp(fmpq(2)), "minf") + (2 * self.t_hi).exp() * integrate_ep(aout[m].mul_exp(fmpq(2)), "pinf"))
        for ci in range(self.nc):
            C = self.cell_a[ci]; h = q2arb(self.h_q[ci]); e2a = (2 * self.tb[ci]).exp()
            for m in range(4):
                s = arb(0)
                for r_ in range(self.p + 1):
                    if C[r_, m] != 0: s += C[r_, m] * moment_right(arb(2), r_, h)
                tot += q2arb(w[m]) * e2a * s
        return tot


if __name__ == "__main__":
    T = ExactTrial()
    print("k =", T.k.str(30), " 3/k - 1 =", (3 / T.k - 1).str(40, radius=True))
    # check cell polynomials against float scipy
    import numpy as np
    from scipy.interpolate import BSpline
    kn = np.array([float(q) for q in T.knots_q]); S = np.array([[float(x) for x in row] for row in T.S_q])
    spl = BSpline(kn, S.T, 7, extrapolate=False)
    rng = np.random.default_rng(3); err = 0.0
    for ci in rng.integers(0, T.nc, 20):
        ta = float(T.tb_q[ci]); h = float(T.h_q[ci]); s = rng.uniform(0, h)
        ref = spl(ta + s)
        C = T.cell_a[ci]
        for m in (0, 1, 7, 100, 259):
            v = sum(float(C[r_, m]) * s ** r_ for r_ in range(8))
            err = max(err, abs(v - ref[m]) / (1 + abs(ref[m])))
    print("cell polynomial check vs scipy: max rel err %.2e" % err)
    T.build_green()
    print("c (Green)        =", T.c.str(45, radius=True))
    print("c (alt via B_1)  =", T.c_alt.str(45, radius=True))
    cc = T.c_from_cosine_modes()
    print("c (cosine modes) =", cc.str(45, radius=True))
    print("target 3/k - 1   =", (3 / T.k - 1).str(45, radius=True))
    print("c - target       =", (T.c - (3 / T.k - 1)).str(10, radius=True))
