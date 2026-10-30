"""Independent review of T4-022 (c1-t4 research/weighted_l2_commutator/PROOF.md, sha256 e9e72abe...c2aed).

Run from artifacts/:  python3 -B arith/t4_022_review.py [--no-float]
Needs python-flint, sympy, numpy.  Under a minute with the FLOAT part.

Rigorous part (exact rationals, sympy, arb at 256 bits):
  (1) the Beurling identity U2 + i U1 = -(I + B)/2 at the symbol level (sympy, exact), B = D_-/D_+;
  (2) the radial Volterra symbols of B on mode n (sympy): unimodular, -(n + i tau)/(n - i tau) for n > 0;
  (3) M_d at d = 4/9 (M_d^9 = 4 7^7/9^9 exactly), the kernel L1 norms P_n, D_n by exact integration (sympy),
      C(a, d) < 1.038258 and the improved real-pair constant with D_(-4) in the pairs m >= 3;
  (4) beta0 = c + 1 - theta - kappa from the exact T4-018 rationals (data/t4_018_state131_reproduction.json,
      sha256 515b7df5..., copied from c1-t4 research/background_norm_reproduction/verification/reproduction.json),
      beta_R > 0.02181481, membership 2/c < a < 1 + 1/c, perturbed rate and contraction display of section 7;
  (5) the forced radius: beta_R > 0 needs R > R_min(a) = (L(a, d)/(beta0 - c a))^(1/d), with L = C_rho C(a,d) + a C_u M_d.
FLOAT part:
  (6) exact block norms (SVD of the discretized log-variable operators, R = 1) against P_n, D_n, and the FLOAT real-pair
      constant against C(a, d);
  (7) 2D FFT check of the Volterra formulas for m = 3, 1, -1 and of inequality (1) on a real centrally odd test function.
"""
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]


def A(x):
    x = Q(x)
    return arb(x.numerator) / x.denominator


# ---------------- (1) symbol identity ----------------
x1, x2 = sp.symbols("xi1 xi2", real=True, nonzero=True)
nrm2 = x1**2 + x2**2
Rj = [sp.I * x1 / sp.sqrt(nrm2), sp.I * x2 / sp.sqrt(nrm2)]          # R_j multiplier i xi_j/|xi| (A2 P7.2)
U1 = sp.simplify(-Rj[0] * Rj[1])
U2 = sp.simplify(Rj[0] ** 2)
Dm, Dp = sp.I * (x1 - sp.I * x2), sp.I * (x1 + sp.I * x2)           # D_- = dx - i dy, D_+ = dx + i dy
Bsym = sp.simplify(Dm / Dp)
chk = sp.simplify(U2 + sp.I * U1 + (1 + Bsym) / 2)
print("(1) U1 symbol =", U1, "; U2 symbol =", U2, "; B = D_-/D_+ =", sp.simplify(Bsym * nrm2), "/|xi|^2")
print("    U2 + i U1 + (1 + B)/2 =", chk, " (T4-022 section 2: U2 + i U1 = -(I + B)/2)")
assert chk == 0
# Both symbols U1, U2 are real and even, so U maps real inputs to real outputs: |U2 f + i U1 f| = |U[f]| pointwise.

# ---------------- (2) Volterra symbols in t = log r ----------------
n, tau, v = sp.symbols("n tau v", positive=True)
fwd = 1 - 2 * n * sp.integrate(sp.exp(-n * v) * sp.exp(sp.I * tau * v), (v, 0, sp.oo), conds="none")
bwd = 1 - 2 * n * sp.integrate(sp.exp(-n * v) * sp.exp(-sp.I * tau * v), (v, 0, sp.oo), conds="none")  # n -> -n
print("(2) B on mode n > 0, F = exp(i tau t):", sp.simplify(fwd), "; on mode -n < 0:", sp.simplify(bwd))
assert sp.simplify(sp.Abs(fwd) ** 2 - 1) == 0 and sp.simplify(sp.Abs(bwd) ** 2 - 1) == 0
# radial ODE check of the canonical solutions: g' - n g/r = f
r, s_ = sp.symbols("r s", positive=True)
f = sp.Function("f")
nn = sp.symbols("nn", integer=True)
g_pos = -r**nn * sp.Integral(s_**(-nn) * f(s_), (s_, r, sp.oo))
g_neg = r**nn * sp.Integral(s_**(-nn) * f(s_), (s_, 0, r))
for name, g in (("n>0", g_pos), ("n<0", g_neg)):
    res = sp.simplify(sp.diff(g, r) - nn * g / r - f(r))
    print(f"    canonical solution {name}: g' - n g/r - f =", res)
    assert res == 0

