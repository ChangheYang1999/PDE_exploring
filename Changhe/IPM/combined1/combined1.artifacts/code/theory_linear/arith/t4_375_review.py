"""Independent review of T4-375 (c1-t4 research/endpoint_gradient_budget/PROOF.md, sha256 ce8e8db2...a2aa8): the
weighted gradient budget forced by an endpoint profile, and the reach of (CI) of T4-351 (reviews/REVIEW_T4_375.md).

Run from artifacts/:  python3 -B -u arith/t4_375_review.py
Needs sympy, mpmath, python-flint (Arb). Reads data/t4_335_sharpE_results.json (run arith/t4_335_sharpE.py first).

Notation as in the PROOF: b = (A + t P)/(4c), t = m/pi, A = F12 and P the exact sine coefficient maps of the
endpoint data (odd n), ||v||_0^2 = int v^2, ||v||_q^2 = int (q^2 v^2 + v'^2) over the full circle,
B0 = min_t ||A + t P||_0/(4c), B1 = min_t ||A + t P||_q/(4c).
Parts:
  (A) sympy and mpmath, exact or high precision: the scaling of the weighted gradient bound under h_R; the polar
      gradient of r^q b; the circle norms of sine polynomials; the weighted projection; the pointwise minimum over t
      (a cross product); the algebra of (4) and (5) and of the improvement factor.
  (B) exact rationals: B0^2, B1^2 and the two minimizing moments from the coefficient maps; comparison with the exact
      strings of c1-t4's result.json; B1^2 >= (q^2 + 1) B0^2.
  (C) Arb: B0, B1, H >= B1/sqrt(2 pi), g0 = Theta'(0), E_q* of T4-335 (2), r_grad, the cap (4), the E = 1 cap and
      Ecrit (5) at the three labeled beta; comparison with result.json.
  (D) Arb, new: the pointwise form of (1) gives, for every real t and every theta,
        H >= |grad f| >= Phi(theta) = |q| |A P' - A' P|(theta) / (4c sqrt(q^2 P^2 + P'^2)(theta))
      at every theta where (qP, P') is nonzero (asserted at theta*), so H >= Phi(theta*). FLOAT minimax min_t max_theta
      for comparison only: the FLOAT agreement does not prove a saddle (revision after T4-385, repair 1).
  (E) Arb: the reach of (CI) with H >= max Phi, with the proved E_q*, with E_new(3/20) of arith/t4_335_sharpE.py,
      with E = 1, and with the FLOAT lower value E_low of that script; V >= |U_lead(0)| or V = 0.
Decimal displays of Arb balls in (E) are rounded outward from the exact endpoints (lower bounds down, upper bounds up;
revision 3, after T4-396 noted nearest-rounded displays in a sibling review; revision 2 printed %.5g, %.4g and %.6f of
float endpoints). E_new(3/20) is labeled as a CLAIMED Arb bound awaiting its separate audit (revision 2 said
"proved").
Output: logs/t4_375_review.log, data/t4_375_review_results.json.
"""
import hashlib
import json
import math
import time
from decimal import Decimal
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as S
from flint import arb, ctx

HERE = Path(__file__).resolve().parents[1]
T4G = Path("RUN_ROOT/theory_audit_T4/research/endpoint_gradient_budget")
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(T4G / "PROOF.md") == "ce8e8db2dc4ce001136d4e9324ce07fd4beb77732744cad351ee7e17675a2aa8"
assert sha(T4G / "verification/result.json") == "5e29af4997b8de34fe53366cc3e86d0f529915bc2e2daaa66f755f28ad6e45fb"
assert sha(T4G / "source/moment_resolved_tail_PROOF.md") == "99aa80a9b5ce0474e26c8a53e53218b2b1bb628f0283eab5eb62b4aeefead6df"
assert sha(T4G / "source/endpoint_closure_inequality_PROOF.md") == "85e01f1bfab61b078138120f3ec6011b76ace5cd45d7436d7cdd5ca35251fc34"
ep_sha = {"007": "bcd0e49225807ba313dfb86ec386b4d3d3411bdcb233072d5047e84cc27ec58b",
          "013": "3a2cf49c387db2fd95e7174a2b5f58103201857f01ba875e391b88714ab96471",
          "014": "8168bf8b326124bc720cc992a5fbe0300d9b1250eb9f4e862b0f2ce38b53b6ce"}
