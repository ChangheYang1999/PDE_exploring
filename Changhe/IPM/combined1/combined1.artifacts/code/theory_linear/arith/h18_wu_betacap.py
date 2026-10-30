"""Proposition WU3 at the largest L2 margin the bL family can certify: every weight pair and every beta_L.

In FW-T-T4L2-bL-v1 the L2 margin enters only through (B-L2)_(beta_L): 1 + c - theta - kappa >= beta_L, with
theta = ess sup (|grad rho| - rho_y)/2 >= 0 (|grad rho| >= rho_y) and kappa = sqrt(kappa^2) >= 0, kappa^2 =
[(log 2 - 1/2)||D rho_x||^2 + (3 log 2 - 2)||D rho_y||^2]/(16 pi) (c1-t4 research/l2_closure/PROOF.md, T4-019).
So beta_L <= 1 + c. Hypothesis (A) there is 9/5 < c < 37/20, so beta_L < 57/20; for the H18 snapshots c = c0 and
beta_L <= 1 + c0. G(mu0) is increasing in its (3,3) entry w2 (beta - mu0), so the WU3 budget is nondecreasing in
beta, and the WU3 bound at beta = 57/20 covers every beta_L and every (w1, w2) of that family, with the registered
floors 1/2, 9/10 and the weight-independent constants K00, A' + B'.

The cell bound is the code of arith/h18_wu_sharp.py: its text up to the line 'ROWS = [' is executed here unchanged
(sha256 of the file asserted), which defines the constants, w2min2, w2lo3 and numer, and runs its three input checks.

Run from artifacts/:  python3 -B -u arith/h18_wu_betacap.py
Takes no arguments. Needs python-flint. Reads arith/h18_wu_sharp.py and the files it pins, data/h18_wu_sharp_results.json
and ../../c1-t4/research/l2_closure/PROOF.md (sha256 asserted), ../notes/T2_localized_BL2.md (sha256 recorded).
Output: stdout (logs/h18_wu_betacap.log by the README command), data/h18_wu_betacap_results.json.
"""
import hashlib
import json
import math
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

from flint import arb

if len(sys.argv) != 1:
    sys.exit("usage: h18_wu_betacap.py (no arguments)")
T0 = time.time()
HERE_ = Path(__file__).resolve().parents[1]
SH = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
WS = HERE_ / "arith/h18_wu_sharp.py"
H_WS = "a4f9f9f0191b9209a3da426f9347865418186f490423736b53649f35087f1197"
assert SH(WS) == H_WS, "h18_wu_sharp.py changed"
src_ws = WS.read_text()
pre = src_ws[:src_ws.index("ROWS = [")]
ns = {"__file__": str(WS), "__name__": "h18_wu_sharp_prefix"}
exec(compile(pre, str(WS), "exec"), ns)
check, N_, FAILS = ns["check"], ns["N_"], ns["FAILS"]
check("sha256 of arith/h18_wu_sharp.py is %s...%s (its prefix executed above)" % (H_WS[:8], H_WS[-8:]), SH(WS) == H_WS)
L2C = HERE_.parent.parent / "c1-t4/research/l2_closure/PROOF.md"
H_L2C = "e15173a459fd59e89c1c4746b0fb6f32d35891cc948930c0ded553ac5aeb6e0f"
WSR = HERE_ / "data/h18_wu_sharp_results.json"
H_WSR = "f3748a52"
BL2 = HERE_.parent / "notes/T2_localized_BL2.md"
check("sha256 of c1-t4 research/l2_closure/PROOF.md is %s...%s (T4-019 target proof)" % (H_L2C[:8], H_L2C[-8:]),
      SH(L2C) == H_L2C)
check("sha256 of data/h18_wu_sharp_results.json begins %s" % H_WSR, SH(WSR).startswith(H_WSR))
OUT = {"inputs": {"arith/h18_wu_sharp.py": SH(WS), "../../c1-t4/research/l2_closure/PROOF.md": SH(L2C),
                  "data/h18_wu_sharp_results.json": SH(WSR), "../notes/T2_localized_BL2.md": SH(BL2)}}
s = L2C.read_text()
for q in ("9/5<c<37/20", "theta=ess sup (sqrt(rho_x²+rho_y²)-rho_y)/2,",
          "kappa²=[(log2-1/2)||D rho_x||_2²+(3log2-2)||D rho_y||_2²]/(16pi).", "c+1-theta-kappa >=2.",
          "Re<A_k h,h> <= -(c+1-theta-kappa)||h||² <=-2||h||².", "||K||<=||K||_HS=kappa"):
    check("l2_closure PROOF.md quote '%s'" % q, q in s)
