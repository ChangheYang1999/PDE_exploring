"""Independent review of T4-402 (c1-t4 research/profile_specific_velocity/PROOF.md, sha256 a98e64b0...6e5ab3d9): the
limiting coefficient of the compensated exterior velocity for a finite odd sine tail, and the bound 583/1000 on the
endpoint subspaces of 007, 013 and 014 (reviews/REVIEW_T4_402.md).

Run from artifacts/:  python3 -B -u arith/t4_402_review.py
Needs sympy, numpy, python-flint (fmpq, arb). Reads c1-t4's PROOF, result.json and the three endpoint JSON files
(hash-bound, read only, none of c1-t4's code is imported or executed) and this lane's data/t4_375_review_results.json
(for Phi(theta*) and V >= |U_lead(0)|; run arith/t4_375_review.py first).
Parts:
  (A) sympy, exact: (9) of the PROOF for every mode n = 1, 3, ..., 21 with symbolic p, by Cartesian differentiation of
      (x^2 + y^2)^((p - n)/2) Im((x + i y)^n) at 2n + 6 rational points of the unit circle (a trigonometric polynomial
      of degree n + 2 in theta that vanishes at 2n + 6 distinct angles is zero); the radial Green tails for n = 1 and
      n = 3 at q = -7/2; the single-mode case b = sin(theta)/a reproduces E_lower of T4-381.
  (B) exact rationals, own code (complex exponential coefficients, not c1-t4's geometry.py): V_A, V_P, S, the cosine
      coefficients of T(theta) and their absolute sum; comparison with result.json; P against Theta0.
  (C) Arb: a rigorous upper bound for max_theta T(theta) (second order Taylor bound on 4096 cells of [0, pi/2]) and
      its square root. FLOAT diagnostics: the per-angle largest eigenvalue form, the constant normalized by the
      pointwise gradient sup (grid in t = m/pi, log spaced; revision 2, the first run used a grid in the angle of
      z = (cos phi, sin phi), which cannot resolve t of order 1e4 to 1e5), and kappa(t) = sup_theta |V_q[b_t]|.
  (D) Arb: the finite-radius question. Kcrit = Ecrit * Phi_lower (independent of Phi), r_beta, the margins
      Ecrit - Eprof, the V term, and the C0 size B0/(sqrt(2 pi) Phi) of the remainder allowed at r_grad.
Output: logs/t4_402_review.log, data/t4_402_review_results.json.
"""
import hashlib
import json
import math
import time
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
import sympy as S
from flint import arb, ctx, fmpq

HERE = Path(__file__).resolve().parents[1]
SRC = Path("RUN_ROOT/theory_audit_T4/research/profile_specific_velocity")
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(SRC / "PROOF.md") == "a98e64b04a4ab8f8e46f311c028d55138e9483f761d84e140ed550066e5ab3d9"
assert sha(SRC / "verification/result.json") == "b8d33a7e9aeb8e2d81ab23b9c73e34b0b6f6dfb7c137e004f5330600a86ebdce"
MAN = json.loads((SRC / "data/manifest.json").read_text())
for k_, v_ in MAN["inputs"].items():
    assert sha(SRC / k_) == v_, k_
RES = json.loads((SRC / "verification/result.json").read_text())
OUT["inputs"] = {"PROOF": sha(SRC / "PROOF.md"), "result": sha(SRC / "verification/result.json"),
                 "manifest": sha(SRC / "data/manifest.json"), **{k_: v_ for k_, v_ in MAN["inputs"].items()}}

