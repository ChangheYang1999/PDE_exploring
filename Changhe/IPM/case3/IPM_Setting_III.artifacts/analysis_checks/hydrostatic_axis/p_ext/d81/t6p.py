# Type (VI), the branches be = 0 and om = 0 (lead).  be = 0: U'(x) = 0, so u1 = -2x, a = x(1 + 4/T) (from
# 6 al + 4 be + 2 om = -T/x with om = -al); om = 0: V'(x) = 0, a = x(1 + 2/T).  The remaining coefficients are
# fixed by the stated equations; the remaining moment numerators must have a common zero.
import sympy as s
x, a, u1, u2, c1, c2, c3, v = s.symbols('x a u1 u2 c1 c2 c3 v')
d, A0 = 21, 1; T = x - d
def psums(cf, kmax):
    r = len(cf); P = []
    for l in range(1, kmax + 1):
        t = -sum(cf[i-1]*P[l-i-1] for i in range(1, min(l-1, r) + 1))
        if l <= r: t -= l*cf[l-1]
        P.append(s.expand(t))
    return P
U = v**2 + u1*v + u2; V = v**3 + c1*v**2 + c2*v + c3
def num(e, var):
    n_ = s.fraction(s.cancel(s.together(e)))[0]
    return s.Poly(n_, var, x).primitive()[1]
for name in ('be = 0', 'om = 0'):
    if name == 'be = 0':
        aa = s.cancel(x*(1 + 4/T)); al = 1/(x - aa); be = 0; om = -al
        assert s.simplify(6*al + 4*be + 2*om + T/x) == 0
        sub = {u1: -2*x, a: aa}
        M = lambda l: A0*(x - 1)**l + 6*a**l + 4*psums([u1, u2], 5)[l-1] + 2*psums([c1, c2, c3], 5)[l-1]
        for l, c in [(1, c1), (2, c2)]:
            sl = s.solve(s.cancel(M(l).subs(sub)), c); assert len(sl) == 1; sub[c] = s.cancel(sl[0])
        Vs = V.subs(sub); sl = s.solve(s.diff(Vs, v).subs(v, x) - om*Vs.subs(v, x), c3); assert len(sl) == 1
        sub[c3] = s.cancel(sl[0]); var = u2; rest = (3, 4, 5)
    else:
        aa = s.cancel(x*(1 + 2/T)); al = 1/(x - aa); om = 0; be = -al
        assert s.simplify(6*al + 4*be + 2*om + T/x) == 0
        sub = {a: aa}
        sl = s.solve(s.diff(U, v).subs(v, x) - be*U.subs(v, x), u2); assert len(sl) == 1; sub[u2] = s.cancel(sl[0])
        M = lambda l: A0*(x - 1)**l + 6*a**l + 4*psums([u1, u2], 5)[l-1] + 2*psums([c1, c2, c3], 5)[l-1]
        sl = s.solve(s.cancel(M(1).subs(sub)), c1); assert len(sl) == 1; sub[c1] = s.cancel(sl[0])
        sl = s.solve(s.diff(V, v).subs(v, x).subs(sub), c2); assert len(sl) == 1; sub[c2] = s.cancel(sl[0])
        sl = s.solve(s.cancel(M(3).subs(sub)), c3); assert len(sl) == 1; sub[c3] = s.cancel(sl[0])
        var = u1; rest = (2, 4, 5)
    Ns = []
    for l in rest:
        e = M(l)
        for _ in range(4): e = e.subs(sub)
        Ns.append(num(e, var))
    print(name, ': numerators of M_%d, M_%d, M_%d have degrees' % rest, [P.degree(var) for P in Ns], 'in', var)
    r1 = s.Poly(s.resultant(Ns[0].as_expr(), Ns[1].as_expr(), var), x)
    r2 = s.Poly(s.resultant(Ns[0].as_expr(), Ns[2].as_expr(), var), x)
    g = s.gcd(r1, r2)
    print('   resultants of degrees', r1.degree(), r2.degree(), '; gcd', s.factor(g.as_expr()))
