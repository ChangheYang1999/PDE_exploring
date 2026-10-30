"""(B-L2) trade-off in the T4-019 / T2-R3 Gram closure (c1-t1, theory_v02 section R).

T4-019 (c1-t4 research/l2_closure/PROOF.md, (7) and (9)) uses (B-L2) only through the L2 rate
beta_L = c + 1 - theta - kappa: Re<A_k h, h> <= -beta_L ||h||^2, and the (3,3) Gram entry w0 (beta_L - mu).
"(B-L2): beta_L >= 2" is the normalization used there.  Here beta_L is kept as a parameter.

Part A (EXACT, rational): the largest mu with G_w(mu) positive definite, by 60-step bisection on the leading
minors, at the two registered weight sets of FW-T-T4L2-sharp-v1 (2^14, 2^18) and FW-T-T4L2-sharpw-v1
(2^15, 2^20).  The printed mu_lo is a certified PD point (lower bound).
Part B (FLOAT): closure arithmetic of T2-R3 at fixed weights and fixed row-sum constant C' (401, 397):
beta = mu0 - C' s - (8/5) r / sqrt(s), eta <= beta r; optimal r = (mu0 - C's) sqrt(s)/3.2 and
s = mu0/(5 C'), giving eta = (mu0 - C's)^2 sqrt(s)/6.4 and G0 <= eta / sqrt(w0).
Part C (EXACT): two certified rational instances at the sharpw weights (beta_L = 7/5 and 1), including the L2
contraction ratio c_s r/beta_L of T4-019 (12) with the L2 inverse norm 1/beta_L in place of 1/2.
Usage (from artifacts/closure_calc):
  OMP_NUM_THREADS=1 python3 -B bl2_trade.py > bl2_trade.out
"""
import math
from fractions import Fraction as Q

C_LO = Q(18103192102, 10 ** 10)  # c, 10 digits (only used for the FLOAT beta_L of the candidates)


def gram(mu, bl, w1, w0):
    return [[Q(1, 2) - mu, Q(-347, 10), Q(-5)],
            [Q(-347, 10), w1 * (Q(9, 10) - mu) - 40, -3 * w1],
            [Q(-5), -3 * w1, w0 * (bl - mu)]]


def pd(M):
    a = M[0][0]
    b = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
         + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    return a > 0 and b > 0 and d > 0


def mu_lo(bl, w1, w0):
    lo, hi = Q(-4), min(Q(1, 2), bl)
    if not pd(gram(lo, bl, w1, w0)):
        return None
    for _ in range(60):
        m = (lo + hi) / 2
        if pd(gram(m, bl, w1, w0)):
            lo = m
        else:
            hi = m
    return lo


WEIGHTS = [("sharp (2^14, 2^18), C' = 401", 2 ** 14, 2 ** 18, 401),
           ("sharpw (2^15, 2^20), C' = 397", 2 ** 15, 2 ** 20, 397)]
BLS = [Q(2), Q(19, 10), Q(9, 5), Q(8, 5), Q(7, 5), Q(6, 5), Q(1), Q(4, 5), Q(3, 5), Q(1, 2), Q(2, 5)]

print("Part A (EXACT). Largest certified PD mu of G_w(mu) as a function of beta_L")
print("Part B (FLOAT). eta and G0 at fixed weights, continuous optimum s = mu/(5C'), r = (mu - C's) sqrt(s)/3.2")
for name, w1, w0, Cp in WEIGHTS:
    print()
    print(name)
    print(f"  {'beta_L':>7} {'mu_lo (exact PD)':>18} {'s':>10} {'eta':>12} {'G0 = eta/sqrt(w0)':>18} {'eta/eta(2)':>10}")
    eta2 = None
    for bl in BLS:
        m = mu_lo(bl, w1, w0)
        if m is None or m <= 0:
            print(f"  {float(bl):7.3f}  no positive Gram rate")
            continue
        assert pd(gram(m, bl, w1, w0))
        mf = float(m)
        s = mf / (5 * Cp)
        base = mf - Cp * s
        eta = base ** 2 * math.sqrt(s) / 6.4
        if eta2 is None:
            eta2 = eta
        print(f"  {float(bl):7.3f} {mf:18.10f} 1/{1 / s:8.0f} {eta:12.4e} {eta / math.sqrt(w0):18.4e} {eta / eta2:10.4f}")
    # smallest beta_L that still gives a positive rate (bisection on beta_L with mu = 0)
    lo, hi = Q(0), Q(2)
    for _ in range(50):
        m = (lo + hi) / 2
        if pd(gram(Q(0), m, w1, w0)):
            hi = m
        else:
            lo = m
    print(f"  smallest beta_L with G_w(0) PD lies in [{float(lo):.8f}, {float(hi):.8f}] (EXACT bracket)")

