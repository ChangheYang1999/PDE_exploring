"""Independent review of T4-259 (c1-t4 research/theory_final_draft_audit/PROOF.md, sha256 0378fab1...baf54): audit of
THEORY_FINAL draft 3 (source sha256 73aa2b48...e7f2), in particular the Fourier proof that the A2 forcing space N_s
(s = 2^-18) and the sharpw forcing space X_t (t = 1/5184) are incomparable (reviews/REVIEW_T4_259.md).

Run from artifacts/:  python3 -B arith/t4_259_review.py
Needs sympy, numpy, python-flint.

Parts:
  (A) exact (sympy): the rank-one resolvent fixture of Section 1, with M(lambda) on the whole axis;
  (B) exact (sympy): Section 2. Parity and reality of (1) and (4) for generic even bumps; the exponent sums of (2),
      (3), (5); the bound omega <= 4^(2/5) (1 + |X|^2)^(1/2); exact scaling of the Fourier summands of (4) for a
      concrete polynomial bump (L2, Hdot^-1, Hessian and its first xi derivative); the fixed-exponent inclusion
      constant X_u <= 2 N_u;
  (C) arb (python-flint): Remark R2 of the review, the one-sided comparison X_t <= kappa(K) N_s on the E_3 class
      with Q3 <= K E_2, and the resulting enlargement factor of the A2 threshold ball;
  (D) Section 4: the unsigned counterexample K = P (exact), the signed compression bound by Cauchy interlacing
      (FLOAT random tests, illustration only), the graded inequality 50/(651 sqrt(28248)) < 25/54684 (exact);
  (E) Section 5 fractions (exact) and the sector counts of the report's section 0.2 at the run value of c (exact).
Output: logs/t4_259_review.log.
"""
import time

import numpy as np
import sympy as sp
from flint import arb, ctx, fmpq

T0 = time.monotonic()

# =============================== (A) Section 1 ===============================
lam = sp.Symbol("lambda", nonnegative=True)
n_ = 3
e = sp.Matrix([1, 0, 0])
P = e * e.T
I3 = sp.eye(n_)
D = -I3
Psi = 2 * e                      # Psi a = 2 a e
Phi = e.T                        # Phi h = <h, e>
A = D + Psi * Phi
assert A == -I3 + 2 * P and A * A == I3
R0 = D.inv()
M0 = 1 + (Phi * R0 * Psi)[0, 0]
assert M0 == -1
Ainv_wood = R0 - R0 * Psi * (1 / M0) * Phi * R0
assert Ainv_wood == A.inv() == A
wood_bound = 1 + 2 * 1 * 1       # ||R|| + ||R Psi|| |M^-1| ||Phi R||
Ml = sp.simplify(1 + (Phi * (D - lam * I3).inv() * Psi)[0, 0])
assert sp.simplify(Ml - (lam - 1) / (lam + 1)) == 0
assert A * e == e and sp.factor((A - lam * I3).det()) == sp.factor(-(lam - 1) * (lam + 1)**2)
print("(A) A = -I + 2P: D = -I (gap 1), M(0) = %s, A^-1 = A (norm 1), Woodbury bound %d, Ae = e;"
      " M(lambda) = 1 + Phi (D - lambda)^-1 Psi = (lambda - 1)/(lambda + 1) vanishes at lambda = 1 = the eigenvalue;"
      " det(A - lambda) = -(lambda - 1)(lambda + 1)^2" % (M0, wood_bound))

# =============================== (B) Section 2 ===============================
x1, x2 = sp.symbols("xi1 xi2", real=True)
Rn = sp.Symbol("R", positive=True)
eta = sp.Function("eta", real=True)
eta0 = sp.Function("eta0", real=True)
bump = lambda a1, a2: eta(a1**2, a2**2)                     # generic real bump, even in each coordinate
f1 = sp.I * (bump(x1, x2 - Rn) - bump(x1, x2 + Rn))
assert sp.simplify(f1.subs(x1, -x1) - f1) == 0               # even in xi1
assert sp.simplify(f1.subs(x2, -x2, simultaneous=True) + f1) == 0   # odd in xi2
assert sp.simplify(sp.conjugate(f1) + f1) == 0                # purely imaginary (eta real)
g4 = sp.I * x2 * eta0(x1**2 + x2**2)
assert sp.simplify(g4.subs(x1, -x1) - g4) == 0 and sp.simplify(g4.subs(x2, -x2) + g4) == 0
print("(B1) (1) and (4): fhat, ghat even in xi1, odd in xi2, purely imaginary: Fourier form of real S1")

