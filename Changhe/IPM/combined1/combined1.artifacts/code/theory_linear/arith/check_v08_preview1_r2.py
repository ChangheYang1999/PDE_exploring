"""Recheck of the regenerated theory_v08 preview1 (c1-t1 drafts/theory_v08_preview1.md, generated 13:29:19Z) against
the findings of reviews/CHECK_T1_v08_FACTORS.md (which reviewed the 13:09Z generation). Review: same file, revision 1.

Run from artifacts/:  python3 -B -u arith/check_v08_preview1_r2.py
Takes no arguments. Needs only the standard library. Reads (read only, hash-bound): the lane copies
../scratch/v08check/theory_v08_preview1_r2.md (13:29Z) and ../scratch/v08check/T1_TEAM_NOTE_v47.md, and
data/check_v08_factors_results.json of arith/check_v08_factors.py (run that first).
Parts:
  (A) inputs; the 24 table rows of the revision.
  (B) exact: each printed factor against 10^(-k) floor(10^k p/t); the rows against team note v47 (p, t, factor).
  (C) the wording that CHECK_T1_v08_FACTORS asked for: present or absent, asserted verbatim.
Output: logs/check_v08_preview1_r2.log, data/check_v08_preview1_r2_results.json.
"""
import hashlib
import json
import math
import re
import sys
import time
from decimal import Decimal
from fractions import Fraction as Fr
from pathlib import Path

if len(sys.argv) != 1:
    sys.exit("usage: check_v08_preview1_r2.py (no arguments)")
t_start = time.time()
HERE = Path(__file__).resolve().parents[1]
LANE = HERE.parent
R6 = LANE.parent
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
OUT = {"inputs": {}}
NCHK = [0]
FAILS = []


def check(name, ok):
    NCHK[0] += 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def num(s_):
    s_ = s_.strip()
    return Fr(s_) if "/" in s_ else Fr(Decimal(s_))


def floor_k(v, k):
    m = math.floor(v * 10**k)
    return ("%d.%0" + str(k) + "d") % divmod(m, 10**k) if k else str(m)


def rows_of(text, strip_source):
    out = []
    prev_p = None
    for line in text.splitlines():
        m_ = re.match(r"^\s*\| ([DSOUPRAK]\d) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$", line)
        if not m_:
            continue
        rid, lab_, ps, ts, fs = m_.groups()
        if strip_source:
            ps, ts = ps.split(" (")[0], ts.split(" (")[0]
        if ps == "same":
            ps = prev_p
        else:
            toks = ps.split()
            ps = toks[1] if toks[0] in ("Etest", "lam1") else toks[0]
        prev_p = ps
        out.append(dict(id=rid, label=lab_, p=ps, t=ts.split()[0] if ts.split() else ts, factor=fs))
    return out


# ---------------------------------------------------------------- (A)
PREV2 = LANE / "scratch/v08check/theory_v08_preview1_r2.md"
NOTE = LANE / "scratch/v08check/T1_TEAM_NOTE_v47.md"
RES = HERE / "data/check_v08_factors_results.json"
check("(A) sha256 of the lane copy of preview1 (13:29Z)",
      sha(PREV2) == "d8c8e8ba4d36e281381c0f7c55447c9636fc39977e6350a00d805c765725cf06")
check("(A) sha256 of the lane copy of team note v47",
      sha(NOTE) == "1633cd35948398bc69d8b20f1f44ccb5e98fbd7e8ab94ae5f542c9fc6c978cac")
for p_ in (PREV2, NOTE, RES):
    OUT["inputs"][str(p_.relative_to(R6))] = sha(p_)
J = json.loads(RES.read_text())
check("(A) check_v08_factors results: 31 checks, none failed", J["checks"] == 31 and J["fails"] == [])
prev = PREV2.read_text()
flat = " ".join(prev.split())
R2 = rows_of(prev, True)
R1 = rows_of(NOTE.read_text(), False)
check("(A) 24 rows in the revision, ids as in note v47", [r_["id"] for r_ in R2] == [r_["id"] for r_ in R1]
      and len(R2) == 24)

