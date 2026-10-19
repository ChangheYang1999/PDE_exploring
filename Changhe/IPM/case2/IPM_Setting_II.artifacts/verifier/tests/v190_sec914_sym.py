# Independent symbolic checks of referee result 38 (Section 9.14 draft), verifier.
import sympy as sp
x, y, s, th, l, t, R, g = sp.symbols('x y s theta l t R gamma', real=True)
ok = {}
# kernel K(Z) = (-sin 2th, cos 2th)/(2 pi |Z|^2) in Cartesian form
def K(z1, z2):
    r2 = z1**2 + z2**2
    return sp.Matrix([-2*z1*z2/r2, (z1**2 - z2**2)/r2]) / (2*sp.pi*r2)
z1, z2 = sp.symbols('z1 z2', real=True)
Kz = K(z1, z2)
DK = Kz.jacobian([z1, z2])
# DK(-Y) at Y = s(cos th, sin th)
sub = {z1: -s*sp.cos(th), z2: -s*sp.sin(th)}
DKm = sp.simplify(DK.subs(sub))
claim = sp.Matrix([[-sp.sin(3*th), sp.cos(3*th)], [sp.cos(3*th), sp.sin(3*th)]]) / (sp.pi*s**3)
ok['DK(-Y) display (Step 4)'] = all(sp.simplify(sp.expand_trig(sp.simplify(e))) == 0 for e in (DKm - claim))
# K div and curl free away from 0, and Biot-Savart convention: K = (G_xy, -G_xx), G = log|Z|/(2pi)
G = sp.log(z1**2 + z2**2)/(4*sp.pi)
ok['K = (G_xy, -G_xx)'] = sp.simplify(Kz - sp.Matrix([sp.diff(G, z1, z2), -sp.diff(G, z1, 2)])) == sp.zeros(2, 1)
ok['div K = curl K = 0'] = (sp.simplify(sp.diff(Kz[0], z1) + sp.diff(Kz[1], z2)) == 0 and
                           sp.simplify(sp.diff(Kz[1], z1) - sp.diff(Kz[0], z2)) == 0)
# zero circular mean of K
Kp = sp.Matrix([-sp.sin(2*th), sp.cos(2*th)])
ok['circular mean 0'] = sp.integrate(Kp, (th, 0, 2*sp.pi)) == sp.zeros(2, 1)
# Step 11: mode-2 coefficient of (1/2pi) int log|r e_th - s e_phi| cos^2 phi dphi, numerically checked in v190_num
# F_R formula: Laplacian and radial/mode-2 assembly
r = sp.symbols('r', positive=True)
Rp = sp.symbols('Rp', positive=True)
rad = -sp.Rational(1, 2)*((r**4/4)*sp.log(r) + sp.integrate(s**3*sp.log(s), (s, r, Rp)))
m2 = sp.Rational(1, 8)*(r**-2*sp.integrate(s**5, (s, 0, r)) + r**2*sp.integrate(s, (s, r, Rp)))
FR_claim_rad = -Rp**4*sp.log(Rp)/8 + Rp**4/32 - r**4/32
FR_claim_m2 = Rp**2*r**2/16 - r**4/24
ok['F_R radial part'] = sp.simplify(sp.expand(rad - FR_claim_rad)) == 0
ok['F_R mode-2 part'] = sp.simplify(sp.expand(m2 - FR_claim_m2)) == 0
F = -Rp**4*sp.log(Rp)/8 + Rp**4/32 + Rp**2*(x**2 - y**2)/16 - (x**2 + y**2)**2/32 - (x**4 - y**4)/24
ok['F_R polar = Cartesian'] = sp.simplify(F.subs({x: r*sp.cos(th), y: r*sp.sin(th)}) -
                                          (FR_claim_rad + FR_claim_m2*sp.cos(2*th))) == 0
ok['-Lap F_R = x^2'] = sp.simplify(-(sp.diff(F, x, 2) + sp.diff(F, y, 2)) - x**2) == 0
Fx = sp.diff(F, x)
ok['d_x F_R'] = sp.simplify(Fx - (Rp**2*x/8 - (7*x**3 + 3*x*y**2)/24)) == 0
perp = lambda p: sp.Matrix([-sp.diff(p, y), sp.diff(p, x)])
U = perp(Fx)
ok['U_R'] = sp.simplify(U - sp.Matrix([x*y/4, Rp**2/8 - (7*x**2 + y**2)/8])) == sp.zeros(2, 1)
ok['DU_R(0) = 0'] = U.jacobian([x, y]).subs({x: 0, y: 0}) == sp.zeros(2, 2)
psic = -(7*x**3 + 3*x*y**2)/24
Wc = perp(psic)
ok['W_circ'] = sp.simplify(Wc - sp.Matrix([x*y/4, -(7*x**2 + y**2)/8])) == sp.zeros(2, 1)
# U_R(0) by direct kernel integral: int_{|Y|<R} K(-Y) Y_1^2 dY
U0 = sp.integrate(sp.integrate(Kp/(2*sp.pi*s**2)*s**2*sp.cos(th)**2*s, (th, 0, 2*sp.pi)), (s, 0, Rp))
ok['U_R(0) = (0, R^2/8) by kernel'] = sp.simplify(U0 - sp.Matrix([0, Rp**2/8])) == sp.zeros(2, 1)
# Step 12
Q3 = -(x**3 - 3*x*y**2)/24; Q2 = (l - sp.Rational(1, 2))*x*y
lap = lambda p: sp.diff(p, x, 2) + sp.diff(p, y, 2)
ok['Q3, Q2 harmonic'] = lap(Q3) == 0 and sp.simplify(lap(Q2)) == 0
ok['grad-perp Q3'] = sp.simplify(perp(Q3) - sp.Matrix([-x*y/4, (-x**2 + y**2)/8])) == sp.zeros(2, 1)
ok['grad-perp Q2'] = sp.simplify(perp(Q2) - sp.Matrix([(sp.Rational(1, 2) - l)*x, (l - sp.Rational(1, 2))*y])) == sp.zeros(2, 1)
psi = sp.expand(psic + Q3 + Q2)
ok['corrected stream'] = sp.simplify(psi - (-x**3/3 + (l - sp.Rational(1, 2))*x*y)) == 0
W = perp(psi); rho = x**2
V = sp.Matrix([l*x, l*y]) + W
ok['W display'] = sp.simplify(W - sp.Matrix([(sp.Rational(1, 2) - l)*x, (l - sp.Rational(1, 2))*y - x**2])) == sp.zeros(2, 1)
ok['V display'] = sp.simplify(V - sp.Matrix([x/2, (2*l - sp.Rational(1, 2))*y - x**2])) == sp.zeros(2, 1)
ok['div W = 0, curl W = -rho_x'] = (sp.simplify(sp.diff(W[0], x) + sp.diff(W[1], y)) == 0 and
                                    sp.simplify(sp.diff(W[1], x) - sp.diff(W[0], y) + sp.diff(rho, x)) == 0)
