"""Falsification checks of c1-t1 THEORY_FINAL draft 36 section 0 and of the endpoint conclusion of c1-coord
NOTES_FOR_TEAM 12:30Z part 2 (c1-coord 12:30Z item 8). Review: reviews/FALSIFY_ENDPOINT_AND_SECTION0.md.

Run from artifacts/:  python3 -B -u arith/falsify_section0.py
Takes no arguments. Needs python-flint (arb). Reads (read only, hash-bound): the lane copy
../scratch/falsify/THEORY_FINAL_d36.md of c1-t1/THEORY_FINAL.md draft 36, c1-shared theory_v03 and theory_v04 (the
registered L^2 radii), c1-t4's T4-414 and T4-425 directories (PROOFs, parameters, endpoint data), c1-t4 and c1-n4
VERIFY_REPORT.md, c1-t1 REVIEWS_v35.md, and this lane's data/t4_375_review_results.json (Phi(theta*), |U_lead(0)|).
No other lane's code is imported or executed.
Parts:
  (A) inputs and the quoted statements, asserted verbatim in the frozen draft.
  (B) Arb: for every registered L^2 radius (fixed balls and family ceilings of theory_v03 NC-T-DIST and theory_v04
      T4-262), the crude cutoff Ecrit of T4-380 (3) and the retained-shape threshold (3) of T4-414, against
      Etest = (-q - 1)/(2(-q)(-q - 3)) (T4-381) and the current universal constant 1747261/10^6 (T4-411, T4-425).
  (C) Arb: the obstruction of T4-425 at every registered radius: its crude argument with the floor Etest, the same
      argument with the floor 1747261/10^6, and a retained-shape bound on the reach of the whole T4-425 class.
  (D) Arb: the cap of the T4-351 test with T4-351's constants (E > 133, H > 33917; the 9.28e-11) and with the current
      ones (E = 1747261/10^6, H >= H0 of T4-380).
  (E) exact: quoted numbers of section 0 traced to the cited ledger sections, and the stated factors recomputed with
      Fractions and rounded down.
Output: logs/falsify_section0.log, data/falsify_section0_results.json.
"""
import hashlib
import json
import math
import re
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: falsify_section0.py (no arguments)")
t_start = time.time()
ctx.prec = 512
HERE = Path(__file__).resolve().parents[1]
LANE = HERE.parent
R6 = LANE.parent
OUT = {}
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
PI = arb.pi()
A_ = lambda fr_: arb(fr_.numerator) / fr_.denominator


def directed(xv, up, sig=7):
    """Decimal string with sig significant digits, >= every point of the ball if up, else <= (exact endpoints)."""
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
    s_ = ("%." + str(pl) + "f") % out
    return s_ if abs(out) >= Fr(1, 10**4) else ("%.*e" % (sig - 1, float(out)) if False else s_)


def sci(xv, up, sig=5):
    """Scientific display, outward: >= the ball if up, else <=."""
    m_, e_ = (xv.upper() if up else xv.lower()).man_exp()
    v_ = Fr(int(m_)) * Fr(2)**int(e_)
    ex = math.floor(math.log10(abs(float(v_))))
    sc = Fr(10)**(sig - 1 - ex)
    n_ = math.ceil(v_ * sc) if up else math.floor(v_ * sc)
    assert (Fr(n_) / sc >= v_) if up else (Fr(n_) / sc <= v_)
    ds = str(abs(n_))
    if len(ds) > sig:                      # carry, e.g. 9.9999 -> 10.000
        ex += 1
        ds = ds[:sig]
    return ("-" if n_ < 0 else "") + ds[0] + "." + ds[1:] + "e" + ("%d" % ex)


def parse(sv):
    m_, r_ = sv.strip().strip("[]").split("+/-")
    return arb(m_.strip(), r_.strip())


def close(x_, y_, rel=40):
    return bool(abs(x_ - y_) < arb(10)**-rel * (1 + abs(y_)))


checks = {}


def check(name, ok):
    checks[name] = bool(ok)
    if not ok:
        print("CHECK FAILED:", name)


# ---------------------------------------------------------------- (A) inputs and quoted statements
TF = LANE / "scratch/falsify/THEORY_FINAL_d36.md"
H_TF = "455d18effe678743099f1ac7b1d530d7875803afbba574c6ea140a63081b0186"
assert sha(TF) == H_TF
tf = TF.read_text()
tfj = re.sub(r"\s+", " ", tf)                       # joined text (line breaks removed)
sec0 = tfj[tfj.index("## 0. Direct answer"):tfj.index("PROMPT.md section 15 questions")]
T4 = R6 / "c1-t4"
P414 = T4 / "research/profile_velocity_shape_cap"
P425 = T4 / "research/radial_averaged_remainder_obstruction"
V03 = R6 / "c1-shared/theory_requirements/theory_v03.md"
V04 = R6 / "c1-shared/theory_requirements/theory_v04.md"
VR4 = T4 / "VERIFY_REPORT.md"
VRN = R6 / "c1-n4/VERIFY_REPORT.md"
REV35 = R6 / "c1-t1/nonlinear_closure/REVIEWS_v35.md"
R375 = HERE / "data/t4_375_review_results.json"
inputs = {"THEORY_FINAL_d36 (lane copy)": H_TF}
for p in (V03, V04, P414 / "PROOF.md", P414 / "data/parameters.json", P425 / "PROOF.md", P425 / "data/parameters.json",
          VR4, VRN, REV35, R375):
    inputs[str(p.relative_to(R6))] = sha(p)
