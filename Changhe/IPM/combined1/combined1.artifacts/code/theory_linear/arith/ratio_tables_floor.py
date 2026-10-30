"""Distance-to-budget ratio tables of this lane against their exact floors: T2_FINAL_SUMMARY section 5, handoff O3
and REVIEW_T4ALT C4. A printed ratio is a valid lower bound when it is <= the exact ratio; the rule of the run is the
floor at the printed digit.

Run from artifacts/:  python3 -B -u arith/ratio_tables_floor.py
Takes no arguments. Needs python-flint (arb). Reads (read only): ../notes/T2_FINAL_SUMMARY.md (the section 5 rows are
parsed from the current file), ../handoff/T2_to_T1_v01.md (the O3 rows, asserted verbatim), ../reviews/REVIEW_T4ALT.md
(hash-bound) and data/family_ceilings_exact_results.json (exact b_fam).
- Summary section 5 divides by the printed budgets 3.7930e-6, 2.8496e-6 and 4.5717e-4 (column headers). The exact
  ratio is distance / printed budget (Fractions). Each printed budget is checked to be above the exact ceiling, so
  these are also lower bounds against the exact ceilings.
- O3 and C4 divide by the budget column. The exact ratio is distance / b_fam (Arb); for TB-rebal b_fam is above its
  printed 3.5125e-7.
The script reports, and does not fail on, printed ratios that are not floors or not lower bounds. It fails if a floor
is <= 1 (the verdict 'ratio > 1') or an input check fails.
Output: logs/ratio_tables_floor.log, data/ratio_tables_floor_results.json.
"""
import hashlib
import json
import math
import re
import sys
import time
from decimal import Decimal
from fractions import Fraction as Q
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: ratio_tables_floor.py (no arguments)")
t0 = time.time()
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]
LANE = HERE.parent
R6 = LANE.parent
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
A = lambda x: arb(Q(x).numerator) / Q(x).denominator
N, FAILS, OUT = [0], [], {"inputs": {}}


def check(name, ok):
    N[0] += 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def unit(s_):
    return Q(10) ** Decimal(s_).as_tuple().exponent


def fmt(v, printed):
    """The multiple v of the printed unit, written as the printed value is (exact Decimal)."""
    dv = Decimal(v.numerator) / Decimal(v.denominator)
    if "e" in printed:
        m_, e_ = printed.split("e")
        return "%se%s" % ((dv.scaleb(-int(e_))).quantize(Decimal(m_)), e_)
    return str(dv.quantize(Decimal(printed)))


def floor_fr(r, u):
    return Q(math.floor(r / u)) * u


def floor_arb(x, u):
    m = math.floor(float(x.mid()) / u) + 2
    while not A(m * u) <= x:
        m -= 1
    return m * u


SUMM = LANE / "notes/T2_FINAL_SUMMARY.md"
HO = LANE / "handoff/T2_to_T1_v01.md"
T4ALT = LANE / "reviews/REVIEW_T4ALT.md"
FCE = HERE / "data/family_ceilings_exact_results.json"
check("sha256 of reviews/REVIEW_T4ALT.md", sha(T4ALT) == "1332bd422eb515f69ccde37a70c8f4606b06096c7e26852a147717f734aa8c24")
for p_ in (SUMM, HO, T4ALT, FCE):
    OUT["inputs"][str(p_.relative_to(R6))] = sha(p_)
FJ = json.loads(FCE.read_text())
check("family_ceilings_exact results: exit state clean", FJ["fails"] == [] and FJ["checks"] == 37)
EX = {k: arb(v["b_fam"]) for k, v in FJ["ceilings"].items()}
check("the exact graded ceiling of the results equals 50/(651 sqrt 28248)",
      EX["graded"].overlaps(A(Q(50, 651)) / arb(28248).sqrt()))

# ---------------------------------------------------------------- summary section 5
summ = SUMM.read_text()
sec5 = summ.split("\n## 5. Candidate comparison (fixed c, L2)\n")[1].split("\n## 6. ")[0]
HDR = "| candidate | fixed-c L2 distance > | source | / best scalar budget 3.7930e-6 | / sharpw 2.8496e-6 | / graded 4.5717e-4 |"
check("summary section 5 header verbatim", HDR in sec5)
BUD = [("3.7930e-6", "TB-sharp"), ("2.8496e-6", "sharpw"), ("4.5717e-4", "graded")]
for bp, k in BUD:
    check("summary budget %s is above the exact %s ceiling (Arb)" % (bp, k), EX[k] < A(Q(Decimal(bp))))
rows = [ln for ln in sec5.splitlines() if ln.startswith("| ") and not ln.startswith(("| candidate", "|---"))]
check("summary section 5 has 5 rows (007, 005, 008, d2, Mpen2)",
      [ln.split("|")[1].strip().split()[0] for ln in rows] == ["007", "005", "008", "d2", "Mpen2"])
