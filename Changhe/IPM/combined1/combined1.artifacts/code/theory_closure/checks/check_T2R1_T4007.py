# Independent arithmetic checks by c1-t1 of (a) T2-R1 Gram positivity (c1-t2 notes/T2_routes_v01.md section 2)
# and (b) the rational relaxations of T4-007 (c1-t4 research/residual_witness/PROOF.md, inequality (6)).
# Exact rationals; standard library only.
from fractions import Fraction as Fr
import math

def G(mu):
    return [[Fr(1, 2) - mu, Fr(-347, 10), Fr(-5)],
            [Fr(-347, 10), 2**14 * (Fr(9, 10) - mu) - 40, Fr(-3 * 2**14)],
            [Fr(-5), Fr(-3 * 2**14), 2**14 * 44 - 2**18 * mu]]

def minors(M):
    m1 = M[0][0]
    m2 = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    m3 = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
          - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
          + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    return m1, m2, m3

for mu in (Fr(1, 10), Fr(297, 1000), Fr(298, 1000)):
    ms = minors(G(mu))
    print("T2-R1 mu =", mu, "leading minors positive:", all(m > 0 for m in ms), [float(m) for m in ms])

# bisection for the sup of admissible mu (float, diagnostic)
lo, hi = Fr(297, 1000), Fr(298, 1000)
for _ in range(40):
    mid = (lo + hi) / 2
    if all(m > 0 for m in minors(G(mid))):
        lo = mid
    else:
        hi = mid
print("T2-R1 sup mu (bisection) ~", float(lo))

# T2-R1 rate on ball: 297/1000 - 4800 s - 5 r / sqrt(s), s = 2^-16, r = 3*2^-15
s = Fr(1, 2**16); r = Fr(3, 2**15)
rate = Fr(297, 1000) - 4800 * s - 5 * r * 2**8
print("T2-R1 rate on ball =", rate, float(rate), "== 13641/128000:", rate == Fr(13641, 128000))
print("T2-R1 eta = r/10 =", r / 10, float(r / 10))
c_s = 1 / (2 * math.sqrt(math.pi * float(s) * (1 + float(s))))
d = c_s * float(r)
print("T2-R1 d = c_s r =", d, " K_L d =", d / (19 / 5 - d))

# (b) T4-007: gap 1/10 - 4800 s - 5 r/sqrt(s) > 0 implies s < 1/48000, r < sqrt(s)/50.
# C1 r < 1/240, C0 r < 3/100000, C0 C1 r^2 < 1/8000000 (using pi > 3).
smax = 1 / 48000
print("T4-007 sup C1 r =", (math.sqrt(smax) / 50) / math.sqrt(8 * math.pi * smax), "bound", 1 / 240)
print("T4-007 sup C0 r =", (math.sqrt(smax) / 50) / (2 * math.sqrt(math.pi)), "bound", 3 / 100000)
print("T4-007 sup C0C1 r^2 =", (smax / 2500) / (2 * math.sqrt(math.pi)) / math.sqrt(8 * math.pi * smax), "bound", 1 / 8e6)
# Same relaxation for the T2-R1 gap 297/1000 - 4800 s - 5 r/sqrt(s) > 0: s < 297/4800000, r < (297/5000) sqrt(s).
smax2 = 297 / 4800000
print("with T2-R1 base: sup C1 r =", (297 / 5000) / math.sqrt(8 * math.pi), " sup C0 r =",
      (297 / 5000) * math.sqrt(smax2) / (2 * math.sqrt(math.pi)))

# Necessary radius for the d2 witness at (0,1) (T4 point_witnesses.json values, PENDING-N4) for several s.
F, Vn, gn = 0.0117458591346551, 1.13414558978361, 8.39318259059732
for s_ in (2.0**-18, 2.0**-16, 1.9e-5, 1.0 / 1024):
    C0 = 1 / (2 * math.sqrt(math.pi * (1 + s_))); C1 = 1 / math.sqrt(8 * math.pi * s_ * (1 + s_))
    A = C1 * Vn + C0 * (1 + gn); B = C0 * C1
    rn = 2 * F / (A + math.sqrt(A * A + 4 * B * F))
    print(f"d2 (0,1): s = {s_:.4e}  necessary H^(2+s) radius >= {rn:.4e}")