MAN = json.loads((T4G / "data/manifest.json").read_text())
for nm, h_ in ep_sha.items():
    assert sha(T4G / f"data/{nm}_endpoint.json") == h_ == MAN["inputs"][f"{nm}_endpoint.json"]["sha256"]
RES = json.loads((T4G / "verification/result.json").read_text())
SHE = json.loads((HERE / "data/t4_335_sharpE_results.json").read_text())

# =============================== (A) exact ===============================
R, s, H, rr = S.symbols("R s H r", positive=True)
q = S.Symbol("q", negative=True)
A1 = S.simplify(S.powsimp(S.expand_power_base((R * (s + 1 / R))**(q - 1), force=True) * R**(1 - q), force=True)
                - (s + 1 / R)**(q - 1)) == 0 and S.simplify(R * (s + 1 / R) - (1 + R * s)) == 0
th = S.Symbol("theta", real=True)
bf = S.Function("b")(th)
f = rr**q * bf
A2 = S.simplify(S.diff(f, rr) - q * rr**(q - 1) * bf) == 0 and S.simplify(S.diff(f, th) / rr - rr**(q - 1) * S.diff(bf, th)) == 0
a1, a3, a5, p1, p3, p5, tt, qq = S.symbols("a1 a3 a5 p1 p3 p5 t qq", real=True)
v = a1 * S.sin(th) + a3 * S.sin(3 * th) + a5 * S.sin(5 * th)
A3 = (S.simplify(S.integrate(v**2, (th, 0, 2 * S.pi)) - S.pi * (a1**2 + a3**2 + a5**2)) == 0
      and S.simplify(S.integrate(S.diff(v, th)**2, (th, 0, 2 * S.pi)) - S.pi * (a1**2 + 9 * a3**2 + 25 * a5**2)) == 0)
ws = [qq**2 + n * n for n in (1, 3, 5)]
aa, pp = [a1, a3, a5], [p1, p3, p5]
Qt = sum(w_ * (a_ + tt * p_)**2 for w_, a_, p_ in zip(ws, aa, pp))
tstar = S.solve(S.diff(Qt, tt), tt)[0]
Swaa = sum(w_ * a_ * a_ for w_, a_ in zip(ws, aa))
Swap = sum(w_ * a_ * p_ for w_, a_, p_ in zip(ws, aa, pp))
Swpp = sum(w_ * p_ * p_ for w_, p_ in zip(ws, pp))
A4 = {"weighted_projection": S.simplify(Qt.subs(tt, tstar) - (Swaa - Swap**2 / Swpp)) == 0,
      "minimizer": S.simplify(tstar + Swap / Swpp) == 0,
      "convex_in_t": S.simplify(S.diff(Qt, tt, 2) - 2 * Swpp) == 0}
