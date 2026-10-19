"""Degree-5 Taylor relations at the center (lead, sympy). rho = x^2 y (1 + delta x^2 + gamma y^2) + O(r^7),
psi = c x y + alpha x y^3 + beta x^3 y + O(r^6), U = (-psi_y, psi_x), W = c_l X + U, c = 3 c_l - 1.
Prints the x^4 y, x^2 y^3, y^5 coefficients of W.grad rho - rho and the Poisson constraint at degree 2."""
import sympy as sp
x, y, cl, al, be, de, ga = sp.symbols('x y c_l alpha beta delta gamma')
c = 3 * cl - 1
rho = x**2 * y * (1 + de * x**2 + ga * y**2)
psi = c * x * y + al * x * y**3 + be * x**3 * y
W1 = cl * x - sp.diff(psi, y); W2 = cl * y + sp.diff(psi, x)
R = sp.expand(W1 * sp.diff(rho, x) + W2 * sp.diff(rho, y) - rho)
P = sp.Poly(R, x, y)
A = sp.Symbol('A')
for m in [(4, 1), (2, 3), (0, 5)]:
    print(m, sp.factor(sp.simplify(P.coeff_monomial(x**m[0] * y**m[1]).subs(cl, (A + 1) / 2))))
print('Poisson degree 2: -Lap psi - d_x rho, xy coefficient:', sp.expand(-(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(rho, x)).coeff(x, 1).coeff(y, 1))