for n in ("007", "013", "014"):
    inputs[str((P414 / f"data/{n}_endpoint.json").relative_to(R6))] = sha(P414 / f"data/{n}_endpoint.json")
assert inputs["c1-t4/research/radial_averaged_remainder_obstruction/PROOF.md"] == \
    "4d13c623b32b738f78fe7963b67fe4548b5617f24b839be5dc2fe35383155bf3"
assert inputs["c1-t4/research/profile_velocity_shape_cap/PROOF.md"] == \
    "0e0f608d167b2c3453568d06ccc4ba8319e67e5c2d066e4c4ee6854c8fb3a66b"
OUT["inputs"] = inputs
QUOTES = {
    "Q1 universal constant": "Reaching the fixed sharpw radius 1351/1024000000 would need E < 0.785064, so the T4-351 "
                             "inequality with a universal velocity constant reaches no registered radius for 007, 013 or 014",
    "Q2 9.28e-11": "can certify no L^2 distance above 9.28e-11 with the current constants, far below every family ceiling",
    "Q3 two-weight": "no radius-dependent use spliced with any universal constant (T4-425, AUDITED: c1-t1 R1-045, accepted "
                     "in T4-432) and no use of its outer amplitude alone (R1-044, CONFIRMED by T4-426) makes the test "
                     "integrand positive below r_beta, for any profile coefficient >= 0",
    "Q4 blocked": "The endpoint route is therefore blocked with the present inputs.",
    "Q5 2.74 H": "it exceeds 2.74 H at every radius up to 18860, above every room and above 1.747261",
    "Q6 matrix version": "the closure matrix (v101) records RULED OUT",
}
for k, q_ in QUOTES.items():
    check("(A) quoted in section 0: " + k, q_ in sec0)
check("(A) NC-T-UNIV-E row of the necessary-condition table",
      "| NC-T-UNIV-E | no universal velocity constant lets the T4-351 test reach a registered radius | AUDITED |" in tf)
check("(A) section 3.4 names the four targets",
      "this is below 0.785064 for the fixed sharpw radius 1351/1024000000" in tfj and
      "at most 0.6819391, 0.6471910 and 0.2694314 at the sharpw, TB-sharp and graded ceilings" in tfj)
p425 = re.sub(r"\s+", " ", (P425 / "PROOF.md").read_text())
check("(A) T4-425 section 4 is stated for the four registered CI targets",
      "## 4. Consequence for all four registered CI targets" in p425 and "for all twelve reference-target pairs" in p425)
v03 = re.sub(r"\s+", " ", V03.read_text())
v04 = V04.read_text()
REG_TEXT = ["Budgets b_fam (rounded up): baseline FW-A2-Db 6.8626e-8, FW-T-TB-rebal-v1 3.5125e-7, FW-T-TB-sharp-v1 "
            "3.7930e-6, FW-T-T4L2-sharp-v1 3.0927e-6, FW-T-T4L2-sharpw-v1 2.8496e-6, FW-T-T4L2-bL-v1 at beta_L = 7/5 "
            "2.5362e-6 and at beta_L = 1 1.9568e-6",
            "For the fixed-radius instances of FW-T-T4L2-trans-v1 and FW-T-T4L2-statL-v1 the budget is R/sqrt(w2): "
            "2^-23 = 1.1921e-7 and 21/(512 * 10^5) = 4.1016e-7"]
for i, t_ in enumerate(REG_TEXT):
    check("(A) theory_v03 registered radii, text %d" % (i + 1), t_ in v03)
check("(A) theory_v04 T4-262 fixed balls",
      "| FW-A2-Db | N_s(h) <= 2^-16 | 2^-25 = 2.98023e-8 | 6.8626e-8 |" in v04 and
      "| FW-T-T4L2-sharp-v1 | X(h) <= 147/200000 | 147/102400000 = 1.435546875e-6 | 3.0927e-6 |" in v04 and
      "| FW-T-T4L2-sharpw-v1 | X(h) <= 1351/10^6 | 1351/1024000000 = 1.3193359375e-6 | 2.8496e-6 |" in v04)
check("(A) theory_v04 graded ceiling bound", "50/(651 sqrt(28248)) < 25/54684 < 4.5717212e-4" in re.sub(r"\s+", " ", v04))
check("(A) closure matrix rows 56 and 57 list these frameworks for 007",
      "| 56 | FW-T-T4L2-v1, FW-T-T4L2-sharp-v1, FW-T-T4L2-sharpw-v1, FW-T-T4L2-trans-v1 (T4-051) | C1-N1-007" in
      (R6 / "c1-shared/closure_matrix.md").read_text() and
      "| 57 | FW-A2-Db, FW-T-TB-rebal-v1, FW-T-TB-sharp-v1, FW-T-TB-graded-v1 | C1-N1-007" in
      (R6 / "c1-shared/closure_matrix.md").read_text())
OUT["closure_matrix_sha256_at_run"] = sha(R6 / "c1-shared/closure_matrix.md")

