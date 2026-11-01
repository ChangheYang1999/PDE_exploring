"""Exact R_2 (obstruction at order 9 of the series with H_6 = 0) for f_1 = sin + b sin3 at delta=2/3, in Q(b*), b* a root of P6.
Shows R_2(b*) != 0, so the canonical normalization H_6 = 0 is obstructed at order 9, and gives H_6 = -R_2/sigma_2 exactly."""
import json, sympy as sp
import sigma_sym as ss
b = ss.b
P6 = sp.Poly(176703765525000*b**6-222533688701250*b**5+96180432855375*b**4-20675598499400*b**3+2783057141280*b**2-243275209320*b+10532171936, b)
def red(d):
    out = {}
    for m, v in d.items():
        num, den = sp.fraction(sp.cancel(sp.together(v)))
        assert sp.Poly(den, b).degree() == 0
        r = sp.Poly(num, b).rem(P6).as_expr() / den
        r = sp.expand(r)
        if r != 0:
            out[m] = r
    return out
def pois_res(fs, n, q):
    """Poisson inverse at resonant order n with the whole stream mode q omitted (canonical H_n = 0: the entire
    coefficient b_{n,q} is the free constant)."""
    out = {}
    Pn = ss.P(n)
    for M, a in fs.items():
        if M + 1 != q:
            ss.add(out, M + 1, -a / (2 * (M + 1 + Pn)))
        if M != 1 and M - 1 != q:
            ss.add(out, M - 1, a / (2 * (M - 1 - Pn)))
    return out
F = {1: {sp.Integer(1): sp.Integer(1), sp.Integer(3): b}}
G = {1: ss.clean(ss.pois(F[1], 1))}
for n in range(2, 10):
    acc = ss.lin(*[ss.T(G[i], ss.P(i), F[n - i], ss.p(n - i)) for i in range(1, n)])
    F[n] = red(ss.clean(ss.scale(acc, 1 / ss.lam(n))))
    if n == 6:
        assert F[6].get(sp.Integer(1), 0) == 0  # O_6 = 0 in Q(b*)
        G[n] = red(ss.clean(pois_res(F[n], 6, 2)))
    elif n < 9:
        G[n] = red(ss.clean(ss.pois(F[n], n)))
R2 = F[9].get(sp.Integer(3), 0)
print('R_2 mod P6 =', sp.factor(R2))
s2 = sp.Poly((183414000*b**3-97851780*b**2+8099325*b+978848), b)
roots = P6.real_roots()
vals = {}
for r in roots:
    rv = sp.N(r, 50)
    R2v = sp.N(R2.subs(b, rv), 30)
    s2v = sp.N(s2.as_expr().subs(b, rv) / 1435033600, 30)
    vals[str(sp.N(r, 20))] = {'R2': str(R2v), 'sigma2': str(s2v), 'H6': str(sp.N(-R2v / s2v, 25))}
    print(sp.N(r, 20), 'R2 =', R2v, ' H6 = -R2/sigma2 =', sp.N(-R2v / s2v, 25))
json.dump({'R2_mod_P6': str(R2), 'nonzero': R2 != 0, 'values': vals}, open('r2_exact.json', 'w'), indent=1)
