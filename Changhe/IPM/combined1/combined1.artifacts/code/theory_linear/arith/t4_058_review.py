"""Independent review of T4-058 (c1-t4 research/dyadic_weighted_closure/PROOF.md, sha256 906111ef...d365): the dyadic
density-velocity space Y, the conditional closure theorem under (H), the fixed-scale counterexample, and the closure
consequences for the current candidates (reviews/REVIEW_T4_058.md).

Run from artifacts/:  python3 -B arith/t4_058_review.py
Needs sympy, mpmath, python-flint.  About half a minute.

Inputs (copies inside artifacts/data):
  a2_state131_farfield.json  = R6/source/analysis2/IPM_Analysis_II.artifacts/numerics/data/state131_farfield.json
                               (sha256 b340c06531f1...e09e14b), the exact far-field
                               sector series of state 131 (residual sectors E_(h,q), h <= 7, q <= 3);
  t4_017_cartesian_witnesses.json (N4 Cartesian intervals, sha256 4596e2d6...407a7e), the d2 point field at (0, 1).

Parts:
  (1) exact (sympy): the Sobolev point constants (3); the Peetre inequality of Section 6; c[g] = 1 for g = -4 y eta(r)
      (Fourier, Gaussian eta) and the sin(3 theta) r^-3 strain kernel; the y-linear coefficient (14) with S1 parity; the
      weighted transport identity behind (10) and behind Lemma B; the dyadic exponent bookkeeping of Lemma Y1;
  (2) exact (sympy) and mpmath: the transport-only model counterexample to (H);
  (3) arb: state 131 windows, Lemma B, the radius ceilings, the T4-022 instance, the origin packet rates (HEURISTIC);
  (4) FLOAT (leading far-field sectors, truncated expansion): lower estimates of Y(F) for state 131 and M ceilings;
  (5) arb: the d2 point lower bound on Y(F).
"""
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]


def A(x):
    x = Q(x)
    return arb(x.numerator) / x.denominator


def f8(x, n=10):
    return x.str(n, radius=False)


# =============================== (1) exact checks ===============================
s, t = sp.symbols("s t", positive=True)
C0sq = sp.simplify(sp.pi * sp.integrate((1 + t) ** (-2 - s), (t, 0, sp.oo)) / (4 * sp.pi**2))
# Frobenius gradient: (2 pi)^-2 int |xi|^2 (1+|xi|^2)^(-2-s) dxi = (2 pi)^-2 pi int_0^oo t (1+t)^(-2-s) dt
C1sq = sp.simplify(sp.pi * sp.integrate(t * (1 + t) ** (-2 - s), (t, 0, sp.oo)) / (4 * sp.pi**2))
print("(1a) C0^2 =", C0sq, "; C1^2 (Frobenius) =", C1sq)
assert sp.simplify(C0sq - 1 / (4 * sp.pi * (1 + s))) == 0
assert sp.simplify(C1sq - 1 / (4 * sp.pi * s * (1 + s))) == 0
assert sp.simplify(sp.integrate((1 + t) ** (-2 - s), (t, 0, sp.oo)) - 1 / (1 + s)) == 0
print("     C1 is decreasing in s, C1 -> (8 pi)^(-1/2) as s -> 1; C0/C1 = sqrt(s)")

x, y, X1, X2 = sp.symbols("x y X1 X2", real=True)
lhs = 2 * (1 + X1**2 + X2**2) * (1 + x**2 + y**2) - (1 + (X1 - x) ** 2 + (X2 - y) ** 2)
rhs = 1 + (X1 + x) ** 2 + (X2 + y) ** 2 + 2 * (X1**2 + X2**2) * (x**2 + y**2)
assert sp.expand(lhs - rhs) == 0
print("(1b) 2<Z>^2<X>^2 - <Z-X>^2 = 1 + |Z+X|^2 + 2|Z|^2|X|^2 >= 0, so <P>^a <X+P>^-a <= 2^(a/2) <X>^a (Peetre)")

