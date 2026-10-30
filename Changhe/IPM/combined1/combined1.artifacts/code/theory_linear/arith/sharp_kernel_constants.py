"""T2-R2: sharpened kernel constants for A2 P8.1 / P8.4 and the resulting D(b)-type threshold.

Run from artifacts/:  python3 -B arith/sharp_kernel_constants.py
Needs python-flint (rigorous part) and mpmath (FLOAT sanity part).  Runtime under a minute.

Notation (notes/T2_sharp_constants.md):  0 < s <= SMAX = 2^-10,
  M_k(s) = int |z|^k kappa_s = s 2^k Gamma(1+k/2) Gamma((k-s)/2) / (2 Gamma(1-s/2)),
  m1 = sup_{0<s<=SMAX} M_1/s <= (sqrt(pi)/2) Gamma((1-SMAX)/2)   (Gamma decreasing on (0,1], Gamma(1-s/2) >= 1),
  M_2/s = 2,  int |z|^k |D kappa_s| = (k+1) M_(k-1)  (radial decreasing kernel in R^2),
  w1 = ||D omega||_inf = (8 sqrt5/5) 6^(-3/5)  (omega = (1+4r^2)^(2/5); unique critical point r^2 = 5/4),
  int |z| |d_l d_j G_2| <= 3 pi/4 (l = j), 3/2 (l != j);  int |z| G_2 = pi/2  (G_2 = K_0(r)/(2 pi)).
Kernel constants (A2 value in brackets):
  k1u  = m1                         unweighted [J^s,d] / s                         [17]
  k1w  = m1 + 8/5                   weighted [J^s,d], weight on the coefficient    [17]
  cru  = (3/2) m1                   transport Taylor remainder, unweighted         [132, together with 28 U1]
  crw  = (3/2) m1 + 32/15           transport Taylor remainder, weight on D^2 u    [132]
  c8   = 1 + w1 * 3 pi/4            weighted Op(xi_l xi_j/<xi>^2)                  [28]
  dtop = 1 + w1 * pi/2              weighted I - J^-2 (dilation commutator)        [6]
Rough transport (units n E^2/sqrt(s)):
  q  = c_s sqrt(s) <= 1/(2 sqrt(pi))                                              [3/10]
  ps = sqrt(s) * (product constant) = 2^s sqrt(1+s)/(2 sqrt(pi))                  [1]
  Pw = ps (1 + w1 m1 s) + w1 m1 s/(2 sqrt(pi))   weighted product                 [1+44s]
  TW = 1 + 4 w1 m1 s                              weighted T_W factor             [1+142s]
  A' = (4/5) q + q TW + 2 Pw,  B' = (9/5) Pw,  low levels c1 = q + ps.   c_U' = A' + B' (needs A' >= c1).
"""
from fractions import Fraction as Q
from flint import arb, ctx
import mpmath as mp

ctx.prec = 200
PI = arb.pi()
SQPI = PI.sqrt()
SMAX = arb(1) / 1024


def up(x, den=10**6):
    """smallest rational k/den with k/den >= upper endpoint of the arb ball x (rigorous round-up)."""
    u = x.mid() + x.rad()
    k = int(mp.ceil(mp.mpf(u.str(40, radius=False)) * den)) + 1
    assert arb(k) / den > x
    return Q(k, den)


# ---------------- rigorous kernel constants ----------------
m1 = SQPI / 2 * arb.gamma((1 - SMAX) / 2)
w1 = arb(8) * arb(5).sqrt() / 5 * arb(6) ** (arb(-3) / 5)
k1u = m1
k1w = m1 + arb(8) / 5
cru = arb(3) / 2 * m1
crw = arb(3) / 2 * m1 + arb(32) / 15
c8 = 1 + w1 * 3 * PI / 4
dtop = 1 + w1 * PI / 2
print("Kernel constants, valid for 0 < s <= 2^-10 (arb upper bounds):")
for name, v, a2 in [("m1 = sup M1/s", m1, "-"), ("w1 = ||D omega||_inf", w1, "2"), ("k1u", k1u, "17"),
                    ("k1w", k1w, "17"), ("cru", cru, "132"), ("crw", crw, "132"), ("c8", c8, "28"),
                    ("dtop", dtop, "6")]:
    print(f"  {name:22s} {v.str(10)}   (A2: {a2})")