# Registered L^2 radii: (label, lower end, upper end of the exact value). Ceilings are printed rounded up
# (theory_v03), so the exact value lies in (printed - one unit, printed]. The graded ceiling is the bound
# 50/(651 sqrt(28248)) < 25/54684 of theory_v04; the T4-425 target is 25/54684 itself.
u = lambda s_: (Fr(s_) - Fr(1, 10**(len(s_.split("e")[0].split(".")[1]) - int(s_.split("e")[1]))), Fr(s_))
REG = [("FW-A2-Db fixed ball (2^-25)", Fr(1, 2**25), Fr(1, 2**25)),
       ("FW-A2-Db family ceiling (6.8626e-8)",) + u("6.8626e-8"),
       ("FW-T-T4L2-trans-v1 fixed ball (2^-23)", Fr(1, 2**23), Fr(1, 2**23)),
       ("FW-T-TB-rebal-v1 family ceiling (3.5125e-7)",) + u("3.5125e-7"),
       ("FW-T-T4L2-statL-v1 fixed ball (21/(512*10^5))", Fr(21, 512 * 10**5), Fr(21, 512 * 10**5)),
       ("FW-T-T4L2-sharpw-v1 fixed ball (1351/1024000000)", Fr(1351, 1024000000), Fr(1351, 1024000000)),
       ("FW-T-T4L2-sharp-v1 fixed ball (147/102400000)", Fr(147, 102400000), Fr(147, 102400000)),
       ("FW-T-T4L2-bL-v1 family ceiling, beta_L = 1 (1.9568e-6)",) + u("1.9568e-6"),
       ("FW-T-T4L2-bL-v1 family ceiling, beta_L = 7/5 (2.5362e-6)",) + u("2.5362e-6"),
       ("FW-T-T4L2-sharpw-v1 family ceiling (2.8496e-6)",) + u("2.8496e-6"),
       ("FW-T-T4L2-sharp-v1 family ceiling (3.0927e-6)",) + u("3.0927e-6"),
       ("FW-T-TB-sharp-v1 family ceiling (3.7930e-6)",) + u("3.7930e-6"),
       ("graded boxes, ceiling (25/54684)", Fr(45697, 10**8), Fr(25, 54684))]
for lab_, lo_, hi_ in REG:
    assert 0 < lo_ <= hi_
assert u("6.8626e-8") == (Fr(68625, 10**12), Fr(68626, 10**12))
assert Fr(45697, 10**8)**2 * 651**2 * 28248 < 2500     # 45697/10^8 < 50/(651 sqrt 28248)

# ---------------------------------------------------------------- constants
PAR414 = json.loads((P414 / "data/parameters.json").read_text())
PAR425 = json.loads((P425 / "data/parameters.json").read_text())
cF = Fr(4076476460239181, 2**51)
assert Fr(PAR414["c"]) == cF and Fr(PAR425["c"]) == cF
qF = 1 / cF - 4
dF = 1 - 1 / cF
DF = 5 * cF - 1
aF = -2 * qF - 2
kF = 4 + dF                                            # kappa = 1 - q
SF = 2 * dF**2 / (aF * (aF + dF) * (aF + 2 * dF))
EminF = (-qF - 1) / (2 * (-qF) * (-qF - 3))
EupF = Fr(PAR425["current_universal"])
assert EupF == Fr(1747261, 10**6) and kF == 1 - qF and DF == cF * kF
cA, qA, dA, DA, aA, kA, SA, Emin, Eup = (A_(v_) for v_ in (cF, qF, dF, DF, aF, kF, SF, EminF, EupF))
lam = arb(1) / 2 + 5 * arb(2)**(1 - qA)                # lambda of T4-425 section 2
s2p = (2 * PI).sqrt()
expo = dA / (-qA - 1)
check("(B) Etest digits 0.793036506422514088", Emin.str(25).startswith("[0.79303650642251408"))
check("(C) lambda > Emin (T4-425)", lam > Emin)


def env_s(Eu):
    """Crossing radius of the envelope min(Eu, lambda (5/s)^delta)."""
    return 5 * (lam / Eu)**(1 / dA)


def T_env(Eu, r):
    """T[min(Eu, lambda (5/s)^delta)](r), formula (5) of T4-425 with Emin replaced by Eu."""
    su = env_s(Eu)
    if r <= su:
        return Eu * (1 - dA / (kA + dA) * (r / su)**kA)
    assert r >= su
    return lam * (5 / r)**dA * kA / (kA + dA)


ru = env_s(Emin)
check("(C) ru = 302748.40... (T4-425)", ru.str(10).startswith("[302748.40"))
check("(C) T[e_min](18860) > 0.79303 (T4-425 (7))", T_env(Emin, arb(18860)) > A_(Fr(79303, 100000)))
check("(E) lambda (5/18860)^delta > 2.74 (the '2.74 H up to 18860')", lam * (arb(5) / 18860)**dA > A_(Fr(274, 100)))
OUT["constants"] = {"Etest": Emin.str(30), "lambda": lam.str(20), "ru": ru.str(20),
                    "s(1747261/10^6)": env_s(Eup).str(20), "T[e_min](18860)": T_env(Emin, arb(18860)).str(20),
                    "lambda (5/18860)^delta": (lam * (arb(5) / 18860)**dA).str(20)}

