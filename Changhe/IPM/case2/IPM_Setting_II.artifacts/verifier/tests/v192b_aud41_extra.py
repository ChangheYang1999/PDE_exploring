"""V192: independent checks of the side claims in the referee answer item 10 (not part of the proof): the regular mode of the
reduced Step 6 system, the x-shifted family, the off-center vertical family, and the scalar modes of b k' = k."""
import sympy as sp
x, y, l, U, a, t0, A, Bc = sp.symbols('x y l U a t0 A B', real=True)
out = []
def chk(name, cond):
    out.append((name, bool(cond))); print(name, bool(cond), flush=True)
beta = 2 * l - sp.Rational(1, 2)
def pde(rho, psi):
    W = (-sp.diff(psi, y), sp.diff(psi, x))
    V = (l * x + W[0], l * y + W[1])
    P = -(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(rho, x)
    T = V[0] * sp.diff(rho, x) + V[1] * sp.diff(rho, y) - rho
    return sp.simplify(P), sp.simplify(T)
fa = (beta / (beta + y))**4
ba = beta * ((beta + y)**3 - beta**3) / (3 * (beta + y)**2)
sa = ba - l * y
P0, T0 = pde(fa * x**2, x * sa)
chk('case (a) background solves both PDEs', P0 == 0 and T0 == 0)
# regular mode of b g' = (1 - 2l + b') g + 2 f u, u' = -g
gr = -4 * U * fa; ur = 2 * U * (2 * l - ba.diff(y))
chk('regular mode: b g\' - (1 - 2l + b\') g - 2 f u = 0 and u\' = -g',
    sp.simplify(ba * gr.diff(y) - (1 - 2 * l + ba.diff(y)) * gr - 2 * fa * ur) == 0 and sp.simplify(ur.diff(y) + gr) == 0)
chk('regular mode: u(0) = U, g(0) = -4U', sp.simplify(ur.subs(y, 0) - U) == 0 and sp.simplify(gr.subs(y, 0) + 4 * U) == 0)
# x-shifted family
P1, T1 = pde(fa * (x + a)**2, (x + a) * sa - a * l * y + t0)
chk('shifted family rho = f (x+a)^2, psi = (x+a) s - a l y + t0 solves both PDEs', P1 == 0 and T1 == 0)
psi1 = (x + a) * sa - a * l * y + t0
W0 = (sp.simplify((-sp.diff(psi1, y)).subs({x: 0, y: 0})), sp.simplify(sp.diff(psi1, x).subs({x: 0, y: 0})))
chk('shifted family: W(0) = (a/2, 0)', sp.simplify(W0[0] - a / 2) == 0 and W0[1] == 0)
# off-center vertical family: b(0) = A, b'(0) = B, f(0) = 1; b'' = -2f, b f' = 2(b' - beta) f
bf = sp.Function('b')(y); ff = sp.Function('f')(y)
P2, T2 = pde(ff * x**2, x * (bf - l * y))
red = {bf.diff(y, 2): -2 * ff, ff.diff(y): 2 * (bf.diff(y) - beta) * ff / bf}
chk('vertical family: PDE residuals vanish modulo b\'\' = -2f, b f\' = 2(b\' - beta) f',
    sp.simplify(P2.subs(red)) == 0 and sp.simplify(T2.subs(red)) == 0)
# numerical local solution with A = 0.3, B = 2, l = 1.5 (beta = 2.5): residual of the ODE system and W(0)
import numpy as np
from scipy.integrate import solve_ivp
lv = 1.5; bv = 2 * lv - 0.5
sol = solve_ivp(lambda yy, Y: [Y[1], -2 * Y[2], 2 * (Y[1] - bv) * Y[2] / Y[0]], [0, 0.1], [0.3, 2.0, 1.0], rtol=1e-12, atol=1e-14, dense_output=True)
chk('vertical family: local solution exists on [0, 0.1] with b bounded away from 0 (A = 0.3)', sol.success and np.min(sol.y[0]) > 0.29)
# scalar modes of b k' = k for the explicit background: k = C |R|^(1/beta), R = ((beta+y)^3 - beta^3)/(3 beta^2)
R = ((beta + y)**3 - beta**3) / (3 * beta**2)
chk('1/b = R\'/(beta R) for case (a)', sp.simplify(1 / ba - R.diff(y) / (beta * R)) == 0)
chk('0 < 1/beta < 2/3 for l > 1', all(0 < 1 / (2 * v - sp.Rational(1, 2)) < sp.Rational(2, 3) for v in [1 + sp.Rational(1, 10**6), 2, 10]))
# E1 at y = 0 with the jet g(0) = g'(0) = k'(0) = 0, f(0) = 1, any b(0): forces u(0) = 0
g0, gp0, kp0, m0, u0, b0, sp0 = sp.symbols('g0 gp0 kp0 m0 u0 b0 sp0', real=True)
E1at0 = g0 * (l - sp0) - 2 * 1 * u0 + b0 * gp0 + 2 * m0 * kp0 - g0
chk('(E1) at 0 with g(0) = g\'(0) = k\'(0) = 0, f(0) = 1 gives u(0) = 0 for any b(0)', sp.solve(E1at0.subs({g0: 0, gp0: 0, kp0: 0}), u0) == [0])
print('ALL', all(c for _, c in out), len(out))
