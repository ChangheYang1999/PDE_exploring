# Type (V) at d = 21: pattern (1; 2, 2, 2, 1, 1, 1, 1), a class of three nodes of value 4 (U, cubic) and a class of four
# nodes of value 2 (V, quartic), A_0 = 1, e = 6 (lead; own implementation, for the cross-check of the external answer).
# Scaled variables as in gen19.py: x = eta, T = x - 21.  pi'(x) = 0 and (A8): U'(x)/U(x) = -T/(2x) = -V'(x)/V(x).
import sys, time, pickle, sympy as s
x, a1, a2, a3, c1, c2, c3, c4, v = s.symbols('x a1 a2 a3 c1 c2 c3 c4 v')
d, A0, al, be = 21, 1, 4, 2
T = A0*x - d
def psums(cf, kmax):
    r = len(cf); P = []
    for l in range(1, kmax + 1):
        t = -sum(cf[i-1]*P[l-i-1] for i in range(1, min(l-1, r) + 1))
        if l <= r: t -= l*cf[l-1]
        P.append(s.expand(t))
    return P
U = v**3 + a1*v**2 + a2*v + a3; V = v**4 + c1*v**3 + c2*v**2 + c3*v + c4
bU = -T/(2*x)
sa3 = s.solve(s.diff(U, v).subs(v, x) - bU*U.subs(v, x), a3)[0]
pU = [s.cancel(q.subs(a3, sa3)) for q in psums([a1, a2, a3], 6)]
pV = psums([c1, c2, c3, c4], 6)
M = lambda l: A0*(x - 1)**l + al*pU[l-1] + be*pV[l-1]
sub = {}
for l, c in [(1, c1), (2, c2), (3, c3)]:
    e = s.cancel(M(l).subs(sub)); sl = s.solve(e, c); assert len(sl) == 1; sub[c] = s.cancel(sl[0])
Vs = V.subs(sub)
sl = s.solve(s.diff(Vs, v).subs(v, x) + bU*Vs.subs(v, x), c4); assert len(sl) == 1; sub[c4] = s.cancel(sl[0])
def num(e):
    n_ = s.fraction(s.cancel(s.together(e)))[0]
    return s.Poly(n_, a2, a1, x).primitive()[1]
N = [num(M(l).subs(sub)) for l in (4, 5, 6)]
for k, P in zip((4, 5, 6), N):
    print('M_%d numerator: deg a2 %d, deg a1 %d, deg x %d, terms %d' % (k, P.degree(a2), P.degree(a1), P.degree(x), len(P.terms())), flush=True)
    print('   leading coefficient in a2:', s.factor(P.as_expr().coeff(a2, P.degree(a2))) if P.degree(a2) <= 2 else '...', flush=True)
pickle.dump({'N': [P.as_expr() for P in N]}, open('t5_21.pkl', 'wb'))
