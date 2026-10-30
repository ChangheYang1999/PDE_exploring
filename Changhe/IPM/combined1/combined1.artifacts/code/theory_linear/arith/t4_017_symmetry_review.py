"""Independent review computations for c1-t4 T4-017 (S1 symmetry point constant).

Run from artifacts/:  python3 -B arith/t4_017_symmetry_review.py [data/t4_017_cartesian_witnesses.json]
Needs mpmath and python-flint.  Runtime about a minute.

Part A (FLOAT sanity checks of the analytic steps; not part of any proof):
  A1  C1^2 = (2pi)^-2 int xi_y^2 <xi>^(-4-2s) = 1/(8 pi s (1+s))   (Beta integral, quadrature check)
  A2  (2pi)^-2 int xi_y^2 cos(2 y xi_y) <xi>^(-4-2s) dxi = -G_s''(2y), with G_s'' from the Bessel formula (6)
  A3  sign of G_s''(r) on a grid r in [1, 40] for several s (the proof gives it analytically)
Part B (rigorous, exact rationals and arb balls):
  B1  the rational relaxations of section 4 of the reviewed PROOF.md, rechecked with Fraction
  B2  sup over the scalar-gap family of C1s*r and C0*r, as arb balls, for mu = 3/10 and mu = 297/1000
  B3  the witness gaps of (4) recomputed from the copied N4 triples; residual recomputed from the triple fields
  B4  last mu (step 1/1000) at which each witness still excludes, with the general-mu symmetric test
"""
import json, sys
from fractions import Fraction as Q
import mpmath as mp
from flint import arb, ctx

# ---------------- Part A: FLOAT sanity checks ----------------
mp.mp.dps = 30

def C1sq_quad(s):
    # (2pi)^-2 * pi * int_0^inf rho^3 (1+rho^2)^(-2-s) drho   (angular mean of sin^2 is 1/2, times 2 pi)
    f = lambda r: r**3 * (1 + r**2) ** (-2 - s)
    return mp.quad(f, [0, 1, 10, 100, mp.inf]) * mp.pi / (4 * mp.pi**2)

def Gpp_bessel(s, r):
    # G_s''(r) = (r/2)^s/(4 pi Gamma(2+s)) [r K_(1-s)(r) - K_s(r)]
    return (r / 2) ** s / (4 * mp.pi * mp.gamma(2 + s)) * (r * mp.besselk(1 - s, r) - mp.besselk(s, r))

def G_heat(s, r):
    return mp.quad(lambda t: t**s * mp.exp(-t - r**2 / (4 * t)), [0, 1, 10, mp.inf]) / (4 * mp.pi * mp.gamma(2 + s))

def cos_moment_quad(s, y):
    # (2pi)^-2 int xi_y^2 cos(2 y xi_y) <xi>^(-4-2s) dxi in polar coordinates;
    # angular integral int_0^{2pi} sin^2(th) cos(a sin th) dth = 2 pi (J0(a) - J1(a)/a), a = 2 y rho
    def f(rho):
        a = 2 * y * rho
        ang = 2 * mp.pi * (mp.besselj(0, a) - mp.besselj(1, a) / a) if a != 0 else mp.pi
        return rho**3 * (1 + rho**2) ** (-2 - s) * ang
    val = mp.quadosc(f, [0, mp.inf], omega=2 * y)
    return val / (4 * mp.pi**2)

print("Part A (FLOAT sanity checks)")
for s in [mp.mpf(1) / 4, mp.mpf(1) / 2]:
    q = C1sq_quad(s)
    print(f"  A1 s={float(s):.4g}: quad {mp.nstr(q, 12)}  formula {mp.nstr(1/(8*mp.pi*s*(1+s)), 12)}")
for s, y in [(mp.mpf(1) / 2, mp.mpf(1) / 2), (mp.mpf(1) / 2, mp.mpf(1)), (mp.mpf(1) / 4, mp.mpf(1))]:
    lhs = cos_moment_quad(s, y)
    rhs = -Gpp_bessel(s, 2 * y)
    num = -mp.diff(lambda r: G_heat(s, r), 2 * y, 2)
    print(f"  A2 s={float(s):.4g} y={float(y):.4g}: quad {mp.nstr(lhs, 12)}  -G''(Bessel) {mp.nstr(rhs, 12)}"
          f"  -G''(numdiff) {mp.nstr(num, 12)}")
