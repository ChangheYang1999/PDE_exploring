"""Compatible axis data at c_l = 3/2 (astra audit2 item 5): exact B_3 = -1 and
G_3 = (11/6 x^2 - 5/6 x^4 - x^7)/((1-x^2)(1+x^2)^3). Also checks B_3 = a2(P)/(6 g(P)^3) with H normalized as x^7 at 0."""
import numpy as np
import sympy as sp
from b3_diag import AxisData

x = sp.symbols('x')
w = -2 * x * (1 - x**2) / (1 + x**2)
g = x**2 / (1 + x**2)
h = 3 - sp.diff(w, x)
a2 = x * (5 * x**2 - 11) / (1 + x**2)**3
b3 = -sp.diff(a2, x) / 3
F3 = sp.simplify(-a2 * sp.diff(g, x) - b3 * g)
G3 = (sp.Rational(11, 6) * x**2 - sp.Rational(5, 6) * x**4 - x**7) / ((1 - x**2) * (1 + x**2)**3)
print('G1 eq residual:', sp.simplify(w * sp.diff(g, x) + (h - 1) * g))
print('G3 eq residual:', sp.simplify(w * sp.diff(G3, x) + (3 * h - 1) * G3 - F3))
print('curl/div constraints: a2\'+3b3 =', sp.simplify(sp.diff(a2, x) + 3 * b3),
      ' h\'-2a2+g\' =', sp.simplify(sp.diff(h, x) - 2 * a2 + sp.diff(g, x)))
f = {k: sp.lambdify(x, v, 'numpy') for k, v in dict(w=w, h=h, a2=a2, b3=b3, g=g, gp=sp.diff(g, x)).items()}
d = AxisData(f['w'], f['h'], f['a2'], f['b3'], f['g'], f['gp'], 1.5, 1.0)
for kw in (dict(), dict(delta=0.3), dict(delta=0.5, nloc=32)):
    b, info = d.b3_fp(**kw)
    print(kw, 'fp B3 =', repr(b), ' err', abs(b + 1), ' odd_rel', info['odd_rel'])
gP = 0.5
a2P = float(a2.subs(x, 1))
print('a2(P)/(6 g(P)^3) =', a2P / (6 * gP**3), ' (H here ~ x^7 e^E; formula normalization differs by H(x)/(2g^4/(g0^4|w|)))')
sol = d.g3_ode(0.02)
xf = np.linspace(0.02, 0.35, 400)
bfit, res, _ = d.b3_fit(xf, sol.sol(xf)[0], npoly=12)
print('ode+fit B3 =', bfit, ' err', abs(bfit + 1))
