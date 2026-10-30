"""c1-t1 R1-028: independent exact checks for T4-211 (triangular Taylor projection of the five origin equations).

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B check_T4211.py > check_T4211.out

1. Symbolic (sympy, c and a free): the leading linear variation ((2c-1) x d_x + y d_y - 1)(-d_y Delta M) + a M_xxy,
   divided by y, for the five leading monomials M = x^(2i) y^(2j); prints the coefficient matrix of
   X = x^2, Y = y^2 (degree 6) and X^2, XY, Y^2 (degree 8). Expected A = 24(a-4c+2), B = -240,
   [[60(a-8c+4), 0, 0], [0, -480c, 0], [0, 12(a-4), -1344]].
2. Exact squared density L2 norms / pi of eta_(i,j) = x^(2i) y^(2j) (1+r^2)^(p-i-j-2), p = (3+1/c)/2, at the 007 value
   of c: -d_y Delta eta = (1+r^2)^(q-3) H by three exact polynomial derivative steps, then the beta-moment formula
   int x^(2u) y^(2v) (1+r^2)^(-A) = pi (2u)!(2v)!/(4^(u+v) u! v!) / prod_(k=1..u+v+1) (A - k). Compared for exact
   equality with squared_L2_over_pi in R6/c1-t4/research/taylor_projection/verification/result.json (read only).
3. The triangle bound sum_i |t_i| B_i with the exact parameters t_i of verification/parameters.json (read only),
   evaluated with mpmath at 60 digits, compared with density_L2_upper_bound_ball of result.json.
Writes no file.
"""
import json, hashlib, sys
sys.set_int_max_str_digits(0)
from fractions import Fraction as Fr
from math import factorial
import sympy as sp
import mpmath as mp

T4 = "RUN_ROOT/theory_audit_T4/research/taylor_projection/verification/"
for f in ("result.json", "parameters.json"):
    print(f, "sha256", hashlib.sha256(open(T4 + f, "rb").read()).hexdigest())
res = json.load(open(T4 + "result.json")); par = json.load(open(T4 + "parameters.json"))
x, y, c, a = sp.symbols("x y c a")
PAIRS = [(2, 1), (0, 3), (3, 1), (1, 3), (0, 4)]
ok = True
# 1. leading linear matrix
lin = {}
for (i, j) in PAIRS:
    M = x**(2*i) * y**(2*j)
    rho = -sp.diff(sp.diff(M, x, 2) + sp.diff(M, y, 2), y)
    Fp = (2*c - 1) * x * sp.diff(rho, x) + y * sp.diff(rho, y) - rho + a * sp.diff(M, x, 2, y, 1)
    lin[(i, j)] = sp.Poly(sp.expand(sp.cancel(Fp / y)), x, y)
def co(P, e):
    return sp.factor(P.coeff_monomial(x**e[0] * y**e[1]))
deg2 = [[co(lin[p], e) for p in PAIRS[:2]] for e in ((2, 0), (0, 2))]
deg4 = [[co(lin[p], e) for p in PAIRS[2:]] for e in ((4, 0), (2, 2), (0, 4))]
print("degree-2 block (rows X, Y; columns alpha, beta):", deg2)
print("degree-4 block (rows X^2, XY, Y^2; columns gamma, delta, epsilon):", deg4)
exp2 = [[24*(a - 4*c + 2), 0], [0, -240]]
exp4 = [[60*(a - 8*c + 4), 0, 0], [0, -480*c, 0], [0, 12*(a - 4), -1344]]
m_ok = all(sp.expand(deg2[r][s] - exp2[r][s]) == 0 for r in range(2) for s in range(2)) and \
       all(sp.expand(deg4[r][s] - exp4[r][s]) == 0 for r in range(3) for s in range(3))
# the degree-6 directions have no degree-4 linear term and vice versa (leading parts are homogeneous)
other = all(co(lin[p], e) == 0 for p in PAIRS[:2] for e in ((4, 0), (2, 2), (0, 4))) and \
        all(co(lin[p], e) == 0 for p in PAIRS[2:] for e in ((2, 0), (0, 2), (0, 0)))
print("matrices as printed in PROOF.md:", m_ok, "; leading parts homogeneous (no cross-degree entries):", other)
ok &= m_ok and other
# 2. exact squared norms
cq = Fr(*map(int, par["c"].split("/")))
p = (3 + 1 / cq) / 2
def dstep(P, s, var):  # d_var [P (1+r^2)^s] = [(1+r^2) d_var P + 2 s var P] (1+r^2)^(s-1)
    return sp.expand((1 + x**2 + y**2) * sp.diff(P, var) + 2 * sp.Rational(s.numerator, s.denominator) * var * P)
B2 = []
for (i, j) in PAIRS:
    l = i + j; q = p - l - 2
    P = sp.Integer(1) * x**(2*i) * y**(2*j)
    Pxx = dstep(dstep(P, q, x), q - 1, x); Pyy = dstep(dstep(P, q, y), q - 1, y)  # Delta eta = (1+r^2)^(q-2) (.)
    H = -dstep(sp.expand(Pxx + Pyy), q - 2, y)                                    # rho = (1+r^2)^(q-3) H
    A = 2 * l + 7 - 1 / cq                                                         # (1+r^2)^(2(q-3)) = (1+r^2)^(-A)
    assert 2 * (q - 3) == -A
    H2 = sp.Poly(sp.expand(H * H), x, y)
    tot = Fr(0)
    for (ex, ey), cf in H2.terms():
        if ex % 2 or ey % 2:
            assert cf == 0  # H is even in x and odd in y, so H^2 has only even monomials
            continue
        u, v = ex // 2, ey // 2
        assert A > u + v + 1
        den = Fr(1)
        for k in range(1, u + v + 2):
            den *= (A - k)
        tot += Fr(int(sp.fraction(cf)[0]), int(sp.fraction(cf)[1])) * Fr(factorial(2*u) * factorial(2*v),
                                                                         4**(u + v) * factorial(u) * factorial(v)) / den
    ref = [d for d in res["direction_norms"] if tuple(d["pair"]) == (i, j)][0]["squared_L2_over_pi"]
    eq = tot == Fr(*map(int, ref.split("/")))
    ok &= eq
    B2.append(tot)
    print(f"eta_{(i, j)}: deg H = {H2.total_degree() // 2}; ||rho[eta]||^2/pi = {float(tot):.15e}; equals c1-t4 exact: {eq}")
# 3. triangle bound
mp.mp.dps = 60
t = {tuple(d["pair"]): Fr(*map(int, d["coefficient"].split("/"))) for d in par["parameters"]}
S = mp.fsum(abs(mp.mpf(t[pp].numerator) / t[pp].denominator) * mp.sqrt(mp.pi * mp.mpf(b.numerator) / b.denominator)
            for pp, b in zip(PAIRS, B2))
print("|t_i| =", [f"{float(abs(t[pp])):.6e}" for pp in PAIRS])
print("sum |t_i| B_i =", mp.nstr(S, 30), "; c1-t4 ball:", res["density_L2_upper_bound_ball"][:40])
refS = mp.mpf(res["density_L2_upper_bound_ball"].strip("[").split(" ")[0])
ok &= abs(S - refS) < mp.mpf("1e-60") and S < mp.mpf("3.424e-12")
print("ALL CHECKS PASS" if ok else "CHECK FAILED")