u1, u2, v1, v2 = S.symbols("u1 u2 v1 v2", real=True)
Qc = (u1 + tt * v1)**2 + (u2 + tt * v2)**2
tc = S.solve(S.diff(Qc, tt), tt)[0]
A5 = S.simplify(Qc.subs(tt, tc) - (u1 * v2 - u2 * v1)**2 / (v1**2 + v2**2)) == 0
# (4), (5), improvement factor and the tail integral, mpmath at 60 digits on random parameter sets
mp.mp.dps = 60
rng = np.random.default_rng(375)
A6 = []
for _ in range(6):
    qv = mp.mpf(-3) - mp.mpf(rng.uniform(0.05, 0.95))
    dv = mp.mpf(rng.uniform(0.1, 0.9))
    Dv, Gv, Ev = [mp.mpf(rng.uniform(1, 30)) for _ in range(3)]
    B0v = mp.mpf(rng.uniform(1, 1e5))
    B1v = B0v * mp.mpf(rng.uniform(1.1, 10))
    rg_ = (Ev * Gv * B1v / (Dv * B0v))**(1 / dv)
    cap = B0v * rg_**(qv + 1) / mp.sqrt(-2 * qv - 2)
    cap_amp = B0v * ((Ev * Gv / Dv)**(1 / dv))**(qv + 1) / mp.sqrt(-2 * qv - 2)
    beta = cap * mp.mpf(rng.uniform(0.2, 5))
    Ec = Dv * B0v / (Gv * B1v) * (B0v / (beta * mp.sqrt(-2 * qv - 2)))**(dv / (-qv - 1))
    rgc = (Ec * Gv * B1v / (Dv * B0v))**(1 / dv)
    capc = B0v * rgc**(qv + 1) / mp.sqrt(-2 * qv - 2)
    tail = mp.quad(lambda x: x**(2 * qv + 1), [rg_, mp.inf])
    A6.append({"Ecrit_gives_cap_beta": abs(capc / beta - 1) < mp.mpf(10)**-50,
               "improvement_factor": abs(cap / cap_amp / (B1v / B0v)**((qv + 1) / dv) - 1) < mp.mpf(10)**-50,
               "tail_integral": abs(tail / (rg_**(2 * qv + 2) / (-2 * qv - 2)) - 1) < mp.mpf(10)**-40,
               "cap_decreasing_in_E": (B0v * ((2 * Ev * Gv * B1v / (Dv * B0v))**(1 / dv))**(qv + 1)) < cap})
OUT["A"] = {"A1_rescaled_gradient_bound": A1, "A2_polar_gradient": A2, "A3_circle_norms": A3,
            "A4_projection": A4, "A5_pointwise_min_over_t": A5, "A6_cap_Ecrit_algebra": A6}
flat = [A1, A2, A3, A5] + list(A4.values()) + [x_ for d_ in A6 for x_ in d_.values()]
assert all(flat)
print("(A) all exact and 60-digit checks pass:", json.dumps(OUT["A"], default=str))

# =============================== (B) exact rationals ===============================
cF = Fr(4076476460239181, 2**51)
qF = 1 / cF - 4
dF = 1 - 1 / cF
assert str(qF) == RES["q"] and str(dF) == RES["delta"] and str(cF) == RES["c"]
DdF = 1 - cF * (qF - dF)
assert str(DdF) == RES["D_delta"] and DdF == cF * (4 + dF)
data = {}
OUT["B"] = {}
for name in ("007", "013", "014"):
    ep = json.loads((T4G / f"data/{name}_endpoint.json").read_text())
    a_ = {int(k_): Fr(v_) for k_, v_ in ep["F12"].items()}
    p_ = {int(k_): Fr(v_) for k_, v_ in ep["P"].items()}
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    ns = sorted(set(a_) | set(p_))
    assert all(n % 2 == 1 and n > 0 for n in ns)
    w_ = {n: qF * qF + n * n for n in ns}
    get = lambda d_, n: d_.get(n, Fr(0))
    Saa = sum(get(a_, n)**2 for n in ns)
    Sap = sum(get(a_, n) * get(p_, n) for n in ns)
    Spp = sum(get(p_, n)**2 for n in ns)
    Waa = sum(w_[n] * get(a_, n)**2 for n in ns)
    Wap = sum(w_[n] * get(a_, n) * get(p_, n) for n in ns)
    Wpp = sum(w_[n] * get(p_, n)**2 for n in ns)
    X0 = Saa - Sap**2 / Spp           # (4c B0)^2/pi
    X1 = Waa - Wap**2 / Wpp           # (4c B1)^2/pi
    row = next(r_ for r_ in RES["rows"] if r_["candidate"] == name)
    X0r, X1r = Fr(row["unweighted_projection_squared_without_pi_exact"]), Fr(row["gradient_projection_squared_without_pi_exact"])
    norm_match = {"X0": [k_ for k_, val in (("(4cB0)^2/pi", X0), ("B0^2/pi", X0 / (4 * cF)**2)) if val == X0r],
                  "X1": [k_ for k_, val in (("(4cB1)^2/pi", X1), ("B1^2/pi", X1 / (4 * cF)**2)) if val == X1r]}
    assert norm_match["X0"] and norm_match["X1"]
    assert X1 >= (qF * qF + 1) * X0 and X0 > 0
    t0_, t1_ = -Sap / Spp, -Wap / Wpp
    g0 = sum(n * b_ for n, b_ in th0.items())
    assert g0 == Fr(row["G_lower_point_exact"])
    data[name] = {"a": a_, "p": p_, "th0": th0, "X0": X0, "X1": X1, "t0": t0_, "t1": t1_, "g0": g0, "row": row}
    OUT["B"][name] = {"modes": ns, "modes_match": ns == row["modes"], "normalization_match": norm_match,
                      "X1_over_X0": float(X1 / X0), "(q^2+1)": float(qF * qF + 1),
                      "t_amplitude": float(t0_), "t_gradient": float(t1_), "g0": float(g0)}
    print("(B) %s: modes %s (= c1-t4: %s); exact projections equal c1-t4's strings as %s and %s; X1/X0 = %.12f >= q^2 + 1"
          " = %.6f; minimizing m/pi: amplitude %.6f, gradient %.6f; Theta'(0) = %.12f (= c1-t4's G_lower_point_exact)"
          % (name, ns, ns == row["modes"], norm_match["X0"], norm_match["X1"], float(X1 / X0), float(qF * qF + 1),
             float(t0_), float(t1_), float(g0)))

