"""V195: independent symbolic checks of referee result 41 (layered ansatz rho = sum f_j(y) x^j,
psi = sum q_j(y) x^j, deg_x rho <= 3, any M; written without reading the referee check script). Equations: -Lap psi = rho_x,
V.grad rho = rho, V = (l x - psi_y, l y + psi_x), beta = 2l - 1/2. Each check prints its name and True/False."""
import sympy as sp
x, y, z, l = sp.symbols('x y z l')
beta = 2 * l - sp.Rational(1, 2)
R = []
def ok(name, val):
    R.append(bool(val)); print('%-78s %s' % (name, bool(val)), flush=True)
def lap(f, X=x, Y=y):
    return sp.diff(f, X, 2) + sp.diff(f, Y, 2)
def transport(rho, psi):
    return sp.expand((l * x - sp.diff(psi, y)) * sp.diff(rho, x) + (l * y + sp.diff(psi, x)) * sp.diff(rho, y) - rho)

# Step 1: general coefficient equations for N = 3, M = 5 (functions of y)
Nn, Mm = 3, 5
fj = [sp.Function('f%d' % j)(y) for j in range(Nn + 1)]
qj = [sp.Function('q%d' % j)(y) for j in range(Mm + 1)]
rho = sum(fj[j] * x**j for j in range(Nn + 1)); psi = sum(qj[j] * x**j for j in range(Mm + 1))
T = sp.Poly(transport(rho, psi), x)
F_ = lambda j: fj[j] if 0 <= j <= Nn else 0
Q_ = lambda j: qj[j] if 0 <= j <= Mm else 0
good = True
for d in range(0, Nn + Mm):
    form = (l * d - 1) * F_(d) + l * y * sp.diff(F_(d), y) + sum(j * Q_(j) * sp.diff(F_(d + 1 - j), y) - (d + 1 - j) * sp.diff(Q_(j), y) * F_(d + 1 - j)
                                                               for j in range(0, d + 2))
    good &= sp.expand(T.coeff_monomial(x**d) - form) == 0
ok('S1 transport x^d coefficient: (ld-1)f_d + l y f_d\' + sum_(j+k=d+1)(j q_j f_k\' - k q_j\' f_k)', good)
P = sp.Poly(sp.expand(-lap(psi) - sp.diff(rho, x)), x)
good = all(sp.expand(P.coeff_monomial(x**j) + (sp.diff(Q_(j), y, 2) + (j + 2) * (j + 1) * Q_(j + 2) + (j + 1) * F_(j + 1))) == 0 for j in range(0, Mm + 1))
ok('S1 Poisson: q_j\'\' + (j+2)(j+1) q_(j+2) = -(j+1) f_(j+1)', good)
# N <= 3, M <= 3 in the a, f, g, k / n, m, s, t notation
a, f, g, k, n, m, s, t = [sp.Function(nm)(y) for nm in 'a f g k n m s t'.split()]
b = l * y + s; u = sp.diff(t, y); D = lambda e: sp.diff(e, y)
rho3 = a * x**3 + f * x**2 + g * x + k; psi3 = n * x**3 + m * x**2 + s * x + t
T3 = sp.Poly(transport(rho3, psi3), x); P3 = sp.Poly(sp.expand(-lap(psi3) - sp.diff(rho3, x)), x)
eqT = {5: 3 * n * D(a) - 3 * a * D(n),
       4: 3 * n * D(f) - 2 * f * D(n) + 2 * m * D(a) - 3 * a * D(m),
       3: 3 * n * D(g) - D(n) * g + 2 * m * D(f) - 2 * f * D(m) + b * D(a) + (3 * (2 * l - D(b)) - 1) * a,
       2: 3 * n * D(k) + 2 * m * D(g) - D(m) * g + b * D(f) + 2 * (beta - D(b)) * f - 3 * a * u,
       1: 2 * m * D(k) + b * D(g) + (2 * l - D(b) - 1) * g - 2 * f * u,
       0: b * D(k) - g * u - k}