# ---------------------------------------------------------------- candidate data
D375 = json.loads(R375.read_text())
CAND = {}
for n in ("007", "013", "014"):
    ep = json.loads((P414 / f"data/{n}_endpoint.json").read_text())
    ep5 = json.loads((P425 / f"data/{n}_endpoint.json").read_text())
    check(f"(A) {n}: T4-414 and T4-425 endpoint data equal", ep["F12"] == ep5["F12"] and ep["P"] == ep5["P"]
          and ep["Theta0"] == ep5["Theta0"])
    A = {int(k_): Fr(v_) for k_, v_ in ep["F12"].items()}
    P = {int(k_): Fr(v_) for k_, v_ in ep["P"].items()}
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    ns = sorted(set(A) | set(P))
    Saa = sum(A.get(m, Fr(0))**2 for m in ns)
    Sap = sum(A.get(m, Fr(0)) * P.get(m, Fr(0)) for m in ns)
    Spp = sum(P.get(m, Fr(0))**2 for m in ns)
    Bv = (PI * A_(Saa - Sap**2 / Spp)).sqrt() / (4 * cA)
    g0v = A_(sum(m * v_ for m, v_ in th0.items()))
    Phi = parse(D375["D"][n]["Phi_theta_star"])
    check(f"(A) {n}: theta* of REVIEW_T4_375 equals the T4-425 angle", D375["D"][n]["theta_star"] == PAR425["angles"][n])
    H0 = arb(PAR414["H0"][n])
    assert PAR425["H0"][n] == PAR414["H0"][n]
    check(f"(A) {n}: H0 integer < Phi", H0 < Phi)
    v0 = parse(D375["E"][n]["V_low"])
    CAND[n] = dict(B=Bv, g0=g0v, Phi=Phi, H0=H0, v0=v0)


def crit(c_, beta, H, v, shape):
    """Largest E for which the delta-only majorant can reach beta: (3) of T4-414 (shape) or T4-380 (3) (crude)."""
    f_ = SA.sqrt() if shape else 1 / aA.sqrt()
    return DA * c_["B"] / (s2p * H) * (c_["B"] * f_ / A_(beta))**expo / c_["g0"] - v / c_["g0"]


def caps(c_, E, H, v):
    """Retained-shape cap (8) and crude cap (7) of T4-381 for a constant coefficient E."""
    r0 = (s2p * H * (v + E * c_["g0"]) / (DA * c_["B"]))**(1 / dA)
    return c_["B"] * r0**(qA + 1) * SA.sqrt(), c_["B"] * r0**(qA + 1) / aA.sqrt()


def r_beta(c_, beta):
    return (c_["B"] / (A_(beta) * aA.sqrt()))**(1 / (-qA - 1))


# consistency with T4-414 and T4-380: the four targets
for n, c_ in CAND.items():
    for key, b_ in PAR414["betas"].items():
        check(f"(B) {n} {key}: shape threshold (H0, V = 0) < Ecrit_upper of T4-414",
              crit(c_, Fr(b_), c_["H0"], arb(0), True) < A_(Fr(PAR414["Ecrit_upper"][key])))
        check(f"(B) {n} {key}: crude Ecrit (H0, V = 0) < 0.785064",
              crit(c_, Fr(b_), c_["H0"], arb(0), False) < A_(Fr(785064, 10**6)))
        Kc = DA * c_["B"] * r_beta(c_, Fr(b_))**dA / (s2p * c_["g0"])
        check(f"(C) {n} {key}: Kcrit/Phi equals the crude Ecrit with H = Phi",
              close(Kc / c_["Phi"], crit(c_, Fr(b_), c_["Phi"], arb(0), False), 15))

# ---------------------------------------------------------------- (B) universal-constant test at every registered radius
capE = {n: caps(c_, Emin, c_["H0"], arb(0)) for n, c_ in CAND.items()}
capEPhi = {n: caps(c_, Emin, c_["Phi"], arb(0)) for n, c_ in CAND.items()}
OUT["B"] = {"caps_at_Etest_H0_V0": {n: {"shape_upper": sci(v_[0], True, 7), "crude_upper": sci(v_[1], True, 7),
                                        "shape_lower": sci(v_[0], False, 7), "crude_lower": sci(v_[1], False, 7)}
                                    for n, v_ in capE.items()},
            "caps_at_Etest_Phi_V0_lower": {n: {"shape": sci(v_[0], False, 7), "crude": sci(v_[1], False, 7)}
                                           for n, v_ in capEPhi.items()},
            "radii": {}}
print("(B) Etest = %s; caps of the T4-351 test at E = Etest, V = 0, H0 integer (007 / 013 / 014):" % Emin.str(20))
print("    retained shape in [%s] ; crude in [%s]" % (
    " / ".join("%s, %s" % (sci(capE[n][0], False, 7), sci(capE[n][0], True, 7)) for n in CAND),
    " / ".join("%s, %s" % (sci(capE[n][1], False, 7), sci(capE[n][1], True, 7)) for n in CAND)))
CLS = {1: "fails for every valid universal E, V = 0", 2: "fails for every valid universal E only with V >= v0",
       3: "NOT EXCLUDED by Etest, even with V >= v0"}
