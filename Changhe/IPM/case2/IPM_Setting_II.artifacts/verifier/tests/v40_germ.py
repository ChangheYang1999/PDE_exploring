"""V40 (referee result 13 germ), sympy: F = x^2 (|x|^(2q) + y^2)^((gamma-2)/(2q)), gamma = 1/a, q = b/a, linear node N = (a x, b y).
Checks: N.grad F = F (x > 0 and x < 0); F = |x|^gamma G(tau), tau = y/|x|^q, G = (1 + tau^2)^((gamma-2)/(2q)) (nonconstant);
anisotropic scaling of F_x: F_x(e^(a t) x, e^(b t) y) = e^((1-a) t) F_x(x, y)."""
import sympy as sp
x, y, t = sp.symbols('x y t', real=True)
a, b = sp.symbols('a b', positive=True)
q = b/a; g = 1/a
out = []
for sgn, xs in ((1, sp.Symbol('X', positive=True)), (-1, -sp.Symbol('X', positive=True))):
    X = sp.Symbol('X', positive=True)
    xv = sgn*X
    F = xv**2*(X**(2*q) + y**2)**((g - 2)/(2*q))
    # derivative in x: d/dx = sgn d/dX
    Fx = sgn*sp.diff(F, X)
    r1 = sp.simplify((a*xv*Fx + b*y*sp.diff(F, y) - F)/F)
    out.append(('N.grad F - F, sign %d' % sgn, r1))
    tau = y/X**q
    G = (1 + tau**2)**((g - 2)/(2*q))
    out.append(('F - |x|^gamma G(tau), sign %d' % sgn, sp.simplify(sp.powsimp(sp.expand_power_base(F - X**g*G, force=True), force=True))))
    Fx_s = Fx.subs({X: sp.exp(a*t)*X, y: sp.exp(b*t)*y}, simultaneous=True)
    out.append(('F_x scaling exponent 1 - a, sign %d' % sgn, sp.simplify(sp.powsimp(sp.expand_power_base(Fx_s/(sp.exp((1 - a)*t)*Fx), force=True), force=True) - 1)))
for n, v in out:
    print(n, ':', v)
# numeric spot checks of the three identities at a = 0.6085, b = 3.3915 (p = 0.5 state of specification M22)
vals = {a: sp.Float('0.6085'), b: sp.Float('3.3915')}
print('spot', [sp.N(v.subs(vals).subs({sp.Symbol('X', positive=True): 0.37, y: -0.81, t: 0.4})) for _, v in out])
