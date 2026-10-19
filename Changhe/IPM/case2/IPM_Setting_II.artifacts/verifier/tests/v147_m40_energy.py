"""V147: specification M40 (i) localized energy identity
    int chi |W|^2 = (1 + 3l) int chi y rho + int y rho V.grad chi - int q W.grad chi,
with grad q = W + rho e_2 (q = Pi - l|X|^2/2), div W = 0, V = l X + W, V.grad rho = rho.
Exact check on the polynomial example rho = x^2, W = ((1/2 - l) x, (l - 1/2) y - x^2) (growth 2; identities only),
with chi = exp(-a x^2 - c y^2 + s x y) shapes, by exact integration over R^2.
"""
import sympy as sp
x, y, l = sp.symbols('x y l', real=True)
ok = []
def rep(n, c):
    ok.append(bool(c)); print(('OK   ' if c else 'FAIL ') + n, flush=True)
rho = x**2; b = 2*l - sp.Rational(1, 2)
W = sp.Matrix([(sp.Rational(1, 2) - l)*x, (l - sp.Rational(1, 2))*y - x**2]); V = l*sp.Matrix([x, y]) + W
q = x**2/4 + b*y**2/2 - l*(x**2 + y**2)/2
rep('F1 grad q = W + rho e_2', sp.simplify(sp.Matrix([sp.diff(q, x), sp.diff(q, y)]) - W - sp.Matrix([0, rho])) == sp.zeros(2, 1))
rep('F2 div W = 0, V.grad rho = rho', sp.simplify(sp.diff(W[0], x) + sp.diff(W[1], y)) == 0 and sp.simplify(V[0]*sp.diff(rho, x) + V[1]*sp.diff(rho, y) - rho) == 0)
for (a, c, s) in [(1, 1, 0), (2, sp.Rational(1, 2), sp.Rational(1, 3)), (sp.Rational(3, 2), 1, -1)]:
    chi = sp.exp(-a*x**2 - c*y**2 + s*x*y)
    gc = sp.Matrix([sp.diff(chi, x), sp.diff(chi, y)])
    lhs = chi*(W[0]**2 + W[1]**2)
    rhs = (1 + 3*l)*chi*y*rho + y*rho*(V.T*gc)[0] - q*(W.T*gc)[0]
    I = sp.integrate(sp.expand(lhs - rhs), (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo))
    rep('F3 identity, chi = exp(-%s x^2 - %s y^2 + %s xy): integral of difference = 0 for all l' % (a, c, s), sp.simplify(I) == 0)
# general proof as a divergence: |W|^2 chi - [...] = div(chi q W) - div(chi y rho V) (pointwise, using the relations)
lhs = sp.Function('chi')(x, y)
chi = lhs; gc = sp.Matrix([sp.diff(chi, x), sp.diff(chi, y)])
expr = chi*(W[0]**2 + W[1]**2) - ((1 + 3*l)*chi*y*rho + y*rho*(V.T*gc)[0] - q*(W.T*gc)[0])
div = sp.diff(chi*q*W[0] - 0, x) + sp.diff(chi*q*W[1], y) - sp.diff(chi*y*rho*V[0], x) - sp.diff(chi*y*rho*V[1], y)
rep('F4 pointwise: integrand difference = div(chi q W - chi y rho V) (example, general chi)', sp.simplify(sp.expand(expr - div)) == 0)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
