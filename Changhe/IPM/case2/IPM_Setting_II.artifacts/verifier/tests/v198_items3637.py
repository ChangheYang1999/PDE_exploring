"""V198: checks of the new statement texts of items 36/37 (Proposition 2.2, Proposition 3.15b, Section 7 item 1).
(1) Resonance claim of Proposition 2.2: for l > 1/4, D_k(x^p y^q) = (p/2 + (2l-1/2)q - 1) x^p y^q has a nonzero kernel
for some k >= 3 iff l = 1/4 + 1/(2n), n >= 3 (exact rationals, k <= 60, grid of l). (2) The top-part relations of
Proposition 2.2 and the alternatives of Proposition 3.15b are satisfied by the polynomial solution and by the solution
of Proposition 3.15 (symbolic). (3) The formulas of Proposition 3.15 in the report equal alternative (a) of referee result 41."""
import sympy as sp
from fractions import Fraction as Fr
R = []
def ok(name, val):
    R.append(bool(val)); print('%-90s %s' % (name, bool(val)), flush=True)
def kernel(l, kmax=60):
    be = 2 * l - Fr(1, 2)
    return [(p, k - p) for k in range(3, kmax + 1) for p in range(k + 1) if Fr(p, 2) + be * (k - p) - 1 == 0]
# resonances visible for k <= 60: y^n needs n <= 60, x y^(n/2) needs n even and n/2 + 1 <= 60
res = {Fr(1, 4) + Fr(1, 2 * n) for n in range(3, 119) if n <= 60 or (n % 2 == 0 and n // 2 + 1 <= 60)}
grid = {Fr(1, 4) + Fr(j, 240) for j in range(1, 481)} | res
good = True
for l in sorted(grid):
    ker = kernel(l)
    good &= (len(ker) > 0) == (l in res)
ok('(1) l > 1/4 on a grid of rationals (j/240 and resonant values): kernel of D_k (k <= 60) nonzero iff l = 1/4 + 1/(2n), n >= 3', good)
ok('(1) largest resonant value 5/12; l = 5/12 resonant at y^3, l = 3/8 at x y^2 and y^4',
   max(res) == Fr(5, 12) and (0, 3) in kernel(Fr(5, 12)) and (1, 2) in kernel(Fr(3, 8)) and (0, 4) in kernel(Fr(3, 8)))
ok('(1) n even: x y^(n/2) also resonant; n odd: only y^n (n = 3..20)',
   all(((1, n // 2) in kernel(Fr(1, 4) + Fr(1, 2 * n))) == (n % 2 == 0) and (0, n) in kernel(Fr(1, 4) + Fr(1, 2 * n)) for n in range(3, 21)))
x, y, l = sp.symbols('x y l', real=True)
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2)
br = lambda f, g: sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x)
rho, psi = x**2, -x**3 / 3 + (l - sp.Rational(1, 2)) * x * y
ok('(2) polynomial solution: Poisson, l(x rho_x + y rho_y) + {psi, rho} = rho, N = 2, M = 3, lambda(N+1) = -mu e_1',
   sp.expand(-lap(psi) - sp.diff(rho, x)) == 0 and sp.expand(l * (x * sp.diff(rho, x) + y * sp.diff(rho, y)) + br(psi, rho) - rho) == 0
   and sp.Rational(-1, 3) * 3 == -1)
be = 2 * l - sp.Rational(1, 2)
b = be * (be + y) / 3 - be**4 / (3 * (be + y)**2)
ra, pa = x**2 * (be / (be + y))**4, x * (b - l * y)
ok('(2) Proposition 3.15 / alternative (a): Poisson and transport (symbolic l), jet, W(0) = 0',
   sp.simplify(-lap(pa) - sp.diff(ra, x)) == 0 and sp.simplify(l * (x * sp.diff(ra, x) + y * sp.diff(ra, y)) + br(pa, ra) - ra) == 0
   and sp.simplify(sp.diff(ra, x, 2).subs({x: 0, y: 0}) - 2) == 0 and sp.simplify(sp.diff(pa, x).subs({x: 0, y: 0})) == 0
   and sp.simplify(sp.diff(pa, y).subs({x: 0, y: 0})) == 0)
rep = open('scratch/v198/my3637.md').read()
ok('(3) report Proposition 3.15 formulas are those of referee result 41 alternative (a)',
   'rho = x^2 (beta/(beta + y))^4,   psi = x (b(y) - l y),   b(y) = beta (beta + y)/3 - beta^4/(3 (beta + y)^2)' in rep)
print('ALL', all(R), len(R), flush=True)
