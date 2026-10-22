# Theorem 10 (single angular mode): which fifth-degree coefficient of R_Theta is which.
import sympy as sp
x, y, b, c, d, e = sp.symbols('x y beta c d e')
q = x**2 + y**2
Psi = x*y*(c + d*q + e*q**2)
Om = -sp.expand(sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2))
U1, U2 = -sp.diff(Psi, y), sp.diff(Psi, x)
W1, W2 = b*x + U1, b*y + U2
Thx = sp.expand(W1*sp.diff(Om, x) + W2*sp.diff(Om, y) + Om)
Th = sp.integrate(Thx, (x, 0, x))
RT = sp.expand(W1*sp.diff(Th, x) + W2*sp.diff(Th, y) - (b - 2)*Th)
P = sp.Poly(RT, x, y)
c21 = sp.factor(P.coeff_monomial(x**2*y))
print('x^2 y :', c21)
sub = {c: 2*b + 2}
c41 = sp.factor(sp.expand(P.coeff_monomial(x**4*y).subs(sub)))
c23 = sp.factor(sp.expand(P.coeff_monomial(x**2*y**3).subs(sub)))
print('x^4 y :', c41)
print('x^2 y^3:', c23)
r41 = sp.simplify(c41 / (18*d**2 - 48*(b + 2)*e))
r23 = sp.simplify(c23 / ((132*b + 78)*d**2 - 32*(3*b + 2)*(8*b + 5)*e))
print('ratio x^4y to 18d^2-48(b+2)e:', r41)
print('ratio x^2y^3 to (132b+78)d^2-...:', r23)
es = sp.solve(c41, e)[0]
print('e from x^4 y:', sp.factor(es), ' x^2y^3 then:', sp.factor(c23.subs(e, es)))
