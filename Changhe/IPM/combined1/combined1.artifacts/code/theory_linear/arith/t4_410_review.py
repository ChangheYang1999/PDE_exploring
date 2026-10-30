"""Independent review of T4-410 (c1-t4 research/two_weight_velocity_remainder/PROOF.md, sha256 asserted below): the
two-weight compensated velocity estimate (1), the remainder J (2), the coarse radius (4), the cutoff model error (5),
the inputs (7) and the conclusions (8), (9); and what (8) can give at the campaign radii (reviews/REVIEW_T4_410.md).

Run from artifacts/:  python3 -B -u arith/t4_410_review.py
Needs sympy, numpy, scipy, python-flint (arb). Reads c1-t4's PROOF, result.json, manifest and parameters, and the
T4-402 endpoint JSON files (hash-bound, read only; none of c1-t4's code is imported or executed), and this lane's
data/t4_375_review_results.json (Phi(theta*)); run arith/t4_375_review.py first.
Parts:
  (A) sympy, exact: the kernel as 1/(2 pi z^2) and its first and third directional derivatives; the five pieces of
      C_a as exact radial integrals with symbolic a; the near-field integral (3) and Lr/(4B) = k r^eps, 2B = L_a A r^a;
      the slope of J and max x exp(-x/2) = 2/e used for (4); the exterior Green coefficients for symbolic n and q,
      the first-sine tail and the dipole compensation; the Hessian size n(n+1) r^(-n-2) of r^-n sin(n theta) at
      rational points (n = 3, 5, ..., 21); the cutoff: C1 endpoints, max |r chi'| = 4/sqrt(3), 1 - chi factorization.
  (B) Arb: c1-t4's fixture (a = -4, q = -7/2, A = 1, D = 8, eta = 1/100) recomputed from the PROOF formulas.
      FLOAT: a quadrature check of (1) for one admissible g (mode 1, a = -4, q = -7/2) with the exact Green formula.
  (C) Arb: the campaign consequence. With (6) taken from T4-335 (7), eps <= delta. A rigorous lower bound
      J(R)/H >= Sigma_q (5/r_beta)^delta for every R0 >= 2, L0 <= R <= r_beta and admissible eps, against
      Ecrit = Kcrit/Phi (007, 013, 014; four targets); the same at c1-t4's campaign eps = 1/4; the structural bound
      J(R) >= 2^(-q) Sigma_q B0/sqrt(2 pi) for R <= r_grad against Kcrit = (D_delta r_beta^delta/g0) B0/sqrt(2 pi).
      FLOAT: the minimum over eps of (C_a + L_a)(5/r_beta)^eps on (0, delta] and on (0, q + 5), the eps range where it
      is below the (F2) room Ecrit - 583/1000, and the radius where Sigma_q (5/R)^delta reaches 0.0989.
Output: logs/t4_410_review.log, data/t4_410_review_results.json.
"""
import hashlib
import json
import math
import time
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
import sympy as S
from flint import arb, ctx
from scipy.integrate import quad

HERE = Path(__file__).resolve().parents[1]
SRC = Path("RUN_ROOT/theory_audit_T4/research/two_weight_velocity_remainder")
SRC402 = Path("RUN_ROOT/theory_audit_T4/research/profile_specific_velocity")
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(SRC / "PROOF.md") == "cd2e6f18fb4b9255503e988e220709cb258338a8b4829080910ca8a11797bde6"
assert sha(SRC / "verification/result.json") == "4763413e14e845a23a298d8e5ab8b712438cbac5cbdef00423f2fd5b2531276f"
assert sha(SRC / "data/manifest.json") == "d66245c1300ee2d75fc2e927af9d0dfac2850643887494e6b792e7d2e248ec0f"
assert sha(SRC / "data/parameters.json") == "20ee2362827c8a67f54edb7133622e2f70b88523c03f592789796e2ddc19be49"
MAN = json.loads((SRC / "data/manifest.json").read_text())
for k_, v_ in MAN["inputs"].items():
    assert sha(SRC / k_) == v_, k_
