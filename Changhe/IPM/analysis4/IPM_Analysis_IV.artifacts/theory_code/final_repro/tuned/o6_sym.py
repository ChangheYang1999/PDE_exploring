"""Exact first-resonance obstruction at delta=2/3: coefficient of sin(theta) in f_6 for f_1 = sin(th) + b sin(M th)."""
import sys
import sympy as sp
b = sp.symbols('b')
dl = sp.Rational(2, 3)
c = 1 / (1 - dl)
M = int(sys.argv[1]) if len(sys.argv) > 1 else 3
p = lambda n: 1 - n * dl
# represent sine series f as dict odd m -> coeff, stream g as dict even m -> coeff
def poisson(n, f):
    pn = p(n)
    g = {}
    mx = max(f) + 1
    for q in range(2, mx + 2, 2):
        j = q // 2
        den = 2 * (4 * j * j - (pn + 1) ** 2)
        num = (pn - 2 * j + 1) * f.get(2 * j - 1, 0) + (pn + 2 * j + 1) * f.get(2 * j + 1, 0)
        if den == 0:
            raise RuntimeError('resonance at n=%d q=%d, obstruction %s' % (n, q, sp.factor(f.get(2*j-1, 0))))
        val = sp.expand(num / den)
        if val != 0:
            g[q] = val
    return g
def prod_sc(s, cc):
    """sine series s (dict m->a, sin(m th)) times cosine series cc (dict m->a, cos(m th)) -> sine series"""
    out = {}
    for m1, a1 in s.items():
        for m2, a2 in cc.items():
            # sin A cos B = (sin(A+B) + sin(A-B))/2
            for m, sg in ((m1 + m2, 1), (m1 - m2, 1)):
                if m == 0:
                    continue
                if m < 0:
                    m, sg2 = -m, -1
                else:
                    sg2 = 1
                out[m] = out.get(m, 0) + sg2 * a1 * a2 / 2
    return {m: sp.expand(v) for m, v in out.items() if sp.expand(v) != 0}
def der(s):
    return {m: m * a for m, a in s.items()}
F = {1: {1: sp.Integer(1), M: b}}
G = {1: poisson(1, F[1])}
for n in range(2, 7):
    acc = {}
    for i in range(1, n):
        j = n - i
        t1 = prod_sc(F[j], der(G[i]))  # f_j * g_i'
        t2 = prod_sc(G[i], der(F[j]))  # g_i * f_j'
        for m, v in t1.items():
            acc[m] = acc.get(m, 0) - p(j) * v
        for m, v in t2.items():
            acc[m] = acc.get(m, 0) + (p(i) + 1) * v
    lam = (n - 1) * (c - 1)
    F[n] = {m: sp.expand(v / lam) for m, v in acc.items() if sp.expand(v) != 0}
    if n < 6:
        G[n] = poisson(n, F[n])
O6 = sp.factor(F[6].get(1, 0))
print('M', M, 'O6 =', O6)
P = sp.Poly(sp.expand(F[6].get(1, 0)), b)
print('real roots', [sp.N(r, 20) for r in sp.real_roots(P)])