# ---------------------------------------------------------------- (B)
OUT["B"] = {}
for r_ in R2:
    k_ = len(r_["factor"].split(".")[1]) if "." in r_["factor"] else 0
    r_["floor"] = floor_k(num(r_["p"]) / num(r_["t"]), k_)
    OUT["B"][r_["id"]] = {"p": r_["p"], "t": r_["t"], "printed": r_["factor"], "floor": r_["floor"]}
    print("    %s  p = %s  t = %s  printed %s  floor %s" % (r_["id"], r_["p"], r_["t"], r_["factor"], r_["floor"]))
check("(B) every printed factor of the revision equals 10^(-k) floor(10^k p/t)", all(r_["floor"] == r_["factor"]
                                                                                    for r_ in R2))
changed = [a["id"] for a, b in zip(R2, R1) if (num(a["p"]), num(a["t"]), a["factor"]) != (num(b["p"]), num(b["t"]),
                                                                                         b["factor"])]
OUT["B_rows_changed_since_v47"] = changed
print("    rows whose p, t or factor differ from note v47: %s" % (", ".join(changed) or "none"))
check("(B) only S2 changed since note v47", changed == ["S2"])
s2 = {r_["id"]: r_ for r_ in R2}["S2"]
check("(B) S2 is now 516.9717852723 / 7.6219e-5 >= 6782715.40 (T4-437)",
      (s2["p"], s2["factor"]) == ("516.9717852723", "6782715.40") and s2["factor"] == J["B_S2_repair"]["floor_2"])
# the interval rows of check_v08_factors part (C) are unchanged, so its lower-end factors apply to the revision
same_C = [rid for rid in J["C"] if rid != "R1" and {r_["id"]: r_ for r_ in R2}[rid]["factor"] == J["C"][rid]["printed"]]
check("(B) the nine family-ceiling rows of check_v08_factors part (C) are printed unchanged", len(same_C) == 9)
OUT["C_rows_still_printed_at_the_rational_target"] = [rid for rid in same_C
                                                      if not J["C"][rid]["printed_holds_on_interval"]]

# ---------------------------------------------------------------- (C)
PRESENT = {
    "R rows name H >= Phi": "Threshold: the room Ecrit_prof - 93/250 with H >= Phi, at most 0.1555681",
    "P2 row on the whole span": "| P2 | any E with N <= E G on the span < Ecrit_prof, graded |",
    "section 0 item 3 scoped": "fails at the four targets (fixed sharpw ball, sharpw, TB and graded ceilings) with every "
                               "universal velocity constant (NC-T-UNIV-E, which section 2 (g) restricts to registered "
                               "radii at or above 1.421e-7)",
    "section 5 (b) scoped": "At the FW-A2-Db radii no such obstruction is proved (section 2 (g)).",
    "section 2 (g) OPEN, not false": "At 2^-25 and 6.8626e-8 the obstruction for an improved universal constant is "
                                     "OPEN, not false",
    "section 2 (g) NC-T-DIST": "007 is excluded from these balls by NC-T-DIST, since 0.004769166867 > 6.8626e-8",
    "graded boxes below 25/54684": "a graded box of the T4-277 type has L^2 radius below 25/54684",
    "section 6 item 4 unchanged": "No request for a sharper universal velocity constant (rows U1 to U4: none can be "
                                  "below 0.79303650642)",
}
ABSENT = {"exact graded ceiling 50/(651 sqrt 28248)": "50/(651", "'rational target' (the radius at which t is taken)": "rational target",
          "old line 122 (unscoped)": "the T4-351 closure inequality fails with every universal velocity constant",
          "old line 416": "above every Ecrit"}
OUT["C"] = {}
for k_, q_ in PRESENT.items():
    OUT["C"][k_] = q_ in flat
    check("(C) present: %s" % k_, q_ in flat)
for k_, q_ in ABSENT.items():
    OUT["C"]["absent: " + k_] = q_ not in flat
    check("(C) absent: %s" % k_, q_ not in flat)
i569 = [i + 1 for i, l_ in enumerate(prev.splitlines()) if "4. No request for a sharper universal velocity" in l_]
OUT["C"]["line of section 6 item 4"] = i569
print("    section 6 item 4 is at line %s; it gives no reason for the FW-A2-Db radii" % i569)
OUT["checks"] = NCHK[0]
OUT["fails"] = FAILS
OUT["elapsed_s"] = round(time.time() - t_start, 3)
(HERE / "data/check_v08_preview1_r2_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (NCHK[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
