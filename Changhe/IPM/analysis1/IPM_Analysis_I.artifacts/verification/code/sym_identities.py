"""Verifier (ipmA-ver): symbolic re-derivation of the exact identities quoted in PROMPT.md.

Each check prints PASS/FAIL. Pure sympy, exact arithmetic. No reuse of team code.
"""
import sympy as sp

x, y, r, s, th, t = sp.symbols('x y r s theta t', real=True)
cl = sp.symbols('c_l', positive=True)
res = []


def check(name, expr):
    e = sp.simplify(expr)
    ok = (e == 0)
    res.append((name, ok))
    print(('PASS ' if ok else 'FAIL ') + name + ('' if ok else '   residual: %s' % e))


# ---------------------------------------------------------------- 1. Green formula
n = sp.symbols('n', positive=True, integer=True)
f = sp.Function('f')
nu = 2 * n
I1 = sp.Integral(s ** (nu + 1) * f(s), (s, 0, r))
I2 = sp.Integral(s ** (1 - nu) * f(s), (s, r, sp.oo))
psi_n = (r ** (-nu) * I1 + r ** nu * I2) / (4 * n)
lhs = -(sp.diff(psi_n, r, 2) + sp.diff(psi_n, r) / r - nu ** 2 * psi_n / r ** 2)
check('Green: -(psi_n\'\'+psi_n\'/r-4n^2 psi_n/r^2) = f_n', sp.simplify(lhs.doit() - f(r)))
# polar Laplacian of psi_n(r) sin(2 n theta) is the radial operator above (standard); check on monomial
a_ = sp.symbols('a')
P = r ** a_ * sp.sin(2 * n * th)
X_, Y_ = r * sp.cos(th), r * sp.sin(th)
lap_polar = sp.diff(P, r, 2) + sp.diff(P, r) / r + sp.diff(P, th, 2) / r ** 2
check('polar Laplacian of r^a sin(2n th) = (a^2-4n^2) r^(a-2) sin(2n th)',
      lap_polar - (a_ ** 2 - 4 * n ** 2) * r ** (a_ - 2) * sp.sin(2 * n * th))

# ---------------------------------------------------------------- 2. psi_xy(0) from mode 1
# near 0: psi ~ psi_1(r) sin(2 theta) = 2 psi_1(r)/r^2 * xy, psi_1(r)/r^2 -> (1/4) int_0^oo f_1(s)/s ds
# (the inner term r^-2 int_0^r s^3 f_1 / r^2 -> 0 if f_1 = O(s)); so psi_xy(0) = (1/2) int_0^oo f_1(s)/s ds
fl = sp.symbols('f1c')
# check with f_1(s) = s*exp(-s) (f_1 = O(s) at 0): psi_1 = ..., limit psi_1/r^2
f1 = s * sp.exp(-s)
psi1 = (r ** -2 * sp.integrate(s ** 3 * f1, (s, 0, r)) + r ** 2 * sp.integrate(f1 / s, (s, r, sp.oo))) / 4
lim = sp.limit(psi1 / r ** 2, r, 0)
check('psi_1/r^2 -> (1/4) int f_1/s ds (test f_1 = s e^-s)', lim - sp.Rational(1, 4) * sp.integrate(f1 / s, (s, 0, sp.oo)))

# ---------------------------------------------------------------- 3. Fourier symbols / kernels
xi1, xi2 = sp.symbols('xi1 xi2', real=True)
# conventions: f(x) = int fhat e^{i x.xi}; d_j -> i xi_j; -Lap -> |xi|^2
rhohat = sp.symbols('rhohat')
psihat = sp.I * xi1 * rhohat / (xi1 ** 2 + xi2 ** 2)
U1hat = -sp.I * xi2 * psihat
U2hat = sp.I * xi1 * psihat
check('U1 symbol = xi1 xi2/|xi|^2', U1hat / rhohat - xi1 * xi2 / (xi1 ** 2 + xi2 ** 2))
check('U2 symbol = -xi1^2/|xi|^2', U2hat / rhohat + xi1 ** 2 / (xi1 ** 2 + xi2 ** 2))
# kernel check: d_i d_j (1/2pi log|x|) = pv (1/2pi)(delta_ij |x|^2 - 2 x_i x_j)/|x|^4 + delta_ij/2 delta
G0 = sp.log(sp.sqrt(x ** 2 + y ** 2)) / (2 * sp.pi)
check('d_x d_y Gamma = -x y/(pi |x|^4) (= K_1 off origin)', sp.diff(G0, x, y) - (-x * y / (sp.pi * (x ** 2 + y ** 2) ** 2)))
check('-d_x d_x Gamma = (x^2-y^2)/(2 pi |x|^4) (= K_2 off origin)',
      -sp.diff(G0, x, 2) - (x ** 2 - y ** 2) / (2 * sp.pi * (x ** 2 + y ** 2) ** 2))
