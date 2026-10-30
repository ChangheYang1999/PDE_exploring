"""T2-R3: T4-019's H-free space X_s with the T2-R2 kernel constants and re-optimized component weights.

Run from artifacts/:  python3 -B arith/t4l2_sharp_framework.py [--no-float]
Needs python-flint (rigorous part); numpy only for the FLOAT weight scan.  Runtime a few seconds.

Norm (weights w1, w2; T4-019 and A2 use w1 = 2^14, w2 = 2^18):
  E_w(h)^2 = P^2 + w1 a^2 + w2 b^2,  P = ||omega D^2 h||, a = ||Dh||, b = ||h||;   X_{s,w}(h) = E_w(J^s h).
Base rate (Gram): (8) of T4-019 (A2 P7.5 (6), (10) before relaxation) and (7) with L2 margin 2 give
  -Re<Lh,h>_E >= mu E^2  iff  G(mu) >= 0,
  G(mu) = [[1/2-mu, -347/10, -5], [-347/10, w1 (9/10-mu) - 40, -3 w1], [-5, -3 w1, w2 (2-mu)]].
Commutator (T2-R2 Proposition 8, rows/columns P, a, b only; off-diagonal entries scale with the weights):
  K00 = dtop C + c8 U1 + (crw + 2 k1w) U2 + k1w R2,  K01 = k1w (U3 + 2 R3)/sqrt(w1),  K02 = k1w R4/sqrt(w2),
  K11 = C + U1 + (cru + k1u) U2 + k1u R2,            K12 = k1u R3 sqrt(w1/w2),
  K22 = C + U1 + cru U2 + k1u R2.
Rough constant (T2-R2 Proposition 12 without the H line): A' + B' <= 1.5871175 < 8/5 (low levels q + p_s and q).
Rate on X_{s,w}: mu0 - C'(w) s - (8/5) X_{s,w}(k)/sqrt(s), 0 < s <= 2^-10.  Closure as in T4-019 section 6.
"""
from fractions import Fraction as Q
from flint import arb, ctx
import math, sys

ctx.prec = 200
PI = arb.pi()
SQPI = PI.sqrt()
SMAX = arb(1) / 1024

m1 = SQPI / 2 * arb.gamma((1 - SMAX) / 2)
w1c = arb(8) * arb(5).sqrt() / 5 * arb(6) ** (arb(-3) / 5)
k1u, k1w = m1, m1 + arb(8) / 5
cru, crw = arb(3) / 2 * m1, arb(3) / 2 * m1 + arb(32) / 15
c8, dtop = 1 + w1c * 3 * PI / 4, 1 + w1c * PI / 2
C, U1, U2, U3, R1, R2, R3, R4 = [arb(x) for x in (2, 6, 24, 160, 22, 32, 80, 2048)]

# rough constant without the H line (Proposition 12 of notes/T2_sharp_constants.md)
s = SMAX
q = 1 / (2 * SQPI)
ps = arb(2) ** s * (1 + s).sqrt() / (2 * SQPI)
Pw = ps * (1 + w1c * m1 * s) + w1c * m1 * s / (2 * SQPI)
Ap = arb(4) / 5 * q + q * (1 + 4 * w1c * m1 * s) + 2 * Pw
Bp = arb(9) / 5 * Pw
c1 = q + ps
assert Ap > c1 and c1 > q
cU = Ap + Bp
assert cU < arb(8) / 5
CU = Q(8, 5)
print(f"rough constant (no H line): A' + B' <= {cU.str(8)} < 8/5; low levels q + p_s = {c1.str(6)} and q = {q.str(6)}")


def Kbound(w1, w2):
    """rigorous integer upper bound of the largest symmetric row sum of the 3x3 sharp block, weights (w1, w2)."""
    a1 = (arb(Q(w1).numerator) / Q(w1).denominator).sqrt()
    a2 = (arb(Q(w2).numerator) / Q(w2).denominator).sqrt()
    K00 = dtop * C + c8 * U1 + (crw + 2 * k1w) * U2 + k1w * R2
    K01 = k1w * (U3 + 2 * R3) / a1
    K02 = k1w * R4 / a2
    K11 = C + U1 + (cru + k1u) * U2 + k1u * R2
    K12 = k1u * R3 * a1 / a2
    K22 = C + U1 + cru * U2 + k1u * R2
    rows = [K00 + K01 / 2 + K02 / 2, K01 / 2 + K11 + K12 / 2, K02 / 2 + K12 / 2 + K22]
    ub = max(int(math.ceil(float((r.mid() + r.rad()).str(30, radius=False)))) for r in rows)
    assert all(r < ub for r in rows)
    return ub, rows, (K00, K01, K02, K11, K12, K22)