check("T2_localized_BL2.md: the bL hypothesis is '(B-L2)_(beta_L): 1 + c - theta - kappa >= beta_L'",
      "(B-L2)_(beta_L): 1 + c - theta - kappa >= beta_L." in BL2.read_text())
L2 = arb(2).log()
check("log 2 - 1/2 > 0 and 3 log 2 - 2 > 0 (so kappa^2 >= 0 and kappa = sqrt(kappa^2) >= 0)", L2 - arb(1) / 2 > 0
      and 3 * L2 - 2 > 0)
C0 = Fr(4076476460239181, 2251799813685248)
check("c0 = 4076476460239181/2251799813685248 lies in (9/5, 37/20), so 1 + c0 < 57/20", Fr(9, 5) < C0 < Fr(37, 20))

# monotonicity in beta: compare with the stored WU3 rows at beta 2 and 11/4 (same floors)
WSRJ = json.loads(WSR.read_text())
prev = {Fr(2): Fr(WSRJ["rows"][0]["Bstar3_upper"]), Fr(11, 4): Fr(WSRJ["rows"][1]["Bstar3_upper"])}
w2min2, w2lo3, numer, cU_lo, A_ = ns["w2min2"], ns["w2lo3"], ns["numer"], ns["cU_lo"], ns["A_"]
FC = ns["FC"]
D007, LEAST = Fr(4769166867, 10**12), Fr(1232449584, 10**12)
NC = 20000
OUT["rows"] = []
for lab, bL in (("bL family, beta_L <= 1 + c0 (H18 snapshots)", 1 + C0), ("bL family, beta_L < 57/20 (any c of (A))",
                                                                            Fr(57, 20))):
    m2, m1 = Fr(1, 2), Fr(9, 10)
    best, arg, n3 = arb(0), None, 0
    for k in range(NC):
        ma, mb = m2 * Fr(k, NC), m2 * Fr(k + 1, NC)
        cand = numer(mb) / (cU_lo * A_(w2min2(ma, m2, m1, bL)).sqrt())
        w3 = w2lo3(ma, mb, m2, m1, bL)
        if w3 is not None:
            n3 += 1
            w3m = w3 if w3 > 1 else arb(1)
            c3 = numer(mb) / (cU_lo * w3m.sqrt())
            if c3.upper() < cand.upper():
                cand = c3
        if cand.upper() > best.upper():
            best, arg = arb(cand.upper()), (ma, mb)
    m_, e_ = best.mid().man_exp()
    bu = Fr(int(m_)) * Fr(2)**int(e_)
    bu5 = Fr(math.ceil(bu * 10**10), 10**10)
    gain = (A_(bu5) / arb(FC["sharpw"]["b_fam"])).upper()
    check("%s: WU3 bound %.6e >= the beta 11/4 bound %.6e >= the beta 2 bound %.6e (monotone in beta)"
          % (lab, float(bu5), float(prev[Fr(11, 4)]), float(prev[Fr(2)])), bu5 >= prev[Fr(11, 4)] >= prev[Fr(2)])
    check("%s: bound < 1/1000 and below the least H18 weak root 0.001232449584 (snapshot 015)" % lab,
          bu5 < Fr(1, 1000) and bu5 < LEAST)
    row = {"label": lab, "beta": str(bL), "Bstar3_upper": str(bu5), "Bstar3_upper_dec": "%.10f" % float(bu5),
           "argmax_cell": [str(arg[0]), str(arg[1])], "cells": NC, "cells_with_3x3": n3,
           "over_registered_sharpw_upper": "%.4f" % (math.ceil(float(gain) * 10**4 * (1 + 1e-12)) / 10**4),
           "factor_007_lower": "%.1f" % (math.floor(float(D007 / bu5) * 10) / 10),
           "factor_least_root_015_lower": "%.1f" % (math.floor(float(LEAST / bu5) * 10) / 10)}
    OUT["rows"].append(row)
    print("  %s: B*3 <= %.4e (cells %d, 3x3 used in %d, argmax cell [%.5f, %.5f]); over registered sharpw <= %s; "
          "007 distance / B*3 >= %s; least H18 root / B*3 >= %s" % (lab, float(bu5), NC, n3, float(arg[0]), float(arg[1]),
                                                                    row["over_registered_sharpw_upper"],
                                                                    row["factor_007_lower"],
                                                                    row["factor_least_root_015_lower"]))
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N_[0], FAILS, round(time.time() - T0, 3)
(HERE_ / "data/h18_wu_betacap_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N_[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