# hat(d_i d_j Gamma) = xi_i xi_j / |xi|^2 (since hat Gamma = -1/|xi|^2); U1 = d_x d_y Gamma * rho (no local term since
# angular mean of K_1 is 0 and delta_12=0); U2 = -d_xd_x Gamma*rho = pv K_2*rho - rho/2. mean of cos(2th) over circle 0:
check('angular mean of (cos^2-sin^2) is 0', sp.integrate(sp.cos(th) ** 2 - sp.sin(th) ** 2, (th, 0, 2 * sp.pi)))

# ---------------------------------------------------------------- 4. centre: normalization, DU(0), DV(0), M_Phi(0)
c = sp.symbols('c')
rho0 = x ** 2 * y
psi0 = c * x * y
U = sp.Matrix([-sp.diff(psi0, y), sp.diff(psi0, x)])
V = cl * sp.Matrix([x, y]) + U
eq = (V[0] * sp.diff(rho0, x) + V[1] * sp.diff(rho0, y) - rho0)
check('x^2 y order: (3c_l - c - 1) x^2 y', sp.expand(eq - (3 * cl - c - 1) * x ** 2 * y))
DU0 = sp.Matrix([[sp.diff(U[0], x), sp.diff(U[0], y)], [sp.diff(U[1], x), sp.diff(U[1], y)]]).subs(c, 3 * cl - 1)
check('DU(0) = diag(-(3c_l-1), 3c_l-1)', (DU0 - sp.diag(-(3 * cl - 1), 3 * cl - 1)).norm())
DV0 = DU0 + cl * sp.eye(2)
check('DV(0) = diag(1-2c_l, 4c_l-1)', (DV0 - sp.diag(1 - 2 * cl, 4 * cl - 1)).norm())
MPhi0 = (1 + 2 * cl) * sp.eye(2) + (DU0 + DU0.T) / 2
check('M_Phi(0) = diag(2-c_l, 5c_l)', (MPhi0 - sp.diag(2 - cl, 5 * cl)).norm())
clv = sp.Float('5.575362610641546', 30)
print('   numeric: DV(0) eigen', [sp.N(e.subs(cl, clv), 12) for e in (1 - 2 * cl, 4 * cl - 1)],
      ' M_Phi(0)', [sp.N(e.subs(cl, clv), 12) for e in (2 - cl, 5 * cl)], ' d(P)=2-2c_l', sp.N(2 - 2 * clv, 12))

