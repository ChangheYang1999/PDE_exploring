"""Verifier's check of the lead's degree-5 Taylor relations at the center (SPEC D14), verifier.
rho = x^2 y (1 + delta x^2 + gamma y^2), psi = c x y + alpha x y^3 + beta x^3 y, W = c_l X + (-psi_y, psi_x),
c = 3 c_l - 1. Prints the Poisson constraint and the degree-5 coefficients of W.grad rho - rho."""
import sympy as sp
x, y, cl, al, be, de, ga = sp.symbols('x y c_l alpha beta delta gamma')
c = 3 * cl - 1
rho = x**2 * y * (1 + de * x**2 + ga * y**2)
psi = c * x * y + al * x * y**3 + be * x**3 * y
# Poisson at degree 1 (xy coefficient of -Lap psi - rho_x)
E = sp.expand(-(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(rho, x))
print('Poisson xy coefficient:', sp.factor(E.coeff(x, 1).coeff(y, 1)))
W1 = cl * x - sp.diff(psi, y)
W2 = cl * y + sp.diff(psi, x)
R = sp.expand(W1 * sp.diff(rho, x) + W2 * sp.diff(rho, y) - rho)
P = sp.Poly(R, x, y)
for (i, j), v in sorted(P.as_dict().items()):
    if i + j <= 5:
        print('x^%d y^%d :' % (i, j), sp.factor(v))
A = 2 * cl - 1
print('lead E = beta - 2 A delta  ->', sp.simplify(P.as_dict().get((4, 1), 0) - (be - 2 * A * de)))
print('lead D2 = (4A+2) gamma - 5 alpha  ->', sp.simplify(P.as_dict().get((2, 3), 0) - ((4 * A + 2) * ga - 5 * al)))
