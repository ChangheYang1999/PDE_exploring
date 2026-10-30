"""Independent review of T4-256 (c1-t4 research/finite_log_tails/PROOF.md, sha256 fa36215d...0d261): finite
polynomial-logarithmic tails modulo E_a are forced to be the pure-power ladder (reviews/REVIEW_T4_256.md).

Run from artifacts/:  python3 -B arith/t4_256_review.py
Needs sympy, python-flint.

Parts (all exact or sympy; no FLOAT claims):
  (A1) the polar form (4): Lap(r^(e+1) Q(log r, th)) = r^(e-1)[A_e Q + 2(e+1) Q_L + Q_LL] and
       -d_x(r^e P) = r^(e-1)[-cos(th)(e P + P_L) + sin(th) P_th], for Q, P polynomials of degree 3 in L = log r with
       undetermined angular coefficients;
  (A2) the velocity (8), the product r^(e+f-1) B_(e,f) of Section 2 and the dilation identity (9), same generality;
  (A3) the recursion (5) for sample exponents and sample S1 polynomials P (exact sine series), and an independent
       check that psi = r^(e+1) Q solves Lap psi = -d_x(r^e P) at random rational points (sympy, 60 digits);
  (A4) the weighted integrability claims of Sections 2 and 3, including the logarithmic endpoint q = a - 1;
  (A5) the descending induction (12) for a sample exponent set: the linear map P -> (cq - 1)P + c P_L on
       polynomials of degree <= d is invertible for q != gamma and has kernel = constants at q = gamma.
Output: logs/t4_256_review.log.
"""
import time

import numpy as np
import sympy as sp
from flint import fmpq

T0 = time.monotonic()
r, th, e, f, c = sp.symbols("r theta e f c", positive=True)
Lr = sp.log(r)
DEG = 3
qk = [sp.Function("q%d" % k)(th) for k in range(DEG + 1)]
pk = [sp.Function("p%d" % k)(th) for k in range(DEG + 1)]
sk = [sp.Function("s%d" % k)(th) for k in range(DEG + 1)]
Ls = sp.Symbol("L")


def lap(F):
    return sp.diff(F, r, 2) + sp.diff(F, r) / r + sp.diff(F, th, 2) / r**2


def dx(F):
    return sp.cos(th) * sp.diff(F, r) - sp.sin(th) / r * sp.diff(F, th)


def dy(F):
    return sp.sin(th) * sp.diff(F, r) + sp.cos(th) / r * sp.diff(F, th)


def poly(cs):                    # sum c_k(th) L^k as a function of the symbol L
    return sum(cc * Ls**k for k, cc in enumerate(cs))


def at_log(Fp):                  # substitute L = log r
    return Fp.subs(Ls, Lr)


Qp, Pp, Sp_ = poly(qk), poly(pk), poly(sk)
lhs = lap(r**(e + 1) * at_log(Qp))
rhs = r**(e - 1) * at_log(sp.diff(Qp, th, 2) + (e + 1)**2 * Qp + 2 * (e + 1) * sp.diff(Qp, Ls) + sp.diff(Qp, Ls, 2))
assert sp.simplify(sp.expand(lhs - rhs)) == 0
lhs = -dx(r**e * at_log(Pp))
rhs = r**(e - 1) * at_log(-sp.cos(th) * (e * Pp + sp.diff(Pp, Ls)) + sp.sin(th) * sp.diff(Pp, th))
assert sp.simplify(sp.expand(lhs - rhs)) == 0
print("(A1) (4) for degree-%d polynomials in log r with undetermined angular coefficients: verified" % DEG)

psi = r**(e + 1) * at_log(Qp)
u1, u2 = -dy(psi), dx(psi)
ur = sp.cos(th) * u1 + sp.sin(th) * u2
ut = -sp.sin(th) * u1 + sp.cos(th) * u2
assert sp.simplify(sp.expand(ur + r**e * at_log(sp.diff(Qp, th)))) == 0
assert sp.simplify(sp.expand(ut - r**e * at_log((e + 1) * Qp + sp.diff(Qp, Ls)))) == 0
Fm = r**f * at_log(Pp)
adv = ur * sp.diff(Fm, r) + ut * sp.diff(Fm, th) / r
Bef = -sp.diff(Qp, th) * (f * Pp + sp.diff(Pp, Ls)) + ((e + 1) * Qp + sp.diff(Qp, Ls)) * sp.diff(Pp, th)
assert sp.simplify(sp.expand(adv - r**(e + f - 1) * at_log(Bef))) == 0
Fe = r**e * at_log(Sp_)
dil = c * r * sp.diff(Fe, r) - Fe
assert sp.simplify(sp.expand(dil - r**e * at_log((c * e - 1) * Sp_ + c * sp.diff(Sp_, Ls)))) == 0
print("(A2) (8) velocity components, transport product r^(e+f-1) B_(e,f) and (9): verified (degree %d)" % DEG)
print("(A) done, %.1f s" % (time.monotonic() - T0), flush=True)


# ---- (A3) recursion (5) on exact sine series ----
def QQ(x):                       # fmpq -> sympy Rational
    return sp.Rational(int(x.p), int(x.q))