# ---------------------------------------------------------------- 5. Phi-energy identity (IBP, pointwise divergence form)
# Claim: -(L0 h) Phi = grad Phi^T M grad Phi + div(J) for h=-Lap Phi, U[h]=(-Phi_xy, Phi_xx), div Ubar = 0.
# Verify pointwise: expression - quadratic form must be a divergence. Use generic polynomial test fields: check that the
# integral over a large box of a compactly supported test vanishes is not symbolic; instead verify the divergence form:
Phi = sp.Function('Phi')(x, y)
w = sp.Function('w')(x, y)          # stream function of Ubar: Ubar = (-w_y, w_x), div Ubar = 0
rb = sp.Function('rb')(x, y)        # rho bar
Ub = sp.Matrix([-sp.diff(w, y), sp.diff(w, x)])
Vb = cl * sp.Matrix([x, y]) + Ub
h = -(sp.diff(Phi, x, 2) + sp.diff(Phi, y, 2))
Uh = sp.Matrix([-sp.diff(Phi, x, y), sp.diff(Phi, x, 2)])
L0h = Vb[0] * sp.diff(h, x) + Vb[1] * sp.diff(h, y) - h + Uh[0] * sp.diff(rb, x) + Uh[1] * sp.diff(rb, y)
gP = sp.Matrix([sp.diff(Phi, x), sp.diff(Phi, y)])
DUb = sp.Matrix([[sp.diff(Ub[0], x), sp.diff(Ub[0], y)], [sp.diff(Ub[1], x), sp.diff(Ub[1], y)]])
M = (1 + 2 * cl) * sp.eye(2) + (DUb + DUb.T) / 2 + sp.Matrix([[sp.diff(rb, y), -sp.diff(rb, x) / 2],
                                                              [-sp.diff(rb, x) / 2, 0]])
Q = (gP.T * M * gP)[0]
diff_ = sp.expand(-L0h * Phi - Q)
# find a flux J with div J = diff_: integrate by constructing candidate flux from the derivation
Px, Py = sp.diff(Phi, x), sp.diff(Phi, y)
lapP = sp.diff(Phi, x, 2) + sp.diff(Phi, y, 2)
# terms: Phi Vb.grad(Lap Phi) ; Phi Lap Phi ; -Phi (Uh.grad rb)
J1 = (Phi * Vb[0] * lapP - lapP * 0)  # placeholder, replaced by systematic flux below
# systematic: we test that diff_ integrates to zero against compact support by checking it is in the image of div
# via the Euler operator: a polynomial-differential expression is a divergence iff its variational derivative w.r.t.
# Phi vanishes identically (for fixed coefficient functions w, rb treated as given).


def euler_operator(Lag, fun, xs):
    # E(L) = sum_alpha (-D)^alpha dL/d(D^alpha fun); L is a divergence iff E(L) == 0 identically
    atoms = sorted(Lag.atoms(sp.Derivative), key=lambda d: -len(d.variables))
    atoms = [d for d in atoms if d.expr == fun] + [fun]
    syms = {d: sp.Symbol('ATOM%d' % i) for i, d in enumerate(atoms)}
    Ls = Lag.subs(syms)          # derivatives replaced first (sorted highest order first)
    total = 0
    for d, sy in syms.items():
        part = sp.diff(Ls, sy).subs({v: k for k, v in syms.items()})
        vars_ = d.variables if isinstance(d, sp.Derivative) else ()
        term = part
        for v in vars_:
            term = -sp.diff(term, v)
        total += term
    return sp.expand(total)


EL = euler_operator(diff_, Phi, [x, y])
check('Phi-identity: (-L0h)Phi - gradPhi^T M gradPhi is a divergence (Euler operator = 0)', sp.simplify(EL))
# sanity: Euler operator of a non-divergence (Phi^2) is nonzero, of a divergence d_x(Phi^2) is zero
check('Euler-operator sanity: E(d_x(Phi^2 w)) = 0', sp.simplify(euler_operator(sp.expand(sp.diff(Phi**2*w, x)), Phi, [x, y])))
print('   sanity E(Phi^2) =', euler_operator(Phi**2, Phi, [x, y]))