for lab_, lo_, hi_ in REG:
    row = {"beta_lower": str(lo_), "beta_upper": str(hi_), "per_candidate": {}}
    cls_all, crude_all, cur_all = [], True, True
    for n, c_ in CAND.items():
        sh_H0 = crit(c_, lo_, c_["H0"], arb(0), True)          # threshold (3) of T4-414 as stated: H0 integer, V = 0
        sh_P = crit(c_, lo_, c_["Phi"], arb(0), True)          # H >= Phi, V = 0
        sh_Pv = crit(c_, lo_, c_["Phi"], c_["v0"], True)       # H >= Phi, V >= v0 (strictest)
        sh_Pv_hi = crit(c_, hi_, c_["Phi"], c_["v0"], True)    # at the largest point of the exact-radius interval
        sh_P_hi = crit(c_, hi_, c_["Phi"], arb(0), True)
        cr_P = crit(c_, lo_, c_["Phi"], arb(0), False)         # crude cutoff of T4-380 (3), H >= Phi, V = 0
        cr_H0 = crit(c_, lo_, c_["H0"], arb(0), False)
        if sh_P < Emin:
            cls = 1
        elif sh_Pv < Emin:
            assert sh_P_hi > Emin
            cls = 2
        else:
            assert sh_Pv_hi > Emin
            cls = 3
        crude_suff = bool(cr_P < Emin)
        cur_fail = bool(cr_H0 < Eup)
        row["per_candidate"][n] = {"shape_H0_V0_upper": directed(sh_H0, True), "shape_Phi_V0_upper": directed(sh_P, True),
                                   "shape_Phi_V0_lower_at_beta_upper": directed(sh_P_hi, False),
                                   "shape_Phi_Vv0_upper": directed(sh_Pv, True),
                                   "shape_Phi_Vv0_lower_at_beta_upper": directed(sh_Pv_hi, False),
                                   "crude_Phi_V0_upper": directed(cr_P, True), "crude_H0_V0_upper": directed(cr_H0, True),
                                   "class": cls, "class_text": CLS[cls], "crude_T4-380_condition_suffices": crude_suff,
                                   "E_1747261_fails_crude_H0_V0": cur_fail}
        cls_all.append(cls)
        crude_all &= crude_suff
        cur_all &= cur_fail
    assert len(set(cls_all)) == 1, lab_
    row.update({"class": cls_all[0], "class_text": CLS[cls_all[0]], "crude_T4-380_condition_suffices": crude_all,
                "E_1747261_fails": cur_all})
    OUT["B"]["radii"][lab_] = row
    pc = row["per_candidate"]
    j_ = lambda k: " / ".join(pc[n][k] for n in CAND)
    print("(B) %s\n    (3) H0, V=0 <= %s ; (3) Phi, V=0 <= %s ; (3) Phi, V>=v0 in [%s ; %s] ; crude Phi, V=0 <= %s\n"
          "    -> %s%s ; 1747261/10^6 fails: %s" % (
              lab_, j_("shape_H0_V0_upper"), j_("shape_Phi_V0_upper"), j_("shape_Phi_Vv0_lower_at_beta_upper"),
              j_("shape_Phi_Vv0_upper"), j_("crude_Phi_V0_upper"), CLS[cls_all[0]],
              " (crude T4-380 condition suffices)" if crude_all else
              (" (needs the retained shape; the crude T4-380 condition does not suffice)" if cls_all[0] < 3 else ""),
              cur_all))
check("(B) every registered radius fails for E = 1747261/10^6", all(r_["E_1747261_fails"] for r_ in OUT["B"]["radii"].values()))
for k_ in (1, 2, 3):
    OUT["B"]["class_%d" % k_] = [k for k, r_ in OUT["B"]["radii"].items() if r_["class"] == k_]
OUT["B"]["needs_retained_shape"] = [k for k, r_ in OUT["B"]["radii"].items()
                                    if r_["class"] < 3 and not r_["crude_T4-380_condition_suffices"]]

# ---------------------------------------------------------------- (C) T4-425 at every registered radius
OUT["C"] = {"radii": {}}
GRID = [Fr(k_ * 1000) for k_ in range(10, 300, 2)]           # Rmax from 10^4 to 2.98 * 10^5 (< ru)
assert all(A_(g_) < ru for g_ in GRID)
reach = {}
for n, c_ in CAND.items():
    best = None
    for g_ in GRID:
        E1 = T_env(Emin, A_(g_))
        sh, _ = caps(c_, E1, c_["H0"], arb(0))
        tail = c_["B"]**2 * A_(g_)**(2 * qA + 2) / aA
        val = (sh**2 + tail).sqrt()
        if best is None or val.upper() < best[0].upper():
            best = (val, g_)
    reach[n] = best
    print("(C) %s: reach of the T4-425 class with floor Etest (retained shape, H0, V = 0) <= %s (Rmax = %s); "
          "lower end with the constant Etest and H = Phi >= %s" % (n, sci(best[0], True, 6), best[1],
                                                                    sci(capEPhi[n][0], False, 6)))
OUT["C"]["reach_upper"] = {n: {"value": sci(v_[0], True, 6), "Rmax": str(v_[1])} for n, v_ in reach.items()}


def reach_bound(c_, Eu, H, v, grid):
    """min over Rmax of sqrt(capS(T[e](Rmax))^2 + B^2 Rmax^(2q+2)/alpha), e = min(Eu, lambda (5/s)^delta)."""
    best = None
    for g_ in grid:
        sh, _ = caps(c_, T_env(Eu, A_(g_)), H, v)
        val = (sh**2 + c_["B"]**2 * A_(g_)**(2 * qA + 2) / aA).sqrt()
        if best is None or val.upper() < best[0].upper():
            best = (val, g_)
    return best


