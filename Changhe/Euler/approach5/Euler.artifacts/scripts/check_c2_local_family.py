"""Exact check of the nondecaying C^2 profile family from an external referee answer (section 2).

U = (-c x - w y, w x + (c-1) y + f(x), z), with f an arbitrary function of x and F' = f,
P = (d/2)(x^2 + y^2) - w a x y + 2 w F(x) - z^2, d = c(1-c) + w^2, a = 1 - 2c.
Checks div U = 0, the profile equation (1-c)U + (B.grad)U + w J U + grad P = 0 with
B = (cI - w J)y + U and J(y1, y2, y3) = (-y2, y1, 0), the formula for B, and Omega = curl U.
"""
import sympy as sp

x, y, z, c, w = sp.symbols('x y z c w', real=True)
F = sp.Function('F')
f = sp.diff(F(x), x)
a = 1 - 2*c
d = c*(1 - c) + w**2
X = sp.Matrix([x, y, z])
U = sp.Matrix([-c*x - w*y, w*x + (c - 1)*y + f, z])
P = d/2*(x**2 + y**2) - w*a*x*y + 2*w*F(x) - z**2
J = lambda v: sp.Matrix([-v[1], v[0], 0])
B = c*X - w*J(X) + U
grad = lambda s: sp.Matrix([sp.diff(s, v) for v in (x, y, z)])
DU = U.jacobian(X)
div = sp.simplify(DU.trace())
res = sp.simplify((1 - c)*U + DU*B + w*J(U) + grad(P))
curl = sp.Matrix([sp.diff(U[2], y) - sp.diff(U[1], z),
                  sp.diff(U[0], z) - sp.diff(U[2], x),
                  sp.diff(U[1], x) - sp.diff(U[0], y)])
print('div U =', div)
print('residual =', list(res))
print('B - (0, -a y + f, (1+c) z) =', list(sp.simplify(B - sp.Matrix([0, -a*y + f, (1 + c)*z]))))
print('Omega =', list(sp.simplify(curl)))
# bracket [B, Omega] = (B.grad)Omega - (Omega.grad)B should equal -(1+c) Omega
br = sp.simplify(curl.jacobian(X)*B - B.jacobian(X)*curl + (1 + c)*curl)
print('[B,Omega] + (1+c) Omega =', list(br))
assert div == 0 and all(e == 0 for e in res) and all(e == 0 for e in br)
print('all identities hold')
