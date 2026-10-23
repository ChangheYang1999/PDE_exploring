"""Checks for the Gaussian non-profile of 3.24 (A.3.24 repair).

rho = -y (1 + 4 x^2) exp(-r^2)/100, c_l = 401/400.
(1) Fourier transform with hat f(xi) = int f(X) exp(-i X.xi) dX.
(2) Bound sup |DU|_op <= (2 pi)^-2 int |xi_1| |hat rho| dxi in closed form.
(3) Pointwise |DU|_op on a grid from the modal stream function.
(4) The weighted-identity defect J = lim int_{|X|>eps} rho U.grad phi dX, phi = r^-3 sin 3th,
    exactly (Mellin continuation) and by direct quadrature.
"""
import sympy as sp
import mpmath as mp

x, y, r, th, t, s, z = sp.symbols('x y r theta t s z', real=True)
xi1, xi2 = sp.symbols('xi1 xi2', real=True)
u = sp.symbols('u', positive=True)

sigma = y * (1 + 4 * x**2) * sp.exp(-(x**2 + y**2))
rho = -sigma / 100

# (1) Fourier transform, separable
def ft1(f, var, k):
    return sp.simplify(sp.integrate(f * sp.exp(-sp.I * var * k), (var, -sp.oo, sp.oo)))

hat_sigma = sp.simplify(ft1(sp.exp(-x**2), x, xi1) * ft1(y * sp.exp(-y**2), y, xi2)
                        + 4 * ft1(x**2 * sp.exp(-x**2), x, xi1) * ft1(y * sp.exp(-y**2), y, xi2))
hat_rho = sp.simplify(-hat_sigma / 100)
audit = sp.I * sp.pi / 200 * xi2 * (3 - xi1**2) * sp.exp(-(xi1**2 + xi2**2) / 4)
print('hat rho =', sp.factor(hat_rho))
print('hat rho - audit formula =', sp.simplify(hat_rho - audit))

# (2) DU symbol: DU = [[-psi_xy, -psi_yy], [psi_xx, psi_xy]], hat psi = i xi1 hat rho/|xi|^2,
# matrix (i xi1 hat rho/|xi|^2) * xi_perp (x) xi with xi_perp = (xi2, -xi1): operator norm |xi1| |hat rho|.
I1 = sp.integrate(sp.Abs(xi1) * sp.Abs(3 - xi1**2) * sp.exp(-xi1**2 / 4), (xi1, -sp.oo, sp.oo))
I1 = sp.simplify(2 * (sp.integrate(xi1 * (3 - xi1**2) * sp.exp(-xi1**2 / 4), (xi1, 0, sp.sqrt(3)))
                      + sp.integrate(xi1 * (xi1**2 - 3) * sp.exp(-xi1**2 / 4), (xi1, sp.sqrt(3), sp.oo))))
I2 = sp.integrate(2 * xi2 * sp.exp(-xi2**2 / 4), (xi2, 0, sp.oo))
bound = sp.simplify(sp.pi / 200 * I1 * I2 / (4 * sp.pi**2))
print('int |xi1||3 - xi1^2| e^{-xi1^2/4} =', sp.simplify(I1), ' int |xi2| e^{-xi2^2/4} =', I2)
print('bound (2pi)^-2 int |xi1||hat rho| =', sp.simplify(bound), '=', sp.N(bound, 12))
print('target (8 e^{-3/4} - 1)/(50 pi) =', sp.N((8 * sp.exp(-sp.Rational(3, 4)) - 1) / (50 * sp.pi), 12))
print('audit 17/(75 pi) =', sp.N(sp.Rational(17, 75) / sp.pi, 12), ' c_l = 401/400 =', 401 / 400)

# (3) Modal stream function for sigma: d_x sigma = f2(r) sin 2th + f4(r) sin 4th
dxs = sp.diff(sigma, x)
pol = sp.simplify(dxs.subs({x: r * sp.cos(th), y: r * sp.sin(th)}))
f2 = sp.simplify(sp.integrate(pol * sp.sin(2 * th), (th, 0, 2 * sp.pi)) / sp.pi)
f4 = sp.simplify(sp.integrate(pol * sp.sin(4 * th), (th, 0, 2 * sp.pi)) / sp.pi)
rest = sp.simplify(pol - f2 * sp.sin(2 * th) - f4 * sp.sin(4 * th))
print('f2 =', f2, ' f4 =', f4, ' remainder =', sp.simplify(sp.expand_trig(rest)))

def green(fm, m):
    # canonical mode solution of -(g'' + g'/r - m^2 g/r^2) = fm
    a = sp.integrate((s**(m + 1) * fm.subs(r, s)), (s, 0, r))
    b = sp.integrate((s**(1 - m) * fm.subs(r, s)), (s, r, sp.oo))
    return sp.simplify((r**(-m) * a + r**m * b) / (2 * m))

p2 = green(f2, 2)
p4 = green(f4, 4)
tt = sp.symbols('tt', positive=True)
print('psi2 (t = r^2):', sp.simplify(p2.subs(r, sp.sqrt(tt))))
print('psi4 (t = r^2):', sp.simplify(p4.subs(r, sp.sqrt(tt))))
for g, m in ((p2, 2), (p4, 4)):
    res = sp.simplify(-(sp.diff(g, r, 2) + sp.diff(g, r) / r - m**2 * g / r**2) - (f2 if m == 2 else f4))
    print('ODE residual mode', m, ':', res, ' series at 0:', sp.series(g, r, 0, m + 3).removeO())

