"""Independent review of T4-414 (c1-t4 research/profile_velocity_shape_cap/PROOF.md, sha256 asserted below): the
retained radial shape (T4-381 (8)) applied with the profile coefficient E = 583/1000 to 007, 013 and 014
(reviews/REVIEW_T4_414.md).

Run from artifacts/:  python3 -B -u arith/t4_414_review.py
Needs sympy, mpmath, python-flint (fmpq, arb). Reads c1-t4's PROOF, check.py (read, not run), result.json, manifest,
parameters and the three endpoint JSON files (hash-bound, read only; none of c1-t4's code is imported or executed)
and this lane's data/t4_375_review_results.json (Phi(theta*), theta*, V_low = |U_lead(0)|; run arith/t4_375_review.py
first) and data/t4_410_review_results.json (J(R)/H lower bounds; run arith/t4_410_review.py first).
Parts:
  (A) sympy, exact: the shape integral (2) with symbolic alpha, delta > 0; the two forms of S; alpha S < 1; D = 5c - 1;
      (3) solves cap = beta for E (substitution); the cap decreases in E.
  (B) Arb, own code: B, g0, r0, the two caps and the thresholds (3) for E = 583/1000, with V = 0 and V = |U_lead(0)|,
      first with c1-t4's integers H0, then with H >= Phi(theta*) of REVIEW_T4_375; comparison with result.json; every
      inequality the PROOF asserts; cap(E = threshold) = beta by direct substitution; the ratio of the retained-shape
      threshold to the crude-cutoff Ecrit of REVIEW_T4_402. Consequences, also in Arb: the room threshold - Eprof for
      Eprof = 583/1000 (T4-402, AUDITED) and 93/250 (T4-415, OPEN), and J(R)/H of the T4-410 campaign check against
      the threshold. E_lower = (a - 1)/(2a(a - 3)), a = -q, of T4-381 (the least admissible universal coefficient)
      exceeds every crude Ecrit, so a universal coefficient below a remainder radius cannot reach beta either.
  (C) FLOAT: mpmath quadrature of sqrt(I) for the delta-only majorant (007, V = 0), against the cap (8).
Output: logs/t4_414_review.log, data/t4_414_review_results.json.
"""
import hashlib
import json
import math
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import sympy as S
from flint import arb, ctx

HERE = Path(__file__).resolve().parents[1]
R6 = Path("RUN_ROOT")
SRC = R6 / "c1-t4/research/profile_velocity_shape_cap"
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(SRC / "PROOF.md") == "0e0f608d167b2c3453568d06ccc4ba8319e67e5c2d066e4c4ee6854c8fb3a66b"
assert sha(SRC / "verification/result.json") == "e94368caabeca952aa08be744c4df75e840d4d6e73ef9b9f990dfc3b950ffe10"
assert sha(SRC / "code/check.py") == "0f1e835ebd63a9260fe75a9b9852ffdb976e476bfc3382720efdf37e86e9f736"
assert sha(SRC / "data/manifest.json") == "aeac422340c535091f216bd24915ddd88f07b3393723bf4cb3f3cc768b21038e"
MAN = json.loads((SRC / "data/manifest.json").read_text())
assert MAN["proof_sha256"] == sha(SRC / "PROOF.md")
for k_, v_ in MAN["inputs"].items():
    assert sha(SRC / k_) == v_, k_
# the sources are the files reviewed before: T4-381 (REVIEW_T4_381_384) and REVIEW_T4_402 (accepted in T4-413)
assert sha(SRC / "source/original_shape_PROOF.md") == sha(R6 / "c1-t4/research/universal_velocity_lower/PROOF.md") \
    == "ca0e008a1bfb7868fb1242af0a0eeb1897552a574dc27f7b1a9ad36e1a0b30b9"