# c[h] = d_y U2[h](0) = (2 pi)^-1 int i xi2 (-xi1^2/|xi|^2) hhat(xi) dxi ; g = -4 y eta, ghat = -4 i d_xi2 etahat
xi1, xi2 = sp.symbols("xi1 xi2", real=True)
rho_, th = sp.symbols("rho theta", positive=True)
etahat = sp.exp(-(xi1**2 + xi2**2) / 4) / 2       # unitary 2D transform of exp(-|X|^2)
ghat = -4 * sp.I * sp.diff(etahat, xi2)
integrand = sp.simplify(sp.I * xi2 * (-xi1**2 / (xi1**2 + xi2**2)) * ghat)
pol = sp.simplify(integrand.subs({xi1: rho_ * sp.cos(th), xi2: rho_ * sp.sin(th)}) * rho_)
cg = sp.simplify(sp.integrate(sp.integrate(pol, (th, 0, 2 * sp.pi)), (rho_, 0, sp.oo)) / (2 * sp.pi))
print("(1c) c[-4 y exp(-r^2)] =", cg, "(= eta(0); also = -g_y(0)/4)")
assert cg == 1
r = sp.sqrt(x**2 + y**2)
kern = sp.diff((x**2 - y**2) / r**4, y)
sin3 = (3 * x**2 * y - y**3) / r**3
assert sp.simplify(kern + 2 * sin3 / r**3) == 0
print("     d_y[cos(2 theta)/r^2] = -2 sin(3 theta)/r^3: the strain kernel away from 0 is a multiple of sin(3 theta) r^-3,"
      " so c[h_R] = O(R^(a-3)) for the packets (16)")

# (14): first-order jets with S1 parity.  h, k, rho in S1 (even x, odd y); velocities: first component odd x even y,
# second even x odd y.  Linear jets: h = hy*y, U[h] = (-ch*x, ch*y) (divergence free), U[k] = (-ck*x, ck*y),
# u = (-du*x, du*y), V = c X + u, D rho(0) = (0, a0).
c, a0, hy, ch, ck, du = sp.symbols("c a0 h_y c_h c_k d_u", real=True)
hlin = hy * y
Uh = (-ch * x, ch * y)
Uk = (-ck * x, ck * y)
V = (c * x - du * x, c * y + du * y)
Dh = (sp.diff(hlin, x), sp.diff(hlin, y))
Akh = V[0] * Dh[0] + V[1] * Dh[1] - hlin + Uh[0] * 0 + Uh[1] * a0 + Uk[0] * Dh[0] + Uk[1] * Dh[1]
coef_y = sp.expand(Akh).coeff(y)
coef_x = sp.expand(Akh).coeff(x)
print("(1d) y-coefficient of A_k h at 0:", sp.factor(coef_y - a0 * ch), "* h_y + a0 c[h];  x-coefficient:", coef_x)
assert sp.simplify(coef_y - ((c + du - 1 + ck) * hy + a0 * ch)) == 0 and coef_x == 0
print("     with (8) c + d_y u2(0) = 1 and c[k] = 0 it equals a0 c[h]; DV(0) = diag(c - d_u, c + d_u) = diag(2c - 1, 1)")
assert sp.simplify((c - du).subs(du, 1 - c) - (2 * c - 1)) == 0

# weighted transport: (1/2) div(V w^2)/w^2 with w = (1 + |X|^2/R^2)^(-a/2), V = cX + grad^perp psi
a, Rw = sp.symbols("a R_w", positive=True)
psi = sp.Function("psi")(x, y)
u1, u2 = -sp.diff(psi, y), sp.diff(psi, x)
w2 = (1 + (x**2 + y**2) / Rw**2) ** (-a)
divVw2 = sp.diff((c * x + u1) * w2, x) + sp.diff((c * y + u2) * w2, y)
target = w2 * (2 * c - 2 * a * ((c * x + u1) * x + (c * y + u2) * y) / (Rw**2 + x**2 + y**2))
assert sp.simplify(divVw2 - target) == 0
print("(1e) div(V w_R^2) = w_R^2 (2c - 2a V.X/(R_w^2 + |X|^2)) for V = cX + grad^perp psi, so")
print("     Re<V.D psi, psi>_(H_a) = -c||psi||^2 + a int psi^2 w^2 V.X/(R_w^2 + |X|^2)   (used in (10) and Lemma B)")
print("     and |W.D log w_R| = a|W.X|/(R_w^2 + |X|^2) <= a C1 R |X|^2/(R_w^2 + |X|^2) < a C1 R for |W| <= C1 R |X|")

