"""The FW-T-TB-rebal-v1 row of FALSIFY_ENDPOINT_AND_SECTION0 section 1 at the exact radius (handoff BE3, T4-454).
The printed ceiling 3.5125e-7 is below the exact b_fam = 3.51254748...e-7, so the interval (3.5124e-7, 3.5125e-7]
used by arith/falsify_section0.py does not contain it. This script recomputes the row on [3.5125e-7, 3.5126e-7]
(3.5126e-7 is the upward rounding, T4-454) with the same formulas, and at the exact b_fam itself.

Run from artifacts/:  python3 -B -u arith/tbrebal_exact_row.py
Takes no arguments. Needs python-flint (arb). Reads (read only, hash-bound): c1-t4's T4-414 and T4-425 directories
(parameters and endpoint data, the same files as arith/falsify_section0.py), data/t4_375_review_results.json,
data/falsify_section0_results.json and data/family_ceilings_exact_results.json. The functions crit and the candidate
data are copied from arith/falsify_section0.py (sha256 f47ab3e0...811bc388, asserted); nothing is imported from it.
Checks:
  (A) inputs; the old row is reproduced exactly from the copied formulas on (3.5124e-7, 3.5125e-7].
  (B) the row on [3.5125e-7, 3.5126e-7] and at the exact b_fam: class, upper bounds, lower ends; the exact b_fam is
      inside [3.5125e-7, 3.5126e-7].
Output: logs/tbrebal_exact_row.log, data/tbrebal_exact_row_results.json.
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
    sys.exit("usage: tbrebal_exact_row.py (no arguments)")
t_start = time.time()
ctx.prec = 512
HERE = Path(__file__).resolve().parents[1]
LANE = HERE.parent
R6 = LANE.parent
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
PI = arb.pi()
A_ = lambda fr_: arb(fr_.numerator) / fr_.denominator
N, FAILS, OUT = [0], [], {"inputs": {}}


def check(name, ok):
    N[0] += 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def directed(xv, up, sig=7):
    """Copied from arith/falsify_section0.py: sig significant digits, outward (exact endpoints)."""
    m_, e_ = (xv.upper() if up else xv.lower()).man_exp()
    v_ = Fr(int(m_)) * Fr(2)**int(e_)
    if v_ == 0:
        return "0"
    ex = math.floor(math.log10(abs(float(v_))))
    pl = sig - 1 - ex
    n_ = math.ceil(v_ * Fr(10)**pl) if up else math.floor(v_ * Fr(10)**pl)
    out = Fr(n_) / Fr(10)**pl
    assert (out >= v_) if up else (out <= v_)
    if pl < 0:
        return "%d" % out
    return ("%." + str(pl) + "f") % out


def parse(sv):
    m_, r_ = sv.strip().strip("[]").split("+/-")
    return arb(m_.strip(), r_.strip())


FS = HERE / "arith/falsify_section0.py"
check("(A) sha256 of arith/falsify_section0.py (the formulas copied here) is f47ab3e0...811bc388 (README row)",
      sha(FS) == "f47ab3e03e0d5268d0905c036f58499ccefe2fc32c607f07f5583115811bc388")
src = FS.read_text()
for frag in ('def crit(c_, beta, H, v, shape):',
             'f_ = SA.sqrt() if shape else 1 / aA.sqrt()',
             'return DA * c_["B"] / (s2p * H) * (c_["B"] * f_ / A_(beta))**expo / c_["g0"] - v / c_["g0"]',
             'Bv = (PI * A_(Saa - Sap**2 / Spp)).sqrt() / (4 * cA)',
             'g0v = A_(sum(m * v_ for m, v_ in th0.items()))',
             'SF = 2 * dF**2 / (aF * (aF + dF) * (aF + 2 * dF))',
             'EminF = (-qF - 1) / (2 * (-qF) * (-qF - 3))',
             '("FW-T-TB-rebal-v1 family ceiling (3.5125e-7)",) + u("3.5125e-7"),'):
    check("(A) falsify_section0.py contains '%s'" % frag, frag in src)
T4 = R6 / "c1-t4"
P414 = T4 / "research/profile_velocity_shape_cap"
P425 = T4 / "research/radial_averaged_remainder_obstruction"
R375 = HERE / "data/t4_375_review_results.json"
RFS = HERE / "data/falsify_section0_results.json"
RFC = HERE / "data/family_ceilings_exact_results.json"
FSJ = json.loads(RFS.read_text())
for p in [P414 / "data/parameters.json", P425 / "data/parameters.json", R375, RFS, RFC, FS] + \
         [P414 / f"data/{n}_endpoint.json" for n in ("007", "013", "014")] + \
         [P425 / f"data/{n}_endpoint.json" for n in ("007", "013", "014")]:
    OUT["inputs"][str(p.relative_to(R6))] = sha(p)
check("(A) the endpoint and parameter files have the hashes recorded by falsify_section0",
      all(FSJ["inputs"].get(k, v) == v for k, v in OUT["inputs"].items()
          if k.startswith("c1-t4/") or k.endswith("t4_375_review_results.json")))

# constants (copied)
PAR414 = json.loads((P414 / "data/parameters.json").read_text())
PAR425 = json.loads((P425 / "data/parameters.json").read_text())
cF = Fr(4076476460239181, 2**51)
assert Fr(PAR414["c"]) == cF and Fr(PAR425["c"]) == cF
qF = 1 / cF - 4
dF = 1 - 1 / cF
DF = 5 * cF - 1
aF = -2 * qF - 2
SF = 2 * dF**2 / (aF * (aF + dF) * (aF + 2 * dF))
EminF = (-qF - 1) / (2 * (-qF) * (-qF - 3))
cA, qA, dA, DA, aA, SA, Emin = (A_(v_) for v_ in (cF, qF, dF, DF, aF, SF, EminF))
s2p = (2 * PI).sqrt()
expo = dA / (-qA - 1)
D375 = json.loads(R375.read_text())
CAND = {}
for n in ("007", "013", "014"):
    ep = json.loads((P414 / f"data/{n}_endpoint.json").read_text())
    A = {int(k_): Fr(v_) for k_, v_ in ep["F12"].items()}
    P = {int(k_): Fr(v_) for k_, v_ in ep["P"].items()}
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    ns = sorted(set(A) | set(P))
    Saa = sum(A.get(m, Fr(0))**2 for m in ns)
    Sap = sum(A.get(m, Fr(0)) * P.get(m, Fr(0)) for m in ns)
    Spp = sum(P.get(m, Fr(0))**2 for m in ns)
    Bv = (PI * A_(Saa - Sap**2 / Spp)).sqrt() / (4 * cA)
    g0v = A_(sum(m * v_ for m, v_ in th0.items()))
    CAND[n] = dict(B=Bv, g0=g0v, Phi=parse(D375["D"][n]["Phi_theta_star"]), H0=arb(PAR414["H0"][n]),
                   v0=parse(D375["E"][n]["V_low"]))


def crit(c_, beta, H, v, shape):
    f_ = SA.sqrt() if shape else 1 / aA.sqrt()
    return DA * c_["B"] / (s2p * H) * (c_["B"] * f_ / beta)**expo / c_["g0"] - v / c_["g0"]


def row(lo, hi):
    """lo, hi: arb radii; upper bounds at lo, lower ends at hi (thresholds decrease in beta)."""
    out = {}
    for n, c_ in CAND.items():
        sh_P, sh_Pv = crit(c_, lo, c_["Phi"], arb(0), True), crit(c_, lo, c_["Phi"], c_["v0"], True)
        sh_P_hi, sh_Pv_hi = crit(c_, hi, c_["Phi"], arb(0), True), crit(c_, hi, c_["Phi"], c_["v0"], True)
        out[n] = {"shape_H0_V0_upper": directed(crit(c_, lo, c_["H0"], arb(0), True), True),
                  "shape_Phi_V0_upper": directed(sh_P, True),
                  "shape_Phi_V0_lower_at_beta_upper": directed(sh_P_hi, False),
                  "shape_Phi_Vv0_upper": directed(sh_Pv, True),
                  "shape_Phi_Vv0_lower_at_beta_upper": directed(sh_Pv_hi, False),
                  "crude_Phi_V0_upper": directed(crit(c_, lo, c_["Phi"], arb(0), False), True),
                  "crude_H0_V0_upper": directed(crit(c_, lo, c_["H0"], arb(0), False), True),
                  "class_1": bool(sh_P < Emin)}
    return out


KEY = "FW-T-TB-rebal-v1 family ceiling (3.5125e-7)"
OLD = FSJ["B"]["radii"][KEY]
check("(A) the old interval is (3.5124e-7, 3.5125e-7] (falsify_section0 results)",
      (Fr(OLD["beta_lower"]), Fr(OLD["beta_upper"])) == (Fr(35124, 10**11), Fr(35125, 10**11)))
old = row(A_(Fr(35124, 10**11)), A_(Fr(35125, 10**11)))
FIELDS = ["shape_H0_V0_upper", "shape_Phi_V0_upper", "shape_Phi_V0_lower_at_beta_upper", "shape_Phi_Vv0_upper",
          "shape_Phi_Vv0_lower_at_beta_upper", "crude_Phi_V0_upper", "crude_H0_V0_upper"]
check("(A) the copied formulas reproduce every field of the old row exactly (007, 013, 014)",
      all(old[n][f] == OLD["per_candidate"][n][f] for n in CAND for f in FIELDS))
check("(A) the old row has the lower end 0.6372628 (007, V >= v0) and class 1",
      OLD["per_candidate"]["007"]["shape_Phi_Vv0_lower_at_beta_upper"] == "0.6372628" and OLD["class"] == 1)

# ---------------------------------------------------------------- (B)
bx = arb(json.loads(RFC.read_text())["ceilings"]["TB-rebal"]["b_fam"])
LO, HI = Fr(35125, 10**11), Fr(35126, 10**11)
check("(B) 3.5125e-7 < exact b_fam < 3.5126e-7 (Arb)", A_(LO) < bx < A_(HI))
new = row(A_(LO), A_(HI))
at = row(bx, bx)
OUT["old_interval"] = {"beta": ["35124/10^11", "35125/10^11"], "per_candidate": old}
OUT["new_interval"] = {"beta": ["35125/10^11", "35126/10^11"], "per_candidate": new}
OUT["at_exact_b_fam"] = {"b_fam": bx.str(25), "per_candidate": at}
check("(B) class 1 on [3.5125e-7, 3.5126e-7] and at the exact b_fam, for 007, 013 and 014 (upper bound < Etest)",
      all(new[n]["class_1"] and at[n]["class_1"] for n in CAND))
check("(B) the old upper bounds (taken at 3.5124e-7) are >= the new ones (taken at 3.5125e-7)",
      all(Fr(old[n][f]) >= Fr(new[n][f]) for n in CAND for f in FIELDS if f.endswith("upper")))
check("(B) the new lower ends (at 3.5126e-7) are <= the old ones (at 3.5125e-7)",
      all(Fr(new[n][f]) <= Fr(old[n][f]) for n in CAND for f in FIELDS if f.endswith("beta_upper")))
print("TB-rebal row, 007 / 013 / 014:")
for lab, r_ in (("old (3.5124e-7, 3.5125e-7]", old), ("new [3.5125e-7, 3.5126e-7]", new), ("at exact b_fam", at)):
    print("  %s:" % lab)
    for f in FIELDS:
        print("    %s: %s" % (f, " / ".join(r_[n][f] for n in CAND)))
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N[0], FAILS, round(time.time() - t_start, 3)
(HERE / "data/tbrebal_exact_row_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
