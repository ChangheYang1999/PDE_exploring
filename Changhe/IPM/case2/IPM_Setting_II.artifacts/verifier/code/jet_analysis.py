"""Order-by-order Taylor analysis at the moving center (verifier, independent).
rho = x^2 + sum_{k>=3} rho_k,  psi = sum_{k>=2} psi_k (psi_0, psi_1 irrelevant: U(0) subtracted).
Transport: (c_l X + U - U(0)).grad rho - rho = 0 ; Poisson: -Lap psi - rho_x = 0."""
import sympy as sp
x, y, cl = sp.symbols('x y c_l')
N = 4
rc = {}; pc = {}
rho = x**2
for k in range(3, N+1):
    for a in range(k+1):
        rc[(a, k-a)] = sp.Symbol(f'r{a}{k-a}'); rho += rc[(a, k-a)]*x**a*y**(k-a)
psi = 0
for k in range(2, N+2):
    for a in range(k+1):
        pc[(a, k-a)] = sp.Symbol(f'p{a}{k-a}'); psi += pc[(a, k-a)]*x**a*y**(k-a)
U = (-sp.diff(psi, y), sp.diff(psi, x))
U0 = [u.subs({x: 0, y: 0}) for u in U]
R = sp.expand((cl*x + U[0] - U0[0])*sp.diff(rho, x) + (cl*y + U[1] - U0[1])*sp.diff(rho, y) - rho)
E = sp.expand(-sp.diff(psi, x, 2) - sp.diff(psi, y, 2) - sp.diff(rho, x))
P = sp.Poly(R, x, y); Q = sp.Poly(E, x, y)
def homog(poly, k):
    return [poly.coeff_monomial(x**a*y**(k-a)) for a in range(k+1)]
print('order 2 transport coefficients (x^2, xy, y^2 order a=0..2 => y^2, xy, x^2):', homog(P, 2))
print('order 0 Poisson:', homog(Q, 0))
sol = sp.solve(homog(P, 2) + homog(Q, 0), [cl, pc[(0, 2)], pc[(2, 0)]], dict=True)
print('solution of order-2 conditions:', sol)

s2 = sol[0]
c = sp.Symbol('c')
P3 = [sp.simplify(e.subs(s2).subs(pc[(1, 1)], c)) for e in homog(sp.Poly(R.subs(s2).subs(pc[(1,1)], c), x, y), 3)]
Q1 = [e for e in homog(sp.Poly(E, x, y), 1)]
print('order 3 transport (coeff of y^3, xy^2, x^2y, x^3):')
for e in P3: print('   ', sp.factor(e))
print('order 1 Poisson (coeff of y, x):', Q1)
# Solve for rho_3 in terms of the cubic psi coefficients
s3 = sp.solve(P3, [rc[(0,3)], rc[(1,2)], rc[(2,1)], rc[(3,0)]], dict=True)
print('rho_3 in terms of psi_3:', s3)
# parametrize psi_3 = -x^3/3 + al*(x^3-3xy^2) + be*(3x^2y-y^3) + (general cubic satisfying Poisson)
s3p = sp.solve(Q1, [pc[(3,0)], pc[(0,3)]], dict=True)
print('Poisson order 1 constrains:', s3p)
