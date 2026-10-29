"""Lead check of the T2 (odd-swirl ring) referee claims (referee answer 'ring', 2026-10-28T20:59Z).
Regular (s, z) forms: R_q = q + 2s(c - Phi_z) q_s + (c z + 2 Phi + 2 s Phi_s) q_z - 2 Phi_z q,
R_eta = (1+c) eta + 2s(c - Phi_z) eta_s + (c z + 2 Phi + 2 s Phi_s) eta_z - 2 q q_z, eta = -(4 s Phi_ss + 8 Phi_s + Phi_zz).
Checks: (A) origin jets (7) through the stated weights; (B) axis equations (17) and the Y equation (18);
(C) ring equations (1), (2); (D) amplitude relation (15) on the germ F = A0 - nu s; (E) 5D harmonicity of H3, H5, H7."""
import sympy as sp, json, time
t0 = time.time()
s, z, c, C, K, h3, h5, h7, lam_w = sp.symbols('s z c C K h3 h5 h7 lam_w')
d = 1 + c; lam = 1 + 4*c; A0 = (1 + 3*c)/2; nu = d/2; a = 2*c - 1
L5 = lambda f: 4*s*sp.diff(f, s, 2) + 8*sp.diff(f, s) + sp.diff(f, z, 2)
def Rq(P, q): return sp.expand(q + 2*s*(c - sp.diff(P, z))*sp.diff(q, s) + (c*z + 2*P + 2*s*sp.diff(P, s))*sp.diff(q, z) - 2*sp.diff(P, z)*q)
def Re(P, q, e): return sp.expand(d*e + 2*s*(c - sp.diff(P, z))*sp.diff(e, s) + (c*z + 2*P + 2*s*sp.diff(P, s))*sp.diff(e, z) - 2*q*sp.diff(q, z))
def wt_part(expr, wmax):
    """terms of weighted degree <= wmax (s weight 2, z weight 1)"""
    p = sp.Poly(sp.expand(expr), s, z)
    return sp.simplify(sum(coef*s**i*z**j for (i, j), coef in p.terms() if 2*i + j <= wmax))
