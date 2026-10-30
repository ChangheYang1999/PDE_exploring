"""c1-t1 R1-036: independent checks for c1-t4 T4-322 (research/scaled_rank_audit/PROOF.md).

Reads data/T4322_shapes.json (generator shapes of C1-N1-016, C1-N1-017 and old_basis.json, made by
extract_T4322_shapes.py).
Exact arithmetic only (fractions, sympy). Checks:
 1. census: the non-legqs shapes of 016 and 017 coincide with old_basis.json (1922, branches 0..7); the
    252 legqs shapes are exactly w = 0, Q = 4, R0 = 25 (016) or 50 (017), j in {1,2,3}, m in {9..15}, N in {0..11};
 2. p_j = (3 + gamma - j delta)/2 is not an integer and p_j - p_k is not an integer (j != k), so the classes
    m - p_j mod 1 and the integer class are pairwise distinct;
 3. the rational factor of each legqs generator, written in v = 1/(1 + r^2) from the c1-n1 definition
    (ts = r^2/(R0^2 + r^2), us = R0^2/(R0^2 + r^2), us^4 P_N(2 ts - 1)), has a pole of order exactly N + 4 at
    v0 = -1/(R0^2 - 1) with the leading coefficient of PROOF.md (1), after the factor (1 - v)^m;
 4. the density of G_(1,9,0) has lowest term 4*19*18*(p_1 - 9 - 4/R0^2) r^17 sin(17 theta), nonzero;
 5. d = 2 p_0 = 3 + gamma < 4 and 2 p_j - 8 < 2 p_0 (growth used in section 4)."""
import json
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

D = json.loads(Path(__file__).with_name("data").joinpath("T4322_shapes.json").read_text())
print("sources", D["sources"])
c = Fr(4076476460239181, 2**51)
g = 1 / c
dl = 1 - g
P = [(3 + g - j * dl) / 2 for j in range(8)]

# 1. census
old = {}
for name, R0 in [("candidate016.json", 25), ("candidate017.json", 50)]:
    sh = D["shapes"][name]
    assert Fr(sh["cl_exact"]) == c
    gens = sh["gens"]
    o = sorted((j, m, tuple(s)) for j, m, s in gens if s[0] != "legqs")
    n = sorted((j, m, tuple(s)) for j, m, s in gens if s[0] == "legqs")
    assert len(gens) == 2174 and len(o) == 1922 and len(set(o)) == 1922 and len(n) == 252
    want = sorted((j, m, ("legqs", 0, N, 4, R0)) for j in (1, 2, 3) for m in range(9, 16) for N in range(12))
    assert n == want, name
    assert {j for j, _, _ in o} == set(range(8))
    old[name] = o
    print(name, "1922 old shapes, branches 0..7; 252 legqs shapes = {1,2,3} x {9..15} x {0..11}, w 0, Q 4, R0", R0)
assert old["candidate016.json"] == old["candidate017.json"]
ob = sorted((j, m, tuple(s)) for j, m, s in D["shapes"]["old_basis.json"]["gens"])
assert len(ob) == 1922 and ob == old["candidate016.json"]
print("old shapes of 016 and 017 identical, and equal to the 1922 shapes of old_basis.json")

# 2. nonintegrality
for j in range(8):
    assert P[j].denominator != 1
    for k in range(j):
        assert (P[j] - P[k]).denominator != 1
fr = [p - (p.numerator // p.denominator) for p in P]
assert len(set(fr)) == 8 and Fr(0) not in fr
print("p_j:", [f"{float(p):.6f}" for p in P])
print("8 nonintegral p_j, 28 nonintegral differences, 8 distinct nonzero fractional parts: ok")

# 3. pole order and coefficient (1)
v = sp.symbols("v")
for R0 in (25, 50):
    a = sp.Integer(R0**2 - 1)
    v0 = -1 / a
    r2 = (1 - v) / v
    ts = r2 / (R0**2 + r2)
    us = sp.Integer(R0**2) / (R0**2 + r2)
    cnt = 0
    for N in range(12):
        PN = sp.legendre(N, sp.Symbol("x"))
        assert PN.subs("x", 1) == 1
        base = sp.cancel(us**4 * PN.subs("x", 2 * ts - 1))
        num, den = sp.fraction(base)
        num, den = sp.Poly(num, v), sp.Poly(den, v)
        # pole order at v0 = multiplicity of (v - v0) in den minus that in num
        def mult(pl):
            k = 0
            while pl.eval(v0) == 0:
                pl = sp.Poly(sp.quo(pl.as_expr(), v - v0), v)
                k += 1
            return k, pl
        kd, dred = mult(den)
        kn, nred = mult(num)
        assert kn == 0 and kd == N + 4, (R0, N, kn, kd)
        lead0 = nred.eval(v0) / dred.eval(v0)
        for m in range(9, 16):
            lead = (1 - v0)**m * lead0
            want = sp.Integer(R0)**8 * v0**4 * sp.binomial(2 * N, N) * (1 - v0)**(m + N) / a**(4 + N)
            assert sp.simplify(lead - want) == 0 and lead != 0
            cnt += 1
    print(f"R0 = {R0}: {cnt} pole coefficients (1) agree, pole order N + 4 exactly")

# 4. lowest density term of G_(1,9,0)
r, th = sp.symbols("r theta", positive=True)
p1 = sp.Rational(P[1].numerator, P[1].denominator)
for R0 in (25, 50):
    f = sp.series(r**18 * (1 + r**2)**(p1 - 9) * (sp.Integer(R0)**2 / (R0**2 + r**2))**4, r, 0, 23).removeO()
    F = sp.expand(sp.diff(f, r, 2) + sp.diff(f, r) / r - 324 * f / r**2)
    s17 = sp.expand(sp.diff(F, r) / 2 + 18 * F / (2 * r))
    s19 = sp.expand(-sp.diff(F, r) / 2 + 18 * F / (2 * r))
    c17 = s17.coeff(r, 17)
    want = 4 * 19 * 18 * (p1 - 9 - sp.Rational(4, R0**2))
    assert sp.simplify(c17 - want) == 0 and c17 != 0
    assert all(s17.coeff(r, k) == 0 for k in range(17)) and all(s19.coeff(r, k) == 0 for k in range(19))
    print(f"R0 = {R0}: sin(17 theta) coefficient of r^17 = {float(c17):.10g} = 4*19*18*(p_1 - 9 - 4/R0^2); "
          "no lower term; the sin(19 theta) part is O(r^19)")

# 5. growth
assert 2 * P[0] == 3 + g and 3 + g < 4 and all(2 * P[j] - 8 < 2 * P[0] for j in (1, 2, 3))
print("d = 3 + gamma =", float(3 + g), "< 4; new generators O(r^(2 p_j - 8))")
print("all checks passed")
