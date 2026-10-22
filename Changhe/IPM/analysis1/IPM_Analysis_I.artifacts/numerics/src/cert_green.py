"""Arb certificate, part 1: exact definition of the trial and rigorous Green boundary values.

(1) Exactification. Stored floats: knots, S (M x nb), D (M x 7), Aout (M x 10), bi, bo, k, L, rmin, R0.  Defined exactly
    from them (ball arithmetic at PREC bits): Ei (M x 7) and Eo (M x 7) by the C^6 join equations at tmin and t0, and
    A_00 (leading far-field coefficient of mode 0) by c[rho~] = 3/k - 1.  The stored Ei, Eo, A_00 are only initial guesses.
(2) Green boundary values A_n(tb_i), B_n(tb_i) (n = 1..Nf = M+1) at all cell boundaries by the exact closed-form
    recurrences (primitive of e^{lam tau} tau^j; cancellation is harmless at PREC bits), and c = (1/2) int f_1/s ds.
Output: data/cert_green.npz with mid/rad arrays (float64) of all quantities plus the exactified coefficients as
decimal strings (60 digits) in data/cert_coeffs.json.
Usage: python3 cert_green.py trial.npz [PREC=256] [hsub=0.0019] [out_prefix=data/cert]   (writes <out_prefix>_green.npz; hsub = radial sub-cell length in t = log r)
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, arb_mat, ctx
from math import factorial
from cert_spline import SplineCells
from modal_fit import OUTER_JL, NIN, NCOR, NOUT

W_NORM = [arb(1) / 4, arb(1) / 8, -arb(1) / 8, -arb(1) / 8]     # c = sum_m W_m int_0^oo r a_m dr


def ball_dyadic(x):
    """Exact dyadic export of an arb ball: midpoint = man * 2^exp (fmpz), radius upper bound = rman * 2^rexp (fmpz)."""
    man, exp = x.mid().man_exp(); rman, rexp = x.rad().man_exp()
    return dict(man=str(man), exp=str(exp), rman=str(rman), rexp=str(rexp))


def load_ball(entry):
    """Re-create an enclosing arb ball from an exported entry. Formats: dict (exact dyadic, lossless: the midpoint is exact and
    the radius is reproduced exactly, then rounded upward when converted); [mid_str, rad_up_str] (legacy, 100 digits + radius
    upper bound); plain string (legacy 60 digits, not an enclosure: widened by 1e-58 relative and flagged)."""
    from flint import fmpz
    if isinstance(entry, dict):
        with_prec = ctx.prec
        ctx.prec = max(with_prec, 1200)
        mid = arb(fmpz(int(entry["man"]))) * (arb(2) ** int(entry["exp"]))
        rad = arb(fmpz(int(entry["rman"]))) * (arb(2) ** int(entry["rexp"])) if int(entry["rman"]) != 0 else arb(0)
        ctx.prec = with_prec
        out = mid + arb(0, float(rad.upper()) * (1 + 2.0 ** -50) + (2.0 ** -1070 if rad != 0 else 0.0))
        return out
    if isinstance(entry, str):
        a = arb(entry); return a + arb(0, 1e-58 * (abs(float(a.mid())) + 1e-300))
    mid, rad = entry
    return arb(mid) + arb(0, float(rad))


def prim_S(lam, coeffs, tau):
    """S(tau) with int e^{lam s} p(s) ds = e^{lam tau} S(tau) (lam != 0) ; polynomial primitive if lam == 0. arb scalars."""
    out = arb(0)
    for j, c in enumerate(coeffs):
        if c == 0: continue
        if lam == 0:
            out += c * tau ** (j + 1) / (j + 1)
        else:
            s = arb(0)
            for l in range(j + 1):
                s += (-1) ** l * (arb(factorial(j)) / factorial(j - l)) * tau ** (j - l) / lam ** (l + 1)
            out += c * s
    return out


def integ_series(lam, coeffs, a, b, nterms=60):
    """int_a^b e^{lam s} p(s) ds by the convergent series sum_j c_j sum_{m>=0} lam^m (b^{j+m+1} - a^{j+m+1}) / (m! (j+m+1)), finite
    interval, with a rigorous tail ball: for |lam| L <= 1 (L = max(|a|,|b|)) the tail after m = nterms is bounded by
    sum_j |c_j| L^{j+1} e (|lam| L)^{nterms+1} / (nterms+1)!.  Used when the closed primitive would cancel catastrophically (|lam| small)."""
    L = arb(max(float(abs(a).upper()), float(abs(b).upper()))) * (1 + arb(2) ** -50)     # enclosing maximum of the two absolute upper endpoints
    x = abs(lam) * L
    assert x <= 1, "series branch needs |lam| L <= 1"
    tot = arb(0); fact = arb(1); lam_m = arb(1)
    for m in range(nterms + 1):
        if m > 0: fact *= m; lam_m *= lam
        for j, c in enumerate(coeffs):
            if c == 0: continue
            tot += c * lam_m * (b ** (j + m + 1) - a ** (j + m + 1)) / (fact * (j + m + 1))
    tail = arb(0)
    fN = fact * (nterms + 1)
    for j, c in enumerate(coeffs):
        tail += abs(c) * L ** (j + 1)
    tail = tail * arb(1).exp() * x ** (nterms + 1) / fN
    return tot + arb(0, 1) * tail                      # the tail stays an Arb ball (no float conversion / underflow)


def integ_scaled(lam, coeffs, a, b, extra):
    """exp(extra) * int_a^b e^{lam s} p(s) ds  (a may be -inf if lam > 0, b may be +inf if lam < 0), arb.  Computed as
    exp(extra + lam*sh) [e^{lam (b - sh)} S(b) - e^{lam (a - sh)} S(a)] with sh = b (lam > 0) or a (lam <= 0); for finite
    intervals with |lam| max(|a|,|b|) < 1/2 the series form (integ_series) is used instead (the closed primitive cancels
    catastrophically for small |lam|, e.g. mu = 2 - 2n + alpha' ~ 1e-14 when alpha' is a non-integer double)."""
    fin_a = not (isinstance(a, float) and np.isinf(a)); fin_b = not (isinstance(b, float) and np.isinf(b))
    if fin_a and fin_b:
        L = arb(max(float(abs(a).upper()), float(abs(b).upper()))) * (1 + arb(2) ** -50)
        if lam == 0 or abs(lam) * L < arb(1) / 2:
            return arb(extra).exp() * integ_series(lam, coeffs, a, b)
    if lam == 0:
        return arb(extra).exp() * (prim_S(lam, coeffs, b) - prim_S(lam, coeffs, a))
    sh = b if lam > 0 else a
    up = arb(0) if (b == arb.pos_inf() or (isinstance(b, float) and np.isinf(b))) else (lam * (b - sh)).exp() * prim_S(lam, coeffs, b)
    lo = arb(0) if (isinstance(a, float) and np.isinf(a)) else (lam * (a - sh)).exp() * prim_S(lam, coeffs, a)
    return (extra + lam * sh).exp() * (up - lo)


class Cert:
    def __init__(self, path, prec=256, hsub=0.0):
        ctx.prec = prec; self.prec = prec
        d = np.load(path); self.d = d
        self.k = arb(float(d["k"])); self.L = arb(float(d["L"])); self.c_l = 1 / self.k
        self.knots_f = d["knots"]; self.p = int(d["p"]); self.M = int(d["S"].shape[0])
        # DEFINITION: the join abscissae are the stored float knots tmin = knots[0], t0 = knots[-1] (exact doubles);
        # rmin = e^{tmin}, R0 = e^{t0} are derived (verifier objection 2026-10-20T14:15Z: the physical pieces must be joined
        # at the same t as the spline ends).
        self.tmin = arb(float(self.knots_f[0])); self.t0 = arb(float(self.knots_f[-1]))
        self.rmin = self.tmin.exp(); self.R0 = self.t0.exp()
        self.S_f = d["S"]; self.D_f = d["D"]; self.Aout_f = d["Aout"]; self.Ei_f = d["Ei"]; self.Eo_f = d["Eo"]
        self.bi = arb(float(d["bi"])); self.bo = arb(float(d["bo"]))
        self.alpha = [(self.k - 3) - j * (1 - self.k) - 2 * l for (j, l) in OUTER_JL]
        self.sc = SplineCells(self.knots_f, self.p, self.S_f)
        self.hsub = hsub
        # sub-cells: every spline cell [t_j, t_{j+1}) split into ceil(h / hsub) equal parts (exact arb boundaries)
        self.parent = []; self.tb = []; self.offs = []
        for ci, j in enumerate(self.sc.cell_j):
            ta, tbb = self.sc.knots[j], self.sc.knots[j + 1]; h = tbb - ta
            ns = int(np.ceil(float(h.mid()) / hsub - 1e-12)) if hsub else 1
            for s_ in range(ns):
                self.tb.append(ta + h * s_ / ns); self.parent.append(ci); self.offs.append(h * s_ / ns)
        self.tb.append(self.sc.knots[self.sc.cell_j[-1] + 1])
        self.nc = len(self.tb) - 1
        self._parent_cache = {}
        self.D = [[arb(float(x)) for x in row] for row in self.D_f]
        self.A = [[arb(float(x)) for x in row] for row in self.Aout_f]
        self.Nf = self.M + 1

    # ---------- modal algebra (same conventions as trial_green) ----------
    def R_from_a(self, a):
        """a: list of M arb -> list of M+1 arb (coefficient of sin((2j+1)theta))."""
        M = self.M; R = [arb(0)] * (M + 1)
        def add(freq, coef):
            if freq < 0: freq, coef = -freq, -coef
            if freq == 0: return
            j = (freq - 1) // 2
            if j <= M: R[j] += coef
        for m in range(M):
            am = a[m] / 8
            add(2 * m + 1, am); add(-(2 * m - 1), am); add(2 * m + 3, am); add(-(2 * m - 3), am)
        return R

    def f_terms(self, terms_a, e2ta):
        """[(alpha, coeffs: list over power of list over M)] -> [(alpha + 2, coeffs: list over power of list over Nf)], times e^{2 t_a}."""
        out = []
        for alpha, c in terms_a:
            deg = len(c) - 1
            Rc = [self.R_from_a(c[q]) for q in range(deg + 1)]                    # (deg+1) x (M+1)
            dRc = [[(3 + alpha) * Rc[q][j] + (Rc[q + 1][j] * (q + 1) if q + 1 <= deg else arb(0)) for j in range(self.M + 1)] for q in range(deg + 1)]
            fc = [[arb(0)] * self.Nf for _ in range(deg + 1)]
            for q in range(deg + 1):
                for j in range(self.M + 1):
                    twoj1 = 2 * j + 1
                    up = (dRc[q][j] - twoj1 * Rc[q][j]) / 2; dn = (dRc[q][j] + twoj1 * Rc[q][j]) / 2
                    if j + 1 <= self.Nf: fc[q][j] += up
                    if j >= 1: fc[q][j - 1] += dn
            out.append((alpha + 2, [[v * e2ta for v in row] for row in fc]))
        return out

    def sub_taylor(self, ci):
        """Taylor coefficients [q][m] of a_m at the start of sub-cell ci (re-centred from the parent cell's expansion)."""
        pc = self.parent[ci]
        if pc not in self._parent_cache:
            if len(self._parent_cache) > 4: self._parent_cache.clear()
            self._parent_cache[pc] = self.sc.cell_taylor(pc)
        T = self._parent_cache[pc]; d = self.offs[ci]
        if d == 0: return T
        p = self.p; out = []
        for q in range(p + 1):
            row = []
            for m in range(self.M):
                v = arb(0)
                for pp in range(q, p + 1):
                    v += T[pp][m] * (arb(factorial(pp)) / (factorial(q) * factorial(pp - q))) * d ** (pp - q)
                row.append(v)
            out.append(row)
        return out

    # ---------- exactification ----------
    def spline_jets(self):
        """Taylor coefficients at tmin^+ (cell 0) and derivatives at t0^- (last cell's end) of a_m, nu = 0..6: lists [nu][m]."""
        T0 = self.sub_taylor(0)                                        # [nu][m] coefficients c_nu (= a^{(nu)}/nu!)
        jet_in = [[T0[nu][m] * factorial(nu) for m in range(self.M)] for nu in range(NCOR)]
        Tl = self.sub_taylor(self.nc - 1); h = self.tb[-1] - self.tb[-2]
        jet_out = []
        for nu in range(NCOR):
            row = []
            for m in range(self.M):
                v = arb(0)
                for q in range(nu, self.p + 1):
                    v += Tl[q][m] * (arb(factorial(q)) / factorial(q - nu)) * h ** (q - nu)
                row.append(v)
            jet_out.append(row)
        return jet_in, jet_out

    def solve_corrections(self, jet, powers_jet, b):
        """Solve for E_i (i=0..6): sum_i E_i d^nu/dtau^nu[e^{b tau} tau^i](0) = jet[nu] - powers_jet[nu], nu = 0..6.
        d^nu/dtau^nu [e^{b tau} tau^i] at 0 = nu!/(nu-i)! b^{nu-i} for i <= nu, else 0 (lower triangular)."""
        E = []
        for nu in range(NCOR):
            rhs = jet[nu] - powers_jet[nu]
            for i in range(nu):
                rhs -= E[i] * (arb(factorial(nu)) / factorial(nu - i)) * b ** (nu - i)
            E.append(rhs / factorial(nu))          # coefficient of tau^nu: nu!/(0)! b^0 = nu!
        return E

    def exactify(self):
        jet_in, jet_out = self.spline_jets()
        self.Ei = []; self.Eo = []
        for m in range(self.M):
            pin = [sum((self.D[m][j] * (2 * (j + 1)) ** nu for j in range(NIN)), arb(0)) + (arb(1) if (m == 0 and nu == 0) else arb(0)) for nu in range(NCOR)]
            self.Ei.append(self.solve_corrections([jet_in[nu][m] for nu in range(NCOR)], pin, self.bi))
            pout = [sum((self.A[m][q] * self.alpha[q] ** nu for q in range(NOUT)), arb(0)) for nu in range(NCOR)]
            self.Eo.append(self.solve_corrections([jet_out[nu][m] for nu in range(NCOR)], pout, -self.bo))
        # normalization: c is affine in A_00 (through Eo[0] as well). Compute c at the current A_00 and at A_00 + 1 (exact affine).
        c0 = self.c_functional()
        A00 = self.A[0][0]
        self.A[0][0] = A00 + 1
        pout = [sum((self.A[0][q] * self.alpha[q] ** nu for q in range(NOUT)), arb(0)) for nu in range(NCOR)]
        self.Eo[0] = self.solve_corrections([jet_out[nu][0] for nu in range(NCOR)], pout, -self.bo)
        c1 = self.c_functional()
        slope = c1 - c0
        target = 3 / self.k - 1
        A00_new = A00 + (target - c0) / slope
        self.A[0][0] = A00_new
        pout = [sum((self.A[0][q] * self.alpha[q] ** nu for q in range(NOUT)), arb(0)) for nu in range(NCOR)]
        self.Eo[0] = self.solve_corrections([jet_out[nu][0] for nu in range(NCOR)], pout, -self.bo)
        self.c_norm = self.c_functional()
        return dict(A00_old=float(A00.mid()), A00_new=A00_new, c_before=c0, c_after=self.c_norm, target=target)

    def inner_terms(self):
        """a_m on the inner region as [(alpha, coeffs [power][m])] in tau' = t - tmin <= 0."""
        terms = [(arb(0), [[arb(1) if m == 0 else arb(0) for m in range(self.M)]])]
        for j in range(NIN):
            terms.append((arb(2 * (j + 1)), [[self.D[m][j] for m in range(self.M)]]))
        terms.append((self.bi, [[self.Ei[m][i] for m in range(self.M)] for i in range(NCOR)]))
        return terms

    def outer_terms(self):
        terms = [(self.alpha[q], [[self.A[m][q] for m in range(self.M)]]) for q in range(NOUT)]
        terms.append((-self.bo, [[self.Eo[m][i] for m in range(self.M)] for i in range(NCOR)]))
        return terms

    def c_functional(self):
        """c = sum_m W_m int_0^oo r a_m dr = sum_m W_m [inner + spline cells + outer] of int e^{2t} a_m dt."""
        tot = arb(0)
        e2min = (2 * self.tmin).exp(); e20 = (2 * self.t0).exp()
        for alpha, c in self.inner_terms():
            for q in range(len(c)):
                unit = [arb(0)] * q + [arb(1)]
                I = integ_scaled(arb(2) + alpha, unit, -np.inf, arb(0), arb(0))   # int_{-inf}^0 e^{(2+alpha) tau} tau^q
                for m in range(4):
                    if c[q][m] != 0: tot += W_NORM[m] * c[q][m] * I * e2min
        for alpha, c in self.outer_terms():
            for q in range(len(c)):
                unit = [arb(0)] * q + [arb(1)]
                I = integ_scaled(arb(2) + alpha, unit, arb(0), np.inf, arb(0))
                for m in range(4):
                    if c[q][m] != 0: tot += W_NORM[m] * c[q][m] * I * e20
        for ci in range(self.nc):
            T = self.sub_taylor(ci); ta = self.tb[ci]; h = self.tb[ci + 1] - ta
            for m in range(4):
                coeffs = [T[q][m] for q in range(self.p + 1)]
                tot += W_NORM[m] * integ_scaled(arb(2), coeffs, arb(0), h, 2 * ta)
        return tot

    # ---------- Green boundary values ----------
    def green(self, verbose=True):
        Nf = self.Nf; nc = self.nc; tb = self.tb
        A = [[arb(0)] * Nf for _ in range(nc + 1)]; B = [[arb(0)] * Nf for _ in range(nc + 1)]
        t0 = time.time()
        self.inner_f = self.f_terms(self.inner_terms(), (2 * tb[0]).exp())
        for n in range(1, Nf + 1):
            acc = arb(0)
            for alpha, fc in self.inner_f:
                lam = 2 * n + 2 + alpha
                for q in range(len(fc)):
                    if fc[q][n - 1] != 0:
                        acc += fc[q][n - 1] * integ_scaled(lam, [arb(0)] * q + [arb(1)], -np.inf, arb(0), arb(0))
            A[0][n - 1] = acc * (2 * tb[0]).exp()
        self.cell_f = []; self.cell_T = []
        for ci in range(nc):
            ta, tbb = tb[ci], tb[ci + 1]; h = tbb - ta
            T = self.sub_taylor(ci)
            self.cell_T.append(T)
            ft = self.f_terms([(arb(0), [[T[q][m] for m in range(self.M)] for q in range(self.p + 1)])], (2 * ta).exp())
            self.cell_f.append(ft)
            e2n = None
            for n in range(1, Nf + 1):
                inc = arb(0)
                for alpha, fc in ft:
                    lam = 2 * n + 2 + alpha
                    coeffs = [fc[q][n - 1] for q in range(len(fc))]
                    inc += integ_scaled(lam, coeffs, arb(0), h, -2 * n * h)
                A[ci + 1][n - 1] = (-2 * n * h).exp() * A[ci][n - 1] + (2 * ta).exp() * inc
            if verbose and ci % 200 == 0:
                print("  forward cell %d/%d  (%.0fs)" % (ci, nc, time.time() - t0), flush=True)
        self.outer_f = self.f_terms(self.outer_terms(), (2 * tb[-1]).exp())
        for n in range(1, Nf + 1):
            acc = arb(0)
            for alpha, fc in self.outer_f:
                mu = 2 - 2 * n + alpha
                for q in range(len(fc)):
                    if fc[q][n - 1] != 0:
                        acc += fc[q][n - 1] * integ_scaled(mu, [arb(0)] * q + [arb(1)], arb(0), np.inf, arb(0))
            B[nc][n - 1] = acc * (2 * tb[-1]).exp()
        for ci in range(nc - 1, -1, -1):
            ta, tbb = tb[ci], tb[ci + 1]; h = tbb - ta
            for n in range(1, Nf + 1):
                inc = arb(0)
                for alpha, fc in self.cell_f[ci]:
                    mu = 2 - 2 * n + alpha
                    coeffs = [fc[q][n - 1] for q in range(len(fc))]
                    inc += integ_scaled(mu, coeffs, arb(0), h, arb(0))
                B[ci][n - 1] = (-2 * n * h).exp() * B[ci + 1][n - 1] + (2 * ta).exp() * inc
            if verbose and ci % 200 == 0:
                print("  backward cell %d/%d  (%.0fs)" % (ci, nc, time.time() - t0), flush=True)
        # c = (1/2)[int_{-inf}^{tmin} f_1 dt + e^{-2 tmin} B_1(tmin)]
        head = arb(0)
        for alpha, fc in self.inner_f:
            for q in range(len(fc)):
                if fc[q][0] != 0:
                    head += fc[q][0] * integ_scaled(alpha, [arb(0)] * q + [arb(1)], -np.inf, arb(0), arb(0))
        self.c_green = (head + B[0][0] * (-2 * tb[0]).exp()) / 2
        self.A, self.B = A, B
        return A, B


def main(path, prec=256, hsub=0.0, out_prefix="data/cert"):
    t0 = time.time()
    C = Cert(path, prec, hsub)
    print("sub-cells: %d (hsub %.4g)" % (C.nc, hsub), flush=True)
    info = C.exactify()
    print("exactification: A00 %.17g -> %s ; c before %s ; c after %s ; target %s" % (info["A00_old"], info["A00_new"].str(25), info["c_before"].str(20), info["c_after"].str(25), info["target"].str(25)), flush=True)
    dEi = max(abs(float(C.Ei[m][i].mid()) - C.Ei_f[m, i]) / (1e-300 + abs(C.Ei_f[m, i])) for m in range(C.M) for i in range(NCOR))
    dEo = max(abs(float(C.Eo[m][i].mid()) - C.Eo_f[m, i]) / (1e-300 + abs(C.Eo_f[m, i])) for m in range(C.M) for i in range(NCOR))
    print("relative change of Ei: %.2e, Eo: %.2e (vs stored floats); %.0fs" % (dEi, dEo, time.time() - t0), flush=True)
    A, B = C.green()
    print("Green done %.0fs; c_green = %s ; c_norm = %s ; 3c_l - 1 - c = %s" % (time.time() - t0, C.c_green.str(25), C.c_norm.str(25), (3 * C.c_l - 1 - C.c_green).str(5)), flush=True)
    def export(rows):
        """mid/rad doubles enclosing the balls: rad_out = succ(rad + u |mid| + eta) covers the mid->double rounding."""
        m = np.array([[float(x.mid()) for x in row] for row in rows]); r = np.array([[float(x.rad()) for x in row] for row in rows])
        r = np.nextafter(np.nextafter(np.nextafter(r, np.inf) + np.nextafter(2.0 ** -53 * np.abs(m), np.inf), np.inf) + 2.0 ** -1074, np.inf)
        return m, r
    Am, Ar = export(A); Bm, Br = export(B)
    print("max relative radius of A: %.2e, of B: %.2e" % ((Ar / np.maximum(np.abs(Am), 1e-300)).max(), (Br / np.maximum(np.abs(Bm), 1e-300)).max()))
    TT = [export(T) for T in C.cell_T]
    Tm = np.array([x[0] for x in TT]); Tr = np.array([x[1] for x in TT])
    tbm, tbr = export([C.tb]); cm_, cr_ = export([[C.c_green]])
    np.savez_compressed(out_prefix + "_green.npz", A_mid=Am, A_rad=Ar, B_mid=Bm, B_rad=Br, tb=tbm[0], tb_rad=tbr[0], T_mid=Tm, T_rad=Tr,
                        c_mid=cm_[0, 0], c_rad=cr_[0, 0], prec=prec, hsub=hsub, parent=np.array(C.parent),
                        note="all (mid, rad) pairs enclose the exact values (rad includes the mid->double conversion error)")
    ball = ball_dyadic
    coeffs = dict(prec=prec, A00=ball(info["A00_new"]), Ei=[[ball(x) for x in row] for row in C.Ei], Eo=[[ball(x) for x in row] for row in C.Eo],
                  c=ball(C.c_green), target=ball(info["target"]), format="exact dyadic: mid = man*2^exp, rad = rman*2^rexp",
                  note="Ei, Eo, A00 are defined by the C^6 join equations and c = 3/k - 1; the other coefficients are the stored floats of the trial file")
    json.dump(coeffs, open(out_prefix + "_coeffs.json", "w"))
    print("saved; total %.0fs" % (time.time() - t0))


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 256, float(sys.argv[3]) if len(sys.argv) > 3 else 0.0,
         sys.argv[4] if len(sys.argv) > 4 else "data/cert")