assert sha(SRC402 / "PROOF.md") == "a98e64b04a4ab8f8e46f311c028d55138e9483f761d84e140ed550066e5ab3d9"
MAN402 = json.loads((SRC402 / "data/manifest.json").read_text())
for k_, v_ in MAN402["inputs"].items():
    assert sha(SRC402 / k_) == v_, k_
RES = json.loads((SRC / "verification/result.json").read_text())
PAR = json.loads((SRC / "data/parameters.json").read_text())
OUT["inputs"] = {"PROOF": sha(SRC / "PROOF.md"), "result": sha(SRC / "verification/result.json"),
                 "manifest": sha(SRC / "data/manifest.json"), "parameters": sha(SRC / "data/parameters.json"),
                 **MAN["inputs"], "402/PROOF": sha(SRC402 / "PROOF.md"), "402/manifest": sha(SRC402 / "data/manifest.json"),
                 **{"402/" + k_: v_ for k_, v_ in MAN402["inputs"].items()}}

# =============================== (A) sympy, exact ===============================
A_ = {}
x, y, u1, u2 = S.symbols("x y u1 u2", real=True)
r2 = x**2 + y**2
K = S.Matrix([-x * y, (x**2 - y**2) / 2]) / (S.pi * r2**2)
z = x + S.I * y
A_["K as v2 + i v1 = 1/(2 pi z^2)"] = S.simplify(K[1] + S.I * K[0] - 1 / (2 * S.pi * z**2)) == 0
# holomorphic: D^k K[u, ..., u] = K^(k)(z) u^k with u = u1 + i u2; |K'| = 1/(pi |z|^3), |K'''| = 12/(pi |z|^5)
uz = u1 + S.I * u2
dd = lambda f_: S.diff(f_, x) * u1 + S.diff(f_, y) * u2
for k, Kk in ((1, -1 / (S.pi * z**3)), (3, -12 / (S.pi * z**5))):
    f1, f2 = K[0], K[1]
    for _ in range(k):
        f1, f2 = dd(f1), dd(f2)
    A_["D^%d K[u,..] = K^(%d)(z) u^%d" % (k, k, k)] = S.simplify(f2 + S.I * f1 - Kk * uz**k) == 0
A_["Taylor remainder factor (1/6)(12/pi)(2/r)^5 = 64/(pi r^5)"] = S.Rational(1, 6) * 12 * 2**5 == 64
# the five pieces of C_a, symbolic a, as exact integrals of the stated majorants (a in (-5, -3), r > 0)
a = S.symbols("a", real=True)
rp, s = S.symbols("r s", positive=True)
ann = S.pi * (2 * rp)**2 * (1 / (2 * S.pi * (rp / 2)**2)) * (rp / 2)**a          # area of |Y| <= 2r, |K| <= 2/(pi r^2)
far = 4 * (2 * rp)**a / (-a)                     # int_{2r}^inf (2/(pi s^2)) s^a 2 pi s ds = 4 int s^(a-1) ds
mom = (1 / (S.pi * rp**3)) * 2 * S.pi * (rp / 2)**(a + 3) / (-a - 3)    # |DK| int_{r/2}^inf s s^a 2 pi s ds
tay = (64 / (S.pi * rp**5)) * 2 * S.pi * (rp / 2)**(a + 5) / (a + 5)    # (64/(pi r^5)) int_0^{r/2} s^3 s^a 2 pi s ds
A_["antiderivatives s^(a-1), s^(a+2), s^(a+4)"] = all(
    S.simplify(S.diff(F_, s) - f_) == 0 for F_, f_ in ((s**a / a, s**(a - 1)), (s**(a + 3) / (a + 3), s**(a + 2)),
                                                       (s**(a + 5) / (a + 5), s**(a + 4))))
