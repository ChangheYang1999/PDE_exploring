"""Exact rational checks for the appendix entries A.3.49-A.3.51 (numbers quoted in the text).

Run with OMP_NUM_THREADS=1.  Exit status is nonzero on failure.
"""
import sys
from fractions import Fraction as Fr
import math

results = []


def report(name, ok, info=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ((": " + info) if info else ""))


# ---------------------------------------------------------------- A.3.49(a)
def b(j, m):
    return (m * m + 4 * j * j) / (4 * abs(4 * j * j - m * m))


m = Fr(11, 3)
b1, b2, b3 = b(1, m), b(2, m), b(3, m)
report("b_1(11/3) = 157/340", b1 == Fr(157, 340), str(b1))
report("b_2(11/3) = 265/92", b2 == Fr(265, 92), str(b2))
report("b_3(11/3) = 445/812", b3 == Fr(445, 812), str(b3))
report("b_3 > b_1 at 11/3", b3 > b1)
# b_j decreasing for j >= 2 at m = 11/3 (first 200 terms)
report("b_j decreasing for 2 <= j <= 200", all(b(j, m) > b(j + 1, m) for j in range(2, 200)))
Bm = Fr(1, 2) + b2 + max(b1, b3)
report("Gershgorin bound = 18342/4669", Bm == Fr(18342, 4669), str(Bm))
report("row sums: 1/4+b1 <= 1/2+b1+b2", Fr(1, 4) + b1 <= Fr(1, 2) + b1 + b2)
report("LCD 18676 and 73368/18676", Fr(1, 2) * 18676 + b2 * 18676 + b3 * 18676 == 73368 and Fr(73368, 18676) == Bm)
report("4669 = 7*23*29", 4669 == 7 * 23 * 29)
s = Fr(2, 5)
mm = 2 + 1 / (1 - s)
report("m = 2 + 1/(1-s) = 11/3 at s = 2/5", mm == m)
beta = mm * (1 - s) - 2
report("beta = 1 - 2s = 1/5", beta == 1 - 2 * s == Fr(1, 5))
km = 1 * Bm - (mm - 1)
report("k_m = 18342/4669 - 8/3 = 17674/14007", km == Fr(17674, 14007), str(km))
eps = beta / km
report("eps(1,2/5) = 14007/88370", eps == Fr(14007, 88370), str(eps))
report("14007/88370 > 0.158", eps > Fr(158, 1000), str(float(eps)))
report("2/(1-s) < m < 4 at s = 2/5", Fr(2) / (1 - s) < mm < 4)

# ---------------------------------------------------------------- A.3.49(d) constants
report("(N^2+4N+5)/(N^2-4) = 37/12 at N = 4", Fr(16 + 16 + 5, 12) == Fr(37, 12))
report("(N^2+4N+5)/(N^2-4) decreasing, N = 4..400",
       all(Fr(N * N + 4 * N + 5, N * N - 4) >= Fr((N + 1) ** 2 + 4 * (N + 1) + 5, (N + 1) ** 2 - 4)
           for N in range(4, 400)))
report("kernel L1 norm (1/(4n))(1/(2n+2)+1/(2n-2)) = 1/(N^2-4), n = 1..50 (n>=2)",
       all(Fr(1, 4 * n) * (Fr(1, 2 * n + 2) + Fr(1, 2 * n - 2)) == Fr(1, 4 * n * n - 4) for n in range(2, 51)))
report("mode-1 factor (8D+8D^2+D^3)/D <= 49/4 at D = 1/2", 8 + 8 * Fr(1, 2) + Fr(1, 4) == Fr(49, 4))
report("(j+1/2) <= (7/512)(1+j)^4 for j = 3..201",
       all(Fr(2 * j + 1, 2) <= Fr(7, 512) * (1 + j) ** 4 for j in range(3, 202)))
report("(1+j) <= (1+j)^4/64 for j >= 3", all(Fr(1 + j) <= Fr((1 + j) ** 4, 64) for j in range(3, 202)))
GU = Fr(49, 8) + Fr(37, 12) * Fr(7, 512) * Fr(1, 2)
Grho = Fr(5, 2) + Fr(9, 8) * Fr(1, 64) * Fr(1, 2)
report("G_U/(DM) <= 49/8 + (37/12)(7/512)/2 < 6.15", GU < Fr(615, 100), str(float(GU)))
report("G_rho/(DM) <= 5/2 + (9/8)(1/64)/2 < 2.51", Grho < Fr(251, 100), str(float(Grho)))
report("total < 9", GU + Grho < 9)
report("0.47/9 > 1/20", Fr(47, 100) / 9 > Fr(1, 20))
report("sqrt(2)/3 > 0.47", 2 / 9 > Fr(47, 100) ** 2)