# ---------------- K matrix (A2 P8.4 (4) structure, background caps (1)) ----------------
C, U1, U2, U3, R1, R2, R3, R4 = [arb(x) for x in (2, 6, 24, 160, 22, 32, 80, 2048)]
r2021 = (arb(20) / 21).sqrt()
K = [[arb(0)] * 4 for _ in range(4)]
K[0][0] = dtop * C + c8 * U1 + (crw + 2 * k1w) * U2 + k1w * R2
K[0][1] = k1w * (U3 + 2 * R3) / 128
K[0][2] = k1w * R4 / 512
K[1][1] = C + U1 + (cru + k1u) * U2 + k1u * R2
K[1][2] = k1u * R3 / 4
K[2][2] = C + U1 + cru * U2 + k1u * R2
K[3][2] = r2021 * k1u * (U1 + R1)
K[3][3] = C
A2K = [[4708, 85 / 2, 68, 0], [0, 4290, 340, 0], [0, 0, 3882, 0], [0, 0, 476, 2]]
print("K matrix entries (sharp upper bound / A2 value):")
for i in range(4):
    print("  " + "  ".join(f"{K[i][j].str(6):>22s}/{A2K[i][j]:<6}" for j in range(4)))
rows = [sum(((K[i][j] + K[j][i]) / 2 for j in range(4)), arb(0)) for i in range(4)]
print("  symmetric row sums:", [r.str(8) for r in rows], " (A2: 19053/4, 17925/4, 4324, 240)")
Cbg_ub = max(up(r, 1) for r in rows)  # integer round-up of the largest row sum
print("  C_bg' =", Cbg_ub, "(rigorous integer upper bound of the largest symmetric row sum; A2: 4800)")
import numpy as np
Kf = np.array([[float(K[i][j].mid().str(20, radius=False)) for j in range(4)] for i in range(4)])
print("  FLOAT lambda_max of sym(K): %.3f (row-sum bound used instead)" % max(np.linalg.eigvalsh((Kf + Kf.T) / 2)))
shares = {"dtop C": dtop * C, "c8 U1": c8 * U1, "(crw+2k1w) U2": (crw + 2 * k1w) * U2, "k1w R2": k1w * R2}
print("  K00 composition:", {k: v.str(5) for k, v in shares.items()})

# ---------------- rough transport constant c_U(s) on 0 < s <= 2^-10 ----------------
s = SMAX
q = 1 / (2 * SQPI)
ps = arb(2) ** s * (1 + s).sqrt() / (2 * SQPI)        # increasing in s, so the value at SMAX bounds all s
Pw = ps * (1 + w1 * m1 * s) + w1 * m1 * s / (2 * SQPI)
TW = 1 + 4 * w1 * m1 * s
Ap = arb(4) / 5 * q + q * TW + 2 * Pw
Bp = arb(9) / 5 * Pw
c1 = q + ps
low2 = q + ps / 2
lowH = ps / 2
assert Ap > c1 and c1 > low2 and low2 > lowH
cU = Ap + Bp
cU_ub = up(cU, 100)
print("Rough transport (units n E^2/sqrt(s)), valid for 0 < s <= 2^-10:")
print(f"  q = {q.str(8)}, ps <= {ps.str(8)}, Pw <= {Pw.str(8)}, TW <= {TW.str(8)}")
print(f"  A' <= {Ap.str(8)} (A2 A_s = 127/50+(653/5)s), B' <= {Bp.str(8)} (A2 (9/5)(1+44s)); low levels <= {c1.str(6)}")
print(f"  c_U' = A'+B' <= {cU.str(8)}  -> use c_U' = {cU_ub} (A2: 5)")

