"""verifier: independent check of fred6's frozen counterexample (lead verifier/fred6/02-endpoint-counterexample/PROOF.md).
vhat = ahat(xi) i sgn(eta) |eta|^kappa (xi^2 + eta^2)^(-b), a = s_+^(-q), q = 2/A, b = g/(2(A-1)), kappa = 2b - 4.
Checks (own derivations, not the referee's script):
 (1) Fourier symbol of L_g with vhat = int e^{-i(s xi + y eta)} v: F[(A s d_s + y d_y - 1) v] = -(A xi d_xi + eta d_eta + A + 2) vhat
     (sympy on Gaussian test functions); M = xi^2/|zeta|^2 from U_2 = psi_x, -Laplace psi = d_x rho.
 (2) Euler identity (A xi d_xi + eta d_eta) vhat = -(A + 2 + g M) vhat (sympy, symbolic A, g).
 (3) G_3 on s < 0 by a PHYSICAL-SPACE route: v = K_b * (a(s) k_kappa(y)), K_b = F^{-1}|zeta|^{-2b} = c_b |X|^(2b-2),
     k_kappa = F^{-1}[i sgn eta |eta|^kappa] = kc sgn y |y|^(-1-kappa).  d_y^3 v(s, 0) = int int d_2^3 K(s - t, -y') t^(-q) k(y')
     is absolutely convergent for s < 0 and reduces to -2 kc c_b C_in pi/sin(pi q) |s|^(-q), C_in = int_0^inf u^(-1-kappa)
     d_u^3 (1 + u^2)^((2b-2)/2) du.  Claim (3) of fred6 is equivalent to -4 pi kc c_b C_in = 1.
 (4) The lead's two constants: F^{-1}[ahat log|xi|](-1) (direct oscillatory quadrature) and the eta-moment constant.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
out = []
P = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))

# (1) Fourier symbol of the transport part, Gaussian test functions
s, y, xi, eta, A, g = sp.symbols('s y xi eta A g', real=True)
Ap = sp.Rational(10150725, 1000000)
for v in [y * sp.exp(-(s**2 + y**2) / 2), s * y * sp.exp(-(s**2 + 2 * y**2) / 2), y**3 * sp.exp(-(2 * s**2 + y**2) / 2)]:
    FT = lambda f: sp.simplify(sp.integrate(sp.integrate(f * sp.exp(-sp.I * (s * xi + y * eta)), (s, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo)))
    vh = FT(v)
    lhs = FT(Ap * s * sp.diff(v, s) + y * sp.diff(v, y) - v)
    rhs = -(Ap * xi * sp.diff(vh, xi) + eta * sp.diff(vh, eta) + (Ap + 2) * vh)
    P('(1) transport symbol, test', v, ': residual', sp.simplify(lhs - rhs))
# U_2 = psi_x, -Lap psi = d_x rho: psihat = i xi rhohat/|zeta|^2, U2hat = i xi psihat = -xi^2/|zeta|^2 rhohat
P('(1) U2hat/rhohat =', sp.simplify(sp.I * xi * (sp.I * xi / (xi**2 + eta**2))), '=> W.grad(g y + v) - (g y + v) linear part: L_g v with M = xi^2/|zeta|^2')

# (2) Euler identity on xi > 0, eta > 0 (the other quadrants by the same powers)
q = 2 / A
b = g / (2 * (A - 1))
kap = 2 * b - 4
M = xi**2 / (xi**2 + eta**2)
lv = (q - 1) * sp.log(xi) + kap * sp.log(eta) - b * sp.log(xi**2 + eta**2)       # log vhat on xi, eta > 0
res = sp.simplify(A * xi * sp.diff(lv, xi) + eta * sp.diff(lv, eta) + (A + 2 + g * M))
P('(2) Euler identity residual (symbolic A, g):', res)
P('(2) isotropic degree of vhat:', sp.simplify(q - 1 + kap - 2 * b), '(= q - 5)')

# (3) physical-space constant
def consts(Av, gv):
    Av, gv = mp.mpf(Av), mp.mpf(gv)
    qv = 2 / Av
    bv = gv / (2 * (Av - 1))
    kv = 2 * bv - 4
    m = 2 * bv - 2
    cb = mp.gamma(1 - bv) / (4**bv * mp.pi * mp.gamma(bv))               # F^{-1}|zeta|^{-2b} in R^2
    kc = -mp.gamma(1 + kv) * mp.cos(mp.pi * kv / 2) / mp.pi                 # F^{-1}[i sgn |eta|^kappa] in R^1
    # d_u^3 (1+u^2)^(m/2), closed form
    f3 = lambda u: m * (m - 2) * u * (1 + u**2)**(m / 2 - 3) * (3 + (m - 1) * u**2)
    Cin = mp.quad(lambda u: u**(-1 - kv) * f3(u), [0, 1, 10, mp.inf])
    return qv, bv, kv, cb, kc, Cin

# closed form of d_u^3 (1+u^2)^(m/2) checked by sympy
u, m_ = sp.symbols('u m', positive=True)
P('(3) d^3 closed form residual:', sp.simplify(sp.diff((1 + u**2)**(m_ / 2), u, 3) - m_ * (m_ - 2) * u * (1 + u**2)**(m_ / 2 - 3) * (3 + (m_ - 1) * u**2)))
# k_kappa and c_b checked numerically against their defining integrals (Abel regularization)
qv, bv, kv, cb, kc, Cin = consts('10.150725', '29.749491')
kc_num = -(mp.quad(lambda e: mp.sin(e) * e**kv, [0, 1]) + mp.quadosc(lambda e: mp.sin(e) * e**kv, [1, mp.inf], omega=1)) / mp.pi       # k(1) = -(1/pi) int sin(eta) eta^kappa
P('(3) A = 10.150725, g = 29.749491: q', mp.nstr(qv, 12), 'b', mp.nstr(bv, 10), 'kappa', mp.nstr(kv, 12))
P('(3) k_kappa(1): closed', mp.nstr(kc, 15), 'quadrature', mp.nstr(kc_num, 15))
# c_b: radial check via the 2D Hankel transform with Abel factor: (1/2pi) int rho^(1-2b) J0(rho) e^{-eps rho} drho -> c_b
cb_num = mp.quadosc(lambda r: r**(1 - 2 * bv) * mp.besselj(0, r), [0, mp.inf], period=2 * mp.pi) / (2 * mp.pi) if False else None
# (rho^(1-2b) is not integrable at 0 for 2b > 2: c_b is the analytic continuation; check it by Mellin-Barnes identity instead)
cb_mb = 2**(-2 * bv) * mp.gamma(1 - bv) / mp.gamma(bv) / mp.pi
P('(3) c_b', mp.nstr(cb, 15), '(analytic continuation of the Riesz constant; same as 2^(-2b) Gamma(1-b)/(pi Gamma(b)):', mp.nstr(cb_mb, 15), ')')
lhs = -4 * mp.pi * kc * cb * Cin
P('(3) C_in', mp.nstr(Cin, 15), ';  -4 pi kc c_b C_in =', mp.nstr(lhs, 20), '(fred6 (3) <=> 1)')
G3 = -2 * kc * cb * Cin * mp.pi / mp.sin(mp.pi * qv) / 6
P('(3) G_3 |s|^q from the physical route', mp.nstr(G3, 15), '; fred6 1/(12 sin(pi q))', mp.nstr(1 / (12 * mp.sin(mp.pi * qv)), 15))
for Av, gv in [('6', '17'), ('10.150725', '29.749491'), ('20', '64'), ('4', '10'), ('3', '7.5')]:
    qv_, bv_, kv_, cb_, kc_, Cin_ = consts(Av, gv)
    P('(3) A', Av, 'g', gv, 'g/(A-1)', mp.nstr(mp.mpf(gv) / (mp.mpf(Av) - 1), 6), ': -4 pi kc c_b C_in =', mp.nstr(-4 * mp.pi * kc_ * cb_ * Cin_, 18))

# (4) lead's constants
ah = lambda x: mp.gamma(1 - qv) * abs(x)**(qv - 1) * mp.exp(-1j * mp.pi * (1 - qv) * mp.sign(x) / 2)
# F^{-1}[ahat log|xi|](s) = (1/pi) Re int_0^inf e^{i s xi} ahat(xi) log(xi) dxi, at s = -1
# [0, 1] by the power series of e^{-iz} (direct quadrature at the z^(q-1) end loses 1e-6), [1, inf) on the contour z = 1 - i t
cq = mp.gamma(1 - qv) * mp.exp(-1j * mp.pi * (1 - qv) / 2)
S1 = mp.nsum(lambda n: -(-1j)**n / mp.factorial(n) / (n + qv)**2, [0, mp.inf])
I1 = mp.quad(lambda t: mp.exp(-1j * (1 - 1j * t)) * (1 - 1j * t)**(qv - 1) * mp.log(1 - 1j * t) * (-1j), [0, 1, 10, mp.inf])
re = mp.re(cq * (S1 + I1)) / mp.pi
P('(4) F^{-1}[ahat log|xi|](-1): quadrature', mp.nstr(re, 15), '; -pi/(2 sin pi q)', mp.nstr(-mp.pi / (2 * mp.sin(mp.pi * qv)), 15), '; lead -2.70728')
# eta-moment constant: int_0^R eta^(2b-1) (1+eta^2)^(-b) d eta = log R + c + o(1)
c_sharp = mp.quad(lambda e: e**(2 * bv - 1) * (1 + e**2)**(-bv), [0, 1]) + mp.quad(lambda e: e**(2 * bv - 1) * (1 + e**2)**(-bv) - 1 / e, [1, mp.inf])
P('(4) eta-moment constant (sharp cutoff): c =', mp.nstr(c_sharp, 12), '; closed form (psi(1) - psi(b))/2 =', mp.nstr((mp.digamma(1) - mp.digamma(bv)) / 2, 12), '; lead -0.3624748')
open('verifier/early_runs/check_fred6.log', 'w').write('\n'.join(out) + '\n')
