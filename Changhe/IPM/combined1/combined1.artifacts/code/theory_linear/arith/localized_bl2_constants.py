# Constants for notes/T2_localized_BL2.md (c1-t2).
# Lemma C: for theta_1 with grad theta_1 in L^2, T = sum_j R_j^* theta_1 R_j - theta_1 (R_j with multiplier i xi_j/|xi|)
# is self-adjoint with Fourier kernel (2 pi)^-2 (cos angle(xi, eta) - 1) theta_1^(xi - eta), and
#   ||T||_HS^2 = (2 pi)^-2 I_1 ||grad theta_1||_2^2,  I_1 = int_(R^2) (1 - cos angle(eta + e, eta))^2 d eta.
# In bipolar coordinates with foci 0 and -e (the angle at eta is the bipolar coordinate sigma, a = 1/2),
#   I_1 = int_0^pi (1 + cos t)^2 (sin t - t cos t)/sin(t)^3 dt          (t = pi - sigma)
#       = int_0^(pi/2) [2 cot(u)^2 - 2 u cos(u)/sin(u)^3 + 4 u cot(u)] du  (t = 2u)
#       = pi (2 log 2 - 1/2),
# so ||T||_HS = C_T ||grad theta_1||_2 with C_T = sqrt((4 log 2 - 1)/(8 pi)).
# Run from artifacts/:  python3 -B arith/localized_bl2_constants.py   (about 10 s)
import time
import numpy as np
import sympy as sp
import mpmath as mp
from scipy import integrate
from flint import arb, ctx

T0 = time.monotonic()
# (1) exact antiderivative: G' equals the integrand, G(0+) = 0, G(pi/2) = pi (2 log 2 - 1/2)
u = sp.symbols("u", positive=True)
v = sp.symbols("v", positive=True)
integrand = 2 * sp.cot(u) ** 2 - 2 * u * sp.cos(u) / sp.sin(u) ** 3 + 4 * u * sp.cot(u)
# G = -cot u + u/sin^2 u - 2u + 4u log sin u - 4 int_0^u log sin v dv
Gpart = -sp.cot(u) + u / sp.sin(u) ** 2 - 2 * u + 4 * u * sp.log(sp.sin(u))
assert sp.simplify(sp.diff(Gpart, u) - 4 * sp.log(sp.sin(u)) - integrand) == 0
t = sp.symbols("t", positive=True)
orig = (1 + sp.cos(t)) ** 2 * (sp.sin(t) - t * sp.cos(t)) / sp.sin(t) ** 3
assert sp.simplify(2 * orig.subs(t, 2 * u) - integrand) == 0                 # dt = 2 du
assert sp.limit(Gpart, u, 0, "+") == 0
# Euler's classical integral int_0^(pi/2) log sin v dv = -(pi/2) log 2 (sympy leaves it unevaluated); checked here to
# 50 digits with mpmath
logsin = -sp.pi * sp.log(2) / 2
mp.mp.dps = 50
assert abs(mp.quad(lambda x: mp.log(mp.sin(x)), [0, mp.pi / 2]) + mp.pi * mp.log(2) / 2) < mp.mpf("1e-45")
I1_exact = sp.simplify(Gpart.subs(u, sp.pi / 2) - 4 * logsin)
assert sp.simplify(I1_exact - sp.pi * (2 * sp.log(2) - sp.Rational(1, 2))) == 0
print("(1) sympy: G' = integrand, G(0+) = 0, int_0^(pi/2) log sin = -(pi/2) log 2; I_1 =", I1_exact)
# (2) arb values
ctx.prec = 256
I1a = arb.pi() * (2 * arb(2).log() - arb(1) / 2)
CT = ((4 * arb(2).log() - 1) / (8 * arb.pi())).sqrt()
print("(2) arb: I_1 =", I1a.str(30, radius=True), "; C_T = sqrt((4 log 2 - 1)/(8 pi)) =", CT.str(30, radius=True))
kx = ((arb(2).log() - arb(1) / 2) / (16 * arb.pi())).sqrt()
ky = ((3 * arb(2).log() - 2) / (16 * arb.pi())).sqrt()
print("    for comparison, the kappa coefficients sqrt((log 2 - 1/2)/(16 pi)) =", kx.str(12),
      "and sqrt((3 log 2 - 2)/(16 pi)) =", ky.str(12))
# (3) FLOAT cross-checks: the 1D bipolar form (50 digits) and a 2D polar quadrature of the defining integral
mp.mp.dps = 50


def g1(tt):
    if tt < mp.mpf("1e-8"):
        q = (mp.mpf(1) / 3 - tt**2 / 30 + tt**4 / 840) / (1 - tt**2 / 6 + tt**4 / 120) ** 3
    else:
        q = (mp.sin(tt) - tt * mp.cos(tt)) / mp.sin(tt) ** 3
    return (1 + mp.cos(tt)) ** 2 * q


I1_1d = mp.quad(g1, [0, mp.pi / 4, mp.pi / 2, 3 * mp.pi / 4, mp.pi])
print("(3) bipolar 1D quadrature (mpmath, 50 digits):", mp.nstr(I1_1d, 30), "; difference from the closed form",
      mp.nstr(I1_1d - mp.pi * (2 * mp.log(2) - mp.mpf(1) / 2), 3))


def f2(p, r):
    ex, ey = r * np.cos(p) + 1.0, r * np.sin(p)
    cth = (ex * r * np.cos(p) + ey * r * np.sin(p)) / (np.hypot(ex, ey) * r)
    return (1 - cth) ** 2 * r


tot = 0.0
for a, b in [(0, 0.5), (0.5, 0.9), (0.9, 1.1), (1.1, 2), (2, 10), (10, 100), (100, 1e4)]:
    val, err = integrate.dblquad(f2, a, b, 0, 2 * np.pi, epsabs=1e-11, epsrel=1e-10)
    tot += val
tot += (3 * np.pi / 4) / 4 / (2 * 1e8)          # tail r > 1e4: integrand ~ sin^4/(4 r^4) r
print("    2D polar quadrature of the defining integral (scipy, FLOAT):", repr(tot), "; relative difference",
      f"{abs(tot / float(I1a.mid()) - 1):.1e}")
# (4) HEURISTIC cost model of notes/T2_localized_BL2.md section 6.2: excess of height H, constant in angle, linear
# ramps of log-length S_r at both ends, total log-length S = 2 S_r, radial speed c:
#   tau/H = C_T sqrt(4 pi)/sqrt(S_r),  omega/H ~ G S/c = 2 G S_r/c;  optimum S_r = (C_T sqrt(4 pi)/4 * c/G)^(2/3)
cf = 4076476460239181 / 2**51
ct = float(CT.mid())
a0 = ct * np.sqrt(4 * np.pi)
print(f"(4) cost model (HEURISTIC): tau/H = {a0:.6f}/sqrt(S_r); optimum S_r = ({a0 / 4:.6f} c/G)^(2/3), c = {cf:.10f}")
for G in (1.0, 0.5, 0.2, 0.15, 0.1):
    sr = (a0 / 4 * cf / G) ** (2 / 3)
    f = a0 / np.sqrt(sr) + 2 * G * sr / cf
    print(f"    G = ||grad rho||_inf = {G:4.2f}: best S_r = {sr:.4f}, (tau + omega)/H = {f:.4f}")
print(f"done in {time.monotonic() - T0:.0f} s")