# ---------------- closure arithmetic (exact rationals) ----------------
mu0 = Q(297, 1000)
Cb, cu = Q(Cbg_ub), cU_ub
import math
print("Closure (rate mu0 - C_bg' s - c_U' N_s(k)/sqrt(s), mu0 = 297/1000 from T2-R1):")
s_opt = mu0 / (5 * Cb)
eta_opt = (4 / (25 * math.sqrt(5))) * float(mu0) ** 2.5 / (float(cu) * math.sqrt(float(Cb)))
print(f"  optimum (non-dyadic): s = {float(s_opt):.4e}, eta = {eta_opt:.4e}")
# dyadic choice s = 2^-13, sqrt(s) = 1/(64 sqrt 2); rational bounds for sqrt 2
S2LO, S2HI = Q(141421356, 10**8), Q(141421357, 10**8)
sd = Q(1, 2**13)
inv_sqrt_s_hi = 64 * S2HI        # 1/sqrt(s) = 64 sqrt 2
sqrt_s_lo = Q(1, 64) / S2HI
mu = mu0 - Cb * sd
# r near mu sqrt(s)/(2 c_U'); take a 2-digit rational
r_float = float(mu) * float(sqrt_s_lo) / (2 * float(cu))
r = Q(round(r_float * 1e5), 10**5)
beta = mu - cu * r * inv_sqrt_s_hi
beta_lb = Q(math.floor(float(beta) * 1000), 1000)
assert beta_lb <= beta and beta_lb > 0
eta = beta_lb * r
print(f"  s = 2^-13: mu = mu0 - C_bg' s = {mu} = {float(mu):.6f}; r = {r}; rate on ball >= {beta_lb} (exact lower bound {float(beta):.6f})")
print(f"  K_H <= 1/{beta_lb} = {float(1/beta_lb):.4f}; threshold eta = rate_lb * r = {eta} = {float(eta):.6e}")
print(f"  gain over FW-T-TB-rebal-v1 (3/327680): {float(eta / Q(3, 327680)):.2f}; over FW-A2-Db (1/1572864): {float(eta * 1572864):.1f}")
# low contraction: d = c_s r, c_s = 1/(2 sqrt(pi s (1+s))) <= 1/(2 sqrt(pi s)) = 32 sqrt 2/sqrt(pi) < 32*S2HI/(1.7724538)
cs_hi = 32 * S2HI / Q(17724538, 10**7)
d = cs_hi * r
KL = 1 / (Q(19, 5) - d)
print(f"  d = c_s r < {float(d):.5f} < a0 margin; K_L = (19/5 - d)^-1 < {float(KL):.4f}; K_L d < {float(KL*d):.5f} < 1")
print(f"  separate component requirements: P2 <= {float(eta):.3e}, G1 <= {float(eta/128):.3e}, G0 <= {float(eta/512):.3e},"
      f" H <= {float(eta/512/math.sqrt(20/21)):.3e}")
# moment step of P8.4 (7) with delta = s/2
print("  P8.4 (7) moment step: delta = s/2 = 2^-14, p = 4/delta = 2^16, kappa = p + 4; 2 + 3/sqrt(s) =",
      f"{2 + 3*64*math.sqrt(2):.1f} < 2^9")

# T4-017 necessary point test for the new family (general-mu formulas of REVIEW_T4_017.md):
c1r = float(mu0) / (4 * float(cu) * math.sqrt(math.pi))
c0r = float(mu0) ** 1.5 / (3 * float(cu) * math.sqrt(3 * math.pi * float(Cb)))
print(f"  T4-017 family test with (C_bg', c_U') = ({Cb}, {cu}): C1s r < {c1r:.5f}, C0 r < {c0r:.3e}")
for name, F, V, D in [("d2 (0,1)", 0.0117458591, 1.1341455898, 8.3931825906),
                      ("Mpen2 (0,2)", 0.0743611985, 2.5378314572, 6.6694055775),
                      ("b6 (0,1)", 2.9582404428, 1.0801115995, 8.0016081038)]:
    bound = c1r * V + c0r * (1 + D) + c1r * c0r
    print(f"    {name}: |F| = {F:.6f}, bound = {bound:.6f}, excluded = {F > bound} (FLOAT; exact recheck needed if cited)")

