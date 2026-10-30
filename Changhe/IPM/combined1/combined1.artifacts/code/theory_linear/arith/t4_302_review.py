"""Review of c1-t4 T4-302 (research/s1_hessian_refinement/PROOF.md): the S1 squared constant 185/96 for
||r^2 D2 U[h]||^2 <= C ||r^2 D2 h||^2 from the balanced Young parameters lambda = 2/3, kappa = 4.
Run from artifacts/:  python3 -B -u arith/t4_302_review.py
Needs sympy and mpmath.
  (A) exact: Q_m and q_m = Q_m/4, the identities (6) of the PROOF, the coefficients (7) as functions of lambda, kappa,
      the values at (1, 4) and (2/3, 4), the division by 8 and the comparison with the lower rows 1 and 5/3.
  (B) the best constant of the same two-parameter Young scheme: min over lambda, kappa > 0 of max(A, B) (Lagrange
      conditions solved by mpmath, 40 digits, then checked by a grid; FLOAT).
Output: logs/t4_302_review.log (stdout).
"""
import time

import mpmath as mp
import sympy as sp

T0 = time.monotonic()
m, u, M, l, k = sp.symbols("m u M lambda kappa", positive=True)
Q = lambda mm: 4 * (mm**4 + 10 * mm**2 + 5 + (2 * mm**2 + 6) * u + u**2)
q = lambda mm: Q(mm) / 4
assert sp.expand(q(M) - q(M - 2) - 4 * (M - 1) * (M**2 + (M - 2)**2 + 10 + 2 * u)) == 0
assert sp.expand(11 * q(1) - q(3) - (64 * u + 10 * u**2)) == 0
assert sp.expand(5 * q(M) - q(M + 2) - (4 * (M - 3) * (M**3 + M**2 + 7 * M + 3) + (8 * M**2 - 8 * M + 16) * u
                                        + 4 * u**2)) == 0
disc = sp.discriminant(8 * M**2 - 8 * M + 16, M)
assert disc < 0
print("(A1) identities (6): q_M - q_(M-2), 11 q_1 - q_3 = 64 u + 10 u^2, 5 q_M - q_(M+2): exact; "
      "disc(8M^2 - 8M + 16) = %s < 0" % disc)
# energies: P has vectors of energy a + b and <= b; N has b and <= 11 a + 5 b
a, b = sp.symbols("a b", nonnegative=True)
PN = sp.expand((1 + l) * (a + b) + (1 + 1 / l) * b + (1 + k) * b + (1 + 1 / k) * (11 * a + 5 * b))
Acoef, Bcoef = PN.coeff(a), PN.coeff(b)
assert sp.simplify(Acoef - (12 + l + 11 / k)) == 0
assert sp.simplify(Bcoef - (8 + l + 1 / l + k + 5 / k)) == 0
for lv, kv in ((1, 4), (sp.Rational(2, 3), 4)):
    Av, Bv = Acoef.subs({l: lv, k: kv}), Bcoef.subs({l: lv, k: kv})
    print("(A2) lambda = %s, kappa = %s: coefficients %s, %s; squared constant max/8 = %s"
          % (lv, kv, Av, Bv, max(Av, Bv) / 8))
assert Acoef.subs({l: sp.Rational(2, 3), k: 4}) == sp.Rational(185, 12) == Bcoef.subs({l: sp.Rational(2, 3), k: 4})
assert sp.Rational(185, 96) < sp.Rational(63, 32) and sp.Rational(5, 3) < sp.Rational(185, 96)
print("(A3) 185/96 = %s < 63/32 = %s; lower rows 1 < 5/3 < 185/96: True"
      % (sp.N(sp.Rational(185, 96), 12), sp.N(sp.Rational(63, 32), 12)))
print("(A) done, %.1f s" % (time.monotonic() - T0))

# (B) best constant of the scheme: A = B and mu grad A + (1 - mu) grad B = 0
mp.mp.dps = 40
Af = lambda x, y: 12 + x + 11 / y
Bf = lambda x, y: 8 + x + 1 / x + y + 5 / y
eqs = lambda x, y, w: [Af(x, y) - Bf(x, y), w + (1 - w) * (1 - 1 / x**2), -11 * w / y**2 + (1 - w) * (1 - 5 / y**2)]
x0, y0, w0 = mp.findroot(eqs, (mp.mpf("0.7"), mp.mpf("4.05"), mp.mpf("0.5")))
cstar = Af(x0, y0)
print("(B) optimum lambda* = %s, kappa* = %s, mu = %s" % (mp.nstr(x0, 15), mp.nstr(y0, 15), mp.nstr(w0, 15)))
print("(B) min max(A, B) = %s, squared constant %s (185/96 = %s, difference %s)"
      % (mp.nstr(cstar, 15), mp.nstr(cstar / 8, 15), mp.nstr(mp.mpf(185) / 96, 15),
         mp.nstr(mp.mpf(185) / 96 - cstar / 8, 6)))
assert 0 < w0 < 1 and x0 > 0 and y0 > 0
grid = min(max(Af(mp.mpf(i) / 1000, mp.mpf(j) / 1000), Bf(mp.mpf(i) / 1000, mp.mpf(j) / 1000))
           for i in range(650, 751) for j in range(3950, 4151, 2))
print("(B) grid lambda in [0.65, 0.75], kappa in [3.95, 4.15]: min max = %s (>= optimum: %s)"
      % (mp.nstr(grid, 15), grid >= cstar - mp.mpf(10)**-30))
assert grid >= cstar - mp.mpf(10)**-30
print("(B) done; total %.1f s" % (time.monotonic() - T0))
