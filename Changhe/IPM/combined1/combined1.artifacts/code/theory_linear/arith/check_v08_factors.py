"""Check of the 24-row factor table of c1-t1 T1_TEAM_NOTE_v47 (theory_v08 consultation, item 3) and of the
universal-constant wording of drafts/theory_v08_preview1.md. Review: reviews/CHECK_T1_v08_FACTORS.md.

Run from artifacts/:  python3 -B -u arith/check_v08_factors.py
Takes no arguments. Needs python-flint (arb). Reads (read only, hash-bound): the lane copies
../scratch/v08check/T1_TEAM_NOTE_v47.md and ../scratch/v08check/theory_v08_preview1.md, c1-t4's T4-437 PROOF.md,
this lane's data/falsify_section0_results.json, reviews/REVIEW_T4_410_CAMPAIGN.md and reviews/REVIEW_T4_415.md.
No other lane's code is imported or executed (c1-t1's v08_factors_007.py is not run).
Parts:
  (A) inputs; the table rows parsed from the note; the quoted preview1 sentences asserted verbatim.
  (B) exact: every printed factor against 10^(-k) floor(10^k p/t), k the printed decimals; the T4-437 S2 repair.
  (C) Arb: the rows at family ceilings (U2-U4, P1, P2, P4, P5, R2, R3), at the lower end of the registered interval
      of the ceiling (the printed ceilings are rounded up, and the graded ceiling is 50/(651 sqrt 28248) < 25/54684),
      with the thresholds of
      data/falsify_section0_results.json for 007 (upper bounds over the interval) and J(R)/H scaled by
      (beta_lo/beta)^(delta/(-q-1)).
  (D) Arb: retained-shape universal-constant factors for 007, and the radii where Etest is below the threshold
      (FW-A2-Db) or only below it with V >= v0 (2^-23), with the NC-T-DIST factors of 007, 013 and 014 there
      (distance floors of 013 and 014 from the lane copy ../scratch/falsify/THEORY_FINAL_d38.md).
Output: logs/check_v08_factors.log, data/check_v08_factors_results.json.
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

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: check_v08_factors.py (no arguments)")
t_start = time.time()
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]
LANE = HERE.parent
R6 = LANE.parent
OUT = {"inputs": {}}
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
A_ = lambda fr_: arb(fr_.numerator) / fr_.denominator
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
    """10^(-k) floor(10^k v) for a Fraction v, as a decimal string with k places."""
    m = math.floor(v * 10**k)
    return ("%d.%0" + str(k) + "d") % divmod(m, 10**k) if k else str(m)


def arb_floor_k(x, k):
    """Largest m/10^k that Arb proves <= x, as a string with k places."""
    m = math.floor(float(x.mid()) * 10**k) + 2
    while not A_(Fr(m, 10**k)) <= x:
        m -= 1
    return ("%d.%0" + str(k) + "d") % divmod(m, 10**k)


# ---------------------------------------------------------------- (A) inputs
NOTE = LANE / "scratch/v08check/T1_TEAM_NOTE_v47.md"
PREV = LANE / "scratch/v08check/theory_v08_preview1.md"
P437 = R6 / "c1-t4/research/theory_v08_factors_audit/PROOF.md"
FALS = HERE / "data/falsify_section0_results.json"
CAMP = LANE / "reviews/REVIEW_T4_410_CAMPAIGN.md"
R415 = LANE / "reviews/REVIEW_T4_415.md"
PIN = {NOTE: "1633cd35948398bc69d8b20f1f44ccb5e98fbd7e8ab94ae5f542c9fc6c978cac",
       PREV: "34d1393cfc35a4507c5c99a4ef791265d803c21a3dd98cb2ee214a2e2e4be784",
       P437: "b7c3e467fdc2a8cf664453730a84c2dd49122063bc5459ef9fcd2b8abc92e48d"}
for p_, h_ in PIN.items():
    check("(A) sha256 of %s" % p_.name, sha(p_) == h_)
for p_ in (NOTE, PREV, P437, FALS, CAMP, R415):
    OUT["inputs"][str(p_.relative_to(R6))] = sha(p_)

note = NOTE.read_text()
ROWS = []
prev_p = None
for line in note.splitlines():
    m_ = re.match(r"^\s*\| ([DSOUPRAK]\d) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$", line)
    if not m_:
        continue
    rid, lab_, ps, ts, fs = m_.groups()
    if ps == "same":
        p_s = prev_p
    else:
        toks = ps.split()
        p_s = toks[1] if toks[0] in ("Etest", "lam1") else toks[0]
    prev_p = p_s
    ROWS.append(dict(id=rid, label=lab_, p=p_s, t=ts, factor=fs))
check("(A) 24 rows parsed", len(ROWS) == 24)
check("(A) row ids D1-D5 S1 S2 O1 U1-U4 P1-P5 R1-R3 A1 K1-K3",
      [r_["id"] for r_ in ROWS] == "D1 D2 D3 D4 D5 S1 S2 O1 U1 U2 U3 U4 P1 P2 P3 P4 P5 R1 R2 R3 A1 K1 K2 K3".split())
prev = PREV.read_text()
flat = " ".join(prev.split())
QUOTES = {"line 122": "For 007, 013 and 014 the T4-351 closure inequality fails with every universal velocity "
                      "constant (NC-T-UNIV-E)",
          "line 416": "Every universal constant is at least Emin = 0.79303650642..., above every Ecrit",
          "line 460": "No request for a sharper universal velocity constant (rows U1 to U4: none can be below "
                      "0.79303650642)",
          "line 218": "Ecrit <= 0.6819391, 0.6471910 and 0.2694314 at the sharpw, TB and graded ceilings"}
for k_, q_ in QUOTES.items():
    check("(A) preview1 %s verbatim" % k_, q_ in flat)

# ---------------------------------------------------------------- (B) exact factors
print("(B) printed factor against 10^(-k) floor(10^k p/t):")
OUT["B"] = {}
for r_ in ROWS:
    p_, t_ = num(r_["p"]), num(r_["t"])
    k_ = len(r_["factor"].split(".")[1]) if "." in r_["factor"] else 0
    fl = floor_k(p_ / t_, k_)
    ok = fl == r_["factor"]
    r_["floor"] = fl
    OUT["B"][r_["id"]] = {"p": r_["p"], "t": r_["t"], "printed": r_["factor"], "floor": fl, "equal": ok}
    print("    %s  p = %s  t = %s  printed %s  floor %s  %s" % (r_["id"], r_["p"], r_["t"], r_["factor"], fl,
                                                              "equal" if ok else "DIFFERENT"))
diff_B = [r_["id"] for r_ in ROWS if r_["floor"] != r_["factor"]]
OUT["B_rows_not_equal_to_floor"] = diff_B
print("    rows whose printed factor differs from the floor: %s" % (", ".join(diff_B) or "none"))
check("(B) every printed factor is <= p/t (a valid lower bound of the ratio of the printed p and t)",
      all(Fr(Decimal(r_["factor"])) <= num(r_["p"]) / num(r_["t"]) for r_ in ROWS))
S2p = Fr(Decimal("516.9717852723"))
s2 = S2p / num("7.6219e-5")
check("(B) S2 repair of T4-437: exact ratio 5169717852723/762190", s2 == Fr(5169717852723, 762190))
check("(B) S2 repair: floor at 2 places is 6782715.40", floor_k(s2, 2) == "6782715.40")
t437 = " ".join(P437.read_text().split())
check("(B) T4-437 PROOF states 516.9717852723 and 6782715.40", "516.9717852723" in t437 and "6782715.40" in t437)
OUT["B_S2_repair"] = {"p": "516.9717852723", "ratio": "5169717852723/762190", "floor_2": floor_k(s2, 2)}

# ---------------------------------------------------------------- (C) family ceilings at the lower end
cF = Fr(4076476460239181, 2**51)
cA = A_(cF)
qA = 1 / cA - 4
dA = 1 - 1 / cA
expo = dA / (-qA - 1)
F = json.loads(FALS.read_text())
RAD = F["B"]["radii"]
K_FIX, K_SW, K_TB, K_GR = ("FW-T-T4L2-sharpw-v1 fixed ball (1351/1024000000)",
                           "FW-T-T4L2-sharpw-v1 family ceiling (2.8496e-6)",
                           "FW-T-TB-sharp-v1 family ceiling (3.7930e-6)", "graded boxes, ceiling (25/54684)")
check("(C) the four target radii are in data/falsify_section0_results.json", all(k_ in RAD for k_ in (K_FIX, K_SW, K_TB, K_GR)))
c07 = lambda key, fld: Fr(Decimal(RAD[key]["per_candidate"]["007"][fld]))
blo = lambda key: Fr(RAD[key]["beta_lower"])
bhi = lambda key: Fr(RAD[key]["beta_upper"])
check("(C) interval ends: sharpw [28495, 28496]/10^10, TB [37929, 37930]/10^10, graded [45697/10^8, 25/54684]",
      (blo(K_SW), bhi(K_SW), blo(K_TB), bhi(K_TB), blo(K_GR), bhi(K_GR)) ==
      (Fr(28495, 10**10), Fr(28496, 10**10), Fr(37929, 10**10), Fr(37930, 10**10), Fr(45697, 10**8), Fr(25, 54684)))
# the campaign and T4-415 rows of 007 that the note quotes (p of R rows, room t of R rows)
camp = CAMP.read_text()
for s_ in ("| sharpw ceiling 28496/10^10 |", "3.974970 / 3.974957 / 3.974975", "4.188388 / 4.188374 / 4.188394",
           "3.452825 / 3.452814 / 3.452830", "0.2694175 / 0.2694314 / 0.2694225", "0.6819038 / 0.6819391 / 0.6819164",
           "0.6471575 / 0.6471910 / 0.6471695"):
    check("(C) REVIEW_T4_410_CAMPAIGN contains '%s'" % s_, s_ in camp)
r415 = R415.read_text()
for s_ in ("0.1555681 / 0.1555954 / 0.1555778", "0.08626771 / 0.08629145 / 0.08627618",
           "0.06291677 / 0.06293930 / 0.06292481", "0.1810598671 / 0.1810691846 / 0.1810632403"):
    check("(C) REVIEW_T4_415 contains '%s'" % s_, s_ in r415)
row = {r_["id"]: r_ for r_ in ROWS}
E372 = Fr(372, 1000)
# (target key, threshold field over the interval, kind) per row; kind: 'thr' = t is a threshold, 'room' = t is
# threshold - 93/250 and p scales with beta
# rows at family ceilings: (target key, threshold field over the interval, kind); kind 'thr': t is a threshold;
# 'room': t is threshold - 93/250 (H >= Phi, V = 0) and p = J(R)/H scales with (beta_lo/beta)^expo
SPEC = {"U2": (K_SW, "crude_H0_V0_upper", "thr"), "U3": (K_TB, "crude_H0_V0_upper", "thr"),
        "U4": (K_GR, "crude_H0_V0_upper", "thr"),
        "P1": (K_GR, "shape_H0_V0_upper", "thr"), "P2": (K_GR, "shape_H0_V0_upper", "thr"),
        "P4": (K_SW, "shape_H0_V0_upper", "thr"), "P5": (K_TB, "shape_H0_V0_upper", "thr"),
        "R2": (K_SW, "shape_Phi_V0_upper", "room"), "R3": (K_TB, "shape_Phi_V0_upper", "room")}
OUT["C"] = {}
print("(C) rows at the lower end of the registered interval (007; thresholds are upper bounds over the interval):")
for rid, (key, fld, kind) in SPEC.items():
    r_ = row[rid]
    k_ = len(r_["factor"].split(".")[1])
    thr = c07(key, fld)
    p_ = A_(num(r_["p"]))
    if kind == "thr":
        t_up = max(num(r_["t"]), thr)
        lo = p_ / A_(t_up)
        res = {"t_used": str(t_up), "t_covers_interval": num(r_["t"]) >= thr}
    else:
        t_up = max(num(r_["t"]), thr - E372)
        p_lo = p_ * (A_(blo(key) / bhi(key)))**expo
        lo = p_lo / A_(t_up)
        res = {"t_used": str(t_up), "t_covers_interval": num(r_["t"]) >= thr - E372, "p_lo": p_lo.str(10)}
        t_h0 = max(num(r_["t"]), c07(key, "shape_H0_V0_upper") - E372)
        res["factor_lo_H0"] = arb_floor_k(p_lo / A_(t_h0), k_)
    res["factor_lo"] = arb_floor_k(lo, k_)
    res["printed"] = r_["factor"]
    res["printed_holds_on_interval"] = Fr(Decimal(r_["factor"])) <= Fr(Decimal(res["factor_lo"]))
    OUT["C"][rid] = res
    print("    %s  %s  t_used %s  factor >= %s  printed %s  %s%s" % (
        rid, key.split(" (")[0], float(t_up), res["factor_lo"], r_["factor"],
        "holds" if res["printed_holds_on_interval"] else "ONLY AT THE PRINTED TARGET",
        ("  (H >= H0 only: >= %s)" % res["factor_lo_H0"]) if "factor_lo_H0" in res else ""))
# R1 at the exact fixed sharpw radius with H >= H0 only: room <= Ecrit(H0) - 93/250, Ecrit(H0) <= t of P3 (T4-422)
r1_h0 = A_(num(row["R1"]["p"])) / A_(num(row["P3"]["t"]) - E372)
OUT["C"]["R1"] = {"printed": row["R1"]["factor"], "room_H0_upper": str(num(row["P3"]["t"]) - E372),
                  "factor_lo_H0": arb_floor_k(r1_h0, 4)}
print("    R1  fixed sharpw (exact radius)  with H >= H0 only: room <= %s, factor >= %s; printed %s needs H >= Phi" % (
    float(num(row["P3"]["t"]) - E372), OUT["C"]["R1"]["factor_lo_H0"], row["R1"]["factor"]))

# ---------------------------------------------------------------- (D) retained shape and FW-A2-Db
Et = A_(Fr(Decimal(row["U1"]["p"])))
check("(D) Etest decimal of the note is a lower bound (0.793036506422514088 <= Emin)",
      Fr(Decimal(row["U1"]["p"])) <= Fr(Decimal("0.7930365064225140883557")))
OUT["D"] = {"shape_factors_007": {}, "not_excluded": {}}
print("(D) universal-constant factors with the retained-shape threshold (3) of T4-414, V = 0, H >= H0, 007:")
for lab_, key in (("fixed sharpw", K_FIX), ("sharpw ceiling", K_SW), ("TB ceiling", K_TB), ("graded", K_GR)):
    f_ = arb_floor_k(Et / A_(c07(key, "shape_H0_V0_upper")), 4)
    OUT["D"]["shape_factors_007"][lab_] = f_
    print("    %s: Etest / %s >= %s" % (lab_, RAD[key]["per_candidate"]["007"]["shape_H0_V0_upper"], f_))
pD = num(row["D1"]["p"])
for key, v in RAD.items():
    if v["class"] == 1:
        continue
    fac = floor_k(pD / Fr(v["beta_upper"]), 0)
    OUT["D"]["not_excluded"][key] = {"class": v["class"], "class_text": v["class_text"],
                                     "shape_Phi_V0_lower_007": v["per_candidate"]["007"]["shape_Phi_V0_lower_at_beta_upper"],
                                     "shape_Phi_Vv0_lower_007": v["per_candidate"]["007"]["shape_Phi_Vv0_lower_at_beta_upper"],
                                     "NC-T-DIST factor 007": fac}
    print("    %s: class %d (%s); 007 threshold >= %s (V = 0), >= %s (V >= v0); NC-T-DIST factor of 007 >= %s" % (
        key, v["class"], v["class_text"], v["per_candidate"]["007"]["shape_Phi_V0_lower_at_beta_upper"],
        v["per_candidate"]["007"]["shape_Phi_Vv0_lower_at_beta_upper"], fac))
# distance floors of 013 and 014 (THEORY_FINAL draft 38 section 8 table, lane copy)
D38 = LANE / "scratch/falsify/THEORY_FINAL_d38.md"
check("(D) sha256 of the draft 38 lane copy", sha(D38) == "ccaa8623477ffdffbb977e866e669cffc9546a657eade246d053941ea0162a02")
OUT["inputs"][str(D38.relative_to(R6))] = sha(D38)
d38 = D38.read_text()
FLO = {"007": pD, "013": Fr(Decimal("0.00199234339")), "014": Fr(Decimal("0.00198301351067"))}
check("(D) draft 38 rows '| 013 | 0.00199234339 (T4-255' and '| 014 | 0.00198301351067 (N4-214'",
      "| 013 | 0.00199234339 (T4-255" in d38 and "| 014 | 0.00198301351067 (N4-214" in d38)
OUT["D"]["NC-T-DIST factors at class 2 and 3 radii"] = {}
for key, v in RAD.items():
    if v["class"] != 1:
        fs_ = {n: floor_k(FLO[n] / Fr(v["beta_upper"]), 0) for n in FLO}
        OUT["D"]["NC-T-DIST factors at class 2 and 3 radii"][key] = fs_
        print("    NC-T-DIST at %s: distance floor / radius >= %s (007 / 013 / 014)" % (key, " / ".join(fs_.values())))
check("(D) FW-A2-Db radii are class 3 and 2^-23 is class 2",
      [v["class"] for k_, v in RAD.items() if v["class"] != 1] == [3, 3, 2])
check("(D) at the class 3 radii the 007 threshold lower bound exceeds Etest even with V >= v0",
      all(Fr(Decimal(v["per_candidate"]["007"]["shape_Phi_Vv0_lower_at_beta_upper"])) > Fr(Decimal(row["U1"]["p"]))
          for v in RAD.values() if v["class"] == 3))

OUT["checks"] = NCHK[0]
OUT["fails"] = FAILS
OUT["elapsed_s"] = round(time.time() - t_start, 3)
(HERE / "data/check_v08_factors_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (NCHK[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
