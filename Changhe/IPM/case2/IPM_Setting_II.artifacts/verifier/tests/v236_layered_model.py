# Sanity model for Proposition 2.6(d): the jet-free layered densities rho = A_+ y_+^p + A_- (-y)_+^p have
# d_x rho = 0, hence W_2 = 0 (the twice-subtracted field of a density with d_x rho = 0 vanishes), and
# V = diag(1/2, beta) X. Check V.grad rho = rho for beta p = 1, and the C^2 / Hessian-bound condition at y = 0.
import sympy as sp
x, y = sp.symbols('x y', real=True); b = sp.symbols('beta', positive=True)
p = 1/b
for name, rho in [('upper', y**p), ('lower', (-y)**p)]:
    yy = sp.symbols('yy', positive=True)
    r = rho.subs(y, yy) if name == 'upper' else rho.subs(y, -yy)
    V2 = b*(yy if name == 'upper' else -yy)
    # V.grad rho with V = (x/2, beta y); rho independent of x
    lhs = V2*sp.diff(rho, y).subs(y, yy if name == 'upper' else -yy)
    print(name, 'V.grad rho - rho =', sp.simplify(lhs - r))
# second derivative near y = 0+: p (p - 1) y^(p - 2) is bounded near 0 only if p = 1 or p >= 2
for pv in [sp.Rational(1, 2), 1, sp.Rational(3, 2), 2]:
    print('p =', pv, ' rho_yy on y > 0 =', sp.simplify(sp.diff(y**pv, y, 2)))
# p = 1: A_+ y_+ + A_- (-y)_+ is C^1 at y = 0 iff A_+ = -A_- (one-sided slopes A_+ and -A_-), and then equals A_+ y
print('p = 1, slopes: right A_+, left -A_-; C^1 iff A_- = -A_+ ; then rho = A_+ y, W_2 = 0, beta = 1, c_l = 3/4')
print('rho = A y fails only the jet: rho(0) = 0 but grad rho(0) = (0, A) != 0')
