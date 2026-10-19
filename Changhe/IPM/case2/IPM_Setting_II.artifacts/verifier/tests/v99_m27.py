"""V99: checks of specification v4.9 M27 (a), (b), (e) by sympy and quadrature (CPU, seconds)."""
import numpy as np, sympy as sp
from scipy import integrate
x, y, a, G, D, n, Gb, l, c = sp.symbols('x y a G Delta n Gbar l c', real=True)
th = sp.symbols('theta', real=True)
print('(a) int_0^pi cos^2 sin3 =', sp.integrate(sp.cos(th)**2*sp.sin(3*th), (th, 0, sp.pi)))
print('    int_0^pi cos^2 sin sin3 =', sp.integrate(sp.cos(th)**2*sp.sin(th)*sp.sin(3*th), (th, 0, sp.pi)))
print('    int_0^2pi |sin3| =', sp.integrate(sp.Abs(sp.sin(3*th)), (th, 0, 2*sp.pi)))
# (b) velocity on y > 0 (s = +1) and y < 0 (s = -1): |y| = s y
for s in (1, -1):
    psi = -Gb/3*x**3 + a/6*(x**3 - 3*x*y**2) - D/2*x*y*(s*y)
    V1 = sp.Rational(1, 2)*x - sp.diff(psi, y); V2 = n*y + sp.diff(psi, x)
    lap = sp.simplify(sp.diff(psi, x, 2) + sp.diff(psi, y, 2) + sp.diff(x**2*(Gb + s*D/2), x))
    div = sp.simplify(sp.diff(V1, x) + sp.diff(V2, y) - (sp.Rational(1, 2) + n))
    al = sp.symbols('alpha'); xi = x*(1 + al*y)
    eq = sp.expand(V1*sp.diff(xi, x) + V2*sp.diff(xi, y) - xi/2)
    alsol = sp.solve(eq.coeff(x, 1).coeff(y, 1), al)
    k = sp.symbols('kappa'); inv = sp.expand((V2 - sp.diff(k*x**2, x)*V1).subs(y, k*x**2))
    ksol = sp.solve(inv.coeff(x, 2), k)
    print('(b) s=%+d: lap psi + d_x rho = %s, div V - 2l = %s, V2 x^2 coeff b = %s, alpha = %s, kappa = %s'
          % (s, lap, div, sp.expand(V2).coeff(x, 2).coeff(y, 0), alsol, ksol))
# (b) geometric term by quadrature: rho = G+ x^2 above y = kappa x^2, G- x^2 below
K = 14/(15*np.pi)
for Gp, Gm, kap, R in ((1.0, 0.7, 2.0, 0.05), (1.0, 0.7, -3.0, 0.04), (2.0, 2.6, 1.5, 0.06)):
    def f(t, r):
        X, Y = r*np.cos(t), r*np.sin(t)
        g = Gp if Y > kap*X**2 else Gm
        return g*np.cos(t)**2*np.sin(3*t)
    pts = []
    val = 0.0
    for lo, hi in ((0, np.pi/2), (np.pi/2, np.pi), (np.pi, 1.5*np.pi), (1.5*np.pi, 2*np.pi)):
        v, _ = integrate.dblquad(lambda t, r: f(t, r), 0, R, lambda r: lo, lambda r: hi, epsabs=1e-13, epsrel=1e-11)
        val += v
    val /= np.pi
    Dl = Gp - Gm
    print('(b) geometric: G+ %g G- %g kappa %g R %g: c_<R %.10e, K Delta R - Delta kappa^2 R^3/pi %.10e, flat %.10e'
          % (Gp, Gm, kap, R, val, K*Dl*R - Dl*kap**2*R**3/np.pi, K*Dl*R))
# (e)
psi = c*x*y - G*x**3/3; rho = G*x**2
V1 = l*x - sp.diff(psi, y); V2 = l*y + sp.diff(psi, x)
sub = {c: l - sp.Rational(1, 2)}
print('(e) lap psi + rho_x =', sp.simplify(sp.diff(psi, x, 2) + sp.diff(psi, y, 2) + sp.diff(rho, x)),
      '; V =', [sp.expand(V1.subs(sub)), sp.expand(V2.subs(sub))],
      '; V.grad rho - rho =', sp.simplify((V1*sp.diff(rho, x) + V2*sp.diff(rho, y) - rho).subs(sub)))
nn = 2*l - sp.Rational(1, 2); eta = y - G*x**2/(nn - 1)
print('    V.grad eta - n eta =', sp.simplify((V1*sp.diff(eta, x) + V2*sp.diff(eta, y) - nn*eta).subs(sub)))
xp = sp.symbols('xp', positive=True); tau = (y - G*xp**2/(nn - 1))/xp**(2*nn)
V1p = V1.subs(x, xp); V2p = V2.subs(x, xp)
print('    V.grad tau (x > 0) =', sp.simplify((V1p*sp.diff(tau, xp) + V2p*sp.diff(tau, y)).subs(sub)))
# int |sin 3 th| numerically (sympy's Abs integral is not trusted)
print('    int_0^2pi |sin3| (quad) =', integrate.quad(lambda t: abs(np.sin(3*t)), 0, 2*np.pi, limit=200, points=[k*np.pi/3 for k in range(1, 6)])[0])
# (b) geometric term, semi-analytic: kappa > 0, sliver 0 < th < th_b(r) (and its mirror at pi) moves from G+ to G-
from scipy.optimize import brentq
def sliver(kap, R):
    F = lambda b: integrate.quad(lambda t: np.cos(t)**2*np.sin(3*t), 0, b, epsabs=1e-16, epsrel=1e-13)[0]
    def inner(r):
        b = brentq(lambda t: np.sin(t) - kap*r*np.cos(t)**2, 0, np.pi/2, xtol=1e-16)
        return 2*F(b)
    return integrate.quad(inner, 0, R, epsabs=1e-18, epsrel=1e-12)[0]/np.pi
for kap in (2.0,):
    for R in (0.1, 0.05, 0.025, 0.0125):
        s_ = sliver(kap, R); pred = kap**2*R**3/np.pi
        print('(b) sliver kappa %g R %g: (c_<R - K Delta R)/(-Delta) %.10e, kappa^2 R^3/pi %.10e, rel. diff %.3e'
              % (kap, R, s_, pred, (s_ - pred)/pred))
