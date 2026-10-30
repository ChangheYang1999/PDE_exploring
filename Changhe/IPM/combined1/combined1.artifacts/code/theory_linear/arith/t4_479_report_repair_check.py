"""Check of c1-coord's repair of the live FINAL_REPORT after c1-t4 T4-479 and reviews/CHECK_T4_479_SHARPW_MAX_T2.md
(answer 1, short answer 1 and the detailed defect paragraph; c1-coord NOTES_FOR_TEAM 16:45Z item 4).

Input: data/inputs/final_report_live_edde27fc_excerpt.txt, lines 22-31, 118-128, 380-385 and 468-472 of
c1-coord/FINAL_REPORT.md at sha256 edde27fc362222bab4b99e972ae3277d713b61174db0eb5f685707150cb3e0c3 (saved
2026-10-29T16:46:41Z, each line prefixed by its number and a tab). The live report keeps changing; if it still has
that hash, the excerpt is also compared with it in a NOTE line (not a counted check, so that a replay after the
report changes gives the same checks); otherwise only the excerpt's own sha256 is checked.
Checked in exact rationals, with mu = 201799/648000, A = 576/5 (as in arith/t4_479_sharpw_max.py):
  - the excerpt states eta* = 40722836401/193491763200000 (above 2.1046e-4) at X_(s,w)(h) <= 201799/149299200;
  - "about 1.3516e-3": 1.35155e-3 <= 201799/149299200 < 1.35165e-3;
  - "at r = 1351/1000000 the estimate already admits 2.1046e-4": beta(r) r >= 21046/10^8 at r = 1351/10^6;
  - "the 007 sharpw norm misses it by a factor above 3594606": with X_(s,w)(F_007) > 756.5312630768 (line 472),
    756.5312630768/eta* > 3594606; and 756.5312630768/(4207/(2 10^7)) > 3596535.57, the factor printed elsewhere.
No c1-coord code is executed.

Run from artifacts/:  python3 -B -u arith/t4_479_report_repair_check.py
Takes no arguments. Output: stdout (logs/t4_479_report_repair_check.log by the README command),
data/t4_479_report_repair_check_results.json.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as Q
from pathlib import Path

if len(sys.argv) != 1:
    sys.exit("usage: t4_479_report_repair_check.py (no arguments)")
T0 = time.time()
HERE = Path(__file__).resolve().parents[1]
R6 = HERE.parents[1]
EXC = HERE / "data/inputs/final_report_live_edde27fc_excerpt.txt"
EXC_SHA = "68168051a89e41ac8502534f468b5fc3fc9b5657cfb5bce1b01788dd51eb7f83"
LIVE = R6 / "c1-coord/FINAL_REPORT.md"
LIVE_SHA = "edde27fc362222bab4b99e972ae3277d713b61174db0eb5f685707150cb3e0c3"
FAILS, N_ = [], [0]


def check(msg, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


raw = EXC.read_bytes()
check("sha256 of the excerpt is %s...%s" % (EXC_SHA[:8], EXC_SHA[-8:]), hashlib.sha256(raw).hexdigest() == EXC_SHA)
lines = {}
for ln in raw.decode().splitlines():
    k, v = ln.split("\t", 1)
    lines[int(k)] = v
check("the excerpt has lines 22-31, 118-128, 380-385, 468-472 (32 lines)",
      sorted(lines) == list(range(22, 32)) + list(range(118, 129)) + list(range(380, 386)) + list(range(468, 473)))
live_sha = hashlib.sha256(LIVE.read_bytes()).hexdigest() if LIVE.exists() else None
if live_sha == LIVE_SHA:
    live = LIVE.read_text().splitlines()
    print("NOTE the live report still has sha256 %s...%s; the excerpt %s its lines (not counted as a check)"
          % (LIVE_SHA[:8], LIVE_SHA[-8:], "equals" if all(live[k - 1] == v for k, v in lines.items()) else
             "DIFFERS FROM"), flush=True)
else:
    print("NOTE the live report has changed since the excerpt was saved; only the excerpt hash is checked", flush=True)
blk = {name: " ".join(lines[k] for k in rng) for name, rng in
       (("answer 1", range(22, 32)), ("short answer 1", range(118, 129)), ("defect paragraph", range(380, 386)))}
for name, b in blk.items():
    check("%s states 40722836401/193491763200000 (above 2.1046e-4) and 201799/149299200, and cites T4-479" % name,
          "40722836401/193491763200000 (above 2.1046e-4)" in b and "201799/149299200" in b and "T4-479" in b)
check("answer 1 and short answer 1 also say that r = 1351/1000000 already admits 2.1046e-4 and cite "
      "CHECK_T4_479_SHARPW_MAX_T2",
      all("1351/1000000" in blk[x] and "admits 2.1046e-4" in blk[x] and "CHECK_T4_479_SHARPW_MAX_T2" in blk[x]
          for x in ("answer 1", "short answer 1")))
check("answer 1 states 'about 1.3516e-3' and 'a factor above 3594606'; line 472 states X_(s,w)(F) > 756.5312630768 "
      "and 3596535.57",
      "(about 1.3516e-3)" in blk["answer 1"] and "factor above 3594606" in blk["answer 1"]
      and "756.5312630768" in lines[472] and "3596535.57" in lines[472])

mu, A = Q(201799, 648000), Q(576, 5)
eta, rs = mu ** 2 / (4 * A), mu / (2 * A)
check("eta* = mu^2/(4A) = 40722836401/193491763200000 > 2.1046e-4 and r* = mu/(2A) = 201799/149299200",
      eta == Q(40722836401, 193491763200000) and eta > Q(21046, 10 ** 8) and rs == Q(201799, 149299200))
check("1.35155e-3 <= r* = %.10e < 1.35165e-3 (rounds to 1.3516e-3)" % float(rs),
      Q(135155, 10 ** 8) <= rs < Q(135165, 10 ** 8))
r = Q(1351, 10 ** 6)
br = (mu - A * r) * r
check("beta(r) r = %s = %.10e >= 2.1046e-4 at r = 1351/10^6" % (br, float(br)), br >= Q(21046, 10 ** 8))
X7 = Q(7565312630768, 10 ** 10)
f_new, f_old = X7 / eta, X7 / Q(4207, 2 * 10 ** 7)
check("756.5312630768/eta* = %.6f > 3594606" % float(f_new), f_new > 3594606)
check("756.5312630768/(4207/(2 10^7)) = %.6f > 3596535.57" % float(f_old), f_old > Q(359653557, 100))
el = time.time() - T0
print("%d checks, %d FAIL, %.2f s" % (N_[0], len(FAILS), el))
OUT = {"input": {"data/inputs/final_report_live_edde27fc_excerpt.txt": EXC_SHA, "c1-coord/FINAL_REPORT.md": LIVE_SHA},
       "eta_star": str(eta), "r_star": str(rs), "beta_r_at_1351e-6": str(br),
       "factor_vs_eta_star": "%.9f" % float(f_new), "factor_vs_published": "%.9f" % float(f_old),
       "checks": N_[0], "fails": FAILS, "elapsed_s": round(el, 2)}
(HERE / "data/t4_479_report_repair_check_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
sys.exit(1 if FAILS else 0)
