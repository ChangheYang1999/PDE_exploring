# Check the external referee's exact local family: Psi = (beta x + (b/2) sin 2x) y, Omega = 2 b sin(2x) y, Theta = 2 b d sin^2(x) y,
# b = beta+2, d = 2beta+1. Profile equations (P) with U = (-Psi_y, Psi_x), W = beta X + U.
import sympy as sp
x, y, be = sp.symbols('x y beta', real=True)
b = be + 2; d = 2*be + 1
Psi = (be*x + b/2*sp.sin(2*x))*y
Om = 2*b*sp.sin(2*x)*y
Th = 2*b*d*sp.sin(x)**2*y
U1, U2 = -sp.diff(Psi, y), sp.diff(Psi, x)
W1, W2 = be*x + U1, be*y + U2
E = sp.simplify(-sp.diff(Psi, x, 2) - sp.diff(Psi, y, 2) - Om)
RT = sp.simplify(W1*sp.diff(Th, x) + W2*sp.diff(Th, y) - (be - 2)*Th)
RO = sp.simplify(W1*sp.diff(Om, x) + W2*sp.diff(Om, y) + Om - sp.diff(Th, x))
print('E =', E, ' R_Theta =', RT, ' R_Omega =', RO)
print('W =', sp.simplify(W1), ',', sp.simplify(W2))
print('a0 =', sp.series(Th.subs(y, 1), x, 0, 3).removeO().coeff(x, 2), ' c = Psi_xy(0) =', sp.diff(Psi, x, y).subs({x: 0, y: 0}))
