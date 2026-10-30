"""Checks for the T2_FINAL_SUMMARY repairs after c1-t4 T4-491 (TEAM_NOTE_v272, 17:28:26Z) and for a sweep of the
decimal displays written with "=" in that file (handoff BT).

T4-491 items, checked independently here:
  1. section 6 item 1 said a scalar closure "needs" a fixed-c L2 distance below 3.79e-6. The FW-T-TB-sharp-v1
     conditions (mu0 = 297/1000, C' = 402, c_U = 8/5, N_s >= 512 ||h||_2, 0 < s <= 2^-10; rate beta = mu0 - 402 s -
     (8/5) r/sqrt(s) > 0, eta <= beta r, low contraction K_L c_s r < 1 with K_L = (19/5 - c_s r)^-1, slope c_s r < 7/10)
     hold at s = 1/4096, r = 512 * 3791/10^9, eta = 10^-7, which is an L2 budget of 3.791e-6 > 3.79e-6. The common
     bound is sup_s (mu0 - C' s) sqrt(s)/(c_U 512), whose square is 4 mu0^3/(27 C' c_U^2 2^18) < (3.7930e-6)^2;
  2. the factor sqrt(k/K) u/v of the relaxed suprema (k = 39068/100, u = 15871/10000; K and v from T4-462
     verification/result.json, as in arith/t4_468_scope.py) lies in (0.99998312568, 0.99998312569), so 0.99998313 is
     its nearest eight-decimal rounding, not its value;
  3. the lower bounds of section 5 do not rank the actual distances (no computation; the check only records that the
     table's smallest lower bound is not 007's);
  4. Proposition G: (50/217)/(3 sqrt 28248) < 4.5717e-4 < 25/54684, so the bound 4.5717e-4 rests on the middle bound,
     and "25/54684 = 4.5717e-4" was a rounded-down display.
Sweep: each decimal below appears after "=" in the 17:25Z summary; each is compared exactly (Fractions) or in Arb
(256 bits) with the expression it displays, and classified as exact, rounded up or rounded down. The expected
classes were entered after test runs: the first classified R_univ(6/5) and the third the second defect box as
rounded up (my expectations had been rounded down). The two section 3 entries (rows T4-335 and T4-359, with
dq = -q* - 3 = 1 - gamma) were added after the summary edit of 17:42Z, which relabels them; the first shows that
the T4-335 row's "<= ... = 5.0442 H" was too strong. The expected class of theta was entered after a Fraction
computation run before 17:43:16Z (I had expected rounded down). A third version adds one check: the T4-335
constant lies in (5.04422709906931, 5.04422709906932), so the 5.04422709906932 of REVIEW_T4_335 R2 and the
"mu < 5.04423" of later documents are valid upper bounds. Decimals printed in the log with FLOAT are float
displays.
No peer code is executed.

Run from artifacts/:  python3 -B -u arith/t4_491_summary_items.py
Takes no arguments. Needs python-flint. Output: stdout (logs/t4_491_summary_items.log by the README command),
data/t4_491_summary_items_results.json.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as Q
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: t4_491_summary_items.py (no arguments)")
T0 = time.time()
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]
RJ = HERE.parents[1] / "c1-t4/research/weight_uniform_gram_audit/verification/result.json"
H_RJ = "61803920bea366913555ebb213ac40b466d370b1c92dd5cfe9cc9b67b9895450"
FAILS, N_ = [], [0]


def check(msg, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


# 1. scalar budget
mu0, Cp, cU, sq = Q(297, 1000), Q(402), Q(8, 5), 512
s, b = Q(1, 4096), Q(3791, 10 ** 9)
r = sq * b
beta = mu0 - Cp * s - cU * r * 64                      # sqrt(s) = 1/64
csr2_up = r ** 2 / (4 * 3 * s * (1 + s))               # (c_s r)^2 < this, since pi > 3
d_up = Q(36, 1000)
check("item 1: s = 1/4096 <= 2^-10, r = 512 * 3791/10^9 = %s, beta = %s > 0, beta r >= 10^-7" % (r, beta),
      0 < s <= Q(1, 1024) and beta == Q(1957759, 20000000000) and beta > 0 and beta * r >= Q(1, 10 ** 7))
check("item 1: (c_s r)^2 < r^2/(12 s (1 + s)) < (36/1000)^2, so slope c_s r < 7/10, 19/5 - c_s r > 0 and "
      "K_L c_s r < (36/1000)/(19/5 - 36/1000) < 1",
      csr2_up < d_up ** 2 and d_up < Q(7, 10) and d_up / (Q(19, 5) - d_up) < 1)
check("item 1: the admitted L2 budget r/512 = 3791/10^9 exceeds 3.79e-6 and is below 3.7930e-6",
      r / sq == b and Q(379, 10 ** 8) < b < Q(37930, 10 ** 10))
sup2 = 4 * mu0 ** 3 / (27 * Cp * cU ** 2 * sq ** 2)
tstar2 = mu0 / (3 * Cp)
check("item 1: sup_s (mu0 - C' s) sqrt(s)/(c_U 512) squared = 4 mu0^3/(27 C' c_U^2 2^18) = %s, in "
      "((3.7929e-6)^2, (3.7930e-6)^2); attained at s = mu0/(3 C') = %s <= 2^-10" % (sup2, tstar2),
      Q(37929, 10 ** 10) ** 2 < sup2 < Q(37930, 10 ** 10) ** 2 and tstar2 <= Q(1, 1024)
      and (mu0 - Cp * tstar2) ** 2 * tstar2 / (cU * sq) ** 2 == sup2)
# 2. relaxation factor
check("sha256 of T4-462 verification/result.json is %s...%s" % (H_RJ[:8], H_RJ[-8:]),
      hashlib.sha256(RJ.read_bytes()).hexdigest() == H_RJ)
RES = json.loads(RJ.read_text())
K, v = arb(RES["K"]), arb(RES["v"])
f = (arb(39068) / 100 / K).sqrt() * (arb(15871) / 10000) / v
check("item 2: f = sqrt(k/K) u/v = %s lies in (0.99998312568, 0.99998312569); 0.99998313 - f in (0, 5e-9)"
      % f.str(15), bool(f > arb("0.99998312568")) and bool(f < arb("0.99998312569"))
      and bool(arb("0.99998313") - f > 0) and bool(arb("0.99998313") - f < arb("5e-9")))
# 3. ordering
lb = {"007": Q(4769166867, 10 ** 12), "005": Q(1625064, 10 ** 8), "008 (mode 7 probe)": Q(1938714195, 10 ** 12),
      "d2": Q(29552675, 10 ** 8), "Mpen2": Q(55006675, 10 ** 8)}
check("item 3: the smallest lower bound in section 5 is that of 008 (mode 7 probe), 0.001938714195 < 0.004769166867 "
      "(007); lower bounds alone do not order the actual distances", min(lb, key=lb.get) == "008 (mode 7 probe)")
# 4. graded
mid2 = Q(50, 651) ** 2 / 28248                         # ((50/217)/(3 sqrt 28248))^2
t2 = Q(1, 28248)
check("item 4: max over t = sqrt(s) of (50/217) t (1/2 - 4708 t^2) is (50/217)/(3 sqrt 28248), at t^2 = 1/28248 "
      "(1/2 - 4708/28248 = 1/3)", Q(1, 2) - 4708 * t2 == Q(1, 3) and 1 - 3 * 4708 * 2 * t2 == 0)
check("item 4: 4.5697e-4 < (50/217)/(3 sqrt 28248) < 4.5698e-4 < 4.5717e-4 < 25/54684 (25/54684 about %.9e, FLOAT)"
      % float(Q(25, 54684)), mid2 < Q(45698, 10 ** 8) ** 2 and Q(45717, 10 ** 8) < Q(25, 54684)
      and mid2 > Q(45697, 10 ** 8) ** 2 and mid2 <= Q(25, 54684) ** 2)
# sweep
c = Q(4076476460239181, 2 ** 51)
g = 1 / c
A = lambda q: arb(q.numerator) / q.denominator
pi = arb.pi()
s18 = Q(1, 2 ** 18)
mu_d, A_d = Q(1, 10) - 4800 * s18, Q(5 * 2 ** 9)       # defect box: mu = 1/10 - 4800 s, A = 5/sqrt(s), sqrt(s) = 2^-9
eps = lambda m, B: ((mu_d - A_d * m - B) ** 2 - 4 * A_d * B * m) / (4 * A_d)
SW = [("line 29: gamma = 1/c", g, "0.552388769"),
      ("line 29: delta = 1 - gamma", 1 - g, "0.447611231"),
      ("line 89: E_lower (REVIEW_T4_375 R4)", Q(40673572058993602044748051350395, 51288398112310268946308133030216),
       "0.7930365064"),
      ("line 111: eta = 3/327680", Q(3, 327680), "9.1553e-6"),
      ("line 122: eta = 5289/50000000", Q(5289, 50000000), "1.0578e-4"),
      ("line 141: 76219/10^9", Q(76219, 10 ** 9), "7.6219e-5"),
      ("line 141: 4207/(2 10^7)", Q(4207, 2 * 10 ** 7), "2.1035e-4"),
      ("line 150: C_w (sharp) = 1 + 32/25 + 2^14", 1 + Q(32, 25) + 2 ** 14, "16386.28"),
      ("line 150: C_w (sharpw) = 1 + 32/25 + 2^15", 1 + Q(32, 25) + 2 ** 15, "32770.28"),
      ("line 174: epsilon_max, m = 2^-17, B = 1/100, s = 2^-18", eps(Q(1, 2 ** 17), Q(1, 100)), "1.8938e-7"),
      ("line 174: epsilon_max, m = 2^-16, B = 1/200, s = 2^-18", eps(Q(1, 2 ** 16), Q(1, 200)), "6.1967e-8"),
      ("line 197: 25/54684", Q(25, 54684), "4.5717e-4"),
      ("line 201: 25/(868 sqrt pi)", 25 / (868 * pi.sqrt()), "0.0162497"),
      ("line 301: R_univ(1) = sqrt(8 pi)/2", (8 * pi).sqrt() / 2, "2.5066"),
      ("line 301: R_univ(6/5) = sqrt(8 pi)(1 - c/5)/(11/5)", (8 * pi).sqrt() * A(1 - c / 5) / A(Q(11, 5)), "1.4537"),
      ("line 326: 6091157959/250000000000", Q(6091157959, 250000000000), "0.0243646318"),
      ("line 353: 2 - gamma", 2 - g, "1.447611"),
      ("line 437: T4-335 8/((-q-1)(-q-2)(-q-3)) at q* = gamma - 4", 8 / ((3 - g) * (2 - g) * (1 - g)), "5.0442"),
      ("line 439: T4-359 theta = dq/(2 + dq), dq = 1 - gamma", (1 - g) / (3 - g), "0.182877"),
      ("line 448: 25/(54684*512)", Q(25, 54684 * 512), "8.93e-7"),
      ("line 483: C_T = sqrt((4 log 2 - 1)/(8 pi))", ((4 * arb(2).log() - 1) / (8 * pi)).sqrt(), "0.2655730865568873")]
sweep = {}
for name, val, disp in SW:
    dq = Q(disp)                                       # the display as an exact decimal
    if isinstance(val, Q):                             # rational value: exact comparison
        kind = "exact" if val == dq else "rounded up" if val < dq else "rounded down"
        vs = "%s (FLOAT %.12e)" % (val, float(val)) if val.denominator > 1 else str(val)
    else:                                              # irrational value: Arb ball against the exact decimal
        kind = "rounded up" if bool(val < A(dq)) else "rounded down" if bool(val > A(dq)) else "undecided"
        vs = val.str(20)
    sweep[name] = {"display": disp, "value": vs, "kind": kind}
    print("SWEEP %s: %s, display %s: %s" % (name, vs, disp, kind), flush=True)
EXP = {"line 29: gamma = 1/c": "rounded up", "line 29: delta = 1 - gamma": "rounded down",
       "line 89: E_lower (REVIEW_T4_375 R4)": "rounded down", "line 150: C_w (sharp) = 1 + 32/25 + 2^14": "exact",
       "line 150: C_w (sharpw) = 1 + 32/25 + 2^15": "exact",
       "line 174: epsilon_max, m = 2^-17, B = 1/100, s = 2^-18": "rounded up",
       "line 174: epsilon_max, m = 2^-16, B = 1/200, s = 2^-18": "rounded up",
       "line 111: eta = 3/327680": "rounded up", "line 122: eta = 5289/50000000": "exact",
       "line 141: 76219/10^9": "exact", "line 141: 4207/(2 10^7)": "exact", "line 197: 25/54684": "rounded down",
       "line 201: 25/(868 sqrt pi)": "rounded up", "line 301: R_univ(1) = sqrt(8 pi)/2": "rounded down",
       "line 301: R_univ(6/5) = sqrt(8 pi)(1 - c/5)/(11/5)": "rounded up",
       "line 326: 6091157959/250000000000": "rounded down", "line 353: 2 - gamma": "rounded down",
       "line 437: T4-335 8/((-q-1)(-q-2)(-q-3)) at q* = gamma - 4": "rounded down",
       "line 439: T4-359 theta = dq/(2 + dq), dq = 1 - gamma": "rounded up",
       "line 448: 25/(54684*512)": "rounded up", "line 483: C_T = sqrt((4 log 2 - 1)/(8 pi))": "rounded down"}
check("sweep: the %d displays are classified as expected (%d exact)"
      % (len(SW), sum(x == "exact" for x in EXP.values())),
      {k: x["kind"] for k, x in sweep.items()} == EXP)
mu335 = 8 / ((3 - g) * (2 - g) * (1 - g))
check("T4-335: 8/((-q*-1)(-q*-2)(-q*-3)) = 8/((3 - gamma)(2 - gamma)(1 - gamma)) lies in (5.04422709906931, "
      "5.04422709906932); 5.0442 < it < 5.04423",
      Q(504422709906931, 10 ** 14) < mu335 < Q(504422709906932, 10 ** 14) and Q(50442, 10 ** 4) < mu335
      < Q(504423, 10 ** 5))
el = time.time() - T0
print("%d checks, %d FAIL, %.2f s" % (N_[0], len(FAILS), el))
OUT = {"input": {"c1-t4/research/weight_uniform_gram_audit/verification/result.json": H_RJ},
       "item1": {"r": str(r), "beta": str(beta), "sup_sq": str(sup2)}, "item2_factor": f.str(15),
       "item4_middle_sq": str(mid2), "sweep": sweep, "checks": N_[0], "fails": FAILS, "elapsed_s": round(el, 2)}
(HERE / "data/t4_491_summary_items_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
sys.exit(1 if FAILS else 0)
