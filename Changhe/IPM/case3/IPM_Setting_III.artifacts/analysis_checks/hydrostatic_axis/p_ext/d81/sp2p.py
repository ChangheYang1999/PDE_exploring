# Pivot branches of sp2.py (beta = 0 or omega = 0), lead 2026-10-21T19:1xZ.  beta = 0: U'(x) = 0 so u1 = -2x, u2 free;
# omega = 0: w1 = -2x, w2 free.  alpha is then fixed by (A8), the other class by its relation, M_1 and M_2 fix the
# remaining coefficients linearly; M_3 and M_4 are rational functions of x alone and must vanish together.
import sys, sympy as s
x, a, u1, u2, w1, w2 = s.symbols('x a u1 u2 w1 w2')
d, A0, wa, wu, wv = [int(t) for t in sys.argv[1:6]]
T = A0*x - d
def ps(c1, c2, K):
    P = [2, -c1]
    for l in range(2, K + 1): P.append(-c1*P[-1] - c2*P[-2])
    return P
for br in ('beta = 0', 'omega = 0'):
    if br == 'beta = 0':     # alpha + omega = 0, wa alpha + wv omega = -T/x
        al = -T/(x*(wa - wv)); sub = {u1: -2*x}; om = -al
        sub[a] = s.cancel(x - 1/al)
        sub[w2] = s.solve((2*x + w1) - om*(x**2 + w1*x + w2), w2)[0]
        free, lin = w1, u2
    else:                    # alpha + beta = 0, wa alpha + wu beta = -T/x
        al = -T/(x*(wa - wu)); sub = {w1: -2*x}; be = -al
        sub[a] = s.cancel(x - 1/al)
        sub[u2] = s.solve((2*x + u1) - be*(x**2 + u1*x + u2), u2)[0]
        free, lin = u1, w2
    pU = ps(u1, u2, 4); pW = ps(w1, w2, 4)
    M = [s.sympify(A0*(x - 1)**l + wa*a**l + wu*pU[l] + wv*pW[l]) for l in range(5)]
    M = [m.subs(sub) for m in M]; M = [m.subs(sub) for m in M]
    sf = s.solve(M[1], free)[0]; M = [s.cancel(m.subs(free, sf)) for m in M]
    sl = s.solve(M[2], lin); assert len(sl) == 1; M = [s.cancel(m.subs(lin, sl[0])) for m in M]
    assert M[1] == 0 and M[2] == 0
    n3, n4 = [s.fraction(s.factor(M[l]))[0] for l in (3, 4)]
    g = s.gcd(n3, n4)
    print(br, ': a =', sub[a], '| numerators of M_3, M_4:', s.factor(n3), '|', s.factor(n4), '| gcd:', g, flush=True)
    rr = [r for r in s.Poly(g, x).real_roots()] if s.Poly(g, x).degree() > 0 else []
    print('   common real roots', rr, flush=True)
