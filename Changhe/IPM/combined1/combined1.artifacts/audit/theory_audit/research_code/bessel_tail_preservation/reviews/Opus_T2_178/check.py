"""Checks for the c1-t2 reviews of T4-178 (Bessel multipliers keep a differentiated power tail) and
T4-177 (growing-weight S1 velocity bound and the exact interval |p| < 2).

Sources (read only):
  c1-t4/research/bessel_tail_preservation/PROOF.md  sha256 bb3f77dc59f21a4ebc1b27c2d972a706d9fe013c436bb54fb8df610f8d9360af
  c1-t4/research/growing_weight_velocity/PROOF.md   sha256 57498412d681621363d935541575b88050855e6c9264dd4293447febbd470c76

Part A (T4-178).
  A1 sympy: the constant in (5) and the closed form of the t-integral in (9).
  A2 mpmath: (5) at sample (alpha, lambda); the Gaussian radial moment (4t)^(b/2) Gamma(1 + b/2).
  A3 FLOAT: for g = <X>^e (radial), J^s g - g from the heat representation (6), rewritten as
      J^s g - g = -c_alpha int_0^inf exp(tau Delta)(Delta g) Gamma(-alpha, tau) d tau,
     with the radial heat kernel. It prints r^(2 - e)(J^s g - g), the bound (9) times r^(2 - e), and the
     value -alpha e^2 expected from the first Taylor term of the symbol (not claimed by the proof).
Part B (T4-177).
  B1 sympy: symbol identities U2 + i U1 = -(1 + B)/2, R1^2 = -1/2 + (R1^2 - R2^2)/2, B even, the velocity
     constants (1 + K)/2, and the pointwise coefficient identities behind (7), (8), (9) of T4-054.
  B2 sympy: -d_y K2 = sin(3 theta)/(pi r^3) for K2 = (x^2 - y^2)/(2 pi |X|^4).
  B3 FLOAT: h = y eta, eta = (1 - |Y|^2)^4 on the unit disk; U2[h](X) by quadrature against K2 at |X| = 4, 8,
     16, 32, compared with M sin(3 theta)/(pi r^3). Also the monopole case (full space) with eta itself.
     A radial profile times one angular mode has an exact multipole field outside its support, so these ratios
     are 1 up to quadrature error; the O(|X|^-4) error in (3) of T4-177 vanishes for these tests.
Runtime: about 15 s on one core.
"""
import math
import sys
import time
import warnings

import mpmath as mp
import numpy as np
import sympy as sp
from scipy import integrate, special

warnings.simplefilter("ignore", integrate.IntegrationWarning)