GRID2 = [Fr(k_ * 1000) for k_ in range(20, 400, 2)]
OUT["C"]["reach_upper_Etest_Phi_v0"] = {}
OUT["C"]["reach_upper_1747261_H0_V0"] = {}
reach_v, reach_cur = {}, {}
for n, c_ in CAND.items():
    reach_v[n] = reach_bound(c_, Emin, c_["Phi"], c_["v0"], GRID)
    reach_cur[n] = reach_bound(c_, Eup, c_["H0"], arb(0), GRID2)
    OUT["C"]["reach_upper_Etest_Phi_v0"][n] = {"value": sci(reach_v[n][0], True, 6), "Rmax": str(reach_v[n][1])}
    OUT["C"]["reach_upper_1747261_H0_V0"][n] = {"value": sci(reach_cur[n][0], True, 6), "Rmax": str(reach_cur[n][1])}
    print("(C) %s: reach with floor Etest, H >= Phi, V >= v0 <= %s (Rmax = %s); with floor 1747261/10^6, H0, V = 0 "
          "<= %s (Rmax = %s)" % (n, sci(reach_v[n][0], True, 6), reach_v[n][1], sci(reach_cur[n][0], True, 6),
                                 reach_cur[n][1]))
for lab_, lo_, hi_ in REG:
    row = {}
    t425, tcur, tshape, tshv, tcr = True, True, True, True, True
    for n, c_ in CAND.items():
        rb = r_beta(c_, lo_)
        Kc = crit(c_, lo_, c_["Phi"], arb(0), False)          # Kcrit/Phi at the smallest beta of the interval
        a425 = bool(rb < ru) and bool(T_env(Emin, rb) > Kc)
        acur = bool(T_env(Eup, rb) > Kc)
        ash = bool(reach[n][0] < A_(lo_))
        ashv = bool(reach_v[n][0] < A_(lo_))
        acur_r = bool(reach_cur[n][0] < A_(lo_))
        row[n] = {"r_beta_lower_end_beta": directed(rb, True, 7), "Kcrit/Phi_upper": directed(Kc, True),
                  "T[e_min](r_beta)_lower": directed(T_env(Emin, rb), False),
                  "T[e_1747261](r_beta)_lower": directed(T_env(Eup, rb), False),
                  "T4-425_crude_with_Etest": a425, "crude_with_1747261": acur, "retained_shape_class_blocked": ash,
                  "retained_shape_class_blocked_V_v0": ashv, "reach_1747261_blocked": acur_r}
        t425 &= a425
        tcur &= acur
        tshape &= ash
        tshv &= ashv
        tcr &= acur_r
    row.update({"T4-425_argument_applies": t425, "blocked_with_1747261_crude": tcur,
                "blocked_with_1747261": tcur or tcr, "blocked_with_1747261_reach": tcr,
                "class_blocked_retained_shape": tshape, "class_blocked_retained_shape_V_v0": tshv})
    OUT["C"]["radii"][lab_] = row
    print("(C) %s\n    r_beta <= %s ; Kcrit/Phi <= %s ; T[e_1747261](r_beta) >= %s\n    T4-425 (7) argument with "
          "floor Etest: %s ; with floor 1747261/10^6: crude %s, reach bound %s ; class with floor Etest blocked (retained "
          "shape): V = 0 %s, V >= v0 %s" % (lab_, " / ".join(row[n]["r_beta_lower_end_beta"] for n in CAND),
                                             " / ".join(row[n]["Kcrit/Phi_upper"] for n in CAND),
                                             " / ".join(row[n]["T[e_1747261](r_beta)_lower"] for n in CAND),
                                             t425, tcur, tcr, tshape, tshv))
check("(C) T4-425's argument applies at its four targets",
      all(OUT["C"]["radii"][k]["T4-425_argument_applies"] for k in (
          "FW-T-T4L2-sharpw-v1 fixed ball (1351/1024000000)", "FW-T-T4L2-sharpw-v1 family ceiling (2.8496e-6)",
          "FW-T-TB-sharp-v1 family ceiling (3.7930e-6)", "graded boxes, ceiling (25/54684)")))
check("(C) blocked at every registered radius with the floor 1747261/10^6 (crude argument or reach bound)",
      all(r_["blocked_with_1747261"] for r_ in OUT["C"]["radii"].values()))

R38 = {"graded boxes, ceiling (25/54684)": "7.9417", "FW-T-T4L2-sharpw-v1 family ceiling (2.8496e-6)": "20.1006",
       "FW-T-TB-sharp-v1 family ceiling (3.7930e-6)": "19.0764"}
OUT["C"]["R1-038"] = {}
GEXACT = arb(50) / (651 * arb(28248).sqrt())        # the graded ceiling of theory_v04; 25/54684 rounds it up
for lab_, pr in R38.items():
    lo_ = [r_ for r_ in REG if r_[0] == lab_][0][2]  # the printed value (25/54684 for graded)
    em = {n: DA * (c_["B"] / (A_(lo_) * aA.sqrt()))**expo / c_["g0"] for n, c_ in CAND.items()}
    lhs = {n: Emin * s2p * c_["H0"] / c_["B"] for n, c_ in CAND.items()}
    check("(C) R1-038: Emax(%s) below %s for 007, 013 and 014" % (lab_, pr), all(e_ < A_(Fr(pr)) for e_ in em.values()))
    check("(C) R1-038: Etest sqrt(2 pi) H0/B > Emax(%s)" % lab_, all(lhs[n] > em[n] for n in CAND))
    OUT["C"]["R1-038"][lab_] = {n: {"Emax_upper": directed(em[n], True), "Etest_sqrt2pi_H0_over_B_lower":
                                    directed(lhs[n], False)} for n in CAND}
    print("(C) R1-038 at %s: Emax <= %s (stated below %s); Etest sqrt(2 pi) H0/B >= %s" % (
        lab_, " / ".join(directed(em[n], True) for n in CAND), pr, " / ".join(directed(lhs[n], False) for n in CAND)))
