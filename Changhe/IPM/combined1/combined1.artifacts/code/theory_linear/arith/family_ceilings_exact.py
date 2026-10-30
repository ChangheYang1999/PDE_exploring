"""Exact family ceilings (NC-T-DIST budgets of theory_v03) against the one-unit brackets below each printed ceiling
that FALSIFY_ENDPOINT_AND_SECTION0 section 1 and CHECK_T1_v08_FACTORS assume (c1-t4 T4-443 repair 5): FW-A2-Db,
TB-rebal, bL at beta_L = 1 and 7/5, sharpw, sharp, TB-sharp; and the graded ceiling against [45697/10^8, 25/54684].
The brackets are those of data/falsify_section0_results.json.
Finding: for TB-rebal the printed 3.5125e-7 is below b_fam (rounded to nearest, not up); asserted as such.

Run from artifacts/:  python3 -B -u arith/family_ceilings_exact.py
Takes no arguments. Needs python-flint (arb). Reads (read only, hash-bound): theory_v01.md and theory_v03.md of
../../c1-shared/theory_requirements, and this lane's arith/distance_budget_update.py.
b_fam = sup over s > 0 of (mu0 - C s) sqrt(s)/(c_U sqrt(W2)) = (2 mu0/3) sqrt(mu0/(3C))/(c_U sqrt(W2)) (theory_v03
NC-T-DIST, printed rounded up). Parameters (mu0, C, c_U) from the rate rows of theory_v01 and theory_v03 (quoted
below); where a row elides C, and for sqrt(W2), from arith/distance_budget_update.py (AUDITED T4-065): 2^10 for the
(2^15, 2^20) weights of sharpw and bL, 512 otherwise.
Output: logs/family_ceilings_exact.log, data/family_ceilings_exact_results.json.
"""
import hashlib
import json
import sys
import time
from decimal import Decimal
from fractions import Fraction as Q
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: family_ceilings_exact.py (no arguments)")
t0 = time.time()
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]
R6 = HERE.parents[1]
TR = R6 / "c1-shared/theory_requirements"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
A = lambda x: arb(Q(x).numerator) / Q(x).denominator
N, FAILS, OUT = [0], [], {"inputs": {}}


def check(name, ok):
    N[0] += 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


V1, V3, DB = TR / "theory_v01.md", TR / "theory_v03.md", HERE / "arith/distance_budget_update.py"
for p_ in (V1, V3, DB):
    OUT["inputs"][str(p_.relative_to(R6))] = sha(p_)
check("sha256 theory_v03", sha(V3) == "e541f3ba19c8a67d51c5792600a461c971cc8575eab18ffeb07cc9a29c2e0b19")
f1, f3, fdb = (" ".join(p_.read_text().split()) for p_ in (V1, V3, DB))
Q3 = ["b_fam = sup over s of (mu0 - C s) sqrt(s)/(c_U sqrt(W2)) = (2 mu0/3) sqrt(mu0/(3C))/(c_U sqrt(W2)).",
      "Budgets b_fam (rounded up): baseline FW-A2-Db 6.8626e-8, FW-T-TB-rebal-v1 3.5125e-7, FW-T-TB-sharp-v1 3.7930e-6,",
      "FW-T-T4L2-sharpw-v1 2.8496e-6",
      "| FW-T-T4L2-sharpw-v1 | 97/250 - 397 s - (8/5) X(k)/sqrt(s);",
      "NORM-T-Xw5184-v1 = NORM-T-XSW-v1[1/5184, 2^15, 2^20]"]
for q_ in Q3:
    check("theory_v03 contains '%s'" % q_[:70], q_ in f3)
q1 = "| FW-T-TB-sharp-v1 | rate 297/1000 - 402 s - (8/5) N_s(k)/sqrt(s);"
check("theory_v01 contains '%s'" % q1, q1 in f1)
for qdb in ('("baseline-gap balls (A2, T4ALT)", Q(1, 10), 4800, Q(5), 512)', '("FW-T-TB-rebal-v1", Q(297, 1000), 4800, Q(5), 512)',
            '("FW-T-TB-sharp-v1", Q(297, 1000), 402, Q(8, 5), 512)', '("FW-T-T4L2-sharp-v1", Q(259, 1000), 401, Q(8, 5), 512)',
            '("FW-T-T4L2-sharpw-v1", Q(97, 250), 397, Q(8, 5), 1024)'):
    check("distance_budget_update.py has %s" % qdb, qdb in fdb)
for q_ in ("| FW-A2-Db | rate 1/10 - 4800 s - 5 N_s(k)/sqrt(s);", "| FW-T-TB-rebal-v1 | rate 297/1000 - ...; K_H <= 10 | d = 6.612e-3; ratio 1.74e-3 | 5 |"):
    check("theory_v01 contains '%s'" % q_[:70], q_ in f1)
