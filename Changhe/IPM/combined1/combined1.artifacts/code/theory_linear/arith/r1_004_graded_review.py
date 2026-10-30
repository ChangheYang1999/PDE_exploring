"""Independent review of the c1-t1 uniform graded point bound (REVIEWS_v02.md R1-004, "consequences" paragraph;
theory_v01 section 5 NC-T-PT, last table row; closure matrix rows 21 and 22).

Run from artifacts/:  python3 -B arith/r1_004_graded_review.py
Needs sympy, python-flint.  A few seconds.

Claim reviewed (c1-t1): in every FW-T-TB-graded-v1 box (T4-013 conditional theorem, c1-t4
research/graded_closure_audit/PROOF.md (3)), positivity of the top margin m2 = 1/2 - 4708 s - (A_s + B_s) nu alone gives
nu = n/sqrt(s) < (1/2)/(127/50 + 9/5), hence C1s n < 0.016250 and C0 n < 3.35e-4, where n = (r2^2 + 2 r1^2 + r0^2)^(1/2)
bounds ||h||_(H^(2+s)) on the box.  With the T4-017 point bound (2) this excludes Mpen2 at (0, 2) and b6 at (0, 1) from
every box (gaps 0.030548, 2.93767) and does not exclude d2 at (0, 1) (gap -0.0098351).

Checks:
  (1) exact (sympy): C0^2 = 1/(4 pi (1+s)), C1^2 = 1/(8 pi s (1+s)) (Beta integrals); (1+|xi|^2)^2 = 1 + 2|xi|^2 + |xi|^4
      with |xi|^4 = sum_ij xi_i^2 xi_j^2 (ordered tensor), so ||h||_(H^(2+s)) <= (P^2 + 2a^2 + b^2)^(1/2) for the
      components (P, a, b) of J^s h (omega >= 1); hence n bounds ||h||_(H^(2+s)) on the box;
  (2) exact: m2 > 0 implies s < 1/9416 and nu < (1/2 - 4708 s)/(A_s + B_s) <= 25/217;
  (3) arb: the c1-t1 coefficients and gaps on data/t4_017_cartesian_witnesses.json (copied from c1-t4, sha256 4596e2d6...);
  (4) arb: the s -> 0 limit of the per-s bound, which shows that no choice of s helps the point test for d2;
  (5) new, exact: uniform L2 and H^(2+s) smallness on every graded box, n < sup_s sqrt(s)(1/2 - 4708 s)/(217/50)
      = (50/217)/(3 sqrt(28248)) < 50/109368 < 1/2000, against the CONFIRMED fixed-c L2 distances of d2
      (0.0027197370, N4-057 with T4-048; 0.0029920, T4-048 with N4-061);
  (6) consistency: the registered instances (i), (ii) and the gradedL2 instance satisfy the per-s bound.
"""
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import sympy as sp
from flint import arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]


def A(x):
    x = Q(x)
    return arb(x.numerator) / x.denominator


# ---------------- (1) point constants and the H^(2+s) bound ----------------
s, t = sp.symbols("s t", positive=True)
# (2 pi)^-2 int_R2 (1+|xi|^2)^(-2-s) dxi = (2 pi)^-2 pi int_0^oo (1+t)^(-2-s) dt  (t = |xi|^2)
C0sq = sp.simplify(sp.pi * sp.integrate((1 + t) ** (-2 - s), (t, 0, sp.oo)) / (4 * sp.pi**2))
# (2 pi)^-2 int xi_y^2 (1+|xi|^2)^(-2-s) dxi = (1/2)(2 pi)^-2 pi int_0^oo t (1+t)^(-2-s) dt
C1sq = sp.simplify(sp.pi * sp.integrate(t * (1 + t) ** (-2 - s), (t, 0, sp.oo)) / (2 * 4 * sp.pi**2))
print("(1) C0^2 =", C0sq, "; C1^2 =", C1sq)
assert sp.simplify(C0sq - 1 / (4 * sp.pi * (1 + s))) == 0
assert sp.simplify(C1sq - 1 / (8 * sp.pi * s * (1 + s))) == 0
x1, x2 = sp.symbols("xi1 xi2", real=True)
q = x1**2 + x2**2
lhs = sp.expand((1 + q) ** 2)
rhs = 1 + 2 * (x1**2 + x2**2) + sum(sp.expand(a**2 * b**2) for a in (x1, x2) for b in (x1, x2))
print("    (1+|xi|^2)^2 - (1 + 2|xi|^2 + sum_ij xi_i^2 xi_j^2) =", sp.simplify(lhs - rhs),
      "; so ||h||_(H^(2+s))^2 = b^2 + 2 a^2 + ||D^2 J^s h||^2 <= P^2 + 2 a^2 + b^2 (omega >= 1)")