worst = None
for s in [mp.mpf(2) ** -16, mp.mpf(1) / 1000, mp.mpf(1) / 10, mp.mpf(1) / 4, mp.mpf(1) / 2]:
    vals = [Gpp_bessel(s, 1 + mp.mpf(k) / 20) for k in range(0, 781)]
    m = min(vals)
    worst = m if worst is None or m < worst else worst
    print(f"  A3 s={float(s):.4g}: min over r in [1,40] (step 1/20) of G_s''(r) = {mp.nstr(m, 8)}"
          f"; G_s''(1/2) = {mp.nstr(Gpp_bessel(s, mp.mpf(1)/2), 8)}")

# ---------------- Part B: rigorous ----------------
ctx.prec = 256
print("Part B (exact / arb)")
# B1: relaxations as stated in section 4 of the reviewed proof
assert Q(3, 200) ** 2 / 3 < Q(87, 10000) ** 2          # 3/(200 sqrt 3) < 87/10000
assert Q(1, 6000) ** 2 / 10 < Q(53, 1000000) ** 2      # 1/(6000 sqrt 10) < 53/10^6
assert Q(87, 10000) * Q(53, 1000000) < Q(1, 2000000)
# the step mu^(3/2)/(1800 sqrt 3) at mu = 3/10 equals 1/(6000 sqrt 10): square both sides exactly
assert (Q(3, 10) ** 3) / (1800**2 * 3) == Q(1, 6000) ** 2 / 10
print("  B1 rational relaxations: all exact comparisons pass")

PI = arb.pi()

def family_sups(mu):
    # family: 0 < s < mu/4800, 0 < r < sqrt(s)(mu - 4800 s)/5
    # C1s r < r/(4 sqrt(pi s)) < mu/(20 sqrt pi) (sup approached as s -> 0); C0 r < mu^(3/2)/(1800 sqrt pi)
    mu = arb(mu.numerator) / mu.denominator
    c1r = mu / (20 * PI.sqrt())
    c0r = mu ** arb(1.5) / (1800 * PI.sqrt())
    return c1r, c0r

for mu in [Q(3, 10), Q(297, 1000)]:
    c1r, c0r = family_sups(mu)
    print(f"  B2 mu={mu}: sup C1s r <= {c1r.str(8)}, sup C0 r <= {c0r.str(8)}, product <= {(c1r*c0r).str(6)}")
c1r, c0r = family_sups(Q(3, 10))
assert c1r < arb(87) / 10000 and c0r < arb(53) / 1000000

path = sys.argv[1] if len(sys.argv) > 1 else "data/t4_017_cartesian_witnesses.json"
data = json.load(open(path))
c = arb("1.8103192")  # only for the consistency print of V2 = c y + u2 (state 131 exponent; d2 etc. share it)
for row in data["rows"]:
    f = row["fields"]
    x, y = row["point"]
    assert x == 0 and abs(y) >= Q(1, 2)
    F = abs(arb(f["residual"])); V = arb(f["velocity_norm"]); D = arb(f["gradient_norm"])
    rho = arb(f["rho"]); u2 = arb(f["u2"]); rhoy = arb(f["rho_y"])
    # consistency: at (0,y) u1 = rho_x = 0, so V = (0, V2) and F = V2 rho_y - rho
    Frec = abs(V * rhoy - rho)
    up = arb(87) / 10000 * V + arb(53) / 1000000 * (1 + D) + arb(1) / 2000000
    gap = F - up
    # sharp family version at mu = 297/1000 (sup values instead of rounded constants)
    c1r2, c0r2 = family_sups(Q(297, 1000))
    up2 = c1r2 * V + c0r2 * (1 + D) + c1r2 * c0r2
    print(f"  B3 {row['candidate']} at {row['point']}: |F| = {F.str(10)} (recomputed V2*rho_y-rho: {Frec.str(10)}),"
          f" |V| = {V.str(8)}, |Drho| = {D.str(8)}")
    print(f"      bound (4) = {up.str(10)}, gap = {gap.str(10)}, positive = {bool(gap > 0)};"
          f" sharp mu=297/1000 gap = {(F-up2).str(8)}")
    # B4: last mu (multiple of 1/1000) for which the witness still excludes every positive-gap ball
    last = None
    for k in range(1, 3001):
        mu = Q(k, 1000)
        a, b = family_sups(mu)
        if F - (a * V + b * (1 + D) + a * b) > 0:
            last = mu
        else:
            break
    print(f"      symmetric test excludes every positive-gap ball for all mu <= {last}"
          f" (= {float(last):.3f}; checked in steps of 1/1000)")
print("done")