j, b = sp.symbols("j b", real=True)
eL2 = sp.simplify(2 * (1 - a) * j - 2 * j + (2 * b + 2) * j)       # 2^(2(1-a)j) ||chi F(2^j .)||^2 with F ~ r^b
eD = sp.simplify(2 * (1 - a) * j + 4 * j - 2 * j + (2 * b - 2) * j)  # Laplacian on the plateau, Delta F ~ r^(b-2)
print("(1f) shell-j exponents of 2: L2 part", sp.factor(eL2), "; Laplacian part", sp.factor(eD),
      "; both = -2(a - 1 - b) j")
assert sp.simplify(eL2 + 2 * (a - 1 - b) * j) == 0 and sp.simplify(eD + 2 * (a - 1 - b) * j) == 0

# =============================== (2) model counterexample ===============================
lam, tt = sp.symbols("lambda t", positive=True)
f = sp.Function("f")
Phi = (sp.exp(lam * tt) * x, sp.exp(tt) * y)
comp = f(*Phi)
lhsm = lam * x * sp.diff(comp, x) + y * sp.diff(comp, y)
assert sp.simplify(lhsm - sp.diff(comp, tt)) == 0
print("(2)  V = (lambda x, y): V.D[f(Phi_t X)] = d/dt f(Phi_t X), so h = -int_0^oo e^-t f(Phi_t X) dt solves"
      " (V.D - 1) h = f")
xi = sp.symbols("xi", positive=True)
chi0 = sp.Function("chi")
expr = -sp.exp(2 * lam * tt) * x**2 * chi0(sp.exp(lam * tt) * x)
sub = sp.simplify(expr.subs(tt, sp.log(xi / x) / lam) * sp.diff(sp.log(xi / x) / lam, xi))
print("     f = x^2 y chi: h_y(x, 0) = -int_0^oo f_y(Phi_t(x,0)) dt = int_x^oo (", sub, ") dxi; h_y(0, y) = 0")
assert sp.simplify(sub + xi * chi0(xi) / lam) == 0
mp.mp.dps = 30
lamv = 2 * mp.mpf(4076476460239181) / mp.mpf(2) ** 51 - 1


def chib(z):
    z = mp.mpf(z)
    return mp.e * mp.exp(-1 / (1 - z * z / 16)) if abs(z) < 4 else mp.mpf(0)


G0 = -mp.quad(lambda z: z * chib(z), [0, 2, 4]) / lamv
for xv in (mp.mpf("1e-2"), mp.mpf("1e-4")):
    T = mp.log(4 / xv) / lamv
    direct = -mp.quad(lambda tv: mp.e ** (2 * lamv * tv) * xv**2 * chib(mp.e ** (lamv * tv) * xv), [0, T / 2, T])
    print(f"     lambda = 2c_l - 1 = {mp.nstr(lamv, 10)}, x = {mp.nstr(xv, 3)}: h_y(x, 0) = {mp.nstr(direct, 12)}"
          f" (limit -(1/lambda) int_0^oo xi chi = {mp.nstr(G0, 12)})")
    assert abs(direct - G0) < mp.mpf("1e-3")
print("     so h_y is discontinuous at 0 and h is not C^1: (H) fails for the transport-only model (no coupling);"
      " the low inverse is this integral for a < (lambda + 3)/(2 lambda)")
print("     packet rates without coupling at 0: e1:", sp.expand((2 + s) * (2 * c - 1) - c - 1), "> 0 for c > 1")

