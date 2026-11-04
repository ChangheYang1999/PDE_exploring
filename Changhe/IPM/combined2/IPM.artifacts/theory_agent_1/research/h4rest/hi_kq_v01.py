# Least HI' cut with the T_IS coefficient q in place of 5q/2 (AT-362: "the stronger T_IS kernel coefficient q is
# also valid in place of 5q/2"). Exact rationals for R and L, arb at 256 bits for phi and K.
# Usage (from the lane root): python3 -B research/h4rest/hi_kq_v01.py > research/h4rest/hi_kq_v01.out
from fractions import Fraction as Fr
import flint
flint.ctx.prec = 256
arb = flint.arb
c = Fr(4076476460239181, 2251799813685248)
q = Fr(21, 10)
L = Fr(1024389316421, 10**12)                      # numerical_audit exchange v725; AT2457
REG = Fr(704955805507, 10**12)                     # inner regional lower (AT2386)
CAP = c + 1 - q                                    # ceiling (AT-211); not an attained rate
TUP = {"plan (11/20, 72)": (Fr(11, 20), Fr(154053513894, 10**12)),       # NEAR_CHECK_v05 (R4 v1)
       "fallback (103/200, 68)": (Fr(103, 200), Fr(181888075312, 10**12))}
def A(x): return arb(x.numerator) / x.denominator
def exact(a):  # exact Fraction of an exact arb (midpoint or radius)
    m, e = a.man_exp()
    return Fr(int(m)) * (Fr(2) ** int(e))
def dec12(a):   # directed 12-place lower and upper displays of the ball a
    lo = exact(a.mid()) - exact(a.rad()); hi = exact(a.mid()) + exact(a.rad())
    fl = (lo * 10**12).__floor__(); ce = -((-hi * 10**12).__floor__())
    f = lambda n: "%d.%012d" % divmod(n, 10**12)
    return f(fl), f(ce)
l2 = arb(2).log()
ctr = 4 * ((A(q) * l2).sinh() - A(q) * l2.sinh()) / l2**3
phi = (1 + arb(5).sqrt()) / 2
K52 = ctr + A(5 * q / 2)
Kq = ctr + A(q)
print("c_tr' =", ctr.str(20))
print("K_5q/2 = c_tr' + 5q/2 =", K52.str(20))
print("K_q    = c_tr' + q    =", Kq.str(20))
print("L =", L, "  R4 v1 tuples of NEAR_CHECK_v05; eps_rest = 0 inside R")
for name, (b0, e) in TUP.items():
    for rname, beta in (("regional", REG), ("ceiling", CAP)):
        R = beta - b0 - e
        assert R > 0
        for kname, K in (("5q/2", K52), ("q", Kq)):
            cut = (phi * K * A(L) / A(R)).sqrt()
            lo, hi = dec12(cut)
            print("%-22s %-8s R = %-28s K_%-4s least cut in [%s, %s]" % (
                name, rname, (str(R) if rname == "regional" else "%.12e" % float(R)), kname, lo, hi))
            for m in (72, 100, 110, 117, 118, 120, 140, 200):
                ceil = A(R) * m * m / (phi * K)
                excl = bool(ceil < A(L))
                ok = bool(ceil > A(L))
                print("    mu_r %4d  u_3 ceiling %s  %s" % (m, ceil.str(12),
                      "EXCLUDED (ceiling < L)" if excl else ("not excluded (ceiling > L)" if ok else "UNDECIDED")))
