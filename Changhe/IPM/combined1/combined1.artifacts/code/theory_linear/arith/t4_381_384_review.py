"""Independent review of T4-381 (c1-t4 research/universal_velocity_lower/PROOF.md, sha256 ca0e008a...0b30b9) and
T4-384 (research/normalized_velocity_lower/PROOF.md, sha256 a18ad405...3c083c): the universal lower bound for the
velocity remainder constant of T4-335 (1), its normalized small-L2 extension, and the retained-delta cap of (CI)
(reviews/REVIEW_T4_381_384.md).

Run from artifacts/:  python3 -B -u arith/t4_381_384_review.py
Needs sympy, mpmath, python-flint (Arb). Reads data/t4_375_review_results.json (theta* of its part (D)), c1-t4's
endpoint data and the two result.json files in place (hashes of c1-t4's files asserted; of the first file only its
theta* values are asserted, see the comment at its load). Executes no c1-t4 code.
Decimal displays of Arb balls in (C) are rounded outward: lower bounds (r0, Etest/H_upper) toward -infinity, upper
bounds (caps, Ecrit upper ends, H_q and L2 upper bounds) toward +infinity, from the exact ball endpoints (revision 2,
after T4-396; version 1 printed nearest-rounded floats of the endpoints).

Notation: a = -q > 3, delta = a - 3, alpha = -2q - 2, Etest = (a - 1)/(2 a (a - 3)) (= E_lower of arith/t2_E_lower.py).
Parts:
  (A) sympy, T4-381: the moment (3) as a Beta value; the homogeneous velocity (6) against the polar form of
      arith/t2_E_lower.py; |W|^2 = 1 + (q-1)(q+3) s^2 c^2 up to the factor, maximal at pi/4 with value Etest^2; the
      Green coefficient of (5); the retained-delta integral (8) and its closed form; the pointwise positive-part bound.
  (B) sympy, T4-384: the gradient components of f_R, the two signed differences behind |R^2 - a r^2| <= a(R^2 + r^2),
      the Cauchy-Schwarz gap, the scaling identity, m_R and ||f_1||_2^2 as Beta values, sup|eta'| = 4/e, the contact
      identity c[g] = -g_y(0)/4 + (1/pi) PV int sin(3 theta) g/r^3 by three routes (integration by parts on the PV
      kernel; the regular mode-1 ODE solution near 0; exact Fourier integrals for y e^(-r^2) and y^3 e^(-r^2)).
  (C) Arb at q = q*: Etest and the moment against c1-t4's strings; r0, the crude and retained-delta caps (7), (8)
      with H0 = Phi(theta*) (REVIEW_T4_375 R2 = T4-380), B = B0, G = Theta'(0), v0 in {0, |U_lead(0)|}, against
      c1-t4's result.json; Ecrit at the four named radii including the fixed sharpw radius 1351/1024000000; the
      T4-384 sequence bounds H_q(k_R) <= C_R + R^(-a-1) K/a, ||k_R||_2 and Etest/H_upper against c1-t4's values.
  (D) FLOAT: r^(-q)|U[k_R] + DK M| at theta = pi/4 from the Green formula for R = 1, 10 and r up to 1e8; the sup over
      theta of the weighted gradient and amplitude of f_R on a radial grid against C_R (the gradient sup over theta is
      max(|F'|, F/r); a first version used sqrt(F'^2 + (F/r)^2), which overestimates by up to sqrt 2 and so exceeded
      C_R at R = 10; that was an error of this check, not of T4-384).
Output: logs/t4_381_384_review.log, data/t4_381_384_review_results.json.
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
T4R = Path("RUN_ROOT/theory_audit_T4/research")
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(T4R / "universal_velocity_lower/PROOF.md") == "ca0e008a1bfb7868fb1242af0a0eeb1897552a574dc27f7b1a9ad36e1a0b30b9"
assert sha(T4R / "universal_velocity_lower/verification/result.json") == "0b3e6350ea9f4183c4020b1ad5af3e43ac2c45408e86b831e9d92a05f95ca03d"
assert sha(T4R / "normalized_velocity_lower/PROOF.md") == "a18ad405134e554e0613f6764ce566b8a3b458295b1445067fa3ad415c41083c"
assert sha(T4R / "normalized_velocity_lower/verification/result.json") == "eedbfd683b7ebca07031071ed25376375acd2e7c4098014a6dfc0760aeb70345"
ep_sha = {"007": "bcd0e49225807ba313dfb86ec386b4d3d3411bdcb233072d5047e84cc27ec58b",
          "013": "3a2cf49c387db2fd95e7174a2b5f58103201857f01ba875e391b88714ab96471",
          "014": "8168bf8b326124bc720cc992a5fbe0300d9b1250eb9f4e862b0f2ce38b53b6ce"}
for nm, h_ in ep_sha.items():
    assert sha(T4R / f"endpoint_gradient_budget/data/{nm}_endpoint.json") == h_
    assert sha(T4R / f"universal_velocity_lower/data/{nm}_endpoint.json") == h_
R381 = json.loads((T4R / "universal_velocity_lower/verification/result.json").read_text())
R384 = json.loads((T4R / "normalized_velocity_lower/verification/result.json").read_text())
P381 = json.loads((T4R / "universal_velocity_lower/data/parameters.json").read_text())
REV = json.loads((HERE / "data/t4_375_review_results.json").read_text())
# The only content used from that file is theta* of its part (D); each value is asserted below to equal T4-381's
# parameter angle exactly. The whole-file hash is printed, not asserted: the file records its own run time, so its
# hash changes on every rerun of arith/t4_375_review.py.
print("inputs: t4_375_review_results.json sha256 %s (printed; its theta* values are asserted in (C))"
      % sha(HERE / "data/t4_375_review_results.json"))

# =============================== (A) sympy, T4-381 ===============================
a, r, s, R, al, dl, u = S.symbols("a r s R alpha delta u", positive=True)
x, y, th = S.symbols("x y theta", real=True)
q = -a
c_, s_ = S.cos(th), S.sin(th)
A = {}
# (3): int_0^inf r^3 (1+r)^(q-1) dr = B(4, a - 3); m = pi B(4, a-3)/a = 6 pi/(a^2 (a-1)(a-2)(a-3))
A["moment_beta"] = S.simplify(S.gammasimp(S.gamma(4) * S.gamma(a - 3) / S.gamma(a + 1)) - 6 / (a * (a - 1) * (a - 2) * (a - 3))) == 0
# (6) against the polar form C (p-1) r^q (c (c^2 + q s^2), -s (s^2 + q c^2)), C = 1/(a (p^2 - 1)), p = q + 2
Cp1 = (q + 1) / (a * ((q + 2)**2 - 1))
W381 = (c_ * (1 + (q - 1) * s_**2) / (a * (q + 3)), -s_ * (1 + (q - 1) * c_**2) / (a * (q + 3)))
Wmine = (Cp1 * c_ * (c_**2 + q * s_**2), -Cp1 * s_ * (s_**2 + q * c_**2))
A["W_equals_t2_E_lower_form"] = all(S.simplify(S.expand(W381[i] - Wmine[i]).subs(c_**2, 1 - s_**2)) == 0 for i in (0, 1))
nW2 = S.expand(W381[0]**2 + W381[1]**2)
A["norm_square"] = S.simplify(nW2 * (a * (q + 3))**2 - (1 + (q - 1) * (q + 3) * s_**2 * c_**2)) == 0
A["value_at_pi/4"] = S.simplify(nW2.subs(th, S.pi / 4) - ((a - 1) / (2 * a * (a - 3)))**2) == 0
A["(q-1)(q+3)>0 for a>3"] = S.simplify(S.expand((q - 1) * (q + 3)) - ((a + 1) * (a - 3))) == 0
# Green coefficient of (5): f = r^q/a gives T = r^(q+3)/(a(a-3)), J = r^(q+1)/(a(a-1)), (T/r - r J)/2
Th, Jh = r**(q + 3) / (a * (a - 3)), r**(q + 1) / (a * (a - 1))
A["green_T"] = S.simplify(-S.diff(Th, r) - r**2 * r**q / a) == 0
A["green_J"] = S.simplify(-S.diff(Jh, r) - r**q / a) == 0
A["green_coefficient"] = S.simplify(S.powsimp((Th / r - r * Jh) / 2 - r**(q + 2) / (a * (q + 1) * (q + 3)), force=True)) == 0
# (8): int_1^inf s^(-alpha-1) (1 - s^-delta)^2 ds = 1/alpha - 2/(alpha+delta) + 1/(alpha+2delta) = 2 delta^2/(...)
I8 = S.integrate(S.expand(s**(-al - 1) * (1 - s**(-dl))**2), (s, 1, S.oo), conds="none")
A["delta_integral"] = S.simplify(I8 - (1 / al - 2 / (al + dl) + 1 / (al + 2 * dl))) == 0
A["delta_closed_form"] = S.simplify(1 / al - 2 / (al + dl) + 1 / (al + 2 * dl) - 2 * dl**2 / (al * (al + dl) * (al + 2 * dl))) == 0
r0 = S.Symbol("r0", positive=True)
A["substitution_r=r0 s"] = S.simplify(S.powsimp((r0 * s)**(2 * q + 1) * r0 - r0**(2 * q + 2) * s**(2 * q + 1), force=True)) == 0
# positive-part bound: if sqrt(2pi) e >= B (r0/r)^delta then [B - sqrt(2pi) e]_+ <= B [1 - (r0/r)^delta]_+ (monotone)
A["alpha=-2q-2>0_and_2q+1=-alpha-1"] = S.simplify((2 * q + 1) - (-(-2 * q - 2) - 1)) == 0
OUT["A"] = {k_: bool(v_) for k_, v_ in A.items()}
assert all(A.values()), A
print("(A) T4-381 exact checks pass:", json.dumps(OUT["A"]))

# =============================== (B) sympy, T4-384 ===============================
B_ = {}
F = r * (R**2 + r**2)**(-(a + 1) / 2) / a
B_["radial_gradient"] = S.simplify(S.diff(F, r) - (R**2 - a * r**2) * (R**2 + r**2)**(-(a + 3) / 2) / a) == 0
B_["angular_gradient"] = S.simplify(F / r - (R**2 + r**2)**(-(a + 1) / 2) / a) == 0
B_["signed_upper_pos"] = S.expand(a * (R**2 + r**2) - (R**2 - a * r**2) - ((a - 1) * R**2 + 2 * a * r**2)) == 0
B_["signed_upper_neg"] = S.expand(a * (R**2 + r**2) + (R**2 - a * r**2) - (a + 1) * R**2) == 0
B_["cauchy_schwarz_gap"] = S.simplify((1 + R**-2) * (R**2 + r**2) - (1 + r)**2 - (R - r / R)**2) == 0
fR = y * (R**2 + x**2 + y**2)**(-(a + 1) / 2) / a
f1 = (y / R) * (1 + (x**2 + y**2) / R**2)**(-(a + 1) / 2) / a
B_["scaling_f_R=R^-a f_1(X/R)"] = S.simplify(S.powsimp(S.expand_power_base(R**(-a) * f1 / fR, force=True), force=True)) == 1
# m_R = (pi/a) int_0^inf r^3 (R^2 + r^2)^(-(a+1)/2) dr = (pi/a)(R^(3-a)/2) B(2, (a-3)/2)
B_["m_R_beta"] = S.simplify(S.expand_func((S.pi / a) * S.gamma(2) * S.gamma((a - 3) / 2) / S.gamma((a + 1) / 2) / 2
                                          - 2 * S.pi / (a * (a - 1) * (a - 3)))) == 0
B_["m_R_substitution"] = S.simplify(S.powsimp(S.expand_power_base(
    (R * S.sqrt(u))**3 * (R**2 * (1 + u))**(-(a + 1) / 2) * R / (2 * S.sqrt(u))
    - R**(3 - a) * u * (1 + u)**(-(a + 1) / 2) / 2, force=True), force=True)) == 0
# ||f_1||_2^2 = (pi/a^2) int r^3 (1 + r^2)^(-a-1) dr = pi B(2, a - 1)/(2 a^2) = pi/(2 a^3 (a - 1))
B_["f1_L2_beta"] = S.simplify(S.gammasimp(S.pi * S.gamma(2) * S.gamma(a - 1) / S.gamma(a + 1) / (2 * a**2)) - S.pi / (2 * a**3 * (a - 1))) == 0
# eta(s) = exp(1 - 1/(1-s)): eta(0) = 1, |eta'| = U^2 e^(1-U) with U = 1/(1-s) >= 1, maximal 4/e at U = 2
sv, U = S.symbols("s_ U", positive=True)
eta = S.exp(1 - 1 / (1 - sv))
B_["eta(0)=1"] = eta.subs(sv, 0) == 1
B_["eta_prime"] = S.simplify(S.diff(eta, sv) + eta / (1 - sv)**2) == 0
B_["eta_prime_max_4/e"] = (S.solve(S.diff(U**2 * S.exp(1 - U), U), U) == [2]
                           and S.simplify((U**2 * S.exp(1 - U)).subs(U, 2) - 4 / S.E) == 0)
# contact identity, route 1: U2 = -g/2 + (1/2pi) PV int cos(2 phi)/|z|^2 g, z = X - Y. d_y moves to the kernel:
# d_{z2}(cos 2phi/|z|^2) = -2 sin 3phi/|z|^3, and the inner-circle boundary term is (pi/2) g_y(X)
z1, z2 = S.symbols("z1 z2", real=True)
rz = S.sqrt(z1**2 + z2**2)
B_["kernel_derivative"] = S.simplify(S.diff((z1**2 - z2**2) / rz**4, z2) + 2 * (3 * z1**2 * z2 - z2**3) / rz**6) == 0
gx, gy = S.symbols("g_x g_y", real=True)
bdry = S.integrate(S.cos(2 * th) * S.sin(th) * (-(S.cos(th) * gx + S.sin(th) * gy)), (th, 0, 2 * S.pi))
B_["boundary_term_pi/2_g_y"] = S.simplify(bdry - S.pi / 2 * gy) == 0 and S.integrate(S.cos(2 * th) * S.sin(th), (th, 0, 2 * S.pi)) == 0
B_["total_coefficient_-1/4"] = S.simplify(-S.Rational(1, 2) + (S.pi / 2) / (2 * S.pi) + S.Rational(1, 4)) == 0
B_["sign_at_origin"] = S.simplify(S.sin(3 * (th + S.pi)) + S.sin(3 * th)) == 0
B_["mode1_PV_term_zero"] = S.integrate(S.sin(3 * th) * S.sin(th), (th, 0, 2 * S.pi)) == 0
# route 2: smooth mode-1 g = F(r) sin(theta), F = F1 r + F3 r^3 + ...: the regular potential a = A1 r + A3 r^3 + ...
# solves a'' + a'/r - a/r^2 = F, so A3 = F1/8; psi = A1 y + A3 r^2 y + ..., and c = -psi_xxy(0) = -2 A3 = -F1/4
F1, F3, A1s, A3s, A5s = S.symbols("F1 F3 A1 A3 A5", real=True)
aser = A1s * r + A3s * r**3 + A5s * r**5
ode = S.expand(S.diff(aser, r, 2) + S.diff(aser, r) / r - aser / r**2 - (F1 * r + F3 * r**3))
sol = S.solve([ode.coeff(r, 1), ode.coeff(r, 3)], [A3s, A5s])
psi = A1s * y + sol[A3s] * (x**2 + y**2) * y
B_["ode_route_c=-F1/4"] = S.simplify(-S.diff(psi, x, 2, y).subs({x: 0, y: 0}) + F1 / 4) == 0
# route 3: exact Fourier. d_y U2(0) = -(1/4pi^2) int (xi1^2/|xi|^2) (i xi2) ghat(xi) dxi, ghat = int g e^{-i X.xi}
k1, k2, rho, ph = S.symbols("k1 k2 rho phi", real=True)
G0 = S.pi * S.exp(-(k1**2 + k2**2) / 4)                       # Fourier transform of e^{-r^2}


def dyU2_origin(order):                                         # g = y^order e^{-r^2}, ghat = (i d_k2)^order G0
    gh = G0
    for _ in range(order):
        gh = S.I * S.diff(gh, k2)
    integrand = S.simplify((k1**2 / (k1**2 + k2**2)) * S.I * k2 * gh)
    pol_ = S.simplify(integrand.subs({k1: rho * S.cos(ph), k2: rho * S.sin(ph)}) * rho)
    return S.simplify(-S.integrate(S.integrate(S.expand(pol_), (ph, 0, 2 * S.pi)), (rho, 0, S.oo)) / (4 * S.pi**2))


c_y1, c_y3 = dyU2_origin(1), dyU2_origin(3)
# identity: y e^{-r^2}: g_y(0) = 1, mode 1 -> -1/4.  y^3 e^{-r^2} = r^3 e^{-r^2}(3 sin - sin 3theta)/4: g_y(0) = 0 and
# (1/pi) int sin3 g / r^3 = (1/pi)(-pi/4) int_0^inf r e^{-r^2} dr = -1/8
pv3 = S.integrate(S.integrate(S.sin(3 * th) * r**3 * S.exp(-r**2) * (3 * S.sin(th) - S.sin(3 * th)) / 4 / r**3 * r,
                              (th, 0, 2 * S.pi)), (r, 0, S.oo)) / S.pi
B_["fourier_y_e^-r2"] = S.simplify(c_y1 + S.Rational(1, 4)) == 0
B_["fourier_y^3_e^-r2"] = S.simplify(c_y3 - pv3) == 0 and S.simplify(pv3 + S.Rational(1, 8)) == 0
B_["c[f_R]"] = S.simplify(-S.diff(fR, y).subs({x: 0, y: 0}) / 4 + R**(-a - 1) / (4 * a)) == 0
OUT["B"] = {k_: bool(v_) for k_, v_ in B_.items()}
OUT["B"]["fourier_values"] = [str(c_y1), str(c_y3), str(pv3)]
assert all(B_.values()), B_
print("(B) T4-384 exact checks pass:", json.dumps(OUT["B"]))

# =============================== (C) Arb at q* ===============================
ctx.prec = 256
PI = arb.pi()
A_ = lambda fr_: arb(fr_.numerator) / fr_.denominator
cF = Fr(4076476460239181, 2**51)
qF = 1 / cF - 4
aF = -qF
dF = aF - 3
assert str(qF) == R381["q"] and str(cF) == P381["c"]
Etest = (aF - 1) / (2 * aF * (aF - 3))
assert str(Etest) == R381["Etest_exact"]
qA, aA, dA, cA = A_(qF), A_(aF), A_(dF), A_(cF)
alA = -2 * qA - 2
DdA = A_(1 - cF * (qF - dF))
EtA = A_(Etest)


def parse(sv_):
    sv_ = sv_.strip()
    if sv_.startswith("["):
        m_, r_ = sv_.strip("[]").split("+/-")
        return arb(m_.strip(), r_.strip())
    return arb(sv_)


def agree(xv, sv_, rel=arb(10)**-60):
    yv = parse(sv_)
    return bool(abs(xv - yv) < xv.rad() + yv.rad() + rel * abs(xv))


mom = 6 * PI / (aA**2 * (aA - 1) * (aA - 2) * (aA - 3))
shape = (2 * dA**2 / ((alA + dA) * (alA + 2 * dA))).sqrt()
OUT["C"] = {"Etest_exact": str(Etest), "Etest": EtA.str(25), "moment": mom.str(25), "shape_factor": shape.str(25),
            "agree": {"Etest": agree(EtA, R381["Etest"]), "moment": agree(mom, R381["moment_exact"]),
                      "shape_factor": agree(shape, R381["cap_shape_improvement_factor"])}}
betas = {k_: Fr(v_) for k_, v_ in P381["betas"].items()}
s22 = alA.sqrt()


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


def Ecrit(beta, V, G, Hl, B0):
    Y = (B0 / (A_(beta) * s22))**(dA / (-qA - 1))
    return (DdA * B0 * Y / ((2 * PI).sqrt() * Hl) - V) / G


pE = 1 / cA + 2
for name in ("007", "013", "014"):
    ep = json.loads((T4R / f"endpoint_gradient_budget/data/{name}_endpoint.json").read_text())
    a_ = {int(k_): Fr(v_) for k_, v_ in ep["F12"].items()}
    p_ = {int(k_): Fr(v_) for k_, v_ in ep["P"].items()}
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    ns = sorted(set(a_) | set(p_))
    get = lambda d_, n: d_.get(n, Fr(0))
    X0 = sum(get(a_, n)**2 for n in ns) - sum(get(a_, n) * get(p_, n) for n in ns)**2 / sum(get(p_, n)**2 for n in ns)
    B0 = (PI * A_(X0)).sqrt() / (4 * cA)
    g0 = A_(sum(n * b_ for n, b_ in th0.items()))
    ang = Fr(P381["angles"][name])
    assert ang == Fr(REV["D"][name]["theta_star"])
    tA = A_(ang)
    a0 = sum(A_(a_[n]) * (n * tA).sin() for n in a_)
    a1 = sum(n * A_(a_[n]) * (n * tA).cos() for n in a_)
    p0 = sum(A_(p_[n]) * (n * tA).sin() for n in p_)
    p1 = sum(n * A_(p_[n]) * (n * tA).cos() for n in p_)
    den = (qA * qA * p0 * p0 + p1 * p1).sqrt()
    assert den > 0                                   # (qP, P') is nonzero at theta*, so the quotient form applies
    Phi = -qA * abs(a0 * p1 - a1 * p0) / (4 * cA * den)
    H0 = arb(Phi.lower())
    V0 = (pE - 1) * abs(sum(n * A_(b_) / (pE * pE - n * n) for n, b_ in th0.items()))
    row = next(rw for rw in R381["rows"] if rw["candidate"] == name)
    res = {"H0": Phi.str(20), "H_point_agree": agree(Phi, row["H_point"], rel=arb(10)**-50), "B0": B0.str(20),
           "g0": g0.str(15), "V0": V0.str(15), "versions": {}}
    for labV, V, key in (("v0 = 0", arb(0), "without_velocity_asymptotic"),
                         ("v0 = |U_lead(0)|", arb(V0.lower()), "with_velocity_asymptotic")):
        rg = ((2 * PI).sqrt() * H0 * (V + EtA * g0) / (DdA * B0))**(1 / dA)
        crude = B0 * rg**(qA + 1) / s22
        dcap = B0 * rg**(qA + 1) * (2 * dA**2 / (alA * (alA + dA) * (alA + 2 * dA))).sqrt()
        dcap2 = B0 * rg**(qA + 1) * (1 / alA - 2 / (alA + dA) + 1 / (alA + 2 * dA)).sqrt()
        rv = row["versions"][key]
        tol = arb(10)**-40                           # H0 here is the lower end of the ball, theirs the midpoint
        ec = {k_: Ecrit(bv, V, g0, H0, B0) for k_, bv in betas.items()}
        res["versions"][labV] = {
            "r0": rg.str(15), "crude_cap": crude.str(15), "delta_cap": dcap.str(15),
            "agree_r0_crude_delta": [agree(rg, rv["r0"], tol), agree(crude, rv["crude_cap"], tol), agree(dcap, rv["delta_shape_cap"], tol)],
            "two_forms_of_(8)_overlap": bool(abs(dcap - dcap2) <= dcap.rad() + dcap2.rad() + arb(10)**-70),
            "crude_below": {k_: bool(crude < A_(bv)) for k_, bv in betas.items()},
            "delta_below": {k_: bool(dcap < A_(bv)) for k_, bv in betas.items()},
            "crude_upper": float(crude.upper()), "delta_upper": float(dcap.upper()), "r0_lower": float(rg.lower()),
            "Ecrit_upper": {k_: float(v_.upper()) for k_, v_ in ec.items()},
            "directed": {"r0_down": directed(rg, False, 8, True), "crude_up": directed(crude, True),
                         "delta_up": directed(dcap, True),
                         "Ecrit_up": {k_: directed(v_, True, 7, True) for k_, v_ in ec.items()}},
            "stated_bounds_Arb": {"delta_cap_below_" + ("1.42081e-7" if key.startswith("without") else "1.12372e-7"):
                                  bool(dcap < (arb(142081) / arb(10)**12 if key.startswith("without") else arb(112372) / arb(10)**12)),
                                  "delta_cap_below_" + ("1.421e-7" if key.startswith("without") else "1.124e-7"):
                                  bool(dcap < (arb(1421) / arb(10)**10 if key.startswith("without") else arb(1124) / arb(10)**10))},
            "Etest_exceeds_Ecrit": {k_: bool(EtA > v_) for k_, v_ in ec.items()}}
        assert all(res["versions"][labV]["agree_r0_crude_delta"]) and all(res["versions"][labV]["crude_below"].values())
        assert all(res["versions"][labV]["Etest_exceeds_Ecrit"].values())
        assert all(res["versions"][labV]["stated_bounds_Arb"].values())
        if key.startswith("without"):
            res["Ecrit_fixed_sharpw_below_0.785064_Arb"] = bool(ec["fixed_sharpw_ball"] < arb(785064) / arb(10)**6)
            assert res["Ecrit_fixed_sharpw_below_0.785064_Arb"]
    assert res["H_point_agree"]
    res["Ecrit_fixed_sharpw_below_0.785064"] = res["versions"]["v0 = 0"]["Ecrit_upper"]["fixed_sharpw_ball"] < 0.785064
    OUT["C"][name] = res
    v0r = res["versions"]["v0 = 0"]
    d0 = v0r["directed"]
    print("(C) %s: H0 = %s (= T4-381 H_point), B0 = %s; v0 = 0: r0 >= %s, crude cap <= %s, delta cap <= %s;"
          " Ecrit <= %s; all equal c1-t4's values (outward-rounded decimals)"
          % (name, Phi.str(15), B0.str(12), d0["r0_down"], d0["crude_up"], d0["delta_up"],
             ", ".join("%s %s" % kv for kv in d0["Ecrit_up"].items())))
    v1r = res["versions"]["v0 = |U_lead(0)|"]
    d1 = v1r["directed"]
    print("    v0 = |U_lead(0)| = %s: r0 >= %s, crude cap <= %s, delta cap <= %s, Ecrit <= %s"
          % (V0.str(10), d1["r0_down"], d1["crude_up"], d1["delta_up"], ", ".join("%s %s" % kv for kv in d1["Ecrit_up"].items())))
print("(C) Etest = %s, moment = %s, shape factor = %s; agree with c1-t4: %s" % (EtA.str(20), mom.str(15), shape.str(15),
                                                                                OUT["C"]["agree"]))
assert all(OUT["C"]["agree"].values())
# T4-384 sequence: H_q(k_R) <= C_R + R^(-a-1) K/a with K = 5 * 2^(a+1) >= H_q(b); ||k_R||_2 <= R^(1-a)||f_1|| + R^(-a-1)||b||/a
Kb = 5 * arb(2)**(aA + 1)
nf1 = (PI / (2 * aA**3 * (aA - 1))).sqrt()
nb = PI.sqrt() / 2                                   # |b| <= |y| on the unit disk: ||b||_2^2 <= int_disk y^2 = pi/4
seq = []
for rw in R384["sequence"]:
    RR = arb(rw["R"])
    Hu = (1 + RR**-2)**((aA + 1) / 2) + RR**(-aA - 1) * Kb / aA
    L2u = RR**(1 - aA) * nf1 + RR**(-aA - 1) * nb / aA
    nE = EtA / Hu
    seq.append({"R": rw["R"], "H_upper": Hu.str(15), "L2_upper": L2u.str(15), "necessary_E": nE.str(15),
                "agree": [agree(Hu, rw["H_upper"], arb(10)**-60), agree(L2u, rw["L2_upper"], arb(10)**-60),
                          agree(nE, rw["necessary_E"], arb(10)**-60)],
                "L2_below_fixed_sharpw": bool(L2u < A_(betas["fixed_sharpw_ball"])),
                "directed": {"H_up": directed(Hu, True, 9, True), "L2_up": directed(L2u, True, 5),
                             "necessary_E_down": directed(nE, False, 8, True)}})
OUT["C"]["T4_384_sequence"] = seq
assert all(all(rw["agree"]) for rw in seq)
print("(C) T4-384 sequence (R, H_q upper, L2 upper, Etest/H_upper, agree with c1-t4, L2 below 1351/1024000000):")
for rw in seq:
    print("    R = %-6s %s  %s  %s  %s  %s" % (rw["R"], rw["H_upper"], rw["L2_upper"], rw["necessary_E"], rw["agree"],
                                            rw["L2_below_fixed_sharpw"]))
    print("           outward decimals: H_q(k_R) <= %s, ||k_R||_2 <= %s, Etest/H_upper >= %s"
          % (rw["directed"]["H_up"], rw["directed"]["L2_up"], rw["directed"]["necessary_E_down"]))

# =============================== (D) FLOAT ===============================
mp.mp.dps = 30
qn = mp.mpf(1) / (mp.mpf(4076476460239181) / 2**51) - 4
an = -qn
Et = (an - 1) / (2 * an * (an - 3))


def Uk_scaled(Rv, rv, tv=mp.pi / 4):
    """r^-q |U[k_R] + DK M| at (r, theta) for r > 1 from the mode-1 Green formula (the bump b drops out for r > 1)."""
    Fv = lambda t_: t_ * (Rv**2 + t_**2)**(-(an + 1) / 2) / an
    pts = [rv, 2 * rv, 10 * rv, 100 * rv, mp.inf]
    T_ = mp.quad(lambda t_: t_**2 * Fv(t_), pts)
    J_ = mp.quad(Fv, pts)
    at_, ap_, app_ = (T_ / rv - rv * J_) / 2, -(T_ / rv**2 + J_) / 2, T_ / rv**3 + Fv(rv)
    vr, vt, vrr, vrt, vtt = ap_ * mp.sin(tv), at_ * mp.cos(tv), app_ * mp.sin(tv), ap_ * mp.cos(tv), -at_ * mp.sin(tv)
    c1, s1 = mp.cos(tv), mp.sin(tv)
    vxx = c1 * c1 * vrr + s1 * s1 * (vr / rv + vtt / rv**2) - 2 * s1 * c1 * (vrt / rv - vt / rv**2)
    vxy = s1 * c1 * (vrr - vr / rv - vtt / rv**2) + (c1 * c1 - s1 * s1) * (vrt / rv - vt / rv**2)
    return float(mp.sqrt(vxx**2 + vxy**2) * rv**an)


rowsD = []
for Rv in (1, 10):
    for rv in (2, 10, 1e2, 1e3, 1e4, 1e6, 1e8):
        if rv > Rv:
            rowsD.append({"R": Rv, "r": rv, "scaled": Uk_scaled(mp.mpf(Rv), mp.mpf(rv))})
OUT["D"] = {"rows": rowsD, "Etest": float(Et)}
print("(D) FLOAT r^-q |U[k_R] + DK M| at theta = pi/4 (limit Etest = %.10f):" % float(Et))
for rw in rowsD:
    print("    R = %-3d r = %-8.0e %.10f" % (rw["R"], rw["r"], rw["scaled"]))
assert abs(rowsD[-1]["scaled"] / float(Et) - 1) < 1e-6
gridD = []
for Rv in (1.0, 2.0, 10.0):
    rr = np.logspace(-3, 6, 20001)
    ff = (Rv**2 + rr**2)**(-(float(an) + 1) / 2) / float(an)
    rad = np.abs(Rv**2 - float(an) * rr**2) * (Rv**2 + rr**2)**(-(float(an) + 3) / 2) / float(an)
    # |grad f_R|^2 = F'^2 sin^2 + (F/r)^2 cos^2 with F = r ff, so the sup over theta is max(|F'|, F/r) = max(rad, ff)
    wg = (1 + rr)**(float(an) + 1) * np.maximum(rad, ff)
    wa = (1 + rr)**float(an) * rr * ff                             # amplitude part of H_q
    CR = (1 + Rv**-2)**((float(an) + 1) / 2)
    gridD.append({"R": Rv, "grid_max_weighted_gradient": float(wg.max()), "grid_max_weighted_amplitude": float(wa.max()),
                  "C_R": CR})
OUT["D"]["gradient_grid"] = gridD
print("(D) FLOAT sup over theta of the weighted gradient and amplitude of f_R on 20001 radii: %s"
      % "; ".join("R = %g: gradient max %.6f, amplitude max %.6f, C_R = %.6f" % (g_["R"], g_["grid_max_weighted_gradient"],
                                                                                g_["grid_max_weighted_amplitude"], g_["C_R"])
                  for g_ in gridD))
assert all(max(g_["grid_max_weighted_gradient"], g_["grid_max_weighted_amplitude"]) <= g_["C_R"] * (1 + 1e-12) for g_ in gridD)
OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_381_384_review_results.json").write_text(json.dumps(OUT, indent=1, default=str))
print("done, %.1f s" % (time.monotonic() - T0))