# =============================== (A) sympy, exact ===============================
x, y, p = S.symbols("x y p", real=True)
OUT["A"] = {}
okA = True
for n in range(1, 22, 2):
    F = (x**2 + y**2)**((p - n) / 2) * S.im(S.expand((x + S.I * y)**n))
    w1, w2 = S.diff(F, x, y), -S.diff(F, x, 2)
    good = True
    for j in range(2 * n + 6):
        s_ = S.Rational(j, 7)
        xv, yv = (1 - s_**2) / (1 + s_**2), 2 * s_ / (1 + s_**2)
        z = S.expand((xv + S.I * yv)**n)
        zm, zp = S.expand(z * (xv - S.I * yv)**2), S.expand(z * (xv + S.I * yv)**2)  # e^{i(n-2)th}, e^{i(n+2)th}
        cm, sm, cp, sp, sn = S.re(zm), S.im(zm), S.re(zp), S.im(zp), S.im(z)
        a_, c_ = (p + n) * (p + n - 2), (p - n) * (p - n - 2)
        v1 = (a_ * cm - c_ * cp) / 4                                   # (p^2 - n^2) times V1 of (9), b_n = 1
        v2 = -(p**2 - n**2) * sn / 2 - (a_ * sm + c_ * sp) / 4         # (p^2 - n^2) times V2 of (9)
        d1 = S.expand(w1.subs({x: xv, y: yv}) - v1)
        d2 = S.expand(w2.subs({x: xv, y: yv}) - v2)
        good = good and d1 == 0 and d2 == 0
    OUT["A"]["(9) mode %d" % n] = good
    okA = okA and good
# radial Green tails at q = -7/2 for f = s^q on s >= 2 (the inner part only adds C r^-n, and I_inf r^-1 for n = 1)
r, s = S.symbols("r s", positive=True)
q0 = S.Rational(-7, 2)
p0 = q0 + 2
for n in (1, 3):
    outer = r**n * S.integrate(s**(1 - n) * s**q0, (s, r, S.oo))
    inner = r**(-n) * S.integrate(s**(n + 1) * s**q0, (s, 2, r))      # the part of int_0^r from s >= 2
    if n == 1:
        inner = r**(-1) * (-S.integrate(s**2 * s**q0, (s, r, S.oo)))  # int_0^r = I_inf - int_r^inf
    An = -(inner + outer) / (2 * n)
    diff_ = S.simplify(An - r**p0 / (p0**2 - n**2))
    # n = 1: no r^-1 remainder beyond -I_inf/(2r); n = 3: remainder is a multiple of r^-3
    ok_ = diff_ == 0 if n == 1 else S.simplify(diff_ * r**3).free_symbols == set()
    OUT["A"]["Green tail n=%d" % n] = bool(ok_)
    okA = okA and bool(ok_)
# single mode b = sin(theta)/a: max |V| = E_lower = (a - 1)/(2 a (a - 3))
aa, th = S.symbols("a theta", positive=True)
pp = 2 - aa
D1 = 4 * (pp**2 - 1)
V1 = ((pp + 1) * (pp - 1) * S.cos(-th) - (pp - 1) * (pp - 3) * S.cos(3 * th)) / D1 / aa
V2 = -S.sin(th) / 2 / aa - ((pp + 1) * (pp - 1) * S.sin(-th) + (pp - 1) * (pp - 3) * S.sin(3 * th)) / D1 / aa
mod2 = S.simplify(S.expand_trig(V1**2 + V2**2).subs(th, S.pi / 4))
OUT["A"]["E_lower at pi/4"] = S.simplify(S.sqrt(mod2) - (aa - 1) / (2 * aa * (aa - 3))).subs(aa, S.Rational(3447611, 10**6)) == 0
kap = (aa + 1) / (aa - 3)
OUT["A"]["|V|^2 = (1+k^2-2k cos4th)/(4a)^2"] = S.simplify(S.expand_trig(V1**2 + V2**2 - (1 + kap**2 - 2 * kap * S.cos(4 * th)) / (4 * aa)**2)) == 0
okA = okA and OUT["A"]["E_lower at pi/4"] and OUT["A"]["|V|^2 = (1+k^2-2k cos4th)/(4a)^2"]
assert okA, OUT["A"]
print("(A) exact checks:", json.dumps(OUT["A"]))

# =============================== (B) exact rationals, own code ===============================
cF = Fr(4076476460239181, 2**51)
qF = 1 / cF - 4
pF = qF + 2
gam = 1 / cF