ok('S1 the six transport equations (x^5 .. x^0)', all(sp.expand(T3.coeff_monomial(x**d) - eqT[d]) == 0 for d in range(6)))
eqP = {3: D(D(n)), 2: D(D(m)) + 3 * a, 1: D(D(b)) + 2 * f + 6 * n, 0: D(u) + g + 2 * m}
ok('S1 Poisson: n\'\' = 0, m\'\' = -3a, b\'\' = -2f - 6n, u\' = -g - 2m', all(sp.expand(P3.coeff_monomial(x**j) + eqP[j]) == 0 for j in range(4)))
# jet consequences at 0: generic Taylor data consistent with Step 1 (f(0) = 1, g = O(y^2), k = O(y^3), b(0) = u(0) = 0)
cf = sp.symbols('a0 a1 n0_ n1 m0 m1 m2 f1 f2 g2 g3 k3 k4 b1 b2 b3 u1 u2 u3')
a0, a1, n0_, n1, m0, m1, m2, f1, f2, g2, g3, k3, k4, b1, b2, b3, u1, u2, u3 = cf
tay = {a: a0 + a1 * y, n: n0_ + n1 * y, m: m0 + m1 * y + m2 * y**2, f: 1 + f1 * y + f2 * y**2, g: g2 * y**2 + g3 * y**3,
       k: k3 * y**3 + k4 * y**4, s: b1 * y + b2 * y**2 + b3 * y**3 - l * y, t: u1 * y**2 / 2 + u2 * y**3 / 3 + u3 * y**4 / 4}
ev = lambda e: sp.expand(e.subs(tay).doit())
x2at0 = ev(eqT[2]).subs(y, 0)
ok('S1 x^2 equation at 0 is 2(beta - b\'(0)) for generic data', sp.expand(x2at0 - 2 * (beta - b1)) == 0)
x1 = ev(eqT[1]); x1_lim = sp.expand(sp.cancel(x1.subs(b1, beta) / y)).subs(y, 0)
ok('S1 (x^1 equation)/y at 0, with b\'(0) = beta, is -2u\'(0) (all other terms vanish)', sp.expand(x1_lim + 2 * u1) == 0)
p0_at0 = ev(eqP[0]).subs(y, 0)
ok('S1 u\' = -g - 2m at 0 with u\'(0) = 0 gives m(0) = 0', sp.solve(p0_at0.subs(u1, 0), m0) == [0])
x3at0 = ev(eqT[3]).subs({y: 0, m0: 0, b1: beta})
ok('S1 x^3 equation at 0 (m(0) = 0, b\'(0) = beta) gives m\'(0) = a(0)/4 for generic n, a', sp.solve(x3at0, m1) == [a0 / 4])
x0 = ev(eqT[0])
ok('S1 constant equation b k\' - g u - k = O(y^3) under the jet', all(sp.expand(x0).coeff(y, j) == 0 for j in range(3)))

# Step 2: exponent and Euler identities, harmonic H
Ns, Ms, js = sp.symbols('N M j', positive=True)
dd = Ns + Ns / Ms
ok('S2 d - j - j/M = (N-j)(1+1/M)', sp.simplify(dd - js - js / Ms - (Ns - js) * (1 + 1 / Ms)) == 0)
ok('S2 d < M for M = N+1 (N = 2..30) and (M+1)/d = M/N', all(sp.Rational(N_) + sp.Rational(N_, N_ + 1 + e) < N_ + 1 + e for N_ in range(2, 31) for e in range(0, 5))
   and sp.simplify((Ms + 1) / dd - Ms / Ns) == 0)
pp = sp.Symbol('p')
good = True
for M_ in range(2, 9):
    H = sp.expand(pp * sp.im(sp.expand((x + sp.I * z)**(M_ + 1))) / (M_ + 1))
    H = sp.expand(sp.im(sp.expand((x + sp.I * z)**(M_ + 1)).subs({x: sp.Symbol('xr', real=True), z: sp.Symbol('zr', real=True)}))
                  .subs({sp.Symbol('xr', real=True): x, sp.Symbol('zr', real=True): z}) * pp / (M_ + 1))
    PH = sp.Poly(H, x, z)
    good &= sp.expand(lap(H, x, z)) == 0 and PH.coeff_monomial(x**M_ * z) == pp and PH.coeff_monomial(x**(M_ + 1)) == 0
    h1 = sp.Poly(H.subs(z, 1) / pp, x)
    good &= h1.degree() == M_ and len(sp.real_roots(h1)) == M_ and sp.degree(sp.gcd(h1, h1.diff(x))) == 0
