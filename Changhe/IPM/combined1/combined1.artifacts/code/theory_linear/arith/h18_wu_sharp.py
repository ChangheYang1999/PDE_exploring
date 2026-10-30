"""Sharpened Proposition WU (WU3): the weight-uniform L2 budget from the full 3x3 determinant of G(mu0).

Setting and hypotheses as in Proposition WU (T2_FINAL_SUMMARY section 2.4, handoff BH3; arith/h18_item2_check.py part
(D)), which used only the 2x2 principal minors. Here, with p = m2 - mu, a = m1 - mu, c = beta - mu, q = w1 a - 40:
    det G = w2 c (p q - (347/10)^2) - 9 p w1^2 - 1041 w1 - 25 q,
so G is positive semidefinite only if p q > (347/10)^2 and w2 >= F(w1; mu) := N(w1; mu)/D(w1; mu), with
    N = 9 p w1^2 + (1041 + 25 a) w1 - 1000,   D = c (p a w1 - 40 p - (347/10)^2).
For mu in a cell [mu_a, mu_b] and every w1 with D(w1; mu) > 0: N(w1; mu) >= N(w1; mu_b) > 0 and
0 < D(w1; mu) <= D(w1; mu_a), since p, a, c decrease in mu. So w2 >= min over w1 of N(w1; mu_b)/D(w1; mu_a). For
alpha w1^2 + beta w1 + gamma over delta w1 - eps (alpha > 0, delta > 0) the minimum over w1 > eps/delta is at the
positive root w1* of alpha delta w1^2 - 2 alpha eps w1 - (beta eps + delta gamma) = 0 and equals
(2 alpha w1* + beta)/delta. The budget on the cell is at most (2 mu_b/3) sqrt(mu_b/(3 K00))/((A' + B') sqrt(w2lo)),
w2lo = max(1, that minimum), also capped by the 2x2 bound of part (D). All in Arb with exact rational cell ends.

Run from artifacts/:  python3 -B -u arith/h18_wu_sharp.py
Takes no arguments. Needs python-flint. Reads arith/h18_item2_check.py, data/h18_item2_check_results.json and
data/family_ceilings_exact_results.json (sha256 asserted) and data/h18_wu_sampling_results.json (sha256 recorded); the
constant formulas are copied from h18_item2_check.py.
Output: stdout (logs/h18_wu_sharp.log by the README command), data/h18_wu_sharp_results.json.
"""
import hashlib
import json
import math
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: h18_wu_sharp.py (no arguments)")
t0 = time.time()
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
A_ = lambda q: arb(q.numerator) / q.denominator
N_, FAILS = [0], []