# =============================== (3) state 131 windows, Lemma B, radius ceilings ===============================
cl = A(Q(4076476460239181, 2**51))
bexp = Q(427123167131315, 4076476460239181)
assert Q(2**52, 4076476460239181) - 1 == bexp
bA = A(bexp)
a0v = A(Q(12102479225522702540364244077864789, 1174964343508337542719888806641664))
beta0 = A(Q(204956566601, 10**11))   # REVIEW_T4_022 item 8: beta0 = 2.04956566601... (only the window edge uses it)
pi = arb.pi()
print("(3a) state 131: c_l =", f8(cl, 15), " b = 2/c - 1 =", f8(bA, 12), " a0 =", f8(a0v, 14))
print("     membership and profile window 2/c < a < 1 + 1/c: (", f8(2 / cl, 9), ",", f8(1 + 1 / cl, 9), ")")
print("     T4-022 energy method needs c a < beta0: a <", f8(beta0 / cl, 9), "; there beta <= beta0 - c a < beta0 - 2 =",
      f8(beta0 - 2, 6))


def C1f(sv):
    return 1 / (4 * pi * sv * (1 + sv)).sqrt()


def bmax(av):
    return 1 + cl - cl * av


def Runiv(av):   # Lemma B, C_U >= 1, C1 > (8 pi)^(-1/2)
    return (8 * pi).sqrt() * bmax(av) / (1 + av)


def Ravail(av):  # Lemma B, C_U = 2/(2 - a) (T4-054), s < c - 1 (origin condition, HEURISTIC for (H))
    return bmax(av) / (C1f(cl - 1) * (2 / (2 - av) + av))


aT = A(Q(221, 200))
CU = 2 / (2 - aT)
bT = A(Q(2181481, 10**8))
R_half = bT / (C1f(A(Q(1, 2))) * (CU + aT))
R_sup = bT * (8 * pi).sqrt() / (CU + aT)
print("(3b) closure (12) <=> M Y(F) <= R < min(beta/(C1 (C_U + a)), a0/C1); eta_max = Y(F)_max = that min / M")
print("     T4-022 instance (a = 221/200, d = 4/9, R_w = 2^29, beta > 0.02181481), C_U = 2/(2-a) =", f8(CU, 8))
print("       R < beta/(C1 (C_U + a)):", f8(R_half, 8), "at s = 1/2;", f8(R_sup, 8), "as s -> 1 (sup over 0 < s < 1)")
YF = A(25963) * A(10**6)   # ||w_R F||_2 >= 2.5963e10 (N4-038, CONFIRMED by T4-032)
print("       Y(F) >= ||w_R F||_2 >= 2.5963e10, so (12) needs M <", (R_sup / YF).str(5))
print("       with any (9) at this a and weight (Lemma B: beta <= 1 + c - c a =", f8(bmax(aT), 8), ") and C_U >= 1: R <",
      f8(Runiv(aT), 6), ", M <", (Runiv(aT) / YF).str(5))
assert R_sup < A(Q(3275, 10**5)) and R_sup / YF < A(Q(127, 10**14)) and Runiv(aT) / YF < A(Q(75, 10**12))
print("       T4-022 method (beta <= beta0 - c a, any a in its window): R < sqrt(8 pi)(beta0 - 2)/(1 + 2/c) =",
      f8((8 * pi).sqrt() * (beta0 - 2) / (1 + 2 / cl), 6))
print("(3c) origin packet rates (principal symbol q xi^T DV(0) xi - c - 1 + kappa, kappa = -a0 xi1^2; HEURISTIC for (H)):")
s_v = cl - 1
s_h = (cl + 1 + a0v) / (2 * cl - 1) - 2
print("     vertical (e2): q - c - 1 < 0 <=> s <", f8(s_v, 9), "(the T4-060 energy condition beta <= c + 1 - q)")
print("     horizontal (e1): q(2c-1) - c - 1 - a0 < 0 <=> s <", f8(s_h, 9), "; rate at s = 1/2:",
      f8((2 + A(Q(1, 2))) * (2 * cl - 1) - cl - 1 - a0v, 8))
print("     without coupling the e1 rate is 3c - 3 + s(2c - 1) =", f8(3 * cl - 3, 8), "+", f8(2 * cl - 1, 8), "s > 0")
print("     C1 at s = c - 1:", f8(C1f(cl - 1), 8), "; (8 pi)^(-1/2) =", f8(1 / (8 * pi).sqrt(), 8))