def vel(b):
    """b: {n: sin coefficient}. Returns V1, V2 of (9) as maps k -> complex coefficient of e^{ik theta}, (re, im)."""
    v1, v2 = {}, {}

    def put(d, k, z):
        re_, im_ = d.get(k, (Fr(0), Fr(0)))
        d[k] = (re_ + z[0], im_ + z[1])
    for n, bn in b.items():
        Dn = 4 * (pF * pF - n * n)
        a_, c_ = bn * (pF + n) * (pF + n - 2) / Dn, bn * (pF - n) * (pF - n - 2) / Dn
        for k, w in ((n - 2, a_), (-(n - 2), a_), (n + 2, -c_), (-(n + 2), -c_)):   # cos(k th) = (e^{ik} + e^{-ik})/2
            put(v1, k, (w / 2, Fr(0)))
        for k, w in ((n, -bn / 2), (n - 2, -a_), (n + 2, -c_)):                       # sin(k th) = (e^{ik} - e^{-ik})/(2i)
            put(v2, k, (Fr(0), -w / 2))
            put(v2, -k, (Fr(0), w / 2))
    return v1, v2


def mul(f, g):
    out = {}
    for k1, (a1, b1) in f.items():
        for k2, (a2, b2) in g.items():
            re_, im_ = out.get(k1 + k2, (Fr(0), Fr(0)))
            out[k1 + k2] = (re_ + a1 * a2 - b1 * b2, im_ + a1 * b2 + b1 * a2)
    return out


def addto(acc, f, sc):
    for k, (a_, b_) in f.items():
        re_, im_ = acc.get(k, (Fr(0), Fr(0)))
        acc[k] = (re_ + sc * a_, im_ + sc * b_)


OUT["B"] = {}
cand = {}
for name in ("007", "013", "014"):
    ep = json.loads((SRC / f"data/{name}_endpoint.json").read_text())
    A = {int(k_): Fr(v_) for k_, v_ in ep["F12"].items()}
    P = {int(k_): Fr(v_) for k_, v_ in ep["P"].items()}
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    ns = sorted(set(A) | set(P))
    G = lambda f, g: sum((qF * qF + n * n) * f.get(n, Fr(0)) * g.get(n, Fr(0)) for n in ns) / 2
    S11, S12, S22 = G(A, A), G(A, P), G(P, P)
    det = S11 * S22 - S12 * S12
    assert S11 > 0 and S22 > 0 and det > 0
    a1, a2 = vel(A)
    b1, b2 = vel(P)
    dAA, dAP, dPP = {}, {}, {}
    for d_, (f1, f2, g1, g2) in ((dAA, (a1, a2, a1, a2)), (dAP, (a1, a2, b1, b2)), (dPP, (b1, b2, b1, b2))):
        addto(d_, mul(f1, g1), Fr(1))
        addto(d_, mul(f2, g2), Fr(1))
    T = {}
    addto(T, dAA, S22 / det)
    addto(T, dAP, -2 * S12 / det)
    addto(T, dPP, S11 / det)
    assert all(v_[1] == 0 and T.get(-k, (None,))[0] == v_[0] for k, v_ in T.items())        # real and even
    Tc = {k: (T[k][0] if k == 0 else 2 * T[k][0]) for k in T if k >= 0 and T[k][0] != 0}  # cosine coefficients
    assert all(k % 2 == 0 for k in Tc)
    l1 = sum(abs(v_) for v_ in Tc.values())
    row = next(r_ for r_ in RES["rows"] if r_["candidate"] == name)
    match = {"S11": str(S11) == row["S11"], "S12": str(S12) == row["S12"], "S22": str(S22) == row["S22"],
             "trace_cosine_coefficients": {str(k): str(v_) for k, v_ in sorted(Tc.items())} == row["trace_cosine_coefficients"],
             "trace_l1_exact": str(l1) == row["trace_l1_exact"], "l1 < (583/1000)^2": l1 < Fr(583, 1000)**2}
    # P = gamma cos(2 th) Theta + sin(2 th) Theta' with Theta = Theta0 (the leading profile of grad R)
    Pchk = {}
    for n, tn in th0.items():
        for k, w in ((n + 2, gam * tn / 2 + n * tn / 2), (n - 2, gam * tn / 2 - n * tn / 2)):
            if k < 0:
                k, w = -k, -w
            if k:
                Pchk[k] = Pchk.get(k, Fr(0)) + w
    Pchk = {k: v_ for k, v_ in Pchk.items() if v_ != 0}
    match["P from Theta0"] = Pchk == P
    assert all(v_ for k_, v_ in match.items() if k_ != "P from Theta0"), match
    cand[name] = {"A": A, "P": P, "ns": ns, "S": (S11, S12, S22), "det": det, "Tc": Tc, "l1": l1,
                  "V": (a1, a2, b1, b2), "th0": th0}
    OUT["B"][name] = {"matches_result_json": match, "modes": ns, "max_cos_degree": max(Tc), "l1": str(l1)}
    print("(B) %s: modes %s; own S, T and l1 equal result.json: %s; l1 < (583/1000)^2: %s; P from Theta0: %s"
          % (name, ns, all(match[k_] for k_ in ("S11", "S12", "S22", "trace_cosine_coefficients", "trace_l1_exact")),
             match["l1 < (583/1000)^2"], match["P from Theta0"]))