def check(name, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


PIN = {HERE / "arith/h18_item2_check.py": "7a166d26300643a7ecafdb6e098f5ebbf14119396b1f7ef6edba57e39db13d63",
       HERE / "data/h18_item2_check_results.json": "7b19020e14e7fe84e4b2ad823e4b7d64dbf3788fa3f4775daba6aed1838f30a2",
       HERE / "data/family_ceilings_exact_results.json": "b1fea0a74af0a7729b38a27f1796deea0b3597b4ca9549ba235e9131af3b98a7"}
SAMP = HERE / "data/h18_wu_sampling_results.json"
for p, h in PIN.items():
    check("sha256 of %s is %s...%s" % (p.relative_to(HERE), h[:8], h[-8:]), sha(p) == h)
src = (HERE / "arith/h18_item2_check.py").read_text()
RES1 = json.loads((HERE / "data/h18_item2_check_results.json").read_text())
SR = json.loads(SAMP.read_text())
FC = json.loads((HERE / "data/family_ceilings_exact_results.json").read_text())["ceilings"]
OUT = {"inputs": {str(p.relative_to(HERE)): sha(p) for p in list(PIN) + [SAMP]}}

# constants: copied from h18_item2_check.py part (D)
CP = ["m1k = SQPI / 2 * arb.gamma((1 - SMAX) / 2)",
      "w1c = arb(8) * arb(5).sqrt() / 5 * arb(6) ** (arb(-3) / 5)",
      "k1u, k1w = m1k, m1k + arb(8) / 5",
      "cru, crw = arb(3) / 2 * m1k, arb(3) / 2 * m1k + arb(32) / 15",
      "c8, dtop = 1 + w1c * 3 * PI / 4, 1 + w1c * PI / 2",
      "Cc, U1, U2, U3, R1, R2, R3, R4 = [arb(x) for x in (2, 6, 24, 160, 22, 32, 80, 2048)]",
      "K00 = dtop * Cc + c8 * U1 + (crw + 2 * k1w) * U2 + k1w * R2",
      "ps = arb(2) ** s_ * (1 + s_).sqrt() / (2 * SQPI)",
      "Pw = ps * (1 + w1c * m1k * s_) + w1c * m1k * s_ / (2 * SQPI)",
      "Ap = arb(4) / 5 * q_ + q_ * (1 + 4 * w1c * m1k * s_) + 2 * Pw",
      "Bp = arb(9) / 5 * Pw"]
check("the %d constant lines below are copied verbatim from h18_item2_check.py" % len(CP), all(c in src for c in CP))
PI = arb.pi()
SQPI = PI.sqrt()
SMAX = arb(1) / 1024
m1k = SQPI / 2 * arb.gamma((1 - SMAX) / 2)
w1c = arb(8) * arb(5).sqrt() / 5 * arb(6) ** (arb(-3) / 5)
k1u, k1w = m1k, m1k + arb(8) / 5
cru, crw = arb(3) / 2 * m1k, arb(3) / 2 * m1k + arb(32) / 15
c8, dtop = 1 + w1c * 3 * PI / 4, 1 + w1c * PI / 2
Cc, U1, U2, U3, R1, R2, R3, R4 = [arb(x) for x in (2, 6, 24, 160, 22, 32, 80, 2048)]
K00 = dtop * Cc + c8 * U1 + (crw + 2 * k1w) * U2 + k1w * R2
s_ = SMAX
q_ = 1 / (2 * SQPI)
ps = arb(2) ** s_ * (1 + s_).sqrt() / (2 * SQPI)
Pw = ps * (1 + w1c * m1k * s_) + w1c * m1k * s_ / (2 * SQPI)
Ap = arb(4) / 5 * q_ + q_ * (1 + 4 * w1c * m1k * s_) + 2 * Pw
Bp = arb(9) / 5 * Pw
K_lo, cU_lo = arb(K00.lower()), arb((Ap + Bp).lower())
check("K00 and A' + B' lower ends equal those of h18_item2_check (%s, %s)" % (RES1["D"]["K00_lower"], RES1["D"]["cU_lower"]),
      K_lo.str(15) == RES1["D"]["K00_lower"] and cU_lo.str(15) == RES1["D"]["cU_lower"])
O12 = Fr(347, 10)**2


def numer(mu):
    m = A_(mu)
    return 2 * m / 3 * (m / (3 * K_lo)).sqrt()


def w2min2(mu, m2, m1, bL):
    Alo = O12 / (m2 - mu)
    w1lo = (Alo + 40) / (m1 - mu)
    return max(Fr(1), Fr(25) / ((m2 - mu) * (bL - mu)), 9 * w1lo**2 / (Alo * (bL - mu)))


def w2lo3(ma, mb, m2, m1, bL):
    """lower bound (arb) of min over w1 of F(w1; mu) for all mu in [ma, mb], or None if not applicable."""
    pa, aa, ca = m2 - ma, m1 - ma, bL - ma
    pb, ab = m2 - mb, m1 - mb
    if pb <= 0:
        return None
    al, be, ga = 9 * pb, 1041 + 25 * ab, Fr(-1000)
    de, ep = ca * pa * aa, ca * (40 * pa + O12)
    disc = (al * ep)**2 + al * de * (be * ep + de * ga)
    assert al > 0 and de > 0 and disc > 0
    x0 = ep / de
    assert al * x0**2 + be * x0 + ga > 0          # N(w1; mb) > 0 on w1 > eps/delta (N increases there)
    w1s = (A_(al * ep) + A_(disc).sqrt()) / A_(al * de)
    assert w1s > A_(x0)
    return (2 * A_(al) * w1s + A_(be)) / A_(de)


ROWS = [("T2-R3, registered floors, beta 2", Fr(1, 2), Fr(9, 10), Fr(2), "sharpw", 0),
        ("TB-sharp E0, registered floors, beta 11/4", Fr(1, 2), Fr(9, 10), Fr(11, 4), "TB-sharp", 1),
        ("T2-R3, state-131 floor ceilings, beta 2 (hypothetical)", Fr(61151, 10**5), Fr(99116, 10**5), Fr(2), "sharpw", None),
        ("TB-sharp E0, state-131 floor ceilings, beta 11/4 (hypothetical)", Fr(61151, 10**5), Fr(99116, 10**5), Fr(11, 4),
         "TB-sharp", None),
        ("T2-R3, state-131 floor ceilings, beta 4 (hypothetical)", Fr(61151, 10**5), Fr(99116, 10**5), Fr(4), "sharpw", None)]
D007 = Fr(4769166867, 10**12)
NC = 20000
OUT["rows"] = []
for lab, m2, m1, bL, reg, si in ROWS:
    best, arg, n3 = arb(0), None, 0
    for k in range(NC):
        ma, mb = m2 * Fr(k, NC), m2 * Fr(k + 1, NC)
        cand = numer(mb) / (cU_lo * A_(w2min2(ma, m2, m1, bL)).sqrt())
        w3 = w2lo3(ma, mb, m2, m1, bL)
        if w3 is not None:
            n3 += 1
            w3m = w3 if w3 > 1 else arb(1)
            c3 = numer(mb) / (cU_lo * w3m.sqrt())
            if c3.upper() < cand.upper():
                cand = c3
        if cand.upper() > best.upper():
            best, arg = arb(cand.upper()), (ma, mb)
    m_, e_ = best.mid().man_exp()
    bu = Fr(int(m_)) * Fr(2)**int(e_)
    bu5 = Fr(math.ceil(bu * 10**10), 10**10)          # upward to 1e-10 absolute
    gain = (A_(bu5) / arb(FC[reg]["b_fam"])).upper()          # over the exact registered family ceiling
    fac = D007 / bu5
    row = {"label": lab, "Bstar3_upper": str(bu5), "Bstar3_upper_dec": "%.10f" % float(bu5),
           "argmax_cell": [str(arg[0]), str(arg[1])], "cells": NC, "cells_with_3x3": n3,
           "over_registered_%s_upper" % reg: "%.4f" % (math.ceil(float(gain) * 10**4 * (1 + 1e-12)) / 10**4),
           "factor_007_lower": "%.1f" % (math.floor(float(fac) * 10) / 10)}
    if si is not None:
        old = Fr(RES1["D"]["rows"][si]["Bstar_upper"])
        smp = SR["rows"][si]["sampled_max_float"]
        check("%s: WU3 bound %.6e <= WU bound %s" % (lab, float(bu5), RES1["D"]["rows"][si]["Bstar_upper"]), bu5 <= old)
        check("%s: WU3 bound >= the largest sampled exactly-PD budget %.6e (FLOAT)" % (lab, smp), float(bu5) >= smp)
        row["sampled_max_float"] = smp
        row["sampled_over_bound"] = smp / float(bu5)
    OUT["rows"].append(row)
    print("  %s: B*3 <= %.4e (cells %d, 3x3 used in %d, argmax cell [%.5f, %.5f]); over registered %s <= %s; "
          "007 distance / B*3 >= %s%s" % (lab, float(bu5), NC, n3, float(arg[0]), float(arg[1]), reg,
                                        row["over_registered_%s_upper" % reg], row["factor_007_lower"],
                                        ("; sampled / bound = %.4f" % row["sampled_over_bound"]) if si is not None else ""))
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N_[0], FAILS, round(time.time() - t0, 3)
(HERE / "data/h18_wu_sharp_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N_[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