# ---------------------------------------------------------------- 6. source point and axis identities
# on y=0: V2 = 0, rho = 0, V1 even in y, rho_x = 0. Differentiate V.grad rho = rho in y at y=0:
# w g' + V2_y g = g  ->  w g' = (1-h)g, with h = V2_y(x,0); div V = 2c_l -> w' + h = 2 c_l.
gg, ww = sp.Function('g')(x), sp.Function('w')(x)
hh = 2 * cl - sp.diff(ww, x)
eqax = ww * sp.diff(gg, x) - (1 - hh) * gg
# (w/g)' = (2c_l-1)/g:
check('axis: w g\' = (1-h) g  <=>  (w/g)\' = (2c_l-1)/g', sp.simplify(sp.diff(ww / gg, x) - (2 * cl - 1) / gg + eqax / gg ** 2))
# at P: w(x*)=0, g>0 -> h=1 -> w' = 2c_l-1; d(P) = 1 - w'(P) + a_tr*w(P) = 2-2c_l
# integral identity: w = -(2c_l-1) g int_x^{x*} dt/g. near 0, g ~ x^2 (g = x^2 + O(x^4)): w ~ (1-2c_l) x requires
# lim_{x->0} g(x) int_x^{x*} 1/g = x * ... ; with 1/g = 1/x^2 + phi(x): int_x^{x*} 1/g = 1/x - 1/x* + int_x^{x*} phi
# w/x -> -(2c_l-1)[1 + x(-1/x* + int phi)]... w = (1-2c_l) x + O(x^2)*[...]. Next order: w is odd in x? w = V1(x,0) is
# odd in x, so w = (1-2c_l) x + O(x^3), requiring the x^2 coefficient (2c_l-1)(1/x* - int_0^x* phi) to vanish:
gs = sp.symbols('g2')   # g = x^2 (1 + g2 x^2 + ...)
xs = sp.symbols('xstar', positive=True)
K0 = sp.symbols('K0')   # K0 = int_0^{x*} phi
g_ser = x ** 2 * (1 + gs * x ** 2)
Ix = 1 / x - 1 / xs + K0 - sp.integrate(sp.series(1 / g_ser - 1 / x ** 2, x, 0, 3).removeO(), (x, 0, x))
wser = sp.series(-(2 * cl - 1) * g_ser * Ix, x, 0, 3).removeO()
c2 = sp.expand(wser).coeff(x, 2)
check('axis integral: x^2-coefficient of w is (2c_l-1)(1/x* - K0) => K0 = 1/x* for odd w', sp.simplify(c2 - (2 * cl - 1) * (1 / xs - K0)))

# ---------------------------------------------------------------- 7. centre Taylor identities (order 5)
dl, gm, al, be = sp.symbols('delta gamma alpha beta')
rho5 = x ** 2 * y * (1 + dl * x ** 2 + gm * y ** 2)
psi5 = c * x * y + al * x * y ** 3 + be * x ** 3 * y
pois = sp.expand(-(sp.diff(psi5, x, 2) + sp.diff(psi5, y, 2)) - sp.diff(rho5, x))
U5 = sp.Matrix([-sp.diff(psi5, y), sp.diff(psi5, x)])
tr = sp.expand(cl * x * sp.diff(rho5, x) + cl * y * sp.diff(rho5, y) + U5[0] * sp.diff(rho5, x) + U5[1] * sp.diff(rho5, y) - rho5)
sol = sp.solve([pois.coeff(x, 1).coeff(y, 1), tr.coeff(x, 2).coeff(y, 1), tr.coeff(x, 4).coeff(y, 1),
                tr.coeff(x, 2).coeff(y, 3)], [c, al, be, gm], dict=True)[0]
print('   centre solve:', sol)
check('centre: c = 3c_l-1', sol[c] - (3 * cl - 1))
check('centre: alpha+beta = -1/3', sol[al] + sol[be] + sp.Rational(1, 3))
check('centre: beta = 2(2c_l-1) delta', sol[be] - 2 * (2 * cl - 1) * dl)
check('centre: (8c_l-2) gamma = 5 alpha', (8 * cl - 2) * sol[gm] - 5 * sol[al])
# note: higher Poisson terms of psi (x y^3, x^3 y) are only constrained via alpha+beta; the split is nonlocal.

# ---------------------------------------------------------------- 8. homogeneous exponents at the saddle
ls, lu = 1 - 2 * cl, 4 * cl - 1
aa = sp.symbols('aa')
for b in (1, 3, 5):
    asol = sp.solve(aa * ls + b * lu - 1, aa)[0]
    print('   saddle mode |x|^a y^%d: a =' % b, sp.simplify(asol), '=', sp.N(asol.subs(cl, clv), 12))
check('p_3 = 6 + 2/(2c_l-1)', sp.solve(aa * ls + 3 * lu - 1, aa)[0] - (6 + 2 / (2 * cl - 1)))
kk = 1 / cl
check('p_3 code form 6+2k/(2-k) equals 6+2/(2c_l-1)', 6 + 2 * kk / (2 - kk) - (6 + 2 / (2 * cl - 1)))