emx = {n: DA * (c_["B"] / (GEXACT * aA.sqrt()))**expo / c_["g0"] for n, c_ in CAND.items()}
OUT["C"]["R1-038_exact_graded_ceiling"] = {n: {"Emax_lower": directed(emx[n], False)} for n in CAND}
print("(C) R1-038 at the exact graded ceiling 50/(651 sqrt 28248): Emax >= %s" % " / ".join(
    directed(emx[n], False) for n in CAND))

# ---------------------------------------------------------------- (D) the 9.28e-11 statement
old = dict(B=A_(Fr(85020)), g0=A_(Fr(285227, 10**4)))
sh_old, cr_old = caps(old, A_(Fr(133)), A_(Fr(33917)), arb(0))
check("(D) T4-351 constants (E 133, H 33917, G 28.5227, B 85020): crude cap < 9.28e-11", cr_old < A_(Fr(928, 10**13)))
OUT["D"] = {"T4-351_constants_crude_cap_upper": sci(cr_old, True, 6), "current": {}}
print("(D) T4-351 constants: crude cap <= %s (T4-351: below 9.28e-11)" % sci(cr_old, True, 6))
for n, c_ in CAND.items():
    sh, cr = caps(c_, Eup, c_["H0"], arb(0))
    OUT["D"]["current"][n] = {"crude_cap_upper": sci(cr, True, 6), "crude_cap_lower": sci(cr, False, 6),
                              "shape_cap_upper": sci(sh, True, 6),
                              "crude_over_9.28e-11_lower": directed(cr / A_(Fr(928, 10**13)), False, 4),
                              "2^-25_over_crude_lower": directed(A_(Fr(1, 2**25)) / cr, False, 4),
                              "6.8626e-8_lower_end_over_crude_lower": directed(A_(Fr(68625, 10**12)) / cr, False, 4)}
    check(f"(D) {n}: current crude cap below 2^-25", cr < A_(Fr(1, 2**25)))
    print("(D) %s, E = 1747261/10^6, H = H0, V = 0, G = g0: crude cap in [%s, %s], retained-shape cap <= %s; "
          "crude cap / 9.28e-11 >= %s; 2^-25 / crude cap >= %s" % (
              n, sci(cr, False, 6), sci(cr, True, 6), sci(sh, True, 6), OUT["D"]["current"][n]["crude_over_9.28e-11_lower"],
              OUT["D"]["current"][n]["2^-25_over_crude_lower"]))

# ---------------------------------------------------------------- (E) quoted numbers and factors
vr4 = VR4.read_text()
vrn = VRN.read_text()


def t4sec(i):
    m_ = re.search(r"^## T4-%d:.*?(?=^## T4-|\Z)" % i, vr4, re.M | re.S)
    return re.sub(r"\s+", " ", m_.group(0)) if m_ else ""


def n4sec(i):
    m_ = re.search(r"^## (?:\S+: )?N4-%d[.,].*?(?=^## |\Z)" % i, vrn, re.M | re.S)
    return re.sub(r"\s+", " ", m_.group(0)) if m_ else ""


TRACE = [  # (number as printed in section 0, [(ledger, id, text expected in that section)])
    ("0.022479506978", [("T4", 270, "11239753489/500000000000")]),
    ("0.00199234339", [("T4", 255, "0.00199234339"), ("N4", 204, "0.00199234339")]),
    ("0.00198301351067", [("T4", 280, "0.00198301351067")]),
    ("0.000351804115950603", [("T4", 298, "0.000351804115950603")]),
    ("0.001232449584356253", [("T4", 304, "0.001232449584356253")]),
    ("0.001092633159", [("T4", 310, "0.001092633159")]),
    ("0.001470360924", [("T4", 311, "0.001470360924")]),
    ("0.001068502321536437", [("T4", 320, "0.001068502321536437")]),
    ("0.00167183069831928", [("T4", 331, "0.00167183069831928")]),
    ("0.001655825792", [("T4", 345, "0.001655825792")]),
    ("0.001328016044", [("T4", 349, "0.001328016044")]),
    ("0.001661806967", [("T4", 357, "0.001661806967")]),
    ("0.001855374677442712", [("T4", 363, "0.001855374677442712")]),
    ("0.001864696854799172", [("T4", 392, "0.001864696854799172")]),
    ("0.00135251075726327", [("T4", 408, "0.00135251075726327")]),
    ("0.002634958245163687", [("N4", 338, "0.002634958245163687")]),
    ("0.001556067368832641", [("N4", 344, "0.001556067368832641")]),
    ("0.004769166867", [("N4", 157, "0.004769166867")]),
    ("3596535.57", [("T4", 238, "756.5312630768"), ("T4", 238, "3596535.57")]),
    ("9.28e-11", [("T4", 351, "9.28e-11"), ("T4", 351, "E>133")]),
    ("2.00215", [("T4", 162, "2.00215")]),
    ("215936.9", [("T4", 325, "215936.94")]),
    ("45174", [("T4", 329, "45174")]),
    ("1.747261", [("T4", 411, "1.747261")]),
    ("85017, 85018 and 85016", [("T4", 339, "85017,85018,85016")]),
    ("0.793036506422514088", [("T4", 381, "0.793036506422514088")]),
    ("999745", [("T4", 380, "999745")]),
]
OUT["E"] = {"trace": {}, "factors": {}}
for num, srcs in TRACE:
    found_tf = num in sec0
    res_ = []
    for led, i, txt in srcs:
        s_ = t4sec(i) if led == "T4" else n4sec(i)
        res_.append({"section": "%s-%d" % (led, i), "section_found": bool(s_), "text_found": txt in s_.replace(" ", "")
                     or txt in s_})
    OUT["E"]["trace"][num] = {"in_section_0": found_tf, "sources": res_}
    ok = found_tf and all(r_["text_found"] for r_ in res_)
    print("(E) trace %-24s in section 0: %s ; %s" % (num, found_tf, "; ".join(
        "%s %s" % (r_["section"], "found" if r_["text_found"] else "NOT FOUND") for r_ in res_)))
    OUT["E"]["trace"][num]["ok"] = ok
