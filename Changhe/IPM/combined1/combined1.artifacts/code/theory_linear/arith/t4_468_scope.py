"""Scope of the six-digit suprema of REVIEW_T4_462 (c1-t4 T4-468, TEAM_NOTE_v245: 'these new suprema are for
equation (8) with k=390.68 and u=1.5871').

The right side of PROOF.md (8) of T4-462 is 4 mu^3 c p a^2 / (27 k u^2 (1440 p + (6O + 5a)^2)), so k and u enter only
through the factor 1/(k u^2). Replacing the rational lower bounds k = 39068/100 and u = 15871/10000 by the Arb values
K (= c1-t2's K00) and v (= A' + B') of T4-462's verification/result.json multiplies the supremum of (8) exactly by
k u^2 / (K v^2), and its square root by f = sqrt(k/K) u/v. This script takes the enclosure of REVIEW_T4_462
(witness <= sqrt sup <= witness (1 + 1e-7), the witness stored to 11 significant digits, hence widened by half a unit
of the 11th digit) and multiplies it by f in 300-bit ball arithmetic. Output: the six-digit values for (8) at the
exact constants. Both problems are relaxations; neither is the full T2-R3 prescription with its weight-dependent
commutator terms.

Run from artifacts/:  python3 -B -u arith/t4_468_scope.py
Takes no arguments. Needs python-flint. Reads, read only: data/review_t4_462_results.json (sha256 asserted),
../../c1-t4/research/weight_uniform_gram_audit/verification/result.json (sha256 asserted, as pinned in
arith/review_t4_462.py). Output: stdout (logs/t4_468_scope.log by the README command), data/t4_468_scope_results.json.
"""
import hashlib
import json
import sys
import time
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: t4_468_scope.py (no arguments)")
T0 = time.time()
ctx.prec = 300
HERE_ = Path(__file__).resolve().parents[1]
SH = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
FAILS, N = [], [0]


def check(msg, ok):
    N[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


REV = HERE_ / "data/review_t4_462_results.json"
H_REV = "7235a4039afa60b237ec53bc3b62747cd9a9618bcf6c58dc448d9a13c7e104ab"
RJ = HERE_.parent.parent / "c1-t4/research/weight_uniform_gram_audit/verification/result.json"
H_RJ = "61803920bea366913555ebb213ac40b466d370b1c92dd5cfe9cc9b67b9895450"
check("sha256 of data/review_t4_462_results.json is %s...%s" % (H_REV[:8], H_REV[-8:]), SH(REV) == H_REV)
check("sha256 of T4-462 verification/result.json is %s...%s" % (H_RJ[:8], H_RJ[-8:]), SH(RJ) == H_RJ)
R, RES = json.loads(REV.read_text()), json.loads(RJ.read_text())
K, v = arb(RES["K"]), arb(RES["v"])
k, u = arb(39068) / 100, arb(15871) / 10000
check("k = 390.68 < K = %s and u = 1.5871 < v = %s" % (K.str(12), v.str(12)), bool(k < K) and bool(u < v))
f = (k / K).sqrt() * u / v
check("f = sqrt(k/K) u/v = %s, 1 - f = %s" % (f.str(12), (1 - f).str(6)), bool(f < 1) and bool(1 - f < arb("1.7e-5")))
OUT = {"inputs": {"data/review_t4_462_results.json": H_REV,
                  "c1-t4/research/weight_uniform_gram_audit/verification/result.json": H_RJ},
       "factor_sqrt": f.str(15), "rows": []}
for r in R["rows"]:
    w = arb(r["sup_lower_witness"])
    half = arb(5) * arb(10) ** (arb(int(f"{float(r['sup_lower_witness']):e}".split("e")[1])) - 11)
    lo0, hi0 = w - half, (w + half) * (1 + arb("1e-7"))
    lo, hi = lo0 * f, hi0 * f
    six0 = "%.5e" % float(r["sup_lower_witness"])
    sixa, sixb = "%.5e" % float(lo.lower()), "%.5e" % float(hi.upper())
    check("%-9s sqrt sup of (8) at k, u in [%s, %s] (six digits %s); at K, v in [%s, %s], six digits %s"
          % (r["label"], lo0.lower().str(10, radius=False), hi0.upper().str(10, radius=False), six0,
             lo.lower().str(10, radius=False), hi.upper().str(10, radius=False), sixa),
          sixa == sixb and bool(lo < hi) and six0 == "%.5e" % float(lo0.lower()) == "%.5e" % float(hi0.upper()))
    OUT["rows"].append({"label": r["label"], "six_digits_at_k_u": six0, "six_digits_at_K_v": sixa,
                        "enclosure_at_K_v": [lo.lower().str(12, radius=False), hi.upper().str(12, radius=False)]})
OUT.update(checks=N[0], fails=FAILS, elapsed_s=round(time.time() - T0, 3))
(HERE_ / "data/t4_468_scope_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("%d checks, %d FAIL, %.2f s" % (N[0], len(FAILS), time.time() - T0))
sys.exit(1 if FAILS else 0)