Ca = S.Rational(1, 2) + 2**(3 - a) + 2**(a + 2) / (-a) + 2**(-a - 2) / (-a - 3) + 2**(2 - a) / (a + 5)
pieces = S.Rational(1, 2) + (ann + far + mom + tay) / rp**a
A_["contact + annulus + far + moment + Taylor = C_a"] = S.simplify(S.powsimp(S.expand_power_base(S.expand(pieces - Ca), force=True), force=True)) == 0
# near field: int_0^(r/2) min(L, 2B/s) ds; the second case (2B/L < r/2) equals 2B(1 + log(Lr/(4B)))
Lp, Bp = S.symbols("L B", positive=True)
case2 = Lp * (2 * Bp / Lp) + S.integrate(2 * Bp / s, (s, 2 * Bp / Lp, rp / 2))
A_["near field, 2B/L < r/2"] = S.simplify(S.expand_log(case2 - 2 * Bp * (1 + S.log(Lp * rp / (4 * Bp))), force=True)) == 0
e_, A0, D0 = S.symbols("epsilon A D", positive=True)
Bn, Ln = A0 * (rp / 2)**a, D0 * (rp / 2)**(a + e_ - 1)
A_["Lr/(4B) = k r^eps"] = S.simplify(S.powsimp(S.expand_power_base(Ln * rp / (4 * Bn) * 2**(e_ + 1) * A0 / (D0 * rp**e_), force=True), force=True)) == 1
A_["2B = L_a A r^a"] = S.simplify(S.powsimp(S.expand_power_base(2 * Bn - 2**(1 - a) * A0 * rp**a, force=True), force=True)) == 0
# slope of J on the branch k r^eps > 1, and x exp(-x/2) <= 2/e
C_, L_, k_ = S.symbols("C L k", positive=True)
J = A0 * rp**(-e_) * (C_ + L_ * (1 + S.log(k_ * rp**e_)))
A_["J slope"] = S.simplify(S.diff(J, rp) + e_ * A0 * rp**(-e_ - 1) * (C_ + L_ * S.log(k_ * rp**e_))) == 0
xx = S.symbols("x", nonnegative=True)
fx = xx * S.exp(-xx / 2)
A_["max x exp(-x/2) = 2/e < 1"] = S.solve(S.diff(fx, xx), xx) == [2] and S.simplify(fx.subs(xx, 2) - 2 / S.E) == 0 \
    and S.limit(fx, xx, S.oo) == 0 and bool(2 / S.E < 1)
# exterior Green coefficients, symbolic n and q (the cutoff part gives the r^-n term with J_n)
n, q = S.symbols("n q", real=True)
p = q + 2
A_["Green particular coefficient -(1/(n-p) + 1/(n+p))/(2n) = 1/(p^2 - n^2)"] = S.simplify(-(1 / (n - q - 2) + 1 / (n + q + 2)) / (2 * n) - 1 / (p**2 - n**2)) == 0
A_["first-sine tail -(1/(p+1) + 1/(1-p))/2 = 1/(p^2 - 1)"] = S.simplify(-(-1 / (-q - 3) + 1 / (-q - 1)) / 2 - 1 / (p**2 - 1)) == 0
# dipole: potential -m y/(2 pi r^2) has velocity -m d_y K, which + DK M (M = (0, m)) cancels
mm = S.symbols("m", real=True)
psi = -mm * y / (2 * S.pi * r2)
A_["dipole velocity = -m d_y K"] = all(S.simplify(e1 + mm * S.diff(e2, y)) == 0
                                       for e1, e2 in ((S.diff(psi, x, y), K[0]), (-S.diff(psi, x, 2), K[1])))
