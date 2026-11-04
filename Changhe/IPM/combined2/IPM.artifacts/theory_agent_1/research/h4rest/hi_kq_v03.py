# Least HI' cut with the origin lower u_3 >= 2 ||Delta S(0)||_op (numerics_agent_1 NOTES 10:23Z; numerical_audit exchange v761: the symbol
# identity u_3 = m_3(ubar) = m_4(Psi) = 2 m_2(S) for ubar = (-Psi_y, Psi_x), S = Sym D ubar, operator matrix norm,
# nonunitary Fourier convention; CLAIMED there), with numerical_audit's exact origin value ||Delta S(0)||_op >=
# 1899576001577/10^12 (numerical_audit exchange v725; AT2456). Part 1 checks the symbol identity exactly (sympy). Part 2 is the
# program of hi_kq_v02.py with L2 = 2 * 1899576001577/10^12 in place of L, at the R4 version 2 tuples (NEAR_CHECK_v07)
# and the whole-plane matrix lower 704955805507/10^12 (AT2534 to AT2536). Exact rationals for R and L, arb at 256 bits.
# Usage (from the lane root): python3 -B research/h4rest/hi_kq_v03.py > research/h4rest/hi_kq_v03.out
from fractions import Fraction as Fr
import sympy as sp
import flint
# ---- part 1: the symbol identity
z1, z2 = sp.symbols("z1 z2", real=True)
P = sp.Symbol("Psihat")
# ubar = (-Psi_y, Psi_x); d_x -> i z1, d_y -> i z2 on the nonunitary transform
uh = sp.Matrix([-sp.I * z2 * P, sp.I * z1 * P])
Du = sp.Matrix(2, 2, lambda i, j: sp.I * (z1, z2)[j] * uh[i])     # (D ubar)_ij = d_j ubar_i
Sh = sp.simplify((Du + Du.T) / 2)
B = sp.simplify(Sh / P)                                            # real symmetric traceless symbol
assert sp.simplify(B[0, 0] + B[1, 1]) == 0 and sp.simplify(B[0, 1] - B[1, 0]) == 0
assert all(sp.im(sp.expand(x)) == 0 for x in B)
a, b = B[0, 0], B[0, 1]
# eigenvalues of [[a, b], [b, -a]] are +-(a^2 + b^2)^(1/2); the operator norm squared is a^2 + b^2
assert sp.expand(a**2 + b**2 - (z1**2 + z2**2)**2 / 4) == 0
assert sp.expand(sum(sp.conjugate(x / P) * (x / P) for x in uh) - (z1**2 + z2**2)) == 0   # |ubarhat|^2 = |zeta|^2 |Psihat|^2
print("symbol check: Shat = Psihat B(zeta), B real symmetric traceless with ||B||_op = |zeta|^2/2; |ubarhat| = |zeta| |Psihat|")
print("  B =", B.tolist())
print("  so m_2(S) = (1/2) m_4(Psi) = (1/2) m_3(ubar) = u_3/2, and sup ||Delta S||_op <= m_2(S) gives u_3 >= 2 ||Delta S(0)||_op")
# ---- part 2: the least cuts
flint.ctx.prec = 256
arb = flint.arb
c = Fr(4076476460239181, 2251799813685248)
q = Fr(21, 10)
DS0 = Fr(1899576001577, 10**12)                    # numerical_audit exchange v725; AT2456
L1 = Fr(1024389316421, 10**12)                     # numerical_audit exchange v725; AT2457 (axis third derivatives)
L = 2 * DS0
assert L == Fr(3799152003154, 10**12) and L > L1
REG = Fr(704955805507, 10**12)                     # whole-plane matrix lower (AT2534 to AT2536)
CAP = c + 1 - q                                    # ceiling (AT-211); not an attained rate
TUP = {"plan (11/20, 72)": (Fr(11, 20), Fr(154030238822, 10**12)),       # NEAR_CHECK_v04, v07 (R4 v2)
       "fallback (103/200, 68)": (Fr(103, 200), Fr(181864800240, 10**12))}
def A(x): return arb(x.numerator) / x.denominator
def exact(x):  # exact Fraction of an exact arb (midpoint or radius)
    m, e = x.man_exp()
    return Fr(int(m)) * (Fr(2) ** int(e))
def dec12(x):   # directed 12-place lower and upper displays of the ball x
    lo = exact(x.mid()) - exact(x.rad()); hi = exact(x.mid()) + exact(x.rad())
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
print("L = 2 ||Delta S(0)||_op lower =", L, "  (L/L_axis =", "%.9f)" % float(L / L1),
      "  R4 v2 tuples of NEAR_CHECK_v07; eps_rest = 0 inside R")
for name, (b0, e) in TUP.items():
    for rname, beta in (("wholeplane", REG), ("ceiling", CAP)):
        R = beta - b0 - e
        assert R > 0
        for kname, K in (("5q/2", K52), ("q", Kq)):
            cut = (phi * K * A(L) / A(R)).sqrt()
            lo, hi = dec12(cut)
            print("%-22s %-10s R = %-28s K_%-4s least cut in [%s, %s]" % (
                name, rname, (str(R) if rname == "wholeplane" else "%.12e" % float(R)), kname, lo, hi))
            for m in (72, 100, 140, 200, 223, 224, 230, 250, 266, 267, 270, 300):
                ceil = A(R) * m * m / (phi * K)
                excl = bool(ceil < A(L))
                ok = bool(ceil > A(L))
                print("    mu_r %4d  u_3 ceiling %s  %s" % (m, ceil.str(12),
                      "EXCLUDED (ceiling < L)" if excl else ("not excluded (ceiling > L)" if ok else "UNDECIDED")))
