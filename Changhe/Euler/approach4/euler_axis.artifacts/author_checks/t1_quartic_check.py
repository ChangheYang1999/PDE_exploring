"""Lead check of the referee's quartic source-maximum threshold for T1 (single S1 source at the origin,
reflection class E). Independent of the referee script: uses the regular (s, z) forms of
ORIGIN_AND_AXIS_REGULARITY.md section 2 and solves the weighted-order equations directly."""
import sympy as sp, json, time
t0 = time.time()
s, z, c, K, h5 = sp.symbols('s z c K h5')
p5, d5, A4, B4, C4 = sp.symbols('p5 d5 A4 B4 C4')
Phi = z/2 + h5*z**5 + p5*s*z**3 + d5*s**2*z
Q = K + A4*z**4 + B4*s*z**2 + C4*s**2
eta = -(4*s*sp.diff(Phi, s, 2) + 8*sp.diff(Phi, s) + sp.diff(Phi, z, 2))
Pz = sp.diff(Phi, z); Ps = sp.diff(Phi, s)
Wsd = 2*s*(c - Pz); Wz = c*z + 2*Phi + 2*s*Ps
Rq = sp.expand(Q + Wsd*sp.diff(Q, s) + Wz*sp.diff(Q, z) - 2*Pz*Q)
Re = sp.expand((1 + c)*eta + Wsd*sp.diff(eta, s) + Wz*sp.diff(eta, z) - 2*Q*sp.diff(Q, z))
lam = sp.symbols('lam')
def wpart(expr, d):
    e = sp.expand(expr.subs({s: lam**2*s, z: lam*z}))
    return sp.expand(e.coeff(lam, d))
low_q = [wpart(Rq, d) for d in range(0, 4)]
low_e = [wpart(Re, d) for d in range(0, 3)]
eqs = []
eqs += sp.Poly(wpart(Rq, 4), s, z).coeffs()
eqs += sp.Poly(wpart(Re, 3), s, z).coeffs()
sol = sp.solve(eqs, [p5, d5, A4, B4, C4], dict=True)
assert len(sol) == 1
sol = sol[0]
delta = c + 1; eps = c - sp.Rational(1, 2); t = delta + eps
ref = {p5: -sp.Rational(5, 8)*h5*(4 + K**2/delta**2)}
ref[d5] = -ref[p5]/4*(1 + K**2/t**2)
ref[A4] = sp.Rational(5, 2)*K*h5/delta
ref[B4] = 3*K*ref[p5]/t
ref[C4] = K*ref[d5]/(2*eps)
match = {str(k): sp.simplify(sol[k] - ref[k]) == 0 for k in ref}
disc = sp.factor(sp.simplify((sol[B4]**2 - 4*sol[A4]*sol[C4])/h5**2))
# referee: B^2 <= 4AC  <=>  (13 - 14c) K^2 >= (c + 1)(56c^2 + 28c - 37)
target = (13 - 14*c)*K**2 - (c + 1)*(56*c**2 + 28*c - 37)
ratio = sp.simplify(disc/target)
cstar = sp.nsimplify((-7 + 9*sp.sqrt(7))/28)
vals = {}
for cv in [sp.Rational(2, 3), sp.Rational(7, 10), sp.Rational(37, 50)]:
    vals[str(cv)] = float(sp.sqrt(((cv + 1)*(56*cv**2 + 28*cv - 37))/(13 - 14*cv)))
out = {
  'lower_orders_vanish': all(sp.simplify(e) == 0 for e in low_q + low_e),
  'coefficients_match_referee': match,
  'disc_over_h5sq_factored': str(disc),
  'disc_over_target': str(ratio),
  'root_of_rhs': str(sp.solve(56*c**2 + 28*c - 37, c)),
  'cstar_numeric': float((-7 + 9*sp.sqrt(7))/28),
  'Kcrit': vals,
  'Kcrit_limit_3/4': float(sp.sqrt(sp.Rational(217, 20))),
  'seconds': round(time.time() - t0, 1),
}
print(json.dumps(out, indent=1))
json.dump(out, open('t1_quartic_check_output.json', 'w'), indent=1)