ok('S2 H = p Im (x+iz)^(M+1)/(M+1): harmonic, x^M z coeff p, H(x,1) has M simple real roots (M=2..8)', good)
# Euler identity for homogeneous H (degree M+1) and R = z^d P(x/z)
P_ = sp.Function('Pf'); dsym = sp.Symbol('d', positive=True); M1 = sp.Symbol('Mp', positive=True)
Hf = sp.Function('Hh')
zz = sp.Symbol('zz', positive=True)
Rh = zz**dsym * P_(x / zz); Hh = zz**(M1) * Hf(x / zz)
lhs = M1 * Hh * sp.diff(Rh, x) - dsym * Rh * sp.diff(Hh, x)
br_ = sp.diff(Hh, x) * sp.diff(Rh, zz) - sp.diff(Hh, zz) * sp.diff(Rh, x)
ok('S2 Euler: deg(H) H R_x - d R H_x = -z {H,R}, {F,G} = F_x G_z - F_z G_x', sp.simplify(lhs + zz * br_) == 0)
# multiplicity: at a simple root of H, P of multiplicity k gives (Mk - N) * leading = 0
kk = sp.Symbol('k', positive=True, integer=True); xi = sp.Symbol('xi')
c1, ck = sp.symbols('c1 ck')
expr = Ms * (c1 * xi) * sp.diff(ck * xi**kk, xi) - Ns * (ck * xi**kk) * c1
ok('S2 multiplicity comparison: M H P\' - N P H_x leading coefficient c1 ck (Mk - N)', sp.simplify(expr - c1 * ck * (Ms * kk - Ns) * xi**kk) == 0)

# Step 3: degree count of the products in the f_j equation
ok('S3 degree bound: (M-i) + (N-k-1) = N-j-1 when i+k = M+j', sp.expand((Ms - sp.Symbol('i')) + (Ns - (Ms + js - sp.Symbol('i')) - 1) - (Ns - js - 1)) == 0)

# Step 4: polynomial cubic: 1 + 6 t^2 (2 beta - 1/2) > 0 for beta > 3/2 (the same identities as referee result 40 Step 6)
tt = sp.Symbol('t', real=True)
bb = sp.Symbol('bb', positive=True)  # bb = beta - 3/2 > 0
ok('S4 1 + 6 t^2 (2beta - 1/2) > 0 for beta > 3/2 (symbolic)', sp.expand(1 + 6 * tt**2 * (2 * (bb + sp.Rational(3, 2)) - sp.Rational(1, 2))).is_positive)
# S4 cubic system: rho_3 = mu (x+ty)^3, psi_2 = (l-1/2)xy, general psi_3; check the three displayed equations from the cubic coefficients
mu, A3, B3, C3, D3 = sp.symbols('mu A3 B3 C3 D3')
r3 = mu * (x + tt * y)**3; p3 = A3 * x**3 + B3 * x**2 * y + C3 * x * y**2 + D3 * y**3; p2 = (l - sp.Rational(1, 2)) * x * y
cub = sp.Poly(sp.expand(l * (x * sp.diff(r3, x) + y * sp.diff(r3, y)) - r3 + (sp.diff(p2, x) * sp.diff(r3, y) - sp.diff(p2, y) * sp.diff(r3, x))
                         + (sp.diff(p3, x) * sp.diff(x**2, y) - sp.diff(p3, y) * sp.diff(x**2, x))), x, y)
pois1 = sp.Poly(sp.expand(-lap(p3) - 2 * x), x, y)
ok('S4 [y](Poisson) = -(2B3 + 6D3), [x^3] = mu/2 - 2B3, [xy^2] = 3mu t^2(2beta-1/2) - 6D3',
   sp.expand(pois1.coeff_monomial(y) + 2 * B3 + 6 * D3) == 0 and sp.expand(cub.coeff_monomial(x**3) - (mu / 2 - 2 * B3)) == 0
   and sp.expand(cub.coeff_monomial(x * y**2) - (3 * mu * tt**2 * (2 * beta - sp.Rational(1, 2)) - 6 * D3)) == 0)

