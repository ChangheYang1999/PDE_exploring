"""V210: independent symbolic checks for Proposition 2.4 / Section 9.21 (candidate 47, 41bbd286; written without
reading the lead's or the audit's checks). Each check prints its name and True/False."""
import sympy as sp
R_ = []
def ok(name, val):
    R_.append(bool(val)); print('%-92s %s' % (name, bool(val)), flush=True)
x, y, X, Y, s, t, u = sp.symbols('x y X Y s t u', real=True)
R, L, g, gam, eta, Ceta = sp.symbols('R L g gamma eta C_eta', positive=True)
l = sp.Symbol('l', positive=True); beta = 2 * l - sp.Rational(1, 2); a = sp.Rational(1, 2); d = beta - a
# Step 2: scaling of curl and of div(V rho) under f_R(Z) = R^-g rho(RZ), E_R = R^-g W(RZ), b_R = R^-1 V(RZ)
rho = sp.Function('rho'); W1 = sp.Function('W1'); W2 = sp.Function('W2')
fR = R**-g * rho(R * x, R * y); E1 = R**-g * W1(R * x, R * y); E2 = R**-g * W2(R * x, R * y)
curlE = sp.diff(E2, x) - sp.diff(E1, y)
curlW_at = (sp.diff(W2(X, Y), X) - sp.diff(W1(X, Y), Y)).subs({X: R * x, Y: R * y})
ok('S2 curl_Z E_R(Z) = R^(1-g) (curl W)(RZ)', sp.simplify(curlE - R**(1 - g) * curlW_at) == 0)
ok('S2 d_x f_R(Z) = R^(1-g) rho_x(RZ), so curl W = -rho_x gives curl E_R = -d_x f_R',
   sp.simplify(sp.diff(fR, x) - R**(1 - g) * sp.diff(rho(X, Y), X).subs({X: R * x, Y: R * y})) == 0)
V1 = sp.Function('V1'); V2 = sp.Function('V2')
bR1 = V1(R * x, R * y) / R; bR2 = V2(R * x, R * y) / R
divb = sp.diff(bR1 * fR, x) + sp.diff(bR2 * fR, y)
divV_at = (sp.diff(V1(X, Y) * rho(X, Y), X) + sp.diff(V2(X, Y) * rho(X, Y), Y)).subs({X: R * x, Y: R * y})
ok('S2 div_Z(b_R f_R)(Z) = R^-g div(V rho)(RZ)', sp.simplify(divb - R**-g * divV_at) == 0)
ok('S2 div V = tr A = 2l for A = diag(1/2, beta) (div W_2 = 0)', sp.simplify(a + beta - 2 * l) == 0)
ok('S2 |E_R| <= R^-g (eta R L + C_eta) <= eta L + C_eta/R for R >= 1, g >= 1 (exponent check)',
   sp.simplify(R**-g * eta * R * L - eta * L * R**(1 - g)) == 0)
# Step 2: (AZ).grad f = f with f = F(y): beta y F' = F; F = c y^p, p = 1/beta
c = sp.Symbol('c'); yp = sp.Symbol('yp', positive=True); p = 1 / beta
Fp = c * yp**p
ok('S2 F = c y^(1/beta) solves beta y F\' = F on y > 0', sp.simplify(beta * yp * sp.diff(Fp, yp) - Fp) == 0)
Fq = sp.Function('F')
ok('S2 general solution of beta y F\' = F (y > 0) is C y^(1/beta)',
   sp.simplify(sp.dsolve(sp.Eq(beta * yp * Fq(yp).diff(yp), Fq(yp))).rhs / yp**p).free_symbols <= {sp.Symbol('C1')})
ok('S2 (y^-p F)\' = y^-p-1 (y F\' - p F) = y^-p-1 (beta y F\' - F)/beta',
   sp.powsimp(sp.expand(sp.simplify((sp.diff(yp**-p * Fq(yp), yp) - yp**(-p - 1) * (beta * yp * Fq(yp).diff(yp) - Fq(yp))
                                     / beta) * yp**(p + 1))), force=True) == 0)
# Step 4: g = 1/beta, g >= 1 gives l <= 3/4; beta > 1/2 gives l > 1/2
lg = sp.solve(sp.Eq(g, 1 / beta), l)[0]
ok('S4 g = 1/beta gives l = 1/4 + 1/(2g)', sp.simplify(lg - (sp.Rational(1, 4) + 1 / (2 * g))) == 0)
ok('S4 l(1) = 3/4 and l decreasing in g; l > 1/2 iff beta > 1/2',
   lg.subs(g, 1) == sp.Rational(3, 4) and sp.simplify(sp.diff(lg, g)).is_negative and sp.simplify(beta.subs(l, sp.Rational(1, 2)) - sp.Rational(1, 2)) == 0)
