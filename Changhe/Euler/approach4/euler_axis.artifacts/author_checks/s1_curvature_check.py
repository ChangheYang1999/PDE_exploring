# Lead check of the verifier's S1 curvature relation 4(c - 1/2)(c + 1) q_rr + [(c + 1)^2 + q0^2] q_zz = 0
# at an S1 source with q_z = 0 there (h_2 = 0), for symbolic c and K = q0. Weight-3 jet of phi, weight-2 jet of q.
import sympy as S
r, z, z0, c, K, h3, p, a, b, t = S.symbols('r z z0 c K h3 p a b t', real=True)
x = z - z0
s = r**2
phi = -c*z0/2 + x/2 + h3*x**3 + p*s*x
q = K + a*x**2 + b*s
Ur = -r*S.diff(phi, z)
Uz = 2*phi + r*S.diff(phi, r)
Wr, Wz = c*r + Ur, c*z + Uz
eta = -(S.diff(phi, r, 2) + 3*S.diff(phi, r)/r + S.diff(phi, z, 2))
Rq = S.expand(q + Wr*S.diff(q, r) + Wz*S.diff(q, z) + 2*(Ur/r)*q)
Re = S.expand((1 + c)*eta + Wr*S.diff(eta, r) + Wz*S.diff(eta, z) - S.diff(q**2, z))
def part(expr, w):
    e = S.expand(expr.subs(z, z0 + t*(z - z0)).subs(r, t*r))
    return S.expand(e.coeff(t, w))
eqs = []
for e, w in ((Rq, 0), (Rq, 1), (Rq, 2), (Re, 1)):
    P = S.Poly(part(e, w), r, z)
    eqs += [cf for cf in P.coeffs()]
sol = S.solve(eqs, [p, a, b], dict=True)
print('solution:', sol)
for so in sol:
    qrr, qzz = 2*so[b], 2*so[a]
    print('relation:', S.simplify(4*(c - S.Rational(1, 2))*(c + 1)*qrr + ((c + 1)**2 + K**2)*qzz))
