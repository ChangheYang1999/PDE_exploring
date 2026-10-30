"""Checks for handoff section BS: wording findings on c1-t1 THEORY_FINAL draft 55 and two c1-t2 errata.

Inputs (read only, sha256 asserted):
  - data/inputs/theory_final_d55_aa2d3063_excerpt.txt: lines 323-329, 406-409, 422-427, 495, 582-586, 683-692,
    1595-1599, 1844-1849 and 2146-2148 of c1-t1/THEORY_FINAL.md draft 55 (sha256
    aa2d306329e3a653d089824eebf9ee741c3383af60c17e0bf61f7deee4325169), saved 2026-10-29T17:13:39Z (a first excerpt
    without lines 2146-2148 was saved at 17:09:04Z), each line prefixed by its number and a tab;
  - data/inputs/c1t4_verify_report_excerpt_1708.txt: lines 1852-1858 (T4-175), 2774-2780 (T4-290), 3087-3093
    (T4-328) and 4493-4503 (T4-485) of c1-t4/VERIFY_REPORT.md (sha256 ed7cb404...2df6b1b9 at 17:09:04Z), same format;
  - data/inputs/theory_v01_47ba2ee7_excerpt.txt: lines 64-66 and 83-85 of c1-t1/drafts/theory_v01.md (sha256
    47ba2ee70a6bfc7f939ca6fd661462d9b2a6988f47e7e545a6e433fd6e5eacb5), saved 2026-10-29T17:10:49Z, same format: the
    (h, k) sector labels;
  - notes/T2_T4L2_sharp.md (sha256 cb72c73e...03635a2f), for its sector list and the K_H displays;
  - handoff/T2_to_T1_v01.md, text only (not pinned: it only grows), for the two T4ALT boxes of section M2.
Checked:
  - (a) draft 55 lines 584 and 1597 label c1-t2 AJ2 CLAIMED; T4-290 CONFIRMS it under stated hypotheses;
  - (b) lines 325-328 and 1846-1848 attribute the 1.0612 (beta 11/4) bound to the T2-R3 L^2 budget, while lines
    685-687 give it for the T2-R1 TB-sharp matrix with E0 as one component;
  - (c) line 425 states the closure inequality without beta > 0 and the slope margin 7/10 - c_s r > 0;
  - (d) line 495 gives epsilon_max 1.8938e-7 without its box (m, B, s);
  - erratum (i): line 684 and section 11 item 80 (line 2147) have "fixed state 131 floors" (from c1-t2
    CHECK_THEORY_V08_T2 D2);
  - erratum (ii), exact: 10000/1037 and 10000/1557 exceed the printed 9.6432 and 6.4226 (rounded-down displays), while
    the exact K_H = 1/beta(r) is below both, so draft 55 line 408 is true (decimals in the log are FLOAT displays);
  - T4-175's floor 6091157959/250000000000 for 005 against c1-t2's 0.024364634 and T4-082's 0.01625064;
  - T4-328's list (2,0), (3,0), (4,0) in the labels e = 1 - l delta - 2q equals the theory_v01 (h, k) list (1,0),
    (2,0), (3,0) (e(h, k) = gamma - h delta - 2k, gamma = 1 - delta) used by the notes, under l = h + 1.
No peer code is executed.

Run from artifacts/:  python3 -B -u arith/bs_draft55_errata_check.py
Takes no arguments. Output: stdout (logs/bs_draft55_errata_check.log by the README command),
data/bs_draft55_errata_check_results.json.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as Q
from pathlib import Path

if len(sys.argv) != 1:
    sys.exit("usage: bs_draft55_errata_check.py (no arguments)")
T0 = time.time()
HERE = Path(__file__).resolve().parents[1]
PINS = {HERE / "data/inputs/theory_final_d55_aa2d3063_excerpt.txt":
        "7798f87c0f53c30dad6fce2740c7e78100409bc4b985768731424ff613c924bf",
        HERE / "data/inputs/c1t4_verify_report_excerpt_1708.txt":
        "6c434e7491b96e0d1544427421741b727941485b59de0dc17b1ec4c7b9d927eb",
        HERE / "data/inputs/theory_v01_47ba2ee7_excerpt.txt":
        "029273020f54dbe55972d999e4c4c30ce4febf44ae443454ae7d8799566be30b",
        HERE.parent / "notes/T2_T4L2_sharp.md": "cb72c73e2b94c95302838ba5826a1a2cece680083f3e6bc37531a6ec03635a2f"}
FAILS, N_ = [], [0]


def check(msg, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


for p, h in PINS.items():
    check("sha256 of %s is %s...%s" % (p.relative_to(HERE.parent), h[:8], h[-8:]),
          hashlib.sha256(p.read_bytes()).hexdigest() == h)


def numbered(p):
    out = {}
    for ln in p.read_text().splitlines():
        k, v = ln.split("\t", 1)
        out[int(k)] = v
    return out


TF = numbered(HERE / "data/inputs/theory_final_d55_aa2d3063_excerpt.txt")
VR = numbered(HERE / "data/inputs/c1t4_verify_report_excerpt_1708.txt")
rng = lambda a, b: list(range(a, b + 1))
check("draft 55 excerpt has the 47 lines 323-329, 406-409, 422-427, 495, 582-586, 683-692, 1595-1599, 1844-1849, "
      "2146-2148",
      sorted(TF) == rng(323, 329) + rng(406, 409) + rng(422, 427) + [495] + rng(582, 586) + rng(683, 692)
      + rng(1595, 1599) + rng(1844, 1849) + rng(2146, 2148))
check("VERIFY_REPORT excerpt has the 32 lines 1852-1858, 2774-2780, 3087-3093, 4493-4503",
      sorted(VR) == rng(1852, 1858) + rng(2774, 2780) + rng(3087, 3093) + rng(4493, 4503))
J = lambda a, b: " ".join(TF[k].strip() for k in rng(a, b))

check("(a) line 584: 'c1-t2 adds (handoff AJ2, CLAIMED)'; line 1597: 'c1-t2 handoff AJ2 and AK2 (CLAIMED)'",
      "c1-t2 adds (handoff AJ2, CLAIMED)" in TF[584] and "c1-t2 handoff AJ2 and AK2 (CLAIMED)" in TF[1597])
check("(a) T4-290 (VERIFY_REPORT line 2779): 'T2's extension is also CONFIRMED under the explicitly unchanged "
      "high-row margin and norm-domination hypotheses'; line 2777 names T2 REVIEW_T4_277",
      "T2's extension is also CONFIRMED under the explicitly unchanged high-row margin and norm-domination hypotheses"
      in VR[2779] and "T2 REVIEW_T4_277" in VR[2777])
check("(b) lines 325-327: 'the T2-R3 L^2 budget above 1.1746 times the sharpw ceiling (beta 2) or 1.0612 times the "
      "TB-sharp ceiling (beta 11/4)'",
      "the T2-R3 L^2 budget above 1.1746 times the sharpw ceiling (beta 2) or 1.0612 times the TB-sharp ceiling "
      "(beta 11/4)" in J(325, 327))
check("(b) lines 1847-1848: '1.0612 over the TB-sharp ceiling (beta 11/4) in the T2-R3 L^2 budget'",
      "1.0612 over the TB-sharp ceiling (beta 11/4) in the T2-R3 L^2 budget" in J(1847, 1848))
check("(b) lines 685-687 (section 2.8): 'T2-R3 balls (beta 2)' and 'balls of the T2-R1 TB-sharp matrix with E0 as "
      "one component (beta 11/4)'",
      "T2-R3 balls (beta 2)" in J(685, 687)
      and "balls of the T2-R1 TB-sharp matrix with E0 as one component (beta 11/4)" in J(685, 687))
check("(c) line 425: 'K_H eta <= r and the L^2 contraction c_s r/beta_L < 1'; lines 425-426 do not mention "
      "'beta > 0' or '7/10'",
      "K_H eta <= r and the L^2 contraction c_s r/beta_L < 1" in TF[425]
      and "beta > 0" not in J(425, 426) and "7/10" not in J(425, 426))
check("(d) line 495: FW-T-T4ALT-defect-v1 row with 'epsilon_max 1.8938e-7' and no box parameters (no '2^-17')",
      "FW-T-T4ALT-defect-v1" in TF[495] and "epsilon_max 1.8938e-7" in TF[495] and "2^-17" not in TF[495])
notes = (HERE.parent / "notes/T2_T4L2_sharp.md").read_text()
hand = (HERE.parent / "handoff/T2_to_T1_v01.md").read_text()
check("(d) handoff M2: 'Box 1 (m = 2^-17, B = 1/100, s = 2^-18): eps_max = 1.8938e-7' and 'Box 2 (m = 2^-16, "
      "B = 1/200): eps_max = 6.1967e-8'",
      "Box 1 (m = 2^-17, B = 1/100, s = 2^-18): eps_max = 1.8938e-7" in hand
      and "Box 2 (m = 2^-16, B = 1/200): eps_max = 6.1967e-8" in hand)
check("erratum (i): line 684 'with the fixed state 131 floors, w1 >= 2, w2 >= 1, C >= K00 >' and line 685 '390.68'",
      "with the fixed state 131 floors, w1 >= 2, w2 >= 1, C >= K00 >" in TF[684] and TF[685].startswith("390.68"))
check("erratum (i): line 2147 (section 11 item 80) 'Lines 612 to 617 (c1-t2 D2, D3): the WU3 hypotheses must be stated "
      "(fixed state 131 floors, w1 >= 2'",
      "Lines 612 to 617 (c1-t2 D2, D3): the WU3 hypotheses must be stated (fixed state 131 floors, w1 >= 2" in TF[2147])

check("erratum (ii): notes lines 'K_H <= 10000/1037 = 9.6432' and 'K_H <= 10000/1557 = 6.4226'; draft 55 line 408 "
      "'K_H = 1/beta <= | 9.6432 | 6.4226'",
      "K_H <= 10000/1037 = 9.6432." in notes and "K_H <= 10000/1557 = 6.4226." in notes
      and "| K_H = 1/beta <= | 9.6432 | 6.4226 |" in TF[408])
res = {}
for name, mu, A, r, disp, quot in (("sharp", Q(200587, 968000), Q(8, 5) * 88, Q(147, 200000), Q(96432, 10 ** 4),
                                    Q(10000, 1037)),
                                   ("sharpw", Q(201799, 648000), Q(8, 5) * 72, Q(1351, 10 ** 6), Q(64226, 10 ** 4),
                                    Q(10000, 1557))):
    beta = mu - A * r
    res[name] = {"beta": str(beta), "K_H_exact": str(1 / beta), "K_H_float": "%.9f" % float(1 / beta),
                 "quotient": str(quot), "quotient_float": "%.9f" % float(quot)}
    check("%s: beta(r) = %s; 10000/%d lies in (%s, %s + 10^-4), so '= %s' is a rounded-down display; 1/beta(r) = %s "
          "<= %s (FLOAT: beta about %.9f, 10000/%d about %.7f, 1/beta about %.6f)"
          % (name, beta, 10000 / quot, float(disp), float(disp), float(disp), 1 / beta, float(disp), float(beta),
             10000 / quot, float(quot), float(1 / beta)),
          disp < quot < disp + Q(1, 10 ** 4) and 1 / beta <= disp and 1 / beta < quot)
check("beta(sharp) = 12551327/121000000 and beta(sharpw) = 63092119/405000000",
      res["sharp"]["beta"] == "12551327/121000000" and res["sharpw"]["beta"] == "63092119/405000000")

check("T4-175 (line 1857): 'CONFIRMED' with lower bound 6091157959/250000000000; line 1855 'above0.02436463'",
      "Result and verdict: CONFIRMED." in VR[1857] and "6091157959/250000000000" in VR[1857]
      and "above0.02436463" in VR[1855])
f175, f2, f082 = Q(6091157959, 250000000000), Q(24364634, 10 ** 9), Q(1625064, 10 ** 8)
check("6091157959/250000000000 = %.12f: > 0.02436463 and < 0.024364634 (so T4-175 confirms 0.02436463, not the "
      "ninth digit of c1-t2's 0.024364634)" % float(f175), Q(2436463, 10 ** 8) < f175 < f2)
check("ratios to T4-082's 0.01625064: about %.6f (T4-175) and about %.6f (c1-t2 W4), FLOAT; both in [1.495, 1.505)"
      % (float(f175 / f082), float(f2 / f082)),
      Q(1495, 1000) <= f175 / f082 < f2 / f082 < Q(1505, 1000))
check("T4-328 (line 3092): 'REFUTED as an indexed specification. The correct nonautomatic L2 list is(2,0),(3,0),(4,0)'",
      "The correct nonautomatic L2 list is(2,0),(3,0),(4,0)" in VR[3092] and "REFUTED" in VR[3092])
TV = numbered(HERE / "data/inputs/theory_v01_47ba2ee7_excerpt.txt")
check("theory_v01 excerpt has lines 64-66 and 83-85; line 65 'gamma = 1/c_l = 0.552389, delta = 1 - gamma = 0.447611'; "
      "line 66 'e(h, k) = gamma - h delta - 2k'; line 84 'the sectors (1,0), (2,0), (3,0) to vanish (exponents 0.105, "
      "-0.343, -0.790)'",
      sorted(TV) == [64, 65, 66, 83, 84, 85] and "gamma = 1/c_l = 0.552389, delta = 1 - gamma = 0.447611" in TV[65]
      and TV[66].startswith("e(h, k) = gamma - h delta - 2k.")
      and "the sectors (1,0), (2,0), (3,0) to vanish (exponents 0.105, -0.343, -0.790)" in TV[84])
check("notes/T2_T4L2_sharp.md: 'FW-T-T4L2-v1 (theory_v01 R2): (1,0), (2,0), (3,0) EXACT-ZERO' (theory_v01 labels)",
      "FW-T-T4L2-v1 (theory_v01 R2): (1,0), (2,0), (3,0) EXACT-ZERO" in notes)
# gamma - h delta - 2k and 1 - l delta - 2q with gamma = 1 - delta, l = h + 1, q = k: both sides are affine in delta,
# so agreement at delta = 0 and delta = 1 is agreement for every delta.
check("with gamma = 1 - delta and l = h + 1: gamma - h delta - 2k = 1 - l delta - 2k (affine in delta, equal at delta = "
      "0 and 1), so the theory_v01 sectors (1,0), (2,0), (3,0) are (l, q) = (2,0), (3,0), (4,0)",
      all((1 - d) - h * d - 2 * k == 1 - (h + 1) * d - 2 * k for d in (Q(0), Q(1)) for h in (1, 2, 3) for k in (0,)))
dl = Q(447611, 10 ** 6)
ex = [float(1 - l * dl) for l in (2, 3, 4)]
check("at delta = 0.447611: 1 - l delta for l = 2, 3, 4 rounds to %.3f, %.3f, %.3f (theory_v01: 0.105, -0.343, -0.790)"
      % tuple(ex),
      ["%.3f" % x for x in ex] == ["0.105", "-0.343", "-0.790"])
check("T4-485 (line 4501): 'CONFIRMED T2 reciprocal review and finite report repair'; line 4503 names the frozen T2 "
      "review dae1f389...",
      "CONFIRMED T2 reciprocal review and finite report repair" in VR[4501]
      and "dae1f3895fc984cfe32ff0418087eeb988bc0b363b5f088ea346c6d65385b057" in VR[4503])
el = time.time() - T0
print("%d checks, %d FAIL, %.2f s" % (N_[0], len(FAILS), el))
OUT = {"input": {str(p.relative_to(HERE.parent)): h for p, h in PINS.items()},
       "K_H": res, "t4_175_floor": "%.12f" % float(f175), "ratio_t4_175_over_t4_082": "%.6f" % float(f175 / f082),
       "checks": N_[0], "fails": FAILS, "elapsed_s": round(el, 2)}
(HERE / "data/bs_draft55_errata_check_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
sys.exit(1 if FAILS else 0)
