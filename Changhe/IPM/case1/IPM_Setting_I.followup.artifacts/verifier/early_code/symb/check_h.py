"""verifier, request (h): conormal modes C |xi|^mu_j y^j at P (FINAL_REPORT 6.4 'Which hypothesis fits a profile').
(1) mu_j = (1 + g* - j)/A at X3; (2) Hoelder class of |xi|^mu y^j; (3) axis restriction of a linearizing coordinate;
(4) y-Taylor coefficients on the axis of |xi(x,y)|^mu y^j, xi even in y, and their size relative to H_i."""
import sympy as sp
import numpy as np

c_l = 5.575362610642                      # X3 (B1)
A = 2 * c_l - 1
gs = 29.7494907                           # g(P) at X3 (B2, trial trace)
print('A =', A, ' g* =', gs, ' g*/A =', gs / A, ' 1 - 2/A =', 1 - 2 / A)
mu = {j: (1 + gs - j) / A for j in range(1, 13, 2)}
print('(1) mu_j:', {j: round(v, 5) for j, v in mu.items()})
print('    mu_j - 2:', {j: round(v - 2, 5) for j, v in mu.items()})

# (2) second xi-derivative of xi_+^mu, xi_-^mu: Hoelder quotient at 0 is exactly mu - 2 (mu non-integer in (2,3))
xi, y, s = sp.symbols('xi y s', real=True)
m3 = sp.Rational(27749491, 10150725)      # rational stand-in for mu_3 (only non-integrality and 2 < mu < 3 are used)
f2 = sp.diff(xi ** m3, xi, 2)
print('(2) d_xi^2 xi^mu =', sp.simplify(f2), '; exponent', m3 - 2, float(m3 - 2))

# (3) linearizing coordinate on the axis: W_2(x,0) = 0, W_1(x,0) = w(x), so W.grad xi = A xi gives w f' = A f for
#     f(x) = xi(x, 0).  With w = A s + w2 s^2 + w3 s^3 + w4 s^4 (s = x - x*): f = c s (1 + e1 s + e2 s^2 + e3 s^3).
As, w2, w3, w4, c = sp.symbols('A w2 w3 w4 c')
e1, e2, e3 = sp.symbols('e1 e2 e3')
w = As * s + w2 * s ** 2 + w3 * s ** 3 + w4 * s ** 4
f = c * s * (1 + e1 * s + e2 * s ** 2 + e3 * s ** 3)
res = sp.expand(w * sp.diff(f, s) - As * f)
sol = sp.solve([res.coeff(s, k) for k in (2, 3, 4)], [e1, e2, e3], dict=True)[0]
print('(3) f/(c s) = 1 +', sp.simplify(sol[e1]), 's +', sp.factor(sol[e2]), 's^2 + ...')
#     closed form: f = c s E(s), log E = -int_0^s (v - A)/(t v) dt, v = w/t; check E' / E against the ODE
v = sp.cancel(w / s)
E = sp.Function('E')
ode = sp.simplify((w * sp.diff(c * s * E(s), s) - As * c * s * E(s)) / (c * s))
print('    ODE for E: ', sp.simplify(ode), ' = 0  <=>  E\'/E = (A - v)/(s v) =', sp.simplify((As - v) / (s * v)))

# (4) xi(x, y) = xi0(x) + xi2(x) y^2 + xi4(x) y^4 (even in y).  y^(2k) coefficient of |xi|^mu (xi0 < 0 on the left
#     axis): leading term binom(mu, k) xi2^k |xi0|^(mu - k).
x0, x2, x4, mus = sp.symbols('x0 x2 x4 mu', positive=True)
ser = sp.series((x0 + x2 * y ** 2 + x4 * y ** 4) ** mus, y, 0, 9).removeO()
for k in range(1, 5):
    ck = sp.expand(ser.coeff(y, 2 * k))
    lead = sp.binomial(mus, k) * x2 ** k * x0 ** (mus - k)
    rest = sp.simplify(sp.expand_func(ck - lead) / x0 ** (mus - k + 1))
    print('(4) k=%d: coeff - binom(mu,k) xi2^k xi0^(mu-k) = xi0^(mu-k+1) *' % k, sp.factor(sp.expand_func(rest)))
#     G_i/H_i exponent from mode j at i = j + 2k: mu_j - k + q_i, q_i = (i-1)/A  ->  g*/A - k (1 - 2/A)
for k in range(0, 6):
    exps = {j: mu[j] - k + (j + 2 * k - 1) / A for j in (1, 3, 5)}
    print('    k=%d: exponent of |s| in (mode j contribution to G_{j+2k})/H_{j+2k}:' % k,
          {j: round(e, 5) for j, e in exps.items()}, ' formula', round(gs / A - k * (1 - 2 / A), 5))
#     size of the j = 3 mode's own G_3 contribution and of the j = 1 mode's G_3 contribution (k = 1)
print('    G_3 contributions: |s|^mu_3 =', round(mu[3], 5), ', mode 1 via curvature |s|^(mu_1 - 1) =', round(mu[1] - 1, 5))
# d_y^2 of |xi|^mu y^j on the cone |y| < kappa r, r = x* - x: O(|y| r^(mu_j + j - 3)); exponents
print('    cone exponent mu_j + j - 3:', {j: round(mu[j] + j - 3, 5) for j in mu})