s = fmpq(1, 2**18)
t = fmpq(1, 5184)
q = (s + t) / 2
assert 0 < s < t <= fmpq(1, 2)
# a_n = R_n^-(2+q): exponents of R_n in a_n^2 R_n^(2k + 2u)
ex = {"H^(2+t) lower bound (2)": -2 * (2 + q) + 4 + 2 * t, "weighted Hessian (3)": -2 * (2 + q) + 4 + 2 * s,
      "D J^s": -2 * (2 + q) + 2 + 2 * s, "J^s": -2 * (2 + q) + 2 * s}
assert ex["H^(2+t) lower bound (2)"] == t - s > 0
assert ex["weighted Hessian (3)"] == s - t < 0 and ex["D J^s"] < 0 and ex["J^s"] < 0
geo = 1 / (arb(4) ** (arb((t - s).p) / (t - s).q) - 1)
print("(B2) q = (s + t)/2 = %s; exponent of R_n in a_n^2 R_n^(4+2t): t - s = %s > 0, so (2) diverges;"
      " in a_n^2 R_n^(4+2s): s - t < 0, sum_n 4^(n(s-t)) = 1/(4^(t-s) - 1) = %s (finite); D J^s and J^s"
      " exponents %s, %s" % (q, ex["H^(2+t) lower bound (2)"], geo.str(6), ex["D J^s"], ex["J^s"]))
rr = sp.Symbol("r", nonnegative=True)
om = (1 + 4 * rr**2) ** sp.Rational(2, 5)
Cw = sp.Rational(4) ** sp.Rational(2, 5)
# omega = ((1 + 4 r^2)/(4 + 4 r^2))^(2/5) C (1 + r^2)^(2/5) with first factor <= 1, and 2/5 <= 1/2
assert sp.expand((4 + 4 * rr**2) - (1 + 4 * rr**2)) == 3 and sp.Rational(2, 5) <= sp.Rational(1, 2)
assert sp.simplify(Cw**5 - 4**2) == 0
print("(B3) omega = (1 + 4 r^2)^(2/5) <= 4^(2/5) (1 + r^2)^(2/5) <= 4^(2/5) (1 + r^2)^(1/2), C = 4^(2/5) = %.6f;"
      " ||(1 + |X|^2)^(1/2) F||^2 = ||Fhat||^2 + sum_k ||d_(xi_k) Fhat||^2 (Plancherel)" % float(Cw))

# exact scaling of the summands of (4) for eta0(rho) = (rho^2 - 1)^3 (4 - rho^2)^3 on 1 < rho < 2
rho, sc = sp.symbols("rho r_n", positive=True)


CS, SN = sp.symbols("C S")


def ang_poly(F):                 # F(xi1, xi2) polynomial -> sum over monomials of int_0^(2 pi) cos^a sin^b dphi (exact)
    Fp = sp.Poly(sp.expand(F.subs({x1: rho * CS, x2: rho * SN}, simultaneous=True)), CS, SN)
    out = 0
    for (a_, b_), cf in Fp.terms():
        if a_ % 2 or b_ % 2:
            continue
        out += cf * 2 * sp.gamma(sp.Rational(a_ + 1, 2)) * sp.gamma(sp.Rational(b_ + 1, 2)) / sp.gamma(
            sp.Rational(a_ + b_ + 2, 2))
    return sp.expand(out)


def annulus_int(F, rpow=1):      # int over sc < |xi| < 2 sc of F(xi1, xi2) |xi|^(rpow - 1) dxi (polar: rho^rpow drho)
    return sp.simplify(sp.integrate(ang_poly(F) * rho**rpow, (rho, sc, 2 * sc)))