# Hessian pair of r^-n sin(n theta) = (x^2 + y^2)^-n Im((x + i y)^n): size n(n+1) r^(-n-2)
okH = True
for nn in range(3, 22, 2):
    F = r2**(-nn) * S.im(S.expand((x + S.I * y)**nn))
    w1, w2 = S.diff(F, x, y), -S.diff(F, x, 2)
    for j in range(1, 6):
        t_ = S.Rational(j, 7)
        for sc in (1, S.Rational(3, 2)):
            xv, yv = sc * (1 - t_**2) / (1 + t_**2), sc * 2 * t_ / (1 + t_**2)
            val = (w1**2 + w2**2).subs({x: xv, y: yv}) - nn**2 * (nn + 1)**2 * (xv**2 + yv**2)**(-nn - 2)
            okH = okH and S.nsimplify(val) == 0
A_["Hessian size of r^-n sin(n theta), n = 3..21"] = okH
# cutoff chi = 3t^2 - 2t^3, t = r/R0 - 1, so r chi'(r) = (1 + t) dchi/dt
t = S.symbols("t", real=True)
chi = 3 * t**2 - 2 * t**3
rchi = (1 + t) * S.diff(chi, t)
crit = [c_ for c_ in S.solve(S.diff(rchi, t), t) if 0 <= c_ <= 1]
A_["cutoff C1 endpoints"] = [chi.subs(t, 0), chi.subs(t, 1), S.diff(chi, t).subs(t, 0), S.diff(chi, t).subs(t, 1)] == [0, 1, 0, 0]
A_["max |r chi'| = 4/sqrt(3) <= 3"] = len(crit) == 1 and S.simplify(rchi.subs(t, crit[0]) - 4 / S.sqrt(3)) == 0 \
    and all(rchi.subs(t, v_) >= 0 for v_ in (0, 1)) and bool(4 / S.sqrt(3) <= 3)
A_["1 - chi = (1 - t)^2 (1 + 2t)"] = S.expand(1 - chi - (1 - t)**2 * (1 + 2 * t)) == 0
assert all(A_.values()), A_
OUT["A"] = A_
print("(A) exact checks:", json.dumps(A_))

# =============================== (B) fixture in Arb, FLOAT check of (1) ===============================
ctx.prec = 200
PI = arb.pi()
AR = lambda fr_: arb(fr_.numerator) / fr_.denominator
two = arb(2)


def directed(xv, up, sig=7):
    """Decimal string with sig significant digits, >= every point of the ball if up, else <= (exact endpoints)."""
    m_, e2 = (xv.upper() if up else xv.lower()).man_exp()
    v_ = Fr(int(m_)) * Fr(2)**int(e2)
    if v_ == 0:
        return "0"
    ex = math.floor(math.log10(abs(float(v_))))
    pl = sig - 1 - ex
    n_ = math.ceil(v_ * Fr(10)**pl) if up else math.floor(v_ * Fr(10)**pl)
    o_ = Fr(n_) / Fr(10)**pl
    assert (o_ >= v_) if up else (o_ <= v_)
    return ("%." + str(max(pl, 0)) + "f") % o_ if pl >= 0 else str(int(o_))


def parse(sv):
    m_, r_ = sv.strip().strip("[]").split("+/-")
    return arb(m_.strip(), r_.strip())


def CaL(aA):
    """(C_a, L_a) of (1) as Arb balls."""
    return (arb(1) / 2 + two**(3 - aA) + two**(aA + 2) / (-aA) + two**(-aA - 2) / (-aA - 3) + two**(2 - aA) / (aA + 5),
            two**(1 - aA))