for q_ in ("| FW-T-T4L2-sharp-v1 | 259/1000 - 401 s - (8/5) X(k)/sqrt(s);", "| FW-T-T4L2-bL-v1[7/5, sharpw] | 359/1000 - 397 s - ...;",
           "| FW-T-T4L2-bL-v1[1, sharpw] | 151/500 - 397 s - ...;", "| 8/5 | 1.692e-4 (s = 1/5476) |", "| 8/5 | 1.066e-4 (s = 1/6561) |",
           "NORM-T-XSW-v1[1/5476, 2^15, 2^20]", "NORM-T-XSW-v1[1/6561, 2^15, 2^20]",
           "FW-T-T4L2-bL-v1 at beta_L = 7/5 2.5362e-6 and at beta_L = 1 1.9568e-6 (c1-t1, same formula)"):
    check("theory_v03 contains '%s'" % q_[:70], q_ in f3)
RADK = json.loads((HERE / "data/falsify_section0_results.json").read_text())["B"]["radii"]
OUT["inputs"]["c1-t2/artifacts/data/falsify_section0_results.json"] = sha(HERE / "data/falsify_section0_results.json")
br = lambda k: (Q(RADK[k]["beta_lower"]), Q(RADK[k]["beta_upper"]))
FAM = {"FW-A2-Db": (Q(1, 10), 4800, Q(5), 512) + br("FW-A2-Db family ceiling (6.8626e-8)") + ("6.8626e-8",),
       "TB-rebal": (Q(297, 1000), 4800, Q(5), 512) + br("FW-T-TB-rebal-v1 family ceiling (3.5125e-7)") + ("3.5125e-7",),
       "bL, beta_L = 1": (Q(151, 500), 397, Q(8, 5), 2**10)
       + br("FW-T-T4L2-bL-v1 family ceiling, beta_L = 1 (1.9568e-6)") + ("1.9568e-6",),
       "bL, beta_L = 7/5": (Q(359, 1000), 397, Q(8, 5), 2**10)
       + br("FW-T-T4L2-bL-v1 family ceiling, beta_L = 7/5 (2.5362e-6)") + ("2.5362e-6",),
       "sharpw": (Q(97, 250), 397, Q(8, 5), 2**10) + br("FW-T-T4L2-sharpw-v1 family ceiling (2.8496e-6)") + ("2.8496e-6",),
       "sharp": (Q(259, 1000), 401, Q(8, 5), 512) + br("FW-T-T4L2-sharp-v1 family ceiling (3.0927e-6)") + ("3.0927e-6",),
       "TB-sharp": (Q(297, 1000), 402, Q(8, 5), 512) + br("FW-T-TB-sharp-v1 family ceiling (3.7930e-6)") + ("3.7930e-6",)}
OUT["ceilings"] = {}
ABOVE = {"TB-rebal"}
for name, (mu0, C, cU, sw, lo, hi, printed) in FAM.items():
    b = (2 * A(mu0) / 3) * (A(mu0) / (3 * C)).sqrt() / (A(cU) * sw)
    OUT["ceilings"][name] = {"mu0": str(mu0), "C": C, "c_U": str(cU), "sqrt_W2": sw, "b_fam": b.str(25),
                             "bracket": [str(lo), str(hi)]}
    print("    %s: b_fam = %s" % (name, b.str(25)))
    unit = Q(10) ** (Decimal(printed).as_tuple().exponent)
    inb = bool(A(lo) < b and b < A(hi))
    above = bool(A(hi) < b and b < A(hi + unit))
    OUT["ceilings"][name].update(in_bracket=inb, printed_is_upper_bound=bool(b < A(hi)))
    if name in ABOVE:
        # finding (run 3, 13:54:41Z): the printed value is below b_fam, so it is not 'rounded up'
        check("%s: printed %s < b_fam < printed + %s (printed is NOT an upper bound)" % (name, printed, unit), above)
    else:
        check("%s: %s < b_fam < %s (strict, Arb)" % (name, lo, hi), inb)
    check("%s: the bracket is one printed unit (%s) below the printed %s" % (name, unit, printed),
          hi == Q(Decimal(printed)) and hi - lo == unit)
g = A(Q(50, 651)) / arb(28248).sqrt()
OUT["ceilings"]["graded"] = {"b_fam": g.str(25), "bracket": ["45697/10^8", "25/54684"]}
print("    graded: 50/(651 sqrt 28248) = %s" % g.str(25))
check("graded: 45697/10^8 < 50/(651 sqrt 28248) < 25/54684", A(Q(45697, 10**8)) < g and g < A(Q(25, 54684)))
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N[0], FAILS, round(time.time() - t0, 3)
(HERE / "data/family_ceilings_exact_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
