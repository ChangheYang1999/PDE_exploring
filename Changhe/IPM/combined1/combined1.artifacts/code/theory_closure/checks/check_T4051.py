"""Independent check by c1-t1 of c1-t4 T4-051 (review R1-009 in nonlinear_closure/REVIEWS_v05.md).

Target: c1-t4/research/transient_low_closure/PROOF.md (sha256 85a6f3ee...), the closure that replaces the
signed low condition of T4-019 by ||exp(t A_k)||_(L2) <= 2 exp(-t) on the normalized ball
B = {X_s(k) <= R, c[k] = 0}, with s = 2^-17, R = 2^-14, eta = R/12.

Part A (arb, 256 bits; my own code written from the statements of the target): the parameters nu, A_s, B_s, m1,
  q, alpha, m2, u1, v1, k1, the stationary bounds G1, G0, G2 of (10), the inverse constant K_X of (11) evaluated
  at the corner (f2, f1, f0) = (1, 1/128, 1/512) eps as in the target, the contraction 2 c_s R and c_s R.
  Then two sharpenings (not needed for the verdict):
  A2. operator-norm form: the bound of (10)-(11) is linear in (f2, 128 f1, 512 f0), which lies in the unit ball,
      so X_s(h) <= ||N|| X_s(f) with the 3 x 3 nonnegative matrix N; ||N||^2 <= t is certified by positive leading
      minors of t I - N^T N.
  A3. general low inverse constant K_L (b <= K_L f0 instead of 2 f0) and re-optimized rational (s, R): certified
      thresholds eta = R/||N|| and contraction K_L c_s R.
Part B (sympy, exact): the concavity step of (6) and its multiplier; the Fourier integral behind c_s; the Young
  step (9); the quadratic root bound used in (10); the origin identity f_y(0) = a0 c[h] + c[k] h_y(0) for
  S1-parity Taylor polynomials; M1(0) and a0 > c - 11/10 > 7/10.
Part C (FLOAT): the multiplier of (6) on a grid; a sampled run of the triangular comparison system of (8)-(9)
  with a transiently growing low norm, to illustrate the claimed decay rates.

Usage (from artifacts/checks):
  OMP_NUM_THREADS=1 python3 -B check_T4051.py > check_T4051.out
Needs python-flint, sympy, numpy, scipy.
"""
import math

import numpy as np
import sympy as sp
from flint import arb, ctx
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

ctx.prec = 256


def params(s, R):
    """parameters of section 4 of the target, as arb, from rational s, R (arb inputs)"""
    nu = R / s.sqrt()
    As = arb(127) / 50 + arb(653) / 5 * s
    Bs = arb(9) / 5 * (1 + 44 * s)
    m1 = arb(9) / 10 - 4290 * s - arb(13) / 10 * nu
    q = 6 + 1360 * s
    alpha = m1 - s * q
    m2 = arb(1) / 2 - 4708 * s - (As + Bs) * nu
    u1 = arb(347) / 5 + 5440 * s + Bs * nu
    v1 = 10 + 34816 * s
    k1 = u1 + s * v1
    cs = 1 / (4 * arb.pi() * s * (1 + s)).sqrt()
    return dict(nu=nu, As=As, Bs=Bs, m1=m1, q=q, alpha=alpha, m2=m2, u1=u1, v1=v1, k1=k1, cs=cs)


def stationary_matrix(p, s, KL):
    """rows (G2, 128 G1, 512 G0) as linear forms in x = (f2, 128 f1, 512 f0) / eps"""
    al, q, m2, k1, v1 = p["alpha"], p["q"], p["m2"], p["k1"], p["v1"]
    G1 = [arb(0), 1 / (128 * al), q * KL / (512 * al)]                     # a <= (f1 + q K_L f0)/alpha
    G0 = [s * G1[0], s * G1[1], KL / 512 + s * G1[2]]                       # b_s <= K_L f0 + s G1
    rt = (40 / m2).sqrt()
    G2 = [(e + k1 * g) / m2 + rt * g for e, g in zip([arb(1), arb(0), v1 * KL / 512], G1)]
    return [G2, [128 * g for g in G1], [512 * g for g in G0]]


