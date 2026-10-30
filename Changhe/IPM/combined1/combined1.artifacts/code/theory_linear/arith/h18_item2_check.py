"""H18 falsification check of T2_FINAL_SUMMARY section 0 item 2 ('Sharper constants are worth at most a factor of
about 2 (T4-119, T2-R3 weight scan)'), and of the claim in the same item that no re-tuning of the weights changes the
distance exclusions of item 1.

Run from artifacts/:  python3 -B -u arith/h18_item2_check.py
Takes no arguments. Needs python-flint (arb). Reads (read only; sha256 asserted unless stated):
  ../scratch/h18/T2_FINAL_SUMMARY.pre_H18.md (lane copy of the summary before the H18 repair),
  ../notes/T2_T4L2_sharp.md (T2-R3), arith/t4l2_sharp_framework.py (constants copied below),
  data/family_ceilings_exact_results.json (exact NC-T-DIST family ceilings),
  ../../c1-t4/VERIFY_REPORT.md (only the T4-119 and T4-185/T4-190 blocks are hashed; the file is append-only),
  ../../c1-t4/TEAM_NOTE_v58.md.
Checks:
  (A) inputs and verbatim quotes.
  (B) the numbers of item 2: the factor 331 (floor 330), the factor 76, the two T4-119 ratios, the FLOAT scan ratio.
  (C) the item 1 factors 1257, 1673, 10.43 are floors of the certified distance over the registered family ceilings;
      no number of item 2 enters them.
  (D) Proposition WU (new, this script): the L2 budget of the T2-R3 scheme, and of the TB-sharp scheme with E0 kept
      as one component, maximized over all weights w1 >= 2, w2 >= 1 and every mu0 with G_w(mu0) positive
      semidefinite, with C >= K00 and c_U >= A' + B'. Rigorous cover of mu0 in (0, m2) (Arb, exact rationals).
      Also the same bound with the state-131 matrix-floor ceilings of T4-119 in place of 1/2 and 9/10 (hypothetical
      floors; T4-119 says they do not bound other candidates).
Output: stdout (logs/h18_item2_check.log by the README command), data/h18_item2_check_results.json.
"""
import hashlib
import json
import math
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: h18_item2_check.py (no arguments)")
t_start = time.time()
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]
LANE = HERE.parent
R6 = LANE.parent
sha_b = lambda b: hashlib.sha256(b).hexdigest()
sha = lambda p: sha_b(Path(p).read_bytes())
A_ = lambda q: arb(q.numerator) / q.denominator
N, FAILS, OUT = [0], [], {"inputs": {}}


def check(name, ok):
    N[0] += 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def up(xv, sig=6):
    """decimal upper bound with sig significant digits (from the exact upper endpoint)."""
    m_, e_ = xv.upper().man_exp()
    v_ = Fr(int(m_)) * Fr(2)**int(e_)
    ex = math.floor(math.log10(float(v_)))
    pl = sig - 1 - ex
    out = Fr(math.ceil(v_ * Fr(10)**pl)) / Fr(10)**pl
    assert out >= v_
    return out


def lo(xv, sig=6):
    m_, e_ = xv.lower().man_exp()
    v_ = Fr(int(m_)) * Fr(2)**int(e_)
    ex = math.floor(math.log10(float(v_)))
    pl = sig - 1 - ex
    out = Fr(math.floor(v_ * Fr(10)**pl)) / Fr(10)**pl
    assert out <= v_
    return out


def fmt(q, sig=6):
    return "%.*e" % (sig - 1, float(q)) if abs(q) < 1e-3 or abs(q) >= 1e5 else ("%.*g" % (sig, float(q)))


# ---------------------------------------------------------------- (A) inputs
SUM = LANE / "scratch/h18/T2_FINAL_SUMMARY.pre_H18.md"
T2R3 = LANE / "notes/T2_T4L2_sharp.md"
FWS = HERE / "arith/t4l2_sharp_framework.py"
RFC = HERE / "data/family_ceilings_exact_results.json"
VR = R6 / "c1-t4/VERIFY_REPORT.md"
TN58 = R6 / "c1-t4/TEAM_NOTE_v58.md"
PIN = {SUM: "f4c565da80f39c120d4a787a16f29f40d828698a7cd7bab962295107904e88d4",
       T2R3: "cb72c73e2b94c95302838ba5826a1a2cece680083f3e6bc37531a6ec03635a2f",
       FWS: "d9799b66b4e77d1f379c994a46c17996f913413d334d39640651810962d6a717",
       RFC: "b1fea0a74af0a7729b38a27f1796deea0b3597b4ca9549ba235e9131af3b98a7",
       TN58: "cecb5ee3753141ff0fb33afb20ce3cf2bce8b9d1f18e74bd3f1b740f42340e89"}
