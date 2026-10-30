"""Independent reproduction of the four-branch finite-family L^2 cutoffs of c1-t4 T4-043 (T4-042 section 6).

Run from artifacts/:  python3 -B arith/b4_family_cutoffs.py
Needs python-flint.  A few seconds.

Theorem used (T4-025, AUDITED; c1-t4 research/finite_family_l2_audit/PROOF.md): for the B = 4 family with radial degree
K, ||F||_2 >= (E_4/sqrt 2) (2 a0 + 1)^(-1/2) prod_(a in A_K, a != a0) |a - a0|/(a + a0 + 1), with a0 = 5 delta/2 - 3/2,
A_K = {l delta/2 + k - 3/2 : 1 <= l <= 8, 0 <= k <= 2K + 4, l delta/2 + k > 1}, and E_4 the full-circle norm of the
exact residual coefficient at 1 - 5 delta (index 4 of c1-n4's stationary_principal.json, data/n4_forcing_sin_4.json).
With delta = N/D each factor is the integer ratio |(l - 5) N + 2 D k| / ((l + 5) N + 2 D (k - 2)), and
(2 a0 + 1)^(-1/2) = sqrt(D/(5N - 2D)).  This script is my own code; it does not import or run any c1-t4 or c1-n4 code.

Checks:
  (a) the exponents in A_K are distinct and all factors lie in (0, 1), so the bound decreases strictly in K;
  (b) anchors from T4-027/T4-029 (T4-019 box: X_s(F) >= (1 - 34 s) 512 ||F||_2 with s = 2^-17, eta = 1/163840):
      the floor at K = 150 and K = 10000, and the crossing K = 25929/25930;
  (c) T4-043: X_(s,w)(F) >= sqrt(w2) ||F||_2 (J^s >= 1), against eta = 76219/10^9 (sharp, sqrt(w2) = 512) and
      eta = 4207/(2 10^7) (sharpw, sqrt(w2) = 1024): last excluded K and the first inconclusive K.
"""
import json
import sys
from fractions import Fraction as Q
from math import gcd
from pathlib import Path

from flint import arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 512
HERE = Path(__file__).resolve().parents[1]

z = json.loads((HERE / "data/n4_forcing_sin_4.json").read_text())
c = Q(z["cl"])
assert c == Q(4076476460239181, 2**51)
delta = 1 - 1 / c
N, D = delta.numerator, delta.denominator
b4 = z["branches"]["4"]
assert Q(b4["residual_exponent"]) == 1 - 5 * delta
e = {int(m): Q(v) for m, v in b4["forcing_sin"].items()}
assert all(m > 0 and m % 2 == 1 for m in e)
pi = arb.pi()
E4 = (pi * arb(sum(v * v for v in e.values()).numerator) / sum(v * v for v in e.values()).denominator).sqrt()
print("delta = N/D with N =", N, ", D =", D, "; E_4 =", E4.str(20), "(", len(e), "odd sine modes up to", max(e), ")")
print("    c1-n4 forcing_full_circle_norm:", b4["forcing_full_circle_norm"][:40])

# (a) distinctness: l delta/2 + k = l' delta/2 + k' with (l, k) != (l', k') needs (l - l') N = 2 D (k' - k), 1 <= |l - l'| <= 7
for dl in range(1, 8):
    assert (dl * N) % (2 * D) != 0
assert gcd(N, D) == 1 and 5 * N > 2 * D            # a0 > -1/2 and (l, k) = (5, 0) is in A_K (5 delta/2 > 1)
print("(a) exponents distinct (no (l - l') N in 2 D Z for 1 <= |l - l'| <= 7); 5 delta/2 > 1, so a0 is in A_K")


def factors(k):
    """Integer ratios (numerator, denominator) for the exponents with this k."""
    out = []
    for l in range(1, 9):
        if l * N + 2 * D * k <= 2 * D:              # l delta/2 + k > 1 fails
            continue
        if (l, k) == (5, 0):
            continue
        num, den = abs((l - 5) * N + 2 * D * k), (l + 5) * N + 2 * D * (k - 2)
        assert 0 < num < den, (l, k)
        out.append((num, den))
    return out


pref = E4 / arb(2).sqrt() * (arb(D) / (5 * N - 2 * D)).sqrt()
prod = arb(1)
for k in range(0, 5):                               # K = 0: k = 0, ..., 4
    for num, den in factors(k):
        prod *= arb(num) / den
lb = {0: pref * prod}
KMAX = 26000
for K in range(1, KMAX + 1):
    for k in (2 * K + 3, 2 * K + 4):
        for num, den in factors(k):
            prod *= arb(num) / den
    lb[K] = pref * prod
print("(a) all", sum(len(factors(k)) for k in range(0, 2 * KMAX + 5)), "factors up to K =", KMAX,
      "are in (0, 1): the bound decreases strictly in K")

# (b) anchors of T4-027 / T4-029
s19 = Q(1, 2**17)
fac19 = (1 - 34 * arb(s19.numerator) / s19.denominator) * 512
eta19 = arb(1) / 163840
print("(b) T4-019 box anchors: floor (1 - 34 s) 512 ||F||_2 lower bound, s = 2^-17:")
for K, ref in ((150, "0.1083720980773968"), (10000, "3.745607591802169e-5"), (25929, "6.103834828383889e-6"),
               (25930, "6.103386574210375e-6")):
    v = fac19 * lb[K]
    print(f"    K = {K}: {v.str(16)}  (T4-027: {ref}); above eta = 1/163840: {bool(v > eta19)}")
    assert abs(float(v.mid().str(20, radius=False)) / float(ref) - 1) < 1e-14
assert fac19 * lb[25929] > eta19 and fac19 * lb[25930] < eta19

# (c) T4-043 cutoffs for the T2-R3 balls
for name, eta, sw2 in (("FW-T-T4L2-sharp-v1", Q(76219, 10**9), 512), ("FW-T-T4L2-sharpw-v1", Q(4207, 2 * 10**7), 1024)):
    et = arb(eta.numerator) / eta.denominator
    ratio = {K: sw2 * lb[K] / et for K in lb}
    excl = [K for K in lb if ratio[K] > 1]
    Kc = max(excl)
    assert excl == list(range(0, Kc + 1)) and ratio[Kc + 1] < 1
    print(f"(c) {name}: sqrt(w2) ||F||_2 lower bound / eta > 1 for K <= {Kc}: ratio at K = {Kc}: {ratio[Kc].str(16)},"
          f" at K = {Kc + 1}: {ratio[Kc + 1].str(16)}")
print("done")
