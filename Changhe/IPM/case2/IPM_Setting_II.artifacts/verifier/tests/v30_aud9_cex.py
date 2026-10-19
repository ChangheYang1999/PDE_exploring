"""V30: referee audit 9 1(c) counterexample x = u + y|u|^{5/2}, rho = u^2: third derivatives of rho in (x, y) (u > 0 side; u < 0 by the
symmetry u -> -u, x -> -x) as u -> 0+, uniformly in y on compacts.  d_x = (1/x_u) d_u, d_y|_x = d_y|_u - (x_y/x_u) d_u."""
import sympy as sp
u = sp.symbols('u', positive=True); y = sp.symbols('y', real=True)
X = u + y*u**sp.Rational(5, 2)
xu, xy = sp.diff(X, u), sp.diff(X, y)
Dx = lambda f: sp.diff(f, u)/xu
Dy = lambda f: sp.diff(f, y) - xy/xu*sp.diff(f, u)
rho = u**2
for name, ops in [('xxx', 'xxx'), ('xxy', 'xxy'), ('xyy', 'xyy'), ('yyy', 'yyy'), ('xx', 'xx'), ('xy', 'xy'), ('yy', 'yy')]:
    f = rho
    for o in ops:
        f = Dx(f) if o == 'x' else Dy(f)
    f = sp.simplify(f)
    lim = sp.limit(f, u, 0, '+')
    lead = sp.simplify(sp.series(f - lim, u, 0, 1).removeO()) if lim.is_finite else None
    print('rho_' + name, ': limit u->0+ =', lim, '| f - limit, leading terms:', lead, flush=True)