# ---------------- (3) M_d, kernel norms, C(a, d) ----------------
a_q, d_q = Q(221, 200), Q(4, 9)
a, d = A(a_q), A(d_q)
Md = d / 2 * ((2 - d) / d) ** (1 - d / 2)
Md9 = Q(4 * 7**7, 9**9)
print("(3) M_d =", Md.str(15), "; M_d^9 - 4*7^7/9^9 contains 0:", (Md**9 - A(Md9)).contains(0))
assert (Md**9 - A(Md9)).contains(0)
xs = sp.symbols("x", positive=True)
dd = sp.Rational(4, 9)
numer = sp.factor(sp.simplify(sp.diff(xs ** (2 - dd) / (1 + xs**2), xs) * (1 + xs**2) ** 2 / xs ** (1 - dd)))
print("    d/dx [x^(2-d)/(1+x^2)] = x^(1-d) (1+x^2)^-2 *", numer, "; unique positive zero x^2 = (2-d)/d =", (2 - dd) / dd)
assert sp.simplify(numer - ((2 - dd) - dd * xs**2)) == 0
# kernel L1 norms (R = 1, common factor a M_d removed), exact integration
aa, ds, pp = sp.symbols("a d p", positive=True)       # p = n - a - d > 0 in the forward case
nv = pp + aa + ds
Pn = sp.simplify(2 * nv * (sp.integrate(sp.exp(-pp * v), (v, 0, sp.oo)) - sp.integrate(sp.exp(-nv * v), (v, 0, sp.oo)))
                 / (aa + ds))
nb_ = sp.symbols("k", positive=True)                  # k = |n| in the backward case
Dn = sp.simplify(2 * nb_ * (sp.integrate(sp.exp(-nb_ * v), (v, 0, sp.oo)) - sp.integrate(sp.exp(-(nb_ + ds) * v), (v, 0, sp.oo)))
                 / ds)
print("    forward kernel norm / (a M_d R^-d):", sp.factor(Pn), " with p = n - a - d > 0; backward (k = |n|):", sp.factor(Dn))
assert sp.simplify(Pn - 2 / (nv - aa - ds)) == 0 and sp.simplify(Dn - 2 / (nb_ + ds)) == 0
P2 = 2 * a * Md / (2 - a - d)
Dm2 = 2 * a * Md / (2 + d)
Dm4 = 2 * a * Md / (4 + d)
C = a * Md / arb(2).sqrt() * ((2 - a - d) ** -2 + (2 + d) ** -2).sqrt()
C_pair = ((P2**2 + Dm2**2) / 2).sqrt() / 2
Cimp = (arb(1) / 2) * ((P2**2 + Dm4**2) / 2).sqrt()        # pairs m >= 3: P_2 and D_(-4)
Cm1 = (arb(1) / 2) * (Dm2**2 / 2).sqrt()                   # pair m = 1: zero positive block, D_(-2)
print("    P_2 =", P2.str(10), " D_-2 =", Dm2.str(10), " D_-4 =", Dm4.str(10), " (units R^-d)")
print("    C(a,d) =", C.str(12), " = (1/2) sqrt((P_2^2 + D_-2^2)/2):", (C - C_pair).contains(0), "; < 1.038258:",
      C < A(Q(1038258, 10**6)))
assert C < A(Q(1038258, 10**6)) and (C - C_pair).contains(0)
assert a + d < 2 and 2 > a + d  # P_n needs n > a + d for n = 2
print("    improved real-pair constant max((1/2)sqrt(D_-2^2/2), (1/2)sqrt((P_2^2+D_-4^2)/2)) =",
      Cimp.str(12), "(m >= 3), m = 1 pair:", Cm1.str(8))