for p, h in PIN.items():
    OUT["inputs"][str(p.relative_to(R6))] = sha(p)
    check("(A) sha256 of %s is %s...%s" % (p.relative_to(R6), h[:8], h[-8:]), sha(p) == h)
vr = VR.read_text()


def block(tag, nxt):
    i, j = vr.index("## %s:" % tag), vr.index("## %s:" % nxt)
    return vr[i:j]


B119, B185, B190 = block("T4-119", "T4-120"), block("T4-185", "T4-186"), block("T4-190", "T4-191")
OUT["inputs"]["c1-t4/VERIFY_REPORT.md T4-119 block"] = sha_b(B119.encode())
check("(A) T4-119 block of c1-t4 VERIFY_REPORT.md has sha256 fc668bed...0ced4927",
      sha_b(B119.encode()) == "fc668bed8f80a4025c58e1a1bf49a3d0e9e90ca2f74edd38cb5d77ea0ced4927")
OUT["inputs"]["c1-t4/VERIFY_REPORT.md T4-185 block"] = sha_b(B185.encode())
OUT["inputs"]["c1-t4/VERIFY_REPORT.md T4-190 block"] = sha_b(B190.encode())
s_sum, s_t2r3, s_fws, s_tn = SUM.read_text(), T2R3.read_text(), FWS.read_text(), TN58.read_text()
ITEM2 = ("2. Sharper constants are worth at most a factor of about 2 (T4-119, T2-R3 weight scan). The linear thresholds improved\n"
         "   from 6.3578e-7 (A2 Theorem D(b)) to 2.1035e-4 (sharpw), a factor 331. No re-tuning of s, weights, box shape or\n"
         "   defect g changes the distance exclusions (sections 2.4 and 5).")
check("(A) summary section 0 item 2, verbatim", ITEM2 in s_sum)
ITEM1 = ("That is 1257 times the best scalar budget,\n   1673 times the sharpw budget and 10.43 times the graded budget.")
check("(A) summary section 0 item 1, the three factors, verbatim", ITEM1 in s_sum)
check("(A) summary item 7: 'improves the proved 133.0042547837 by a factor 76'",
      "E_new(3/20) <= 1.749109" in s_sum and "improves the proved 133.0042547837 by a factor 76" in s_sum)
Q119 = ["At beta_L=2 with all other constants fixed, the threshold ceilings are approximately0.000165554533577083 (sharp) "
        "and0.000380259638882139 (sharpw).",
        "Their ratios to the published thresholds are2.17209007697664 and1.80774727303132, giving safe bounds2.2 and1.81.",
        "The ceiling itself need not be attainable, so this does not refute a sharper1.8 estimate based on additional "
        "information.",
        "The intervals are[0.972875,0.99116),[0.587238,0.61151),[-1.230876,-1.20662)",
        "quantify the maximum benefit within the fixed TP-5 Gram scheme"]
for q in Q119:
    check("(A) T4-119 quote '%s...'" % q[:60], q in B119)
check("(A) TEAM_NOTE_v58 quote 'These are ceilings with all other constants fixed, not attainable improvements.'",
      "These are ceilings with all other constants fixed, not attainable improvements." in s_tn)
check("(A) T4-119 identifies the second interval as the E2 (Hessian, M2) floor: 'relative to the improved P96 floor0.587238'",
      "the increase over the improved P96 floor0.587238" in B119)
check("(A) T4-185 is AUDITED with strict distance > 4769166867/10^12 (T4-190 block)",
      "T4-185 is AUDITED, giving strict fixed-c L2 distance >4769166867/10^12" in B190)
Q2R3 = ["largest eta is about 3.9e-4 (w = (2^20, 2^26), mu0 0.496; about 4.0e-4 in the limit mu0 -> 1/2)",
        "G_w(mu) = [[1/2 - mu, -347/10, -5], [-347/10, w1 (9/10 - mu) - 40, -3 w1], [-5, -3 w1, w2 (2 - mu)]].",
        "Assume (A) to (D), w1 >= 2, w2 >= 1, 0 < s <= 2^-10",
        "Hence the maximum on\n   [0, 1] is A' + B' <= 1.5871175 < 8/5.",
        "Only the off-diagonal entries depend on the weights",
        "so ||h||_(H^(2+s)) <= X_{s,w}(h)"]