# Step 5
mm = sp.Function('mm')(y)
aa = -sp.diff(mm, y, 2) / 3
ok('S5 2m a\' - 3a m\' with a = -m\'\'/3 is -(2m m\'\'\' - 3m\'m\'\')/3', sp.expand(2 * mm * sp.diff(aa, y) - 3 * aa * sp.diff(mm, y) + (2 * mm * sp.diff(mm, y, 3) - 3 * sp.diff(mm, y) * sp.diff(mm, y, 2)) / 3) == 0)
ok('S5 (4m m\'\' - 5m\'^2)\' = 2(2m m\'\'\' - 3m\'m\'\')', sp.expand(sp.diff(4 * mm * sp.diff(mm, y, 2) - 5 * sp.diff(mm, y)**2, y) - 2 * (2 * mm * sp.diff(mm, y, 3) - 3 * sp.diff(mm, y) * sp.diff(mm, y, 2))) == 0)
mp = sp.Function('mp', positive=True)(y)
ok('S5 (m^(-1/4))\'\' = m^(-9/4)(5m\'^2 - 4m m\'\')/16 (m > 0)', sp.simplify(sp.diff(mp**sp.Rational(-1, 4), y, 2) - mp**sp.Rational(-9, 4) * (5 * sp.diff(mp, y)**2 - 4 * mp * sp.diff(mp, y, 2)) / 16) == 0)

# Step 6: substitutions g = C b + r, k' = v + C u, f = C m + h, a = C n
A, n0, cc, C = sp.symbols('A n0 c C')
nf, hf, rf, vf, bf, uf, mf = [sp.Function(nm)(y) for nm in ('nf', 'hf', 'rf', 'vf', 'bf', 'uf', 'mf')]
sub = {a: C * nf, f: C * mf + hf, g: C * bf + rf, n: nf, m: mf}
def S(e):
    e = e.subs({s: bf - l * y}).doit()
    e = e.subs({sp.diff(t, y): uf, sp.diff(t, y, 2): sp.diff(uf, y)}).doit()
    e = e.subs(sub).doit()
    e = e.subs({sp.diff(k, y): vf + C * uf}).doit()
    return sp.expand(e)
e4 = S(eqT[4]); e3 = S(eqT[3]); e2 = S(eqT[2]); e1 = S(eqT[1]); p1 = S(eqP[1]); p0 = S(eqP[0])
Dn = lambda e: sp.diff(e, y)
ok('S6 x^4 eq becomes 3n h\' - 2n\' h', sp.expand(e4 - (3 * nf * Dn(hf) - 2 * Dn(nf) * hf)) == 0)
ok('S6 b\'\' = -2Cm - 2h - 6n', sp.expand(p1 - (Dn(Dn(bf)) + 2 * C * mf + 2 * hf + 6 * nf)) == 0)
ok('S6 3n r\' - n\' r = 2h m\' - 2m h\' - (6l-1)C n', sp.expand(e3 - (3 * nf * Dn(rf) - Dn(nf) * rf - (2 * hf * Dn(mf) - 2 * mf * Dn(hf) - (6 * l - 1) * C * nf))) == 0)
ok('S6 u\' = -Cb - r - 2m', sp.expand(p0 - (Dn(uf) + C * bf + rf + 2 * mf)) == 0)
ok('S6 3n v = -b h\' + 2(b\'-beta)h - 2beta C m - 2m r\' + r m\'',
   sp.expand(e2 - (3 * nf * vf - (-bf * Dn(hf) + 2 * (Dn(bf) - beta) * hf - 2 * beta * C * mf - 2 * mf * Dn(rf) + rf * Dn(mf)))) == 0)
ok('S6 E = 2m v + b r\' + (2l-b\'-1) r + C(2l-1) b - 2h u',
   sp.expand(e1 - (2 * mf * vf + bf * Dn(rf) + (2 * l - Dn(bf) - 1) * rf + C * (2 * l - 1) * bf - 2 * hf * uf)) == 0)