assert Cimp > Cm1

# ---------------- (4) beta0, beta_R and section 7 ----------------
z = json.loads((HERE / "data/t4_018_state131_reproduction.json").read_text())
rec = next(vv for vv in z.values() if isinstance(vv, dict) and "D_rho_x" in vv)
qx = A(Q(rec["D_rho_x"]["rational_energy_over_pi_half"]))
qy = A(Q(rec["D_rho_y"]["rational_energy_over_pi_half"]))
log2 = arb(2).log()
kappa = (((log2 - A(Q(1, 2))) * qx + (3 * log2 - 2) * qy) / 32).sqrt()
cl = A(Q(4076476460239181, 2**51))
theta = A(Q(1, 20))
beta0 = cl + 1 - theta - kappa
print("(4) kappa(state131) =", kappa.str(12), " (T2 review of T4-019 FLOAT input: 0.7107535441929825)")
print("    beta0 = c + 1 - theta - kappa =", beta0.str(12), " > 2.04956566:", beta0 > A(Q(204956566, 10**8)))
assert beta0 > A(Q(204956566, 10**8))
Crho, Cu = 186, 22
R = arb(2) ** 29
Rmd = R ** (-d)
L_orig = Crho * C + a * Cu * Md
L_imp = Crho * Cimp + a * Cu * Md
betaR = beta0 - cl * a - L_orig * Rmd
betaR_imp = beta0 - cl * a - L_imp * Rmd
print("    c a =", (cl * a).str(12), "; beta0 - c a =", (beta0 - cl * a).str(10))
print("    R^-d at R = 2^29:", Rmd.str(10), "; loss [C_rho C + a C_u M_d] R^-d =", (L_orig * Rmd).str(10))
print("    beta_R =", betaR.str(12), " > 0.02181481:", betaR > A(Q(2181481, 10**8)), "; > 1/50:", betaR > A(Q(1, 50)))
assert betaR > A(Q(2181481, 10**8))
print("    with the improved pair constant: beta_R =", betaR_imp.str(10))
print("    membership: 2/c =", (2 / cl).str(12), " < a = 1.105 < 1 + 1/c =", (1 + 1 / cl).str(8), ":",
      2 / cl < a and a < 1 + 1 / cl, "; margin a - 2/c =", (a - 2 / cl).str(6))
assert 2 / cl < a and a < 1 + 1 / cl
Dg = A(Q(1, 250))
riesz = (1 + arb(2) ** (abs(1 - a) / 2) * (2 + a) / (2 - a)) / 2     # C_2(-a) of A2 P7.2 (2), centrally odd, |beta| < 2
rate = betaR - a * Dg
print("    section 7: C_2(-a) =", riesz.str(10), "; rate beta_R - a D =", rate.str(10), " > 0.01739481:",
      rate > A(Q(1739481, 10**8)), "; contraction C_2 D/rate =", (riesz * Dg / rate).str(10), " < 0.528646:",
      riesz * Dg / rate < A(Q(528646, 10**6)))
assert rate > A(Q(1739481, 10**8)) and riesz * Dg / rate < A(Q(528646, 10**6))
# sufficient upper decay exponent for C_rho, C_u: |D rho| ~ r^(1/c - 1), |u| ~ r^(1/c) at infinity
print("    sup r^d |D rho| < infinity for a profile with |D rho| ~ r^(1/c - 1) needs d <= 1 - 1/c =", (1 - 1 / cl).str(8),
      "(d = 4/9 =", d.str(8), ")")

# ---------------- (5) forced radius ----------------
def Rmin(aa_):
    a_ = A(aa_)
    Cad = a_ * Md / arb(2).sqrt() * ((2 - a_ - d) ** -2 + (2 + d) ** -2).sqrt()
    marg = beta0 - cl * a_
    return (((Crho * Cad + a_ * Cu * Md) / marg) ** (1 / d)), Cad, marg