for q in Q2R3:
    check("(A) T2-R3 note quote '%s...'" % q[:60].replace("\n", " "), q in s_t2r3)
for frag in ("m1 = SQPI / 2 * arb.gamma((1 - SMAX) / 2)",
             "w1c = arb(8) * arb(5).sqrt() / 5 * arb(6) ** (arb(-3) / 5)",
             "k1u, k1w = m1, m1 + arb(8) / 5",
             "cru, crw = arb(3) / 2 * m1, arb(3) / 2 * m1 + arb(32) / 15",
             "c8, dtop = 1 + w1c * 3 * PI / 4, 1 + w1c * PI / 2",
             "C, U1, U2, U3, R1, R2, R3, R4 = [arb(x) for x in (2, 6, 24, 160, 22, 32, 80, 2048)]",
             "q = 1 / (2 * SQPI)",
             "ps = arb(2) ** s * (1 + s).sqrt() / (2 * SQPI)",
             "Pw = ps * (1 + w1c * m1 * s) + w1c * m1 * s / (2 * SQPI)",
             "Ap = arb(4) / 5 * q + q * (1 + 4 * w1c * m1 * s) + 2 * Pw",
             "Bp = arb(9) / 5 * Pw",
             "K00 = dtop * C + c8 * U1 + (crw + 2 * k1w) * U2 + k1w * R2",
             "rows = [K00 + K01 / 2 + K02 / 2, K01 / 2 + K11 + K12 / 2, K02 / 2 + K12 / 2 + K22]"):
    check("(A) t4l2_sharp_framework.py contains '%s'" % frag, frag in s_fws)
FC = json.loads(RFC.read_text())["ceilings"]

# ---------------------------------------------------------------- (B) numbers of item 2
OUT["B"] = {}
eta_sw, eta_sh, eta_db = Fr(4207, 2 * 10**7), Fr(76219, 10**9), Fr(63578288, 10**14)
f331 = eta_sw / eta_db
check("(B) 2.1035e-4 / 6.3578288e-7 lies in (330, 331): the printed 'factor 331' is rounded to nearest; floor 330",
      330 < f331 < 331 and round(f331) == 331)
OUT["B"]["sharpw_over_A2Db"] = float(f331)
f76 = Fr(1330042547837, 10**10) / Fr(1749109, 10**6)
check("(B) 133.0042547837 / 1.749109 lies in [76, 77): 'a factor 76' is a floor", 76 <= f76 < 77)
OUT["B"]["Eq_star_over_Enew"] = float(f76)
r_sw = Fr("0.000380259638882139") / eta_sw
r_sh = Fr("0.000165554533577083") / eta_sh
check("(B) T4-119 ratios recomputed: 0.000380259638882139 / 2.1035e-4 = 1.807747273...; 0.000165554533577083 / 7.6219e-5 = 2.172090077...",
      abs(r_sw - Fr("1.80774727303132")) < Fr(1, 10**13) and abs(r_sh - Fr("2.17209007697664")) < Fr(1, 10**13))
OUT["B"]["T4_119_ratios"] = [float(r_sw), float(r_sh)]
r_scan = Fr(4, 10**4) / eta_sw, Fr(39, 10**5) / eta_sw
check("(B) T2-R3 FLOAT weight scan: 3.9e-4 and 4.0e-4 are 1.854 and 1.902 times 2.1035e-4 (FLOAT, not a bound)",
      Fr(1854, 1000) < r_scan[1] < Fr(1855, 1000) and Fr(1901, 1000) < r_scan[0] < Fr(1902, 1000))
OUT["B"]["scan_ratios_float"] = [float(r_scan[1]), float(r_scan[0])]

# ---------------------------------------------------------------- (C) item 1 factors
D007 = Fr(4769166867, 10**12)
OUT["C"] = {}
for key, printed, claim, digits in (("TB-sharp", Fr(37930, 10**10), 1257, 0), ("sharpw", Fr(28496, 10**10), 1673, 0),
                                    ("graded", Fr(45717, 10**8), Fr(1043, 100), 2)):
    bx = arb(FC[key]["b_fam"])
    check("(C) %s: exact family ceiling (Arb) <= printed %s" % (key, fmt(printed, 5)), bx < A_(printed))
    ratio = D007 / printed
    fl = Fr(math.floor(ratio * 10**digits), 10**digits)
    check("(C) %s: floor(4769166867e-12 / %s) at %d decimals = %s (the item 1 factor)" % (key, fmt(printed, 5), digits,
                                                                                          str(float(claim))),
          fl == claim)
    ex_lo = A_(D007) / bx
    check("(C) %s: distance / exact ceiling > the printed factor (Arb)" % key, ex_lo > A_(Fr(claim)))
    OUT["C"][key] = {"printed_budget": str(printed), "factor_floor": str(fl), "factor_exact_lower": ex_lo.str(12)}