# =============================== (C) Arb max of T, FLOAT diagnostics ===============================
ctx.prec = 200
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
    return ("%." + str(max(pl, 0)) + "f") % out if pl >= 0 else str(int(out))


OUT["C"] = {}
NC = 4096
for name, cd in cand.items():
    Tc = {k: A_(v_) for k, v_ in cd["Tc"].items()}
    M1 = sum((abs(v_) * k for k, v_ in Tc.items()), arb(0))
    M2 = sum((abs(v_) * k * k for k, v_ in Tc.items()), arb(0))
    hw = PI / (4 * NC)                                             # half-width of a cell of [0, pi/2]
    up = arb(0)
    low = arb(0)
    for i in range(NC):
        tm = (2 * i + 1) * hw
        val = sum((v_ * (k * tm).cos() for k, v_ in Tc.items()), arb(0))
        der = sum((-v_ * k * (k * tm).sin() for k, v_ in Tc.items()), arb(0))
        bound = val + abs(der) * hw + M2 * hw * hw / 2
        if i == 0 or bound.upper() > up.upper():
            up = bound
        low = val if val.lower() > low.lower() else low
    Tmax_up = arb(up.upper())
    Emax = Tmax_up.sqrt()
    cd["Eprof_trace_max"] = Emax
    cd["Eprof_l1"] = A_(cd["l1"]).sqrt()
    OUT["C"][name] = {"max_T_upper": directed(Tmax_up, True, 10), "max_T_lower_point": directed(low, False, 10),
                      "sqrt_max_T_upper": directed(Emax, True, 7), "sqrt_l1_upper": directed(cd["Eprof_l1"], True, 7)}
    # FLOAT diagnostics
    thv = np.linspace(0, 2 * np.pi, 8193)[:-1]
    a1, a2, b1, b2 = cd["V"]
    ev = lambda f: sum(float(re_) * np.cos(k * thv) - float(im_) * np.sin(k * thv) for k, (re_, im_) in f.items())
    VA = np.array([ev(a1), ev(a2)])
    VP = np.array([ev(b1), ev(b2)])
    S11, S12, S22 = (float(v_) for v_ in cd["S"])
    Gaa, Gap, Gpp = (VA * VA).sum(0), (VA * VP).sum(0), (VP * VP).sum(0)
    det = S11 * S22 - S12 * S12
    tr = (S22 * Gaa - 2 * S12 * Gap + S11 * Gpp) / det
    dt = (Gaa * Gpp - Gap * Gap) / det
    lam = (tr + np.sqrt(np.maximum(tr * tr - 4 * dt, 0))) / 2
    qf = float(qF)
    fA = sum(float(v_) * np.sin(n * thv) for n, v_ in cd["A"].items())
    fP = sum(float(v_) * np.sin(n * thv) for n, v_ in cd["P"].items())
    dA = sum(n * float(v_) * np.cos(n * thv) for n, v_ in cd["A"].items())
    dP = sum(n * float(v_) * np.cos(n * thv) for n, v_ in cd["P"].items())
    def ratio(z1, z2):
        num = np.hypot(z1 * VA[0] + z2 * VP[0], z1 * VA[1] + z2 * VP[1]).max()
        return num / np.hypot(qf * (z1 * fA + z2 * fP), z1 * dA + z2 * dP).max()
    # z = (1, t): the relevant t are of order 1e4 to 1e5, so a grid in t (log spaced, both signs), then z = (0, 1)
    tl = np.concatenate([-np.logspace(8, -2, 3001), [0.0], np.logspace(-2, 8, 3001)])
    rv = np.array([ratio(1.0, t) for t in tl])
    k0 = int(rv.argmax())
    tf = np.linspace(tl[max(k0 - 1, 0)], tl[min(k0 + 1, len(tl) - 1)], 801)
    rf = np.array([ratio(1.0, t) for t in tf])
    best = (float(rf.max()), float(tf[int(rf.argmax())]))
    if ratio(0.0, 1.0) > best[0]:
        best = (float(ratio(0.0, 1.0)), float("inf"))
    c4 = 4 * float(cF)
    kap = lambda t: np.hypot(VA[0] + t * VP[0], VA[1] + t * VP[1]).max() / c4
    nsup = lambda t: np.hypot(qf * (fA + t * fP), dA + t * dP).max() / c4
    tg = np.linspace(-4e5, 4e5, 8001)
    kv = np.array([kap(t) for t in tg])
    i0 = int(kv.argmin())
    cd["kap"] = kap
    cd["nsup"] = nsup
    OUT["C"][name].update({"FLOAT_max_theta_sqrt_T": float(np.sqrt(tr.max())), "FLOAT_max_theta_sqrt_lambda_max": float(np.sqrt(lam.max())),
                           "FLOAT_sup_normalized_constant": float(best[0]), "FLOAT_sup_normalized_argmax_t": best[1],
                           "FLOAT_min_t_kappa": float(kv[i0]), "FLOAT_argmin_t_kappa": float(tg[i0])})
    print("(C) %s: max_theta T <= %s (point value >= %s), so sqrt(max T) <= %s; sqrt(l1) <= %s. FLOAT: sqrt(max T) = %.6f,"
          " sqrt(max lambda_max) = %.6f, sup-normalized constant over span(A, P) = %.6f; min_t kappa(t) = %.6g at t = %.6g"
          % (name, OUT["C"][name]["max_T_upper"], OUT["C"][name]["max_T_lower_point"], OUT["C"][name]["sqrt_max_T_upper"],
             OUT["C"][name]["sqrt_l1_upper"], np.sqrt(tr.max()), np.sqrt(lam.max()), best[0], kv[i0], tg[i0]))

