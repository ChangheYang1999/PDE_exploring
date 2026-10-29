"""Lead check of the referee record 't1scal' (2026-10-29T00:18Z) for phi = z(1 + b z^2)/(2(1 + a s + z^2)^(p + 1)), p = 1/(2c):
(R) the logarithmic radial speed at a = 1, (c r W_r + z W_z)/R^2 = c + [3t - 1 + b u t(5t - 3)]/(2(1 + u)^(p + 1)), u = R^2, t = z^2/R^2,
    and its lower bound c - 1/2 for 0 <= b <= 3 (sampled);
(C) the upper-axis coefficients C0, C1 of -Delta_5 phi = -(8 phi_s + phi_zz) at s = 0;
(A) the pole-sign bound A(p) = p(2p - 1)/(4(p + 1)) = (1 - c)/(4c(1 + 2c)) and the joint N2-N3 region."""
import sympy as sp, json, time, random, math
t0 = time.time(); res = {}
r, z, a, b, p, c, u, t, Z = sp.symbols('r z a b p c u t Z', positive=True)
s = sp.symbols('s', nonnegative=True)
# (R)
phi_r = z*(1 + b*z**2)/(2*(1 + r**2 + z**2)**(p + 1))
Ur = -r*sp.diff(phi_r, z); Uz = 2*phi_r + r*sp.diff(phi_r, r)
speed = (r*(c*r + Ur) + z*(c*z + Uz))/(r**2 + z**2)
claim = c + (3*t - 1 + b*u*t*(5*t - 3))/(2*(1 + u)**(p + 1))
diff = sp.simplify((speed - claim.subs({u: r**2 + z**2, t: z**2/(r**2 + z**2)})))
res['R_formula_ok'] = diff == 0
random.seed(1); worst = 1e9
for _ in range(20000):
    cv = random.uniform(0.5001, 0.9999); pv = 1/(2*cv); bv = random.uniform(0, 3)
    uv = 10**random.uniform(-4, 4); tv = random.uniform(0, 1)
    val = cv + (3*tv - 1 + bv*uv*tv*(5*tv - 3))/(2*(1 + uv)**(pv + 1)) - (cv - 0.5)
    worst = min(worst, val)
res['R_min_speed_minus_(c-1/2)_sampled'] = worst
# (C)
phi = z*(1 + b*z**2)/(2*(1 + a*s + z**2)**(p + 1))
axis = sp.simplify(-(8*sp.diff(phi, s) + sp.diff(phi, z, 2)).subs(s, 0))
# large-z expansion: substitute z = 1/Z, factor z^(-1-2p)
ser = sp.simplify(axis.subs(z, 1/Z)*Z**(-1 - 2*p))
ser = sp.series(sp.simplify(ser), Z, 0, 3).removeO()
C0 = sp.simplify(ser.coeff(Z, 0)); C1 = sp.simplify(ser.coeff(Z, 2))
C0c = b/2*(8*a*(p + 1) - 2*p*(2*p - 1))
C1c = 4*a*(p + 1)*(1 - b*(p + 2)) - (p + 1)*(2*p + 1)*(1 - b*(p + 1))
res['C0_ok'] = sp.simplify(C0 - C0c) == 0
res['C1_ok'] = sp.simplify(C1 - C1c) == 0
res['C_Z1_coeff_zero'] = sp.simplify(ser.coeff(Z, 1)) == 0
# (A)
A = p*(2*p - 1)/(4*(p + 1))
res['A_closed_form_ok'] = sp.simplify(A.subs(p, 1/(2*c)) - (1 - c)/(4*c*(1 + 2*c))) == 0
res['A_values'] = {f'{cv:.2f}': float(A.subs(p, 1/(2*sp.Rational(int(round(cv*100)), 100)))) for cv in (0.62, 0.66, 0.70, 0.74, 0.78, 0.82, 0.86)}
res['A_at_3/4'] = str(sp.nsimplify(A.subs(p, sp.Rational(2, 3))))
d = sp.symbols('d', positive=True); delta = 1 + c
# K^2 = delta^2 (4 a (p + 1)/(3 d) - 1) > 0  <=>  a > 3d/(4(p + 1)); with a < A(p): d < p(2p - 1)/3
res['joint_region_upper_d'] = str(sp.simplify(sp.solve(sp.Eq(3*d/(4*(p + 1)), A), d)[0]))
res['seconds'] = round(time.time() - t0, 1)
json.dump(res, open('checks/t1scal_check_output.json', 'w'), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
