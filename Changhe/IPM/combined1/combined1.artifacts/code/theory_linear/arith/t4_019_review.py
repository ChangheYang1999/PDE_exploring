"""Independent checks for reviews/REVIEW_T4_019.md (c1-t2 review of c1-t4 research/l2_closure/PROOF.md, T4-019).

Run from artifacts/:  python3 -B arith/t4_019_review.py [--no-float]
Exact part: Fractions and python-flint arb (prec 200).  FLOAT part: scipy quadrature of the Hilbert-Schmidt angular
constants of T4-016 in elliptic coordinates (independent of c1-t4 code).  Runtime: well under a minute.
"""
from fractions import Fraction as Q
from flint import arb, ctx
import sys

ctx.prec = 200
PI = arb.pi()

# (1) Gram matrix of (9): combine (7) at k = 0 (-<Lh,h> >= 2 b^2), (8) and weights 1, 2^14, 2^18; subtract (1/4) E^2.
c_P2, c_Pa, c_Pb, c_a2 = Q(1, 2), -Q(347, 5), -Q(10), -Q(40)          # Hessian line of (8)
g_a2, g_ab = Q(9, 10), -Q(6)                                           # gradient line of (8)
l_b2 = Q(2)                                                            # L2 line, (7)
w1, w2 = Q(2**14), Q(2**18)
G = [[c_P2 - Q(1, 4), c_Pa / 2, c_Pb / 2],
     [c_Pa / 2, c_a2 + w1 * g_a2 - w1 / 4, w1 * g_ab / 2],
     [c_Pb / 2, w1 * g_ab / 2, w2 * l_b2 - w2 / 4]]
m1 = G[0][0]
m2 = G[0][0] * G[1][1] - G[0][1] ** 2
m3 = (G[0][0] * (G[1][1] * G[2][2] - G[1][2] ** 2) - G[0][1] * (G[1][0] * G[2][2] - G[1][2] * G[2][0])
      + G[0][2] * (G[1][0] * G[2][1] - G[1][1] * G[2][0]))
print("(1) Gram matrix G =", [[str(x) for x in row] for row in G])
print("    leading minors:", m1, m2, m3, " positive:", m1 > 0 and m2 > 0 and m3 > 0)
assert (m1, m2, m3) == (Q(1, 4), Q(144831, 100), Q(1077858728, 25))
print("    Hessian Pa coefficient 28*(9/5)+3+16 =", Q(28) * Q(9, 5) + 3 + 16)

# (2) K3 = first three rows/columns of the A2 P8.4 K matrix; symmetric row sums.
K3 = [[Q(4708), Q(85, 2), Q(68)], [Q(0), Q(4290), Q(340)], [Q(0), Q(0), Q(3882)]]
rs = [sum((K3[i][j] + K3[j][i]) / 2 for j in range(3)) for i in range(3)]
print("(2) K3 symmetric row sums:", [str(x) for x in rs], " max < 4800:", max(rs) < 4800)

# (3) rough constant A_s + B_s on 0 < s <= 2^-10 (both increasing in s)
s = Q(1, 1024)
As, Bs = Q(127, 50) + Q(653, 5) * s, Q(9, 5) * (1 + 44 * s)
print("(3) A_s + B_s at s = 2^-10:", As + Bs, "=", float(As + Bs), "< 5:", As + Bs < 5,
      "; A_s >= 13/10 (so x = 1 is the worst case):", As >= Q(13, 10))

# (4) parameter box s = 2^-17, r = 2^-14 (arb, rigorous)
s, r = arb(1) / 2**17, arb(1) / 2**14
beta = arb(1) / 4 - 4800 * s - 5 * r / s.sqrt()
cs = 1 / (2 * (PI * s * (1 + s)).sqrt())
print("(4) beta =", beta.str(12), " > 1/10:", bool(beta > arb(1) / 10))
print("    eta/beta < r (self-map):", bool((r / 10) / beta < r))
print("    c_s =", cs.str(10), "; c_s r =", (cs * r).str(10), "< 0.006234:", bool(cs * r < arb(6234) / 10**6),
      "; contraction ratio c_s r/2 =", (cs * r / 2).str(10))
