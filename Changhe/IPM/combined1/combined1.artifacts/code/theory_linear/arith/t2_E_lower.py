"""A lower bound for every constant E valid in (1) of T4-335, and the consequence for (CI) of T4-351
(reviews/REVIEW_T4_375.md R4, notes/T2_TB_sharpE.md).

Run from artifacts/:  python3 -B -u arith/t2_E_lower.py
Needs sympy, mpmath, numpy, python-flint (Arb). Reads data/t4_375_review_results.json (theta* of part (D)) and
c1-t4's endpoint data in place (hashes asserted).

Statement. Let -4 < q < -3, Q = -q, delta = -q - 3, p = q + 2, and
    h(Y) = y (1 + |Y|)^(q-1) / Q = eta(rho) sin(theta),   eta(rho) = rho (1 + rho)^(q-1) / Q.
h is real, C1, S1 and centrally odd, with H_q(h) <= 1 (the H_q of T4-335 and T4-351). Its first moment is
M = (0, m), m = pi B(4, delta)/Q. For every unit vector e,
    lim_(r -> infinity) r^(-q) [U[h](r e) + DK(r e) M] = U_hom(e),
where U_hom = (v_xy, -v_xx) for v = C r^p sin(theta), C = 1/(Q (p^2 - 1)), and
    max_e |U_hom(e)| = |U_hom(pi/4)| = (Q - 1)/(2 delta Q).
So every E valid in (1), even only for r >= R0 with any R0, satisfies E >= E_lower = (Q - 1)/(2 delta Q), an exact
rational at q = q*: 0.79304...
Proof route (exact parts in (A)): the Newtonian potential of the mode-1 density eta(rho) sin(theta) is a(r) sin(theta)
with a = -(1/2)[I(r)/r + r J(r)], I(r) = int_0^r s^2 eta, J(r) = int_r^inf eta. With I = I_inf - T and
eta = s^q/Q + eps, |eps| <= (1 - q) s^(q-1)/Q (s > 0), one gets a = -I_inf/(2r) + C r^p + e(r) with e, r e', r^2 e'' all
O(r^(q+1)). The dipole part -I_inf sin(theta)/(2r) has velocity -DK(X) M exactly, and the Hessian of e(r) sin(theta)
is O(r^(q-1)). Hence r^(-q)[U[h] + DK M](r e) = U_hom(e) + O(1/r).
Parts:
  (A) sympy, exact: Delta(C r^p sin) = r^q sin/Q; Cartesian v_xx, v_xy of v = C y r^(p-1) and their polar forms;
      div U_hom = 0, curl U_hom = -d_x g; |U_hom|^2 = (C(p-1))^2 f(cos^2 theta), f(u) = f(1-u),
      f = (q+1)^2/4 + (1 - (q+1)^2/4) (2u - 1)^2; C(p-1) = -1/(delta Q); the admissibility identities for h; the mode-1
      Green formula (ODE) and the remainder formulas a~, a~', a~''; the dipole velocity plus DK M = 0; the tail
      orders; the Beta value of the moment.
  (B) exact rationals and Arb: E_lower; Ecrit of T4-375 (5) recomputed in Arb with H >= Phi(theta*) (this lane's
      REVIEW_T4_375 R2), G >= Theta'(0), V >= 0, for 007, 013, 014 and the three registered ceilings; the cap of
      (CI) at E = E_lower. Also with T4-375's H >= B1/sqrt(2 pi) alone, where every Ecrit exceeds E_lower.
  (C) FLOAT: (C1) the Green-formula velocity against a direct principal-value quadrature of the kernel at nine
      points (independent of the potential); (C2) r^(-q)[U[h] + DK M](r e) - U_hom(e) for r = 2 to 1e8 (O(1/r));
      (C3) the sup over r >= 2 and theta of r^(-q)|U[h] + DK M| (a FLOAT value of this test at finite r).
Decimal displays of Arb balls in (B) are rounded outward from the exact endpoints (lower bounds down, upper bounds up;
revision 3, after T4-396 noted nearest-rounded displays in a sibling review; revision 2 printed %.5g and %.4g of float
endpoints, which rounded r_grad = 19279.98... up to 19280 for 013).
Output: logs/t2_E_lower.log, data/t2_E_lower_results.json.
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


ep_sha = {"007": "bcd0e49225807ba313dfb86ec386b4d3d3411bdcb233072d5047e84cc27ec58b",
          "013": "3a2cf49c387db2fd95e7174a2b5f58103201857f01ba875e391b88714ab96471",
          "014": "8168bf8b326124bc720cc992a5fbe0300d9b1250eb9f4e862b0f2ce38b53b6ce"}
MAN = json.loads((T4G / "data/manifest.json").read_text())
for nm, h_ in ep_sha.items():
    assert sha(T4G / f"data/{nm}_endpoint.json") == h_ == MAN["inputs"][f"{nm}_endpoint.json"]["sha256"]
REV = json.loads((HERE / "data/t4_375_review_results.json").read_text())
# Only theta* and Phi(theta*) of its part (D) are used. theta* is asserted to equal the exact angles below (the same
# rationals as c1-t4's universal_velocity_lower/data/parameters.json). The whole-file hash is printed, not asserted:
# the file records its own run time, so its hash changes on every rerun of arith/t4_375_review.py (revision 3).
THETA_STAR = {"007": "1279020439190/874656646161", "013": "556370290457/380474310587", "014": "1200820150315/821180442832"}
assert all(REV["D"][n_]["theta_star"] == v_ for n_, v_ in THETA_STAR.items())
print("inputs: t4_375_review_results.json sha256 %s (printed; theta* asserted)" % sha(HERE / "data/t4_375_review_results.json"))

# =============================== (A) exact ===============================
x, y = S.symbols("x y", real=True)
r, s, rho, u = S.symbols("r s rho u", positive=True)
th = S.Symbol("theta", real=True)
q = S.Symbol("q", negative=True)
Q = -q
p = q + 2
C = 1 / (Q * (p**2 - 1))
pol = {x: r * S.cos(th), y: r * S.sin(th)}
R2 = x**2 + y**2
v = C * y * R2**((p - 1) / 2)
g = y * R2**((q - 1) / 2) / Q                         # g = r^q sin(theta)/Q, the homogeneous limit of h


def same(e1, e2):
    return S.simplify(S.powsimp(S.expand_power_base(S.expand(e1 - e2), force=True), force=True)) == 0


A1 = S.simplify((S.diff(v, x, 2) + S.diff(v, y, 2) - g).subs(pol)) == 0
vxx, vxy = S.diff(v, x, 2), S.diff(v, x, y)
c_, s_ = S.cos(th), S.sin(th)
vxx_pol = C * (p - 1) * r**q * s_ * (s_**2 + q * c_**2)
vxy_pol = C * (p - 1) * r**q * c_ * (c_**2 + q * s_**2)
A2 = same(vxx.subs(pol), vxx_pol) and same(vxy.subs(pol), vxy_pol)
U1, U2 = vxy, -vxx
A3 = {"div_free": same(S.diff(U1, x) + S.diff(U2, y), 0),
      "curl_is_minus_dx_g": same(S.diff(U2, x) - S.diff(U1, y), -S.diff(g, x))}
fu = (1 - u) * (1 + u * (q - 1))**2 + u * (q + u * (1 - q))**2
A4 = {"modulus": same((vxy_pol**2 + vxx_pol**2).subs(c_, S.sqrt(u)).subs(s_, S.sqrt(1 - u)),
                      (C * (p - 1))**2 * r**(2 * q) * fu),
      "f_symmetric": S.expand(fu - fu.subs(u, 1 - u)) == 0,
      "f_quadratic": S.expand(fu - ((q + 1)**2 / 4 + (1 - (q + 1)**2 / 4) * (2 * u - 1)**2)) == 0,
      "f_at_0_and_1": S.expand(fu.subs(u, 0)) == 1 and S.expand(fu.subs(u, 1)) == 1,
      "C(p-1)_equals_-1/(delta Q)": S.simplify(C * (p - 1) + 1 / ((-q - 3) * Q)) == 0}
# admissibility of h = y (1 + rho)^(q-1)/Q = phi(rho) sin(theta)/Q, phi = rho (1 + rho)^(q-1)
phi = rho * (1 + rho)**(q - 1)
Qs = S.Symbol("Qs", positive=True)
A5 = {"phi_prime": same(S.diff(phi, rho), (1 + rho)**(q - 2) * (1 + q * rho)),
      "phi_over_rho_weight": same(phi / rho * (1 + rho)**(1 - q), 1),
      "amplitude_weight": same(phi * (1 + rho)**(-q), rho / (1 + rho)),
      "factorization": S.expand((Qs * (1 + rho))**2 - (1 - Qs * rho)**2 - (Qs + 2 * Qs * rho - 1) * (Qs + 1)) == 0,
      "polar_gradient_sq": same((S.diff(phi * s_, rho)**2 + (S.diff(phi * s_, th) / rho)**2),
                                S.diff(phi, rho)**2 * s_**2 + (phi / rho)**2 * c_**2)}
# Cartesian gradient of h against the polar decomposition at random rational points, q = -3.4476..., 40 digits
mp.mp.dps = 40
qn = mp.mpf(4076476460239181) / 2**51
qn = 1 / qn - 4
hx = S.lambdify((x, y, q), S.diff(y * (1 + S.sqrt(R2))**(q - 1) / Q, x), "mpmath")
hy = S.lambdify((x, y, q), S.diff(y * (1 + S.sqrt(R2))**(q - 1) / Q, y), "mpmath")
rng = np.random.default_rng(1)
grad_rows = []
for _ in range(12):
    X1, X2 = [mp.mpf(int(rng.integers(-4000, 4000))) / int(rng.integers(1, 300)) for _ in range(2)]
    rr_ = mp.sqrt(X1**2 + X2**2)
    lhs = (hx(X1, X2, qn)**2 + hy(X1, X2, qn)**2) * (1 + rr_)**(2 - 2 * qn)
    rhs = ((X2 / rr_)**2 * (1 + qn * rr_)**2 / (1 + rr_)**2 + (X1 / rr_)**2) / qn**2
    grad_rows.append([float(rr_), float(abs(lhs / rhs - 1)), float(mp.sqrt(lhs))])
A5["cartesian_gradient_spot_checks"] = max(rw[1] for rw in grad_rows) < mp.mpf(10)**-30
A5["weighted_gradient_at_most_1_on_spots"] = all(rw[2] <= 1 for rw in grad_rows)
# mode-1 Green formula: a = -(I/r + r J)/2 solves a'' + a'/r - a/r^2 = eta; remainder a~ = (T/r - r J)/2
Ifun, Jfun, Tfun, et = [S.Function(n_)(r) for n_ in ("I", "J", "T", "eta")]
a = -(Ifun / r + r * Jfun) / 2
sub = {S.Derivative(Ifun, (r, 2)): S.diff(r**2 * et, r), S.Derivative(Jfun, (r, 2)): -S.diff(et, r),
       S.Derivative(Ifun, r): r**2 * et, S.Derivative(Jfun, r): -et}
A6 = {"green_ode": S.simplify((S.diff(a, r, 2) + S.diff(a, r) / r - a / r**2).subs(sub) - et) == 0}
at = (Tfun / r - r * Jfun) / 2                        # T = int_r^inf s^2 eta, T' = -r^2 eta
subT = {S.Derivative(Tfun, (r, 2)): -S.diff(r**2 * et, r), S.Derivative(Jfun, (r, 2)): -S.diff(et, r),
        S.Derivative(Tfun, r): -r**2 * et, S.Derivative(Jfun, r): -et}
A6["a~_prime"] = S.simplify(S.diff(at, r).subs(subT) + (Tfun / r**2 + Jfun) / 2) == 0
A6["a~_second"] = S.simplify(S.diff(at, r, 2).subs(subT) - (Tfun / r**3 + et)) == 0
A6["a~_ode"] = S.simplify((S.diff(at, r, 2) + S.diff(at, r) / r - at / r**2).subs(subT) - et) == 0
# homogeneous part: eta = r^q/Q gives T = r^(q+3)/(Q delta), J = r^(q+1)/(Q (-q-1)), a~ = C r^p
Th, Jh = r**(q + 3) / (Q * (-q - 3)), r**(q + 1) / (Q * (-q - 1))
A6["homogeneous_T"] = same(-S.diff(Th, r), r**2 * r**q / Q)
A6["homogeneous_J"] = same(-S.diff(Jh, r), r**q / Q)
A6["homogeneous_a~_is_C_r^p"] = same((Th / r - r * Jh) / 2, C * r**p)
# tails: eps = eta - s^q/Q = s^q [(1 + 1/s)^(q-1) - 1]/Q and (1 + t)^(q-1) - 1 lies in [(q-1) t, 0] for t > 0 (mean
# value theorem), so |eps| <= (1-q) s^(q-1)/Q, |T - T_hom| <= (1-q) r^(q+2)/(Q (-q-2)), |J - J_hom| <= (1-q) r^q/Q^2
# and e = O(r^(q+1)), e' = O(r^q), e'' = O(r^(q-1)); spot check of the eps bound at 40 digits
A6["eps_identity"] = same(rho * (1 + rho)**(q - 1), rho**q * (1 + 1 / rho)**(q - 1))
A6["eps_bound_spots"] = all(abs(sv * (1 + sv)**(qn - 1) - sv**qn) * sv**(1 - qn) <= (1 - qn) * (1 + mp.mpf(10)**-30)
                            for sv in [mp.mpf(10)**(k_ / mp.mpf(4)) for k_ in range(-12, 41)])
# dipole: v_d = -m y/(2 pi r^2) has velocity (m/pi)(cos 3t, sin 3t)/r^3; DK(X)(0, m) = m d_y K = -(m/pi)(cos 3t, sin 3t)/r^3
mm = S.Symbol("m", real=True)
vd = -mm * y / (2 * S.pi * R2)
Ud = (S.diff(vd, x, y), -S.diff(vd, x, 2))
Kk = (-x * y / (S.pi * R2**2), (x**2 - y**2) / (2 * S.pi * R2**2))
A7 = {"dipole_plus_DKM_zero": all(S.simplify(Ud[i] + mm * S.diff(Kk[i], y)) == 0 for i in (0, 1)),
      "moment_angular": S.integrate(s_**2, (th, 0, 2 * S.pi)) == S.pi,
      "a_dipole_is_-I_inf_over_2r": S.simplify(a.subs(Ifun, S.Symbol("Iinf") - Tfun) - (-S.Symbol("Iinf") / (2 * r) + at)) == 0}
# moment m = pi int_0^inf s^2 eta s ds ... = pi int_0^inf s^3 (1+s)^(q-1)/Q ds = pi B(4, delta)/Q
dl = -qn - 3
# substitution s = w/(1-w), 1 - w = z^(1/delta): int_0^inf s^3 (1+s)^(q-1) ds = int_0^1 (1 - z^(1/delta))^3 dz/delta
Iinf_q = mp.quad(lambda z_: (1 - z_**(1 / dl))**3, [0, 1]) / dl / (-qn)
A7["beta_value"] = abs(Iinf_q / (mp.beta(4, dl) / (-qn)) - 1) < mp.mpf(10)**-30
OUT["A"] = {"A1_laplacian": A1, "A2_cartesian_polar": A2, "A3_div_curl": A3, "A4_modulus": A4, "A5_admissibility": A5,
            "A5_spot_rows_[rho,relerr,weighted_grad]": grad_rows, "A6_green": A6, "A7_dipole_moment": A7}
flat = [A1, A2] + list(A3.values()) + list(A4.values()) + list(A5.values()) + list(A6.values()) + list(A7.values())
assert all(flat), OUT["A"]
print("(A) all exact checks pass:", json.dumps({k_: v_ for k_, v_ in OUT["A"].items() if "rows" not in k_}))

# =============================== (B) exact rationals and Arb ===============================
cF = Fr(4076476460239181, 2**51)
qF = 1 / cF - 4
QF = -qF
dF = 1 - 1 / cF
assert dF == QF - 3
E_lower = (QF - 1) / (2 * dF * QF)
ctx.prec = 256
PI = arb.pi()
A_ = lambda fr_: arb(fr_.numerator) / fr_.denominator
cA, qA, dA = A_(cF), A_(qF), A_(dF)
DdA = A_(1 - cF * (qF - dF))
s22 = (-2 * qA - 2).sqrt()
ELA = A_(E_lower)
betas = {"sharpw_rounded_ceiling": Fr(28496, 10**10), "TB_sharp_rounded_ceiling": Fr(3793, 10**9),
         "original_graded_ceiling": Fr(25, 54684)}


def capf(E, V, G, Hlow, B0):
    rg_ = ((arb(2) * PI).sqrt() * Hlow * (V + E * G) / (DdA * B0))**(1 / dA)
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


def Ecrit(beta, V, G, Hlow, B0):    # largest E with cap(E) >= beta; cap is decreasing in E, H and V
    Y = (B0 / (A_(beta) * s22))**(dA / (-qA - 1))
    return (DdA * B0 * Y / ((arb(2) * PI).sqrt() * Hlow) - V) / G


OUT["B"] = {"E_lower_exact": str(E_lower), "E_lower": float(E_lower), "E_lower_20": ELA.str(20)}
print("(B) E_lower = (Q - 1)/(2 delta Q) = %s = %.12f (exact rational)" % (ELA.str(15), float(E_lower)))
for name in ("007", "013", "014"):
    ep = json.loads((T4G / f"data/{name}_endpoint.json").read_text())
    a_ = {int(k_): Fr(v_) for k_, v_ in ep["F12"].items()}
    p_ = {int(k_): Fr(v_) for k_, v_ in ep["P"].items()}
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    ns = sorted(set(a_) | set(p_))
    get = lambda d_, n: d_.get(n, Fr(0))
    Saa = sum(get(a_, n)**2 for n in ns)
    Sap = sum(get(a_, n) * get(p_, n) for n in ns)
    Spp = sum(get(p_, n)**2 for n in ns)
    Wq = {n: qF * qF + n * n for n in ns}
    Waa = sum(Wq[n] * get(a_, n)**2 for n in ns)
    Wap = sum(Wq[n] * get(a_, n) * get(p_, n) for n in ns)
    Wpp = sum(Wq[n] * get(p_, n)**2 for n in ns)
    B0 = (PI * A_(Saa - Sap**2 / Spp)).sqrt() / (4 * cA)
    B1 = (PI * A_(Waa - Wap**2 / Wpp)).sqrt() / (4 * cA)
    g0 = A_(sum(n * b_ for n, b_ in th0.items()))
    tA = A_(Fr(REV["D"][name]["theta_star"]))
    a0 = sum(A_(a_[n]) * (n * tA).sin() for n in a_)
    a1 = sum(n * A_(a_[n]) * (n * tA).cos() for n in a_)
    p0 = sum(A_(p_[n]) * (n * tA).sin() for n in p_)
    p1 = sum(n * A_(p_[n]) * (n * tA).cos() for n in p_)
    assert qA * qA * p0 * p0 + p1 * p1 > 0          # (qP, P') nonzero at theta*: the quotient form applies
    Phi = -qA * abs(a0 * p1 - a1 * p0) / (4 * cA * (qA * qA * p0 * p0 + p1 * p1).sqrt())
    Hinf = arb(Phi.lower())
    HL2 = B1 / (2 * PI).sqrt()
    assert abs(Phi - arb(REV["D"][name]["Phi_theta_star"].strip("[]").split("+/-")[0])) < arb(10)**-6
    rowsE = {}
    for labH, Hl in (("H >= max Phi (REVIEW_T4_375 R2)", Hinf), ("H >= B1/sqrt(2pi) (T4-375)", HL2)):
        ec = {k_: Ecrit(bv, arb(0), g0, Hl, B0) for k_, bv in betas.items()}
        rg_, cap = capf(ELA, arb(0), g0, Hl, B0)
        rowsE[labH] = {"Ecrit_upper": {k_: float(x_.upper()) for k_, x_ in ec.items()},
                       "E_lower_exceeds_Ecrit": {k_: bool(ELA > x_) for k_, x_ in ec.items()},
                       "r_grad_at_E_lower": float(rg_.lower()), "cap_at_E_lower_upper": float(cap.upper()),
                       "cap_at_E_lower_below_ceiling": {k_: bool(cap < A_(bv)) for k_, bv in betas.items()},
                       "directed": {"Ecrit_up": {k_: directed(x_, True, 7, True) for k_, x_ in ec.items()},
                                    "r_grad_down": directed(rg_, False, 8, True), "cap_up": directed(cap, True)}}
    main = rowsE["H >= max Phi (REVIEW_T4_375 R2)"]
    assert all(main["E_lower_exceeds_Ecrit"].values()) and all(main["cap_at_E_lower_below_ceiling"].values())
    OUT["B"][name] = {"B0": B0.str(15), "B1": B1.str(15), "H_inf_lower": Hinf.str(15), "g0": g0.str(15), "rows": rowsE}
    for labH, rw in rowsE.items():
        print("(B) %s, %s, V = 0, G = Theta'(0): Ecrit <= %s; E_lower > Ecrit: %s; at E = E_lower r_grad >= %s,"
              " cap <= %s, below each ceiling: %s (outward-rounded decimals)"
              % (name, labH, ", ".join("%s %s" % (k_, x_) for k_, x_ in rw["directed"]["Ecrit_up"].items()),
                 rw["E_lower_exceeds_Ecrit"], rw["directed"]["r_grad_down"], rw["directed"]["cap_up"],
                 rw["cap_at_E_lower_below_ceiling"]))

# =============================== (C) FLOAT ===============================
mp.mp.dps = 30
qf = float(qn)
Qf = -qf
Cf = 1 / (Qf * ((qf + 2)**2 - 1))
etaf = lambda t_: t_ * (1 + t_)**(qn - 1) / (-qn)


def Uhom(t_):
    c1, s1 = np.cos(t_), np.sin(t_)
    k_ = Cf * (qf + 1)                                # C (p - 1)
    return np.array([k_ * c1 * (c1 * c1 + qf * s1 * s1), -k_ * s1 * (s1 * s1 + qf * c1 * c1)])


def polar_U(av, ap, app, rv, tv):                     # U = (v_xy, -v_xx) for v = a(r) sin(theta)
    vr, vt, vrr = ap * np.sin(tv), av * np.cos(tv), app * np.sin(tv)
    vrt, vtt = ap * np.cos(tv), -av * np.sin(tv)
    c1, s1 = np.cos(tv), np.sin(tv)
    vxx = c1 * c1 * vrr + s1 * s1 * (vr / rv + vtt / rv**2) - 2 * s1 * c1 * (vrt / rv - vt / rv**2)
    vxy = s1 * c1 * (vrr - vr / rv - vtt / rv**2) + (c1 * c1 - s1 * s1) * (vrt / rv - vt / rv**2)
    return np.array([vxy, -vxx])


def tilde(rv):                                        # a~, a~', a~'' at r (the non-dipole part of a)
    rv = mp.mpf(rv)
    pts = [rv, 2 * rv, 10 * rv, 100 * rv, mp.inf]
    T_ = mp.quad(lambda t_: t_**2 * etaf(t_), pts)
    J_ = mp.quad(etaf, pts)
    return [float(z_) for z_ in ((T_ / rv - rv * J_) / 2, -(T_ / rv**2 + J_) / 2, T_ / rv**3 + etaf(rv))]


def full_a(rv):                                       # a, a', a'' with the dipole part
    at_, ap_, app_ = tilde(rv)
    Iinf = float(Iinf_q)
    return at_ - Iinf / (2 * rv), ap_ + Iinf / (2 * rv**2), app_ - Iinf / rv**3


# (C1) direct principal-value quadrature: U[h](X) = (0, -h(X)/2) + int_0^inf (ds/s) int dpsi (-sin 2psi, cos 2psi)/(2 pi) h(X + s e_psi)
def hfun(Y1, Y2):
    return Y2 * (1 + np.hypot(Y1, Y2))**(qf - 1) / Qf


def U_direct(X, npsi=8192, nleg=600):
    from numpy.polynomial.legendre import leggauss
    gx, gw = leggauss(nleg)
    rv = float(np.hypot(*X))
    psi = 2 * np.pi * (np.arange(npsi) + 0.5) / npsi
    wv = np.stack([-np.sin(2 * psi), np.cos(2 * psi)]) / npsi        # (1/2pi) * (2pi/N)
    tot = np.zeros(2)
    for lo, hi in ((0, rv / 2), (rv / 2, rv), (rv, 1.5 * rv), (1.5 * rv, 2 * rv)):
        sv = (hi - lo) / 2 * gx + (hi + lo) / 2
        ww = (hi - lo) / 2 * gw
        for s1, w1 in zip(sv, ww):
            tot += w1 / s1 * (wv @ hfun(X[0] + s1 * np.cos(psi), X[1] + s1 * np.sin(psi)))
    # s = 2r/tau, ds/s = dtau/tau, tau in (0, 1)
    tv_ = (gx + 1) / 2
    tw = gw / 2
    for t1, w1 in zip(tv_, tw):
        s1 = 2 * rv / t1
        tot += w1 / t1 * (wv @ hfun(X[0] + s1 * np.cos(psi), X[1] + s1 * np.sin(psi)))
    return tot + np.array([0.0, -hfun(X[0], X[1]) / 2])


rowsC1 = []
for rv in (0.7, 3.0, 12.0):
    for tv in (0.35, np.pi / 4, 1.2):
        X = np.array([rv * np.cos(tv), rv * np.sin(tv)])
        Ud_ = U_direct(X)
        Ud2 = U_direct(X, npsi=16384, nleg=900)
        Ug = polar_U(*full_a(rv), rv, tv)
        rowsC1.append({"r": rv, "theta": tv, "direct": Ud_.tolist(), "green": Ug.tolist(),
                       "abs_diff": float(np.max(np.abs(Ud2 - Ug))), "rel_diff": float(np.max(np.abs(Ud2 - Ug)) / np.max(np.abs(Ug))),
                       "refinement_change": float(np.max(np.abs(Ud2 - Ud_)))})
errC1 = max(rw["rel_diff"] for rw in rowsC1)
print("(C1) Green-formula velocity vs direct PV kernel quadrature at r = 0.7, 3, 12 and theta = 0.35, pi/4, 1.2: max relative"
      " difference %.2e (refinement change at most %.1e)" % (errC1, max(rw["refinement_change"] for rw in rowsC1)))
# (C2) convergence to U_hom
tg = np.linspace(0, np.pi / 2, 91)
rowsC2 = []
for rv in (2.0, 5.0, 10.0, 1e2, 1e3, 1e4, 1e6, 1e8):
    av = tilde(rv)
    vals = np.array([polar_U(*av, rv, t_) * rv**Qf for t_ in tg])
    hom = np.array([Uhom(t_) for t_ in tg])
    rowsC2.append({"r": rv, "max_err": float(np.max(np.linalg.norm(vals - hom, axis=1))),
                   "r_times_max_err": float(rv * np.max(np.linalg.norm(vals - hom, axis=1))),
                   "max_modulus": float(np.max(np.linalg.norm(vals, axis=1))),
                   "argmax_theta": float(tg[np.argmax(np.linalg.norm(vals, axis=1))])})
    print("(C2) r = %.0e: max_theta |r^-q (U[h] + DK M) - U_hom| = %.3e (times r: %.4f); max_theta r^-q |U[h] + DK M| = %.6f at"
          " theta = %.3f" % (rv, rowsC2[-1]["max_err"], rowsC2[-1]["r_times_max_err"], rowsC2[-1]["max_modulus"],
                             rowsC2[-1]["argmax_theta"]))
hom_max = float(np.max(np.linalg.norm(np.array([Uhom(t_) for t_ in np.linspace(0, np.pi / 2, 100001)]), axis=1)))
assert abs(hom_max - float(E_lower)) < 1e-9 and errC1 < 1e-6
# (C3) sup over r >= 2 and theta (FLOAT)
best = (0.0, None, None)
tg3 = np.linspace(0, np.pi / 2, 721)
for lr in np.linspace(np.log(2), np.log(1e8), 241):
    rv = float(np.exp(lr))
    av = tilde(rv)
    md = np.linalg.norm(np.array([polar_U(*av, rv, t_) for t_ in tg3]), axis=1) * rv**Qf
    j = int(np.argmax(md))
    if md[j] > best[0]:
        best = (float(md[j]), rv, float(tg3[j]))
OUT["C"] = {"C1_rows": rowsC1, "C1_max_rel_diff": errC1, "C2_rows": rowsC2, "U_hom_grid_max": hom_max,
            "C3_sup_r>=2": {"value": best[0], "r": best[1], "theta": best[2]}}
print("(C3) FLOAT sup over r in [2, 1e8] and theta of r^-q |U[h] + DK M| (H_q(h) <= 1): %.6f at r = %.4g, theta = %.4f;"
      " the limit value is E_lower = %.6f" % (best[0], best[1], best[2], float(E_lower)))
OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t2_E_lower_results.json").write_text(json.dumps(OUT, indent=1, default=str))
print("done, %.1f s" % (time.monotonic() - T0))