E0 = lambda z2: (z2 - 1)**3 * (4 - z2)**3                    # eta0 as a polynomial in rho^2
psi_r = x2 / sc * E0((x1**2 + x2**2) / sc**2) / sc           # |b_n r_n^-1 psi(xi/r_n)| / b_n, without the i
L2n = annulus_int(psi_r**2)
Hm1 = annulus_int(psi_r**2, rpow=-1)
Hess = annulus_int(sum((xi_ * xj_ * psi_r)**2 for xi_ in (x1, x2) for xj_ in (x1, x2)))
dHess = annulus_int(sum(sp.diff(xi_ * xj_ * psi_r, xk)**2 for xi_ in (x1, x2) for xj_ in (x1, x2) for xk in (x1, x2)))
for name, val, pw in (("L2^2", L2n, 0), ("Hdot^-1^2", Hm1, -2), ("Hessian^2", Hess, 4), ("d_xi Hessian^2", dHess, 2)):
    ratio = sp.simplify(val / sc**pw)
    assert not ratio.has(sc) and ratio > 0
    print("(B4) summand of (4) for eta0 = (rho^2-1)^3 (4-rho^2)^3, divided by b_n^2: %-15s = r_n^%d x %s"
          % (name, pw, sp.nsimplify(ratio)))
print("     with b_n = r_n the Hdot^-1 terms b_n^2 r_n^-2 x const are constant and (5) diverges,"
      " while the Hessian terms"
      " b_n^2 (r_n^4 + r_n^2) sum to a finite value")
w_N = (2**14, 2**18)
w_X = (2**15, 2**20)
kap = max(fmpq(w_X[0], w_N[0]), fmpq(w_X[1], w_N[1]), 1)
assert kap == 4
print("(B5) common exponent u: X_u(f)^2 <= max(1, 2^15/2^14, 2^20/2^18) N_u(f)^2 = 4 N_u(f)^2, so X_u <= 2 N_u")
print("(B) done, %.1f s" % (time.monotonic() - T0), flush=True)

# =============================== (C) Remark R2 ===============================
ctx.prec = 200
sA, tA = arb(s.p) / s.q, arb(t.p) / t.q
etaA2 = arb(1) / 1572864                                    # A2 Theorem D(b): N_s(F) <= 2^-16/24
etaW = arb(4207) / 20000000                                 # sharpw: X_t(F) <= 2.1035e-4


def kappa(K):                    # X_t <= kappa(K) N_s on {Q3 <= K E_2}
    return 2 * (((2 * arb(K)**2 + 16410) ** (tA / 2)) + 34 * tA) / (1 - 34 * sA)


rows = []
for K in (0, 10**3, 10**6, 10**12, 10**100):
    kp = kappa(K)
    rows.append((K, kp, etaW / (kp * etaA2)))
    print("(C) K = %-7s kappa(K) = %s, enlargement eta_w/(kappa eta_A2) = %s"
          % ("1e%d" % len(str(K)[1:]) if K else "0", kp.str(8), (etaW / (kp * etaA2)).str(8)))
# largest K with kappa(K) eta_A2 <= eta_w: (2K^2 + 16410)^(t/2) <= Y
Y = etaW * (1 - 34 * sA) / (2 * etaA2) - 34 * tA
log10Kmax = (Y.log() * 2 / tA - arb(2).log()) / (2 * arb(10).log())
print("(C) N_s(F) <= eta_A2 and Q3 <= K E_2 imply X_t(F) <= eta_w for every K up to 10^%s (log10 of the bound)"
      % log10Kmax.str(6))
print("(C) done, %.1f s" % (time.monotonic() - T0), flush=True)

# =============================== (D) Section 4 ===============================
# unsigned subtraction inside S1 fails: K = P on a one-dimensional V
Kp = sp.Matrix([[1, 0], [0, 0]])
hs2 = sum(v**2 for v in Kp)
comp = Kp[0, 0]**2                                          # HS^2 of the compression to V = span(e1)
assert hs2 - comp == 0 and max(Kp.eigenvals()) == 1
print("(D1) K = P_V, dim V = 1: ||K||_HS^2 - ||P_V K P_V||_HS^2 = 0 but ||K||_op = 1 (unsigned compression"
      " subtraction inside S1 is invalid); signed bound with q = 1 gives sqrt(0 + 1) = 1")