# m from m'' = -3 A z, m(0) = 0, m'(0) = A/4
mz = A * (y / 4 - 3 * y**2 / 2 - cc * y**3 / 2)
ok('S6 m = A(y/4 - 3y^2/2 - c y^3/2): m\'\' = -3A(1+cy), m(0) = 0, m\'(0) = A/4',
   sp.expand(sp.diff(mz, y, 2) + 3 * A * (1 + cc * y)) == 0 and mz.subs(y, 0) == 0 and sp.diff(mz, y).subs(y, 0) == A / 4)

# Step 7: c = 0, exact polynomials
Cv = A / n0; m7 = mz.subs(cc, 0)
b7 = sp.integrate(sp.integrate(-2 * Cv * m7 - 2 - 6 * n0, (y, 0, y)), (y, 0, y)) + beta * y
r7 = sp.integrate((2 * sp.diff(m7, y) - (6 * l - 1) * Cv * n0) / (3 * n0), (y, 0, y))
u7 = sp.integrate(-Cv * b7 - r7 - 2 * m7, (y, 0, y))
v7 = (2 * (sp.diff(b7, y) - beta) - 2 * beta * Cv * m7 - 2 * m7 * sp.diff(r7, y) + r7 * sp.diff(m7, y)) / (3 * n0)
E7 = sp.expand(2 * m7 * v7 + b7 * sp.diff(r7, y) + (2 * l - sp.diff(b7, y) - 1) * r7 + Cv * (2 * l - 1) * b7 - 2 * u7)
lead = lambda e, var: sp.Poly(sp.expand(e), var).LC() * var**sp.Poly(sp.expand(e), var).degree()
ok('S7 leading terms m, b, r, u, v (c = 0)',
   sp.simplify(lead(m7, y) + 3 * A * y**2 / 2) == 0 and sp.simplify(lead(b7, y) - A**2 * y**4 / (4 * n0)) == 0
   and sp.simplify(lead(r7, y) + A * y**2 / n0) == 0 and sp.simplify(lead(u7, y) + A**3 * y**5 / (20 * n0**2)) == 0
   and sp.simplify(lead(v7, y) + A**2 * y**3 / (3 * n0**2)) == 0)
ok('S7 deg E = 5 with [y^5] E = 8A^3/(5 n0^2)', sp.Poly(E7, y).degree() == 5 and sp.simplify(sp.Poly(E7, y).LC() - 8 * A**3 / (5 * n0**2)) == 0)
# check the setup reproduces the equations with h = 1, n = n0: residuals of Step 6 equations vanish
ok('S7 r, u, v satisfy their Step 6 equations (c = 0) and r(0) = u(0) = 0, b(0) = 0, b\'(0) = beta',
   sp.expand(3 * n0 * sp.diff(r7, y) - (2 * sp.diff(m7, y) - (6 * l - 1) * Cv * n0)) == 0 and r7.subs(y, 0) == 0 and u7.subs(y, 0) == 0
   and b7.subs(y, 0) == 0 and sp.diff(b7, y).subs(y, 0) == beta and sp.expand(sp.diff(b7, y, 2) + 2 * Cv * m7 + 2 + 6 * n0) == 0)

