"""Lead check of the referee record 'c2saddle' (2026-10-28T21:43Z): (K) the source-strain kernel for odd eta (reflection class E),
(E) the fractional equatorial ODEs and the identity E (c - f)/A = K (3c + mu)/mu, (X) the c = 3/5, k = 5/2 local example,
(M) the central moment value -(c + mu)/3 from phi_z(0, 0) = -(c + mu)/2."""
import sympy as sp, json, time
t0 = time.time(); res = {}
r, z, Z, c, mu, K, Q = sp.symbols('r z Z c mu K Q', positive=True)
# (K) phi(0, Z) = (1/4) int_{z>0} r^3 eta [rho_-^-3 - rho_+^-3]; differentiate in Z
G = (r**2 + (z - Z)**2)**sp.Rational(-3, 2) - (r**2 + (z + Z)**2)**sp.Rational(-3, 2)
dG = sp.diff(G, Z).subs(Z, 1)
plus = 3*((z - 1)*(r**2 + (z - 1)**2)**sp.Rational(-5, 2) + (z + 1)*(r**2 + (z + 1)**2)**sp.Rational(-5, 2))
minus = 3*((z - 1)*(r**2 + (z - 1)**2)**sp.Rational(-5, 2) - (z + 1)*(r**2 + (z + 1)**2)**sp.Rational(-5, 2))
res['K_plus_kernel_correct'] = sp.simplify(dG - plus) == 0
res['K_minus_kernel_correct'] = sp.simplify(dG - minus) == 0
# sign of the corrected kernel: z >= 1 positive; near the axis for 0 < z < 1 negative; large r positive
Sp = plus/3
res['K_sample_z1.5_r0.3'] = float(Sp.subs({z: 1.5, r: 0.3}))
res['K_sample_z0.5_r0.1'] = float(Sp.subs({z: 0.5, r: 0.1}))
res['K_sample_z0.5_r5'] = float(Sp.subs({z: 0.5, r: 5}))
# (E) equatorial ODEs from R_q, R_eta with phi = z f(s) + O(z^3), q = A |z|^k, eta = E sgn(z) |z|^(k-1) (z > 0)
s = sp.symbols('s', positive=True); k = 1 + (1 + c)/mu
f, A, E = [sp.Function(n)(s) for n in ('f', 'A', 'E')]
phi = z*f; q = A*z**k; eta = E*z**(k - 1)
Ws = 2*s*(c - sp.diff(phi, z)); Wz = c*z + 2*phi + 2*s*sp.diff(phi, s)
Rq = sp.simplify(((1 - 2*sp.diff(phi, z))*q + Ws*sp.diff(q, s) + Wz*sp.diff(q, z))/z**k)
Re_lin = sp.simplify(((1 + c)*eta + Ws*sp.diff(eta, s) + Wz*sp.diff(eta, z))/z**(k - 1))
h = 2*s*(c - f); b = c + 2*f + 2*s*sp.diff(f, s)
res['E_q_ode'] = sp.simplify(Rq - (h*sp.diff(A, s) + (1 - 2*f + k*b)*A)) == 0
res['E_eta_ode'] = sp.simplify(Re_lin - (h*sp.diff(E, s) + ((1 + c) + (k - 1)*b)*E)) == 0
Ap = -(1 - 2*f + k*b)*A/h; Ep = -((1 + c) + (k - 1)*b)*E/h
res['E_identity'] = sp.simplify(Ep/E - Ap/A - sp.diff(f, s)/(c - f)) == 0
f0 = -(c + mu)/2; E0 = 2*K*Q/mu
res['E_constant'] = str(sp.simplify(E0*(c - f0)/Q))  # expect K (3c + mu)/mu
res['E_constant_ok'] = sp.simplify(E0*(c - f0)/Q - K*(3*c + mu)/mu) == 0
res['E_recovers_smooth'] = sp.simplify((K*(3*c + mu)/mu).subs(mu, 1 + c) - K*(1 + 4*c)/(1 + c)) == 0
# (X) example c = 3/5, k = 5/2, K = Q = 1
cc = sp.Rational(3, 5); kk = sp.Rational(5, 2); mm = (1 + cc)/(kk - 1)
res['X_mu'] = str(mm); res['X_phi_lin'] = str(-(cc + mm)/2); res['X_phi_sing'] = str(-2/(mm*kk*(kk + 1)))
# check the axis system for phi = F(z), q = q(z) to the first nonlinear order: w = c z + 2F, w q' = (w' - delta) q, w eta = 2 q (q - K), eta = -F''
zz = sp.symbols('zz', positive=True)
c6 = sp.symbols('c6')
F = -(cc + mm)/2*zz - sp.Rational(3, 14)*zz**sp.Rational(7, 2) + c6*zz**6  # c6: next term, exponent 2k + 1 of the phi set
w = cc*zz + 2*F; qq = zz**kk + sp.Rational(9, 56)*zz**5
eq1 = sp.expand(w*sp.diff(qq, zz) - (sp.diff(w, zz) - (1 + cc))*qq)
eq2 = sp.expand(w*(-sp.diff(F, zz, 2)) - 2*qq*(qq - 1))
res['X_eq1_leading_terms'] = str(sp.nsimplify(sp.series(eq1/zz**kk, zz, 0, 4).removeO()))
lead2 = sp.nsimplify(sp.series(eq2/zz**kk, zz, 0, 3).removeO())
c6v = sp.solve(sp.expand(lead2/zz**sp.Rational(5, 2)).subs(zz, 0), c6)[0]
res['X_c6'] = str(c6v)
res['X_eq2_leading_terms_after_c6'] = str(sp.simplify(lead2.subs(c6, c6v)))
res['X_eq2_order_zero_ok'] = sp.simplify(lead2.subs(c6, c6v)) == 0
# (M) central moment: phi_z(0,0) = (3/2) int_{z>0} z r^3 eta R^-5 = -(c + mu)/2
res['M_value'] = str(sp.Rational(2, 3)*(-(c + mu)/2))
res['seconds'] = round(time.time() - t0, 2)
print(json.dumps(res, indent=1))
json.dump(res, open('author_checks/c2saddle_check_output.json', 'w'), indent=1)