rng = np.random.default_rng(259)
worst = -np.inf
for trial in range(4000):
    n1 = int(rng.integers(3, 12))
    n2 = int(rng.integers(2, 8))
    B1 = rng.standard_normal((n1, n1)); K1 = (B1 + B1.T) / 2 + rng.normal() * np.eye(n1)
    B2 = rng.standard_normal((n2, n2)); K2 = (B2 + B2.T) / 2
    kappa2 = np.sum(K1**2) + np.sum(K2**2) + abs(rng.normal())   # any kappa2 >= total HS^2
    m1 = int(rng.integers(1, n1)); m2 = int(rng.integers(1, n2 + 1))
    V = rng.standard_normal((n1, m1)); W = rng.standard_normal((n2, m2))
    G, Bm = V.T @ V, V.T @ K1 @ V                          # Gram and form matrices, non-orthonormal basis
    T_S1 = np.trace(np.linalg.solve(G, Bm) @ np.linalg.solve(G, Bm))
    Gw, Bw = W.T @ W, W.T @ K2 @ W
    T_oth = np.trace(np.linalg.solve(Gw, Bw) @ np.linalg.solve(Gw, Bw))
    qmin = max(np.max(np.linalg.eigvals(np.linalg.solve(G, Bm)).real), 0.0)
    qq = qmin + abs(rng.normal()) * (trial % 2)             # any q >= 0 with q G - B psd
    lmax = np.max(np.linalg.eigvalsh(K1))
    if lmax <= 0:
        continue
    worst = max(worst, lmax**2 - (kappa2 - T_oth - T_S1 + qq**2))
assert worst < 1e-9
print("(D2) FLOAT, 4000 random trials (S1 block 3..11, other block 2..7, random non-orthonormal compressions):"
      " max of lambda_max(K|S1)^2 - (kappa2 - T_other - T_S1 + q^2) = %.2e <= 0" % worst)
assert 651 * 168 == 2 * 54684 and 168**2 < 28248
assert (fmpq(50) / (651 * fmpq(45717, 10**8)))**2 < 28248
print("(D3) 651 * 168 = 109368 = 2 * 54684 and 168^2 = 28224 < 28248, so 50/(651 sqrt(28248)) < 25/54684 = %.9e;"
      " also 50/(651 sqrt(28248)) = %.9e < 4.5717e-4 (exact check)" % (25 / 54684, 50 / (651 * 28248**0.5)))

# =============================== (E) Section 5 and sector counts ===============================
fr = {"sharp": fmpq(147, 200000) / 2**9, "sharpw": fmpq(1351, 10**6) / 2**10, "A2": fmpq(1, 2**16) / 2**9}
assert fr["sharp"] == fmpq(147, 102400000) and fr["sharpw"] == fmpq(1351, 1024000000) and fr["A2"] == fmpq(1, 2**25)
print("(E1) r/sqrt(w2): sharp 147/200000/2^9 = %s = %.15f; sharpw 1351/10^6/2^10 = %s = %.16f; A2 2^-16/2^9 = %s"
      % (fr["sharp"], float(fr["sharp"]), fr["sharpw"], float(fr["sharpw"]), fr["A2"]))
c_run = fmpq(4076476460239181, 2**51)
dl = 1 - 1 / c_run
secs = [(K, L, 1 - K * dl - 2 * L) for K in range(1, 12) for L in range(0, 3)]
ge2 = sorted([(K, L) for K, L, qv in secs if qv >= -2])
ge1 = sorted([(K, L) for K, L, qv in secs if qv >= -1])
assert c_run * (1 - dl) - 1 == 0                            # the sector at exponent gamma is (c gamma - 1) Theta_0 = 0
print("(E2) run value of c, density labels (K, L), exponent 1 - K delta - 2L (c1-n1 label (K - 1, L)):"
      " exponent >= -2: %d sectors %s; exponent >= -1: %d sectors %s; the sector (1,0) at gamma vanishes"
      " identically (c gamma - 1 = 0)" % (len(ge2), ge2, len(ge1), ge1))
print("total %.1f s" % (time.monotonic() - T0))