def gram_minors(mu, w1, w2):
    G = [[Q(1, 2) - mu, -Q(347, 10), Q(-5)],
         [-Q(347, 10), w1 * (Q(9, 10) - mu) - 40, -3 * w1],
         [Q(-5), -3 * w1, w2 * (2 - mu)]]
    d1 = G[0][0]
    d2 = G[0][0] * G[1][1] - G[0][1] ** 2
    d3 = (G[0][0] * (G[1][1] * G[2][2] - G[1][2] ** 2) - G[0][1] * (G[1][0] * G[2][2] - G[1][2] * G[2][0])
          + G[0][2] * (G[1][0] * G[2][1] - G[1][1] * G[2][0]))
    return d1, d2, d3


def mu0_of(w1, w2):
    """largest k/1000 with G(k/1000) positive definite (exact leading minors), and the failure at (k+1)/1000."""
    k = 0
    while all(d > 0 for d in gram_minors(Q(k + 1, 1000), w1, w2)):
        k += 1
    return Q(k, 1000)


# T4-019 check: weights (2^14, 2^18) at mu = 1/4 reproduce its minors
assert gram_minors(Q(1, 4), Q(2**14), Q(2**18)) == (Q(1, 4), Q(144831, 100), Q(1077858728, 25))

cases = [("FW-T-T4L2-sharp-v1 (A2/T4-019 weights)", Q(2**14), Q(2**18), 88),
         ("FW-T-T4L2-sharpw-v1 (weights 2^15, 2^20)", Q(2**15), Q(2**20), 72)]
out = {}
for name, w1, w2, isq in cases:
    mu0 = mu0_of(w1, w2)
    Cb, rows, Ks = Kbound(w1, w2)
    print(f"\n{name}: w1 = {w1}, w2 = {w2}")
    print(f"  base rate mu0 = {mu0} (exact Gram minors positive; {mu0 + Q(1, 1000)} fails)")
    print("  K block (P, a, b):", ", ".join(k.str(6) for k in Ks))
    print("  symmetric row sums:", [r.str(7) for r in rows], " -> C' =", Cb)
    sd = Q(1, isq * isq)                       # s = 1/isq^2, sqrt(s) = 1/isq exactly
    assert sd <= Q(1, 1024)
    mu = mu0 - Cb * sd
    r = Q(math.floor(float(mu) / isq / (2 * float(CU)) * 10**6), 10**6)
    beta = mu - CU * r * isq
    beta_lb = Q(math.floor(float(beta) * 10**4), 10**4)
    assert 0 < beta_lb <= beta
    eta = Q(math.floor(float(beta_lb * r) * 10**9), 10**9)
    assert eta <= beta_lb * r                  # self-map: X(T k) <= eta/beta <= r
    cs = isq / (2 * SQPI)                      # c_s <= 1/(2 sqrt(pi s)), s = 1/isq^2
    csr = cs * arb(r.numerator) / r.denominator
    print(f"  s = 1/{isq*isq} = {float(sd):.4e} (sqrt s = 1/{isq}); mu0 - C's = {mu} = {float(mu):.6f}")
    print(f"  r = {r}; rate on the ball >= {beta_lb} (exact {float(beta):.6f}); K_H <= 1/({beta_lb}) = {float(1/beta_lb):.4f}")
    print(f"  threshold eta = {eta} = {float(eta):.6e}; K_H eta <= r: {eta / beta_lb <= r}")
    print(f"  L2 contraction ratio c_s r/2 <= {(csr / 2).str(6)} < 1; slope 7/10 - c_s r > 0: {bool(arb(7) / 10 - csr > 0)}")
    print(f"  component requirements (each necessary): P <= {float(eta):.4e}, G1 <= {float(eta) / math.sqrt(w1):.4e},"
          f" G0 <= {float(eta) / math.sqrt(w2):.4e}  (G1 = ||D J^s F||, G0 = ||J^s F||)")
    cmp_const = max(1 + Q(32, 25) + w1, 1 + w2 / w1, Q(1))
    print(f"  comparison (13) with these weights: X <= E^(1-s) (2 Q3^2 + {float(cmp_const):.2f} E^2)^(s/2) + 34 s E,"
          f" (factor {float(cmp_const)**(float(sd)/2):.6f} per unit, 34 s = {34*float(sd):.2e}; with T2-R2 Lemma 5: 1.92 s)")
    out[name] = (mu0, Cb, sd, r, beta_lb, eta, w1, w2)

print("\ngains: eta(sharp-v1)/eta(T4-019 = 1/163840) =", f"{float(out[cases[0][0]][5] * 163840):.2f};",
      "eta(sharpw-v1)/eta(T4-019) =", f"{float(out[cases[1][0]][5] * 163840):.2f}")
e0, e1 = out[cases[0][0]], out[cases[1][0]]
print("sharpw-v1 versus sharp-v1, per pure component: P", f"{float(e1[5] / e0[5]):.3f},",
      "G1", f"{float(e1[5] / e0[5]) * math.sqrt(2**14 / 2**15):.3f},", "G0", f"{float(e1[5] / e0[5]) * math.sqrt(2**18 / 2**20):.3f}")
