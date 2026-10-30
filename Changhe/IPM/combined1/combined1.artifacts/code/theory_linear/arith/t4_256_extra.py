"""Supplement to reviews/REVIEW_T4_256.md, remark R3: the stream construction of Section 1 of T4-256 is log-free
exactly for -3 < e < 1; at the two ends a sine-even angular resonance forces a log r in the canonical stream.

Run from artifacts/:  python3 -B arith/t4_256_extra.py
Needs sympy. Output: logs/t4_256_extra.log.
"""
import sympy as sp

r, th, e = sp.symbols("r theta e", real=True)
r = sp.Symbol("r", positive=True)


def lap(F):
    return sp.diff(F, r, 2) + sp.diff(F, r) / r + sp.diff(F, th, 2) / r**2


def dx(F):
    return sp.cos(th) * sp.diff(F, r) - sp.sin(th) / r * sp.diff(F, th)


def sin_coef(expr, m):
    return sp.simplify(sp.integrate(sp.expand(sp.expand_trig(expr)) * sp.sin(m * th), (th, 0, 2 * sp.pi)) / sp.pi)


# coefficient of sin(2 theta) in r^(1-e) * (-d_x(r^e sin(n theta))) for n = 1, 3, as a function of e
for n in (1, 3):
    rhs = sp.simplify(-dx(r**e * sp.sin(n * th)) * r**(1 - e))
    print("n = %d: -d_x(r^e sin(n th)) = r^(e-1) * [%s]; sin(2 th) coefficient %s"
          % (n, sp.simplify(sp.expand(sp.expand_trig(rhs))), sp.factor(sin_coef(rhs, 2))))
# e = -3, density r^-3 sin(theta): A_(-3) = d_th^2 + 4 kills sin(2 th), and the right side contains 2 sin(2 th)
src = -dx(r**-3 * sp.sin(th))
psi_log = -sp.Rational(1, 2) * r**-2 * sp.log(r) * sp.sin(2 * th)
assert sp.simplify(lap(psi_log) - src) == 0
a2, b2 = sp.symbols("a2 b2")
psi_pow = r**-2 * (a2 * sp.sin(2 * th) + b2 * sp.sin(4 * th))
res = sp.simplify(sp.expand((lap(psi_pow) - src) * r**4))
print("e = -3: Lap(r^-2 (a2 sin 2th + b2 sin 4th)) + d_x(r^-3 sin th) = r^-4 * [%s]: never zero" % sp.factor(res))
print("e = -3: psi = -(1/2) r^-2 log(r) sin(2 th) solves Lap psi = -d_x(r^-3 sin th) exactly")
# e = 1, density r sin(3 theta): A_1 = d_th^2 + 4, right side contains -2 sin(2 th)
src = -dx(r * sp.sin(3 * th))
rhs = sp.simplify(sp.expand(sp.expand_trig(src)))
psi_log = r**2 * sp.log(r) * (-sp.Rational(1, 2)) * sp.sin(2 * th)
chk = sp.simplify(sp.expand(sp.expand_trig(lap(psi_log) - src)))
print("e = 1: -d_x(r sin 3th) = %s; Lap(-(1/2) r^2 log(r) sin 2th) - that = %s (a pure sin 4th term, solvable"
      " without logs)" % (rhs, chk))
assert sin_coef(chk, 2) == 0
print("so in T4-256 the open range -3 < e < 1 (e + 1 in (-2, 2)) is exactly the log-free range; e in [a - 1, 1) with"
      " a > -2 stays inside it")
