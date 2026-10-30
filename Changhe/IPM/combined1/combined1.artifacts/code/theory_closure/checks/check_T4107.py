"""c1-t1 review R1-014 of c1-t4 T4-107 (continuous weighted-Laplacian lower bound for the dyadic norm Y)
and of the uniform d2 cover T4-112 (UNIFORM_COVER.md).

Written from the statements of the targets. Parts:
  A  polar formula Delta(r z^d P(t) sin(n th)) = r^-1 z^d (T_(d,1)^2 P - n^2 P) sin(n th), T_(d,k) as in T4-107 (sympy)
  B  change of variables of (3): direct radial quadrature against the z-integral (mpmath, test components)
  C  plateau algebra: shell exponent 2(1-a)j + 4j - 2j = 2(2-a)j; core and shell weight comparisons (exact)
  D  cover arithmetic from the seven d2 norms (T4-107 values, CONFIRMED by N4 in T4-116), with the values
     rounded down by 1e-20 before use; ceilings with c the binary64 value used by the source
  E  log-convexity exponents and A = 1 + 1/c < 7/4 (exact)
Run: OMP_NUM_THREADS=1 python3 -B check_T4107.py > check_T4107.out
"""
import time
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp

T0 = time.time()
mp.mp.dps = 50
ok_all = True


def report(tag, ok, msg=""):
    global ok_all
    ok_all &= bool(ok)
    print(f"[{tag}] {'OK' if ok else 'FAIL'} {msg}")


# ---------------------------------------------------------------- A
r, th, d, n = sp.symbols("r theta d n", positive=True)
t = r**2 / (1 + r**2)
z = 1 - t
T = sp.symbols("T")
coeffs = sp.symbols("p0:5")
Pt = sum(cf * T**k for k, cf in enumerate(coeffs))


def Td(Pexpr, dd, k):
    return (k - 2 * dd * T) * Pexpr + 2 * T * (1 - T) * sp.diff(Pexpr, T)


K = Td(Td(Pt, d, 1), d, 1) - n**2 * Pt
for nn in (1, 3, 5):
    F = r * z**d * Pt.subs(T, t) * sp.sin(nn * th)
    lap = sp.diff(F, r, 2) + sp.diff(F, r) / r + sp.diff(F, th, 2) / r**2
    rhs = z**d * K.subs({T: t, n: nn}) * sp.sin(nn * th) / r
    diff = sp.simplify(sp.expand((lap - rhs) / (z**d * sp.sin(nn * th))))
    report("A1", diff == 0, f"polar Laplacian formula, generic quartic P, symbolic d, n = {nn}")
# r d_r t = 2 t (1 - t), r d_r z^d = -2 d t z^d
report("A2", sp.simplify(r * sp.diff(t, r) - 2 * t * (1 - t)) == 0, "r d_r t = 2t(1-t)")
report("A3", sp.simplify(r * sp.diff(z**d, r) + 2 * d * t * z**d) == 0, "r d_r z^d = -2 d t z^d")

# ---------------------------------------------------------------- B
# Two components in the same angular mode, K_i = t L_i(t); compare
#   pi int_0^inf (1+r^2)^(2-a) |r^-1 (z^d1 K_1 + z^d2 K_2)|^2 r dr
# with (pi/2) sum_(i,k) int_0^1 z^(d_i+d_k+a-3) (1-z) L_i(1-z) L_k(1-z) dz.
L1 = lambda tt: 1 + 2 * tt - 3 * tt**2
L2 = lambda tt: -mp.mpf(1) / 2 + tt**3
for (dd1, dd2, a) in [(mp.mpf(3) / 2, mp.mpf(2), mp.mpf(1)), (mp.mpf(9) / 4, mp.mpf(5) / 2, mp.mpf(1) / 4),
                      (mp.mpf(2), mp.mpf(13) / 5, mp.mpf(3) / 2)]:
    def integrand_r(rr):
        tt = rr**2 / (1 + rr**2)
        zz = 1 - tt
        val = zz**dd1 * tt * L1(tt) + zz**dd2 * tt * L2(tt)
        return (1 + rr**2) ** (2 - a) * (val / rr) ** 2 * rr

    direct = mp.pi * mp.quad(integrand_r, [0, 1, 10, 100, mp.inf])
    tot = 0
    for (da, La) in ((dd1, L1), (dd2, L2)):
        for (db, Lb) in ((dd1, L1), (dd2, L2)):
            tot += mp.quad(lambda zz: zz ** (da + db + a - 3) * (1 - zz) * La(1 - zz) * Lb(1 - zz), [0, 1])
    viaz = mp.pi / 2 * tot
    report("B1", abs(direct - viaz) < mp.mpf(10) ** -30 * abs(direct),
           f"d = ({mp.nstr(dd1, 4)}, {mp.nstr(dd2, 4)}), a = {mp.nstr(a, 3)}: radial {mp.nstr(direct, 20)} z-form {mp.nstr(viaz, 20)}")

