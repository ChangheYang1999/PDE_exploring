"""Certified (rigorous) upper bounds of the localized forcing norms of the trial residual at the source P = (x_*, 0):
    ||tau eps~||_{H^s}  and  N_lam(tau eps~) = ( int (lam^2 + |xi|^2)^s |(tau eps~)^(xi)|^2 dxi )^{1/2},   s = 31/10,
with the inhomogeneous Sobolev norm of SPEC 3.15 (unitary Fourier transform, J^r = (1 - Lap)^{r/2}, so that for integer m
||f||_{H^m}^2 = sum_{|alpha| <= m} (multinomial) ||D^alpha f||_2^2 and ||f||_{H^4} = ||(1 - Lap)^2 f||_2, ||f||_{H^3}^2 = ||(1 - Lap) f||_2^2 +
||grad (1 - Lap) f||_2^2), and the admissible cutoff tau(X) = S(sigma), sigma = (|X - P| - 7 delta/4)/(delta/2): tau = 1 on B_{7 delta/4}(P),
supp tau in B_{9 delta/4}(P) (SPEC 3.15: tau = 1 on supp chi, supp tau in B_{9 delta/4}); S(sigma) = step(1 - sigma) with step the
degree-9 C^4 polynomial step 126 u^5 - 420 u^6 + 540 u^7 - 315 u^8 + 70 u^9 ('p9', the lead's tau_poly9) or the degree-11 C^5 step
462 u^6 - 1980 u^7 + 3465 u^8 - 3080 u^9 + 1386 u^10 - 252 u^11 ('p11').

Method.
 1. Fractional order by Hoelder: (lam^2 + |xi|^2)^{3.1} = [(lam^2 + |xi|^2)^3]^{0.9} [(lam^2 + |xi|^2)^4]^{0.1}, so
       N_lam(f)^2 <= I3^{0.9} I4^{0.1},  I3 = lam^2 ||(lam^2 - Lap) f||_2^2 + ||grad (lam^2 - Lap) f||_2^2,  I4 = ||(lam^2 - Lap)^2 f||_2^2
    (Plancherel; lam = 1 gives the H^3 and H^4 norms; f = tau eps~ is in W^{4,infty} with compact support, tau in C^4 piecewise polynomial,
    eps~ in C^5 away from the spline knots and C^4 across them within the region, so the distributional derivatives are the a.e. ones).
 2. The L^2 norms are bounded by sum over cells of area x sup^2, where the cells are polar rectangles about the ORIGIN
    (radial sub-intervals of the certificate's spline sub-cells x angular cells) covering B_{3 delta}(P) (coverage checked as in cert_n8.py),
    the lower half-plane by the parity (tau even in y, |D^alpha eps~| even in y).
 3. Pointwise bounds on each cell by the Leibniz formulas (f = tau, g = eps~):
       Lap(fg) = f Lap g + 2 grad f . grad g + g Lap f,
       grad Lap(fg) = grad f Lap g + f grad Lap g + 2 D^2f grad g + 2 D^2g grad f + grad g Lap f + g grad Lap f,
       Lap^2(fg) = f Lap^2 g + g Lap^2 f + 2 Lap f Lap g + 4 grad f . grad Lap g + 4 grad g . grad Lap f + 4 D^2 f : D^2 g,
    with |D^2 f : D^2 g| <= ||D^2 f||_F ||D^2 g||_F.  For the radial cutoff (rho = |X - P|, tau^{(j)} = (2/delta)^j S^{(j)}(sigma)):
       |grad tau| = |tau'|,  Lap tau = tau'' + tau'/rho,  ||D^2 tau||_F^2 = tau''^2 + (tau'/rho)^2,  (Lap tau)' = tau''' + tau''/rho - tau'/rho^2,
       Lap^2 tau = tau'''' + 2 tau'''/rho - tau''/rho^2 + tau'/rho^3,
    bounded on the cell from the range of sigma (distance range of the cell to P, rigorous as in cert_n8.py) with Arb enclosures of the
    exact integer polynomials S^{(j)} on 16 sub-intervals, and rho >= max(dist_min, 7 delta/4) on the support of the derivatives.
 4. The residual derivatives: bivariate Taylor models (BiTM) in (sigma_t, phi) = (t - t_a, theta - theta_c) on each (spline sub-cell x
    angular cell): the per-mode Taylor models of d_t^i eps_N (i <= 4; cert_resid._cell_core_deriv, the same TMs as the derivative
    certificate of NUM_REPORT 7.3b) are summed over the modes N with the Taylor coefficients in phi of
    d_theta^j sin((2N+1) theta) = (2N+1)^j sin((2N+1)(theta_c + phi) + j pi/2) (Arb values at theta_c, remainder
    (2N+1)^{j+Qp+1} w^{Qp+1}/(Qp+1)!, |phi| <= w).  The sums over N keep the angular cancellation (mid-rad matrix products, rigorous
    rounding bounds), unlike the Wiener sums W_i_j of 7.3b.  Cartesian derivatives by the exact recursion
    d_x = e^{-t}(cos th d_t - sin th d_th), d_y = e^{-t}(sin th d_t + cos th d_th) applied to BiTMs (coefficient functions e^{-t},
    cos(th + b pi/2), sin(th + b pi/2) as TMs; products truncated with the truncation added to the remainder).  Suprema of BiTMs over
    sub-cells by tensor Bernstein coefficients after exact re-centring (as cert_resid.bernstein_sup_sub / cert_n8.poly_range_subs).
 5. Output: I3, I4 for each lam, the bounds H^3, H^4, H^{3.1} (lam = 1) and N_lam, and the suprema of |D^alpha eps~| (|alpha| <= 4) over
    B_{9 delta/4}(P) and B_{3 delta}(P).
All arithmetic rigorous: src/midrad.py (mid-rad float64 with outward rounding), Arb (python-flint) for transcendental values, imported as
mid/rad; every sum of nonnegative bounds rounded outward (succ).
Usage: python3 src/cert_forcing.py data/cert_green.npz data/trial_v2_h0.008.npz out.json [delta=33/2000] [cutoff=p9|p11] [KSUB=16] [ntheta=16] [KP=2] [Qp=8] [ci_lo ci_hi]
       (ci_lo ci_hi = radial cell range of one piece; the per-cell pieces are combined by: python3 src/cert_forcing.py merge out_merged.json piece1.json piece2.json ...)
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import comb, factorial
from fractions import Fraction
from flint import arb, ctx, arb_poly
from midrad import MR, mr_matmul, succ, U, ETA
from cert_resid import Certifier, TMArr, tm_exp, bernstein_matrix, mag

XSTAR_LO, XSTAR_HI = 8.60006380515688, 8.600063805157474       # certified bracket of x_* (runs/axis_cell.json, S1; as in cert_n8.py).  These literals are
# the binary64 numbers stored in that JSON (Python's shortest repr round-trips exactly); the S1 ball x_star_mid +/- x_star_rad =
# 8.600063805157177 +/- 2.9402020296740933e-13 (runs/scalars_full.json) lies inside [XSTAR_LO, XSTAR_HI] (checked below).
XSTAR = 0.5 * (XSTAR_LO + XSTAR_HI)
XRAD = float(np.nextafter(max(XSTAR_HI - XSTAR, XSTAR - XSTAR_LO), np.inf))
assert XSTAR_LO <= 8.600063805157177 - 2.9402020296740933e-13 and 8.600063805157177 + 2.9402020296740933e-13 <= XSTAR_HI    # S1 ball inside the bracket (exact doubles)
NDER = 4


def f_up(x):
    """outward (upper) float conversion of an Arb bound: float() rounds to nearest, so step one ulp up."""
    return float(np.nextafter(float(x), np.inf))


def f_lo(x):
    return float(np.nextafter(float(x), -np.inf))
S_ORDER = 3.1          # the fractional order: 3.1 = 0.9 x 3 + 0.1 x 4


def pred(x): return -succ(-np.asarray(x, float))


# ----------------------------------------------------------------------------------------------------------------------------------
class Cell:
    """Geometry of a bivariate Taylor-model cell [0, h] x [-w, w]: upper bounds h_up, w_up and of their powers."""
    def __init__(self, h_up, w_up, Qs, Qp):
        self.h_up = float(h_up); self.w_up = float(w_up); self.Qs = Qs; self.Qp = Qp
        self.hpow = np.array([1.0] + [succ(self.h_up ** i * (1 + 2 * i * U)) for i in range(1, 2 * Qs + 3)])
        self.wpow = np.array([1.0] + [succ(self.w_up ** i * (1 + 2 * i * U)) for i in range(1, 2 * Qp + 3)])
        # the degree weights h^q w^p (q <= 2Qs, p <= 2Qp) must stay in the normal range: the truncation bounds multiply them by the
        # coefficient magnitudes, and an underflowed weight would not be covered by the additive eta allowances (referee forcing1, item 5)
        assert self.hpow.min() * self.wpow.min() > 2.0 ** -900, "degree weights too small (underflow risk)" 


class BiTM:
    """Bivariate Taylor model: polynomial sum_{q <= Qs, p <= Qp} c[q, p] sigma^q phi^p (MR coefficients) + remainder r (float >= 0) on the cell."""
    __slots__ = ("c", "r", "cell")

    def __init__(self, c, r, cell):
        self.c = c; self.r = float(r); self.cell = cell

    @staticmethod
    def zero(cell):
        return BiTM(MR(np.zeros((cell.Qs + 1, cell.Qp + 1))), 0.0, cell)

    @staticmethod
    def from_sigma(coef, rem, cell):
        """TM in sigma only: coef MR (Qs+1,), remainder rem."""
        c = MR(np.zeros((cell.Qs + 1, cell.Qp + 1))); c.m[:, 0] = coef.m; c.r[:, 0] = coef.r
        return BiTM(c, rem, cell)

    @staticmethod
    def from_phi(coef, rem, cell):
        c = MR(np.zeros((cell.Qs + 1, cell.Qp + 1))); c.m[0, :] = coef.m; c.r[0, :] = coef.r
        return BiTM(c, rem, cell)

    def __add__(self, other):
        return BiTM(self.c + other.c, succ(self.r + other.r), self.cell)

    def __sub__(self, other):
        return BiTM(self.c - other.c, succ(self.r + other.r), self.cell)

    def __neg__(self):
        return BiTM(-self.c, self.r, self.cell)

    def scale(self, s):
        """multiply by an MR scalar."""
        return BiTM(self.c * s, succ(succ(self.r * float(s.mag())) * succ(1 + 2 * U)), self.cell)

    def sup_crude(self):
        """upper bound of sup |f| on the cell: sum |c_qp| h^q w^p + r."""
        cl = self.cell; a = mag(self.c) * cl.hpow[:cl.Qs + 1, None] * cl.wpow[None, :cl.Qp + 1]
        n = a.size
        return succ(succ(succ(a.sum() * succ(1 + (n + 2) * U)) + (n + 2) * ETA) + self.r)

    def __mul__(self, other):
        if isinstance(other, MR):
            return self.scale(other)
        cl = self.cell; Qs, Qp = cl.Qs, cl.Qp
        # full polynomial product in float64 with the error model of midrad.mr_matmul: every output coefficient is a sum of at most
        # K = (Qs+1)(Qp+1) products, |fl - exact| <= gamma_{2K} sum |a b| (any order), propagated radii |a| r_b + r_a |b| + r_a r_b
        # (their float sums inflated by 1 + gamma), underflow allowance 4 (K+1) eta
        am, ar, bm, br = self.c.m, self.c.r, other.c.m, other.c.r
        fm = np.zeros((2 * Qs + 1, 2 * Qp + 1)); fabs = np.zeros_like(fm); fr = np.zeros_like(fm); babs = np.abs(bm)
        for q1 in range(Qs + 1):
            for p1 in range(Qp + 1):
                a = am[q1, p1]; ra = ar[q1, p1]
                if a == 0.0 and ra == 0.0: continue
                sl = (slice(q1, q1 + Qs + 1), slice(p1, p1 + Qp + 1))
                fm[sl] += a * bm; fabs[sl] += abs(a) * babs; fr[sl] += abs(a) * br + ra * babs + ra * br
        K = (Qs + 1) * (Qp + 1); gam = succ(2 * K * U / (1 - 2 * K * U))
        full = MR(fm, succ(succ(succ(fabs * gam) + succ(fr * succ(1 + gam))) + 4 * (K + 1) * ETA))
        kept = MR(full.m[:Qs + 1, :Qp + 1].copy(), full.r[:Qs + 1, :Qp + 1].copy())
        # truncated terms (q > Qs or p > Qp): bounded by |c| h^q w^p
        wgt = cl.hpow[:2 * Qs + 1, None] * cl.wpow[None, :2 * Qp + 1]
        tr = mag(full) * wgt; tr[:Qs + 1, :Qp + 1] = 0.0; n = tr.size
        trunc = succ(succ(tr.sum() * succ(1 + (n + 2) * U)) + (n + 2) * ETA)
        s1 = BiTM(self.c, 0.0, cl).sup_crude(); s2 = BiTM(other.c, 0.0, cl).sup_crude()
        rem = succ(succ(succ(succ(s1 * other.r) + succ(s2 * self.r)) + succ(self.r * other.r)) + trunc)
        return BiTM(kept, rem, cl)

    __rmul__ = __mul__


class BernSup:
    """Tensor-Bernstein upper bounds of sup |f| of a BiTM over the Ks x Kp sub-cells of its cell (re-centring exact in MR, vectorized over
    the sub-cells).  Sub-cell (ks, kp): sigma in [ks hk, (ks+1) hk], phi in [-w + kp wk, -w + (kp+1) wk], hk >= h/Ks, wk >= 2w/Kp (the union
    covers the cell; a Bernstein bound on a slightly larger sub-cell is valid for the exact one)."""
    def __init__(self, cell, Ks, Kp, hk=None, wk=None):
        self.cell = cell; self.Ks = Ks; self.Kp = Kp
        Qs, Qp = cell.Qs, cell.Qp
        self.Bs = bernstein_matrix(Qs); Bp = bernstein_matrix(Qp); self.BpT = MR(Bp.m.T.copy(), Bp.r.T.copy())
        self.hk = succ(cell.h_up / Ks) if hk is None else float(hk); self.wk = succ(2.0 * cell.w_up / Kp) if wk is None else float(wk)
        assert (arb(self.hk) * Ks).lower() >= cell.h_up and (arb(self.wk) * Kp).lower() >= 2.0 * cell.w_up    # the sub-intervals cover the cell (exact-real test in Arb; referee forcing2)
        self.hkP = Certifier.mr_powers(self.hk, Qs); self.wkP = Certifier.mr_powers(self.wk, Qp)
        a_s = MR(np.array([ks * self.hk for ks in range(Ks)]), succ(U * np.array([ks * self.hk for ks in range(Ks)])))
        a_p = MR.exact(-cell.w_up) + MR(np.array([kp * self.wk for kp in range(Kp)]), succ(U * np.array([kp * self.wk for kp in range(Kp)])))
        # powers AS[ks, m] = a_s^m, AP[kp, m] = a_p^m
        AS = [MR.exact(np.ones(Ks))]; AP = [MR.exact(np.ones(Kp))]
        for m in range(1, Qs + 1): AS.append(AS[-1] * a_s)
        for m in range(1, Qp + 1): AP.append(AP[-1] * a_p)
        self.AS = MR(np.stack([x.m for x in AS], 1), np.stack([x.r for x in AS], 1)); self.AP = MR(np.stack([x.m for x in AP], 1), np.stack([x.r for x in AP], 1))

    def sups(self, f):
        """array (Ks, Kp) of upper bounds of sup |f| over the sub-cells."""
        c = f.c; Qs, Qp, Ks, Kp = self.cell.Qs, self.cell.Qp, self.Ks, self.Kp
        # sigma re-centre for all ks: c1[ks, j, p] = sum_{i >= j} c[i, p] C(i, j) a_s^{i-j}, then x hk^j
        c1m = np.zeros((Ks, Qs + 1, Qp + 1)); c1r = np.zeros_like(c1m)
        for j in range(Qs + 1):
            acc = None
            for i in range(j, Qs + 1):
                term = MR(c.m[i][None, :], c.r[i][None, :]) * MR.exact(float(comb(i, j))) * MR(self.AS.m[:, i - j][:, None], self.AS.r[:, i - j][:, None])
                acc = term if acc is None else acc + term
            c1m[:, j, :] = acc.m; c1r[:, j, :] = acc.r
        c1 = MR(c1m, c1r) * MR(self.hkP.m[None, :, None], self.hkP.r[None, :, None])
        # phi re-centre for all kp: c2[ks, kp, j, p'] = sum_{p >= p'} c1[ks, j, p] C(p, p') a_p^{p-p'}, then x wk^{p'}
        c2m = np.zeros((Ks, Kp, Qs + 1, Qp + 1)); c2r = np.zeros_like(c2m)
        for pp in range(Qp + 1):
            acc = None
            for p in range(pp, Qp + 1):
                term = MR(c1.m[:, None, :, p], c1.r[:, None, :, p]) * MR.exact(float(comb(p, pp))) * MR(self.AP.m[None, :, None, p - pp], self.AP.r[None, :, None, p - pp])
                acc = term if acc is None else acc + term
            c2m[:, :, :, pp] = acc.m; c2r[:, :, :, pp] = acc.r
        c2 = MR(c2m, c2r) * MR(self.wkP.m[None, None, None, :], self.wkP.r[None, None, None, :])
        Bc = mr_matmul(mr_matmul(self.Bs, c2), self.BpT)          # (Ks, Kp, Qs+1, Qp+1): tensor Bernstein coefficients (batched matmul)
        return succ(mag(Bc).max(axis=(-1, -2)) + f.r)


# ----------------------------------------------------------------------------------------------------------------------------------
def cart_from_polar(J, order, emt, cos_b, sin_b):
    """Same recursion as cert_n8.cart_from_polar_mr / TrialJets.polar_to_cart, on objects with +, -, * (BiTM x BiTM, BiTM x MR scalar).
    J: dict (i, l) -> d_t^i d_th^l f (i + l <= order); emt: e^{-t}; cos_b[b], sin_b[b]: cos(th + b pi/2), sin(th + b pi/2) (b <= order).
    Returns dict (a, b) -> d_x^a d_y^b f, a + b <= order."""
    cache_coef = {}

    def coef(kind, a, b):
        key = (kind, a, b)
        if key not in cache_coef:
            ang = cos_b[b] if kind == "c" else sin_b[b]
            cache_coef[key] = (emt * ang) * MR.exact((-1.0) ** a)
        return cache_coef[key]

    def apply(Fj, ordr, which):
        out = {}
        for i in range(ordr):
            for j in range(ordr - i):
                acc = None
                for a in range(i + 1):
                    for b in range(j + 1):
                        cc = MR.exact(float(comb(i, a) * comb(j, b)))
                        if which == "x":
                            term = coef("c", a, b) * Fj[(i - a + 1, j - b)] - coef("s", a, b) * Fj[(i - a, j - b + 1)]
                        else:
                            term = coef("s", a, b) * Fj[(i - a + 1, j - b)] + coef("c", a, b) * Fj[(i - a, j - b + 1)]
                        term = term * cc
                        acc = term if acc is None else acc + term
                out[(i, j)] = acc
        return out
    D = {(0, 0): J[(0, 0)]}
    cache = {(0, 0): (J, order)}
    for a in range(order + 1):
        for b in range(order + 1 - a):
            if a == 0 and b == 0: continue
            if b == 0:
                Fj, ordr = cache[(a - 1, 0)]; cur = apply(Fj, ordr, "x"); cache[(a, 0)] = (cur, ordr - 1)
            else:
                Fj, ordr = cache[(a, b - 1)]; cur = apply(Fj, ordr, "y"); cache[(a, b)] = (cur, ordr - 1)
            D[(a, b)] = cur[(0, 0)]
    return D


# ----------------------------------------------------------------------------------------------------------------------------------
STEP_POLY = {"p9": [0, 0, 0, 0, 0, 126, -420, 540, -315, 70], "p11": [0, 0, 0, 0, 0, 0, 462, -1980, 3465, -3080, 1386, -252]}


class Cutoff:
    """S(sigma) = step(1 - sigma) as exact integer polynomials with derivatives; Arb range bounds on sub-intervals of [0, 1].
    tau = S(sigma), sigma = (rho - r_in)/(delta/2); tau^{(j)}(rho) = (2/delta)^j S^{(j)}(sigma)."""
    def __init__(self, kind, delta_frac, nsub=16):
        ctx.prec = 128
        step = STEP_POLY[kind]
        # checks of the step: step(1) = 1, step^{(k)}(0) = 0 for k < first nonzero degree, symmetry step(u) + step(1-u) = 1 (exact integer arithmetic)
        assert sum(step) == 1
        S = [0] * len(step)                                   # S(sigma) = sum_k step_k (1 - sigma)^k = sum_i sigma^i sum_k step_k C(k,i) (-1)^i
        for k, sk in enumerate(step):
            for i in range(k + 1): S[i] += sk * comb(k, i) * (-1) ** i
        assert all(S[i] + step[i] == (1 if i == 0 else 0) for i in range(len(step)))      # S(sigma) + step(sigma) = 1: symmetry
        self.kind = kind; self.S = [S]
        for j in range(1, 5):
            prev = self.S[-1]; self.S.append([prev[i] * i for i in range(1, len(prev))])
        self.polys = [arb_poly([arb(c) for c in Sj]) for Sj in self.S]
        self.smooth = min(i for i, c in enumerate(step) if c != 0) - 1       # C^{smooth} across the joins (p9: 4, p11: 5)
        self.delta = arb(delta_frac.numerator) / delta_frac.denominator
        self.r_in = self.delta * 7 / 4; self.r_out = self.delta * 9 / 4; self.half = self.delta / 2
        two_over_delta = 2 / self.delta
        self.scale_up = [1.0] + [float(succ(float((two_over_delta ** j).upper()))) for j in range(1, 5)]      # upper bounds of (2/delta)^j
        self.nsub = nsub

    def sup_abs(self, j, lo, hi):
        """upper bound of sup |S^{(j)}| over [lo, hi] subset [0, 1] (floats lo <= hi) by Arb evaluation on nsub sub-intervals.  Each
        sub-interval [a, b] is evaluated in the CENTRED form p(m + s) (Taylor shift by composition, exact in Arb) at the ball s in [-r, r],
        m = (a+b)/2, r = (b-a)/2: the radius then propagates through the local Taylor coefficients, not through the large alternating
        monomial coefficients (the plain Horner evaluation at the ball over-estimates by factors up to 1e5 near sigma = 1)."""
        if hi <= lo: hi = lo
        best = 0.0; n = self.nsub
        for i in range(n):
            a = arb(lo) + (arb(hi) - arb(lo)) * i / n; b = arb(lo) + (arb(hi) - arb(lo)) * (i + 1) / n
            m = (a + b) / 2; r = (b - a) / 2
            shifted = self.polys[j](arb_poly([m, 1]))              # p(m + s) as a polynomial in s
            ru = abs(r).upper()                                      # exact upper bound of the half-width
            v = shifted(arb(0).union(ru).union(-ru))                # ball [-ru, ru] containing s
            best = max(best, float(succ(float(abs(v).upper()))))
        return best

    def quantities(self, dmin, dmax):
        """From the distance range [dmin, dmax] of a cell to P (floats, outward): sup bounds T0 = sup tau, T1..T4 = sup |tau^{(j)}| (rho-derivatives),
        and the derived bounds TL = |Lap tau|, T2F = ||D^2 tau||_F, TL1 = |grad Lap tau|, TL2 = |Lap^2 tau|.  None if the cell misses supp tau."""
        r_in_lo = f_lo(self.r_in.lower()); r_out_hi = f_up(self.r_out.upper())            # outward double conversions (referee forcing1, item 3)
        if dmin >= r_out_hi: return None
        # sigma range (outward): sigma_lo = (dmin - r_in)/half rounded down, sigma_hi = (dmax - r_in)/half rounded up; clipped to [0, 1]
        slo = f_lo(((arb(dmin) - self.r_in) / self.half).lower()); shi = f_up(((arb(dmax) - self.r_in) / self.half).upper())
        slo_c = min(max(slo, 0.0), 1.0); shi_c = min(max(shi, 0.0), 1.0)
        T0 = 1.0 if slo <= 0.0 else self.sup_abs(0, slo_c, shi_c)
        if shi <= 0.0:                                       # the cell lies inside B_{7 delta/4}: tau = 1, derivatives 0
            return dict(T0=1.0, T1=0.0, T2=0.0, T3=0.0, T4=0.0, TL=0.0, T2F=0.0, TL1=0.0, TL2=0.0, sigma=[slo, shi])
        T = [T0] + [succ(self.sup_abs(j, slo_c, shi_c) * self.scale_up[j] * (1 + 4 * U)) for j in range(1, 5)]
        rho_m = max(dmin, r_in_lo)                           # lower bound of rho on the support of the derivatives within the cell
        inv = succ(1.0 / rho_m * (1 + 2 * U)); inv2 = succ(inv * inv); inv3 = succ(inv2 * inv)
        TL = succ(T[2] + succ(T[1] * inv))
        T2F = succ(np.sqrt(succ(succ(T[2] * T[2]) + succ(succ(T[1] * inv) ** 2))) * (1 + 2 * U))
        TL1 = succ(succ(T[3] + succ(T[2] * inv)) + succ(T[1] * inv2))
        TL2 = succ(succ(succ(T[4] + succ(2 * succ(T[3] * inv))) + succ(T[2] * inv2)) + succ(T[1] * inv3))
        return dict(T0=T[0], T1=T[1], T2=T[2], T3=T[3], T4=T[4], TL=TL, T2F=T2F, TL1=TL1, TL2=TL2, sigma=[slo, shi])


# ----------------------------------------------------------------------------------------------------------------------------------
def merge(paths, out):
    """Merge partial outputs (chunks of radial cells, same parameters): sums of I3, I4, maxima of the suprema, union of the rows."""
    parts = [json.load(open(p)) for p in paths]
    base = dict(parts[0]); keyset = ["delta", "cutoff", "KSUB", "ntheta", "KP", "Qs", "Qp", "theta_max", "radial_cells_cover", "green", "trial", "x_star_bracket", "s", "code_version"]
    for k in ("nbs", "nbp", "Kser"):
        if k in base: keyset.append(k)
    for p in parts[1:]:
        for k in keyset: assert p[k] == base[k], ("parameter mismatch", k)
    cov = base["radial_cells_cover"]; need = list(range(cov[0], cov[1] + 1))
    # every (radial cell, angular cell) pair exactly once: parts may be chunks in the radial index and (v2) in the angular index
    nth = base["ntheta"]; pairs = []
    for p in parts:
        qr = p.get("qchunk", [0, nth - 1])
        pairs += [(ci, q) for ci in p["chunk"] for q in range(qr[0], qr[1] + 1)]
    assert sorted(pairs) == [(ci, q) for ci in need for q in range(nth)], "the parts do not cover (radial cells x angular cells) exactly once"
    chunks = need
    lams = list(parts[0]["results"].keys())
    acc = {l: dict(I3=0.0, I4=0.0) for l in lams}
    for p in parts:
        for l in lams:
            acc[l]["I3"] = succ(acc[l]["I3"] + p["results"][l]["I3"]); acc[l]["I4"] = succ(acc[l]["I4"] + p["results"][l]["I4"])
    base["results"] = {l: finish(float(l), acc[l]["I3"], acc[l]["I4"]) for l in lams}
    for ball in base["sup_D_eps"]:
        for k in base["sup_D_eps"][ball]:
            vals = [(p["sup_D_eps"][ball][k], p["where"][ball].get(k)) for p in parts]
            v, w = max(vals, key=lambda z: z[0]); base["sup_D_eps"][ball][k] = v; base["where"][ball][k] = w
    area = {b: 0.0 for b in base["area_sum"]}
    for p in parts:
        for b in area: area[b] = float(succ(area[b] + p["area_sum"][b]))
    base["area_sum"] = area
    base["n_subcells_in_support"] = sum(p["n_subcells_in_support"] for p in parts); base["time"] = sum(p["time"] for p in parts)
    if "regime_count" in base:
        base["regime_count"] = {k: sum(p["regime_count"][k] for p in parts) for k in base["regime_count"]}
        base["worst_series"] = {k: max(p["worst_series"][k] for p in parts) for k in base["worst_series"]}
    base["cells"] = sum([p["cells"] for p in parts], []); base["chunk"] = chunks; base["qchunk"] = [0, nth - 1]; base["merged_from"] = paths
    base["radial_cells"] = cov; base["n_radial_cells"] = len(need); base["partial"] = False; base["done"] = True
    json.dump(base, open(out, "w"), indent=1)
    print("merged %d parts -> %s" % (len(parts), out))
    for l in lams:
        r = base["results"][l]
        print("  lam = %s: I3 <= %.6g, I4 <= %.6g;  order-3 <= %.5g, order-4 <= %.5g,  ORDER-3.1 BOUND <= %.5g" % (l, r["I3"], r["I4"], r["bound_order3"], r["bound_order4"], r["bound_order_3_1"]))
    for ball in base["sup_D_eps"]:
        print("  sup |D^alpha eps~| on %s: " % ball + ", ".join("%s: %.3e" % (k, v) for k, v in base["sup_D_eps"][ball].items()))


def finish(lam, I3, I4):
    """From the certified I3, I4 (floats, upper bounds): order-3 and order-4 norms (square roots) and the order-3.1 bound
    N <= I3^{9/20} I4^{1/20} (Hoelder, N^2 <= I3^{0.9} I4^{0.1}), evaluated in Arb with the EXACT rational exponents and converted outward
    (referee forcing1, item 6: float pow with the binary64 exponent 0.45 is not an outward evaluation)."""
    ctx.prec = 128
    n3 = f_up(arb(I3).sqrt().upper()); n4 = f_up(arb(I4).sqrt().upper())
    n31 = f_up(((arb(I3) ** (arb(9) / 20)) * (arb(I4) ** (arb(1) / 20))).upper()) if I3 > 0 and I4 > 0 else 0.0
    return dict(lam=lam, I3=float(I3), I4=float(I4), bound_order3=float(n3), bound_order4=float(n4), bound_order_3_1=float(n31))


def main(green, trial, out, delta_str="33/2000", cutoff="p9", KSUB=16, ntheta=16, KP=2, Qp=8, chunk=None):
    t0 = time.time()
    C = Certifier(green, trial, Q=12); Qs = C.Q
    ctx.prec = 128
    dfrac = Fraction(delta_str); cut = Cutoff(cutoff, dfrac)
    delta = cut.delta; xs = arb(XSTAR, XRAD)
    R3 = 3 * delta; R94 = cut.r_out
    # ---- radial cells covering [x_* - 3 delta, x_* + 3 delta] (as in cert_n8.py)
    t_lo_need = float(pred(float((xs - R3).log().lower()))); t_hi_need = float(succ(float((xs + R3).log().upper())))
    tb_lo = C.tb.lower(); tb_hi = C.tb.upper()
    cells = [ci for ci in range(C.nc) if tb_hi[ci + 1] > t_lo_need and tb_lo[ci] < t_hi_need]
    assert tb_hi[cells[0]] <= t_lo_need and tb_lo[cells[-1] + 1] >= t_hi_need, "radial coverage"
    assert cells == list(range(cells[0], cells[-1] + 1)), "cells contiguous"
    cover = [int(cells[0]), int(cells[-1])]
    if chunk is not None:                                   # chunk = (lo, hi): absolute cell indices ci to process in this run (inclusive)
        cells = [ci for ci in cells if chunk[0] <= ci <= chunk[1]]
        print("chunk: cells %d..%d of the cover %d..%d" % (cells[0], cells[-1], cover[0], cover[1]), flush=True)
    # ---- angular cells: theta in [0, theta_max], theta_max >= asin(3 delta/x_*) (tangent lines from the origin), ntheta cells
    theta_max_f = float(np.nextafter(float(((R3 / xs).asin() * arb("1.000001")).upper()), np.inf)); theta_max = arb(theta_max_f)
    assert (theta_max - (R3 / xs).asin()).lower() > 0, "angular coverage"
    dth = theta_max / ntheta
    w_up = float(np.nextafter(float((dth / 2).upper()), np.inf))                       # half-width (upper bound); the exact cell is within [theta_c - w, theta_c + w]
    print("delta = %s, cutoff %s (C^%d step), radial cells %d (ci %d..%d, r in [%.5f, %.5f]), theta_max %.6g, ntheta %d, w %.3e, KSUB %d, KP %d, Qs %d, Qp %d" % (
        dfrac, cutoff, cut.smooth, len(cells), cells[0], cells[-1], np.exp(tb_lo[cells[0]]), np.exp(tb_hi[cells[-1] + 1]), theta_max_f, ntheta, w_up, KSUB, KP, Qs, Qp), flush=True)
    Nmax = C.Nmax; twoN1 = 2.0 * np.arange(Nmax + 1) + 1.0
    XS_MR = MR(XSTAR, XRAD)
    lams = [1.0, 500.0]
    acc = {lam: dict(I3=0.0, I4=0.0) for lam in lams}
    keys = [(a, b) for a in range(NDER + 1) for b in range(NDER + 1 - a)]
    supD = {"B94": {k: 0.0 for k in keys}, "B3": {k: 0.0 for k in keys}}
    where = {"B94": {}, "B3": {}}
    area_tot = {"B94": 0.0, "B3": 0.0}
    ncell_used = 0; nsub_used = 0; rows = []
    # trig factor tables per angular cell (independent of the radial cell): for mode frequencies f_N = 2N+1 and the coordinate factor f = 1
    ang_tables = []
    inv_fact = [MR(1.0 / factorial(p), succ(U / factorial(p))) for p in range(Qp + 1)]
    for q in range(ntheta):
        theta_c = dth * (q + arb(1) / 2)                      # exact centre of the cell as an Arb ball
        th1 = dth * q; th2 = dth * (q + 1)
        sN = []; cN = []
        for N in range(Nmax + 1):
            s_, c_ = (theta_c * int(2 * N + 1)).sin_cos(); sN.append(s_); cN.append(c_)
        SN = MR.from_arb(sN); CN = MR.from_arb(cN)
        trig = [SN, CN, -SN, -CN]                              # sin(a + m pi/2) for m mod 4
        s1, c1 = theta_c.sin_cos(); S1 = MR.from_arb([s1]); C1 = MR.from_arb([c1]); trig1 = [S1, C1, -S1, -C1]
        # powers f_N^m, m <= NDER + Qp (MR)
        fpow = [MR.exact(np.ones(Nmax + 1))]
        for m in range(1, NDER + Qp + 2): fpow.append(fpow[-1] * MR.exact(twoN1))
        # T_j[p][N] = f_N^{j+p} sin(a_N + (j+p) pi/2)/p!  -> MR arrays (Nmax+1, Qp+1); remainder factor per N: f_N^{j+Qp+1} w^{Qp+1}/(Qp+1)!
        Tj = []; remfac = []
        wq = succ(w_up ** (Qp + 1) * (1 + 2 * (Qp + 1) * U) / factorial(Qp + 1))
        for j in range(NDER + 1):
            cols = []
            for p in range(Qp + 1):
                cols.append(fpow[j + p] * trig[(j + p) % 4] * inv_fact[p])
            Tj.append(MR(np.stack([c.m for c in cols], 1), np.stack([c.r for c in cols], 1)))
            remfac.append(succ(mag(fpow[j + Qp + 1]) * wq * (1 + 2 * U)))
        # coordinate-factor TMs in phi: cos(theta_c + phi + b pi/2) = sum_p sin(theta_c + (b + p + 1) pi/2) phi^p/p!, sin(.. + b pi/2) = sum_p sin(theta_c + (b+p) pi/2) phi^p/p!
        cosb = []; sinb = []
        for b in range(NDER + 2):
            cc = [trig1[(b + p + 1) % 4] * inv_fact[p] for p in range(Qp + 1)]
            ss = [trig1[(b + p) % 4] * inv_fact[p] for p in range(Qp + 1)]
            cosb.append(MR(np.array([x.m[0] for x in cc]), np.array([x.r[0] for x in cc])))
            sinb.append(MR(np.array([x.m[0] for x in ss]), np.array([x.r[0] for x in ss])))
        ang_tables.append(dict(q=q, theta_c=theta_c, th1=th1, th2=th2, Tj=Tj, remfac=remfac, cosb=cosb, sinb=sinb, trig_rem=wq,
                               cos_th1=MR.from_arb([th1.cos()]), sin_th1=MR.from_arb([th1.sin()]), cos_th2=MR.from_arb([th2.cos()])))
    print("angular tables done (%.0fs)" % (time.time() - t0), flush=True)
    tim = dict(jets=0.0, rec=0.0, bern=0.0, geo=0.0)
    for idx, ci in enumerate(cells):
        h = C.tb[ci + 1] - C.tb[ci]; h_up = h.mag()
        assert succ(2.0 * C.Nf * h_up) <= 1.0, 'ODE remainder hypothesis 2 Nf h <= 1'
        res = C.cell_core_deriv(h_up, C.e_ta[ci], [(0.0, C.T[ci])], C.A[ci], C.B[ci], C.m_ta[ci], C.wfar_ta[ci], NDER)
        eps = C._last_eps                                       # list over i <= NDER of TMArr over N: coefficients (Nmax+1, Qs+1), remainders (Nmax+1,)
        cell = Cell(h_up, w_up, Qs, Qp); bern = BernSup(cell, KSUB, KP)
        hpow1 = cell.hpow
        epsT = [MR(eps[i].c.m.T.copy(), eps[i].c.r.T.copy()) for i in range(NDER + 1)]          # (Qs+1, Nmax+1)
        epsSup = [eps[i].sup(hpow1) for i in range(NDER + 1)]                                      # per-mode crude sups (Nmax+1,)
        ta = arb(float(C.d["tb"][ci]), float(C.d["tb_rad"][ci]))
        Ec, Er = tm_exp(-1.0, h_up, Qs); inv_e = MR.from_arb([(-ta).exp()])
        EMT = BiTM.from_sigma(Ec * MR(inv_e.m[0], inv_e.r[0]), succ(Er * float(inv_e.mag()[0]) * (1 + 2 * U)), cell)
        # radial sub-interval ranges r_lo[ks], r_hi[ks] (Arb, outward)
        hk = arb(bern.hk)
        r_lo = np.zeros(KSUB); r_hi = np.zeros(KSUB)
        for ks in range(KSUB):
            tcell = (ta + hk * ks).union(ta + hk * (ks + 1))
            r_lo[ks] = float(pred(float(tcell.exp().lower()))); r_hi[ks] = float(succ(float(tcell.exp().upper())))
        for A in ang_tables:
            t1 = time.time()
            # (t, theta)-jets as BiTMs: coefficients sum_N eps_N^{(i)}[q] T_j[N, p]; remainder sum_N rem_N^{(i)} f_N^j + sum_N sup_N^{(i)} remfac_j[N]
            J = {}
            for i in range(NDER + 1):
                for j in range(NDER + 1 - i):
                    cf = mr_matmul(epsT[i], A["Tj"][j])
                    r1 = succ(succ((eps[i].r * (twoN1 ** j)).sum() * succ(1 + (Nmax + 2) * U)) + (Nmax + 2) * ETA)          # (2N+1)^j exact in float64 for j <= 4
                    r2 = succ(succ((epsSup[i] * A["remfac"][j]).sum() * succ(1 + (Nmax + 2) * U)) + (Nmax + 2) * ETA)      # additive eta allowance: the relative rule alone is not outward for subnormal terms (ver 08:07Z)
                    J[(i, j)] = BiTM(cf, succ(r1 + r2), cell)
            cos_b = [BiTM.from_phi(A["cosb"][b], A["trig_rem"], cell) for b in range(NDER + 2)]
            sin_b = [BiTM.from_phi(A["sinb"][b], A["trig_rem"], cell) for b in range(NDER + 2)]
            t2 = time.time(); tim["jets"] += t2 - t1
            D = cart_from_polar(J, NDER, EMT, cos_b, sin_b)
            t3 = time.time(); tim["rec"] += t3 - t2
            lap = D[(2, 0)] + D[(0, 2)]; lapx = D[(3, 0)] + D[(1, 2)]; lapy = D[(2, 1)] + D[(0, 3)]
            lap2 = D[(4, 0)] + D[(2, 2)].scale(MR.exact(2.0)) + D[(0, 4)]
            S = {k: bern.sups(D[k]) for k in keys}
            SL = bern.sups(lap); SLx = bern.sups(lapx); SLy = bern.sups(lapy); SL2 = bern.sups(lap2)
            t4 = time.time(); tim["bern"] += t4 - t3
            # geometry of the sub-cells: theta in [th1 + kp wk, th1 + (kp+1) wk] (wk >= exact width/KP), r in [r_lo[ks], r_hi[ks]]
            for kp in range(KP):
                # the geometric sub-cell IS the Bernstein sub-cell: theta in [theta_c - w_up + kp wk, theta_c - w_up + (kp+1) wk] (exact reals);
                # their union covers the angular cell [th1, th2] (theta_c - w_up <= th1, KP wk >= 2 w_up).  (Referee forcing1, item 2: the earlier
                # version used th1 + kp wk, shifted by w_up - dth/2 ~ 1e-20 from the Bernstein sub-cell.)
                thA = A["theta_c"] + arb(-w_up) + arb(bern.wk) * kp; thB = thA + arb(bern.wk)
                thA0 = thA if thA.lower() >= 0 else arb(0)                   # dmin: the distance to P is even in theta, so a sub-cell straddling the axis has its minimum at theta = 0
                cA = MR.from_arb([thA0.cos()]); sA = MR.from_arb([thA0.sin()]); cB = MR.from_arb([thB.cos()])
                dth_up = f_up((thB - thA).upper())
                for ks in range(KSUB):
                    R1 = MR.exact(r_lo[ks]); R2 = MR.exact(r_hi[ks])
                    # dmin: min over the cell of |X - P| is at theta = thA; dist(x_* cos thA, [r1, r2])^2 + (x_* sin thA)^2
                    xc = XS_MR * cA; g1 = float((R1 - xc).lower()[0]); g2 = float((xc - R2).lower()[0]); g = max(0.0, g1, g2)
                    xsn = XS_MR * sA
                    d2_lo = pred(pred(g * g * (1 - 4 * U)) + pred(float(xsn.mig()[0]) ** 2 * (1 - 4 * U)))
                    dmin = float(pred(np.sqrt(max(d2_lo, 0.0)) * (1 - 4 * U)))
                    # dmax: at theta = thB and r in {r1, r2}: d^2 = r^2 - 2 r x_* cos thB + x_*^2 (upper bounds)
                    xcB = XS_MR * cB
                    d2a = (R1 * R1 - MR.exact(2.0) * R1 * xcB + XS_MR * XS_MR).upper()[0]; d2b = (R2 * R2 - MR.exact(2.0) * R2 * xcB + XS_MR * XS_MR).upper()[0]
                    dmax = float(succ(np.sqrt(max(d2a, d2b, 0.0)) * (1 + 4 * U)))
                    area = succ(succ(0.5 * succ(succ(r_hi[ks] * r_hi[ks]) - r_lo[ks] * r_lo[ks] * (1 - 2 * U)) * dth_up) * 2.0 * (1 + 4 * U))   # both half-planes (|theta| even symmetry)
                    # suprema of |D^alpha eps~| on the balls (cells with dmin <= radius)
                    for ball, rad in (("B94", f_up(R94.upper())), ("B3", f_up(R3.upper()))):
                        if dmin <= rad:
                            area_tot[ball] = succ(area_tot[ball] + area)
                            for k in keys:
                                v = S[k][ks, kp]
                                if v > supD[ball][k]:
                                    supD[ball][k] = float(v); where[ball][k] = dict(ci=ci, q=A["q"], ks=ks, kp=kp, r=[float(r_lo[ks]), float(r_hi[ks])], dmin=dmin, dmax=dmax)
                    TQ = cut.quantities(dmin, dmax)
                    if TQ is None: continue
                    nsub_used += 1
                    G0 = S[(0, 0)][ks, kp]
                    G1 = succ(np.sqrt(succ(succ(S[(1, 0)][ks, kp] ** 2) + succ(S[(0, 1)][ks, kp] ** 2))) * (1 + 2 * U))
                    G2F = succ(np.sqrt(succ(succ(succ(S[(2, 0)][ks, kp] ** 2) + succ(2 * succ(S[(1, 1)][ks, kp] ** 2))) + succ(S[(0, 2)][ks, kp] ** 2))) * (1 + 2 * U))
                    GL = SL[ks, kp]; GL1 = succ(np.sqrt(succ(succ(SLx[ks, kp] ** 2) + succ(SLy[ks, kp] ** 2))) * (1 + 2 * U)); GL2 = SL2[ks, kp]
                    T0, T1, TL, T2F, TL1, TL2 = TQ["T0"], TQ["T1"], TQ["TL"], TQ["T2F"], TQ["TL1"], TQ["TL2"]
                    F0 = succ(T0 * G0)
                    F1 = succ(succ(T0 * G1) + succ(T1 * G0))
                    FL = succ(succ(succ(T0 * GL) + succ(2 * succ(T1 * G1))) + succ(G0 * TL))
                    FL1 = succ(succ(succ(succ(succ(T1 * GL) + succ(T0 * GL1)) + succ(2 * succ(T2F * G1))) + succ(2 * succ(G2F * T1))) + succ(succ(G1 * TL) + succ(G0 * TL1)))
                    FL2 = succ(succ(succ(succ(succ(T0 * GL2) + succ(G0 * TL2)) + succ(2 * succ(TL * GL))) + succ(4 * succ(T1 * GL1))) + succ(succ(4 * succ(G1 * TL1)) + succ(4 * succ(T2F * G2F))))
                    for lam in lams:
                        l2 = lam * lam; l4 = l2 * l2
                        a3 = succ(succ(l2 * succ(succ(l2 * F0) + FL) ** 2) + succ(succ(succ(l2 * F1) + FL1) ** 2))
                        a4 = succ(succ(succ(succ(l4 * F0) + succ(2 * succ(l2 * FL))) + FL2) ** 2)
                        acc[lam]["I3"] = succ(acc[lam]["I3"] + succ(area * a3)); acc[lam]["I4"] = succ(acc[lam]["I4"] + succ(area * a4))
                    rows.append(dict(ci=ci, q=A["q"], ks=ks, kp=kp, dmin=dmin, dmax=dmax, area=float(area), sigma=TQ["sigma"], G0=float(G0), G1=float(G1), G2F=float(G2F), GL=float(GL), GL1=float(GL1), GL2=float(GL2),
                                     T0=T0, T1=T1, T2F=T2F, TL=TL, TL1=TL1, TL2=TL2, F0=float(F0), F1=float(F1), FL=float(FL), FL1=float(FL1), FL2=float(FL2),
                                     rem_D={"%d_%d" % k: float(D[k].r) for k in keys}, rem_lap=[float(lap.r), float(lapx.r), float(lapy.r), float(lap2.r)]))
            ncell_used += 1; tim["geo"] += time.time() - t4
        print("  timers: jets %.0fs recursion %.0fs bernstein %.0fs geometry %.0fs" % (tim["jets"], tim["rec"], tim["bern"], tim["geo"]), flush=True)
        print("radial cell %d/%d ci=%d r=[%.5f, %.5f] remA %.1e rem_eps4 %.1e | running I3 %.4g I4 %.4g (lam=1) | sup|eps| B94 %.3e |grad| %.3e |D4| %.3e (%.0fs)" % (
            idx + 1, len(cells), ci, r_lo.min(), r_hi.max(), res["remA"], res["rem_eps_4"], acc[1.0]["I3"], acc[1.0]["I4"], supD["B94"][(0, 0)],
            max(supD["B94"][(1, 0)], supD["B94"][(0, 1)]), max(supD["B94"][k] for k in keys if sum(k) == 4), time.time() - t0), flush=True)
    # ---- results
    results = {str(lam): finish(lam, acc[lam]["I3"], acc[lam]["I4"]) for lam in lams}
    out_d = dict(green=green, trial=trial, delta=str(dfrac), cutoff=cutoff, cutoff_smoothness="C^%d" % cut.smooth, cutoff_poly_step=STEP_POLY[cutoff],
                 s=S_ORDER, KSUB=KSUB, ntheta=ntheta, KP=KP, Qs=Qs, Qp=Qp, theta_max=theta_max_f, radial_cells=[int(cells[0]), int(cells[-1])],
                 radial_cells_cover=cover, chunk=[int(c) for c in cells], partial=(chunk is not None),
                 x_star_bracket=[XSTAR_LO, XSTAR_HI], n_angular_cells=ntheta, n_radial_cells=len(cells), n_subcells_in_support=nsub_used,
                 area_sum={k: float(v) for k, v in area_tot.items()}, results=results,
                 sup_D_eps={ball: {"%d_%d" % k: supD[ball][k] for k in keys} for ball in supD}, where={ball: {"%d_%d" % k: v for k, v in where[ball].items()} for ball in where},
                 cells=rows, code_version="cert_forcing.py v1.2 (2026-10-21 shift 4; v1.1 + additive eta allowance in the jet remainder sums, G2F/T2F row fields)", time=time.time() - t0, done=True)
    json.dump(out_d, open(out, "w"), indent=1)
    print("\nRESULTS (rigorous upper bounds), delta = %s, cutoff %s:" % (dfrac, cutoff))
    for lam in lams:
        r = results[str(lam)]
        print("  lam = %g: I3 <= %.6g, I4 <= %.6g;  order-3 norm <= %.5g, order-4 norm <= %.5g,  ORDER-3.1 BOUND <= %.5g" % (lam, r["I3"], r["I4"], r["bound_order3"], r["bound_order4"], r["bound_order_3_1"]))
    for ball in ("B94", "B3"):
        print("  sup |D^alpha eps~| on %s: " % ball + ", ".join("%d%d: %.3e" % (k[0], k[1], supD[ball][k]) for k in keys))
    print("done %.0fs -> %s" % (time.time() - t0, out))


if __name__ == "__main__":
    a = sys.argv
    if a[1] == "merge":
        merge(a[3:], a[2])                       # python3 cert_forcing.py merge out.json part1.json part2.json ...
    else:
        main(a[1], a[2], a[3], a[4] if len(a) > 4 else "33/2000", a[5] if len(a) > 5 else "p9", int(a[6]) if len(a) > 6 else 16,
             int(a[7]) if len(a) > 7 else 16, int(a[8]) if len(a) > 8 else 2, int(a[9]) if len(a) > 9 else 8,
             (int(a[10]), int(a[11])) if len(a) > 11 else None)