# ---------------------------------------------------------------- A.3.50(a)
cstar_inv = 73746
report("73746 = 2*4097*9", 2 * 4097 * 9 == cstar_inv)
report("4097^(1/4) < 9 (9^4 = 6561 > 4097)", 9 ** 4 > 4097 and 64 ** 2 + 1 == 4097)
report("C = 1179936 = 16*73746", 1179936 == 16 * cstar_inv)
report("294984 = 4*73746", 294984 == 4 * cstar_inv)
report("4B/L = 4/C = 1/294984", Fr(4, 1179936) == Fr(1, 294984))
report("2/pi*(1+L^-2) <= 4 for L >= 1 (pi > 3)", Fr(2, 3) * 2 <= 4)
report("H <= (2/7) 64^(-1/2) = 1/28", Fr(2, 7) / 8 == Fr(1, 28))
report("r >= 64: (1/2)(24/28) = 3/7 and 3/7 + 2/294984 < 1 - 1/294984",
       Fr(1, 2) * Fr(24, 28) == Fr(3, 7) and Fr(3, 7) + Fr(3, 294984) < 1)
report("transport at (0,1): 2^(5/4) > 2 so 6*2^(-5/4) < 3 < 9/e (e < 3)", 2 ** 5 > 2 ** 4)
# (1+r^2/2)/(1+r^2)^(5/4) <= 1 : (1+s/2)^4 <= (1+s)^5 coefficientwise
import itertools
lhs = [Fr(math.comb(4, k), 2 ** k) for k in range(5)]
rhs = [math.comb(5, k) for k in range(6)]
report("(1+s/2)^4 <= (1+s)^5 coefficientwise", all(lhs[k] <= rhs[k] for k in range(5)))

# ---------------------------------------------------------------- A.3.50(e) rectangle
report("(7/3)^4 = 2401/81 < 32, so 7*2^(-5/4) < 3", Fr(7, 3) ** 4 == Fr(2401, 81) and Fr(2401, 81) < 32)
report("e < 11/4 and (11/4)(16/15) = 44/15 < 3", Fr(11, 4) * Fr(16, 15) == Fr(44, 15) and Fr(44, 15) < 3)
report("25/16 - 36/25 = 49/400 >= 1/L^2 for L >= 3", Fr(25, 16) - Fr(36, 25) == Fr(49, 400) and Fr(1, 9) <= Fr(49, 400))
report("(11/4)^3 (16/15)^2 = 5324/225 < 25", Fr(11, 4) ** 3 * Fr(16, 15) ** 2 == Fr(5324, 225) and Fr(5324, 225) < 25)
report("r^2 <= 1 + 36/25 = 61/25 < 5/2, (2/5)^3 = 8/125", Fr(61, 25) < Fr(5, 2) and Fr(2, 5) ** 3 == Fr(8, 125))
F2 = Fr(4, 5) * Fr(1, 25) * Fr(8, 125)
report("area * (1/5)^2 * 8/125 = 32/15625", F2 == Fr(32, 15625), str(F2))
ratio2 = Fr(9, 13) ** 2 * Fr(32, 15625) / 4
report("(81/169)(32/62500) > 10^-4 (pi < 4)", Fr(81, 169) * Fr(32, 62500) == ratio2 and ratio2 > Fr(1, 10 ** 4),
       str(float(ratio2)))
report("int_0^1 r dr + int_1^inf r^-3 dr = 1", Fr(1, 2) + Fr(1, 2) == 1)
report("13/9 = (9+4)/9", Fr(13, 9) == Fr(9 + 4, 9))

# ---------------------------------------------------------------- A.3.51(c),(d)
A = 11
e1, e2 = 4 + 2 * (A - 1), 4 + 4 * (A - 1)
astar = Fr(2 * (A * A - 18 * A + 1), A - 9)
report("e_1 = 24, e_2 = 44 at A = 11", e1 == 24 and e2 == 44)
report("a_*(11) = -76", astar == -76)
report("beta(a) = -4a - 304 at A = 11 vanishes at -76", (20 - e1) * astar + e1 ** 2 - 20 * e2 == 0)
a = -76
P = [Fr((a - e1) * (a - e2), 20 * e1), Fr(2 * (a - e2), e1), Fr(1)]
report("P at a = -76 is t^2 - 10 t + 25", P == [25, -10, 1])
c = [x / 25 for x in P]
report("c = (1, -2/5, 1/25) after dividing by 25", c == [1, Fr(-2, 5), Fr(1, 25)])
a = -100
P = [Fr((a - e1) * (a - e2), 20 * e1), Fr(2 * (a - e2), e1), Fr(1)]
cn = [x / P[0] for x in P]
disc = cn[1] ** 2 - 4 * cn[0] * cn[2]
report("a = -100: normalized (1, -10/31, 5/186)", cn == [1, Fr(-10, 31), Fr(5, 186)], str(cn))
report("a = -100: discriminant -10/2883", disc == Fr(-10, 2883), str(disc))
report("9 + sqrt 80 threshold: A^2 - 18A + 1 at A = 9 + sqrt80 is 0", (81 + 80) - 18 * 9 + 1 == 0)

bad = [n for n, ok in results if not ok]
print("%d checks, %d failed" % (len(results), len(bad)))
sys.exit(1 if bad else 0)