ok['V.grad rho = rho'] = sp.simplify(V[0]*sp.diff(rho, x) + V[1]*sp.diff(rho, y) - rho) == 0
a, b = sp.symbols('a b', real=True)
Vc = sp.Matrix([l*x, l*y]) + Wc + sp.Matrix([[a, b], [b, -a]])*sp.Matrix([x, y])
ok['affine-only residual cubic'] = sp.expand(Vc[0]*2*x - (2*(l + a)*x**2 + 2*b*x*y + x**2*y/2)) == 0
# Step 6 jet linearization with M
lin = sp.expand((sp.Matrix([l*x, l*y]) + sp.Matrix([[a, b], [b, -a]])*sp.Matrix([x, y])).dot(sp.Matrix([2*x, 0])))
ok['jet linearization'] = sp.expand(lin - (2*(l + a)*x**2 + 2*b*x*y)) == 0
ok['stream of MX'] = sp.simplify(perp(-a*x*y + b*(x**2 - y**2)/2) - sp.Matrix([a*x + b*y, b*x - a*y])) == sp.zeros(2, 1)
# Step 8 layer: F = (0, -f(x)), transport (x/2) f' = f, first integral; additive transport
f = sp.Function('f'); h = sp.Function('h')
Fv = sp.Matrix([0, -f(x)])
ok['layer field div/curl'] = (sp.diff(Fv[0], x) + sp.diff(Fv[1], y) == 0 and
                              sp.simplify(sp.diff(Fv[1], x) - sp.diff(Fv[0], y) + sp.diff(f(x), x)) == 0)
Vl = sp.Matrix([l*x, l*y]) + Fv + sp.Matrix([(sp.Rational(1, 2) - l)*x, (l - sp.Rational(1, 2))*y])
rh = f(x) + h(y)
lhs = sp.expand(Vl[0]*sp.diff(rh, x) + Vl[1]*sp.diff(rh, y))
ok['additive transport display'] = sp.simplify(lhs - (x/2*sp.diff(f(x), x) + ((2*l - sp.Rational(1, 2))*y - f(x))*sp.diff(h(y), y))) == 0
ok['d_x(f/x^2)'] = sp.simplify(sp.diff(f(x)/x**2, x) - (x*sp.diff(f(x), x) - 2*f(x))/x**3) == 0
# f_gamma
fg = x**2*(1 + x**2)**((g - 2)/2)
ok['f_gamma derivative'] = sp.simplify(sp.diff(fg, x) - x*(2 + g*x**2)*(1 + x**2)**((g - 4)/2)) == 0
ok['f_gamma jet'] = sp.simplify(sp.series(fg.subs(g, sp.Rational(3, 2)), x, 0, 4).removeO() - x**2) == 0
# Step 10 Q construction on a sample centered harmonic field of degree 3 stream
c1, c2, c3, c4 = sp.symbols('c1:5', real=True)
Qs = c1*(x**2 - y**2) + c2*x*y + c3*(x**3 - 3*x*y**2) + c4*(3*x**2*y - y**3)
H = perp(Qs)
Qrec = sp.integrate(H[1].subs(y, 0).subs(x, s), (s, 0, x)) - sp.integrate(H[0].subs(y, t), (t, 0, y))
ok['Step 10 Q recovers stream'] = sp.simplify(Qrec - Qs) == 0
# Laplacian of r^k q(th): k^2 q + q''
q = sp.Function('q'); k = sp.symbols('k', positive=True, integer=True)
pol = r**k*q(th)
lap_pol = sp.diff(pol, r, 2) + sp.diff(pol, r)/r + sp.diff(pol, th, 2)/r**2
ok['polar Laplacian'] = sp.simplify(lap_pol - r**(k - 2)*(k**2*q(th) + sp.diff(q(th), th, 2))) == 0
for kk, v in ok.items():
    print(f'{kk}: {v}')
print('ALL', all(ok.values()), len(ok))
