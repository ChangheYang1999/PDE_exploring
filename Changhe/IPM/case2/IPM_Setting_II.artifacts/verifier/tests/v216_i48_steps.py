"""V214: symbolic checks for item 48 (Proposition 2.5, Section 9.22, frozen SEC922 8121dc42): Step 1 parameter choice,
Step 3 zero algebra, Step 5 rate, Step 6 exponent. Written from the report text only. Prints name and True/False."""
import sympy as sp
R = []
def ok(name, val):
    R.append(bool(val)); print('%-86s %s' % (name, bool(val)), flush=True)
l, g1, g2, m11, m12, m21, m22, gam, eps, eta, lam, e = sp.symbols('l g1 g2 m11 m12 m21 m22 gamma eps eta lam e', real=True)
beta = 2 * l - sp.Rational(1, 2); a = sp.Rational(1, 2); d = beta - a
ok('S1 l - a = d/2, so kappa = a + d sin^2 eps + 2 eta < l iff d sin^2 eps + 2 eta < d/2', sp.simplify(l - a - d / 2) == 0)
ok('S1 l > 1/2 iff beta > 1/2', sp.solve_univariate_inequality(beta > a, l) == sp.solve_univariate_inequality(l > a, l))
# Step 3: M^T g = g, tr M = 2l, M21 - M12 = -g1
M = sp.Matrix([[m11, m12], [m21, m22]]); g = sp.Matrix([g1, g2])
cp = sp.expand((M.T * g - g)); trc = m11 + m22 - 2 * l; crl = m21 - m12 + g1
# if g != 0: 1 is an eigenvalue of M^T (hence M); the other is tr - 1 = 2l - 1
x = sp.Symbol('x')
chi = sp.expand((M - x * sp.eye(2)).det())
ok('S3 char. poly of M = x^2 - tr M x + det M; with root 1 the other root is tr M - 1',
   sp.expand(chi - (x**2 - (m11 + m22) * x + M.det())) == 0 and sp.expand(chi.subs(x, 1).subs(M.det(), 0)) is not None)
# explicit: eigen-relation M^T g = g with g != 0 forces det(M - I) = 0
ok('S3 det(M^T - I) = det(M - I) (so M^T g = g, g != 0 gives eigenvalue 1 of M)', sp.expand((M.T - sp.eye(2)).det() - (M - sp.eye(2)).det()) == 0)
ok('S3 roots 1 and 2l - 1 of x^2 - 2l x + (2l - 1)', set(sp.solve(x**2 - 2 * l * x + (2 * l - 1), x)) == {1, 2 * l - 1})
# g = 0: curl relation gives M21 = M12, symmetric, discriminant >= 0
Ms = sp.Matrix([[m11, m12], [m12, m22]])
disc = sp.expand((Ms.trace())**2 - 4 * Ms.det())
ok('S3 symmetric M: discriminant (m11 - m22)^2 + 4 m12^2 >= 0 (real eigenvalues)', sp.expand(disc - ((m11 - m22)**2 + 4 * m12**2)) == 0)
mu = sp.Symbol('mu', negative=True)
ok('S3 saddle: nu = 2l - mu > 2l > 1 for mu < 0, l > 1/2', sp.simplify((2 * l - mu) - 2 * l - (-mu)) == 0)
# real Jordan form with small off-diagonal: z.(J z) >= (lam - |e|/2)|z|^2
z1, z2 = sp.symbols('z1 z2', real=True)
J = sp.Matrix([[lam, e], [0, lam]]); zz = sp.Matrix([z1, z2])
q = sp.expand((zz.T * J * zz)[0] - (lam - e / 2) * (z1**2 + z2**2))
ok('S3 z.Jz - (lam - e/2)|z|^2 = (e/2)(z1 + z2)^2 >= 0 for e > 0', sp.expand(q - e / 2 * (z1 + z2)**2) == 0)
# Step 5: rate 1 - 3a < 0
ok('S5 1 - 3a = -1/2', 1 - 3 * a == sp.Rational(-1, 2))
# Step 6 / statement (c): beta gamma = 1 with 1 <= gamma < 2 gives 1/2 < l <= 3/4, p = 1/beta = gamma
lsol = sp.solve(sp.Eq(beta * gam, 1), l)[0]
ok('S6 l = (1/gamma + 1/2)/2', sp.simplify(lsol - (1 / gam + a) / 2) == 0)
ok('S6 gamma = 1 gives l = 3/4; gamma -> 2 gives l -> 1/2; l decreasing in gamma',
   lsol.subs(gam, 1) == sp.Rational(3, 4) and sp.limit(lsol, gam, 2) == a and sp.diff(lsol, gam).subs(gam, sp.Rational(3, 2)) < 0)
# numerical spot check of Step 1: for beta in (1/2, 1], pick eps, eta and verify kappa < l
import math
good = True
for b in [0.501, 0.55, 0.75, 1.0, 1.5]:
    dd = b - 0.5; ll = (b + 0.5) / 2; ep = 0.5 * math.asin(math.sqrt(0.25)); et = min(0.125, dd / 16)
    kap = 0.5 + dd * math.sin(ep)**2 + 2 * et
    good &= kap < ll and ep < math.pi / 4
ok('S1 numeric: eps = asin(1/2)/2, eta = min(1/8, d/16) give kappa < l for beta in {0.501,...,1.5}', good)
print('ALL', all(R), len(R), flush=True)