# =============================== (C) Arb ===============================
ctx.prec = 256
PI = arb.pi()
A_ = lambda fr_: arb(fr_.numerator) / fr_.denominator
cA, qA, dA, DdA = A_(cF), A_(qF), A_(dF), A_(DdF)
Eq = (arb(1) / 2 + arb(2)**(-qA) + arb(2)**(3 - qA) + arb(2)**(qA + 2) / (-qA) + arb(2)**(-qA - 2) / (-qA - 3)
      + arb(2)**(2 - qA) / (qA + 5))
betas = {"sharpw_rounded_ceiling": Fr(28496, 10**10), "TB_sharp_rounded_ceiling": Fr(3793, 10**9),
         "original_graded_ceiling": Fr(25, 54684)}
s22 = (-2 * qA - 2).sqrt()


def parse(sv):                      # "[mid +/- rad]" or a plain number, as an arb ball
    sv = sv.strip()
    if sv.startswith("["):
        m_, r_ = sv.strip("[]").split("+/-")
        return arb(m_.strip(), r_.strip())
    return arb(sv)


def agree(x, sv, rel=arb(10)**-60):
    y = parse(sv)
    return bool(abs(x - y) < (x.rad() + y.rad()) + rel * abs(x) + arb(10)**-200)


def capf(E, V, G, Hlow, B0):
    rg_ = (arb(2) * PI).sqrt() * Hlow * (V + E * G) / (DdA * B0)
    rg_ = rg_**(1 / dA)
    return rg_, B0 * rg_**(qA + 1) / s22


def directed(xv, up, sig=7, fixed=False):
    """Decimal string with sig significant digits, >= every point of the ball xv if up, else <= every point.
    Exact: works on the exact endpoint xv.upper() or xv.lower() as a dyadic rational."""
    m_, e_ = (xv.upper() if up else xv.lower()).man_exp()
    v_ = Fr(int(m_)) * Fr(2)**int(e_)
    assert v_ > 0
    k_ = int(math.floor(math.log10(float(v_))))
    while Fr(10)**k_ > v_:
        k_ -= 1
    while Fr(10)**(k_ + 1) <= v_:
        k_ += 1
    pl = sig - 1 - k_
    n_ = math.ceil(v_ * Fr(10)**pl) if up else math.floor(v_ * Fr(10)**pl)
    d_ = Decimal(n_).scaleb(-pl)
    out = format(d_, "f") if fixed else format(d_, ".%de" % (sig - 1))
    assert (Fr(Decimal(out)) >= v_) if up else (Fr(Decimal(out)) <= v_)
    return out


