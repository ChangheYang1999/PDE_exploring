"""Falsification test of Proposition WU (T2_FINAL_SUMMARY section 2.4, handoff BH3) by direct sampling.

For mu0 on a grid of (0, 1/2) and w1 on a log2 grid, find (by bisection on log2 w2) the least w2 on a 1/64-octave grid
for which the full 3x3 matrix G(mu0) is positive definite, confirm positive definiteness there by exact rational
leading minors, and evaluate the budget (2 mu0/3) sqrt(mu0/(3 K00))/((A' + B') sqrt(w2)) with the lower ends of K00 and
A' + B' from data/h18_item2_check_results.json. Every sampled budget must be below the proved bound B*; the largest
sampled value shows how close B* is to being attained (FLOAT, a sampled lower estimate of the true supremum, not a
bound).

Run from artifacts/:  python3 -B -u arith/h18_wu_sampling.py
Takes no arguments; standard library only. Reads data/h18_item2_check_results.json (sha256 asserted).
Output: stdout (logs/h18_wu_sampling.log by the README command), data/h18_wu_sampling_results.json.
"""
import hashlib
import json
import math
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

if len(sys.argv) != 1:
    sys.exit("usage: h18_wu_sampling.py (no arguments)")
t0 = time.time()
HERE = Path(__file__).resolve().parents[1]
RES = HERE / "data/h18_item2_check_results.json"
H_RES = "7b19020e14e7fe84e4b2ad823e4b7d64dbf3788fa3f4775daba6aed1838f30a2"
N, FAILS = [0], []


def check(name, ok):
    N[0] += 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


check("sha256 of data/h18_item2_check_results.json is 7b19020e...838f30a2",
      hashlib.sha256(RES.read_bytes()).hexdigest() == H_RES)
R = json.loads(RES.read_text())
# lower ends, as printed by the Arb str of h18_item2_check.py: '[m +/- r]' or an exact decimal
def lower_of(sv):
    sv = sv.strip("[]")
    if "+/-" in sv:
        m, r = sv.split("+/-")
        return float(Fr(m.strip()) - Fr(r.strip()))
    return float(Fr(sv))


K00 = lower_of(R["D"]["K00_lower"])
CU = lower_of(R["D"]["cU_lower"])
check("K00 lower end in (390.68, 390.69) and A' + B' lower end in (1.5871, 1.5872)",
      390.68 < K00 < 390.69 and 1.5871 < CU < 1.5872)


def G(mu, w1, w2, m2, m1, bL):
    return [[m2 - mu, Fr(-347, 10), Fr(-5)], [Fr(-347, 10), w1 * (m1 - mu) - 40, -3 * w1], [Fr(-5), -3 * w1, w2 * (bL - mu)]]


def pd_exact(g):
    d1 = g[0][0]
    d2 = g[0][0] * g[1][1] - g[0][1] * g[1][0]
    d3 = (g[0][0] * (g[1][1] * g[2][2] - g[1][2] * g[2][1]) - g[0][1] * (g[1][0] * g[2][2] - g[1][2] * g[2][0])
          + g[0][2] * (g[1][0] * g[2][1] - g[1][1] * g[2][0]))
    return d1 > 0 and d2 > 0 and d3 > 0


def pd_float(mu, w1, w2, m2, m1, bL):
    a, b, c = m2 - mu, -34.7, -5.0
    d, e, f = w1 * (m1 - mu) - 40, -3 * w1, w2 * (bL - mu)
    d2 = a * d - b * b
    d3 = a * (d * f - e * e) - b * (b * f - e * c) + c * (b * e - d * c)
    return a > 0 and d2 > 0 and d3 > 0


def budget(mu, w2):
    return (2 * mu / 3) * math.sqrt(mu / (3 * K00)) / (CU * math.sqrt(w2))


OUT = {"rows": []}
for idx, (lab, m2, m1, bL) in enumerate((("T2-R3, beta_L 2", Fr(1, 2), Fr(9, 10), Fr(2)),
                                         ("TB-sharp E0, beta 11/4", Fr(1, 2), Fr(9, 10), Fr(11, 4)))):
    Bstar = float(Fr(R["D"]["rows"][idx]["Bstar_upper"]))
    best, nchk, nexact = (0.0, None), 0, 0
    for i in range(1, 400):
        mu = m2 * Fr(i, 400)
        muf = float(mu)
        for j in range(4, 30 * 16 + 1):
            l1 = Fr(j, 16)
            w1f = 2.0**float(l1)
            if not (0.5 - muf) * (w1f * (float(m1) - muf) - 40) > 34.7**2:
                continue
            lo_, hi_ = 0, 60 * 64          # log2 w2 in 1/64 steps, w2 in [1, 2^60]
            if not pd_float(muf, w1f, 2.0**60, float(m2), float(m1), float(bL)):
                continue
            while hi_ - lo_ > 1:
                mid = (lo_ + hi_) // 2
                if pd_float(muf, w1f, 2.0**(mid / 64), float(m2), float(m1), float(bL)):
                    hi_ = mid
                else:
                    lo_ = mid
            k = hi_ if not pd_float(muf, w1f, 1.0, float(m2), float(m1), float(bL)) else 0
            v = budget(muf, 2.0**(k / 64))
            nchk += 1
            if v > best[0]:
                # exact confirmation on a dyadic-rational stand-in: w1 = floor(2^l1 * 2^20) / 2^20, w2 = ceil(...) / 2^20
                w1e = Fr(math.floor(w1f * 2**20), 2**20)
                w2e = Fr(math.ceil(2.0**(k / 64) * 2**20), 2**20)
                if pd_exact(G(mu, w1e, w2e, m2, m1, bL)):
                    nexact += 1
                    best = (budget(muf, float(w2e)), (str(mu), float(w1e), float(w2e)))
    ok = best[0] < Bstar
    check("%s: every exactly positive-definite sampled point has budget < B* = %s (largest sampled %.6e, FLOAT)"
          % (lab, R["D"]["rows"][idx]["Bstar_upper"], best[0]), ok)
    OUT["rows"].append({"label": lab, "Bstar_upper": R["D"]["rows"][idx]["Bstar_upper"], "sampled_max_float": best[0],
                        "at_mu0_w1_w2": best[1], "ratio_sampled_over_Bstar": best[0] / Bstar,
                        "points_sampled": nchk, "exact_confirmations": nexact})
    print("  %s: sampled %d points; largest budget %.6e at mu0 %s, w1 %.6g, w2 %.6g; %.4f of B*"
          % (lab, nchk, best[0], best[1][0], best[1][1], best[1][2], best[0] / Bstar))
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N[0], FAILS, round(time.time() - t0, 3)
(HERE / "data/h18_wu_sampling_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