print()
print("FLOAT beta_L = c + 1 - theta - kappa of the numerics_v02 candidates (theta, kappa from numerics_v02 section 3)")
cf = float(C_LO)
for nm, th, ka in [("005", 0.0471, 1.36), ("006", 9.25, 14.1), ("d2 (theta <= 2/25, kappa = 0.7092)", 0.08, 0.7092)]:
    print(f"  {nm}: beta_L = {cf + 1 - th - ka:.4f}")

print()
print("Part C (EXACT). Certified rational instances of FW-T-T4L2-bL-v1 at the sharpw weights (2^15, 2^20), C' = 397")
print("  beta = mu0 - C' s - (8/5) r/sqrt(s) >= beta_lb, eta <= beta_lb r; L2 contraction ratio c_s r/beta_L with")
print("  c_s = [2 sqrt(pi s (1+s))]^-1, checked as (c_s r)^2 = r^2/(4 pi s (1+s)) <= (ratio beta_L)^2 with pi >= 333/106")
PI_LO = Q(333, 106)
INST = [  # (beta_L, mu0, n with s = 1/n^2, r, beta_lb, eta, ratio claim)
    (Q(7, 5), Q(359, 1000), 74, Q(1213, 10 ** 6), Q(1395, 10000), Q(1692, 10 ** 7), Q(196, 10 ** 4)),
    (Q(1), Q(302, 1000), 81, Q(918, 10 ** 6), Q(1162, 10000), Q(1066, 10 ** 7), Q(229, 10 ** 4)),
]
for bl, mu0, n, r, blb, eta, ratio in INST:
    assert pd(gram(mu0, bl, 2 ** 15, 2 ** 20)), "Gram not PD"
    s = Q(1, n * n)
    beta = mu0 - 397 * s - Q(8, 5) * r * n
    ok_beta = beta >= blb
    ok_eta = eta <= blb * r
    ok_ratio = r * r / (4 * PI_LO * s * (1 + s)) <= (ratio * bl) ** 2
    ok_slope = r * r / (4 * PI_LO * s * (1 + s)) <= Q(7, 10) ** 2
    print(f"  beta_L = {bl}: mu0 = {mu0} (G_w(mu0) PD), s = 1/{n * n}, r = {r}, beta = {float(beta):.8f} >= {blb}: {ok_beta};"
          f" eta = {eta} = {float(eta):.4e} <= beta_lb r = {float(blb * r):.6e}: {ok_eta}; c_s r/beta_L <= {ratio}: {ok_ratio};"
          f" c_s r < 7/10: {ok_slope}; G0 <= eta/1024 = {float(eta / 1024):.4e}; K_H = 1/beta_lb <= {float(1 / blb):.4f}")
    assert ok_beta and ok_eta and ok_ratio and ok_slope

print()
print("Part D (EXACT Gram, FLOAT eta). Sensitivity to the matrix floors m2 of (B5) M_2 and m1 of (B4) M_1, beta_L = 2.")
print("  Generalized Gram [[m2 - mu, -347/10, -5], [-347/10, w1 (m1 - mu) - 40, -3 w1], [-5, -3 w1, w0 (2 - mu)]].")
print("  Floors: A2 (1/2, 9/10); state131 P96 whole-plane lower bounds (293619/500000, 972875/1000000) (c1-t2 handoff Q2);")
print("  state131 TP-4/T4-093 packet caps (0.61151, 0.99116) are upper limits for any certificate at these weights.")


def gram_f(mu, m2, m1, bl, w1, w0):
    return [[m2 - mu, Q(-347, 10), Q(-5)],
            [Q(-347, 10), w1 * (m1 - mu) - 40, -3 * w1],
            [Q(-5), -3 * w1, w0 * (bl - mu)]]


def mu_lo_f(m2, m1, bl, w1, w0):
    lo, hi = Q(-4), m2
    for _ in range(60):
        m = (lo + hi) / 2
        if pd(gram_f(m, m2, m1, bl, w1, w0)):
            lo = m
        else:
            hi = m
    return lo


FLOORS = [("A2 floors", Q(1, 2), Q(9, 10)), ("P96 bounds", Q(293619, 500000), Q(972875, 1000000)),
          ("TP-4 caps (limit)", Q(61151, 100000), Q(99116, 100000))]
for name, w1, w0, Cp in WEIGHTS:
    print(" ", name)
    for fl, m2, m1 in FLOORS:
        m = mu_lo_f(m2, m1, Q(2), w1, w0)
        mf = float(m)
        s = mf / (5 * Cp)
        eta = (mf - Cp * s) ** 2 * math.sqrt(s) / 6.4
        print(f"    {fl:>18}: mu_lo = {mf:.8f}, FLOAT eta = {eta:.4e}, G0 = {eta / math.sqrt(w0):.4e}")