def Ecrit(beta, V, G, Hlow, B0):    # largest E with cap(E) >= beta: necessary for the test to reach beta
    Y = (B0 / (A_(beta) * s22))**(dA / (-qA - 1))
    return (DdA * B0 * Y / ((arb(2) * PI).sqrt() * Hlow) - V) / G


assert agree(Eq, RES["valid_E"])
OUT["C"] = {"E_q*": Eq.str(30)}
for name, dd in data.items():
    B0 = (PI * A_(dd["X0"])).sqrt() / (4 * cA)
    B1 = (PI * A_(dd["X1"])).sqrt() / (4 * cA)
    HL2 = B1 / (2 * PI).sqrt()
    g0 = A_(dd["g0"])
    rg_, cap = capf(Eq, arb(0), g0, HL2, B0)
    _, cap1 = capf(arb(1), arb(0), g0, HL2, B0)
    row = dd["row"]
    chk = {"B0": agree(B0, row["B0"]), "B1": agree(B1, row["B1"]), "B1/B0": agree(B1 / B0, row["B1_over_B0"]),
           "H_lower": agree(HL2, row["H_lower_bound"]), "r_grad": agree(rg_, row["r_grad_lower_bound"]),
           "cap": agree(cap, row["CI_cap_upper_bound"]), "cap_E1": agree(cap1, row["hypothetical_E_equal_1_cap"]),
           "improvement": agree((B1 / B0)**((qA + 1) / dA), row["cap_improvement_factor"]),
           "gradient_moment": agree(PI * A_(dd["t1"]), row["gradient_minimizing_moment"])}
    ecs = row["necessary_Ecrit"]
    ecs = json.loads(ecs.replace("'", '"')) if isinstance(ecs, str) else ecs
    ec = {k_: Ecrit(bv, arb(0), g0, HL2, B0) for k_, bv in betas.items()}
    for k_ in betas:
        chk["Ecrit_" + k_] = agree(ec[k_], ecs[k_])
    assert all(chk.values()), chk
    claims = {"H_above_328627": HL2 > 328627, "r_grad_above_1.498e8": rg_ > 149800000,
              "cap_below_3.752e-16": cap < arb(3752) / arb(10)**19, "E1_cap_below_1.5411e-4": cap1 < arb(15411) / arb(10)**8,
              "Ecrit_sharpw_below_2.0746": ec["sharpw_rounded_ceiling"] < arb(20746) / 10000,
              "Ecrit_TB_below_1.96887": ec["TB_sharp_rounded_ceiling"] < arb(196887) / 100000,
              "Ecrit_graded_below_0.81966": ec["original_graded_ceiling"] < arb(81966) / 100000}
    assert all(claims.values()), claims
    dd.update({"B0": B0, "B1": B1, "HL2": HL2, "g0A": g0})
    OUT["C"][name] = {"agree_with_c1-t4": chk, "stated_bounds": claims, "B0": B0.str(20), "B1": B1.str(20),
                      "H_L2": HL2.str(20), "r_grad": rg_.str(15), "cap": cap.str(15), "cap_E1": cap1.str(15),
                      "Ecrit": {k_: x_.str(15) for k_, x_ in ec.items()}}
    print("(C) %s: B0 = %s, B1 = %s, H >= B1/sqrt(2pi) = %s; r_grad = %s; cap(E_q*) = %s; cap(E = 1) = %s; Ecrit: %s;"
          " all %d values agree with c1-t4's result.json; all 7 stated bounds hold"
          % (name, B0.str(12), B1.str(12), HL2.str(12), rg_.str(10), cap.str(6), cap1.str(6),
             ", ".join("%s %s" % (k_, x_.str(8)) for k_, x_ in ec.items()), len(chk)))

