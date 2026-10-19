"""V143: the gauge statement for rho = x^2 (referee audit 26 (42)-(44); FR Section 2 growth-class sentences).
Part A (sympy): Newtonian potential F, psi_circ, W_circ; the obstruction x^2 y/2 for W_circ + M X; the general
harmonic cubic + quadratic gauge that makes x^2 a profile (unique); the particular-solution decomposition of FR line 45.
Part B (numerics): the radially truncated twice-subtracted law (own quadrature, W2 of tests/v142_m39.py, Rmax = R)
for rho = x^2 at several X and two truncation radii R, compared with W_circ.
"""
import sys, math
import numpy as np
import sympy as sp
ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)
x, y, l = sp.symbols('x y l', real=True)
m11, m12, a, b, c, d = sp.symbols('m11 m12 a b c d', real=True)
lap = lambda u: sp.diff(u, x, 2) + sp.diff(u, y, 2)
perp = lambda P: sp.Matrix([-sp.diff(P, y), sp.diff(P, x)])
rho = x**2
F = -(x**2 + y**2)**2/32 - (x**4 - y**4)/24
rep('C1 -Lap F = x^2 (referee audit 26 (42))', sp.expand(-lap(F) - rho) == 0)
# interior homogeneous parts of the truncated Newtonian potential: modes 0 and 2 only -> constant and x^2 - y^2, x y
psiF = sp.diff(F, x)
rep('C2 psi = d_x F solves -Lap psi = rho_x', sp.expand(-lap(psiF) - sp.diff(rho, x)) == 0)
# the omitted harmonic quadratic A (x^2 - y^2) + B x y gives d_x of it = 2 A x + B y: velocity constant -> removed by centering
A_, B_ = sp.symbols('A B'); Wq = perp(sp.diff(A_*(x**2 - y**2) + B_*x*y, x))
rep('C3 omitted harmonic quadratic of F gives a constant velocity', all(sp.diff(Wq[i], v) == 0 for i in range(2) for v in (x, y)), Wq.T)
Wc = perp(psiF); Wc = Wc - Wc.subs({x: 0, y: 0}) - Wc.jacobian([x, y]).subs({x: 0, y: 0})*sp.Matrix([x, y])
psi_circ = -(7*x**3 + 3*x*y**2)/24
rep('C4 psi_circ = d_x F = -(7x^3 + 3xy^2)/24', sp.expand(psiF - psi_circ) == 0)
rep('C5 centered W_circ = (xy/4, -(7x^2 + y^2)/8) (referee audit 26 (43)); DW(0) = 0 by parity', sp.expand(Wc - sp.Matrix([x*y/4, -(7*x**2 + y**2)/8])) == sp.zeros(2, 1))
rep('C6 psi_circ = -x(x^2 + y^2)/4 - (x^3 - 3xy^2)/24', sp.expand(psi_circ + x*(x**2 + y**2)/4 + (x**3 - 3*x*y**2)/24) == 0)
# obstruction: V = l X + M X + W_circ, M symmetric traceless
Ms = sp.Matrix([[m11, m12], [m12, -m11]])
V = l*sp.Matrix([x, y]) + Ms*sp.Matrix([x, y]) + sp.Matrix([x*y/4, -(7*x**2 + y**2)/8])
E = sp.Poly(sp.expand(V[0]*sp.diff(rho, x) + V[1]*sp.diff(rho, y) - rho), x, y)
rep('C7 W_circ + M X: coefficient of x^2 y in V.grad rho - rho is 1/2 for all l, M (not a profile)', E.coeff_monomial(x**2*y) == sp.Rational(1, 2), E.as_expr())
# general gauge: add a Re z^3 + b Im z^3 + c Re z^2 + d Im z^2 to psi_circ (all harmonic stream polynomials of degree 2, 3)
z = x + sp.I*y
G = a*sp.re(sp.expand(z**3)) + b*sp.im(sp.expand(z**3)) + c*sp.re(sp.expand(z**2)) + d*sp.im(sp.expand(z**2))
psiG = psi_circ + G
VG = l*sp.Matrix([x, y]) + perp(psiG)
EG = sp.Poly(sp.expand(VG[0]*sp.diff(rho, x) + VG[1]*sp.diff(rho, y) - rho), x, y)
solG = sp.solve(EG.coeffs(), [a, b, c, d], dict=True)
rep('C8 x^2 is a profile iff a = -1/24, b = 0, c = 0, d = (l - 1/2)/2 (unique gauge in degrees 2, 3)',
    solG == [{a: -sp.Rational(1, 24), b: 0, c: 0, d: (l - sp.Rational(1, 2))/2}], solG)