fx_ = PAR["illustrative_fixture"]
fa, fq, fA, fD, feta = (AR(Fr(fx_[k_])) for k_ in ("a", "q", "A", "D", "eta"))
fe = fq - fa
fCa, fLa = CaL(fa)
fk = fD / (two**(fe + 1) * fA)
fR = (fA * (fCa + fLa * (2 + (fk.log() if fk > 1 else arb(0)))) / feta)**(2 / fe)
fJ = fA * fR**(-fe) * (fCa + fLa * (1 + ((fk * fR**fe).log() if fk * fR**fe > 1 else arb(0))))
fix = RES["fixture"]
agree = lambda v_, s_: bool(abs(v_ - (parse(s_) if "+/-" in s_ else arb(s_))) < arb(10)**-40 * (1 + abs(v_)))
OUT["B"] = {"fixture": {"C_a": fCa.str(20), "L_a": fLa.str(20), "k": fk.str(20), "coarse_radius": fR.str(20),
                        "J_at_radius": fJ.str(20), "J_at_radius_below_eta": bool(fJ < feta),
                        "agrees_with_result_json": {k_: agree(v_, fix[k_]) for k_, v_ in
                                                    (("C_a", fCa), ("L_a", fLa), ("k", fk), ("coarse_radius", fR),
                                                     ("J_at_radius", fJ))}}}
assert all(OUT["B"]["fixture"]["agrees_with_result_json"].values()) and OUT["B"]["fixture"]["J_at_radius_below_eta"]
print("(B) fixture: C_a = %s, L_a = %s, k = %s, coarse radius (4) = %s, J there = %s < eta = 1/100: %s; all five agree "
      "with result.json to relative 1e-40: %s" % (fCa.str(10), fLa.str(10), fk.str(10), fR.str(10), fJ.str(10),
                                         OUT["B"]["fixture"]["J_at_radius_below_eta"],
                                         all(OUT["B"]["fixture"]["agrees_with_result_json"].values())))

# FLOAT: g = f(r) sin(theta), f(r) = r (1 + r^2)^((aF - 1)/2), aF = -4, qF = -7/2. A and D read off on a grid (FLOAT).
# Canonical potential psi = A1(r) sin(theta) = y G(r), G = A1/r, from the Green formula of Section 3 (n = 1).
aF, qF_ = -4.0, -3.5
epF = qF_ - aF
f = lambda s_: s_ * (1 + s_ * s_)**((aF - 1) / 2)
fp = lambda s_: (1 + s_ * s_)**((aF - 1) / 2) * (1 + (aF - 1) * s_ * s_ / (1 + s_ * s_))
gr = np.linspace(0, 400, 400001)[1:]
Af = float(np.max(np.abs(f(gr)) / (1 + gr)**aF))
Df = float(np.max(np.hypot(fp(gr), f(gr) / gr) / (1 + gr)**(qF_ - 1)))
Iinf = quad(lambda s_: s_**2 * f(s_), 0, np.inf, limit=400, epsabs=0, epsrel=1e-13)[0]
mF = math.pi * Iinf                                  # M_g = (0, pi I_inf)


def vel(rr, ths):
    I1 = quad(lambda s_: s_**2 * f(s_), 0, rr, limit=400, epsabs=0, epsrel=1e-13)[0]
    I2 = quad(lambda s_: f(s_), rr, np.inf, limit=400, epsabs=0, epsrel=1e-13)[0]
    A0_ = -(I1 / rr + rr * I2) / 2
    A1_ = -(-I1 / rr**2 + I2) / 2
    A2_ = f(rr) - A1_ / rr + A0_ / rr**2
    G1 = A1_ / rr - A0_ / rr**2
    G2 = A2_ / rr - 2 * A1_ / rr**2 + 2 * A0_ / rr**3
    X, Y = rr * np.cos(ths), rr * np.sin(ths)
    psi_xy = G1 * X / rr + X * Y * Y * (G2 - G1 / rr) / rr**2
    psi_xx = Y * (G1 / rr + X * X * (G2 - G1 / rr) / rr**2)
    dyK1 = -(X * rr**2 - 4 * X * Y * Y) / (math.pi * rr**6)
    dyK2 = (-2 * Y * rr**2 - 4 * Y * (X * X - Y * Y)) / (2 * math.pi * rr**6)
    return np.hypot(psi_xy + mF * dyK1, -psi_xx + mF * dyK2)


