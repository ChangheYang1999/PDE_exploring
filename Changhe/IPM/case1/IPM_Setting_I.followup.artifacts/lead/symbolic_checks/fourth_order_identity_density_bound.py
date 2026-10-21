# Lead check of a referee's identity (17): (D + 4 b_y - 1) K - F = E_yyyy - (a_yyy/a) E_y - f_y (V0)_yyy
import sympy as sp
s, y = sp.symbols('s y')
a = sp.Function('a')(s, y); b = sp.Function('b')(s, y); f = sp.Function('f')(s, y)
d = sp.diff
K = d(f, y, 4) - d(f, y)/a*d(a, y, 3)
D = lambda u: a*d(u, s) + b*d(u, y)
F = ((d(a, y)*d(a, y, 3)/a - d(a, y, 4))*(d(f, s) + b*d(f, y)/a)
     - 4*d(a, y)*d(f, s, y, y, y) - 6*d(a, y, 2)*d(f, s, y, y) - 4*d(a, y, 3)*d(f, s, y)
     - 6*d(b, y, 2)*d(f, y, 3) - 4*d(b, y, 3)*d(f, y, 2)
     + (d(a, s) - 3*d(b, y))*d(f, y)/a*d(a, y, 3))
E = a*d(f, s) + b*d(f, y) - f
V0 = d(a, s) + d(b, y)
lhs = D(K) + (4*d(b, y) - 1)*K - F
rhs = d(E, y, 4) - d(a, y, 3)/a*d(E, y) - d(f, y)*d(V0, y, 3)
print('identity (17) residual:', sp.simplify(sp.expand(lhs - rhs)))
