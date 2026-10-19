"""V192: independent symbolic checks of Proposition 3.15a / Section 9.16 (working draft of the lead analyst), written from the text,
not from check_315a.py: coefficient equations, the identities used in Steps 2-8, the explicit case (a) and (b)
solutions, and the incompatibility in Step 8."""
import sympy as sp
x, y, l = sp.symbols('x y l', real=True)
out = []
def chk(name, cond):
    out.append((name, bool(cond))); print(name, bool(cond), flush=True)
f, g, k, n, m, s, t = [sp.Function(c)(y) for c in 'fgknmst']
beta = 2 * l - sp.Rational(1, 2)
rho = f * x**2 + g * x + k
psi = n * x**3 + m * x**2 + s * x + t
W = (-sp.diff(psi, y), sp.diff(psi, x))
V = (l * x + W[0], l * y + W[1])
# Step 1: Poisson coefficients
P = sp.expand(-(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(rho, x))
Pc = sp.Poly(P, x).all_coeffs()[::-1]
chk('Poisson: coefficients of x^0..x^3 are -(t\'\' + 2m) - g, -(s\'\' + 6n) - 2f, -m\'\', -n\'\'',
    [sp.simplify(c) for c in Pc] == [sp.simplify(-(t.diff(y, 2) + 2 * m) - g), sp.simplify(-(s.diff(y, 2) + 6 * n) - 2 * f),
                                     sp.simplify(-m.diff(y, 2)), sp.simplify(-n.diff(y, 2))])
b = l * y + s; u = t.diff(y)
chk('V_1 = x(l - s\') - n\' x^3 - m\' x^2 - u, V_2 = b + 2m x + 3n x^2',
    sp.expand(V[0] - (x * (l - s.diff(y)) - n.diff(y) * x**3 - m.diff(y) * x**2 - u)) == 0
    and sp.expand(V[1] - (b + 2 * m * x + 3 * n * x**2)) == 0)
T = sp.expand(V[0] * sp.diff(rho, x) + V[1] * sp.diff(rho, y) - rho)
Tc = sp.Poly(T, x).all_coeffs()[::-1]
D = lambda q: q.diff(y)
E = [b * D(k) - g * u - k,
     g * (l - D(s)) - 2 * f * u + b * D(g) + 2 * m * D(k) - g,
     2 * f * (l - D(s)) - g * D(m) + b * D(f) + 2 * m * D(g) + 3 * n * D(k) - f,
     2 * m * D(f) - 2 * f * D(m) + 3 * n * D(g) - D(n) * g,
     3 * n * D(f) - 2 * f * D(n)]
chk('transport: degree 4 in x and coefficients x^0..x^4 equal (E0)..(E4)', len(Tc) == 5 and all(sp.expand(a - c) == 0 for a, c in zip(Tc, E)))
# Step 2: strain; 1 - 4l = -2 beta; Step 3 exponent; Step 6 kappa
chk('b\'(0) = l + s\'(0) = 2l - 1/2 = beta when s\'(0) = l - 1/2; 1 - 4l = -2 beta; 1 - 2l + beta = 1/2',
    sp.simplify(l + (l - sp.Rational(1, 2)) - beta) == 0 and sp.simplify(1 - 4 * l + 2 * beta) == 0 and sp.simplify(1 - 2 * l + beta - sp.Rational(1, 2)) == 0)
B = sp.symbols('B', positive=True)
chk('beta > 3/2 for l > 1: 5/(4 beta) < 5/6, kappa = 1/(2 beta) in (0, 1/3)',
    sp.simplify(beta.subs(l, 1) - sp.Rational(3, 2)) == 0 and all(sp.Rational(5, 4) / bb < sp.Rational(5, 6) and 0 < 1 / (2 * bb) < sp.Rational(1, 3) for bb in [sp.Rational(3, 2) + sp.Rational(1, 10**6), 2, 10]))
# Step 4 / 8 logarithmic-derivative identities
chk('(f^3/n^2)\' = f^2 (3n f\' - 2f n\')/n^3', sp.simplify(sp.diff(f**3 / n**2, y) - f**2 * (3 * n * D(f) - 2 * f * D(n)) / n**3) == 0)
chk('(m/f)\' = (m\' f - m f\')/f^2', sp.simplify(sp.diff(m / f, y) - (D(m) * f - m * D(f)) / f**2) == 0)
chk('(g^3/n)\' = g^2 (3n g\' - n\' g)/n^2', sp.simplify(sp.diff(g**3 / n, y) - g**2 * (3 * n * D(g) - D(n) * g) / n**2) == 0)
# Step 5: case n = m = 0, (E2) becomes b f' = 2(b' - beta) f with l - s' = 2l - b'
bb = sp.Function('bb')(y); ff = sp.Function('ff')(y)
E2n0 = 2 * ff * (l - (bb.diff(y) - l)) + bb * ff.diff(y) - ff
chk('(E2) with n = m = 0: b f\' - 2(b\' - beta) f', sp.expand(E2n0 - (bb * ff.diff(y) - 2 * (bb.diff(y) - beta) * ff)) == 0)
fa = (beta / (beta + y))**4
ba = beta * (beta + y) / 3 - beta**4 / (3 * (beta + y)**2)
chk('case (a): b f\' = 2(b\' - beta) f, b\'\' = -2f, f(0) = 1, b(0) = 0, b\'(0) = beta, b\'\'(0) = -2',
    sp.simplify(ba * fa.diff(y) - 2 * (ba.diff(y) - beta) * fa) == 0 and sp.simplify(ba.diff(y, 2) + 2 * fa) == 0
    and sp.simplify(fa.subs(y, 0) - 1) == 0 and sp.simplify(ba.subs(y, 0)) == 0 and sp.simplify(ba.diff(y).subs(y, 0) - beta) == 0
    and sp.simplify(ba.diff(y, 2).subs(y, 0) + 2) == 0)
chk('case (a): b = beta((beta + y)^3 - beta^3)/(3 (beta + y)^2)', sp.simplify(ba - beta * ((beta + y)**3 - beta**3) / (3 * (beta + y)**2)) == 0)
# Step 6: with n = m = 0, (E1) and t'' = -g read b g' = (1 - 2l + b') g + 2 f u, u' = -g
E1n0 = g * (l - (bb.diff(y) - l)) - 2 * f * u + bb * D(g) - g
chk('(E1) with n = m = 0: b g\' - (1 - 2l + b\') g - 2 f u', sp.expand(E1n0 - (bb * D(g) - (1 - 2 * l + bb.diff(y)) * g - 2 * f * u)) == 0)
kap = sp.symbols('kappa', positive=True); eta = sp.symbols('eta', positive=True)
chk('int_0^y (y/eta)^kappa d eta = y/(1 - kappa) for kappa = 1/5', sp.simplify(sp.integrate((y / eta)**sp.Rational(1, 5), (eta, 0, y)).subs(y, 3) - sp.Rational(3, 1) / (1 - sp.Rational(1, 5))) == 0)
# Step 8: z = 1 + c y, f = z^(2/3), b from (b z^(-1/3))' = beta z^(-1/3)
c, n0 = sp.symbols('c n0', nonzero=True)
z = 1 + c * y
f8 = z**sp.Rational(2, 3)
b8 = 3 * beta / (2 * c) * (z - z**sp.Rational(1, 3))
chk('Step 8: f\'/f = 2c/(3z)', sp.simplify(f8.diff(y) / f8 - 2 * c / (3 * z)) == 0)
chk('Step 8: b solves b\' = beta + c b/(3z), b(0) = 0, and b f\' = 2(b\' - beta) f',
    sp.simplify(b8.diff(y) - beta - c * b8 / (3 * z)) == 0 and sp.simplify(b8.subs(y, 0)) == 0
    and sp.simplify(b8 * f8.diff(y) - 2 * (b8.diff(y) - beta) * f8) == 0)
chk('Step 8: b\'\' = (beta c/3) z^(-5/3)', sp.simplify(b8.diff(y, 2) - beta * c / 3 * z**sp.Rational(-5, 3)) == 0)
Z = sp.symbols('Z', positive=True)
h = Z**sp.Rational(7, 3) + 3 * n0 * Z**sp.Rational(8, 3)
chk('Step 8: (beta c/3) z^(-5/3) = -2 z^(2/3) - 6 n0 z  <=>  z^(7/3) + 3 n0 z^(8/3) = -beta c/6',
    sp.simplify((beta * c / 3 * Z**sp.Rational(-5, 3) + 2 * Z**sp.Rational(2, 3) + 6 * n0 * Z) * Z**sp.Rational(5, 3) / 2 - (beta * c / 6 + h)) == 0)
d1 = sp.diff(h, Z).subs(Z, 1); d2 = sp.diff(h, Z, 2).subs(Z, 1)
chk('Step 8: h\'(1) = 7/3 + 8 n0, h\'\'(1) = 28/9 + (40/3) n0, no common root',
    sp.simplify(d1 - (sp.Rational(7, 3) + 8 * n0)) == 0 and sp.simplify(d2 - (sp.Rational(28, 9) + sp.Rational(40, 3) * n0)) == 0
    and sp.solve([d1, d2], n0) == [])
# Step 8, c = 0: f = 1, (E2) on I_0 with k = 0 gives s'' = 0 and n0 = -1/3; then k'' = -2 s'' = 0
chk('Step 8, c = 0: s\'\' = -2f - 6n = 0 with f = 1 gives n0 = -1/3', sp.solve(-2 - 6 * n0, n0) == [sp.Rational(-1, 3)])
# case (b) solution on R^2
rb = x**2; pb = -x**3 / 3 + (l - sp.Rational(1, 2)) * x * y + sp.Symbol('t0')
Wb = (-sp.diff(pb, y), sp.diff(pb, x)); Vb = (l * x + Wb[0], l * y + Wb[1])
chk('case (b): -Lap psi = rho_x, V.grad rho = rho, W(0) = 0',
    sp.expand(-(sp.diff(pb, x, 2) + sp.diff(pb, y, 2)) - sp.diff(rb, x)) == 0
    and sp.expand(Vb[0] * sp.diff(rb, x) + Vb[1] * sp.diff(rb, y) - rb) == 0 and all(sp.simplify(w.subs({x: 0, y: 0})) == 0 for w in Wb))
# case (b) satisfies all coefficient equations with f = 1, g = k = m = 0, n = -1/3, s = (l - 1/2) y, t = t0
sub = {f: 1, g: 0, k: 0, m: 0, n: sp.Rational(-1, 3), s: (l - sp.Rational(1, 2)) * y, t: sp.Symbol('t0')}
chk('case (b) in (E0)..(E4) and the Poisson equations', all(sp.simplify(e.subs(sub).doit()) == 0 for e in E + Pc))
print('ALL', all(o[1] for o in out), len(out))