def put(o, n, v):
    if n == 0 or v == 0:
        return
    if n < 0:
        n, v = -n, -v
    o[n] = o.get(n, fmpq(0)) + v
    if o[n] == 0:
        del o[n]


def times_cos1(S):               # cos(th) * sum S_n sin(n th)
    o = {}
    for n, v in S.items():
        put(o, n + 1, v / 2)
        put(o, n - 1, v / 2)
    return o


def times_sin1_dth(S):           # sin(th) * d/dth sum S_n sin(n th) = sum n S_n sin(th) cos(n th)
    o = {}
    for n, v in S.items():
        put(o, n + 1, n * v / 2)
        put(o, 1 - n, n * v / 2)
    return o


def lin(*terms):
    o = {}
    for s, S in terms:
        for n, v in S.items():
            put(o, n, s * v)
    return o


def solve_Q(P, ee):              # P = [P_0, ..., P_d] sine series (odd n); returns Q by (5)
    d = len(P) - 1
    H = []
    for k in range(d + 1):
        PL = P[k + 1] if k < d else {}
        H.append(lin((-ee * 1, times_cos1(P[k])), (fmpq(-(k + 1)), times_cos1(PL)), (fmpq(1), times_sin1_dth(P[k]))))
    Q = [dict() for _ in range(d + 3)]
    for k in range(d, -1, -1):
        rhs = lin((fmpq(1), H[k]), (-2 * (ee + 1) * (k + 1), Q[k + 1]), (fmpq(-(k + 2) * (k + 1)), Q[k + 2]))
        assert all(m % 2 == 0 for m in rhs)
        Q[k] = {m: v / ((ee + 1)**2 - m * m) for m, v in rhs.items()}
    return Q[:d + 1], H


rng = np.random.default_rng(256)
samples = [fmpq(-13, 10), fmpq(-1), fmpq(-7, 3), fmpq(1, 3), fmpq(9, 10)]
for ee in samples:
    P = [{n: fmpq(int(rng.integers(-9, 10)), int(rng.integers(1, 9))) for n in (1, 3, 5)} for _ in range(3)]
    Q, H = solve_Q(P, ee)
    es = QQ(ee)
    Pexpr = sum(sum(QQ(v) * sp.sin(n * th) for n, v in Pk.items()) * Lr**k for k, Pk in enumerate(P))
    Qexpr = sum(sum(QQ(v) * sp.sin(m * th) for m, v in Qk.items()) * Lr**k for k, Qk in enumerate(Q))
    resid = lap(r**(es + 1) * Qexpr) + dx(r**es * Pexpr)
    worst = 0
    for _ in range(6):
        sub = {r: sp.Rational(int(rng.integers(11, 90)), 9), th: sp.Rational(int(rng.integers(1, 600)), 97)}
        val = abs(sp.N(resid.subs(sub), 60))
        worst = max(worst, float(val))
        assert val < 1e-40
    print("(A3) e = %s: degree-2 S1 P with harmonics 1, 3, 5; Q from (5) has even harmonics %s and solves"
          " Lap psi = -d_x(r^e P) at 6 random rational points, max |residual| %.1e"
          % (ee, sorted({m for Qk in Q for m in Qk}), worst))
print("(A3) done, %.1f s" % (time.monotonic() - T0), flush=True)

# ---- (A4) integrability ----
for aa in (sp.Rational(-19, 10), sp.Rational(-1, 2), sp.Rational(3, 2)):
    for k in (1, 2):
        assert sp.integrate(r**(2 * (aa - 1) - 2 * aa + 1) * sp.log(r)**(2 * k), (r, sp.E, sp.oo)) == sp.oo
        assert sp.integrate(r**(2 * (aa - 1 - sp.Rational(1, 10)) - 2 * aa + 1) * sp.log(r)**(2 * k),
                            (r, sp.E, sp.oo)).is_finite
print("(A4) int r^(2q-2a+1) (log r)^(2k) dr over r > e: diverges at q = a - 1 and converges at q = a - 1 - 1/10"
      " (a = -19/10, -1/2, 3/2; k = 1, 2)")

# ---- (A5) the descending step (12) ----
c_run = fmpq(4076476460239181, 2**51)
gam = 1 / c_run
for q in (gam, gam + fmpq(1, 7), 2 * gam - 1, gam - 2, fmpq(-13, 10)):
    for d in (1, 2, 3):
        M = sp.zeros(d + 1, d + 1)  # P = sum p_k L^k -> (cq - 1) P + c P_L on the basis L^0..L^d
        for k in range(d + 1):
            M[k, k] = QQ(c_run * q - 1)
            if k >= 1:
                M[k - 1, k] = QQ(c_run * k)
        rank = M.rank()
        if q == gam:
            assert rank == d and M.nullspace()[0][1:, 0] == sp.zeros(d, 1)
        else:
            assert rank == d + 1
print("(A5) (cq - 1)P + c P_L on polynomials of degree <= 1, 2, 3: invertible for q = gamma + 1/7, 2 gamma - 1,"
      " gamma - 2, -13/10; at q = gamma its kernel is the constants (run value of c)")
print("total %.1f s" % (time.monotonic() - T0))