# ---------------- FLOAT sanity checks (mpmath; skipped with --no-float) ----------------
import sys
if "--no-float" in sys.argv:
    print("done (FLOAT checks skipped)"); sys.exit(0)
mp.mp.dps = 20
print("FLOAT sanity checks:")
sf = mp.mpf(2) ** -10
nu = 1 + sf / 2
ck = sf / (4 * mp.pi * mp.gamma(1 - sf / 2))
kappa = lambda r: ck * (2 / r) ** nu * mp.besselk(nu, r)          # kappa_s(z), |z| = r
dkappa = lambda r: ck * 2 ** nu * r ** (-nu) * mp.besselk(nu + 1, r)  # |D kappa_s| = -kappa_s'
pts = [0, mp.mpf(10) ** -8, mp.mpf(10) ** -5, 1e-3, 0.1, 1, 5, 20, 60]
Mk_formula = lambda k: sf * 2**k * mp.gamma(1 + mp.mpf(k) / 2) * mp.gamma((k - sf) / 2) / (2 * mp.gamma(1 - sf / 2))
for k in (1, 2, 3):
    val = 2 * mp.pi * mp.quad(lambda r: r ** (k + 1) * kappa(r), pts)
    print(f"  M_{k}/s at s=2^-10: quadrature {mp.nstr(val/sf, 10)}, formula {mp.nstr(Mk_formula(k)/sf, 10)}")
for k in (2, 3):
    val = 2 * mp.pi * mp.quad(lambda r: r ** (k + 1) * dkappa(r), pts)
    print(f"  int |z|^{k} |D kappa|/s: quadrature {mp.nstr(val/sf, 10)}, (k+1) M_(k-1)/s = {mp.nstr((k+1)*Mk_formula(k-1)/sf, 10)}")
Gpp = lambda r: (mp.besselk(0, r) + mp.besselk(1, r) / r) / (2 * mp.pi)
Gp_r = lambda r: -mp.besselk(1, r) / (2 * mp.pi * r)
NTH = 200
def ang(r):
    a, b = Gpp(r), Gp_r(r)
    return 2 * mp.pi * sum(abs(a * mp.cos(mp.pi * (j + mp.mpf(1)/2) / NTH)**2 + b * mp.sin(mp.pi * (j + mp.mpf(1)/2) / NTH)**2)
                           for j in range(NTH)) / NTH
q11 = mp.quad(lambda r: r * r * ang(r), [0, 0.5, 2, 8, 40])
q12 = 2 * mp.quad(lambda r: r * r * (Gpp(r) - Gp_r(r)), [0, 1, 10, 40])
print(f"  int|z||q_11| = {mp.nstr(q11, 8)} (midpoint rule in angle; bound 3pi/4 = {mp.nstr(3*mp.pi/4, 8)}); int|z||q_12| = {mp.nstr(q12, 8)} (= 3/2)")
print(f"  int|z| G_2 = {mp.nstr(mp.quad(lambda r: r*r*mp.besselk(0, r), [0, 1, 10, 50]), 10)} (= pi/2)")
grid = max((16 / mp.mpf(5)) * (k / mp.mpf(1000)) * (1 + 4 * (k / mp.mpf(1000))**2) ** (-mp.mpf(3)/5) for k in range(1, 5000))
print(f"  max_r |omega'(r)| on grid = {mp.nstr(grid, 8)}; w1 = {w1.str(8)}")
print("done")