OUT["summary_section5"] = {}
print("summary section 5 (exact Fractions, distance / printed budget):")
for ln in rows:
    c_ = [x.strip() for x in ln.strip("|").split("|")]
    d = Q(Decimal(c_[1].split()[0]))
    for f_, (bp, k) in zip(c_[3:6], BUD):
        u = unit(f_)
        r = d / Q(Decimal(bp))
        fl = floor_fr(r, u)
        e = {"distance": c_[1].split()[0], "budget": bp, "printed": f_, "floor": fmt(fl, f_),
             "printed_is_floor": Q(Decimal(f_)) == fl, "printed_is_lower_bound": Q(Decimal(f_)) <= r}
        OUT["summary_section5"]["%s / %s" % (c_[0].split()[0], k)] = e
        check("summary %s / %s: floor %s > 1" % (c_[0].split()[0], bp, e["floor"]), fl > 1)
        print("    %s / %s: printed %s, floor %s%s" % (c_[0].split()[0], bp, f_, e["floor"],
                                                    "" if e["printed_is_lower_bound"] else "  NOT A LOWER BOUND"))

# ---------------------------------------------------------------- handoff O3 and REVIEW_T4ALT C4
O3 = ["| baseline-gap balls (A2, T4ALT) | 6.8626e-8 | 4.36e4 | 4.31e6 | 8.02e6 |",
      "| FW-T-TB-rebal-v1 | 3.5125e-7 | 8.52e3 | 8.41e5 | 1.57e6 |",
      "| FW-T-TB-sharp-v1 | 3.7930e-6 | 789 | 7.79e4 | 1.45e5 |",
      "| FW-T-T4L2-sharp-v1 | 3.0927e-6 | 967 | 9.56e4 | 1.78e5 |",
      "| FW-T-T4L2-sharpw-v1 | 2.8496e-6 | 1050 | 1.04e5 | 1.93e5 |",
      "| graded and gradedL2 boxes (Proposition G) | 4.5698e-4 | 6.55 | 647 | 1204 |"]
C4 = ["| baseline-gap balls | 6.8626e-8 | 4.31e6 | 8.02e6 |",
      "| FW-T-TB-rebal-v1 | 3.5125e-7 | 8.41e5 | 1.57e6 |",
      "| FW-T-TB-sharp-v1 | 3.7930e-6 | 7.79e4 | 1.45e5 |",
      "| FW-T-T4L2-sharp-v1 | 3.0927e-6 | 9.56e4 | 1.78e5 |",
      "| FW-T-T4L2-sharpw-v1 | 2.8496e-6 | 1.04e5 | 1.93e5 |",
      "| graded and gradedL2 boxes (REVIEW_R1_004_GRADED.md, Proposition G) | 4.5698e-4 | 647 | 1204 |"]
ho = HO.read_text()
t4 = T4ALT.read_text()
check("handoff O3 header and the six rows verbatim",
      "| family | L2 budget | d2 T4-048 (0.0029920) | d2 T4-064 | Mpen2 T4-064 |" in ho and all(r_ in ho for r_ in O3)
      and "d2 >\n    0.29552675, Mpen2 > 0.55006675" in ho)
check("REVIEW_T4ALT C4 header and the six rows verbatim",
      "| framework | L2 budget | d2 (0.29552675) | Mpen2 (0.55006675) |" in t4 and all(r_ in t4 for r_ in C4))
KEY = ["FW-A2-Db", "TB-rebal", "TB-sharp", "sharp", "sharpw", "graded"]
for tab, rows_, dists in (("handoff O3", O3, ["0.0029920", "0.29552675", "0.55006675"]),
                          ("REVIEW_T4ALT C4", C4, ["0.29552675", "0.55006675"])):
    OUT[tab] = {}
    nb = 0
    print("%s (Arb, distance / exact b_fam):" % tab)
    for r_, k in zip(rows_, KEY):
        c_ = [x.strip() for x in r_.strip("|").split("|")]
        check("%s %s: the printed budget %s agrees with the exact ceiling to its printed digit" % (tab, k, c_[1]),
              abs(EX[k] - A(Q(Decimal(c_[1])))) < A(unit(c_[1])))
        for d_, f_ in zip(dists, c_[2:]):
            u = unit(f_)
            x = A(Q(Decimal(d_))) / EX[k]
            fl = floor_arb(x, u)
            lb = bool(A(Q(Decimal(f_))) <= x)
            nb += not lb
            OUT[tab]["%s / %s" % (d_, k)] = {"printed": f_, "floor": fmt(fl, f_), "printed_is_floor": Q(Decimal(f_)) == fl,
                                              "printed_is_lower_bound": lb}
            check("%s %s, distance %s: floor %s > 1" % (tab, k, d_, fmt(fl, f_)), fl > 1)
            print("    %s, %s: printed %s, floor %s%s" % (k, d_, f_, fmt(fl, f_), "" if lb else "  NOT A LOWER BOUND"))
    OUT[tab + " not lower bounds"] = nb
nb5 = [k for k, v in OUT["summary_section5"].items() if not v["printed_is_lower_bound"]]
OUT["summary_section5 not lower bounds"] = nb5
print("summary section 5 entries that are not lower bounds: %s" % (", ".join(nb5) or "none"))
print("handoff O3: %d of 18 not lower bounds; REVIEW_T4ALT C4: %d of 12" % (
    OUT["handoff O3 not lower bounds"], OUT["REVIEW_T4ALT C4 not lower bounds"]))
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N[0], FAILS, round(time.time() - t0, 3)
(HERE / "data/ratio_tables_floor_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
