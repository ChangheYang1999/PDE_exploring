# Independent check (lead) of the referee's c = 3/5 S1 jet sample, using the cylindrical (r, z) residuals
# of MATHEMATICAL_FORMULATION.md section 2 rather than the referee's (s, x) code.
import sympy as S
r, z, z0, eps, tau, t = S.symbols('r z z0 eps tau t', real=True)
c = S.Rational(3, 5)
x = z - z0
s = r**2
phi = (-3*z0/10 + x/2
       + eps*(x**4 - S.Rational(169, 96)*s*x**2 + S.Rational(30589, 93312)*s**2)
       + tau*(x**5 - S.Rational(1405, 512)*s*x**3 + S.Rational(546545, 591872)*s**2*x))
q = (1 + eps*(S.Rational(5, 3)*x**3 - S.Rational(845, 216)*s*x)
     + tau*(S.Rational(25, 16)*x**4 - S.Rational(21075, 4352)*s*x**2 + S.Rational(2732725, 591872)*s**2))
Ur = -r*S.diff(phi, z)
Uz = 2*phi + r*S.diff(phi, r)
Wr, Wz = c*r + Ur, c*z + Uz
eta = -(S.diff(phi, r, 2) + 3*S.diff(phi, r)/r + S.diff(phi, z, 2))
Rq = q + Wr*S.diff(q, r) + Wz*S.diff(q, z) + 2*(Ur/r)*q
Re = (1 + c)*eta + Wr*S.diff(eta, r) + Wz*S.diff(eta, z) - S.diff(q**2, z)
def lowest_weight(expr):
    # substitute r -> t r, x -> t x and find the lowest power of t present
    e = S.expand(S.simplify(expr).subs(z, z0 + t*(z - z0)).subs(r, t*r))
    p = S.Poly(e, t)
    return min(m[0] for m in p.monoms()) if not e == 0 else None
print('eta jet:', S.factor(S.expand(eta)))
print('lowest weight in R_q  :', lowest_weight(Rq))
print('lowest weight in R_eta:', lowest_weight(Re))