rv35 = re.sub(r"\s+", " ", REV35.read_text())
OUT["E"]["trace"]["7.9417"] = {"in_section_0": "7.9417" in sec0, "REVIEWS_v35": "below 7.9417" in rv35}
print("(E) trace 7.9417 in section 0: %s ; REVIEWS_v35: %s" % ("7.9417" in sec0, "below 7.9417" in rv35))

G = Fr(25, 54684)
FACT = [  # (quoted text in section 0, numerator, denominator, printed factor)
    ("4.357 times the graded ceiling", Fr("0.00199234339"), G, "4.357"),
    ("more than 2.337 times the graded ceiling", Fr("0.001068502321536437"), G, "2.337"),
    ("3.656 times the graded ceiling", Fr("0.00167183069831928"), G, "3.656"),
    ("more than 3.621 times the graded ceiling", Fr("0.001655825792"), G, "3.621"),
    ("(ratio 2.904; N4-272)", Fr("0.001328016044"), G, "2.904"),
    ("more than 3.634 times the graded ceiling", Fr("0.001661806967"), G, "3.634"),
    ("more than 4.058 times the graded ceiling", Fr("0.001855374677442712"), G, "4.058"),
    ("more than 4.078 times the graded ceiling", Fr("0.001864696854799172"), G, "4.078"),
    ("more than 2.958 times the graded ceiling", Fr("0.00135251075726327"), G, "2.958"),
    ("more than 5.763 times the graded ceiling", Fr("0.002634958245163687"), G, "5.763"),
    ("more than 3.403 times the graded ceiling", Fr("0.001556067368832641"), G, "3.403"),
    ("That is more than 1257 times the largest scalar ceiling", Fr("0.004769166867"), Fr("3.7930e-6"), "1257"),
    ("more than 10.43 times the graded ceiling", Fr("0.004769166867"), G, "10.43"),
    ("NC-T-DIST fails by a factor above 1673", Fr("0.004769166867"), Fr("2.8496e-6"), "1673"),
    ("the stated tolerance is 330.8 times larger", Fr("2.1035e-4"), Fr("6.3578e-7"), "330.8"),
    ("a factor above 3596535.57", Fr("756.5312630768"), Fr("2.1035e-4"), "3596535.57"),
    ("a factor above 3596535.57", Fr("756.53"), Fr("2.1035e-4"), "3596535.57"),
]
for txt, a_, b_, pr in FACT:
    d_ = len(pr.split(".")[1]) if "." in pr else 0
    fl = Fr(math.floor(a_ / b_ * 10**d_), 10**d_)
    valid = Fr(pr) <= a_ / b_                 # a lower-bound factor must not exceed the exact ratio
    ok = (txt in sec0) and valid
    key = "%s [%s / %s]" % (txt, a_, b_)
    OUT["E"]["factors"][key] = {"printed": pr, "floor": ("%." + str(d_) + "f") % fl, "valid_lower_bound": valid,
                                "equals_floor": fl == Fr(pr), "quoted_in_section_0": txt in sec0}
    print("(E) factor %-60s %s / %s: printed %-11s floor %s%s" % (
        txt[:60], a_, b_, pr, ("%." + str(d_) + "f") % fl,
        "" if (ok and fl == Fr(pr)) else ("   (valid lower bound, below the floor)" if ok else "   <-- NOT a lower bound")))
    if a_ != Fr("756.53"):
        check("(E) factor %s is a valid lower bound and quoted" % pr, ok)
check("(E) line 197 states X > 756.53 next to the factor 3596535.57",
      "X_(s,w)(F) > 756.53 against 2.1035e-4, a factor above 3596535.57" in tfj)
check("(E) 1.3193359375e-6 / 2^-25 >= 44.2 and 2.8496e-6 / 6.8626e-8 >= 41.5 (section 4)",
      Fr(1351, 1024000000) * 2**25 >= Fr(442, 10) and Fr("2.8496e-6") / Fr("6.8626e-8") >= Fr(415, 10))
check("(E) 93/250 - 0.3714757 <= 5.25e-4", Fr(93, 250) - Fr("0.3714757") <= Fr("5.25e-4"))
L_ = (A_(Fr("215936.9")) / A_(Fr(1, 1000)))**(1 / (1 + 4 * dA - 1))
check("(E) (C_00/1e-3)^(1/(-q-1)) with q = -1 - 4 delta is near 45174", abs(L_ - 45174) < 1)
OUT["E"]["L_45174"] = L_.str(15)

OUT["checks"] = checks
OUT["elapsed_s"] = round(time.time() - t_start, 2)
allok = all(checks.values())
print("checks: %d, all pass: %s" % (len(checks), allok))
(HERE / "data/falsify_section0_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("elapsed %.1f s" % OUT["elapsed_s"])
assert allok