# ---------------------------------------------------------------- 9. far-field Theta_1 relation
T0, T1, F = sp.Function('T0')(th), sp.Function('T1')(th), sp.Function('F')(th)
k = sp.symbols('k', positive=True)
rho_far = r ** k * T0 * (1 + r ** (k - 1) * T1)
psi_far = r ** (k + 1) * F
UgradRho = (sp.diff(psi_far, r) * sp.diff(rho_far, th) - sp.diff(psi_far, th) * sp.diff(rho_far, r)) / r
expr = sp.expand((1 / k) * r * sp.diff(rho_far, r) + UgradRho - rho_far)
# collect r^(2k-1)
e2 = sp.simplify(expr / r ** (2 * k - 1))
e2 = sp.expand(e2)
# the r^(3k-2) terms (UgradRho with T1) are higher order: remove them by substitution r^(k-1) -> 0 after factoring
lead = sp.limit(sp.expand(expr * r ** (1 - 2 * k)).subs(r, sp.Symbol('R') ** (1 / (k - 1))).subs(sp.Symbol('R'), 0), sp.Symbol('R'), 0) if False else None
coef = sp.expand(expr * r ** (1 - 2 * k))
coef0 = sp.simplify(coef.subs(r ** (k - 1), 0)) if False else None
# manual: r^(2k-1) coefficient
part_a = ((1 / k) * (2 * k - 1) - 1) * T0 * T1
part_b = ((k + 1) * F * sp.diff(T0, th) - k * sp.diff(F, th) * T0)
check('far-field: r^(2k-1) coefficient is (1-c_l) T0 T1 + (k+1) F T0\' - k F\' T0 (c_l=1/k)',
      sp.simplify(sp.expand(((1 / k) * r * sp.diff(r ** (2 * k - 1) * T0 * T1, r) - r ** (2 * k - 1) * T0 * T1
                             + (sp.diff(psi_far, r) * sp.diff(r ** k * T0, th) - sp.diff(psi_far, th) * sp.diff(r ** k * T0, r)) / r)
                            / r ** (2 * k - 1)) - (part_a + part_b)))
check('far-field: leading r^k order cancels (c_l k = 1)', sp.simplify((1 / k) * r * sp.diff(r ** k * T0, r) - r ** k * T0))
check('(1/k)(2k-1)-1 = -(c_l-1)', sp.simplify(((1 / k) * (2 * k - 1) - 1) + (1 / k - 1)))
# canonical far-field mode: -Lap(r^(k+1) sin 2n th) = (4n^2-(k+1)^2) r^(k-1) sin 2n th
P2 = r ** (k + 1) * sp.sin(2 * n * th)
check('far-field mode: -Lap r^(k+1) sin2n th = (4n^2-(k+1)^2) r^(k-1) sin 2n th',
      -(sp.diff(P2, r, 2) + sp.diff(P2, r) / r + sp.diff(P2, th, 2) / r ** 2) - (4 * n ** 2 - (k + 1) ** 2) * r ** (k - 1) * sp.sin(2 * n * th))

# ---------------------------------------------------------------- 10. scaling symmetry
lam = sp.symbols('lambda', positive=True)
# rho_lam(X) = lam rho(X/lam): psi_lam = lam^2 psi(X/lam), U_lam = lam U(X/lam); check V.grad rho - rho scales
# a_lam(0) = lam^-2; kernel direction of L at exact solution: rho - X.grad rho, c[rho - G] = 0 since psi[G]=X.grad psi - psi
psi_t = c * x * y + al * x * y ** 3 + be * x ** 3 * y
psiG = x * sp.diff(psi_t, x) + y * sp.diff(psi_t, y) - psi_t
check('psi[G]_xy(0) = c (so c[rho - G] = 0)', sp.diff(psiG, x, y).subs({x: 0, y: 0}) - c)

print()
print('SUMMARY: %d checks, %d failed' % (len(res), sum(1 for _, ok in res if not ok)))