psi_fin = sp.expand(psiG.subs(solG[0]))
rep('C9 resulting psi = -x^3/3 + (l - 1/2) x y; added = -(x^3 - 3xy^2)/24 + (l - 1/2) x y (referee audit 26 (44))',
    sp.expand(psi_fin - (-x**3/3 + (l - sp.Rational(1, 2))*x*y)) == 0 and sp.expand(G.subs(solG[0]) - (-(x**3 - 3*x*y**2)/24 + (l - sp.Rational(1, 2))*x*y)) == 0)
Wf = perp(psi_fin)
rep('C10 W = ((1/2 - l) x, (l - 1/2) y - x^2), V = (x/2, (2l - 1/2) y - x^2) (referee audit 26 (40))',
    sp.expand(Wf - sp.Matrix([(sp.Rational(1, 2) - l)*x, (l - sp.Rational(1, 2))*y - x**2])) == sp.zeros(2, 1) and
    sp.expand(l*sp.Matrix([x, y]) + Wf - sp.Matrix([x/2, (2*l - sp.Rational(1, 2))*y - x**2])) == sp.zeros(2, 1))
rep('C11 FR line 45: psi - (-x(x^2 + y^2)/4) = -(x^3 - 3xy^2)/12 + (l - 1/2) x y; -Lap(-x(x^2+y^2)/4) = 2x',
    sp.expand(psi_fin + x*(x**2 + y**2)/4 - (-(x**3 - 3*x*y**2)/12 + (l - sp.Rational(1, 2))*x*y)) == 0 and sp.expand(-lap(-x*(x**2 + y**2)/4) - 2*x) == 0)
# angular cancellation of the derivative subtractions for rho = x^2 (complex form: 2 xi/eta^3 and 3 xi^2/eta^4 against modes 0, +-2)
th = sp.symbols('theta', real=True)
rhoth = sp.cos(th)**2
c1 = sp.integrate(sp.expand(sp.exp(-3*sp.I*th)*rhoth, complex=True), (th, 0, 2*sp.pi))
c2 = sp.integrate(sp.expand(sp.exp(-4*sp.I*th)*rhoth, complex=True), (th, 0, 2*sp.pi))
rep('C12 circle means of DK(-Y) X rho and D^2K(-Y)[X, X] rho vanish for rho = x^2 (subtractions inactive, R-independent)', sp.simplify(c1) == 0 and sp.simplify(c2) == 0)
if len(sys.argv) > 1 and sys.argv[1] == 'symonly':
    print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok)); sys.exit(0)
# Part B: numerics with the W2 quadrature of tests/v142_m39.py (definitions only)
src = open(__file__.replace('v143_gauge.py', 'v142_m39.py')).read()
s0 = src.index('import torch'); s1 = src.index('results = {}')
exec(src[s0:s1])
import torch
for R in [1e3, 1e6]:
    for P in [(0.6, 0.4), (2.0, -1.0), (-3.0, 2.5), (7.0, 5.0)]:
        w1, w2 = W2(lambda X_, Y_: X_**2, P, Rmax=R)
        e1 = P[0]*P[1]/4; e2 = -(7*P[0]**2 + P[1]**2)/8
        err = max(abs(w1 - e1), abs(w2 - e2))/(1 + P[0]**2 + P[1]**2)
        rep('D1 rho = x^2 truncated at R = %g, X = %s: W_2 = W_circ' % (R, P), err < 1e-6, '(W2 = %.9f, %.9f; W_circ %.9f, %.9f; rel err %.1e)' % (w1, w2, e1, e2, err))
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