# Step 8: c != 0, exact power sums in z = 1 + c y (z > 0); d/dy = c d/dz
zp = sp.Symbol('zp', positive=True); w = sp.Symbol('w', positive=True)
yz = (zp - 1) / cc
m8 = sp.expand(mz.subs(y, yz)); h8 = zp**sp.Rational(2, 3); n8 = n0 * zp; Cv = A / n0
dY = lambda e: cc * sp.diff(e, zp)
rhs_b = sp.expand((-2 * Cv * m8 - 2 * h8 - 6 * n8) / cc**2)
b8 = sp.integrate(sp.integrate(rhs_b.subs(zp, w), (w, 1, zp)).subs(zp, w), (w, 1, zp)) + beta / cc * (zp - 1)
b8 = sp.expand(b8)
rhsr = sp.expand(2 * h8 * dY(m8) - 2 * m8 * dY(h8) - (6 * l - 1) * Cv * n8)
# n0 c (3 z r_z - r) = rhsr  ->  (r z^(-1/3))_z = rhsr z^(-4/3) / (3 n0 c)
r8 = sp.expand(zp**sp.Rational(1, 3) * sp.integrate(sp.expand(rhsr * zp**sp.Rational(-4, 3) / (3 * n0 * cc)).subs(zp, w), (w, 1, zp)))
u8 = sp.expand(sp.integrate(sp.expand((-Cv * b8 - r8 - 2 * m8) / cc).subs(zp, w), (w, 1, zp)))
v8 = sp.expand((-b8 * dY(h8) + 2 * (dY(b8) - beta) * h8 - 2 * beta * Cv * m8 - 2 * m8 * dY(r8) + r8 * dY(m8)) / (3 * n8))
E8 = sp.expand(2 * m8 * v8 + b8 * dY(r8) + (2 * l - dY(b8) - 1) * r8 + Cv * (2 * l - 1) * b8 - 2 * h8 * u8)
ok('S8 no logarithms in b, r, u, v, E', not any(e.has(sp.log) for e in (b8, r8, u8, v8, E8)))
def lead_pow(e):
    terms = sp.Add.make_args(sp.expand(e)); d = {}
    for tm in terms:
        c_, ex = tm.as_coeff_exponent(zp)
        d[ex] = d.get(ex, 0) + c_
    d = {ex: sp.simplify(v_) for ex, v_ in d.items()}; d = {ex: v_ for ex, v_ in d.items() if v_ != 0}
    e_max = max(d); return e_max, d[e_max]
lm = [lead_pow(e) for e in (m8, b8, r8, u8, v8)]
want = [(3, -A / (2 * cc**2)), (5, A**2 / (20 * n0 * cc**4)), (sp.Rational(8, 3), -A / (3 * n0 * cc**2)),
        (6, -A**3 / (120 * n0**2 * cc**5)), (sp.Rational(11, 3), 7 * A**2 / (270 * n0**2 * cc**3))]
print('   S8 leading (exponent, coefficient):', lm, flush=True)
ok('S8 leading terms m, b, r, u, v (c != 0)', all(lm[i][0] == want[i][0] and sp.simplify(lm[i][1] - want[i][1]) == 0 for i in range(5)))
eE = lead_pow(E8); print('   S8 leading term of E:', eE, flush=True)
ok('S8 leading term of E: exponent 20/3, coefficient 4A^3/(135 n0^2 c^5)', eE[0] == sp.Rational(20, 3) and sp.simplify(eE[1] - 4 * A**3 / (135 * n0**2 * cc**5)) == 0)
ok('S8 r, u, b satisfy their equations and initial values at z = 1',
   sp.simplify(n0 * cc * (3 * zp * sp.diff(r8, zp) - r8) - rhsr) == 0 and r8.subs(zp, 1) == 0 and u8.subs(zp, 1) == 0
   and sp.simplify(b8.subs(zp, 1)) == 0 and sp.simplify(dY(b8).subs(zp, 1) - beta) == 0 and sp.simplify(cc**2 * sp.diff(b8, zp, 2) - (-2 * Cv * m8 - 2 * h8 - 6 * n8)) == 0)
ok('S8 h = z^(2/3) solves 3n h\' - 2n\' h = 0 with h(0) = 1', sp.simplify(3 * n8 * dY(h8) - 2 * n0 * cc * h8) == 0 and h8.subs(zp, 1) == 1)

# Step 9: the quadratic case, explicit solution (a)
hy = 1 + y / beta; fa = hy**-4; ba = beta**2 * (hy - hy**-2) / 3; pa = sp.diff(ba, y) - beta
ok('S9 b = beta(beta+y)/3 - beta^4/(3(beta+y)^2) equals beta^2(h - h^-2)/3', sp.simplify(ba - (beta * (beta + y) / 3 - beta**4 / (3 * (beta + y)**2))) == 0)
ok('S9 (a): b\'\' = -2f, b f\' = 2(b\'-beta) f, b(0) = 0, b\'(0) = beta, f(0) = 1',
   sp.simplify(sp.diff(ba, y, 2) + 2 * fa) == 0 and sp.simplify(ba * sp.diff(fa, y) - 2 * (sp.diff(ba, y) - beta) * fa) == 0
   and sp.simplify(ba.subs(y, 0)) == 0 and sp.simplify(sp.diff(ba, y).subs(y, 0) - beta) == 0 and fa.subs(y, 0) == 1)
