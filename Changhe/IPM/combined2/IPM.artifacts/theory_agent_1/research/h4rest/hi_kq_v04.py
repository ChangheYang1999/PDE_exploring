# Least HI' cut with the T_IS coefficient q/2 (K_half = c_tr' + q/2; CONFIRMED by theory_audit, AT2565, from the operator
# symbol ||Shat(zeta)||_op = |zeta| |ubarhat(zeta)|/2 of a planar divergence-free ubar, AT2564) and the origin lower
# u_3 >= L2 = 2 * 1899576001577/10^12 (AT2564; numerical_audit exchange v725, AT2456), at the R4 version 2 tuples
# (NEAR_CHECK_v07), the whole-plane matrix lower 704955805507/10^12 (AT2534 to AT2536) and the ceiling c + 1 - q.
# Same arithmetic as hi_kq_v03.py (exact rationals for R and L, arb at 256 bits, directed 12-place displays).
# Usage (from the lane root): python3 -B research/h4rest/hi_kq_v04.py > research/h4rest/hi_kq_v04.out
from fractions import Fraction as Fr
import flint
flint.ctx.prec = 256
arb = flint.arb
c = Fr(4076476460239181, 2251799813685248)
q = Fr(21, 10)
L = 2 * Fr(1899576001577, 10**12)
assert L == Fr(3799152003154, 10**12)
REG = Fr(704955805507, 10**12)
CAP = c + 1 - q
TUP = {"plan (11/20, 72)": (Fr(11, 20), Fr(154030238822, 10**12)),
       "fallback (103/200, 68)": (Fr(103, 200), Fr(181864800240, 10**12))}
def A(x): return arb(x.numerator) / x.denominator
def exact(x):
    m, e = x.man_exp()
    return Fr(int(m)) * (Fr(2) ** int(e))
def dec12(x):
    lo = exact(x.mid()) - exact(x.rad()); hi = exact(x.mid()) + exact(x.rad())
    fl = (lo * 10**12).__floor__(); ce = -((-hi * 10**12).__floor__())
    f = lambda n: "%d.%012d" % divmod(n, 10**12)
    return f(fl), f(ce)
l2 = arb(2).log()
ctr = 4 * ((A(q) * l2).sinh() - A(q) * l2.sinh()) / l2**3
phi = (1 + arb(5).sqrt()) / 2
Kh = ctr + A(q / 2)
print("c_tr' =", ctr.str(20))
print("K_half = c_tr' + q/2 =", Kh.str(20))
print("L2 =", L, "  R4 v2 tuples of NEAR_CHECK_v07; eps_rest = 0 inside R")
for name, (b0, e) in TUP.items():
    for rname, beta in (("wholeplane", REG), ("ceiling", CAP)):
        R = beta - b0 - e
        assert R > 0
        cut = (phi * Kh * A(L) / A(R)).sqrt()
        lo, hi = dec12(cut)
        print("%-22s %-10s R = %-28s K_half least cut in [%s, %s]" % (
            name, rname, (str(R) if rname == "wholeplane" else "%.12e" % float(R)), lo, hi))
        for m in (54, 55, 70, 71, 79, 80, 140, 200, 207, 208, 224, 267):
            ceil = A(R) * m * m / (phi * Kh)
            excl = bool(ceil < A(L)); ok = bool(ceil > A(L))
            print("    mu_r %4d  u_3 ceiling %s  %s" % (m, ceil.str(12),
                  "EXCLUDED (ceiling < L2)" if excl else ("not excluded (ceiling > L2)" if ok else "UNDECIDED")))