CaF = 0.5 + 2**(3 - aF) + 2**(aF + 2) / (-aF) + 2**(-aF - 2) / (-aF - 3) + 2**(2 - aF) / (aF + 5)
LaF = 2**(1 - aF)
kF = Df / (2**(epF + 1) * Af)
# homogeneous limit: r^-aF (U + DK M) -> V_aF[sin(theta)] of T4-402 (9) with q = aF, n = 1, b_1 = 1
pL = aF + 2
thg = np.linspace(0, math.pi / 2, 181)
DL = 4 * (pL * pL - 1)
VL1 = ((pL + 1) * (pL - 1) * np.cos(-thg) - (pL - 1) * (pL - 3) * np.cos(3 * thg)) / DL
VL2 = -np.sin(thg) / 2 - ((pL + 1) * (pL - 1) * np.sin(-thg) + (pL - 1) * (pL - 3) * np.sin(3 * thg)) / DL
limF = float(np.hypot(VL1, VL2).max())
rowsB = []
for rr in (2.0, 4.0, 16.0, 64.0, 256.0):
    lhs = float(vel(rr, thg).max())
    rhs = Af * rr**aF * (CaF + LaF * (1 + max(0.0, math.log(kF * rr**epF))))
    rowsB.append({"r": rr, "lhs": lhs, "rhs": rhs, "rhs_over_lhs": rhs / lhs, "lhs_over_r^a": lhs / rr**aF})
    assert lhs <= rhs
OUT["B"]["FLOAT_check_of_(1)"] = {"a": aF, "q": qF_, "A": Af, "D": Df, "C_a": CaF, "L_a": LaF, "k": kF, "rows": rowsB,
                                  "limit_sup_theta_|V_a[sin]|": limF}
print("(B) FLOAT g = r sin(theta)(1 + r^2)^(-5/2): A = %.6g, D = %.6g, k = %.6g; limit of r^-a |U + DK M| = %.6g"
      % (Af, Df, kF, limF))
for rw in rowsB:
    print("(B) FLOAT r = %g: max_theta |U[g] + DK M_g| = %.6g, bound (1) = %.6g, ratio %.4g; r^-a |U + DK M| = %.6g"
          % (rw["r"], rw["lhs"], rw["rhs"], rw["rhs_over_lhs"], rw["lhs_over_r^a"]))

# =============================== (C) Arb, the campaign consequence ===============================
cF = Fr(4076476460239181, 2**51)
assert Fr(PAR["campaign_c"]) == cF and Fr(RES["campaign_q"]) == 1 / cF - 4
qF = 1 / cF - 4
dF = 1 - 1 / cF
qA, dA, cA = AR(qF), AR(dF), AR(cF)
Dd = 1 - cA * (qA - dA)
s22 = (-2 * qA - 2).sqrt()
# Sigma_q <= C_a + L_a for every a = q - eps in (-5, q): 2^(3-a), 2^(1-a) and 2^(2-a)/(a+5) increase as a decreases
# (a + 5 > 0); the terms 2^(a+2)/(-a) and 2^(-a-2)/(-a-3) are positive and dropped.
Sig = arb(1) / 2 + two**(3 - qA) + two**(1 - qA) + two**(2 - qA) / (qA + 5)
e4 = AR(Fr(PAR["campaign_epsilon"]))
Ca4, La4 = CaL(qA - e4)
assert Fr(RES["campaign_a"]) == qF - Fr(PAR["campaign_epsilon"])
gain = (4 + dA) / (4 + 2 * dA)                     # D_delta/(1 - c(q - 2 delta)) = (4 + delta)/(4 + 2 delta), 1 - cq = 4c
assert abs(gain - Dd / (1 - cA * (qA - 2 * dA))) < arb(10)**-50
OUT["C"] = {"Sigma_q_lower": directed(Sig, False, 7), "2^-q_lower": directed(two**(-qA), False, 7),
            "D_delta_lower": directed(Dd, False, 9), "C_a+L_a_at_eps_1/4_lower": directed(Ca4 + La4, False, 7),
            "gain_(4+delta)/(4+2delta)_lower": directed(gain, False, 7)}