assert sha(SRC / "source/profile_review.md") == "ffb49200aa1277900c8db4e7749a7a79a193d59ff4c3b0f514c190f22421c9af"
for n_ in ("007", "013", "014"):
    assert sha(SRC / f"data/{n_}_endpoint.json") == sha(R6 / f"c1-t4/research/profile_specific_velocity/data/{n_}_endpoint.json")
RES = json.loads((SRC / "verification/result.json").read_text())
PAR = json.loads((SRC / "data/parameters.json").read_text())
OUT["inputs"] = {"PROOF": sha(SRC / "PROOF.md"), "result": sha(SRC / "verification/result.json"),
                 "check.py": sha(SRC / "code/check.py"), "manifest": sha(SRC / "data/manifest.json"), **MAN["inputs"]}

# =============================== (A) sympy, exact ===============================
al, de, u, r0s, Bs, bt = S.symbols("alpha delta u r0 B beta", positive=True)
OUT["A"] = {}
Iu = S.integrate((1 - u**(-de))**2 * u**(-al - 1), (u, 1, S.oo), conds="none")
Sform = 1 / al - 2 / (al + de) + 1 / (al + 2 * de)
Sprod = 2 * de**2 / (al * (al + de) * (al + 2 * de))
OUT["A"]["int_1^inf (1 - u^-delta)^2 u^(-alpha-1) du = 1/alpha - 2/(alpha+delta) + 1/(alpha+2delta)"] = S.simplify(Iu - Sform) == 0
OUT["A"]["1/alpha - 2/(alpha+delta) + 1/(alpha+2delta) = 2delta^2/(alpha(alpha+delta)(alpha+2delta))"] = S.simplify(Sform - Sprod) == 0
OUT["A"]["(alpha+delta)(alpha+2delta) - 2delta^2 = alpha^2 + 3 alpha delta (so alpha S < 1)"] = \
    S.expand((al + de) * (al + 2 * de) - 2 * de**2 - al**2 - 3 * al * de) == 0
cs = S.symbols("c", positive=True)
qs, ds = 1 / cs - 4, 1 - 1 / cs
OUT["A"]["D = 1 - c(q - delta) = 5c - 1"] = S.simplify(1 - cs * (qs - ds) - (5 * cs - 1)) == 0
OUT["A"]["alpha = -2q - 2 = 6 - 2/c, and 2q + 1 = -alpha - 1"] = S.simplify(-2 * qs - 2 - (6 - 2 / cs)) == 0
# (3): with r0^delta = sqrt(2 pi) H0 (v0 + E g0)/(D B) and cap = B r0^(q+1) sqrt(S) (q + 1 = -alpha/2), the threshold
# E* of (3) gives r0^delta = (B sqrt(S)/beta)^(2 delta/alpha), hence cap = beta
H0s, v0s, g0s, Ds, Ss, Es = S.symbols("H0 v0 g0 D S E", positive=True)
Ecr = Ds * Bs / (S.sqrt(2 * S.pi) * H0s) * (Bs * S.sqrt(Ss) / bt)**(2 * de / al) / g0s - v0s / g0s
r0d = S.sqrt(2 * S.pi) * H0s * (v0s + Ecr * g0s) / (Ds * Bs)
OUT["A"]["(3): r0^delta at E* equals (B sqrt(S)/beta)^(2 delta/alpha)"] = S.simplify(r0d - (Bs * S.sqrt(Ss) / bt)**(2 * de / al)) == 0
capE = Bs * ((S.sqrt(2 * S.pi) * H0s * (v0s + Es * g0s) / (Ds * Bs))**(1 / de))**(-al / 2) * S.sqrt(Ss)
dcap = S.simplify(S.diff(capE, Es) / capE)
OUT["A"]["d log cap/dE = -alpha g0/(2 delta (v0 + E g0)) < 0"] = S.simplify(dcap + al * g0s / (2 * de * (v0s + Es * g0s))) == 0
assert all(OUT["A"].values()), OUT["A"]
print("(A) exact checks:", json.dumps(OUT["A"]))

