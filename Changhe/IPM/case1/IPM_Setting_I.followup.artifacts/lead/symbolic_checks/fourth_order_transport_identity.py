# Lead check of the referee's identities (18)-(20): (D + 4 b_y - 1) K - Fcal = E_yyyy - (a_yyy/a) E_y - f_y V_yyy
# with K = f_yyyy - (f_y/a) a_yyy, E = a f_s + b f_y - f, V = a_s + b_y, D = a d_s + b d_y.
import sympy as sp
s, y = sp.symbols('s y')
a = sp.Function('a')(s, y); b = sp.Function('b')(s, y); f = sp.Function('f')(s, y)
d = sp.diff
D = lambda u: a*d(u, s) + b*d(u, y)
K = d(f, y, 4) - d(f, y)/a*d(a, y, 3)
F = ((d(a, y)*d(a, y, 3)/a - d(a, y, 4))*(d(f, s) + b*d(f, y)/a)
     - 4*d(a, y)*d(f, s, y, 3) - 6*d(a, y, 2)*d(f, s, y, 2) - 4*d(a, y, 3)*d(f, s, y)
     - 6*d(b, y, 2)*d(f, y, 3) - 4*d(b, y, 3)*d(f, y, 2)
     + (d(a, s) - 3*d(b, y))*d(f, y)/a*d(a, y, 3))
E = a*d(f, s) + b*d(f, y) - f
V = d(a, s) + d(b, y)
lhs = D(K) + (4*d(b, y) - 1)*K - F
rhs = d(E, y, 4) - d(a, y, 3)/a*d(E, y) - d(f, y)*d(V, y, 3)
print('identity (20) residual:', sp.simplify(sp.expand(lhs - rhs)))
# linear-field check of (26): J |Y|/|y| = (R/r)^q with J = e^{3t}, Y = y e^t, R = r e^{At}, q = 4/A
t, A, r0 = sp.symbols('t A r0', positive=True)
print('(26) linear:', sp.simplify(sp.exp(3*t)*sp.exp(t) - (r0*sp.exp(A*t)/r0)**(4/A)))