# ---------------------------------------------------------------- C
a_, j_ = sp.symbols("a j", real=True)
expo = 2 * (1 - a_) * j_ + 4 * j_ - 2 * j_  # 2^(2(1-a)j) from (2), 4^(2j) from Delta, 4^(-j) from dX
report("C1", sp.simplify(expo - 2 * (2 - a_) * j_) == 0, "shell exponent 2(1-a)j + 4j - 2j = 2(2-a)j")
# core: r < 2 gives 1 + r^2 < 5; shell j >= 1: r < 2^(j+1) gives 1 + r^2 < 1 + 4^(j+1) <= 5 * 4^j
okC = all(1 + 4 ** (jj + 1) <= 5 * 4**jj for jj in range(1, 200))
report("C2", okC, "1 + 4^(j+1) <= 5*4^j for j = 1..199 (and for all j >= 0, since 1 <= 4^j)")
# hence for 0 < a < 2: 2^(2(2-a)j) = (4^j)^(2-a) >= (5^-1 (1+r^2))^(2-a) on shell j; 1 >= (5^-1 (1+r^2))^(2-a) on r < 2
for aa in (Fr(1, 10), Fr(1), Fr(3, 2), Fr(19, 10)):
    worst = max(((1 + mp.mpf(2) ** (2 * jj + 2)) / (5 * mp.mpf(4) ** jj)) ** (2 - mp.mpf(aa.numerator) / aa.denominator) for jj in range(1, 60))
    report("C3", worst <= 1, f"a = {aa}: max over shells of 5^(a-2)(1+r^2)^(2-a)/2^(2(2-a)j) at the outer edge = {mp.nstr(worst, 12)}")

# ---------------------------------------------------------------- D
c = mp.mpf(4076476460239181) / mp.mpf(2251799813685248)
Nval = {  # T4-107 values (verification/d2_2048.json, 2048-bit balls of radius < 1e-27), CONFIRMED by N4 (T4-116)
    Fr(0): "1161.65961265051177522337874978",
    Fr(1, 4): "392.468789957814782578942883587",
    Fr(1, 2): "142.246591604972905800229631527",
    Fr(3, 4): "54.9396454319633355936054433800",
    Fr(1): "22.6836992643493619141169390081",
    Fr(5, 4): "10.2218155242158799174781951496",
    Fr(3, 2): "5.25474052266154688610110607568",
}
eps = mp.mpf(10) ** -20
Nlo = {k: mp.mpf(v) - eps for k, v in Nval.items()}
Nhi = {k: mp.mpf(v) + eps for k, v in Nval.items()}


def B(aa):
    aa = mp.mpf(aa.numerator) / aa.denominator
    return mp.sqrt(8 * mp.pi) * (1 + c - c * aa) ** 2 / (1 + aa)


mono = all(Nhi[Fr(k + 1, 4)] < Nlo[Fr(k, 4)] for k in range(6))
report("D0", mono, "the seven values decrease in a, as the monotonicity of N requires")
ratios = []
for k in range(6):
    lo, hi = Fr(k, 4), Fr(k + 1, 4)
    lhs = mp.mpf(5) ** ((mp.mpf(lo.numerator) / lo.denominator - 2) / 2) * Nlo[hi]
    rat = lhs / B(lo)
    ratios.append(rat)
    report("D1", rat > 1, f"cell [{lo}, {hi}]: 5^((l-2)/2) N(h) = {mp.nstr(lhs, 15)}  B(l) = {mp.nstr(B(lo), 15)}  ratio {mp.nstr(rat, 15)}")
lb_last = Nlo[Fr(3, 2)] ** 2 / Nhi[Fr(5, 4)]
lhs = mp.mpf(5) ** (-mp.mpf(1) / 4) * lb_last
rat = lhs / B(Fr(3, 2))
ratios.append(rat)
report("D2", rat > 1, f"cell [3/2, 7/4]: N(7/4) >= N(3/2)^2/N(5/4) = {mp.nstr(lb_last, 15)}; 5^(-1/4) * that = {mp.nstr(lhs, 15)}  "
       f"B(3/2) = {mp.nstr(B(Fr(3, 2)), 15)}  ratio {mp.nstr(rat, 15)}")
mn = min(ratios)
report("D3", mn > mp.mpf("1.35446238584"), f"minimum ratio {mp.nstr(mn, 15)} (cell [1/2, 3/4]); T4-112 states > 1.35446238584264")
# Y lower bounds 5^((a-2)/2) N(a) at the grid points versus the ceilings (pointwise view)
for k in range(7):
    aa = Fr(k, 4)
    yl = mp.mpf(5) ** ((mp.mpf(aa.numerator) / aa.denominator - 2) / 2) * Nlo[aa]
    print(f"     a = {aa}: Y(F) >= {mp.nstr(yl, 12)}, ceiling {mp.nstr(B(aa), 12)}")

# ---------------------------------------------------------------- E
report("E1", Fr(2) - Fr(3, 2) == ((Fr(2) - Fr(5, 4)) + (Fr(2) - Fr(7, 4))) / 2,
       "2 - 3/2 is the mean of 2 - 5/4 and 2 - 7/4 (Cauchy-Schwarz with weights (1+r^2)^(3/8), (1+r^2)^(1/8))")
cq = Fr(4076476460239181, 2251799813685248)
A = 1 + 1 / cq
report("E2", A == Fr(6328276273924429, 4076476460239181) and A < Fr(7, 4) and cq > Fr(4, 3),
       f"A = 1 + 1/c = 6328276273924429/4076476460239181 = {float(A):.12f} < 7/4")
# toy check of the log-convexity inequality on a sample measure
f = lambda rr: (1 + rr**2) ** (-mp.mpf(17) / 10) * (1 + mp.sin(rr))
Nt = lambda aa: mp.sqrt(mp.quad(lambda rr: (1 + rr**2) ** (2 - aa) * f(rr) ** 2 * rr, [0, 1, 10, 100, mp.inf]))
report("E3", Nt(mp.mpf(3) / 2) ** 2 <= Nt(mp.mpf(5) / 4) * Nt(mp.mpf(7) / 4),
       f"toy profile: N(3/2)^2 = {mp.nstr(Nt(1.5)**2, 10)} <= N(5/4) N(7/4) = {mp.nstr(Nt(1.25) * Nt(1.75), 10)}")

print(f"ALL {'OK' if ok_all else 'FAIL'}; total time {time.time() - T0:.1f} s")