check("(C) the family data entering the ceilings are (mu0, C, c_U, sqrt W2) = (297/1000, 402, 8/5, 512) for TB-sharp and "
      "(97/250, 397, 8/5, 1024) for sharpw; no T4-119 ceiling and no FLOAT scan value enters",
      (FC["TB-sharp"]["mu0"], FC["TB-sharp"]["C"], FC["TB-sharp"]["c_U"], FC["TB-sharp"]["sqrt_W2"]) == ("297/1000", 402, "8/5", 512)
      and (FC["sharpw"]["mu0"], FC["sharpw"]["C"], FC["sharpw"]["c_U"], FC["sharpw"]["sqrt_W2"]) == ("97/250", 397, "8/5", 1024))

# ---------------------------------------------------------------- (D) Proposition WU
PI = arb.pi()
SQPI = PI.sqrt()
SMAX = arb(1) / 1024
m1k = SQPI / 2 * arb.gamma((1 - SMAX) / 2)
w1c = arb(8) * arb(5).sqrt() / 5 * arb(6) ** (arb(-3) / 5)
k1u, k1w = m1k, m1k + arb(8) / 5
cru, crw = arb(3) / 2 * m1k, arb(3) / 2 * m1k + arb(32) / 15
c8, dtop = 1 + w1c * 3 * PI / 4, 1 + w1c * PI / 2
Cc, U1, U2, U3, R1, R2, R3, R4 = [arb(x) for x in (2, 6, 24, 160, 22, 32, 80, 2048)]
K00 = dtop * Cc + c8 * U1 + (crw + 2 * k1w) * U2 + k1w * R2
s_ = SMAX
q_ = 1 / (2 * SQPI)
ps = arb(2) ** s_ * (1 + s_).sqrt() / (2 * SQPI)
Pw = ps * (1 + w1c * m1k * s_) + w1c * m1k * s_ / (2 * SQPI)
Ap = arb(4) / 5 * q_ + q_ * (1 + 4 * w1c * m1k * s_) + 2 * Pw
Bp = arb(9) / 5 * Pw
cUlo = Ap + Bp
check("(D) K00 in (390.68, 390.69) (T2-R2 Proposition 8: 390.69) and A' + B' in (1.5871, 1.5872) (T2-R3 step 3)",
      arb(39068) / 100 < K00 < arb(39069) / 100 and arb(15871) / 10000 < cUlo < arb(15872) / 10000)
K_lo = arb(K00.lower())
cU_lo = arb(cUlo.lower())
OFF12, OFF13, D22, OFF23 = Fr(347, 10)**2, Fr(25), Fr(40), Fr(9)


def w2min(mu, m2, mg, bL):
    """least w2 allowed by the 2x2 principal minors (and w2 >= 1) of G(mu), minimized over w1 (exact)."""
    Alo = OFF12 / (m2 - mu)
    w1lo = (Alo + D22) / (mg - mu)
    assert Alo > 40 and w1lo >= 2
    return max(Fr(1), OFF13 / ((m2 - mu) * (bL - mu)), OFF23 * w1lo**2 / (Alo * (bL - mu)))


def numer(mu):
    m = A_(mu)
    return 2 * m / 3 * (m / (3 * K_lo)).sqrt()


def Bstar(m2, mg, bL, n=4000):
    """upper bound of sup over mu0 in (0, m2) of numer(mu0) / (c_U sqrt(w2min(mu0))): numer and w2min increase in mu0."""
    best, arg = arb(0), None
    for k in range(n):
        a, b = m2 * Fr(k, n), m2 * Fr(k + 1, n)
        v = numer(b) / (cU_lo * A_(w2min(a, m2, mg, bL)).sqrt())
        if v.upper() > best.upper():
            best, arg = arb(v.upper()), (a, b)
    return best, arg


def float_peak(m2, mg, bL, n=20000):
    vals = []
    for k in range(1, n):
        mu = m2 * Fr(k, n)
        vals.append((float(numer(mu).mid()) / (float(cU_lo.mid()) * math.sqrt(float(w2min(mu, m2, mg, bL)))), float(mu),
                     float(w2min(mu, m2, mg, bL))))
    return max(vals)


