"""V118: symbolic checks of identities used in referee result 23 (Theorem 3.1 proof). CPU, sympy.
(4) vorticity law: V.grad(omega) - (1-l) omega - d_x W.grad rho = -d_x(V.grad rho - rho), omega = -rho_x.
(41) rescaled transport: f = e^-s rho(e^{ls} Z), u = e^-s W(e^{ls} Z): d_s f + e^{-lambda s} u.grad f = +e^{-s}(V.grad rho - rho)(e^{ls} Z).
(62) d_x(r cos 3th) = 2 cos 2th - cos 4th and (1/2pi) int cos 2th (2 cos 2th - cos 4th) = 1.
(26) det(l F, F') = l L^2 Theta' for F = L e_Theta.
(59) Q_0 = d_a^2 (R e_a) = -R e_a."""
import sympy as sp
x, y, l, s = sp.symbols('x y l s', real=True)
rho = sp.Function('rho')(x, y); W1 = sp.Function('W1')(x, y); W2 = sp.Function('W2')(x, y)
V1 = l*x + W1; V2 = l*y + W2
res = V1*sp.diff(rho, x) + V2*sp.diff(rho, y) - rho
om = -sp.diff(rho, x)
lhs = V1*sp.diff(om, x) + V2*sp.diff(om, y) - (1 - l)*om - (sp.diff(W1, x)*sp.diff(rho, x) + sp.diff(W2, x)*sp.diff(rho, y))
print('(4)', sp.simplify(lhs + sp.diff(res, x)) == 0)
# (41): check numerically with explicit test functions (identity holds for any rho, W)
Z1, Z2 = sp.symbols('Z1 Z2', real=True)
rr = lambda a, b: sp.sin(a)*b**2 + a**3*sp.cos(b) + a*b
w1 = lambda a, b: sp.cos(a + 2*b) + a*b**2
w2 = lambda a, b: sp.exp(-a**2)*b - a**2
E = sp.exp(l*s)
f = sp.exp(-s)*rr(E*Z1, E*Z2); u1 = sp.exp(-s)*w1(E*Z1, E*Z2); u2 = sp.exp(-s)*w2(E*Z1, E*Z2)
lam = l - 1
lhs41 = sp.diff(f, s) + sp.exp(-lam*s)*(u1*sp.diff(f, Z1) + u2*sp.diff(f, Z2))
a, b = sp.symbols('a b', real=True)
R = (l*a + w1(a, b))*sp.diff(rr(a, b), a) + (l*b + w2(a, b))*sp.diff(rr(a, b), b) - rr(a, b)
rhs41 = sp.exp(-s)*R.subs({a: E*Z1, b: E*Z2}, simultaneous=True)
d = (lhs41 - rhs41).subs({l: sp.Rational(17, 10), s: sp.Rational(3, 10), Z1: sp.Rational(2, 7), Z2: -sp.Rational(5, 11)})
print('(41)', abs(sp.N(d, 30)) < 1e-20)
r, th = sp.symbols('r th', positive=True)
g = r*sp.cos(3*th)
gx = sp.cos(th)*sp.diff(g, r) - sp.sin(th)/r*sp.diff(g, th)
print('(62a)', sp.simplify(sp.expand_trig(gx - (2*sp.cos(2*th) - sp.cos(4*th)))) == 0)
print('(62b)', sp.integrate(sp.cos(2*th)*(2*sp.cos(2*th) - sp.cos(4*th)), (th, 0, 2*sp.pi))/(2*sp.pi))
L = sp.Function('L')(a); T = sp.Function('T')(a)
F = sp.Matrix([L*sp.cos(T), L*sp.sin(T)]); Fp = F.diff(a)
print('(26)', sp.simplify(sp.Matrix.hstack(l*F, Fp).det() - l*L**2*sp.diff(T, a)) == 0)
Rr = sp.symbols('R', positive=True)
print('(59)', sp.simplify(sp.Matrix([Rr*sp.cos(a), Rr*sp.sin(a)]).diff(a, 2) + sp.Matrix([Rr*sp.cos(a), Rr*sp.sin(a)])) == sp.zeros(2, 1))
