# Singleton plus two pairs (pattern (1; 3, 2, 2, 1, 1) for d = 19), lead 2026-10-21T19:1xZ.  Scaled variables as in
# gen19.py: x = eta, singleton a (value wa), U = v^2 + u1 v + u2 (value wu), W = v^2 + w1 v + w2 (value wv), e = 4.
# pi'(x) = 0 and (A8) give alpha + beta + omega = 0 and wa alpha + wu beta + wv omega = -T/x with alpha = 1/(x - a),
# beta = U'(x)/U(x), omega = W'(x)/W(x); these fix u2, w2 (pivots beta, omega); M_1 fixes w1; M_2 is quadratic in u1
# with a constant leading coefficient.  M_3, M_4 reduced mod M_2 are r1 u1 + r0 and q1 u1 + q0.
import sys, time, sympy as s
x, a, u1, u2, w1, w2 = s.symbols('x a u1 u2 w1 w2')
d, A0, wa, wu, wv = [int(t) for t in sys.argv[1:6]]
T = A0*x - d
al = 1/(x - a)
be = (-T/x - (wa - wv)*al)/(wu - wv)
om = -al - be
def ps(c1, c2, K):   # power sums of the roots of v^2 + c1 v + c2
    P = [2, -c1]
    for l in range(2, K + 1): P.append(-c1*P[-1] - c2*P[-2])
    return P
U = lambda v: v**2 + u1*v + u2
W = lambda v: v**2 + w1*v + w2
su2 = s.solve((2*x + u1) - be*U(x), u2)[0]
sw2 = s.solve((2*x + w1) - om*W(x), w2)[0]
pU = ps(u1, su2, 4); pW = ps(w1, sw2, 4)
M = [A0*(x - 1)**l + wa*a**l + wu*pU[l] + wv*pW[l] for l in range(5)]
sw1 = s.solve(M[1], w1)[0]
def num(e):
    nm, dn = s.fraction(s.cancel(s.together(s.sympify(e).subs(w1, sw1))))
    return s.Poly(nm, u1, a, x), s.factor(dn)
t0 = time.time()
(P2, D2), (P3, D3), (P4, D4) = [num(M[l]) for l in (2, 3, 4)]
print('deg_u1', P2.degree(u1), P3.degree(u1), P4.degree(u1), 'lc_u1(M2):', s.factor(s.Poly(P2.as_expr(), u1).LC()), flush=True)
print('denominators', D2, '|', D3, '|', D4, flush=True)
Q2 = s.Poly(P2.as_expr(), u1)
def red(P):
    r = s.prem(s.Poly(P.as_expr(), u1), Q2)   # lc(Q2) is a product of the two pivots, nonzero in the main branch
    return [s.expand(r.coeff_monomial(u1**i)) for i in (1, 0)]
(r1, r0), (q1, q0) = red(P3), red(P4)
H1 = s.Poly(s.expand(r1*q0 - r0*q1), a, x)
R3 = s.Poly(s.resultant(Q2.as_expr(), s.expand(r1*u1 + r0), u1), a, x)
print('H1 deg_a', H1.degree(a), 'deg_x', H1.degree(x), '| R3 deg_a', R3.degree(a), 'deg_x', R3.degree(x), '%.0f s' % (time.time() - t0), flush=True)
G = s.gcd(H1.as_expr(), R3.as_expr())
print('gcd(H1, R3) =', s.factor(G), flush=True)
fH = s.factor_list(H1.as_expr()); fR = s.factor_list(R3.as_expr())
print('factors H1:', [(s.Poly(f, a, x).degree(a), s.Poly(f, a, x).degree(x), k) for f, k in fH[1]], flush=True)
print('factors R3:', [(s.Poly(f, a, x).degree(a), s.Poly(f, a, x).degree(x), k) for f, k in fR[1]], flush=True)
import pickle
pickle.dump({'H1': H1.as_expr(), 'R3': R3.as_expr(), 'r1': r1, 'r0': r0, 'q1': q1, 'q0': q0, 'P2': P2.as_expr()}, open('sp2_%d_%d_%d_%d_%d.pkl' % (d, A0, wa, wu, wv), 'wb'))