ok('S9 b p\'\' = 2 p p\', b p\' = beta p + 3p^2/2, f = (1+3p/(2beta))^(4/3), h = (1+3p/(2beta))^(-1/3)',
   sp.simplify(ba * sp.diff(pa, y, 2) - 2 * pa * sp.diff(pa, y)) == 0 and sp.simplify(ba * sp.diff(pa, y) - beta * pa - 3 * pa**2 / 2) == 0
   and sp.simplify(1 + 3 * pa / (2 * beta) - hy**-3) == 0)
bq, pq, fq = [sp.Function(nm)(y) for nm in ('bq', 'pq', 'fq')]
ok('S9 derivative of b p\' - beta p - 3p^2/2 vanishes given b\' = p + beta, b p\'\' = 2pp\'',
   sp.expand((sp.diff(bq * sp.diff(pq, y) - beta * pq - 3 * pq**2 / 2, y)).subs(sp.diff(bq, y), pq + beta).subs(sp.diff(pq, y, 2), 2 * pq * sp.diff(pq, y) / bq)) == 0)
ok('S9 f\' = -4f^2/(beta+3p/2) from b p\' = p(beta+3p/2), p\' = -2f, b f\' = 2pf (along (a))',
   sp.simplify(sp.diff(fa, y) + 4 * fa**2 / (beta + 3 * pa / 2)) == 0)
ok('S9 b vanishes on (-beta, inf) only at 0: b = beta^2 h^-2 (h^3 - 1)/3', sp.simplify(ba - beta**2 * hy**-2 * (hy**3 - 1) / 3) == 0)

# Step 10: residue of (1 - 2l + b')/b at 0
res = sp.series((1 - 2 * l + sp.diff(ba, y)) / ba, y, 0, 1).removeO()
Bt = sp.Symbol('Bt', positive=True)
baB = ba.subs(l, (Bt + sp.Rational(1, 2)) / 2); 
q10 = sp.cancel(((1 - 2 * l + sp.diff(ba, y)) / ba).subs(l, (Bt + sp.Rational(1, 2)) / 2) - 1 / (2 * Bt * y))
ok('S10 (1-2l+b\')/b - 1/(2beta y) is regular at y = 0 (symbolic beta)', sp.cancel(q10 * y).subs(y, 0) == 0 and sp.denom(sp.cancel(q10)).subs(y, 0) != 0)
q11 = sp.cancel(1 / baB - 1 / (Bt * y))
ok('S10 1/b - 1/(beta y) is regular at y = 0 (symbolic beta)', sp.denom(q11).subs(y, 0) != 0)
ok('S10 kappa < 1 and 1/beta < 1 for l > 1', (1 / (2 * beta)).subs(l, 1) < 1 and (1 / beta).subs(l, 1) < 1)

# Step 11: the two solutions
for name, rr, ps_ in [('(a)', x**2 * fa, x * (ba - l * y) + sp.Symbol('Q')), ('(b)', x**2, -x**3 / 3 + (l - sp.Rational(1, 2)) * x * y + sp.Symbol('Q'))]:
    Vv = (l * x - sp.diff(ps_, y), l * y + sp.diff(ps_, x))
    ok('S11 %s: -Lap psi = rho_x, V.grad rho = rho, W(0) = 0, jet x^2' % name,
       sp.simplify(-lap(ps_) - sp.diff(rr, x)) == 0 and sp.simplify(Vv[0] * sp.diff(rr, x) + Vv[1] * sp.diff(rr, y) - rr) == 0
       and sp.simplify(sp.diff(ps_, y).subs({x: 0, y: 0})) == 0 and sp.simplify(sp.diff(ps_, x).subs({x: 0, y: 0})) == 0
       and sp.simplify(sp.diff(rr, x, 2).subs({x: 0, y: 0}) - 2) == 0 and sp.simplify(rr.subs(x, 0)) == 0)
print('ALL', all(R), len(R), flush=True)