print("(5) beta_R > 0 needs R > R_min(a) = (L(a,d)/(beta0 - c a))^(1/d), d = 4/9, (C_rho, C_u) = (186, 22):")
for aa_ in (Q(1105, 1000), Q(11049, 10000), Q(1106, 1000), Q(111, 100), Q(112, 100), Q(113, 100)):
    if A(aa_) <= 2 / cl:
        continue
    Rm, Cad, marg = Rmin(aa_)
    print(f"    a = {str(aa_):10s} C(a,d) = {Cad.str(8)}, beta0 - c a = {marg.str(8)}, R_min = {Rm.str(6)}"
          f" = 2^{float((Rm.log() / log2).mid().str(10, radius=False)):.3f}")
Rm, _, _ = Rmin(a_q)
print("    at a = 221/200: R_min =", Rm.str(8), "; 2^29 =", R.str(10))
# On 2/c < a < beta0/c, C(a, d) increases and beta0 - c a decreases in a, so R_min(a) > lim_(a -> 2/c) R_min(a):
a_end = 2 / cl
C_end = a_end * Md / arb(2).sqrt() * ((2 - a_end - d) ** -2 + (2 + d) ** -2).sqrt()
R_inf = ((Crho * C_end + a_end * Cu * Md) / (beta0 - 2)) ** (1 / d)
print("    infimum over all admissible a (a -> 2/c, monotonicity): R_min >", R_inf.str(8),
      f"= 2^{float((R_inf.log() / log2).mid().str(10, radius=False)):.3f}")
assert R_inf > 10**8
# hypothetical upper end: theta = kappa = 0 (beta0 = c + 1), a -> 2/c
marg_best = cl + 1 - 2
Rbest = ((Crho * C + a * Cu * Md) / marg_best) ** (1 / d)
print("    even with theta = kappa = 0 (beta0 = c + 1) and a = 1.105: R_min =", Rbest.str(6))

if "--no-float" in sys.argv:
    print("done (FLOAT checks skipped)")
    sys.exit(0)

# ---------------- (6) FLOAT: true block norms ----------------
import numpy as np

af, df = 221 / 200, 4 / 9
Mdf = float(Md.mid().str(20, radius=False))


def block(nb, h, T):
    t = np.arange(-T, T + h / 2, h)
    w = (1 + np.exp(2 * t)) ** (-af / 2)
    tt, ss = t[:, None], t[None, :]
    if nb > 0:
        K = np.where(ss >= tt, -2 * nb * np.exp(-df * tt) * np.exp(-nb * (ss - tt)) * (w[:, None] / w[None, :] - 1), 0.0)
    else:
        K = np.where(ss <= tt, 2 * nb * np.exp(-df * tt) * np.exp(nb * (tt - ss)) * (w[:, None] / w[None, :] - 1), 0.0)
    return K * h


print("(6) FLOAT block norms of r^-d (w B w^-1 - B) on angular mode n (R = 1), against the Volterra bounds:")
blocks = {}
for (h, T) in ((0.03, 14.0), (0.02, 16.0)):
    for nb in (2, 4, 6, -2, -4, -6):
        K = block(nb, h, T)
        blocks[(nb, h)] = K
        nrm = np.linalg.norm(K, 2)
        bound = 2 * af * Mdf / (nb - af - df) if nb > 0 else 2 * af * Mdf / (abs(nb) + df)
        rows = np.abs(K).sum(1).max()
        cols = np.abs(K).sum(0).max()
        print(f"    h={h}, T={T}: n={nb:+d}: ||block|| = {nrm:.6f}, Schur sqrt(row*col) = {np.sqrt(rows*cols):.6f},"
              f" Volterra bound = {bound:.6f}")
    pairs = []
    for m in (1, 3, 5, 7):
        Kn = np.zeros_like(blocks[(-2, h)]) if m == 1 else blocks[(m - 1, h)] if (m - 1, h) in blocks else None
        Kneg = blocks.get((-m - 1, h))
        if Kn is None or Kneg is None:
            continue
        lam = np.linalg.eigvalsh(Kn.T @ Kn + Kneg.T @ Kneg).max() / 2
        pairs.append((m, np.sqrt(lam) / 2))
    print("    FLOAT real-pair constants (1/2) sqrt(lambda_max(T_(m-1)^T T_(m-1) + T_(-m-1)^T T_(-m-1))/2):",
          ", ".join(f"m={m}: {c:.6f}" for m, c in pairs), f"; C(a,d) = {float(C.mid().str(20, radius=False)):.6f}")
    Ctrue = max(c for _, c in pairs)
    Lf = 186 * Ctrue + af * 22 * Mdf
    b0f = float(beta0.mid().str(20, radius=False)) - float((cl * a).mid().str(20, radius=False))
    print(f"    with the FLOAT constant {Ctrue:.6f}: L = {Lf:.3f} (Volterra: {float(L_orig.mid().str(20, radius=False)):.3f}),"
          f" R_min = {(Lf / b0f) ** (1 / df):.4e} = 2^{np.log2((Lf / b0f) ** (1 / df)):.3f}")