# =============================== (4) FLOAT: Y(F) of state 131 from the leading far-field sectors ===============================
ff = json.loads((HERE / "data/a2_state131_farfield.json").read_text())
assert ff["cl"] == "4076476460239181/2251799813685248"
sect = {}
for key, val in ff["residual_sectors_E"].items():
    if not val["series"]:
        continue
    e = Q(val["exponent"])
    co = {int(n): Q(v["exact"]) for n, v in val["series"].items()}
    L2sq = sum(v * v for v in co.values())                         # ||E||^2 / pi (full circle)
    Dsq = sum(((n * n - e * e) * v) ** 2 for n, v in co.items())   # ||e^2 E + E''||^2 / pi
    sect[key] = (e, A(L2sq).sqrt() * pi.sqrt(), A(Dsq).sqrt() * pi.sqrt())
e10, nE, DE = sect["1,0"]
assert e10 == bexp
print("(4a) leading residual sector (1,0) of state 131 (exact A2 series, odd harmonics 1..39): ||E||_(L2(S1)) =",
      f8(nE, 14), "(numerics_v01: 0.1820788910711258)")
assert abs(nE - A(Q(1820788910711258, 10**16))) < A(Q(1, 10**15))
print("     ||b^2 E + E''||_(L2(S1)) =", f8(DE, 12), "; ratio", f8(DE / nE, 8),
      "(the H^2-type weight of the angular profile)")
KL = (A(2) ** (2 * bA + 2) - 1) / (2 * bA + 2)      # int_1^2 r^(2b+1) dr
KD = (1 - A(2) ** (2 * bA - 2)) / (2 - 2 * bA)       # int_1^2 r^(2b-3) dr
print("     plateau integrals int_1^2 r^(2b+1) dr =", f8(KL, 8), ", int_1^2 r^(2b-3) dr =", f8(KD, 8))
# shell lower estimate: ||Delta F||_(shell j) >= ||Delta F_10||_shell - sum_others ||Delta F_hq||_shell (truncated expansion)


def shellD(e, D, jj):   # ||r^(e-2) G||_(L2(2^j < r < 2^(j+1))) with ||G||_(L2(S1)) = D
    ee = 2 * e - 2
    integ = (A(2) ** ((jj + 1) * ee) - A(2) ** (jj * ee)) / ee
    return D * integ.sqrt()


others = [(k, v) for k, v in sect.items() if k != "1,0"]
jstar = None
for jj in range(1, 60):
    lead = shellD(A(e10), DE, jj)
    rest = sum((shellD(A(e), D, jj) for _, (e, _, D) in others), arb(0))
    if jstar is None and rest < lead / 2:
        jstar = jj
        print(f"     from shell j = {jj} (r >= 2^{jj}) the other {len(others)} sectors' Laplacian norms sum to < 1/2 of the (1,0) one"
              f" (ratio {f8(rest / lead, 4)})")
        break
assert jstar is not None


def Ylead(av, j0, which):
    eps = av - 1 - bA
    xg = A(2) ** (-2 * eps)
    geo = xg**j0 / (1 - xg)
    if which == "L2":
        return nE * (KL * geo).sqrt()
    return DE * (KD * geo).sqrt()


print("(4b) FLOAT lower estimates of Y(F) (leading sector only, all shells j >= j0) and the M ceiling of (12):")
print("     a        eps=a-1-b   beta_max   R_univ    R_avail   Y_L2(j>=1) Y_Lap(j>=1) Y_Lap/2(j>=j*)  M_ceil   "
      "1/beta_max  forced Y(h)/R_univ")
grid = [2 / cl + A(Q(1, 10**4)), aT, A(Q(111, 100)), A(Q(112, 100)), beta0 / cl, A(Q(115, 100)), A(Q(12, 10)),
        A(Q(125, 100)), A(Q(13, 10)), A(Q(135, 100)), A(Q(14, 10)), A(Q(145, 100)), A(Q(15, 10)), A(Q(155, 100))]