# =============================== (D) the finite-radius question ===============================
R375 = json.loads((HERE / "data/t4_375_review_results.json").read_text())
OUT["D"] = {"t4_375_review_results_sha256": sha(HERE / "data/t4_375_review_results.json")}


def parse(sv):
    m_, r_ = sv.strip().strip("[]").split("+/-")
    return arb(m_.strip(), r_.strip())


dF = 1 - 1 / cF
DdF = 1 - cF * (qF - dF)
qA, dA_, DdA, cA = A_(qF), A_(dF), A_(DdF), A_(cF)
s22 = (-2 * qA - 2).sqrt()
betas = {"sharpw": Fr(28496, 10**10), "TB": Fr(3793, 10**9), "graded": Fr(25, 54684)}
for name, cd in cand.items():
    A, P, ns = cd["A"], cd["P"], cd["ns"]
    Saa = sum(A.get(n, Fr(0))**2 for n in ns)
    Sap = sum(A.get(n, Fr(0)) * P.get(n, Fr(0)) for n in ns)
    Spp = sum(P.get(n, Fr(0))**2 for n in ns)
    B0 = (PI * A_(Saa - Sap**2 / Spp)).sqrt() / (4 * cA)
    g0 = A_(sum(n * v_ for n, v_ in cd["th0"].items()))
    D375 = R375["D"][name]
    Phi = parse(D375["Phi_theta_star"])
    Vl = parse(R375["E"][name]["V_low"])
    row = {}
    for lab, bt in betas.items():
        rb = (B0 / (A_(bt) * s22))**(1 / (-qA - 1))                     # cap(r_grad) = beta exactly at r_grad = rb
        Lam = DdA * B0 * rb**dA_ / (2 * PI).sqrt()                       # (CI) reaches beta only if H V + C_vel G <= Lam
        Kc = Lam / g0                                                    # V = 0, G = g0: C_vel <= Kc
        Ec = Kc / Phi                                                    # the Ecrit of REVIEW_T4_375 (V = 0, H = Phi)
        EcV = (Lam / Phi - Vl) / g0                                      # with V >= |U_lead(0)|
        row[lab] = {"r_beta": directed(rb, True, 7), "Kcrit_upper": directed(Kc, True, 7), "Ecrit_upper": directed(Ec, True, 7),
                    "Ecrit_V_upper": directed(EcV, True, 7),
                    "margin_583_upper": directed(Ec - arb(583) / 1000, True, 7),
                    "margin_sqrt_l1_upper": directed(Ec - cd["Eprof_l1"], True, 7),
                    "margin_sqrt_maxT_upper": directed(Ec - cd["Eprof_trace_max"], True, 7),
                    "margin_V_583_upper": directed(EcV - arb(583) / 1000, True, 7),
                    "583_below_Ecrit_upper": bool(arb(583) / 1000 < Ec)}
        if lab == "sharpw":
            Kf = float(Kc.mid())
            kap, nsup = cd["kap"], cd["nsup"]
            # FLOAT: the t-window where the asymptotic velocity coefficient kappa(t) is below Kcrit, by bisection
            t0 = OUT["C"][name]["FLOAT_argmin_t_kappa"]

            def edge(lo, hi):
                for _ in range(60):
                    mid = (lo + hi) / 2
                    if (kap(mid) <= Kf) == (kap(lo) <= Kf):
                        lo = mid
                    else:
                        hi = mid
                return (lo + hi) / 2
            row[lab]["FLOAT_t_window_kappa_below_Kcrit"] = [edge(t0, t0 - 2e6), edge(t0, t0 + 2e6)]
            tst = float(parse(D375["m_at_theta_star"]).mid()) / math.pi
            row[lab]["FLOAT_kappa_at_t_theta_star"] = kap(tst)
            row[lab]["FLOAT_Nsup_at_t_theta_star"] = nsup(tst)
            row[lab]["C0_ratio_B0_over_sqrt2pi_Phi_upper"] = directed(B0 / ((2 * PI).sqrt() * Phi), True, 7)
    OUT["D"][name] = row
    sw = row["sharpw"]
    print("(D) %s sharpw: r_beta <= %s; Kcrit <= %s; Ecrit <= %s (V = 0), <= %s (V >= |U_lead(0)|); margins Ecrit - Eprof <= "
          "%s (583/1000), %s (sqrt l1), %s (sqrt max T), %s (V term, 583/1000); C0 ratio B0/(sqrt(2pi) Phi) <= %s. FLOAT: "
          "kappa(t) <= Kcrit for t in [%.6g, %.6g]; at t = m(theta*)/pi kappa = %.6g, Nsup = %.6g"
          % (name, sw["r_beta"], sw["Kcrit_upper"], sw["Ecrit_upper"], sw["Ecrit_V_upper"], sw["margin_583_upper"],
             sw["margin_sqrt_l1_upper"], sw["margin_sqrt_maxT_upper"], sw["margin_V_583_upper"],
             sw["C0_ratio_B0_over_sqrt2pi_Phi_upper"], *sw["FLOAT_t_window_kappa_below_Kcrit"],
             sw["FLOAT_kappa_at_t_theta_star"], sw["FLOAT_Nsup_at_t_theta_star"]))
    for lab in ("TB", "graded"):
        print("(D) %s %s: Ecrit <= %s; margin to 583/1000 <= %s; 583/1000 below Ecrit bound: %s"
              % (name, lab, row[lab]["Ecrit_upper"], row[lab]["margin_583_upper"], row[lab]["583_below_Ecrit_upper"]))

OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_402_review_results.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
print("elapsed %.1f s" % OUT["elapsed_s"])
