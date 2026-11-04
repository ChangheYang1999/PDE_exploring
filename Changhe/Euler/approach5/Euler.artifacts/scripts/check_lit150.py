# Coordinator check of the literature agent claim LIT150 (axis pressure of a pure-swirl tail): algebraic steps only.
import sympy as sp

y1, y2, y3, X3, c, w = sp.symbols('y1 y2 y3 X3 c omega', real=True)
s = sp.sqrt(y1**2 + y2**2)
ephi = sp.Matrix([-y2, y1, 0]) / s
X = sp.Matrix([0, 0, X3])
d = X - sp.Matrix([y1, y2, y3])
# (1) kernel of d_i d_j Gamma at an axial point, contracted with V V^T, V = v e_phi
v = sp.symbols('v', real=True)
V = v * ephi
dot = sp.simplify((d.T * V)[0])
print("(X-y).V =", dot)
num = sp.simplify(3 * dot**2 - (d.T * d)[0] * (V.T * V)[0])
print("3((X-y).V)^2 - |X-y|^2|V|^2 + |X-y|^2 v^2 =", sp.simplify(num + (d.T * d)[0] * v**2))
# contact term: d_i d_j (1/(4 pi |x|)) = PV(...) - delta_ij delta_0 / 3; trace check of the PV kernel
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
r = sp.sqrt(x1**2 + x2**2 + x3**2)
G = 1 / (4 * sp.pi * r)
H = sp.Matrix(3, 3, lambda i, j: sp.diff(G, [x1, x2, x3][i], [x1, x2, x3][j]))
xs = sp.Matrix([x1, x2, x3])
K = (3 * xs * xs.T - r**2 * sp.eye(3)) / (4 * sp.pi * r**5)
print("Hessian(Gamma) - K off 0:", sp.simplify(H - K) == sp.zeros(3, 3))
# (2) homogeneous harmonic functions of degree -2p on R^3 minus 0: need l(l+1) = 2p(2p-1)
p = (1 - c) / c
lam = sp.simplify(2 * p * (2 * p - 1))
print("2p(2p-1) at c=2/5, 1/2:", lam.subs(c, sp.Rational(2, 5)), lam.subs(c, sp.Rational(1, 2)))
print("d/dc 2p(2p-1) sign on (2/5,1/2):", sp.simplify(sp.diff(lam, c)).subs(c, sp.Rational(9, 20)))
# (3) remainder exponent and energy coefficient
q = 2 * p + 1
print("(1-c) - c q =", sp.simplify((1 - c) - c * q))
print("q - 3 =", sp.simplify(q - 3), " (positive iff c < 1/2)")
print("flux exponents 3-2q, 2-3q, 2-2p-q:", [sp.simplify(e) for e in (3 - 2 * q, 2 - 3 * q, 2 - 2 * p - q)])
# energy identity: U.(DU (A y)) = div(A y |U|^2/2) - tr(A)|U|^2/2, tr A = 3c
print("energy coefficient (1-c) - 3c/2 =", sp.simplify((1 - c) - sp.Rational(3, 2) * c))
# (4) Poisson sign: div of the profile equation; tr(A DU) + div(omega J U) cancel for A = cI - omega J
J = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
A = c * sp.eye(3) - w * J
M = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'm{i}{j}'))  # M = DU, M[i,j] = d_j U_i
M = M.subs(sp.Symbol('m22'), -sp.Symbol('m00') - sp.Symbol('m11'))  # div U = 0
lin = (M * A).trace() + w * (J * M).trace()
print("tr(DU A) + omega tr(J DU) =", sp.simplify(lin))