rows = []
for av in grid:
    eps = av - 1 - bA
    YL, YD1 = Ylead(av, 1, "L2"), Ylead(av, 1, "D")
    YDs = Ylead(av, jstar, "D") / 2
    Mc = Runiv(av) / YDs
    forced = YDs / (cl - 1) / Runiv(av)
    rows.append((av, Mc, 1 / bmax(av), forced))
    print("     " + "   ".join(f"{float(v.mid().str(8, radius=False)):.4g}".ljust(8) for v in
                               (av, eps, bmax(av), Runiv(av), Ravail(av), YL, YD1, YDs, Mc, 1 / bmax(av), forced)))
assert all(Mc < ib for _, Mc, ib, _ in rows) and all(fo > 1 for _, _, _, fo in rows)
print("     every row: M_ceil < 1/beta_max, and the forced far field (h ~ F_10/(c - 1), HEURISTIC) gives Y(h) > R_univ")
# fine scan of the whole window 2/c < a < 1 + 1/c (FLOAT, same conservative estimate)
lo, hi = 2 / cl, 1 + 1 / cl
mx_Mb, mx_M, mn_fo = arb(0), arb(0), arb(10**9)
NS = 2000
for i in range(1, NS):
    av = lo + (hi - lo) * i / NS
    YDs = Ylead(av, jstar, "D") / 2
    Mc = Runiv(av) / YDs
    mx_M = max(mx_M, Mc.mid())
    mx_Mb = max(mx_Mb, (Mc * bmax(av)).mid())
    mn_fo = min(mn_fo, (YDs / (cl - 1) / Runiv(av)).mid())
print(f"     scan of {NS - 1} points in the window: max M_ceil = {f8(mx_M, 5)}, max M_ceil * beta_max = {f8(mx_Mb, 5)},"
      f" min forced Y(h)/R_univ = {f8(mn_fo, 5)}")
assert mx_Mb < A(Q(3, 10)) and mn_fo > 1
# full truncated expansion: ||Delta F||^2 on shells as an exact quadratic form in the 31 sectors (FLOAT: truncation)
keys = sorted(sect)
gco = {}
for key in keys:
    val = ff["residual_sectors_E"][key]
    e = Q(val["exponent"])
    gco[key] = (e, {int(n): (e * e - int(n) ** 2) * Q(v["exact"]) for n, v in val["series"].items()})
gram = {}
for k1 in keys:
    for k2 in keys:
        e1, g1 = gco[k1]
        e2, g2 = gco[k2]
        ip = sum(g1[n] * g2.get(n, 0) for n in g1)
        if ip:
            gram[(k1, k2)] = (e1 + e2, A(ip) * pi)


def Yfull(av, j0):
    tot = arb(0)
    for (_, _), (esum, ip) in gram.items():
        pexp = A(esum) - 2
        xg = A(2) ** (2 - 2 * av + A(esum))
        tot += ip * (A(2) ** pexp - 1) / pexp * xg**j0 / (1 - xg)
    return tot.sqrt()


print("     full truncated expansion (all 31 sectors with cross terms), Laplacian part of Y(F) (FLOAT):")
print("     a        Y_full(j>=1)  Y_full(j>=4)  Y_full(j>=j*)  Y_lead(j>=j*)")
for av in (aT, A(Q(13, 10)), A(Q(15, 10))):
    print("     " + "   ".join(f"{float(v.mid().str(8, radius=False)):.4g}".ljust(11) for v in
                               (av, Yfull(av, 1), Yfull(av, 4), Yfull(av, jstar), Ylead(av, jstar, "D"))))

# =============================== (5) d2 point lower bound ===============================
wit = json.loads((HERE / "data/t4_017_cartesian_witnesses.json").read_text())
row = next(rw for rw in wit["rows"] if rw["candidate"] == "C1-A2-d2")
Fd2 = abs(arb(row["fields"]["residual"]))
Ylow = Fd2 * (4 * pi).sqrt()
print("(5)  d2 at (0, 1): |F| =", f8(Fd2, 10), "; by (4) on chi0 F, Y(F) >= |F(0,1)|/C0(s) >= sqrt(4 pi)|F(0,1)| =",
      Ylow.str(8))
assert Ylow > A(Q(41637, 10**6))
print("     (12) then needs M < R/Y(F) < beta sqrt(s)/(|F(0,1)| (C_U + a)) (point form, C0/C1 = sqrt(s))")
print("done")