assert sp.simplify(lhs - rhs) == 0

# ---------------- (2) the top margin ----------------
print("(2) m2 = 1/2 - 4708 s - (A_s + B_s) nu, A_s = 127/50 + (653/5) s, B_s = (9/5)(1 + 44 s)")
ss = sp.symbols("s", nonnegative=True)
AB = sp.Rational(127, 50) + sp.Rational(653, 5) * ss + sp.Rational(9, 5) * (1 + 44 * ss)
print("    A_s + B_s =", sp.expand(AB), "(increasing in s, value 217/50 at s = 0)")
assert sp.expand(AB) == sp.Rational(217, 50) + sp.Rational(1049, 5) * ss
nu_max = Q(1, 2) / Q(217, 50)
assert nu_max == Q(25, 217)
print("    m2 > 0 with nu >= 0 gives 4708 s < 1/2, s < 1/9416, and nu < (1/2 - 4708 s)/(A_s + B_s) <= 25/217 =",
      float(nu_max))

# ---------------- (3) c1-t1 coefficients and gaps ----------------
PI = arb.pi()
c1coef = A(nu_max) / (4 * PI.sqrt())                    # C1s n = nu/(4 sqrt(pi (1+s))) <= nu/(4 sqrt(pi))
c0coef = A(nu_max) * A(Q(1, 9416)).sqrt() / (4 * PI).sqrt()   # C0 n <= nu sqrt(s)/sqrt(4 pi), s < 1/9416
print("(3) coefficient of |V| < 25/(868 sqrt(pi)) =", c1coef.str(12), "(c1-t1: 0.016249700)")
print("    coefficient of (1 + |D rho|) <", c0coef.str(12), "(c1-t1: 0.00033492080)")
assert c1coef < A(Q(16250, 10**6)) and c0coef < A(Q(335, 10**6))
data = json.loads((HERE / "data/t4_017_cartesian_witnesses.json").read_text())
gaps = {}
fields = {}
for row in data["rows"]:
    fl = row["fields"]
    F, V, G = arb(fl["residual"]), arb(fl["velocity_norm"]), arb(fl["gradient_norm"])
    fields[row["candidate"]] = (F, V, G, row["point"])
    g = abs(F) - (c1coef * V + c0coef * (1 + G) + c0coef * c1coef)
    gaps[row["candidate"]] = g
    print(f"    {row['candidate']:>12} {row['point']}: |F| = {abs(F).str(10)}, |V| = {V.str(10)}, |D rho| = {G.str(10)},"
          f" uniform graded gap = {g.str(10)}, excluded: {bool(g > 0)}")
ref = {"C1-A2-d2": "-0.0098350810", "C1-A2-Mpen2": "0.030548113", "C1-A2-b6": "2.9376687"}
for k, v in ref.items():
    assert abs(gaps[k] - arb(v)) < arb("1e-7"), k
assert gaps["C1-A2-Mpen2"] > 0 and gaps["C1-A2-b6"] > 0 and gaps["C1-A2-d2"] < 0
print("    agree with c1-t1 check_T4013_T4017.out to the printed digits")

