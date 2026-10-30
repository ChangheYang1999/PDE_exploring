"""Check of the 'Targets' bullet of section 1.1 of c1-t1 drafts/theory_v08_preview2.md (generated 13:55:03Z), asked in
c1-t1 T1_TEAM_NOTE_v48 item 1 ('c1-t2: please check this bullet by 15:30Z'), with the next bullet (H >= H0) and the
24 rows of the factor table. Review: reviews/CHECK_T1_v08_FACTORS.md, section 'Revision 2'.

Run from artifacts/:  python3 -B -u arith/check_v08_preview2.py
Takes no arguments. Needs python-flint (arb). Reads (read only, hash-bound): the lane copies
../scratch/v08check2/theory_v08_preview2.md and ../scratch/v08check2/T1_TEAM_NOTE_v48.md, the lane copy
../scratch/v08check/theory_v08_preview1_r2.md (for the rows changed since), the lane copies of c1-t1
T1_TEAM_NOTE_v49 and c1-t4 TEAM_NOTE_v228 (T4-454, for the status labels), and the results of
arith/check_v08_factors.py, arith/family_ceilings_exact.py and arith/falsify_section0.py (run those first).
Parts:
  (A) inputs; the two bullets asserted verbatim; the 24 rows.
  (B) exact: each printed factor against 10^(-k) floor(10^k p/t); k = 4, or 2 for ratios of 100 or more (the rule
      stated in section 1.1); the rows changed since preview1 as regenerated at 13:29Z.
  (C) every number and inequality of the two bullets against the lane results: targets, brackets (Arb), the
      lower-end factors, 'U2, U3, P4 and P5 hold there as printed', 'their t is an upper bound of the radius' (rows D).
Output: logs/check_v08_preview2.log, data/check_v08_preview2_results.json.
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
    sys.exit("usage: check_v08_preview2.py (no arguments)")
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


def num(s_):
    s_ = s_.strip()
    return Q(s_) if "/" in s_ else Q(Decimal(s_))


def floor_k(v, k):
    m = math.floor(v * 10**k)
    return ("%d.%0" + str(k) + "d") % divmod(m, 10**k) if k else str(m)


def rows_of(text):
    out, prev_p = [], None
    for line in text.splitlines():
        m_ = re.match(r"^\s*\| ([DSOUPRAK]\d) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$", line)
        if not m_:
            continue
        rid, lab_, ps, ts, fs = m_.groups()
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
PV2 = LANE / "scratch/v08check2/theory_v08_preview2.md"
V48 = LANE / "scratch/v08check2/T1_TEAM_NOTE_v48.md"
PV1 = LANE / "scratch/v08check/theory_v08_preview1_r2.md"
RCF = HERE / "data/check_v08_factors_results.json"
RFC = HERE / "data/family_ceilings_exact_results.json"
RFS = HERE / "data/falsify_section0_results.json"
V49 = LANE / "scratch/v08check2/T1_TEAM_NOTE_v49.md"
T228 = LANE / "scratch/v08check2/TEAM_NOTE_v228_c1t4.md"
PIN = {PV2: "5940b948c623aab0e744375d26100c99356f6bdc6acb46d915822e8b86d70158",
       V48: "bb9cc9a022a10d04fa023eacdc339f54231fe57b016c4a3d945b5e60e77f800f",
       PV1: "d8c8e8ba4d36e281381c0f7c55447c9636fc39977e6350a00d805c765725cf06",
       V49: "2c8aa6391e215e17a8bde35a506d1e3bc11d30af4896c5c659024758a29dc3b5",
       T228: "cbcaaee6cde345eb2cc2d1569e1529e6b4d008aea08792f83bad4ab587dbabda"}
for p_, h_ in PIN.items():
    check("(A) sha256 of %s" % p_.relative_to(LANE), sha(p_) == h_)
for p_ in (PV2, V48, PV1, V49, T228, RCF, RFC, RFS):
    OUT["inputs"][str(p_.relative_to(R6))] = sha(p_)
CF, FC = json.loads(RCF.read_text()), json.loads(RFC.read_text())
check("(A) check_v08_factors and family_ceilings_exact results are clean",
      CF["fails"] == [] and CF["checks"] == 31 and FC["fails"] == [] and FC["checks"] == 37)
RADK = json.loads(RFS.read_text())["B"]["radii"]
v48 = V48.read_text()
check("(A) note v48 asks: 'c1-t2: please check this bullet by 15:30Z.'", "c1-t2: please check this bullet by 15:30Z." in v48)
pv2 = PV2.read_text()
flat = " ".join(pv2.split())
TGT = ("- Targets. The fixed sharpw ball is the exact radius 1351/1024000000. At the ceilings, t is evaluated at the "
       "printed rational targets 28496/10^10 (sharpw), 3793/10^9 (TB) and 25/54684 (graded), which are the exact targets "
       "of T4-425 and T4-414. The registered ceilings are at or below these targets, and a smaller radius has a larger "
       "threshold. At the exact graded ceiling 50/(651 sqrt 28248) < 25/54684 (theory_v04) rows U4, P1 and P2 are at "
       "least 2.9432, 2.0544 and 2.0515 (c1-t2 CHECK_T1_v08_FACTORS revision 1, handoff BB2; CLAIMED). For the sharpw "
       "and TB family ceilings, c1-t2 handoff BE1 (13:53Z; Arb at 256 bits; CLAIMED, c1-t2's own) evaluates the "
       "theory_v03 formula and finds 28495/10^10 < sharpw ceiling < 28496/10^10 and 37929/10^10 < TB-sharp ceiling < "
       "37930/10^10, so each printed ceiling is the exact one rounded up at the printed digit. With this bracket R2 and "
       "R3 are at least 46.0752 and 66.5677 at the exact ceilings, and U2, U3, P4 and P5 hold there as printed (c1-t2 "
       "BB2 and BE2). K2 and K3 are not evaluated below the printed targets. Rows D are not affected, since their t is "
       "an upper bound of the radius. Every row still fails.")
HH0 = ("- Rows R1 to R3 use the room with H >= Phi(theta*) (T4-380), as T4-414 does. With only H >= H0 they are at "
       "least 22.1948, 46.0750 and 66.5674 (c1-t2 BA4; CLAIMED).")
check("(A) the Targets bullet verbatim", TGT in flat)
check("(A) the H >= H0 bullet verbatim", HH0 in flat)
OUT["Targets_line"] = [i + 1 for i, l_ in enumerate(pv2.splitlines()) if l_.startswith("- Targets.")]
ROWS = rows_of(pv2)
check("(A) 24 rows, ids D1-D5 S1 S2 O1 U1-U4 P1-P5 R1-R3 A1 K1-K3",
      [r_["id"] for r_ in ROWS] == "D1 D2 D3 D4 D5 S1 S2 O1 U1 U2 U3 U4 P1 P2 P3 P4 P5 R1 R2 R3 A1 K1 K2 K3".split())
row = {r_["id"]: r_ for r_ in ROWS}

# ---------------------------------------------------------------- (B)
OUT["B"] = {}
for r_ in ROWS:
    k_ = len(r_["factor"].split(".")[1]) if "." in r_["factor"] else 0
    v_ = num(r_["p"]) / num(r_["t"])
    r_["floor"] = floor_k(v_, k_)
    OUT["B"][r_["id"]] = {"p": r_["p"], "t": r_["t"], "printed": r_["factor"], "floor": r_["floor"], "k": k_,
                          "k_rule": k_ == (2 if v_ >= 100 else 4)}
    print("    %s  p = %s  t = %s  printed %s  floor %s  k %d" % (r_["id"], r_["p"], r_["t"], r_["factor"], r_["floor"], k_))
check("(B) every printed factor equals 10^(-k) floor(10^k p/t)", all(r_["floor"] == r_["factor"] for r_ in ROWS))
badk = [rid for rid, v in OUT["B"].items() if not v["k_rule"]]
OUT["B_k_rule_exceptions"] = badk
print("    rows not following 'k = 4 (k = 2 for ratios of 100 or more)': %s" % (", ".join(badk) or "none"))
check("(B) every row follows the stated k rule", badk == [])
P1R = {r_["id"]: r_ for r_ in rows_of(PV1.read_text())}
chg = [r_["id"] for r_ in ROWS if (num(r_["p"]), num(r_["t"]), r_["factor"]) !=
       (num(P1R[r_["id"]]["p"]), num(P1R[r_["id"]]["t"]), P1R[r_["id"]]["factor"])]
OUT["B_rows_changed_since_preview1_r2"] = chg
print("    rows whose p, t or factor differ from preview1 (13:29Z): %s" % (", ".join(chg) or "none"))
check("(B) no row changed since preview1 (13:29Z)", chg == [])

# ---------------------------------------------------------------- (C)
K_FIX, K_SW, K_TB, K_GR = ("FW-T-T4L2-sharpw-v1 fixed ball (1351/1024000000)",
                           "FW-T-T4L2-sharpw-v1 family ceiling (2.8496e-6)",
                           "FW-T-TB-sharp-v1 family ceiling (3.7930e-6)", "graded boxes, ceiling (25/54684)")
bl = lambda k: Q(RADK[k]["beta_lower"])
bu = lambda k: Q(RADK[k]["beta_upper"])
check("(C) fixed sharpw radius 1351/1024000000 (falsify_section0 radii)", bl(K_FIX) == bu(K_FIX) == Q(1351, 1024000000))
check("(C) targets 28496/10^10, 3793/10^9, 25/54684 are the upper ends of the registered intervals",
      (bu(K_SW), bu(K_TB), bu(K_GR)) == (Q(28496, 10**10), Q(3793, 10**9), Q(25, 54684)))
EX = {k: arb(v["b_fam"]) for k, v in FC["ceilings"].items()}
check("(C) 'at or below these targets': exact sharpw, TB-sharp, graded ceilings are strictly below (Arb)",
      EX["sharpw"] < A(Q(28496, 10**10)) and EX["TB-sharp"] < A(Q(3793, 10**9)) and EX["graded"] < A(Q(25, 54684)))
check("(C) exact graded ceiling 50/(651 sqrt 28248) (Arb overlap with the results)",
      EX["graded"].overlaps(A(Q(50, 651)) / arb(28248).sqrt()))
check("(C) 28495/10^10 < sharpw < 28496/10^10 and 37929/10^10 < TB-sharp < 37930/10^10 (Arb, strict)",
      A(Q(28495, 10**10)) < EX["sharpw"] < A(Q(28496, 10**10))
      and A(Q(37929, 10**10)) < EX["TB-sharp"] < A(Q(37930, 10**10)))
check("(C) these are the brackets of family_ceilings_exact (in_bracket true for sharpw and TB-sharp)",
      FC["ceilings"]["sharpw"]["in_bracket"] and FC["ceilings"]["TB-sharp"]["in_bracket"]
      and FC["ceilings"]["sharpw"]["bracket"] == ["5699/2000000000", "1781/625000000"]
      and FC["ceilings"]["TB-sharp"]["bracket"] == ["37929/10000000000", "3793/1000000000"])
C = CF["C"]
check("(C) U4, P1, P2 at the exact graded ceiling: >= 2.9432, 2.0544, 2.0515 (check_v08_factors part (C))",
      (C["U4"]["factor_lo"], C["P1"]["factor_lo"], C["P2"]["factor_lo"]) == ("2.9432", "2.0544", "2.0515"))
check("(C) these were computed from 45697/10^8, below the exact graded ceiling (so valid there)",
      bl(K_GR) == Q(45697, 10**8) and A(bl(K_GR)) < EX["graded"])
check("(C) R2, R3 at the exact sharpw and TB ceilings: >= 46.0752, 66.5677",
      (C["R2"]["factor_lo"], C["R3"]["factor_lo"]) == ("46.0752", "66.5677"))
check("(C) U2, U3, P4, P5 hold as printed over the registered interval, and are printed unchanged in preview2",
      all(C[r]["printed_holds_on_interval"] and C[r]["printed"] == row[r]["factor"] for r in ("U2", "U3", "P4", "P5")))
check("(C) U4, P1, P2, R2, R3 of preview2 are the values printed at the rational targets",
      all(C[r]["printed"] == row[r]["factor"] for r in ("U4", "P1", "P2", "R2", "R3")))
check("(C) H >= H0: R1, R2, R3 >= 22.1948, 46.0750, 66.5674",
      (C["R1"]["factor_lo_H0"], C["R2"]["factor_lo_H0"], C["R3"]["factor_lo_H0"]) == ("22.1948", "46.0750", "66.5674"))
DT = {"D1": "TB-sharp", "D2": "sharpw", "D3": "sharp", "D5": "graded"}
check("(C) rows D: t of D1, D2, D3, D5 is above the exact TB-sharp, sharpw, sharp and graded ceilings (Arb)",
      all(EX[k] < A(num(row[d]["t"])) for d, k in DT.items()))
check("(C) row D4: t is the exact fixed sharpw radius", num(row["D4"]["t"]) == Q(1351, 1024000000))
check("(C) no row of preview2 uses the TB-rebal ceiling 3.5125e-7 (which is below its exact value)",
      all(r_["t"] != "3.5125e-7" for r_ in ROWS) and "3.5125e-7 (" not in " ".join(r_["label"] for r_ in ROWS))
# status labels: T4-454 (c1-t4 TEAM_NOTE_v228) accepts the BE brackets, not the R2/R3 factor formulas
t228 = " ".join(T228.read_text().split())
v49 = " ".join(V49.read_text().split())
Q228 = ["T4-454 independently accepts the exact brackets in handoff BE.",
        "The six other scalar ceilings lie in the one-unit brackets below their printed values, and the graded ceiling "
        "lies between 45697/10^8 and 25/54684.",
        "I have not individually audited the historical O3/C4 table entries or the R2/R3 factor formulas in this result."]
check("(C) c1-t4 TEAM_NOTE_v228 (T4-454): the three quoted sentences verbatim", all(q_ in t228 for q_ in Q228))
Q49 = ["the BE stamp 14:00Z in the Targets bullet of section 1.1",
       "c1-t2: the Targets bullet check asked in v48 (by 15:30Z) is still open."]
check("(C) c1-t1 T1_TEAM_NOTE_v49 item 2: the two quoted phrases verbatim", all(q_ in v49 for q_ in Q49))
OUT["status"] = {"BE brackets (sharpw, TB-sharp, graded)": "AUDITED (T4-454, c1-t4 TEAM_NOTE_v228)",
                 "R2/R3 lower-end factors, U4/P1/P2 lower-end factors, H >= H0 values": "CLAIMED (c1-t2; not in T4-454)"}
# wording notes, recorded (not failures): the BE time stamp and the status label
OUT["notes"] = {
    "BE time cited": "13:53Z" if "handoff BE1 (13:53Z;" in flat else None,
    "line 674 cites BE (13:53Z)": "evaluated in c1-t2 handoff BE (13:53Z;" in flat,
    "status label of BE": "CLAIMED, c1-t2's own",
}
print("    notes: %s" % OUT["notes"])
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N[0], FAILS, round(time.time() - t0, 3)
(HERE / "data/check_v08_preview2_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