# ---------------- (7) FLOAT: 2D FFT checks ----------------
N, Lb = 1024, 40.0
xg = (np.arange(N) - N // 2) * (2 * Lb / N)
X, Y = np.meshgrid(xg, xg, indexing="ij")
k = 2 * np.pi * np.fft.fftfreq(N, d=2 * Lb / N)
K1, K2 = np.meshgrid(k, k, indexing="ij")
KK = K1**2 + K2**2
KK[0, 0] = 1.0
Bm = (K1 - 1j * K2) ** 2 / KK
Bm[0, 0] = 0.0
rr = np.sqrt(X**2 + Y**2)
Z = X + 1j * Y


def apply(sym, f_):
    return np.fft.ifft2(sym * np.fft.fft2(np.fft.ifftshift(f_)))


def sh(F):
    return np.fft.fftshift(F)


G = np.exp(-rr**2 / 2)
with np.errstate(divide="ignore", invalid="ignore"):
    tests = {
        "m=3 (n=2)": (Z**3 * G, np.conj(Z) * 0 + Z * (rr**2 - 4) * G),
        "m=1 (n=0)": (Z * G, np.conj(Z) * G),
        "m=-1 (n=-2)": (np.conj(Z) * G,
                        np.where(rr > 0, (np.conj(Z) / rr) ** 3 * (rr * G - 4 * rr**-3 * (2 - (rr**2 + 2) * G)), 0)),
    }
mask = (rr < 15) & (rr > 0)
print("(7) FLOAT 2D FFT (N = 1024, box [-40, 40]^2): Volterra formulas of section 2")
for name, (fin, expect) in tests.items():
    out = sh(apply(Bm, fin))
    err = np.abs(out - expect)[mask].max() / np.abs(expect)[mask].max()
    print(f"    {name}: max relative deviation of B f from the formula on 0 < r < 15: {err:.2e}")
# inequality (1) on a real centrally odd (S1) test function
U1s, U2s = K1 * K2 / KK, -K1**2 / KK
U1s[0, 0] = U2s[0, 0] = 0.0
phi = Y * (1 + X**2 - 0.3 * Y**2 + 0.05 * X**2 * Y**2) * np.exp(-rr**2 / 3) + 0.4 * X**2 * Y * np.exp(-((X - 0) ** 2 + (Y - 0) ** 2) / 8)
for Rr in (1.0, 2.0, 4.0):
    w = (1 + rr**2 / Rr**2) ** (-af / 2)
    cm = [sh(apply(S, phi / w)).real * w - sh(apply(S, phi)).real for S in (U1s, U2s)]
    with np.errstate(divide="ignore"):
        rd = np.where(rr > 0, rr**-df, 0.0)
    lhs = np.sqrt(((rd * cm[0]) ** 2 + (rd * cm[1]) ** 2).sum())
    ratio = lhs / np.sqrt((phi**2).sum())
    print(f"    R = {Rr}: ||r^-d (w U[w^-1 phi] - U[phi])|| / ||phi|| = {ratio:.5f}; C(a,d) R^-d = "
          f"{float(C.mid().str(20, radius=False)) * Rr**-df:.5f}")
print("done")
