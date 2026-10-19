"""V197b: sympy checks of the potential matching stated in referee audit 42 replacement 5 and of its centered field."""
import sympy as sp
u, v, R, r, th, a, b, x, y = sp.symbols('u v R r theta a b x y', real=True)
Rp = sp.Symbol('Rp', positive=True)
P = []
def ok(n, val):
    P.append(bool(val)); print('%-90s %s' % (n, bool(val)))
lap = lambda f: sp.diff(f, u, 2) + sp.diff(f, v, 2)
F0 = -(u**2 + v**2) / 4; F1 = R**2 * u / 4 - u * (u**2 + v**2) / 8
F2 = R**2 * (u**2 - v**2) / 16 - (u**2 + v**2)**2 / 32 - (u**4 - v**4) / 24
ok('-Lap F0 = 1, -Lap F1 = u, -Lap F2 = u^2', sp.simplify(-lap(F0) - 1) == 0 and sp.simplify(-lap(F1) - u) == 0 and sp.simplify(-lap(F2) - u**2) == 0)
pol = {u: r * sp.cos(th), v: r * sp.sin(th)}
E0 = -(Rp**2 / 2) * sp.log(r); E1 = Rp**4 * r * sp.cos(th) / (8 * r**2)
I0 = F0.subs(pol).subs(R, Rp); I1 = F1.subs(pol).subs(R, Rp)
c0 = sp.simplify((E0 - I0).subs(r, Rp))
ok('F0 + const matches -(R^2/2) log r in value and normal derivative at r = R (const = R^2/4 - R^2 log R/2)',
   sp.simplify(c0 - (Rp**2 / 4 - Rp**2 * sp.log(Rp) / 2)) == 0 and sp.simplify(sp.diff(E0 - I0, r).subs(r, Rp)) == 0)
ok('F1 matches R^4 u/(8|z|^2) in value and normal derivative at r = R',
   sp.simplify((E1 - I1).subs(r, Rp)) == 0 and sp.simplify(sp.diff(E1 - I1, r).subs(r, Rp)) == 0)
# exterior potential of u 1_B is the dipole: Newtonian far-field coefficient (1/2pi) int u^2 = R^4/8
s, ph = sp.symbols('s phi', positive=True)
ok('dipole coefficient (1/(2 pi)) int_B w_1^2 dw = R^4/8', sp.simplify(sp.integrate(sp.integrate((s * sp.cos(ph))**2 * s, (s, 0, Rp)), (ph, 0, 2 * sp.pi)) / (2 * sp.pi) - Rp**4 / 8) == 0)
Phi = (F2 + 2 * a * F1 + a**2 * F0).subs({u: x - a, v: y - b})
ok('-Lap Phi = x^2 for the potential of x^2 on B(d, R)', sp.simplify(-(sp.diff(Phi, x, 2) + sp.diff(Phi, y, 2)) - x**2) == 0)
Ux = sp.diff(Phi, x); U = sp.Matrix([-sp.diff(Ux, y), sp.diff(Ux, x)])
W = sp.expand(U - U.subs({x: 0, y: 0}))
Wc = sp.Matrix([x * y / 4, -(7 * x**2 + y**2) / 8])
st = sp.expand(sp.I * (a + sp.I * b) * (x - sp.I * y) / 4)
ok('centered grad-perp d_x Phi = W_circ + (i/4)(a + ib) Xbar', sp.simplify(W[0] - Wc[0] - sp.re(st)) == 0 and sp.simplify(W[1] - Wc[1] - sp.im(st)) == 0)
print('ALL', all(P), len(P))
