# Lead checks of the auditrev findings that change formulas in AXISYMMETRIC_OBSTRUCTION_AUDIT.md (v37; the finding-12 test and
# the eigenvalue and derivative assertions were repaired for v38 after the referee's second review found that b was declared
# positive, so the cancellation root could not be found, and that all_pass omitted those checks).
# Usage: python3 checks/auditrev_check.py; writes checks/auditrev_check_output.json.
import json, sympy as sp
r, z, R, mu, rho = sp.symbols('r z R mu rho', positive=True)
out = {}
# finding 5: local Cartesian C^2 S2-type source with fractional swirl power (c = 2/3, j = 3/4, A = -4/7)
c, j, A = sp.Rational(2, 3), sp.Rational(3, 4), sp.Rational(-4, 7)
Ur, Uz, Ut = A*r, -2*A*z, r**(2*j + 1)
P = -A*(1 + A)/2*r**2 + r**(4*j + 2)/(4*j + 2) + A*(1 - 2*A)*z**2
Wr, Wz = c*r + Ur, c*z + Uz
mr = (1 - c)*Ur + Wr*sp.diff(Ur, r) + Wz*sp.diff(Ur, z) - Ut**2/r + sp.diff(P, r)
mt = (1 - c)*Ut + Wr*sp.diff(Ut, r) + Wz*sp.diff(Ut, z) + Ur*Ut/r
mz = (1 - c)*Uz + Wr*sp.diff(Uz, r) + Wz*sp.diff(Uz, z) + sp.diff(P, z)
dv = sp.diff(r*Ur, r)/r + sp.diff(Uz, z)
out['f5_momentum_and_div_zero'] = all(sp.simplify(e) == 0 for e in (mr, mt, mz, dv))
out['f5_eigenvalues'] = [str(c + A), str(c - 2*A)]
out['f5_A_formula'] = sp.simplify(A + (1 + 2*j*c)/(2*(j + 1))) == 0
# finding 9: eta from w eta = 2 q (q - K) with w ~ -m z, q ~ Q |z|^k, leading order on z < 0
K, Q, m, k = sp.symbols('K Q m k', positive=True)
zn = sp.Symbol('zn', negative=True)
eta_neg = sp.simplify((2*Q*(-zn)**k*(-K))/(-m*zn) / (-zn)**(k - 1))   # leading coefficient on z < 0
out['f9_negative_side_coefficient'] = str(eta_neg)                     # expect -2 K Q / m = (2 K Q/m) sgn(z)
out['f9_sign_ok'] = sp.simplify(eta_neg + 2*K*Q/m) == 0
# finding 13: squared 5D L^2 mass of a homogeneous cubic in a ball of radius rho scales like rho^11
out['f13_radial_integral'] = str(sp.integrate(R**6*R**4, (R, 0, rho)))
# finding 21: reflected source-strain kernel, value at r = 1, z = 2 and the equatorial expansion
S1 = (z - 1)/(r**2 + (z - 1)**2)**sp.Rational(5, 2) + (z + 1)/(r**2 + (z + 1)**2)**sp.Rational(5, 2)
v = sp.nsimplify(S1.subs({r: 1, z: 2}))
out['f21_S1_at_1_2'] = str(sp.simplify(v)); out['f21_positive'] = bool(v > 0)
zz = sp.Symbol('zz')
ser = sp.series(S1.subs(z, zz), zz, 0, 2).removeO()
out['f21_equatorial_expansion_ok'] = sp.simplify(ser - 2*(r**2 - 4)*(r**2 + 1)**sp.Rational(-7, 2)*zz) == 0
# finding 12: the far-axis coefficient (2 K^2 H/c)(H + b + b/c) vanishes at b = -H c/(c + 1)
H, cc = sp.symbols('H c', positive=True)
b = sp.Symbol('b', real=True)
coef = 2*K**2*H/cc*(H + b + b/cc)
out['f12_zero_at'] = str(sp.solve(H + b + b/cc, b))
out['f12_vanishes_at_root'] = sp.simplify(coef.subs(b, -H*cc/(cc + 1))) == 0
out['f12_root_negative'] = bool(sp.simplify(-H*cc/(cc + 1)).is_negative)
# finding 1: oscillatory remainder r R^(-alpha-2) sin(R^3) has derivative of order R^(1-alpha)
al = sp.Symbol('alpha', positive=True)
d = sp.diff(R**(-al - 1)*sp.sin(R**3), R)
out['f1_derivative_leading'] = str(sp.simplify(sp.expand(d).coeff(sp.cos(R**3))))
out['f1_derivative_ok'] = sp.simplify(sp.expand(d).coeff(sp.cos(R**3)) - 3*R**(1 - al)) == 0
out['f5_eigenvalues_ok'] = out['f5_eigenvalues'] == ['2/21', '38/21']
out['all_pass'] = bool(out['f5_momentum_and_div_zero'] and out['f5_A_formula'] and out['f9_sign_ok'] and out['f21_positive']
                       and out['f21_equatorial_expansion_ok'] and out['f13_radial_integral'] == 'rho**11/11'
                       and out['f12_vanishes_at_root'] and out['f12_root_negative'] and out['f1_derivative_ok']
                       and out['f5_eigenvalues_ok'])
json.dump(out, open(__file__.replace('.py', '_output.json'), 'w'), indent=1)
print(json.dumps(out, indent=1))
