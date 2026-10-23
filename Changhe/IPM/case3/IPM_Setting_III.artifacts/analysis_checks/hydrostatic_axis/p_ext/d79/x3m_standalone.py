"""Self-contained certificates for the six cases requiring elimination.

All arithmetic is exact. The other three cases have short proofs in PROOF.md.
"""
from math import comb

import sympy as s

x, p, v = s.symbols("x p v")


def ps(cs, count):
    """Power sums from signed monic coefficients cs=(c1,...,ck)."""
    k = len(cs)
    out = [s.Integer(k)]
    for j in range(1, count + 1):
        out.append(s.cancel(
            -sum(cs[i-1]*out[j-i] for i in range(1, min(j, k+1)))
            - (j*cs[j-1] if j <= k else 0)))
    return out


def monic(cs):
    k = len(cs)
    return v**k + sum(c*v**(k-i) for i, c in enumerate(cs, 1))


def numerator(expr):
    return s.Poly(s.cancel(expr).as_numer_denom()[0], p, x).primitive()[1].as_expr()


def two(A, alpha, beta, m):
    T, delta = A*x-17, alpha-beta
    q = s.cancel(((T+delta)*x*p-(T+2*delta)*x*x)/T)
    h = ps([-p, q], m+1)
    cs = []
    for j in range(1, m):
        c = s.Symbol("c")
        moment = A*(x-1)**j + alpha*h[j] + beta*ps(cs+[c], j)[j]
        polynomial = s.Poly(s.expand(moment), c)
        assert polynomial.degree() == 1
        assert polynomial.coeff_monomial(c) == -j*beta
        cs.append(s.cancel(-polynomial.coeff_monomial(1)/(-j*beta)))
    V0 = monic(cs+[0])
    cs.append(s.cancel((delta*x*s.diff(V0, v).subs(v, x)-T*V0.subs(v, x))/T))
    k = ps(cs, m+1)
    return [numerator(A*(x-1)**j+alpha*h[j]+beta*k[j])
            for j in (m, m+1)]


def three(A, wa, wb, wq):
    T, da, db = A*x-17, wa-wq, wb-wq
    S = (T+da)*x-T*p
    b = s.cancel(x*((T+da+db)*x-(T+db)*p)/S)
    c1 = s.cancel((A*(x-1)+wa*p+wb*b)/wq)
    c2 = s.cancel((A*(x-1)**2+wa*p*p+wb*b*b+wq*c1*c1)/(2*wq))
    F = A*(x-1)**3+wa*p**3+wb*b**3+wq*(-c1**3+3*c1*c2)
    G = (2*x-p-b)*(x*x+c1*x+c2)+(x-p)*(x-b)*(2*x+c1)
    return numerator(F), numerator(G)


cases = [
    ("P1", three, (1, 8, 4, 2), 54, 117906107843398875),
    ("P3", three, (1, 6, 2, 4), 54, 404653762118544939),
    ("P4", three, (3, 6, 4, 2), 54, 227878304546276464090725),
    ("P7", two, (1, 2, 4, 3), 26, 103379449173),
    ("P8", two, (3, 4, 2, 3), 26, 64870937400638655),
    ("P9", two, (1, 4, 2, 4), 38, 586402695525647),
]
for name, build, args, degree, minimum in cases:
    F, G = build(*args)
    R = s.Poly(s.resultant(F, G, p), x).primitive()[1]
    if R.LC() < 0:
        R = -R
    cs = list(reversed(R.all_coeffs()))
    shifted = [sum(cs[j]*comb(j, k)*19**(j-k)
                   for j in range(k, len(cs))) for k in range(len(cs))]
    assert R.degree() == degree
    assert len(shifted) == degree+1
    assert min(shifted) == minimum
    assert all(c > 0 for c in shifted)
    print(name, degree, len(shifted), minimum, flush=True)
print("All six resultant certificates passed.", flush=True)