def corner_norm(N):
    v = [N[i][0] + N[i][1] + N[i][2] for i in range(3)]
    return (v[0] ** 2 + v[1] ** 2 + v[2] ** 2).sqrt()


def op_norm_upper(N, rel=1e-9):
    """certified upper bound for ||N||_op: t I - N^T N has positive leading minors at t = (1 + rel) lambda_float"""
    Nf = np.array([[float(x.mid()) for x in row] for row in N])
    lam = float(np.linalg.eigvalsh(Nf.T @ Nf).max())
    t = arb(lam) * (1 + arb(rel))
    G = [[sum(N[k][i] * N[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    M = [[(t if i == j else arb(0)) - G[i][j] for j in range(3)] for i in range(3)]
    d1 = M[0][0]
    d2 = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    d3 = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
          + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    assert d1 > 0 and d2 > 0 and d3 > 0, "op-norm certificate failed"
    return t.sqrt(), math.sqrt(lam)


def fmt(x, n=10):
    return x.str(n, radius=False)


print("=" * 100)
print("Part A. Arb arithmetic (256 bits)")
print("=" * 100)
s0, R0 = arb(1) / 131072, arb(1) / 16384
p = params(s0, R0)
print("A1. target parameters s = 2^-17, R = 2^-14:")
for k in ("nu", "As", "Bs", "m1", "q", "alpha", "m2", "u1", "v1", "k1", "cs"):
    print(f"    {k:>5} = {p[k].str(15)}")
assert p["alpha"] > arb("0.83849") and p["m2"] > arb("0.36814")
N0 = stationary_matrix(p, s0, arb(2))
G2c, G1c, G0c = (N0[0][0] + N0[0][1] + N0[0][2], (N0[1][0] + N0[1][1] + N0[1][2]) / 128,
                 (N0[2][0] + N0[2][1] + N0[2][2]) / 512)
KXc = corner_norm(N0)
print(f"    corner evaluation (target (10)-(11)): G1 = {G1c.str(12)}, G0 = {G0c.str(12)}, G2 = {G2c.str(12)},"
      f" K_X = {KXc.str(15)}")
assert KXc < arb("11.490384") and KXc < 12
contr = 2 * p["cs"] * R0
print(f"    2 c_s R = {contr.str(15)} (< 0.012467: {bool(contr < arb('0.012467'))}); c_s R = {(p['cs'] * R0).str(15)}"
      f" (< 0.006234: {bool(p['cs'] * R0 < arb('0.006234'))}); 12 K_X eta / R = K_X/12 = {(KXc / 12).str(10)} < 1")
assert contr < arb("0.012467") and p["cs"] * R0 < arb("0.006234")
print("    all target inequalities reproduced.")

print()
KXo, KXo_f = op_norm_upper(N0)
print(f"A2. operator-norm form at the target point: ||N|| <= {KXo.str(12)} (float {KXo_f:.10f}) against the corner"
      f" value {KXc.str(10)}; so X_s(F) <= R/{fmt(KXo, 8)} = {fmt(R0 / KXo, 8)} suffices instead of R/12 ="
      f" {fmt(R0 / 12, 8)}.")
print("    Reason: (f2, 128 f1, 512 f0) lies in the closed unit ball when X_s(f) <= 1, and the corner (1, 1, 1) has")
print("    Euclidean length sqrt 3; the bound is monotone in each component, so the sup over the ball is ||N||.")

print()
print("A3. general low inverse constant K_L (hypothesis: ||A_k^-1||_(L2) <= K_L on B), rational (s, R) re-optimized")


def kx_float(ls, lR, KL):
    s, R = 2.0 ** ls, 2.0 ** lR
    nu = R / math.sqrt(s)
    m1 = 0.9 - 4290 * s - 1.3 * nu
    q = 6 + 1360 * s
    al = m1 - s * q
    m2 = 0.5 - 4708 * s - (127 / 50 + 653 / 5 * s + 9 / 5 * (1 + 44 * s)) * nu
    if min(al, m2) <= 0:
        return None
    k1 = 347 / 5 + 5440 * s + 9 / 5 * (1 + 44 * s) * nu + s * (10 + 34816 * s)
    v1 = 10 + 34816 * s
    G1 = np.array([0, 1 / 128, q * KL / 512]) / al
    G0 = np.array([0, 0, KL / 512]) + s * G1
    G2 = (np.array([1, 0, v1 * KL / 512]) + k1 * G1) / m2 + math.sqrt(40 / m2) * G1
    return float(np.linalg.norm(np.vstack([G2, 128 * G1, 512 * G0]), 2))


print("    K_L | 1/sqrt(s) |       R |    nu |    m2 | ||N|| <= | eta = R/||N|| | K_L c_s R | FLOAT optimum eta")
for KL, n_s, R_rat in ((sp.Rational(1, 2), 225, sp.Rational(21, 100000)), (1, 227, sp.Rational(21, 100000)),
                       (2, 228, sp.Rational(21, 100000)), (4, 229, sp.Rational(21, 100000)),
                       (8, 229, sp.Rational(21, 100000)), (16, 229, sp.Rational(21, 100000))):
    obj = lambda x: (-(2.0 ** x[1]) / kx_float(x[0], x[1], float(KL))) if kx_float(x[0], x[1], float(KL)) else 1.0
    res = minimize(obj, [-15.6, -12.2], method="Nelder-Mead", options=dict(xatol=1e-7, fatol=1e-15))
    s_a = arb(1) / (n_s * n_s)
    R_a = arb(int(R_rat.p)) / int(R_rat.q)
    KL_a = arb(int(sp.Rational(KL).p)) / int(sp.Rational(KL).q)
    pp = params(s_a, R_a)
    assert pp["alpha"] > 0 and pp["m2"] > 0
    Nk = stationary_matrix(pp, s_a, KL_a)
    up, _ = op_norm_upper(Nk)
    th = KL_a * pp["cs"] * R_a
    assert th < 1 and pp["cs"] * R_a < arb(7) / 10
    print(f"    {str(KL):>3} | {n_s:>9} | {str(R_rat):>7} | {fmt(pp['nu'], 4):>5} | {fmt(pp['m2'], 4):>5} |"
          f" {fmt(up, 7):>8} | {fmt(R_a / up, 6):>12} | {fmt(th, 5):>9} | {-res.fun:.5e}")
print("    (eta values are certified lower bounds of the admissible X_s(F) threshold at the stated rational point;")
print("     the target's K_L = 2 point gives R/12 = 5.0863e-06. The FLOAT optimum is over (s, R) with K_L c_s R < 1.)")

print()
print("=" * 100)
print("Part B. Exact symbolic checks")
print("=" * 100)
tt, ss = sp.symbols("t s", positive=True)
# (6): for 0 < s <= 1 and t >= 1, t^s - 1 <= s (t - 1): g(t) = s(t-1) - t^s + 1 has g(1) = 0, g' = s(1 - t^(s-1)) >= 0
g = ss * (tt - 1) - tt ** ss + 1
print("B1. (6): g(t) = s(t-1) - t^s + 1: g(1) =", sp.simplify(g.subs(tt, 1)), "; g'(t) =", sp.simplify(sp.diff(g, tt)),
      ">= 0 for t >= 1, 0 < s <= 1; and sqrt(1 + r^2) - 1 <= r since (1 + r)^2 = 1 + 2r + r^2 >= 1 + r^2")
# c_s: int_{R^2} |xi|^2 (1 + |xi|^2)^(-2-s) d xi = pi/(s(1+s)); then ||Dh||_inf <= (2 pi)^-2 int |xi| |h^| <=
#      (2 pi)^-2 (pi/(s(1+s)))^(1/2) (2 pi) ||J^(2+s) h||_2 and ||J^(2+s) h||^2 = b_s^2 + 2 a^2 + ||D^2 J^s h||^2 <= X_s^2
r = sp.symbols("r", positive=True)
s_num = sp.Rational(1, 131072)
I_cs = sp.integrate(2 * sp.pi * r ** 3 * (1 + r ** 2) ** (-2 - ss), (r, 0, sp.oo), conds="none")
print("B2. int |xi|^2 <xi>^(-4-2s) d xi =", sp.simplify(sp.gammasimp(I_cs)), "; claim pi/(s(1+s)); at s = 2^-17 the",
      "difference is", sp.N((I_cs - sp.pi / (ss * (1 + ss))).subs(ss, s_num), 5))
assert abs(sp.N((I_cs - sp.pi / (ss * (1 + ss))).subs(ss, s_num), 30)) < 1e-20
print("    (1/(2 pi)) sqrt(pi/(s(1+s))) = (4 pi s(1+s))^(-1/2) = c_s:",
      sp.simplify(1 / (2 * sp.pi) * sp.sqrt(sp.pi / (ss * (1 + ss))) - (4 * sp.pi * ss * (1 + ss)) ** sp.Rational(-1, 2)) == 0,
      "; <xi>^4 = 1 + 2|xi|^2 + |xi|^4 gives the J^(2+s) split; weights 1 <= 2^18, 2 <= 2^14, omega >= 1")
# (9) Young
P, a, b, m2, k1, v1 = sp.symbols("P a b m2 k1 v1", positive=True)
lhs = -2 * m2 * P ** 2 + 2 * (k1 * a + v1 * b) * P + 80 * a ** 2
rhs = -m2 * P ** 2 + (2 * k1 ** 2 / m2 + 80) * a ** 2 + (2 * v1 ** 2 / m2) * b ** 2
gap = sp.simplify(rhs - lhs - (m2 / 2) * (P - 2 * k1 * a / m2) ** 2 - (m2 / 2) * (P - 2 * v1 * b / m2) ** 2)
print("B3. (9): rhs - lhs = (m2/2)(P - 2 k1 a/m2)^2 + (m2/2)(P - 2 v1 b/m2)^2 + (", gap, ")")
assert gap == 0
# quadratic root: m P^2 <= B P + C with P >= 0 implies P <= (B + sqrt(B^2 + 4 m C))/(2m) <= B/m + sqrt(C/m)
m, Bq, Cq = sp.symbols("m B C", positive=True)
root = (Bq + sp.sqrt(Bq ** 2 + 4 * m * Cq)) / (2 * m)
d = sp.simplify((Bq / m + sp.sqrt(Cq / m)) ** 2 * 4 * m ** 2 - (2 * m * root) ** 2)
print("B4. root bound: (2m(B/m + sqrt(C/m)))^2 - (B + sqrt(B^2 + 4mC))^2 =", sp.factor(sp.expand(d)),
      "; this is >= 0 because (B + 2 sqrt(mC))^2 >= B^2 + 4mC")
# origin identity with S1-parity Taylor polynomials (h even in x, odd in y; U1 odd in x, even in y; U2 even x, odd y)
x, y = sp.symbols("x y", real=True)
cc, a0 = sp.symbols("c a0", positive=True)
H = sp.symbols("h01 h21 h03", real=True)
Rr = sp.symbols("r03 r21", real=True)
Wh = sp.symbols("wh10 wh01 wh30 wh12 wh21 wh03", real=True)
Wk = sp.symbols("wk10 wk01 wk30 wk12 wk21 wk03", real=True)
Uu = sp.symbols("u10 u30 u12 u21 u03", real=True)
h_ = H[0] * y + H[1] * x ** 2 * y + H[2] * y ** 3
rho_ = a0 * y + Rr[0] * y ** 3 + Rr[1] * x ** 2 * y
# u = U[rho]: normalized so that c + d_y u2(0) = 1, divergence free at first order
u1_ = (cc - 1) * x + Uu[1] * x ** 3 + Uu[2] * x * y ** 2
u2_ = (1 - cc) * y + Uu[3] * x ** 2 * y + Uu[4] * y ** 3
W1 = -Wh[1] * x + Wh[2] * x ** 3 + Wh[3] * x * y ** 2      # U[h], divergence free at first order: d_x W1 = -d_y W2
W2 = Wh[1] * y + Wh[4] * x ** 2 * y + Wh[5] * y ** 3       # Wh01 = c[h]
K1 = -Wk[1] * x + Wk[2] * x ** 3 + Wk[3] * x * y ** 2
K2 = Wk[1] * y + Wk[4] * x ** 2 * y + Wk[5] * y ** 3       # Wk01 = c[k]
V1, V2 = cc * x + u1_, cc * y + u2_
Ah = (V1 * sp.diff(h_, x) + V2 * sp.diff(h_, y) - h_ + W1 * sp.diff(rho_, x) + W2 * sp.diff(rho_, y)
      + K1 * sp.diff(h_, x) + K2 * sp.diff(h_, y))
fy0 = sp.expand(sp.diff(Ah, y).subs({x: 0, y: 0}))
print("B5. d_y(A_k h)(0) =", fy0, "; claim a0 c[h] + c[k] h_y(0) = a0 wh01 + wk01 h01:",
      sp.simplify(fy0 - (a0 * Wh[1] + Wk[1] * H[0])) == 0)
assert sp.simplify(fy0 - (a0 * Wh[1] + Wk[1] * H[0])) == 0
Fy0 = sp.expand(sp.diff(V1 * sp.diff(rho_, x) + V2 * sp.diff(rho_, y) - rho_, y).subs({x: 0, y: 0}))
print("    d_y F(0) for F = V.D rho - rho:", Fy0, "(zero by the normalization c + d_y u2(0) = 1)")
assert Fy0 == 0
Du0 = sp.Matrix([[sp.diff(u1_, x), sp.diff(u1_, y)], [sp.diff(u2_, x), sp.diff(u2_, y)]]).subs({x: 0, y: 0})
A0 = sp.Matrix([[a0, 0], [0, 0]])
M10 = sp.eye(2) - (Du0 + Du0.T) / 2 + A0
print("B6. M1(0) = I - sym Du(0) + A(0) =", M10.tolist(), "; M1 >= 9/10 gives a0 >= c - 11/10 > 9/5 - 11/10 = 7/10")
assert sp.simplify(M10 - sp.diag(2 - cc + a0, cc)) == sp.zeros(2)

print()
print("=" * 100)
print("Part C. FLOAT checks (not proofs)")
print("=" * 100)
rr = np.concatenate([np.linspace(1e-6, 10, 200001), np.logspace(1, 12, 20001)])
for sv in (2.0 ** -17, 1 / 1024, 0.3, 1.0):
    ratio = ((1 + rr ** 2) ** (sv / 2) - 1) / (sv * rr)
    print(f"C1. (6) multiplier ((1 + r^2)^(s/2) - 1)/(s r) on r in (0, 1e12], s = {sv:.3e}: max = {ratio.max():.8f} (<= 1)")
    assert ratio.max() <= 1 + 1e-12
# C2. comparison system with a transiently growing low norm b(t) = 2 e^-t sin^2-type profile bounded by 2 e^-t b(0)
pf = params(s0, R0)
al_f, m2_f, q_f, k1_f, v1_f = (float(pf[k].mid()) for k in ("alpha", "m2", "q", "k1", "v1"))


def rhs(t, y):
    av, P2 = y
    bt = 2 * math.exp(-t) * (1 - 0.5 * math.exp(-5 * t))   # starts at 1, rises above 1, then decays
    Pv = math.sqrt(max(P2, 0.0))
    return [-al_f * av + q_f * bt, 2 * (-m2_f * P2 + (k1_f * av + v1_f * bt) * Pv + 40 * av * av)]


sol = solve_ivp(rhs, (0, 60), [1.0, 1.0], rtol=1e-10, atol=1e-14, dense_output=True)
ts = np.array([10.0, 20.0, 40.0, 60.0])
av, P2 = sol.sol(ts)
rate_a = -np.diff(np.log(av)) / np.diff(ts)
rate_P = -np.diff(np.log(np.sqrt(P2))) / np.diff(ts)
print(f"C2. equality case of (8) with b(t) = 2 e^-t (1 - e^(-5t)/2): a(t) at t = 10, 20, 40, 60: {np.array2string(av, precision=4)};"
      f" observed rates {np.array2string(rate_a, precision=4)} (claimed: any rate below min(alpha, 1) = 0.8385)")
print(f"    P(t): {np.array2string(np.sqrt(P2), precision=4)}; observed rates {np.array2string(rate_P, precision=4)}"
      f" (claimed: any rate below min(m2/2, alpha, 1) = {min(m2_f / 2, al_f, 1):.4f}); sup_t P(t) = {np.sqrt(sol.sol(np.linspace(0, 60, 6001))[1]).max():.2f}"
      " (prefactor, not contractive)")
