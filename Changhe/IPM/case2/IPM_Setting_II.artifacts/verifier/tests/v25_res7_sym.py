"""V25: sympy checks of referee result 7 claims (referee result 7): local model, cubic jet without symmetry, limiting equilibrium
graph, far-field resonance, singular family, invariant slow graph, nullcline speed."""
import sympy as sp
x, y, p, a, d, k, t = sp.symbols('x y p a d k t', real=True)
out = []
def chk(name, e):
    e = sp.simplify(e); out.append((name, e)); print(name, '->', e)
# 1. exact local model
f = x**2; psi = (1 - p/2)*x*y - x**3/3
U = sp.Matrix([-sp.diff(psi, y), sp.diff(psi, x)]); b = sp.Matrix([x, y]) + U
chk('model b - claimed', sp.simplify(b - sp.Matrix([p/2*x, (2 - p/2)*y - x**2])).norm())
chk('model transport b.grad f - p f', b[0]*sp.diff(f, x) + b[1]*sp.diff(f, y) - p*f)
chk('model div b - 2', sp.diff(b[0], x) + sp.diff(b[1], y) - 2)
chk('model curl b + f_x', sp.diff(b[1], x) - sp.diff(b[0], y) + sp.diff(f, x))
chk('model -Lap psi - f_x', -(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(f, x))
chk('model c - (1 - p/2)', sp.diff(psi, x, y).subs({x: 0, y: 0}) - (1 - p/2))
# invariant graph y = k x^2: b2 = 2 k x b1
ks = sp.solve(sp.expand((b[1] - 2*k*x*b[0]).subs(y, k*x**2)/x**2), k)
chk('slow graph k - 1/(2 - 3p/2)', ks[0] - 1/(2 - sp.Rational(3, 2)*p))
print('   series', sp.series(ks[0], p, 0, 3))
# 2. cubic jet (rescaled variables): f = x^2 + f3, psi = (1-p/2) x y - x^3/3 + harmonic cubic + 0 quadratic harmonic
f30, f21, f12, f03, al, be = sp.symbols('f30 f21 f12 f03 al be')
f3 = f30*x**3 + f21*x**2*y + f12*x*y**2 + f03*y**3
psi3 = -x**3/3 + al*(x**3 - 3*x*y**2) + be*(3*x**2*y - y**3)
assert sp.simplify(-(sp.diff(psi3, x, 2) + sp.diff(psi3, y, 2)) - sp.diff(x**2, x)) == 0
b1 = sp.Matrix([p/2*x, (2 - p/2)*y])
w2 = sp.Matrix([-sp.diff(psi3, y), sp.diff(psi3, x)])
eq = sp.expand(b1[0]*sp.diff(f3, x) + b1[1]*sp.diff(f3, y) + w2[0]*sp.diff(x**2, x) + w2[1]*sp.diff(x**2, y) - p*f3)
P = sp.Poly(eq, x, y)
eqs = [P.coeff_monomial(m) for m in [x**3, x**2*y, x*y**2, y**3]]
sol = sp.solve(eqs, [f12, f03, al, be], dict=True)
print('cubic jet solution (f30 = a, f21 = d free):', sol)
s0 = sol[0]
chk('f12 + p a/(8 - 3p)', s0[f12].subs({f30: a, f21: d}) + p*a/(8 - 3*p))
chk('f03', s0[f03])
# strong zero curve x = kk(y): f = (x - kk y^2)^2 (1 + a x + d y) + O(4) -> kk'' = 2 kk
kk = sp.symbols('kk')
e = sp.Poly(sp.expand((x - kk*y**2)**2*(1 + a*x + d*y)), x, y)
kks = sp.solve(e.coeff_monomial(x*y**2) - s0[f12].subs({f30: a, f21: d}), kk)[0]
chk("k''(0) - p a/(8-3p)", 2*kks - p*a/(8 - 3*p))
# limiting equilibrium graph at p = 0: b2 = 2 y + w2_2 = 0, y = h(x) = h2 x^2
b2full = (2 - p/2)*y + w2[1].subs(s0).subs({f30: a, f21: d})
h2 = sp.symbols('h2')
h2s = sp.solve(sp.expand(b2full.subs(y, h2*x**2)).coeff(x, 2).subs(p, 0), h2)
print('   w2 at p=0:', sp.simplify(w2.subs(s0).subs({f30: a, f21: d}).subs(p, 0)).T)
chk('h2 - (1/2 + d/4)', h2s[0] - (sp.Rational(1, 2) + d/4))
# the first component vanishes on the graph at p = 0, to order x^2? b1_full = p/2 x + w2_1
b1full = p/2*x + w2[0].subs(s0).subs({f30: a, f21: d})
chk('b_*1 on graph, x^2 coefficient (p=0)', sp.expand(b1full.subs(y, h2s[0]*x**2).subs(p, 0)).coeff(x, 2))
# 3. far-field resonance
th = sp.symbols('th', real=True)
A0, a1, b1c, a2, b2c, a3, b3c = sp.symbols('A0 a1 b1c a2 b2c a3 b3c', real=True)
A = A0 + a1*sp.cos(th) + b1c*sp.sin(th) + a2*sp.cos(2*th) + b2c*sp.sin(2*th) + a3*sp.cos(3*th) + b3c*sp.sin(3*th)
rhs = sp.sin(th)*sp.diff(A, th) - p*sp.cos(th)*A
rc = sp.integrate(sp.expand(rhs*sp.cos(th)), (th, 0, 2*sp.pi))/sp.pi
rs = sp.integrate(sp.expand(rhs*sp.sin(th)), (th, 0, 2*sp.pi))/sp.pi
chk('Psi_cos + A0/(p+2) + a2/(2p)', rc/((p + 1)**2 - 1) + A0/(p + 2) + a2/(2*p))
chk('Psi_sin + b2/(2p)', rs/((p + 1)**2 - 1) + b2c/(2*p))
chk('rhs form vs (sin A)\' - (p+1) cos A', rhs - (sp.diff(sp.sin(th)*A, th) - (p + 1)*sp.cos(th)*A))
# 4. singular family
ap, am = sp.symbols('ap am', positive=True)
xp = sp.symbols('xp', positive=True)
for fs, var, sgn in [(ap*xp**p, xp, 1)]:
    fx = sp.diff(fs, xp)
    chk('singular transport x f_x - p f', xp*fx - p*fs)
# 1D transition exponent: f(x), b = ((1-s) x, (1+s) y - f): (1-s) x f' = p f
s_ = sp.symbols('s')
F = sp.Function('F')
print('   1D ODE solution:', sp.dsolve((1 - s_)*x*F(x).diff(x) - p*F(x)))
# 5. saddle order: q2 = 2 + (4 l - 1)/sigma with l = 1/p, sigma = s/p
chk('q2 rescaled', 2 + (4/p - 1)/(s_/p) - (2 + (4 - p)/s_))
# 6. nullcline speed: b1 = p f/f_x on the nullcline, f = x^2 + O(3): p x^2/(2x) = p x/2
chk('nullcline', p*x**2/(2*x) - p*x/2)
print('ALL ZERO:', all(sp.simplify(v) == 0 for _, v in out))
