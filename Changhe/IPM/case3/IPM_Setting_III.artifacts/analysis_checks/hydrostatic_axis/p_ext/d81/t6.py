# Type (VI) at d = 21: pattern (1; 3, 2, 2, 1, 1, 1), a singleton a of value 6, a pair U = v^2 + u1 v + u2 of value 4
# and a class V = v^3 + c1 v^2 + c2 v + c3 of three nodes of value 2, A_0 = 1, e = 5 (lead; own implementation).
# pi'(x) = 0 and (A8): al + be + om = 0, 6 al + 4 be + 2 om = -T/x with al = 1/(x - a), be = U'(x)/U(x),
# om = V'(x)/V(x).  Regular branch be om != 0: u2 from be, M_1, M_2 give c1, c2, c3 from om; M_3, M_4, M_5 remain.
import sys, pickle, time, sympy as s
x, a, u1, u2, c1, c2, c3, v = s.symbols('x a u1 u2 c1 c2 c3 v')
d, A0 = 21, 1
T = A0*x - d
al = 1/(x - a); be = (-T/x - 4*al)/2; om = -al - be
def psums(cf, kmax):
    r = len(cf); P = []
    for l in range(1, kmax + 1):
        t = -sum(cf[i-1]*P[l-i-1] for i in range(1, min(l-1, r) + 1))
        if l <= r: t -= l*cf[l-1]
        P.append(s.expand(t))
    return P
U = v**2 + u1*v + u2; V = v**3 + c1*v**2 + c2*v + c3
sub = {u2: s.cancel(s.solve(s.diff(U, v).subs(v, x) - be*U.subs(v, x), u2)[0])}
pU = [s.cancel(q.subs(sub)) for q in psums([u1, u2], 5)]
pV = psums([c1, c2, c3], 5)
M = lambda l: A0*(x - 1)**l + 6*a**l + 4*pU[l-1] + 2*pV[l-1]
for l, c in [(1, c1), (2, c2)]:
    sl = s.solve(s.cancel(M(l).subs(sub)), c); assert len(sl) == 1; sub[c] = s.cancel(sl[0])
Vs = V.subs(sub)
sl = s.solve(s.diff(Vs, v).subs(v, x) - om*Vs.subs(v, x), c3); assert len(sl) == 1; sub[c3] = s.cancel(sl[0])
def num(e):
    n_ = s.fraction(s.cancel(s.together(e)))[0]
    P = s.Poly(n_, u1, a, x).primitive()[1]
    return P
t0 = time.time()
N = [num(M(l).subs(sub).subs(sub)) for l in (3, 4, 5)]
for k, P in zip((3, 4, 5), N):
    fl = s.factor_list(P.as_expr())[1]
    print('M_%d numerator: deg u1 %d, deg a %d, deg x %d, terms %d; factors (deg u1, deg a, deg x, mult):' % (k, P.degree(u1), P.degree(a), P.degree(x), len(P.terms())),
          [(s.Poly(f, u1, a, x).degree(u1), s.Poly(f, u1, a, x).degree(a), s.Poly(f, u1, a, x).degree(x), m) for f, m in fl], '%.0f s' % (time.time() - t0), flush=True)
pickle.dump({'N': [P.as_expr() for P in N]}, open('t6_21.pkl', 'wb'))