# =============================== (D) pointwise (sup-norm) form ===============================


def trig_arrays(cf, thv):
    ns_ = sorted(cf)
    val = sum(float(cf[n]) * np.sin(n * thv) for n in ns_)
    der = sum(n * float(cf[n]) * np.cos(n * thv) for n in ns_)
    return val, der


qf, cf_ = float(qF), float(cF)
OUT["D"] = {}
for name, dd in data.items():
    thv = np.linspace(0, np.pi / 2, 400001)
    Av, dAv = trig_arrays(dd["a"], thv)
    Pv, dPv = trig_arrays(dd["p"], thv)
    Phi = abs(qf) * np.abs(Av * dPv - dAv * Pv) / (4 * cf_ * np.sqrt(qf * qf * Pv**2 + dPv**2))
    j = int(np.argmax(Phi))
    # refine by golden section on the explicit function
    lo, hi = thv[max(j - 2, 0)], thv[min(j + 2, len(thv) - 1)]

    def phi1(x):
        a0, a1_ = trig_arrays(dd["a"], np.array([x]))
        p0, p1_ = trig_arrays(dd["p"], np.array([x]))
        return float(abs(qf) * abs(a0[0] * p1_[0] - a1_[0] * p0[0]) / (4 * cf_ * np.sqrt(qf * qf * p0[0]**2 + p1_[0]**2)))
    gr = (np.sqrt(5) - 1) / 2
    x1, x2 = hi - gr * (hi - lo), lo + gr * (hi - lo)
    for _ in range(80):
        if phi1(x1) > phi1(x2):
            hi, x2 = x2, x1
            x1 = hi - gr * (hi - lo)
        else:
            lo, x1 = x1, x2
            x2 = lo + gr * (hi - lo)
    ths = Fr((lo + hi) / 2).limit_denominator(10**12)
    tA = A_(ths)

    def arb_trig(cf, x):
        val = sum(A_(cf[n]) * (n * x).sin() for n in cf)
        der = sum(n * A_(cf[n]) * (n * x).cos() for n in cf)
        return val, der
    a0, a1_ = arb_trig(dd["a"], tA)
    p0, p1_ = arb_trig(dd["p"], tA)
    assert (qA * qA * p0 * p0 + p1_ * p1_) > 0          # (qP, P') nonzero at theta*: the quotient form applies
    PhiA = -qA * abs(a0 * p1_ - a1_ * p0) / (4 * cA * (qA * qA * p0 * p0 + p1_ * p1_).sqrt())
    tbest = -(qA * qA * a0 * p0 + a1_ * p1_) / (qA * qA * p0 * p0 + p1_ * p1_)    # minimizing t at theta*
    # FLOAT minimax: min over t of max over the grid of |(q b_t, b_t')|, near the pointwise minimizer
    tb = float(tbest.mid())
    Fmax = lambda t_: float(np.max(np.sqrt(qf * qf * (Av + t_ * Pv)**2 + (dAv + t_ * dPv)**2)) / (4 * cf_))
    lo_t, hi_t = tb - 0.05 * abs(tb), tb + 0.05 * abs(tb)
    for _ in range(100):
        m1, m2 = lo_t + (hi_t - lo_t) / 3, hi_t - (hi_t - lo_t) / 3
        if Fmax(m1) < Fmax(m2):
            hi_t = m2
        else:
            lo_t = m1
    tmm = (lo_t + hi_t) / 2
    mm = Fmax(tmm)
    # also: the full pointwise bound (1) at theta* includes the amplitude part, max(|b|, |grad|) = |grad| since |q| > 1
    Hinf = arb(PhiA.lower())
    ratio = Hinf / dd["HL2"]
    dd.update({"Hinf": Hinf, "theta_star": ths})
    OUT["D"][name] = {"theta_star": str(ths), "theta_star_float": float(ths), "Phi_theta_star": PhiA.str(20),
                      "Phi_theta_star_down": directed(PhiA, False, 12, True), "ratio_down": directed(ratio, False, 7, True),
                      "H_inf_lower": Hinf.str(20), "ratio_to_B1_over_sqrt2pi": ratio.str(12),
                      "m_at_theta_star": (PI * tbest).str(15), "FLOAT_grid_max_Phi": float(Phi[j]),
                      "FLOAT_minimax_min_t_max_theta": mm, "FLOAT_minimax_m": float(np.pi * tmm),
                      "FLOAT_minimax_gap_relative": (mm - float(PhiA.mid())) / mm}
    print("(D) %s: theta* = %.10f; H >= Phi(theta*) = %s (Arb) >= %s, at least %s times B1/sqrt(2pi); the minimizing"
          " moment at theta* is m = %s; FLOAT minimax min_m max_theta = %.6f at m = %.4f (relative gap to Phi(theta*) %.1e)"
          % (name, float(ths), PhiA.str(12), OUT["D"][name]["Phi_theta_star_down"], OUT["D"][name]["ratio_down"],
             (PI * tbest).str(10), mm, np.pi * tmm, (mm - float(PhiA.mid())) / mm))