res = {}
# (E)
H3 = z**3 - sp.Rational(3, 4)*s*z
H5 = z**5 - sp.Rational(5, 2)*s*z**3 + sp.Rational(5, 8)*s**2*z
H7 = z**7 - sp.Rational(21, 4)*s*z**5 + sp.Rational(35, 8)*s**2*z**3 - sp.Rational(35, 64)*s**3*z
res['E_harmonic'] = [sp.simplify(L5(H)) == 0 for H in (H3, H5, H7)]
res['E_L5_s3z'] = sp.simplify(L5(s**3*z) - 48*s**2*z) == 0
# (A) origin jets
P = A0*z + h3*H3 + h5*H5 + h7*H7 - C**2/(72*c)*s**3*z
q = C*s*z + 5*C*h3/lam*s*z**3
e = -L5(P)
res['A_eta_wt5'] = str(sp.factor(wt_part(e, 5)))
res['A_eta_matches'] = sp.simplify(wt_part(e, 5) - 2*C**2/(3*c)*s**2*z) == 0
# q terms through weight 5 are exact; R_q through weight 5 must vanish
res['A_Rq_wt5_zero'] = sp.simplify(wt_part(Rq(P, q), 5)) == 0
res['A_Reta_wt5_zero'] = sp.simplify(wt_part(Re(P, q, e), 5)) == 0
# does an s^2 z term in q get forced? add b s^2 z and solve weight-5 R_q
b = sp.Symbol('b'); qb = q + b*s**2*z
sol = sp.solve(sp.Poly(wt_part(Rq(P, qb), 5), s, z).coeffs(), b, dict=True)
res['A_s2z_coefficient_forced'] = str(sol)
# (B) axis equations
f, g1, g2, Q, Q2, J, J3 = [sp.Function(n)(z) for n in ('f', 'g1', 'g2', 'Q', 'Q2', 'J', 'J3')]
PB = f + s*g1 + s**2*g2
qB = s*Q + s**2*Q2
eB = s**2*J + s**3*J3
w = c*z + 2*f
rq1 = sp.expand(Rq(PB, qB)).coeff(s, 1)
re2 = sp.expand(Re(PB, qB, eB)).coeff(s, 2)
wp = sp.diff(w, z)
res['B_Rq_s1'] = sp.simplify(rq1 - (w*sp.diff(Q, z) - (2*wp - lam)*Q)) == 0
res['B_Reta_s2'] = sp.simplify(re2 - (w*sp.diff(J, z) + (1 + 7*c - 2*wp)*J - 2*Q*sp.diff(Q, z))) == 0
# also R_eta at s^0 and s^1 with eta = s^0 e0(z) + s e1(z): homogeneous transport
e0, e1 = sp.Function('e0')(z), sp.Function('e1')(z)
re01 = sp.expand(Re(PB, qB, e0 + s*e1))
res['B_Reta_s0'] = str(sp.simplify(re01.coeff(s, 0)))
res['B_Reta_s1'] = str(sp.simplify(re01.coeff(s, 1) - (w*sp.diff(e1, z) + (d + 2*(c - sp.diff(f, z)))*e1)))
q0f = sp.Function('q0f')(z)
res['B_Rq_s0'] = str(sp.simplify(sp.expand(Rq(PB, q0f + s*Q)).coeff(s, 0)))
# Y equation: substitute J' and Q' from the axis equations
Yf = w*J/Q**2
Qp = (2*wp - lam)*Q/w
Jp = (2*Q*Qp - (1 + 7*c - 2*wp)*J)/w
dY = sp.diff(Yf, z).subs({sp.Derivative(Q, z): Qp, sp.Derivative(J, z): Jp})
res['B_Y_eq'] = sp.simplify(w*dY + (wp - d)*(Yf - 4) + 2*a) == 0
# (C) ring equations
F, G, Qr, T, E = [sp.Function(n)(s) for n in ('F', 'G', 'Qr', 'T', 'E')]
PC = z*F + z**3*G; qC = z*Qr + z**3*T; eC = z*E
h = 2*s*(c - F); bb = c + 2*F + 2*s*sp.diff(F, s)
res['C_q_z1'] = sp.simplify(sp.expand(Rq(PC, qC)).coeff(z, 1) - (h*sp.diff(Qr, s) + (d + 2*s*sp.diff(F, s))*Qr)) == 0
res['C_e_z1'] = sp.simplify(sp.expand(Re(PC, qC, eC)).coeff(z, 1) - (h*sp.diff(E, s) + (d + bb)*E - 2*Qr**2)) == 0
res['C_poisson_z1'] = sp.simplify(sp.expand(-L5(PC)).coeff(z, 1) - (-(4*s*sp.diff(F, s, 2) + 8*sp.diff(F, s)) - 6*G)) == 0
# ring values: F = c - (d/2) x + f2 x^2, x = s - 1; E(1) from (d + b(1)) E(1) = 2K^2
f2 = sp.Symbol('f2'); xx = s - 1
Fr = c - d/2*xx + f2*xx**2
b1 = (c + 2*Fr + 2*s*sp.diff(Fr, s)).subs(s, 1)
res['C_e0'] = str(sp.simplify(2*K**2/(d + b1)))
# k1: h Q' + (d + 2 s F') Q = 0 at order x with Q = K + k1 x
k1 = sp.Symbol('k1')
X = sp.Symbol('X')
FX = c - d/2*X + f2*X**2  # F as a function of X = s - 1
expr = sp.expand(2*(1 + X)*(c - FX)*k1 + (d + 2*(1 + X)*sp.diff(FX, X))*(K + k1*X))
res['C_k1'] = str([sp.factor(v) for v in sp.solve(expr.coeff(X, 1), k1)])
res['C_k1_matches'] = sp.simplify(sp.solve(expr.coeff(X, 1), k1)[0] - K*(d - 4*f2)/d) == 0
res['C_order0'] = str(sp.simplify(expr.coeff(X, 0)))
# (D) amplitude relation on F = A0 - nu s: integrand of (15)
Fl = A0 - nu*s
integrand = sp.simplify((1 + 3*c - 2*Fl + 2*s*sp.diff(Fl, s))/(2*s*(c - Fl)))
res['D_integrand_linear_germ'] = str(integrand)
res['seconds'] = round(time.time() - t0, 2)
print(json.dumps(res, indent=1))
json.dump(res, open('author_checks/t2_ring_check_output.json', 'w'), indent=1)
