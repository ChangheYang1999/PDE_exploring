"""c1-t1 R1-024: exact side conditions of T4-199 (potential-to-density injectivity) for candidate 007.

Run from artifacts/checks:
  python3 -B check_T4199.py > check_T4199.out

The analytic proof is reviewed by hand in nonlinear_closure/REVIEWS_v20.md. This script checks only the exact
hypotheses: (1) every generator of the 007 snapshot is H_m (1+r^2)^(p_j-m) T(t) with j in 0..7, integer m >= 0 and a
polynomial T (spec 'mono' t^h or 'leg' t^w P_n(2t-1), integers h, w, n >= 0; no explicit p, no 'legq' or 'legqs');
(2) the snapshot c equals the c of T4-199; (3) d = max 2 p_j = 3 + gamma < 4; (4) no p_j is an integer and no
difference p_j - p_k (j != k) is an integer; (5) c, gamma, delta and the p_j agree with c1-t4
verification/parameters.json (copy data/T4199_parameters.json, sha256 checked). Input:
data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json (sha256 checked; copy of the c1-shared 007 snapshot).
"""
import collections
import hashlib
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.set_int_max_str_digits(0)
SNAP = Path("data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json")
SNAP_SHA = "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21"
assert hashlib.sha256(SNAP.read_bytes()).hexdigest() == SNAP_SHA
d = json.loads(SNAP.read_text())
g = d["generators"]
c = Fr(4076476460239181, 2**51)
assert Fr(d["cl_exact"]) == c
gamma, delta = 1 / c, 1 - 1 / c
p = {j: (3 + gamma - j * delta) / 2 for j in range(8)}
PAR = Path("data/T4199_parameters.json")
PAR_SHA = "eb73db2c8ba7849fd0738f9ce9e6510c548bbd3443952b2748c88e9e5f74d85f"
assert hashlib.sha256(PAR.read_bytes()).hexdigest() == PAR_SHA
par = json.loads(PAR.read_text())
assert Fr(par["c"]) == c and Fr(par["gamma"]) == gamma and Fr(par["delta"]) == delta
T4 = par["p_j"]
assert all(p[j] == Fr(T4[str(j)]) for j in range(8))
print(f"snapshot sha256 {SNAP_SHA}; {len(g)} generators; c = {c} (equals T4-199 c)")
bad = []
for x in g:
    s = x["spec"]
    ok = set(x) == {"coef", "coef_float", "j", "m", "spec"} and isinstance(x["j"], int) and 0 <= x["j"] <= 7
    ok = ok and isinstance(x["m"], int) and x["m"] >= 0
    ok = ok and ((s[0] == "mono" and len(s) == 2 and isinstance(s[1], int) and s[1] >= 0)
                 or (s[0] == "leg" and len(s) == 3 and all(isinstance(v, int) and v >= 0 for v in s[1:])))
    if not ok:
        bad.append(x)
assert not bad, bad[:3]
print("(1) every generator: keys {coef, coef_float, j, m, spec}, j in 0..7, m >= 0, spec mono/leg with nonnegative"
      " integers:", not bad)
print("    branch counts", dict(sorted(collections.Counter(x["j"] for x in g).items())),
      "spec counts", dict(collections.Counter(x["spec"][0] for x in g)),
      "m range", min(x["m"] for x in g), max(x["m"] for x in g))
dmax = max(2 * v for v in p.values())
assert dmax == 3 + gamma and dmax < 4 and delta > 0
print(f"(3) d = max 2 p_j = 3 + gamma = {float(dmax):.12f} < 4; delta = {delta} > 0")
assert all(v.denominator != 1 for v in p.values())
diffs = [(j, k, p[j] - p[k]) for j in range(8) for k in range(j + 1, 8)]
assert len(diffs) == 28 and all(v.denominator != 1 for _, _, v in diffs)
print("(4) p_j nonintegral for j = 0..7; all 28 differences nonintegral; denominators of p_j:",
      sorted(set(v.denominator for v in p.values())))
print("    gcd checks: delta in lowest terms", delta.denominator == 4076476460239181,
      "| max |p_j - p_k| =", float(max(abs(v) for _, _, v in diffs)))
print(f"(5) c, gamma, delta, p_0..p_7 equal to c1-t4 parameters.json (sha256 {PAR_SHA}): True")