betas = {"sharpw": Fr(28496, 10**10), "TB": Fr(3793, 10**9), "graded": Fr(25, 54684), "fixed_sharpw_ball": Fr(1351, 1024000000)}
R375 = json.loads((HERE / "data/t4_375_review_results.json").read_text())
OUT["C"]["t4_375_review_results_sha256"] = sha(HERE / "data/t4_375_review_results.json")
qf, df = float(qA.mid()), float(dA.mid())


def CLf(e):
    af = qf - e
    return 0.5 + 2**(3 - af) + 2**(af + 2) / (-af) + 2**(-af - 2) / (-af - 3) + 2**(2 - af) / (af + 5) + 2**(1 - af)


for name in ("007", "013", "014"):
    ep = json.loads((SRC402 / f"data/{name}_endpoint.json").read_text())
    Am = {int(k_): Fr(v_) for k_, v_ in ep["F12"].items()}
    Pm = {int(k_): Fr(v_) for k_, v_ in ep["P"].items()}
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    ns = sorted(set(Am) | set(Pm))
    Saa = sum(Am.get(n_, Fr(0))**2 for n_ in ns)
    Sap = sum(Am.get(n_, Fr(0)) * Pm.get(n_, Fr(0)) for n_ in ns)
    Spp = sum(Pm.get(n_, Fr(0))**2 for n_ in ns)
    B0 = (PI * AR(Saa - Sap**2 / Spp)).sqrt() / (4 * cA)
    g0 = AR(sum(n_ * v_ for n_, v_ in th0.items()))
    Phi = parse(R375["D"][name]["Phi_theta_star"])
    C0 = B0 / (2 * PI).sqrt()
    row = {"C0_upper": directed(C0, True, 7), "Phi_lower": directed(Phi, False, 7), "g0": g0.str(15)}
    for lab, bt in betas.items():
        rb = (B0 / (AR(bt) * s22))**(1 / (-qA - 1))
        Kc = Dd * B0 * rb**dA / ((2 * PI).sqrt() * g0)
        Ec = Kc / Phi
        jlow = Sig * (arb(5) / rb)**dA                 # J(R)/H for R0 >= 2, L0 <= R <= r_beta, 0 < eps <= delta
        j4 = (Ca4 + La4) * (arb(5) / rb)**e4           # the same at eps = 1/4
        room = Dd * rb**dA / g0                        # Kcrit/C0
        struct = two**(-qA) * Sig                      # J(R)/C0 for L0 <= R <= r_grad (E of (6) = E of r_grad)
        rbf = float(rb.mid())
        es1 = np.linspace(1e-6, df, 20001)
        es2 = np.linspace(1e-6, qf + 5 - 1e-6, 40001)
        v1 = np.array([CLf(e) * (5 / rbf)**e for e in es1])
        v2 = np.array([CLf(e) * (5 / rbf)**e for e in es2])
        rw = {"r_beta_upper": directed(rb, True, 7), "Kcrit_upper": directed(Kc, True, 7),
              "Ecrit_upper": directed(Ec, True, 7), "Ecrit_minus_583/1000_upper": directed(Ec - arb(583) / 1000, True, 7),
              "J_over_H_lower": directed(jlow, False, 7), "J_over_H_lower_eps_1/4": directed(j4, False, 7),
              "J_Phi_over_Kcrit_lower": directed(jlow * Phi / Kc, False, 7),
              "F2_fails": bool(jlow > Ec - arb(583) / 1000), "F3_fails": bool(jlow * Phi > Kc),
              "room_Kcrit_over_C0_upper": directed(room, True, 7), "structural_J_over_C0_lower": directed(struct, False, 7),
              "structural_ratio_lower": directed(struct / room, False, 7),
              "structural_ratio_without_2^-q_lower": directed(Sig / room, False, 7),
              "FLOAT_min_eps_le_delta": [float(v1.min()), float(es1[int(v1.argmin())])],
              "FLOAT_min_eps_lt_q+5": [float(v2.min()), float(es2[int(v2.argmin())])]}
        ok_ = es2[v2 < float((Ec - arb(583) / 1000).mid())]      # eps where the A_in H-term alone fits the (F2) room
        rw["FLOAT_eps_range_inner_term_below_F2_room"] = [float(ok_.min()), float(ok_.max())] if len(ok_) else None
        assert rw["F2_fails"] and rw["F3_fails"] and struct > room and Sig > room and j4 > jlow
        row[lab] = rw
    row["FLOAT_R_with_Sigma_q_(5/R)^delta_=_0.0989"] = 5 * (float(Sig.mid()) / 0.0989)**(1 / df)
    OUT["C"][name] = row
    print("(C) %s: C0 = B0/sqrt(2 pi) <= %s; Phi(theta*) >= %s; g0 = %s; FLOAT: Sigma_q (5/R)^delta = 0.0989 at R = %.6g"
          % (name, row["C0_upper"], row["Phi_lower"], row["g0"], row["FLOAT_R_with_Sigma_q_(5/R)^delta_=_0.0989"]))
    for lab in betas:
        rw = row[lab]
        if rw["FLOAT_eps_range_inner_term_below_F2_room"]:
            print("(C) %s %s: FLOAT (C_a + L_a)(5/r_beta)^eps < Ecrit - 583/1000 only for eps in [%.4g, %.4g]"
                  % (name, lab, *rw["FLOAT_eps_range_inner_term_below_F2_room"]))
        print("(C) %s %s: r_beta <= %s; Kcrit <= %s; Ecrit <= %s, Ecrit - 583/1000 <= %s; J(R)/H >= %s (eps <= delta), >= %s "
              "(eps = 1/4); J Phi/Kcrit >= %s; (F2) fails: %s, (F3) fails: %s; Kcrit/C0 <= %s; structural J/C0 >= %s, "
              "ratio >= %s (without 2^-q: %s); FLOAT min (C_a + L_a)(5/r_beta)^eps = %.6g at eps = %.6g (eps <= delta), "
              "%.6g at eps = %.6g (eps < q + 5)"
              % (name, lab, rw["r_beta_upper"], rw["Kcrit_upper"], rw["Ecrit_upper"], rw["Ecrit_minus_583/1000_upper"],
                 rw["J_over_H_lower"], rw["J_over_H_lower_eps_1/4"], rw["J_Phi_over_Kcrit_lower"], rw["F2_fails"],
                 rw["F3_fails"], rw["room_Kcrit_over_C0_upper"], rw["structural_J_over_C0_lower"],
                 rw["structural_ratio_lower"], rw["structural_ratio_without_2^-q_lower"], *rw["FLOAT_min_eps_le_delta"],
                 *rw["FLOAT_min_eps_lt_q+5"]))
print("(C) Sigma_q >= %s; 2^-q >= %s; D_delta >= %s; C_a + L_a at eps = 1/4 >= %s; (4 + delta)/(4 + 2 delta) >= %s"
      % (OUT["C"]["Sigma_q_lower"], OUT["C"]["2^-q_lower"], OUT["C"]["D_delta_lower"], OUT["C"]["C_a+L_a_at_eps_1/4_lower"],
         OUT["C"]["gain_(4+delta)/(4+2delta)_lower"]))

OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_410_review_results.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
print("elapsed %.1f s" % OUT["elapsed_s"])
