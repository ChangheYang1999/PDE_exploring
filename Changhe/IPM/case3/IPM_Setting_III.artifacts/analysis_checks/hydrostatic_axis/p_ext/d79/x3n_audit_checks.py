"""Exact checks for the non-resultant parts of the A.3.80 audit."""
from collections import Counter
import json
from pathlib import Path

import sympy as s

A, a, c, T, z, x = s.symbols("A a c T z x")
b2 = ((T + a - c)*x*z - (T + 2*a - 2*c)*z**2)/T
b3 = -(A + a*x)/c
b4 = ((T - a + c)*b3*z - (T - 2*a + 2*c)*z**2)/T
Q = s.Poly(s.expand(c*T*(A + a*(x**2-2*b2) + c*(b3**2-2*b4))), x)
K = (
    A**2*T**2 + A*(a+c)*(1+2*z)*T**2 + 2*A*(a-c)**2*z*T
    + 2*(a+c)**2*z**2*T**2 + 4*(a-c)**2*z**2*(T*(a+c)-a*c)
)
assert s.expand(Q.LC() - a*(a+c)*T) == 0
assert s.expand(s.discriminant(Q.as_expr(), x) + 4*a*c*K) == 0

eta, y, b = s.symbols("eta y b")
S = (T+a-b)*eta - T*x
cleared = eta*((a-b)*(eta-y)+(c-b)*(eta-x)) + T*(eta-x)*(eta-y)
assert s.expand(s.diff(cleared, y) + S) == 0
assert s.cancel(
    cleared.subs(x, (T+a-b)*eta/T) + (a-b)*(c-b)*eta**2/T
) == 0


def partitions(total, largest=None):
    if total == 0:
        yield ()
        return
    if largest is None:
        largest = total
    for first in range(min(total, largest), 0, -1):
        for tail in partitions(total-first, first):
            yield (first,) + tail


def exclusion(a0, mu):
    counts = Counter(2*k for k in mu)
    if len(counts) == 1:
        return "equal"
    if len(counts) == 2:
        for value, count in counts.items():
            if count != 1:
                continue
            other = next(v for v in counts if v != value)
            if value > other:
                return "one exception, larger"
            if a0 >= 3:
                return "one exception, A0 >= 3"
            if other-value == 2:
                return "one exception, gap 2"
    if sum(count % 2 for count in counts.values()) >= 3:
        return "three odd classes"
    if sorted(counts.values()) == [2, 2] and 2 in counts:
        return "two pairs, value 2"
    return None


enumeration = []
for degree in range(5, 18, 2):
    patterns = [
        (a0, mu)
        for a0 in range(1, degree, 2)
        for mu in partitions((degree-a0)//2)
        if len(mu) >= 3
    ]
    enumeration.append({
        "degree": degree,
        "count": len(patterns),
        "patterns": [
            {"A0": a0, "multiplicities": mu, "exclusion": exclusion(a0, mu)}
            for a0, mu in patterns
        ],
        "survivors": [(a0, mu) for a0, mu in patterns if exclusion(a0, mu) is None],
    })
assert [p["count"] for p in enumeration] == [0, 1, 3, 7, 14, 25, 42]
assert [p["survivors"] for p in enumeration] == [
    [], [], [], [], [],
    [(1, (3, 3, 1)), (1, (3, 2, 1, 1)), (1, (2, 2, 1, 1, 1))],
    [(1, (4, 2, 1, 1)), (1, (3, 2, 2, 1)),
     (1, (2, 2, 2, 1, 1)), (1, (2, 2, 1, 1, 1, 1)),
     (3, (3, 2, 1, 1)), (3, (2, 2, 1, 1, 1))],
]

n, v = s.symbols("n v")
z15 = (15+2*n)/(14+2*n)
x15 = z15*(n-2)/n
b15 = -(1+2*x15)/6
c15 = (1+2*x15**2+6*b15**2)/12
pi15 = (v-x15)*(v**2-b15*v+c15)
dp15 = s.factor(s.diff(pi15, v).subs(v, z15))
assert [s.cancel(q).subs(n, 1) for q in (z15, x15, b15, c15, dp15)] == [
    s.Rational(17, 16), -s.Rational(17, 16), s.Rational(3, 16),
    s.Rational(37, 128), s.Rational(683, 128),
]
q15 = s.Poly(s.fraction(dp15)[0], n).primitive()[1]
assert all(q > 0 for q in s.Poly(q15.as_expr().subs(n, n+1).expand(), n).all_coeffs())

f = 749*n**4 + 88168*n**3 + 2994312*n**2 + 22061260*n - 25153453
lo, hi = s.Integer(1), s.Rational(1001, 1000)
assert f.subs(n, lo) < 0 < f.subs(n, hi)
assert all(q > 0 for q in s.Poly(s.diff(f, n), n).all_coeffs())
z107 = (107+2*n)/(106+2*n)
x107 = z107*(n-13)/n
b107 = -(1+18*x107)/44
c107 = (1+18*x107**2+44*b107**2)/88
pi107 = (v-x107)*(v**2-b107*v+c107)
dp107 = s.factor(s.diff(pi107, v).subs(v, z107))
assert s.cancel(dp107 - 9*f/(3872*n**2*(n+53)**2)) == 0
assert s.cancel(1+18*x107+44*b107) == 0
assert s.cancel(1+18*x107**2+44*(b107**2-2*c107)) == 0
M3 = 1+18*x107**3+44*(b107**3-3*b107*c107)
A7diff = s.factor(M3*z107-107*x107*c107)
assert s.cancel(A7diff - 9*(2*n+107)*f/(352*n**2*(n+53)**4)) == 0

# Check the full numerator identity (A5), modulo the exact equation f(n)=0.
u = s.symbols("u")
u1 = 1/x107 - 1
usum = b107/c107 - 2
uprod = (1-b107+c107)/c107
upair = u**2-usum*u+uprod
phinum = (u-u1)*upair + 18*u*upair + 44*u*(u-u1)*(2*u-usum)
desired = 107*(1+u)**2*(u+1/(107+2*n))
for k in range(4):
    diff = s.cancel(s.expand(phinum-desired).coeff(u, k))
    assert s.rem(s.fraction(diff)[0], f, n) == 0

record = {
    "generic_discriminant_identity": True,
    "type_II_pivot_and_S_nonzero_identity": True,
    "enumeration": enumeration,
    "d15_pi_prime": str(dp15),
    "d107_quartic": str(f),
    "d107_endpoint_values": [str(f.subs(n, lo)), str(f.subs(n, hi))],
    "d107_pi_prime": str(dp107),
    "d107_A7_difference": str(A7diff),
    "d107_full_A5_modulo_quartic": True,
}
Path("checks.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({k: v for k, v in record.items() if k != "enumeration"}, indent=2))
print("All exact checks passed.")