psi_sigma = p2 * sp.sin(2 * th) + p4 * sp.sin(4 * th)
psi_rho = -psi_sigma / 100
# strain c = psi_xy(0) = 2 * (r^2 coefficient of psi2)/... : psi2 ~ C r^2 means psi ~ C r^2 sin 2th = 2 C x y
C2 = sp.limit(-p2 / 100 / r**2, r, 0)
print('c = psi_xy(0) =', 2 * C2, ' (expected -1/400)')

# DU from the polar stream function: Cartesian second derivatives via sympy
X, Y = sp.symbols('X Y', real=True)
Rr = sp.sqrt(X**2 + Y**2)
psi_cart = psi_rho.subs({sp.sin(2 * th): 2 * X * Y / Rr**2,
                         sp.sin(4 * th): 4 * X * Y * (X**2 - Y**2) / Rr**4}).subs(r, Rr)
pxx = sp.lambdify((X, Y), sp.diff(psi_cart, X, 2), 'mpmath')
pxy = sp.lambdify((X, Y), sp.diff(psi_cart, X, Y), 'mpmath')
pyy = sp.lambdify((X, Y), sp.diff(psi_cart, Y, 2), 'mpmath')
mp.mp.dps = 30
best = 0
for i in range(1, 61):
    for j in range(0, 61):
        a, b = mp.mpf(i) / 15, mp.mpf(j) / 15
        M = mp.matrix([[-pxy(a, b), -pyy(a, b)], [pxx(a, b), pxy(a, b)]])
        nrm = mp.sqrt(max(mp.eig(M.T * M)[0], key=lambda v: mp.re(v)).real)
        best = max(best, nrm)
print('max |DU|_op on grid (0,4]x[0,4] step 1/15:', mp.nstr(best, 8))

# (4) weighted identity defect
phi = r**-3 * sp.sin(3 * th)
psi = psi_rho
Ugradphi = (sp.diff(psi, r) * sp.diff(phi, th) - sp.diff(psi, th) * sp.diff(phi, r)) / r
rho_pol = -(r + r**3) * sp.exp(-r**2) * sp.sin(th) / 100 - r**3 * sp.exp(-r**2) * sp.sin(3 * th) / 100
chk = sp.simplify(sp.expand_trig(rho_pol - rho.subs({x: r * sp.cos(th), y: r * sp.sin(th)})))
print('modal form of rho ok:', chk == 0)
ang = sp.simplify(sp.integrate(sp.expand(rho_pol * Ugradphi * r), (th, 0, 2 * sp.pi)))
radial = sp.simplify(ang.subs(r, sp.sqrt(tt)) / (2 * sp.sqrt(tt)))  # dr = dt/(2 sqrt t)
radial = sp.expand(sp.simplify(radial))
print('radial integrand in t (times 10^4/(3pi/4)):', sp.simplify(radial * 10**4 / (3 * sp.pi / 4)))
print('integrand series at t=0:', sp.series(radial, tt, 0, 2))
# Mellin continuation: int_0^inf t^z F(t) dt termwise, then z -> 0
terms = sp.Add.make_args(sp.expand(radial))
Mz = 0
for term in terms:
    coeff, rest_ = term.as_independent(tt)
    # rest_ = t^k * exp(-a t)
    k = sp.degree(sp.powsimp(rest_ * sp.exp(sp.Wild('w'))), tt) if False else None
    pw = sp.powsimp(rest_)
    a_exp = 0
    kk = 0
    for fac in sp.Mul.make_args(pw):
        if fac.func == sp.exp:
            a_exp = -sp.simplify(fac.args[0] / tt)
        elif fac == tt:
            kk += 1
        elif fac.is_Pow and fac.base == tt:
            kk += fac.exp
        else:
            coeff *= fac
    Mz += coeff * sp.gamma(z + kk + 1) / a_exp**(z + kk + 1)
J_exact = sp.simplify(sp.limit(Mz, z, 0))
J_target = sp.pi * (sp.Rational(33, 8) * sp.log(2) - sp.Rational(83, 32)) / 10**4
print('J (Mellin) =', J_exact, ' equals pi[(33/8)log2 - 83/32]/10^4:', sp.simplify(J_exact - J_target) == 0)
print('J numeric =', sp.N(J_exact, 25))
Fnum = sp.lambdify(tt, radial, 'mpmath')
mp.mp.dps = 120  # the 1/t^4 terms cancel near 0, so use high precision and start at t = 1e-12
Jq = mp.quad(lambda v: Fnum(v), [mp.mpf('1e-12'), mp.mpf('1e-3'), 1, 5, 40, mp.inf])
print('J by radial quadrature =', mp.nstr(Jq, 25))

# direct 2D quadrature with circular truncation eps -> small, as an independent check of the angular step
rho_f = sp.lambdify((r, th), rho_pol, 'mpmath')
ug_f = sp.lambdify((r, th), Ugradphi, 'mpmath')
mp.mp.dps = 20
J2 = mp.quad(lambda rr: mp.quad(lambda a: rho_f(rr, a) * ug_f(rr, a) * rr, [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]),
             [mp.mpf('1e-4'), 1, 3, 8])
print('J by 2D quadrature on 1e-4 < r < 8:', mp.nstr(J2, 12))
D = sp.Rational(1, 400)
a0 = sp.Rational(-1, 100)
print('required value -pi D (D + a0/4) =', -sp.pi * D * (D + a0 / 4))
