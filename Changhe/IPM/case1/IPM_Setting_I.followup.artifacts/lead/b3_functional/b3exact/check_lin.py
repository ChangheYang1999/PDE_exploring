"""Checks of lin_r12.py: (1) the framework: f.p. int_0^x* J_0 on R12 data reproduces B_3^nat = C_A (1 - S_A/L^2);
(2) the linearization: finite-eps nonlinear difference int (J_eps - J_0) against eps * (linear response)."""
import sys
import numpy as np
import sympy as sp
from scipy.integrate import quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
sys.argv = ['lin_r12.py', '8.6', '1.0', '0.3']
src = open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), 'lin_r12.py')).read().split("z = np.load")[0]
exec(src)
# (1) f.p. of J_0: J_0 = q m^(beta-1), m = A (1-u^2)/x; x^(5+beta) J_0 = E(x) smooth even: subtract E0 + E2 x^2 + E4 x^4
tt = sp.symbols('tt', positive=True)
a2S = (sp.diff(gS, t) - sp.diff(wS, t, 2)) / 2
qS = sp.diff(a2S, t) / gS ** 3 - 3 * a2S * sp.diff(gS, t) / gS ** 4
E = sp.simplify(qS * t ** 6)   # J_0 x^(5+beta) = A^(beta-1) E (1-u^2)^(beta-1)
Ef = sp.lambdify(t, E, 'numpy')
ser = sp.series(qS * t ** 6 * (1 - (t / L) ** 2) ** (beta - 1), t, 0, 18).removeO()
cs = [float(ser.coeff(t, k)) for k in range(18)]
print('series coefficients of x^(5+beta) J_0 / A^(beta-1) (k = 0, 2, 4):', ['%.6e' % cs[k] for k in (0, 2, 4)])
Afac = A ** (beta - 1)
J0 = lambda x: Afac * Ef(x) * (1 - (x / L) ** 2) ** (beta - 1) / x ** (5 + beta)
xc = 0.5   # f.p. on [0, xc] from the series (radius of convergence L), quadrature beyond
I1 = Afac * sum(cs[k] * xc ** (k - 4 - beta) / (k - 4 - beta) for k in range(0, 18, 2))
I1 += quad(J0, xc, 0.9 * xs, limit=400, epsrel=1e-12)[0]
xc = 0.9 * xs
D = xs - xc
def tail(tau):   # x = x* - D tau^(1/beta); (1-u)^(beta-1) dx/dtau combines into a smooth factor
    x = xs - D * tau ** (1 / beta)
    return Afac * Ef(x) * (1 + x / L) ** (beta - 1) * (D / L) ** (beta - 1) * D / beta / x ** (5 + beta)
I2 = quad(tail, 0, 1, limit=400, epsrel=1e-12)[0]
SA = 6 * A * (4 * A - 3) / (8 * A - 1)
print('f.p. B_3^nat on R12 L=8.6: %.8f   closed form C_A (1 - S_A/L^2) with C_A = 0.530667: %.8f' % (
    xs ** (p3 - 2) / (3 * N) * (I1 + I2), 0.530667 * (1 - SA / L ** 2)))
# (2) nonlinear finite-eps difference for the bump at x0 = 1, sig = 0.3 (b flat at 0, cut off near x*)
x0 = 1.0
lo, hi = x0 * np.exp(-9 * sig), 0.95 * xs
xx = np.geomspace(lo, hi, 400001)
def Jeps(x, e, Ks):
    w, w1, w2, w3 = [f(x) for f in W]; b, b1, b2, b3 = [f(x, x0) for f in Bf]
    we = w * (1 + e * b); we1 = w1 * (1 + e * b) + e * w * b1
    we2 = w2 * (1 + e * b) + 2 * e * w1 * b1 + e * w * b2
    we3 = w3 * (1 + e * b) + 3 * e * w2 * b1 + 3 * e * w1 * b2 + e * w * b3
    g = G[0](x) * (1 + e * b) * np.exp(e * A * Ks(x))    # exact: d ln g = ln(1 + e b) + e A int_0^x b/(w (1 + e b))
    r = G[1](x) / G[0](x) + e * (b1 + A * b / w) / (1 + e * b)
    g1 = g * r
    rp = R[1](x) + e * ((b2 + A * (b1 * w - b * w1) / w ** 2) * (1 + e * b) - (b1 + A * b / w) * e * b1) / (1 + e * b) ** 2
    g2 = g1 * r + g * rp
    a2 = (g1 - we2) / 2; a2p = (g2 - we3) / 2
    q = a2p / g ** 3 - 3 * a2 * g1 / g ** 4
    return q * (np.abs(we) / g) ** (beta - 1)
for e in (1e-4, 1e-5):
    Kc = cumulative_trapezoid(Bf[0](xx, x0) / (W[0](xx) * (1 + e * Bf[0](xx, x0))), xx, initial=0.0)
    Ksp = CubicSpline(np.log(xx), Kc); Kinf = Kc[-1]
    Ks = lambda x: Ksp(np.log(x)) if x < hi else Kinf
    pts = [lo, x0 * np.exp(-sig), x0, x0 * np.exp(sig), 0.8 * xs, hi]
    f = lambda x: Jeps(x, e, Ks) - Jeps(x, 0.0, lambda x: 0.0)
    Id = sum(quad(f, a, b, limit=400, epsabs=0, epsrel=1e-10)[0] for a, b in zip(pts[:-1], pts[1:]))
    Dd = xs - hi
    Id += quad(lambda tau: f(xs - Dd * tau ** (1 / beta)) * Dd / beta * tau ** (1 / beta - 1), 0, 1, limit=400)[0]
    print('eps %.0e: nonlinear dB3nat/eps = %.6e' % (e, xs ** (p3 - 2) / (3 * N) * Id / e))
