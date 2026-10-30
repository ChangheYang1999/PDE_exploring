"""Rigorous radial integrals for multi-scale (legqs) terms (lane c1-n3; notes/LEGQS_EXTENSION_PLAN.md section 3).

Compactified variable v = 1/(1+r^2) in (0, 1], t = 1 - v. A scale R gives (R^2 + r^2)^(-N) = v^N (1 + a v)^(-N), a = R^2 - 1.
Building blocks:
  partial_fractions(Ms, As): prod_R (1 + a_R v)^(-M_R) = sum_R sum_{i=1}^{M_R} c_(R,i) (1 + a_R v)^(-i), exact rationals (pairwise
      reduction 1/((1+a v)(1+b v)) = (a/(a-b))/(1+a v) - (b/(a-b))/(1+b v), repeated).
  J(bp, k, a, i) = int_0^1 v^bp (1-v)^k (1+a v)^(-i) dv = B(bp+1, k+1) 2F1(i, bp+1; bp+k+2; -a)  (arb ball; a = 0: Beta only).
  integral_poly(P, bp, Ms, As): int_0^1 v^bp P(v) prod_R (1+a_R v)^(-M_R) dv for an exact rational polynomial P in v (ball).
Self test (python3 legqs_integrals.py): partial fractions against direct evaluation; J against mpmath quadrature; integral_poly against
the exact Beta route when all M_R = 0.
"""
from fractions import Fraction as Q
from functools import lru_cache
import sys
from flint import arb, fmpq, fmpq_poly, ctx
sys.set_int_max_str_digits(0)
ctx.prec = 512   # default working precision for every ball in this module

def aq(q): q = Q(q); return arb(q.numerator) / q.denominator

def partial_fractions(Ms, As):
    """prod_R (1 + a_R v)^(-M_R) -> dict (R index, i) -> Fraction coefficient of (1 + a_R v)^(-i). Exact."""
    terms = {}
    # start with the first scale alone, then multiply in the others one factor at a time
    idx = [r for r, M in enumerate(Ms) if M > 0]
    if not idx: return {}
    cur = {(idx[0], Ms[idx[0]]): Q(1)}
    for r in idx[1:]:
        for _ in range(Ms[r]):
            new = {}
            for (s, i), c in cur.items():
                if s == r:
                    new[(s, i + 1)] = new.get((s, i + 1), Q(0)) + c
                else:
                    # 1/((1+a v)^i (1+b v)) with a = A_s (power i), b = A_r:
                    # 1/((1+a v)(1+b v)) = (a/(a-b))/(1+a v) - (b/(a-b))/(1+b v); apply to one factor of (1+a v)^(-i) recursively:
                    a, b = Q(As[s]), Q(As[r])
                    # (1+a v)^(-i) (1+b v)^(-1) = (a/(a-b)) (1+a v)^(-i) ... use the reduction on the pair (1+a v)^(-1)(1+b v)^(-1) and
                    # keep the remaining (1+a v)^(-(i-1)) factor: result = (a/(a-b)) (1+a v)^(-i) - (b/(a-b)) (1+a v)^(-(i-1)) (1+b v)^(-1)
                    new[(s, i)] = new.get((s, i), Q(0)) + c * a / (a - b)
                    # the second part still has a (1+b v)^(-1) factor: reduce recursively by the same identity (depth i-1), expanding fully
                    rest_c = -c * b / (a - b); ii = i - 1
                    while ii > 0:
                        new[(s, ii)] = new.get((s, ii), Q(0)) + rest_c * a / (a - b)
                        rest_c = rest_c * (-b / (a - b)); ii -= 1
                    new[(r, 1)] = new.get((r, 1), Q(0)) + rest_c
            cur = {k: v for k, v in new.items() if v}
    return cur

