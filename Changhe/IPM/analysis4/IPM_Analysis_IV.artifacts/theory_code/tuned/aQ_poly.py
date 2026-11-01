"""a_Q(b) = [sin theta] f_Q for f_1 = sin(theta) + b sin(3 theta) at delta = 2/Q, h = 1 (exact, polar recursion of
hh_tune.py with coefficients in Q[b]); also gcd with the primitive P_2Q read from a file, if given.
usage: aQ_poly.py Q [P2Q_file]"""
import sys
import sympy as sp
from fractions import Fraction as Fr
Q = int(sys.argv[1])
b = sp.Symbol('b')
dl = sp.Rational(2, Q)
cm1 = sp.Rational(2, Q - 2)
def P_(n): return 2 - n * dl
def p_(n): return 1 - n * dl
def add(d, m, v):
    if m == 0: return
    if m < 0: m, v = -m, -v
    d[m] = d.get(m, sp.Poly(0, b, domain='QQ')) + v
def T(g, Pi, f, pj):
    out = {}
    for l, bb in g.items():
        for m, a in f.items():
            w = bb * a * sp.Rational(1, 2)
            add(out, l + m, w * (Pi * m - pj * l))
            add(out, m - l, w * (-pj * l - Pi * m))
    return {m: v for m, v in out.items() if not v.is_zero}
def pois(f, n):
    out = {}
    Pn = P_(n)
    for l, a in f.items():
        add(out, l + 1, a * (-sp.Rational(1) / (2 * (l + 1 + Pn))))
        if l != 1:
            den = 2 * (l - 1 - Pn)
            assert den != 0
            add(out, l - 1, a * (sp.Rational(1) / den))
    return {m: v for m, v in out.items() if not v.is_zero}
F = {1: {1: sp.Poly(1, b, domain='QQ'), 3: sp.Poly(b, b, domain='QQ')}}
G = {1: pois(F[1], 1)}
for n in range(2, Q + 1):
    acc = {}
    for i in range(1, n):
        for m, v in T(G[i], P_(i), F[n - i], p_(n - i)).items():
            acc[m] = acc.get(m, sp.Poly(0, b, domain='QQ')) + v
    lam = (n - 1) * cm1
    F[n] = {m: v * (1 / lam) for m, v in acc.items() if not v.is_zero}
    if n < Q:
        G[n] = pois(F[n], n)
aQ = F[Q].get(1, sp.Poly(0, b, domain='QQ'))
print('Q =', Q, ' a_Q degree', aQ.degree(), ' leading coefficient', aQ.LC())
print('a_Q =', aQ.as_expr())
if len(sys.argv) > 2:
    cc = [int(x) for x in open(sys.argv[2]).read().strip().split(',')]
    P = sp.Poly(cc, b, domain='QQ')
    g = sp.gcd(P, aQ)
    print('gcd(P_2Q, a_Q) degree', sp.Poly(g, b).degree())