T0 = time.time()
mp.mp.dps = 30
print("t4_177_178_review.py start", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

# ---------------------------------------------------------------- A1


def qsub(f, alpha, extra=()):
    """int_0^inf f(t) dt for f ~ t^(-alpha) at 0: substitute t = u^m, m = 1/(1 - alpha), which removes the
    endpoint singularity (plain tanh-sinh loses about 2 percent at alpha = 0.95)."""
    m = 1 / (1 - alpha)
    g = lambda u: f(u ** m) * m * u ** (m - 1)
    pts = sorted(set([mp.mpf(0)] + [mp.mpf(q) ** (1 / m) for q in list(extra) + [1, 10]])) + [mp.inf]
    return mp.quad(g, pts)


al, lam, t, b = sp.symbols("alpha lambda t b", positive=True)
# int_0^inf (e^-t - e^-(1+lam) t) t^(-1-alpha) dt = Gamma(1-alpha)((1+lam)^alpha - 1)/alpha  (Frullani type)
# check d/d lam of both sides: int e^-(1+lam)t t^-alpha dt = Gamma(1-alpha)(1+lam)^(alpha-1)
lhs_d = sp.integrate(sp.exp(-(1 + lam) * t) * t ** (-al), (t, 0, sp.oo), conds="none")
rhs_d = sp.diff(sp.gamma(1 - al) * ((1 + lam) ** al - 1) / al, lam)
print("A1 d/dlambda of (5), difference:", sp.simplify(sp.gammasimp(lhs_d - rhs_d)))
# value at lam = 0 is 0 on both sides, so (5) follows.
# closed form of the t-integral in (9), checked numerically (the symbolic integral is slow and returns a Piecewise):
# int_0^inf e^-t t^(-1-alpha) [t + 4^(b/2) Gamma(1+b/2) t^(1+b/2)/(1+b/2)] dt
#   = Gamma(1-alpha) + 4^(b/2) Gamma(1+b/2) Gamma(1+b/2-alpha)/(1+b/2)
worst9 = mp.mpf(0)
for a_m in [mp.mpf("0.05"), mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.75"), mp.mpf("0.95")]:
    for b_m in [mp.mpf("0.3"), mp.mpf("1.447611231"), mp.mpf("4.790444924"), mp.mpf(7)]:
        num = qsub(lambda s: mp.exp(-s) * s ** (-1 - a_m) * (s + 4 ** (b_m / 2) * mp.gamma(1 + b_m / 2) * s ** (1 + b_m / 2) / (1 + b_m / 2)), a_m)
        cf = mp.gamma(1 - a_m) + 4 ** (b_m / 2) * mp.gamma(1 + b_m / 2) * mp.gamma(1 + b_m / 2 - a_m) / (1 + b_m / 2)
        worst9 = max(worst9, abs(num / cf - 1))
print("A1 t-integral in (9) against the printed bracket at 20 points: max relative error", mp.nstr(worst9, 5))

# ---------------------------------------------------------------- A2
worst = mp.mpf(0)
for a_ in ["0.1", "0.276194", "0.5", "0.9"]:
    a_ = mp.mpf(a_)
    for l_ in ["0.3", "1", "10", "1000"]:
        l_ = mp.mpf(l_)
        val = a_ / mp.gamma(1 - a_) * qsub(lambda s: mp.exp(-s) * (-mp.expm1(-l_ * s)) * s ** (-1 - a_), a_, [1 / l_])
        worst = max(worst, abs(val - ((1 + l_) ** a_ - 1)) / ((1 + l_) ** a_ - 1))
print("A2 (5) at 16 sample points: max relative error", mp.nstr(worst, 5))
worst = mp.mpf(0)
for b_ in ["0.5", "1.552389", "2.7", "5"]:
    b_ = mp.mpf(b_)
    for t_ in ["0.01", "1", "7"]:
        t_ = mp.mpf(t_)
        mom = mp.quad(lambda r: r ** b_ * mp.exp(-r * r / (4 * t_)) / (4 * mp.pi * t_) * 2 * mp.pi * r, [0, mp.sqrt(t_), mp.inf])
        worst = max(worst, abs(mom / ((4 * t_) ** (b_ / 2) * mp.gamma(1 + b_ / 2)) - 1))
print("A2 Gaussian radial moment at 12 points: max relative error", mp.nstr(worst, 5))
# the elementary inequality (1+u)^q <= 2^max(q-1,0)(1+u^q), q = b/2
worst = -1.0
for q in [0.25, 0.5, 0.776, 1.0, 1.35, 2.5]:
    u = np.logspace(-6, 6, 2001)
    worst = max(worst, float(np.max((1 + u) ** q / (2 ** max(q - 1, 0) * (1 + u ** q)))))
print("A2 max of (1+u)^q / (2^max(q-1,0)(1+u^q)) on samples:", round(worst, 12), "(must be <= 1)")

# ---------------------------------------------------------------- A3
c_val = 4076476460239181 / 2 ** 51
gam = 1 / c_val


def heat_radial(fun, r, tau):
    """exp(tau Delta) fun at radius r, fun radial; kernel (1/(2 tau)) exp(-(r-rho)^2/(4 tau)) i0e(r rho/(2 tau)) rho."""
    sd = math.sqrt(2 * tau)
    lo = max(0.0, r - 40 * sd)
    hi = r + 40 * sd
    pts = [p for p in (r - 5 * sd, r, r + 5 * sd) if lo < p < hi]

    def ker(rho):
        return (1 / (2 * tau)) * math.exp(-(r - rho) ** 2 / (4 * tau)) * special.i0e(r * rho / (2 * tau)) * rho * fun(rho)

    v, _ = integrate.quad(ker, lo, hi, points=pts or None, limit=400, epsabs=0, epsrel=1e-11)
    return v


def a3_case(e, s):
    alpha = s / 2
    c_alpha = alpha / math.gamma(1 - alpha)
    lap = lambda rr: e * (1 + rr * rr) ** (e / 2 - 2) * (2 + e * rr * rr)
    beta = e - 2
    bb = abs(beta)
    C_b = 2 ** (bb / 2 + max(bb / 2 - 1, 0))
    M = max(abs(lap(rr)) / (1 + rr * rr) ** (beta / 2) for rr in np.linspace(0, 1e4, 200001))
    bound = M * C_b * c_alpha * (math.gamma(1 - alpha) + 4 ** (bb / 2) * math.gamma(1 + bb / 2) * math.gamma(1 + bb / 2 - alpha) / (1 + bb / 2))
    rows = []
    for r in [3.0, 10.0, 30.0, 100.0]:
        wgt = lambda tau: float(mp.gammainc(-alpha, tau))
        integrand = lambda tau: heat_radial(lap, r, tau) * wgt(tau)
        v1, _ = integrate.quad(integrand, 0, 1, limit=200, epsabs=0, epsrel=1e-9)
        v2, _ = integrate.quad(integrand, 1, 60, limit=200, epsabs=0, epsrel=1e-9)
        val = -c_alpha * (v1 + v2)
        jr = (1 + r * r) ** (beta / 2)
        rows.append((r, val / jr, bound))
    return alpha, rows


for e, s in [(gam, 1.0), (gam, 0.5), (gam - 2.0, 1.0), (-2.790444924, 1.5)]:
    alpha, rows = a3_case(e, s)
    print(f"A3 g = <X>^e, e = {e:.9f}, s = {s}: expected limit -alpha e^2 = {-alpha * e * e:.9f}")
    for r, ratio, bound in rows:
        print(f"    r = {r:6.1f}: <X>^(2-e)(J^s g - g) = {ratio:.9f}   bound (9) coefficient = {bound:.6f}   ok = {abs(ratio) <= bound}")

# ---------------------------------------------------------------- B1
x1, x2 = sp.symbols("xi1 xi2", real=True)
n2 = x1 ** 2 + x2 ** 2
Bsym = (x1 - sp.I * x2) ** 2 / n2
U1 = x1 * x2 / n2          # -R1 R2, with R_j symbol -i xi_j/|xi| (the product does not depend on the sign convention)
U2 = -x1 ** 2 / n2         # R1^2
print("B1 U2 + i U1 + (1 + B)/2 =", sp.simplify(U2 + sp.I * U1 + (1 + Bsym) / 2))
print("B1 R1^2 - (-1/2 + (R1^2 - R2^2)/2) =", sp.simplify(U2 - (-sp.Rational(1, 2) + (U2 - (-x2 ** 2 / n2)) / 2)))
print("B1 B(-xi) - B(xi) =", sp.simplify(Bsym.subs({x1: -x1, x2: -x2}, simultaneous=True) - Bsym))
pp = sp.symbols("p", positive=True)
print("B1 (1 + (2+p)/(2-p))/2 - 2/(2-p) =", sp.simplify((1 + (2 + pp) / (2 - pp)) / 2 - 2 / (2 - pp)))
print("B1 (1 + (1+p)/(1-p))/2 - 1/(1-p) =", sp.simplify((1 + (1 + pp) / (1 - pp)) / 2 - 1 / (1 - pp)))
# pointwise coefficients of (7)-(9): treat |H|^2 integrals with weight functions and Re int H' conj H = 0
n_, a_, p_ = sp.symbols("n a p", positive=True)
# ||F||^2 = ||D||^2 + (n-a) int (n+a-2p)|H|^2 ; ||G||^2 - ||F||^2 = 4 n int p |H|^2
K2n = ((n_ + a_) / (n_ - a_)) ** 2
lhs9 = (K2n - 1) * (sp.Symbol("D2") + (n_ - a_) * (n_ + a_ - 2 * p_)) - 4 * n_ * p_
rhs9 = 4 * n_ * a_ / (n_ - a_) ** 2 * (sp.Symbol("D2") + (n_ ** 2 - a_ ** 2) / a_ * (a_ - p_))
print("B1 identity (9) of T4-054 (pointwise coefficient form), difference:", sp.simplify(lhs9 - rhs9))

# ---------------------------------------------------------------- B2
X, Y = sp.symbols("x y", real=True)
r_, th = sp.symbols("r theta", positive=True)
K2 = (X ** 2 - Y ** 2) / (2 * sp.pi * (X ** 2 + Y ** 2) ** 2)
dy = sp.diff(K2, Y).subs({X: r_ * sp.cos(th), Y: r_ * sp.sin(th)})
print("B2 -d_y K2 - sin(3 theta)/(pi r^3) =", sp.simplify(sp.expand_trig(-dy - sp.sin(3 * th) / (sp.pi * r_ ** 3))))
dx = sp.diff(K2, X).subs({X: r_ * sp.cos(th), Y: r_ * sp.sin(th)})
print("B2 (x moment would give) -d_x K2 =", sp.simplify(sp.expand_trig(-dx)))

# ---------------------------------------------------------------- B3
eta = lambda rr: (1 - rr * rr) ** 4 if rr < 1 else 0.0
Mdip = math.pi * integrate.quad(lambda rr: rr ** 3 * eta(rr), 0, 1)[0]
Mmono = 2 * math.pi * integrate.quad(lambda rr: rr * eta(rr), 0, 1)[0]


def u2_at(Xx, Xy, kind):
    def f(th_, rr):
        yx, yy = rr * math.cos(th_), rr * math.sin(th_)
        dxx, dyy = Xx - yx, Xy - yy
        k = (dxx * dxx - dyy * dyy) / (2 * math.pi * (dxx * dxx + dyy * dyy) ** 2)
        src = yy * eta(rr) if kind == "dip" else eta(rr)
        return k * src * rr
    v, _ = integrate.dblquad(f, 0, 1, 0, 2 * math.pi, epsabs=1e-14, epsrel=1e-10)
    return v


for th0 in [0.3, 1.1]:
    for R in [4.0, 8.0, 16.0, 32.0]:
        Xx, Xy = R * math.cos(th0), R * math.sin(th0)
        vd = u2_at(Xx, Xy, "dip")
        pred = Mdip * math.sin(3 * th0) / (math.pi * R ** 3)
        vm = u2_at(Xx, Xy, "mono")
        predm = Mmono * math.cos(2 * th0) / (2 * math.pi * R ** 2)
        print(f"B3 theta = {th0}, r = {R:5.1f}: S1 dipole U2/pred = {vd / pred:.10f}; radial monopole U2/pred = {vm / predm:.10f}")

print(f"EXIT 0 elapsed {time.time() - T0:.1f} s")
sys.exit(0)