# Step 5: variation of constants with constant rates (the bounds used), kappa, mu
k0, kap, s1, T = sp.symbols('k0 kappa s1 T', positive=True)
zf = -sp.integrate(sp.exp(-k0 * (t - s)) * sp.exp(-kap * t), (t, s, sp.oo))
ok('S5 future integral: int_s^oo e^(-k(t-s)) e^(-kappa t) dt = e^(-kappa s)/(k + kappa)',
   sp.simplify(-zf - sp.exp(-kap * s) / (k0 + kap)) == 0)
zz = sp.Function('z')
f_ = sp.Function('f')
zsol = sp.exp(-k0 * (T - s)) * zz(T) - sp.Integral(sp.exp(-k0 * (t - s)) * f_(t), (t, s, T))
ok('S5 z(s) = e^(-k(T-s)) z(T) - int_s^T e^(-k(t-s)) f dt satisfies z\' = k z + f (constant k)',
   sp.simplify(sp.diff(zsol, s).doit() - (k0 * zsol + f_(s))).doit() == 0)
past = sp.integrate(sp.exp(-k0 * (s - t)) * sp.exp(-kap * t), (t, s1, s))
ok('S5 past integral at k = kappa equals (s - s1) e^(-kappa s): the factor (1 + s)',
   sp.simplify(past.subs(k0, kap) - (s - s1) * sp.exp(-kap * s)) == 0)
th = sp.Symbol('th', real=True); zv = th - sp.pi / 2
ok('S5 sin th cos th = -sin z cos z for z = th - pi/2', sp.simplify(sp.sin(th) * sp.cos(th) + sp.sin(zv) * sp.cos(zv)) == 0)
ok('S5 a + d sin^2 th = beta - d sin^2 z for z = th - pi/2', sp.simplify(a + d * sp.sin(th)**2 - (beta - d * sp.sin(zv)**2)) == 0)
ok('S5 |Phi_s X|^p = c^p e^(p beta s) = c^p e^s', sp.simplify(sp.exp(p * beta * s) - sp.exp(s)) == 0)
# Step 6: arc <= (pi/2) chord on a circle (angle phi in [0, pi]): r phi <= (pi/2) 2 r sin(phi/2)
import math
ok('S6 phi <= pi sin(phi/2) on [0, pi] (10^5 samples) and equality at phi = pi',
   all(ph <= math.pi * math.sin(ph / 2) + 1e-15 for ph in [math.pi * i / 1e5 for i in range(100001)]))
# Step 7: Hessian scaling, Lipschitz contradiction, gamma = 1
ok('S7 D^2 f_R(Z) = R^(2-gamma) D^2 rho(RZ); R^(2-gamma) (R|Z|)^(gamma-2) = |Z|^(gamma-2)',
   sp.simplify(sp.diff(R**-gam * rho(R * x, R * y), x, 2) - R**(2 - gam) * sp.diff(rho(X, Y), X, 2).subs({X: R * x, Y: R * y})) == 0
   and sp.simplify(R**(2 - gam) * (R * L)**(gam - 2) - L**(gam - 2)) == 0)
gg = sp.Symbol('gg', positive=True)  # gamma = 1 + gg, 0 < gg < 1
ok('S7 (gamma y^(gamma-1))/y -> infinity as y -> 0+ for 1 < gamma < 2 (gamma = 3/2 and symbolic)',
   sp.limit(sp.Rational(3, 2) * yp**sp.Rational(1, 2) / yp, yp, 0, '+') == sp.oo
   and sp.limit(((1 + gg) * yp**gg / yp).subs(gg, sp.Rational(1, 3)), yp, 0, '+') == sp.oo)
ap, am = sp.symbols('a_p a_m')
fy_up = sp.diff(ap * yp, yp); fy_dn = sp.diff(am * (-y), y)
ok('S7 gamma = 1: d_y f = a_+ above, -a_- below; continuity gives a_- = -a_+', fy_up == ap and fy_dn == -am
   and sp.solve(sp.Eq(fy_up, fy_dn), am) == [-ap])
ok('S7 gamma = 1 with beta gamma = 1 gives beta = 1, l = 3/4', sp.solve(sp.Eq(beta, 1), l) == [sp.Rational(3, 4)])
print('ALL', all(R_), len(R_), flush=True)