# =============================== (E) reach of (CI) ===============================
E_new = arb(SHE["B"]["E_new_upper"])
E_low = SHE["D"]["best_lower"]
OUT["E"] = {"E_new_upper": SHE["B"]["E_new_upper"], "E_low_FLOAT": E_low}
pE = 1 / cA + 2
for name, dd in data.items():
    tharb = {n: A_(b_) for n, b_ in dd["th0"].items()}
    V0 = (pE - 1) * abs(sum(n * b_ / (pE * pE - n * n) for n, b_ in tharb.items()))       # |U_lead(0)|, a lower bound for V
    Vlow = arb(V0.lower())
    rows = []
    for labE, E in (("E_q* (T4-335, proved)", Eq), ("E_new(3/20) (t4_335_sharpE.py, CLAIMED)", E_new),
                    ("E = 1 (hypothetical)", arb(1)), ("E_low (FLOAT lower value of the best constant)", arb(E_low))):
        for labH, Hl in (("H >= B1/sqrt(2pi) (T4-375)", dd["HL2"]), ("H >= max Phi (this review)", dd["Hinf"])):
            for labV, V in (("V = 0", arb(0)), ("V >= |U_lead(0)|", Vlow)):
                rg_, cap = capf(E, V, dd["g0A"], Hl, dd["B0"])
                rows.append({"E": labE, "H": labH, "V": labV, "r_grad": float(rg_.lower()), "cap_upper": float(cap.upper()),
                             "r_grad_down": directed(rg_, False, 6), "cap_up": directed(cap, True, 5),
                             "reaches": {k_: bool(cap > A_(bv)) for k_, bv in betas.items()}})
    ecr = {}
    for labH, Hl in (("T4-375", dd["HL2"]), ("max Phi", dd["Hinf"])):
        for labV, V in (("V=0", arb(0)), ("V>=|U_lead(0)|", Vlow)):
            ecr[labH + ", " + labV] = {k_: directed(Ecrit(bv, V, dd["g0A"], Hl, dd["B0"]), True, 7, True)
                                       for k_, bv in betas.items()}
    OUT["E"][name] = {"V_low": V0.str(15), "rows": rows, "Ecrit_upper": ecr}
    print("(E) %s: V >= |U_lead(0)| = %s; upper bounds for Ecrit (necessary for (CI) to reach beta), rounded up:"
          % (name, V0.str(10)))
    for k_, d_ in ecr.items():
        print("    %-28s %s" % (k_, ", ".join("%s %s" % (b_, x_) for b_, x_ in d_.items())))
    for rw in rows:
        print("    %-48s %-28s %-17s r_grad >= %s, cap <= %s" % (rw["E"], rw["H"], rw["V"], rw["r_grad_down"], rw["cap_up"]))
OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_375_review_results.json").write_text(json.dumps(OUT, indent=1, default=str))
print("done, %.1f s" % (time.monotonic() - T0))