# =============================== (B) Arb, own code ===============================
ctx.prec = 256
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
    return ("%." + str(max(pl, 0)) + "f") % out if pl >= 0 else ("%d" % out if out.denominator == 1 else str(float(out)))


def parse(sv):
    m_, r_ = sv.strip().strip("[]").split("+/-")
    return arb(m_.strip(), r_.strip())


def close(x_, y_, rel=40):
    return bool(abs(x_ - y_) < arb(10)**-rel * (1 + abs(y_)))


cF = Fr(4076476460239181, 2**51)
assert Fr(PAR["c"]) == cF and Fr(PAR["E"]) == Fr(583, 1000)
qF = 1 / cF - 4
dF = 1 - 1 / cF
DF = 1 - cF * (qF - dF)
aF = -2 * qF - 2
SF = 2 * dF**2 / (aF * (aF + dF) * (aF + 2 * dF))
assert DF == 5 * cF - 1 and SF == 1 / aF - 2 / (aF + dF) + 1 / (aF + 2 * dF)
assert str(SF) == RES["shape_factor_exact"] and str(qF) == RES["q_exact"] and str(dF) == RES["delta_exact"]
cA, qA, dA, DA, aA, SA = (A_(v_) for v_ in (cF, qF, dF, DF, aF, SF))
s2p = (2 * PI).sqrt()
shape_to_crude = (aA * SA).sqrt()
assert close(shape_to_crude, parse(RES["shape_to_crude"]))
expo = dA / (-qA - 1)                                     # delta/(-q-1) in (3)
ratio_shape = shape_to_crude**expo                        # threshold ratio (retained/crude) when v0 = 0
betas = {k_: Fr(v_) for k_, v_ in PAR["betas"].items()}
aqF = -qF
ElowF = (aqF - 1) / (2 * aqF * (aqF - 3))                  # E_lower (Etest) of T4-381, a = -q
Elow = A_(ElowF)
R375 = json.loads((HERE / "data/t4_375_review_results.json").read_text())
R410 = json.loads((HERE / "data/t4_410_review_results.json").read_text())
OUT["deps"] = {"t4_375_review_results_sha256": sha(HERE / "data/t4_375_review_results.json"),
               "t4_410_review_results_sha256": sha(HERE / "data/t4_410_review_results.json")}
lab410 = {"sharpw_rounded_ceiling": "sharpw", "TB_sharp_rounded_ceiling": "TB", "original_graded_ceiling": "graded",
          "fixed_sharpw_ball": "fixed_sharpw_ball"}
EPROF = {"583/1000": Fr(583, 1000), "93/250": Fr(93, 250)}
OUT["B"] = {"shape_to_crude": shape_to_crude.str(30), "threshold_ratio_retained_over_crude_v0_0": ratio_shape.str(30),
           "E_lower": Elow.str(30), "E_lower_lower": directed(Elow, False, 8)}
OUT["C"] = {}


def caps(Bv, Hv, v_, E_, g0v):
    r0 = (s2p * Hv * (v_ + E_ * g0v) / (DA * Bv))**(1 / dA)
    return r0, Bv * r0**(qA + 1) * SA.sqrt(), Bv * r0**(qA + 1) / aA.sqrt()


def crit(Bv, Hv, v_, g0v, beta, shape=True):
    f_ = SA.sqrt() if shape else 1 / aA.sqrt()
    return DA * Bv / (s2p * Hv) * (Bv * f_ / A_(beta))**expo / g0v - v_ / g0v


