"""Check of the maximality point of c1-t4 T4-479 (TEAM_NOTE_v258) on the frozen 16:30 report of c1-coord
(coordination/frozen/FINAL_REPORT_frozen_1630.md, lines 22-26 and 110-116): is 2.1035e-4 the largest admissible
residual of FW-T-T4L2-sharpw-v1 at s = 1/5184, w = (2^15, 2^20)?

The parameter checks of FW-T-T4L2-sharpw-v1 (notes/T2_T4L2_sharp.md section 3) hold for any r > 0 with
beta(r) = mu - A r > 0 (mu = mu0 - C' s, A = (8/5)/sqrt(s)), eta <= beta(r) r, c_s r/2 < 1 and 7/10 - c_s r > 0.
So at fixed norm the supremum of admissible eta over r is mu^2/(4A), attained at r* = mu/(2A). The same value is
epsilon_max of FW-T-T4L2-defect-v1 (AUDITED T4-065) at g = 0 (m = 0, B = 0). Checked here in exact rationals:
  - mu = 201799/648000, A = 576/5, eta* = 40722836401/193491763200000, r* = 201799/149299200;
  - beta(r) r = eta* - A (r - r*)^2, so every other r gives less; eta* > 4207/(2 10^7) and eta* > 2.1046e-4;
  - at r*: c_s r*/2 < 1 and 7/10 - c_s r* > 0, with c_s = (4 pi s (1 + s))^(-1/2) and pi > 314159/100000.
Side value (Arb, not norm-comparable): the theory_v03 rate row over all s gives sup = (5/2) C'^2 s0^(5/2) at
s0 = mu0/(5 C') = 97/496250, a threshold in the different norm X_(s0,w).
No c1-t4 or c1-coord code is executed. Read only (sha256 asserted): the frozen report, notes/T2_T4L2_sharp.md.

Run from artifacts/:  python3 -B -u arith/t4_479_sharpw_max.py
Takes no arguments. Needs python-flint (arb). Output: stdout (logs/t4_479_sharpw_max.log by the README command),
data/t4_479_sharpw_max_results.json.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as Q
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: t4_479_sharpw_max.py (no arguments)")
T0 = time.time()
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]
R6 = HERE.parents[1]
REPORT = R6 / "c1-coord/coordination/frozen/FINAL_REPORT_frozen_1630.md"
NOTES = HERE.parent / "notes/T2_T4L2_sharp.md"
PINS = {REPORT: "244c9c223dad0925c570d594cb4afdfcbbcb8196d5981a6c8cf024827813f838",
        NOTES: "cb72c73e2b94c95302838ba5826a1a2cece680083f3e6bc37531a6ec03635a2f"}
FAILS, N_ = [], [0]


def check(msg, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


for p, h in PINS.items():
    check("sha256 of %s is %s...%s" % (p.relative_to(R6), h[:8], h[-8:]),
          hashlib.sha256(p.read_bytes()).hexdigest() == h)
rep = REPORT.read_text().splitlines()
blk1 = " ".join(rep[21:26])
blk2 = " ".join(rep[109:116])
check("frozen report lines 22-26: 'The largest admissible residual is that of FW-T-T4L2-sharpw-v1' with 2.1035e-4",
      "The largest admissible" in blk1 and "FW-T-T4L2-sharpw-v1" in blk1 and "2.1035e-4" in blk1)
check("frozen report lines 110-116: 'The largest admissible residual in a scalar norm is FW-T-T4L2-sharpw-v1' with "
      "2.1035e-4 and radius 1351/1000000",
      "The largest admissible residual in a scalar norm is FW-T-T4L2-sharpw-v1" in blk2.replace("  ", " ")
      and "2.1035e-4" in blk2 and "1351/1000000" in blk2)
notes = NOTES.read_text()
check("notes/T2_T4L2_sharp.md: beta = mu0 - C' s - (8/5) r/sqrt(s), mu0 - C' s = 201799/648000, r = 1351/1000000, "
      "eta = 4207/20000000",
      "beta = mu0 - C' s - (8/5) r/sqrt(s)" in notes and "mu0 - C' s = 201799/648000" in notes
      and "r = 1351/1000000" in notes and "eta = 4207/20000000" in notes)

mu0, Cp, s = Q(97, 250), 397, Q(1, 5184)
mu = mu0 - Cp * s
A = Q(8, 5) * 72                      # (8/5)/sqrt(s), sqrt(s) = 1/72
eta_star = mu ** 2 / (4 * A)
r_star = mu / (2 * A)
check("mu = 201799/648000, A = 576/5", mu == Q(201799, 648000) and A == Q(576, 5))
check("eta* = mu^2/(4A) = %s = 201799^2 * 5/(648000^2 * 2304)" % eta_star,
      eta_star == Q(40722836401, 193491763200000) and 201799 ** 2 == 40722836401)
check("r* = mu/(2A) = %s; beta(r*) = mu/2 > 0; beta(r*) r* = eta*" % r_star,
      r_star == Q(201799, 149299200) and mu - A * r_star == mu / 2 and (mu - A * r_star) * r_star == eta_star)
rr = [Q(1351, 10 ** 6), Q(1, 1000), Q(2, 1000), r_star + Q(1, 10 ** 12), r_star - Q(1, 10 ** 12)]
check("beta(r) r = eta* - A (r - r*)^2 at r = 1351/10^6, 1/1000, 2/1000, r* +- 10^-12 (each < eta*)",
      all((mu - A * x) * x == eta_star - A * (x - r_star) ** 2 and (mu - A * x) * x < eta_star for x in rr))
beta_pub = mu - A * Q(1351, 10 ** 6)
check("at the published r = 1351/10^6: beta = %s >= 1557/10000 and 4207/(2 10^7) <= (1557/10000) r <= beta r < eta*"
      % beta_pub, beta_pub >= Q(1557, 10000) and Q(4207, 2 * 10 ** 7) <= Q(1557, 10000) * Q(1351, 10 ** 6)
      <= beta_pub * Q(1351, 10 ** 6) < eta_star)
check("2.1046e-4 < eta* < 2.1047e-4 and eta* > 4207/(2 10^7) = 2.1035e-4",
      Q(21046, 10 ** 8) < eta_star < Q(21047, 10 ** 8) and eta_star > Q(4207, 2 * 10 ** 7))
ratio = eta_star / Q(4207, 2 * 10 ** 7)
check("eta*/(4207/(2 10^7)) = %.9f, in (1.0005, 1.0006)" % float(ratio), Q(10005, 10000) < ratio < Q(10006, 10000))
cs2_up = 1 / (4 * Q(314159, 100000) * s * (1 + s))            # c_s^2 < this, since pi > 314159/100000
x2 = cs2_up * r_star ** 2                                      # (c_s r*)^2 < x2
check("(c_s r*)^2 < %.9e < (0.02746)^2, so c_s r*/2 < 0.01373 < 1 and 7/10 - c_s r* > 0.67254 > 0" % float(x2),
      x2 < Q(2746, 10 ** 5) ** 2)
cs = 1 / (4 * arb.pi() * (arb(1) / 5184) * (arb(5185) / 5184)).sqrt()
csr = cs * (arb(201799) / 149299200)
check("Arb: c_s = %s, c_s r* = %s (inside the rational bound)" % (cs.str(12), csr.str(12)),
      bool(csr < arb(2746) / 10 ** 5) and bool(csr > 0))
m, B = Q(0), Q(0)
eps_defect = ((mu - A * m - B) ** 2 - 4 * A * B * m) / (4 * A)
check("FW-T-T4L2-defect-v1 epsilon_max at g = 0 (m = B = 0) equals eta*", eps_defect == eta_star)
s0 = mu0 / (5 * Cp)
check("theory_v03 rate row over s: the optimum s0 = mu0/(5 C') = %s solves mu0 - C' s = 4 C' s" % s0,
      s0 == Q(97, 496250) and mu0 - Cp * s0 == 4 * Cp * s0)
s0a = arb(97) / 496250
sup_s = arb(5) / 2 * Cp ** 2 * s0a ** 2 * s0a.sqrt()
fs = lambda sa: (arb(mu0.numerator) / mu0.denominator - Cp * sa) ** 2 * sa.sqrt() * 5 / 32
check("Arb: sup over s = (5/2) C'^2 s0^(5/2) = %s = (mu0 - C' s0)^2 sqrt(s0) 5/32; above eta* (different norm)"
      % sup_s.str(12), bool(abs(sup_s - fs(s0a)) < arb(10) ** -60) and bool(sup_s > arb(eta_star.numerator)
                                                                          / eta_star.denominator))
el = time.time() - T0
print("%d checks, %d FAIL, %.2f s" % (N_[0], len(FAILS), el))
OUT = {"input": {str(p.relative_to(R6)): h for p, h in PINS.items()},
       "mu": str(mu), "A": str(A), "eta_star": str(eta_star), "r_star": str(r_star),
       "eta_star_over_published": "%.12f" % float(ratio), "cs_r_star_sq_upper": str(x2),
       "s0": str(s0), "sup_over_s_arb": sup_s.str(20), "checks": N_[0], "fails": FAILS, "elapsed_s": round(el, 2)}
(HERE / "data/t4_479_sharpw_max_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
sys.exit(1 if FAILS else 0)