# Containment at equal s: w' <= 4 w componentwise gives E_w' <= 2 E_w, so E_w(f) <= eta0 implies E_w'(f) <= 2 eta0.
print("at equal s: E_(2^15,2^20) <= 2 E_(2^14,2^18); 2 eta(sharp-v1) =", f"{2*float(e0[5]):.4e}", "< eta(sharpw-v1) =",
      f"{float(e1[5]):.4e}:", 2 * e0[5] < e1[5], "(the two frameworks use different s, so this is a comparison, not an inclusion)")
# T4-017 symmetric point test for the scalar-gap families (general-mu formulas of reviews/REVIEW_T4_017.md, FLOAT).
# Uses only ||h||_(H^(2+s)) <= X_(s,w)(h), valid for w1 >= 2, w2 >= 1.
for name in out:
    mu0, Cb = out[name][0], out[name][1]
    c1r = float(mu0) / (4 * float(CU) * math.sqrt(math.pi))
    c0r = float(mu0) ** 1.5 / (3 * float(CU) * math.sqrt(3 * math.pi * Cb))
    print(f"T4-017 family test, {name}: C1s r < {c1r:.5f}, C0 r < {c0r:.3e}")
    for nm, F, V, D in [("d2 (0,1)", 0.0117458591, 1.1341455898, 8.3931825906),
                        ("Mpen2 (0,2)", 0.0743611985, 2.5378314572, 6.6694055775),
                        ("b6 (0,1)", 2.9582404428, 1.0801115995, 8.0016081038)]:
        bound = c1r * V + c0r * (1 + D) + c1r * c0r
        print(f"    {nm}: |F| = {F:.6f}, bound = {bound:.6f}, excluded = {F > bound} (FLOAT)")

# T4-017 symmetric point test for the two specific balls (arb; witness triples copied from c1-t4, N4/T4-ORIGIN values).
# For h in the ball and |y| >= 1/2 on the axis x = 0: |h_y| <= C1s r, |h|, |U[h]| <= C0 r, with
# C1s^2 <= C1^2/2 = 1/(8 pi s (1+s)) / 2 and C0^2 = 1/(4 pi (1+s)) (reviews/REVIEW_T4_017.md steps 2, 3, 8; these use
# only ||h||_(H^(2+s)) <= X_(s,w)(h)).  A solution in the ball forces |F| <= C1s r |V| + C0 r (1 + |D rho|) + C1s r C0 r.
import json
wit = json.load(open("data/t4_017_cartesian_witnesses.json"))["rows"]
for name in out:
    mu0, Cb, sd, r = out[name][:4]
    sA = arb(sd.numerator) / sd.denominator
    rA = arb(r.numerator) / r.denominator
    c1sr = rA / (4 * (PI * sA * (1 + sA)).sqrt())
    c0r = rA / (2 * (PI * (1 + sA)).sqrt())
    print(f"point test on the specific ball of {name}: C1s r <= {c1sr.str(8)}, C0 r <= {c0r.str(8)}")
    for row in wit:
        f = row["fields"]
        assert row["point"][0] == 0 and abs(Q(row["point"][1])) >= Q(1, 2)
        F = abs(arb(f["residual"])); V = arb(f["velocity_norm"]); D = arb(f["gradient_norm"])
        gap = F - (c1sr * V + c0r * (1 + D) + c1sr * c0r)
        print(f"    {row['candidate']} at {tuple(row['point'])}: gap |F| - bound = {gap.str(8)}, excluded = {bool(gap > 0)}")

if "--no-float" in sys.argv:
    print("done (FLOAT scan skipped)"); sys.exit(0)
import numpy as np
print("\nFLOAT weight scan (optimal non-dyadic s = mu0/(5C'), eta_opt = (4/(25 sqrt5)) mu0^(5/2)/(c_U sqrt C')):")
k00 = float(Kbound(Q(2**14), Q(2**18))[2][0].mid().str(20, radius=False))


def mumax(w1, w2):
    lo, hi = 0.0, 0.5
    for _ in range(50):
        m = (lo + hi) / 2
        G = np.array([[0.5 - m, -34.7, -5], [-34.7, w1 * (0.9 - m) - 40, -3 * w1], [-5, -3 * w1, w2 * (2 - m)]])
        lo, hi = (m, hi) if np.linalg.eigvalsh(G).min() >= 0 else (lo, m)
    return lo


for l1, l2 in [(14, 18), (14, 19), (15, 19), (15, 20), (16, 20), (16, 21), (17, 22), (18, 24), (20, 26)]:
    w1, w2 = 2.0**l1, 2.0**l2
    m = mumax(w1, w2)
    Cb = Kbound(Q(2**l1), Q(2**l2))[0]
    eta = (4 / (25 * math.sqrt(5))) * m**2.5 / (1.6 * math.sqrt(Cb))
    print(f"  w = (2^{l1}, 2^{l2}): mu0 {m:.4f}, C' {Cb}, eta_opt {eta:.3e}, G1 {eta/math.sqrt(w1):.3e}, G0 {eta/math.sqrt(w2):.3e}")
print("done")