allok = True
for name in ("007", "013", "014"):
    ep = json.loads((SRC / f"data/{name}_endpoint.json").read_text())
    A = {int(k_): Fr(v_) for k_, v_ in ep["F12"].items()}
    P = {int(k_): Fr(v_) for k_, v_ in ep["P"].items()}
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    ns = sorted(set(A) | set(P))
    Saa = sum(A.get(n, Fr(0))**2 for n in ns)
    Sap = sum(A.get(n, Fr(0)) * P.get(n, Fr(0)) for n in ns)
    Spp = sum(P.get(n, Fr(0))**2 for n in ns)
    Bv = (PI * A_(Saa - Sap**2 / Spp)).sqrt() / (4 * cA)          # ||sin n||^2 = pi on [0, 2pi]
    g0F = sum(n * v_ for n, v_ in th0.items())
    g0v = A_(g0F)
    row = next(r_ for r_ in RES["rows"] if r_["candidate"] == name)
    D375 = R375["D"][name]
    assert D375["theta_star"] == PAR["angles"][name]                 # c1-t4's angle is theta* of REVIEW_T4_375
    Phi = parse(D375["Phi_theta_star"])
    Vlow = parse(R375["E"][name]["V_low"])                           # |U_lead(0)|, own computation in REVIEW_T4_375
    H0 = arb(PAR["H0"][name])
    v0F = Fr(row["v0_exact"])
    chk = {"B": close(Bv, parse(row["B"]), 35), "g0 exact": str(g0F) == row["g0_exact"],
           "H0 integer < Phi(theta*)": bool(H0 < Phi), "Phi equals c1-t4 H_point": close(Phi, parse(row["H_point"]), 14),
           "v0 equals own |U_lead(0)|": close(A_(v0F), Vlow, 14), "g0 > 0, v0 > 0": g0F > 0 and v0F > 0}
    res = {"checks": chk, "B": Bv.str(20), "g0": g0v.str(20), "Phi": Phi.str(20), "v0": A_(v0F).str(20), "versions": {}}
    for vl, v_ in (("V_zero", arb(0)), ("V_lead", A_(v0F))):
        r0, cap, crude = caps(Bv, H0, v_, A_(Fr(583, 1000)), g0v)
        ver = row["versions"][vl]
        vchk = {"radius": close(r0, parse(ver["radius"]), 35), "cap": close(cap, parse(ver["cap"]), 35),
                "crude_cap": close(crude, parse(ver["crude_cap"]), 35),
                "cap < 7643/10^10": bool(cap < A_(Fr(PAR["cap_upper"]))),
                "cap < every beta": all(bool(cap < A_(b_)) for b_ in betas.values())}
        th = {}
        for key, beta in betas.items():
            cr = crit(Bv, H0, v_, g0v, beta)
            cc = crit(Bv, H0, v_, g0v, beta, shape=False)
            crP = crit(Bv, Phi, v_, g0v, beta)                         # with H >= Phi(theta*) (stricter)
            _, capc, _ = caps(Bv, H0, v_, cr, g0v)
            tv = ver["thresholds"][key]
            vchk.update({f"{key}: retained equals result.json": close(cr, parse(tv["retained_shape"]), 35),
                         f"{key}: crude equals result.json": close(cc, parse(tv["crude_cutoff"]), 35),
                         f"{key}: retained < Ecrit_upper < 583/1000": bool(cr < A_(Fr(PAR["Ecrit_upper"][key])) < A_(Fr(583, 1000))),
                         f"{key}: retained < crude": bool(cr < cc),
                         f"{key}: crude Ecrit < E_lower": bool(cc < Elow),
                         f"{key}: cap(E = threshold) = beta": close(capc, A_(beta), 60)})
            if vl == "V_zero":
                vchk[f"{key}: retained/crude = (alpha S)^(delta/(2(-q-1)))"] = close(cr / cc, ratio_shape, 60)
            th[key] = {"retained_upper_H0": directed(cr, True), "crude_upper_H0": directed(cc, True),
                       "retained_upper_Phi": directed(crP, True), "crude_upper_Phi": directed(crit(Bv, Phi, v_, g0v, beta, False), True)}
            for en, ef in EPROF.items():
                th[key][f"room_{en}_upper"] = directed(crP - A_(ef), True)
            if vl == "V_zero":
                J = arb(R410["C"][name][lab410[key]]["J_over_H_lower"])
                th[key]["T4-410 J/H lower"] = R410["C"][name][lab410[key]]["J_over_H_lower"]
                th[key]["J/H over retained threshold, lower"] = directed(J / crP, False)
                assert J > crP
        res["versions"][vl] = {"checks": vchk, "r0_lower": directed(r0, False), "cap_upper": directed(cap, True),
                               "crude_cap_upper": directed(crude, True), "thresholds": th}
        allok = allok and all(vchk.values())
    allok = allok and all(chk.values())
    OUT["B"][name] = res
    for vl in ("V_zero", "V_lead"):
        rv = res["versions"][vl]
        print("(B) %s %s: r0 >= %s; cap (8) <= %s; crude cap (7) <= %s; all checks: %s"
              % (name, vl, rv["r0_lower"], rv["cap_upper"], rv["crude_cap_upper"], all(rv["checks"].values())))
        for key, tv in rv["thresholds"].items():
            print("    %s: threshold (3) <= %s (H0 integer), <= %s (H >= Phi); crude <= %s / %s; room for 583/1000 <= %s,"
                  " for 93/250 <= %s%s" % (key, tv["retained_upper_H0"], tv["retained_upper_Phi"], tv["crude_upper_H0"],
                                           tv["crude_upper_Phi"], tv["room_583/1000_upper"], tv["room_93/250_upper"],
                                           ("; T4-410 J/H >= %s, ratio to threshold >= %s" % (tv["T4-410 J/H lower"],
                                            tv["J/H over retained threshold, lower"])) if "T4-410 J/H lower" in tv else ""))
    print("(B) %s: input checks %s" % (name, json.dumps(chk)))