# ---------------- (4) the s -> 0 limit ----------------
# For fixed s the box bound is n < n(s) = sqrt(s)(1/2 - 4708 s)/(A_s + B_s).  The per-s point bound
# C1s n(s) |V| + C0 n(s)(1 + |D rho|) + C0 C1s n(s)^2 tends to (25/217)/(4 sqrt(pi)) |V| as s -> 0, and boxes with n
# arbitrarily close to n(s) exist (shrink r2 only).  So the test with m2 > 0 alone cannot exclude d2 if
# |F| < (25/217)/(4 sqrt(pi)) |V|.
F, V, G, pt = fields["C1-A2-d2"]
lim = c1coef * V
print("(4) d2 at", pt, ": s -> 0 limit of the per-s bound = 25/(868 sqrt pi) |V| =", lim.str(10), "> |F| =",
      abs(F).str(10), ":", bool(lim > abs(F)))
assert lim > abs(F)
print("    so no choice of s or of box shape lets the m2-only point test exclude d2 at (0, 1)")

# ---------------- (5) uniform L2 / H^(2+s) smallness ----------------
f = sp.sqrt(ss) * (sp.Rational(1, 2) - 4708 * ss)
crit = sp.solve(sp.diff(f, ss), ss)
assert crit == [sp.Rational(1, 28248)]
fmax = sp.nsimplify(f.subs(ss, crit[0]))
print("(5) sup_(s > 0) sqrt(s)(1/2 - 4708 s) at s = 1/28248:", fmax, "=", sp.N(fmax, 12))
assert sp.simplify(fmax - sp.Rational(1, 3) / sp.sqrt(28248)) == 0
# f is concave in sqrt(s) = u: f = u/2 - 4708 u^3, f'' = -6*4708*u < 0 for u > 0, so the critical point is the maximum
u = sp.symbols("u", positive=True)
assert sp.diff(u / 2 - 4708 * u**3, u, 2).is_negative
bound = sp.Rational(50, 217) * fmax
print("    hence n < sqrt(s)(1/2 - 4708 s)/(A_s + B_s) <= (50/217)/(3 sqrt(28248)) =", sp.N(bound, 12))
# 168^2 = 28224 < 28248, so 1/sqrt(28248) < 1/168
assert 168**2 < 28248
rat = Q(50, 217) * Q(1, 3) * Q(1, 168)
print("    < (50/217)(1/3)(1/168) =", rat, "=", float(rat), "< 1/2000:", rat < Q(1, 2000))
assert rat == Q(50, 109368) and rat < Q(1, 2000)
for name, dist in (("N4-057 (CONFIRMED by T4-048)", Q(27197370, 10**10)), ("T4-048 (CONFIRMED by N4-061)", Q(29920, 10**7))):
    print(f"    d2 fixed-c L2 distance {name}: {float(dist)} = {float(dist / rat):.2f} x the uniform graded bound")
    assert dist > rat
print("    every h in a FW-T-TB-graded-v1 box (m2 > 0) has ||h||_2 <= ||J^s h||_2 <= r0 <= n < 50/109368 and"
      " ||h||_(H^(2+s)) <= n < 50/109368; the same holds for FW-T-TB-gradedL2-v1 boxes ((G2) is unchanged)")

# ---------------- (6) consistency with the registered instances ----------------
inst = (("FW-T-TB-graded-v1 (i), c1-t1", Q(5, 2**18), (Q(2022, 10**7), Q(3347, 10**10), Q(1899, 10**11))),
        ("FW-T-TB-graded-v1 (ii), T4-013 rational box", Q(1, 50000), (Q(1, 5000), Q(1, 3000000), Q(1, 50000000))),
        ("FW-T-TB-gradedL2-v1 instance", Q(5, 2**18), (Q(2023, 10**7), Q(332, 10**9), Q(184, 10**10))))
for name, sv, (r2, r1, r0) in inst:
    n = (A(r2) ** 2 + 2 * A(r1) ** 2 + A(r0) ** 2).sqrt()
    ns = A(sv).sqrt() * (A(Q(1, 2)) - 4708 * A(sv)) / (A(Q(217, 50)) + A(Q(1049, 5)) * A(sv))
    m2 = A(Q(1, 2)) - 4708 * A(sv) - (A(Q(217, 50)) + A(Q(1049, 5)) * A(sv)) * n / A(sv).sqrt()
    print(f"(6) {name}: s = {sv}, n = {n.str(8)} < n(s) = {ns.str(8)}; m2 = {m2.str(8)}")
    assert n < ns and m2 > 0
print("done")