def J(bp, k, a, i, prec=512):
    """int_0^1 v^bp (1-v)^k (1+a v)^(-i) dv as an arb ball; bp > -1 rational, k >= 0 integer, a >= 0 rational, i >= 0 integer."""
    old = ctx.prec; ctx.prec = prec
    b1 = aq(bp) + 1; k1 = arb(k + 1)
    beta = (b1.gamma() * k1.gamma() / (b1 + k1).gamma())
    if i == 0 or Q(a) == 0: res = beta
    else:
        # Pfaff transformation to z in (0, 1): 2F1(i, b1; b1+k1; -a) = (1+a)^(-i) 2F1(i, k1; b1+k1; a/(1+a))
        A = aq(a); z = A / (1 + A); res = beta * (1 + A) ** (-i) * z.hypgeom_2f1(arb(i), k1, b1 + k1)   # python-flint: z.hypgeom_2f1(a, b, c)
    ctx.prec = old
    return res

def integral_poly(P, bp, Ms, As, prec=512):
    """int_0^1 v^bp P(v) prod_R (1+a_R v)^(-M_R) dv, P an fmpq_poly in v. Ball. Uses partial fractions and J with k = 0 (monomials)."""
    old = ctx.prec; ctx.prec = prec
    coeffs = P.coeffs()
    pf = partial_fractions(Ms, As) if any(Ms) else {(-1, 0): Q(1)}
    total = arb(0)
    for (r, i), c in pf.items():
        a = As[r] if r >= 0 else 0
        for n, cn in enumerate(coeffs):
            if not cn: continue
            total += aq(c) * aq(Q(str(cn))) * J(Q(bp) + n, 0, a, i, prec)
    ctx.prec = old
    return total

if __name__ == '__main__':
    import random, mpmath
    random.seed(5); ok = True
    # test 1: partial fractions
    for trial in range(6):
        As = [Q(99), Q(624), Q(2499)][:random.randint(1, 3)]; Ms = [random.randint(0, 4) for _ in As]
        if not any(Ms): continue
        pf = partial_fractions(Ms, As)
        for v in (Q(1, 7), Q(3, 5), Q(1, 1000)):
            direct = Q(1)
            for a, M in zip(As, Ms): direct /= (1 + a * v) ** M
            viapf = sum(c / (1 + As[r] * v) ** i for (r, i), c in pf.items())
            if direct != viapf: ok = False; print('PF MISMATCH', Ms, As, v)
    print('partial fractions exact:', ok)
    # test 2: J against mpmath
    mpmath.mp.dps = 40; ok2 = True
    for (bp, k, a, i) in [(Q(1, 3), 2, Q(99), 3), (Q(-1, 2) + Q(1824676646553933, 4076476460239181), 5, Q(9999), 7), (Q(7, 4), 0, Q(0), 0), (Q(2, 5), 1, Q(624), 1)]:
        ref = mpmath.quad(lambda v: v ** float(bp) * (1 - v) ** k * (1 + float(a) * v) ** (-i), [0, 1e-3, 1e-1, 1])
        val = J(bp, k, a, i)
        if not (abs(float(val.mid()) - float(ref)) <= 1e-9 * abs(float(ref)) + 1e-30): ok2 = False; print('J MISMATCH', bp, k, a, i, val, ref)
    print('J against mpmath quadrature:', ok2)
    # test 3: integral_poly with Ms = 0 against exact Beta (e2norms.integral in t with t = 1 - v): int v^bp P(v) dv
    sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent)); import e2norms as E
    P = fmpq_poly([fmpq(random.randint(-50, 50), random.randint(1, 9)) for _ in range(6)])
    bp = Q(3, 7)
    exact = sum(Q(str(c)) * Q(1) / (bp + n + 1) for n, c in enumerate(P.coeffs()))     # int v^(bp+n) dv = 1/(bp+n+1)
    val = integral_poly(P, bp, [0, 0], [Q(99), Q(624)])
    print('integral_poly (no scales) contains the exact value:', val.contains(aq(exact)), val.str(12))
    # test 4: integral_poly with scales against mpmath
    Ms = [2, 1]; As = [Q(99), Q(624)]
    val = integral_poly(P, bp, Ms, As)
    pf = lambda v: sum(float(Q(str(c))) * v ** n for n, c in enumerate(P.coeffs()))
    ref = mpmath.quad(lambda v: v ** float(bp) * pf(v) / ((1 + 99 * v) ** 2 * (1 + 624 * v)), [0, 1e-4, 1e-2, 1e-1, 1])
    print('integral_poly with scales vs mpmath:', val.str(12), float(ref), 'rel diff', abs(float(val.mid()) - float(ref)) / abs(float(ref)))