assert allok
print("(B) shape_to_crude sqrt(alpha S) = %s; threshold ratio retained/crude (v0 = 0) = %s"
      % (shape_to_crude.str(15), ratio_shape.str(15)))
print("(B) E_lower = (a - 1)/(2a(a - 3)) >= %s exceeds every crude Ecrit (H0, both V versions, all targets): asserted"
      % OUT["B"]["E_lower_lower"])

# =============================== (C) FLOAT quadrature of I ===============================
mp.mp.dps = 30
OUT["C"]["FLOAT_quadrature"] = {}
for name in ("007",):
    rv = OUT["B"][name]
    Bf = mp.mpf(parse(rv["B"]).mid().str(25, radius=False))
    g0f = mp.mpf(parse(rv["g0"]).mid().str(25, radius=False))
    Hf = mp.mpf(PAR["H0"][name])
    qf, df, Df = (mp.mpf(x_.numerator) / x_.denominator for x_ in (qF, dF, DF))
    Ef = mp.mpf(583) / 1000
    ehat = lambda r: Hf * Ef * g0f * r**(-df) / Df                     # the delta-only majorant, V = 0
    integrand = lambda r: max(Bf - mp.sqrt(2 * mp.pi) * ehat(r), 0)**2 * r**(2 * qf + 1)
    r0f = (mp.sqrt(2 * mp.pi) * Hf * Ef * g0f / (Df * Bf))**(1 / df)
    Iq = mp.quad(integrand, [r0f, 10 * r0f, 1000 * r0f, mp.inf])
    cap_arb = caps(parse(rv["B"]), arb(PAR["H0"][name]), arb(0), A_(Fr(583, 1000)), parse(rv["g0"]))[1]
    capf = mp.mpf(cap_arb.mid().str(25, radius=False))
    OUT["C"]["FLOAT_quadrature"][name] = {"sqrt_I": float(mp.sqrt(Iq)), "cap": float(capf),
                                          "relative_difference": float(abs(mp.sqrt(Iq) - capf) / capf)}
    print("(C) FLOAT %s: sqrt(I) by quadrature = %.12g, cap (8) = %.12g, relative difference %.2e"
          % (name, mp.sqrt(Iq), capf, abs(mp.sqrt(Iq) - capf) / capf))

OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_414_review_results.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
print("elapsed %.1f s" % OUT["elapsed_s"])