print("    c_s sqrt(s) = 1/(2 sqrt(pi(1+s))) <", (1 / (2 * PI.sqrt())).str(8), "< 3/10")
print("    slope: a0 >= c - 11/10 > 7/10 (M1 >= 9/10 at the origin); 7/10 - c_s r > 0:", bool(arb(7) / 10 - cs * r > 0))

# (5) comparison constant 16410 in (13): ||D(omega D^2 f)||^2 <= 2 Q3^2 + 2 (4/5)^2 P^2, plus 2^14 P^2 and 2^18 a^2.
# Coefficients of P^2, 2^14 a^2, 2^18 b^2 in ||F||_(H^1)^2 - 2 Q3^2:
cP = 1 + 2 * Q(16, 25) + 2**14
ca = 1 + Q(2**18, 2**14)
cb = Q(1)
print("(5) H^1 coefficients (P^2, 2^14 a^2, 2^18 b^2):", cP, ca, cb, " max <= 16410:", max(cP, ca, cb) <= 16410)
# sup |omega'|/omega = sup (16/5) r/(1+4r^2) = 4/5 at r = 1/2
print("    sup |D omega|/omega = (16/5)(1/2)/2 =", Q(16, 5) * Q(1, 2) / 2)
# weighted commutator in (13): A2 uses 17 s ||D omega||_inf <= 34 s; T2-R2 Lemma 5 gives w1 m1 s.
w1a = arb(8) * arb(5).sqrt() / 5 * arb(6) ** (arb(-3) / 5)
m1a = PI.sqrt() / 2 * arb.gamma((1 - arb(1) / 1024) / 2)
print("    T2-R2 alternative for 34 in (13): w1 m1 =", (w1a * m1a).str(8))

# (6) kappa for the state131 seminorms reported by T4-018 (FLOAT inputs, N4/T4 values)
Dx, Dy = arb("4.66141632497324"), arb("16.3343155955634")
kap = (((arb(2).log() - arb(1) / 2) * Dx**2 + (3 * arb(2).log() - 2) * Dy**2) / (16 * PI)).sqrt()
print("(6) kappa(state131) from T4-018 seminorms:", kap.str(12), "(T4-018: 0.7107535441929825)")

if "--no-float" in sys.argv:
    print("done (FLOAT checks skipped)"); sys.exit(0)

# (7) FLOAT: Hilbert-Schmidt angular constants.  HS^2 of K = (1/2)[R1,[R1,b]] - (1/2)[R1,[R2,a]], a = rho_x, b = rho_y,
# equals (2pi)^-4 (1/4) int |rho^(zeta)|^2 |zeta|^4 Phi(zeta^) dzeta with
# Phi(z) = int_{R^2} d1^2 (z2 d1 - z1 d2)^2 dx,  d = x/|x| - (x - z)/|x - z|.
# T4-016 is equivalent to Phi(z) = pi[(log2 - 1/2) z1^2 + (3 log2 - 2) z2^2].
import numpy as np
from scipy import integrate


def Phi(phi, mu_max=40.0):
    z = np.array([np.cos(phi), np.sin(phi)]); zp = np.array([-z[1], z[0]])

    def f(nu, mu):  # elliptic coordinates with foci 0 and z
        X = z / 2 + 0.5 * np.cosh(mu) * np.cos(nu) * z + 0.5 * np.sinh(mu) * np.sin(nu) * zp
        Y = X - z
        d = X / np.hypot(*X) - Y / np.hypot(*Y)
        jac = 0.25 * (np.sinh(mu) ** 2 + np.sin(nu) ** 2)
        return d[0] ** 2 * (z[1] * d[0] - z[0] * d[1]) ** 2 * jac

    val, err = integrate.dblquad(f, 0, mu_max, 0, 2 * np.pi, epsabs=1e-11, epsrel=1e-11)
    return val, err


L2 = np.log(2.0)
for phi in (0.0, np.pi / 2, 0.7, 2.0):
    v, e = Phi(phi)
    pred = np.pi * ((L2 - 0.5) * np.cos(phi) ** 2 + (3 * L2 - 2) * np.sin(phi) ** 2)
    print(f"(7) Phi(angle {phi:.4f}) = {v:.12f} (quad err {e:.1e}); T4-016 prediction {pred:.12f}; diff {v - pred:.2e}")
print("done")