# monotonicity spot checks of the two ingredients (the proof is in the review text)
for (m2, mg, bL) in ((Fr(1, 2), Fr(9, 10), Fr(2)), (Fr(61151, 10**5), Fr(99116, 10**5), Fr(4))):
    grid = [m2 * Fr(k, 200) for k in range(0, 200)]
    w = [w2min(mu, m2, mg, bL) for mu in grid]
    check("(D) w2min increases on a 200-point grid of [0, m2) for (m2, m1, beta_L) = (%s, %s, %s)" % (m2, mg, bL),
          all(w[i] <= w[i + 1] for i in range(len(w) - 1)))
# the registered points satisfy the necessary conditions (consistency)
check("(D) sharpw registered point (mu0 97/250, w = (2^15, 2^20)) satisfies w2 >= w2min(97/250)",
      Fr(2**20) >= w2min(Fr(97, 250), Fr(1, 2), Fr(9, 10), Fr(2)))
check("(D) TB-sharp registered point (mu0 297/1000, w = (2^14, 2^18), beta 11/4) satisfies w2 >= w2min(297/1000)",
      Fr(2**18) >= w2min(Fr(297, 1000), Fr(1, 2), Fr(9, 10), Fr(11, 4)))
ROWS = [("T2-R3 scheme, registered floors (M2 1/2, M1 9/10, beta_L 2)", Fr(1, 2), Fr(9, 10), Fr(2), "sharpw",
         "PROVED within the scheme"),
        ("TB-sharp scheme, E0 one component (M2 1/2, M1 9/10, E0 rate 11/4)", Fr(1, 2), Fr(9, 10), Fr(11, 4), "TB-sharp",
         "PROVED within the scheme"),
        ("T2-R3 with state-131 floor ceilings (M2 0.61151, M1 0.99116), beta_L 2", Fr(61151, 10**5), Fr(99116, 10**5),
         Fr(2), "sharpw", "hypothetical floors"),
        ("TB-sharp with state-131 floor ceilings, E0 rate 11/4", Fr(61151, 10**5), Fr(99116, 10**5), Fr(11, 4),
         "TB-sharp", "hypothetical floors"),
        ("T2-R3 with state-131 floor ceilings, beta_L 4", Fr(61151, 10**5), Fr(99116, 10**5), Fr(4), "sharpw",
         "hypothetical floors")]
OUT["D"] = {"K00_lower": K_lo.str(15), "cU_lower": cU_lo.str(15), "rows": []}
print("Proposition WU: weight-uniform L2 budgets (upper bounds, Arb cover of mu0 with 4000 cells)")
for lab, m2, mg, bL, reg, status in ROWS:
    bs, arg = Bstar(m2, mg, bL)
    pk = float_peak(m2, mg, bL)
    regb = arb(FC[reg]["b_fam"])
    gain = bs / regb
    fac = A_(D007) / bs
    check("(D) %s: B* >= FLOAT peak (cover is an upper bound of the sampled values)" % lab, float(bs.upper()) >= pk[0])
    check("(D) %s: B* < 0.004769166867 / 300 (007 excluded from every ball of the scheme, any weights)" % lab,
          fac > 300)
    row = {"label": lab, "status": status, "m2": str(m2), "m1": str(mg), "beta": str(bL),
           "Bstar_upper": fmt(up(bs, 5), 5), "float_peak": "%.5e at mu0 %.4f, w2min %.4g" % pk,
           "gain_over_registered_upper": fmt(up(gain, 4), 4), "registered": reg,
           "factor_007_lower": fmt(lo(fac, 4), 4), "argmax_cell": [str(arg[0]), str(arg[1])]}
    OUT["D"]["rows"].append(row)
    print("  %s [%s]: B* <= %s (FLOAT peak %s); over the registered %s ceiling <= %s; 007 distance / B* >= %s"
          % (lab, status, row["Bstar_upper"], row["float_peak"], reg, row["gain_over_registered_upper"],
             row["factor_007_lower"]))
r0, r1 = OUT["D"]["rows"][0], OUT["D"]["rows"][1]
check("(D) registered floors: every T2-R3 ball (any weights) has L2 budget < 6.8e-6 and every E0 TB-sharp ball < 8.2e-6",
      Fr(r0["Bstar_upper"]) < Fr(68, 10**7) and Fr(r1["Bstar_upper"]) < Fr(82, 10**7))
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N[0], FAILS, round(time.time() - t_start, 3)
(HERE / "data/h18_item2_check_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
