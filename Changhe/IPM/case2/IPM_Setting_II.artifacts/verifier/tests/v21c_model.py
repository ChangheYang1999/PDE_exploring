"""V21(c): symbolic check of the referee result 4 exact curved-layer model and of the reduced wall ODE (own derivation)."""
import sympy as sp
x, y, l = sp.symbols('x y l', real=True)
be = 2*l - sp.Rational(1, 2)
f = (be/(be + y))**4
b = be*(be + y)/3 - be**4/(3*(be + y)**2)
rho = x**2*f
s = b - l*y
psi = x*s
W1, W2 = -sp.diff(psi, y), sp.diff(psi, x)          # W = (-psi_y, psi_x) (PROMPT convention, -Lap psi = rho_x)
V1, V2 = l*x + W1, l*y + W2
chk = {}
chk['poisson -Lap psi - rho_x'] = sp.simplify(-sp.diff(psi, x, 2) - sp.diff(psi, y, 2) - sp.diff(rho, x))
chk['div W'] = sp.simplify(sp.diff(W1, x) + sp.diff(W2, y))
chk['curl W + rho_x'] = sp.simplify(sp.diff(W2, x) - sp.diff(W1, y) + sp.diff(rho, x))
chk['transport V.grad rho - rho'] = sp.simplify(V1*sp.diff(rho, x) + V2*sp.diff(rho, y) - rho)
chk['W(0)'] = [sp.simplify(W1.subs({x: 0, y: 0})), sp.simplify(W2.subs({x: 0, y: 0}))]
chk['psi_xy(0) - (l - 1/2)'] = sp.simplify(sp.diff(psi, x, y).subs({x: 0, y: 0}) - (l - sp.Rational(1, 2)))
J = sp.Matrix([[sp.diff(V1, x), sp.diff(V1, y)], [sp.diff(V2, x), sp.diff(V2, y)]]).subs({x: 0, y: 0})
chk['DV(0) - diag(1/2, beta)'] = sp.simplify(J - sp.diag(sp.Rational(1, 2), be))
ser = sp.series(f, y, 0, 2).removeO()
chk['rho jet: f = 1 - 4y/beta + O(y^2)'] = sp.simplify(ser - (1 - 4*y/be))
xi = x*(be/(be + y))**2
chk['xi^2 - rho'] = sp.simplify(xi**2 - rho)
chk['V.grad xi - xi/2'] = sp.simplify(V1*sp.diff(xi, x) + V2*sp.diff(xi, y) - xi/2)
chk["b' - (beta/3 + 2beta^4/(3(beta+y)^3))"] = sp.simplify(sp.diff(b, y) - (be/3 + 2*be**4/(3*(be + y)**3)))
# first integral of the reduced ODE b b''' = (-2 beta + 2 b') b''
bf = sp.Function('B')(y)
FI = bf*bf.diff(y, 2) - sp.Rational(3, 2)*bf.diff(y)**2 + 2*be*bf.diff(y)
dFI = sp.expand(FI.diff(y) - (bf*bf.diff(y, 3) - (-2*be + 2*bf.diff(y))*bf.diff(y, 2)))
chk["d/dy first integral minus ODE"] = sp.simplify(dFI)
chk["first integral on model: b b'' - (3b'-beta)(b'-beta)/2"] = sp.simplify(b*sp.diff(b, y, 2) - (3*sp.diff(b, y) - be)*(sp.diff(b, y) - be)/2)
# wall system for general x-even data: Lap W2 = -rho_xx follows from div, curl
# far field of the model: W2(0,y) linear tail coefficient
chk['W2(0,y)/y at infinity + (l+1/2)/3'] = sp.simplify(sp.limit(W2.subs(x, 0)/y, y, sp.oo) + (l + sp.Rational(1, 2))/3)
# zeros of V: V2 = b(y) (x-independent), b' > 0 on y > -beta -> only y = 0; at y = 0, V1 = x (2l - b'(0)) = x/2
chk['V1(x,0) - x/2'] = sp.simplify(V1.subs(y, 0) - x/2)
for k, v in chk.items():
    print(f'{k:55s} {v}')
# numerical spot check of b' > 0 on y > -beta for several l
import numpy as np
bp = sp.lambdify((y, l), sp.diff(b, y))
for lv in [1.01, 1.5, 3.0]:
    bv = 2*lv - 0.5
    ys = -bv + bv*np.geomspace(1e-6, 100, 2000)
    print('l', lv, 'min b\' on (-beta, 99 beta):', bp(ys, lv).min(), '(beta/3 =', bv/3, ')')
