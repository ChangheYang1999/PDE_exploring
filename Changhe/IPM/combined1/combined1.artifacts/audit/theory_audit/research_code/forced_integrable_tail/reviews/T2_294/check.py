"""Independent review of T4-294 (c1-t4 research/forced_integrable_tail/PROOF.md, sha256 1c490b83...0e1a): the
weighted pointwise velocity bound (2), the forced leading coefficient (4)-(5) and the branch-3 tail repair (6)
(reviews/REVIEW_T4_294.md).

Run from artifacts/:  python3 -B -u arith/t4_294_review.py
Needs sympy, mpmath, python-flint.

Parts:
  (A) sympy: the four region integrals of Section 1 and C_q; the radial identity of Section 2; density and stream of
      the potential r^d cos(n th) (the leading sector of (6)); the descendant expansion of (1 + r^2)^p P(t); the origin
      order of t^(m+4) cos(2m th); for remark R2, int_0^inf rho^2 (1 + rho)^q d rho and the constant C'_q.
  (B) arb: C_q at q = -1 - 4 delta and C'_q at q = 1 - 9 delta, with directed decimal bounds.
  (C) exact (fmpq): for 007, 013, 014, my constructor (copied from arith/t4_281_review.py) on the raw c1-n1
      generator files; the coefficients A1_m from my branch-3 polynomials against c1-t4's stored correction; the
      repaired state rebuilt from the generator polynomials plus (6); all density and stream sectors before and
      after (L <= 2); every residual coefficient at exponent >= gamma - 4, products included, after the repair.
Output: logs/t4_294_review.log, data/t4_294_review_results.json.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from flint import arb, ctx, fmpq, fmpq_poly

sys.set_int_max_str_digits(0)
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]
T0 = time.monotonic()
OUT = {}

# =============================== (A) sympy ===============================
q, r, rho, d, s = sp.symbols("q r rho d s", real=True)
rp = sp.symbols("r_", positive=True)
# (A1) region integrals of Section 1, for -3 < q < 0 (checked symbolically and at q = -2.79 by quadrature)
Ia = sp.integrate(1 / (2 * sp.pi * rho**2) * rho * 2 * sp.pi * rho, (rho, 0, rp / 2))
assert sp.simplify(Ia - rp / 2) == 0
ca = sp.simplify(2**(1 - q) * rp**(q - 1) * Ia / rp**q)
cb = sp.simplify(8 / (sp.pi * rp**3) * 2 * sp.pi * (rp / 2)**(q + 3) / (q + 3) / rp**q)
cc = sp.simplify(2 / (sp.pi * rp**2) * (rp / 2)**q * 4 * sp.pi * rp**2 / rp**q)
cd = sp.simplify(4 * (2 * rp)**q / (-q) / rp**q)
assert sp.simplify(ca - 2**(-q)) == 0 and sp.simplify(cb - 2**(1 - q) / (q + 3)) == 0
assert sp.simplify(cc - 2**(3 - q)) == 0 and sp.simplify(cd - 2**(q + 2) / (-q)) == 0
mp.mp.dps = 30
qn, rn = mp.mpf("-2.79"), mp.mpf(7)
# substitution rho = (r/2) v^10 removes the endpoint singularity of rho^(q+2)
assert abs(mp.quad(lambda v: (rn / 2)**(qn + 3) * 10 * v**(10 * qn + 29), [0, 1]) - (rn / 2)**(qn + 3) / (qn + 3)) < 1e-20
assert abs(mp.quad(lambda x: x**(qn - 1), [2 * rn, mp.inf]) - (2 * rn)**qn / (-qn)) < 1e-20
assert sp.simplify(sp.pi * ((2 * rp)**2 - (rp / 2)**2) - sp.Rational(15, 4) * sp.pi * rp**2) == 0
Cq_sym = sp.Rational(1, 2) + 2**(-q) + 2**(1 - q) / (q + 3) + 2**(3 - q) + 2**(q + 2) / (-q)
print("(A1) Section 1: int_(|Z|<r/2) |K||Z| = r/2; the four regions give 2^-q, 2^(1-q)/(q+3), 2^(3-q), 2^(q+2)/(-q)"
      " times H r^q (sympy; the two power integrals also by quadrature at q = -2.79, r = 7); annulus area 15 pi r^2/4"
      " <= 4 pi r^2")
# |K| and zero angular mean (also A1, A2 of t4_281_review.py)
z1, z2, th = sp.symbols("z1 z2 theta", real=True)
K1 = -z1 * z2 / (sp.pi * (z1**2 + z2**2)**2)
K2 = (z1**2 - z2**2) / (2 * sp.pi * (z1**2 + z2**2)**2)
assert sp.simplify(K1**2 + K2**2 - 1 / (4 * sp.pi**2 * (z1**2 + z2**2)**2)) == 0
assert all(sp.integrate(Kc.subs({z1: sp.cos(th), z2: sp.sin(th)}), (th, 0, 2 * sp.pi)) == 0 for Kc in (K1, K2))
print("(A1) |K(Z)| = 1/(2 pi |Z|^2) and both components have zero angular mean")
# (A2) Section 2: radial identity and the ODE form
c, g, p = sp.symbols("c gamma p", positive=True)
w = sp.symbols("w", positive=True)                     # w = gamma - p > 0
lhs = rp**g / c * sp.integrate(s**(-w - 1), (s, rp, sp.oo), conds="none")
rhs = rp**(g - w) / (1 - c * (g - w))
assert sp.simplify((lhs - rhs).subs(g, 1 / c)) == 0
f = sp.Function("f")
assert sp.simplify((c * rp**(1 + g) * sp.diff(rp**(-g) * f(rp), rp) - (c * rp * sp.diff(f(rp), rp) - f(rp))).subs(
    g, 1 / c)) == 0
assert sp.simplify(c * rp * sp.diff(rp**p, rp) - rp**p - (c * p - 1) * rp**p) == 0
print("(A2) Section 2: r^gamma/c int_r^inf t^(p-gamma-1) dt = r^p/(1 - c p) (p < gamma, gamma = 1/c);"
      " c r^(1+gamma) d_r(r^-gamma h) = c r h_r - h; (c r d_r - 1) r^p = (c p - 1) r^p")
# (A3) density -d_y Delta chi and stream d_x d_y chi of chi = r^d cos(n th); Delta psi = -d_x rho
def Dx(F):
    return sp.cos(th) * sp.diff(F, rp) - sp.sin(th) / rp * sp.diff(F, th)


def Dy(F):
    return sp.sin(th) * sp.diff(F, rp) + sp.cos(th) / rp * sp.diff(F, th)


def Lap(F):
    return sp.diff(F, rp, 2) + sp.diff(F, rp) / rp + sp.diff(F, th, 2) / rp**2


def tri(F):
    return sp.expand(sp.expand(F).rewrite(sp.exp))


for n in range(0, 11, 2):
    chi_ = rp**d * sp.cos(n * th)
    dens = -Dy(Lap(chi_))
    strm = Dx(Dy(chi_))
    Td = {n + 1: -(d * d - n * n) * (d - 2 - n) / 2, n - 1: (d * d - n * n) * (d - 2 + n) / 2}
    Ps_ = {n + 2: (d - n) * (d - n - 2) / 4, n - 2: -(d + n) * (d + n - 2) / 4}
    claimD = sum(v * rp**(d - 3) * sp.sin(k * th) for k, v in Td.items())
    claimS = sum(v * rp**(d - 2) * sp.sin(k * th) for k, v in Ps_.items())
    assert tri(dens - claimD) == 0 and tri(strm - claimS) == 0, n
    assert tri(Lap(strm) + Dx(dens)) == 0
print("(A3) for chi = r^d cos(n th), n = 0, 2, ..., 10, d symbolic: -d_y Delta chi and d_x d_y chi are the Tr and Pr"
      " formulas of code/check.py (exponents d - 3 and d - 2), and Delta psi = -d_x rho")
# (A4) (1 + r^2)^p P(t) = r^(2p) [P(1) + z (p P(1) - P'(1)) + O(z^2)], z = r^-2; the correction has P(1) = 0, -A1
zz, tt, A1s = sp.symbols("z t A1")
a = sp.symbols("a0:6")
P = sum(a[k] * tt**k for k in range(6))
ser = sp.series(((1 + zz)**p * P.subs(tt, 1 / (1 + zz))), zz, 0, 2).removeO()
assert sp.expand(ser - (P.subs(tt, 1) + zz * (p * P.subs(tt, 1) - sp.diff(P, tt).subs(tt, 1)))) == 0
for m in range(4):
    Qm = -A1s * tt**(m + 4) * (1 - tt)
    serq = sp.series(((1 + zz)**p * Qm.subs(tt, 1 / (1 + zz))), zz, 0, 2).removeO()
    assert sp.expand(serq + A1s * zz) == 0
print("(A4) (1 + z)^p P(1/(1 + z)) = P(1) + z (p P(1) - P'(1)) + O(z^2) (degree 5, symbolic); for"
      " -A1 t^(m+4) (1 - t), m = 0..3: 0 - A1 z + O(z^2)")
# (A5) origin: r^(2m) cos(2m th) = Re (x + i y)^(2m), so t^(m+4) cos(2m th) = |X|^8 Re (x+iy)^(2m) (1+|X|^2)^(-m-4)
x, y = sp.symbols("x y", real=True)
for m in range(6):
    polar = rp**(2 * m) * sp.cos(2 * m * th)
    cart = sp.re(sp.expand((x + sp.I * y)**(2 * m)))
    assert tri(polar - cart.subs({x: rp * sp.cos(th), y: rp * sp.sin(th)})) == 0
print("(A5) r^(2m) cos(2m th) = Re (x + i y)^(2m), m = 0..5: t^(m+4) cos(2m th) is smooth with lowest homogeneous"
      " degree 2m + 8")
# (A6) remark R2: int_0^inf rho^2 (1 + rho)^q = 2/((-q-1)(-q-2)(-q-3)), q < -3
sq = sp.symbols("sq", positive=True)              # q = -3 - sq
Ib = sp.integrate(rho**2 * (1 + rho)**(-3 - sq), (rho, 0, sp.oo), conds="none")
assert sp.simplify(Ib - 2 / ((2 + sq) * (1 + sq) * sq)) == 0
print("(A6) R2: int_0^inf rho^2 (1 + rho)^q d rho = 2/((-q-1)(-q-2)(-q-3)) for q < -3")
print("(A) done, %.1f s" % (time.monotonic() - T0))

# =============================== (B) arb constants ===============================
cr = fmpq(4076476460239181, 2**51)
dl = 1 - 1 / cr
q1 = -1 - 4 * dl
q2 = 1 - 9 * dl
A_ = lambda v: arb(v.p) / v.q


def Cq(qq):
    Q_ = A_(qq)
    return arb(1) / 2 + arb(2)**(-Q_) + arb(2)**(1 - Q_) / (Q_ + 3) + arb(2)**(3 - Q_) + arb(2)**(Q_ + 2) / (-Q_)


def Cqp(qq):                                      # remark R2, q < -3, r >= 2: |U[h]| <= C'_q H r^-3
    Q_ = A_(qq)
    return (arb(2)**(Q_ + 3) * (arb(1) / 2 + arb(2)**(-Q_) + arb(2)**(3 - Q_) + arb(2)**(Q_ + 2) / (-Q_))
            + arb(32) / ((-Q_ - 1) * (-Q_ - 2) * (-Q_ - 3)))


C1v, C2v = Cq(q1), Cqp(q2)
assert C1v < arb("129.002792") and C1v > arb("129.002791")
OUT["B"] = {"q1": str(q1), "Cq": C1v.str(30), "q2": str(q2), "Cprime_q2": C2v.str(30)}
print("(B) q = -1 - 4 delta = %s = %.15f; C_q = %s, so 129.002791 < C_q < 129.002792 (c1-t4: 129.0027919004...)"
      % (q1, float(q1), C1v.str(25)))
print("    R2: q2 = 1 - 9 delta = %.15f in (gamma - 4, -3) = (%.12f, -3): %s; C'_q2 = %s"
      % (float(q2), float(1 / cr - 4), (1 / cr - 4 < q2 < -3), C2v.str(20)))
assert 1 / cr - 4 < q2 < -3 and -3 < q1 < 0
# ========================= constructor, copied verbatim from arith/t4_249_review.py =========================
tp = fmpq_poly([0, 1])
Wq = fmpq_poly([1, -1])


def Top(P, beta, e):
    return fmpq_poly([e, -2 * beta]) * P + 2 * tp * Wq * P.derivative()


def legendre_shift(nn):          # P_n(2t - 1)
    xx = fmpq_poly([-1, 2])
    p0, p1 = fmpq_poly([1]), xx
    if nn == 0:
        return p0
    for mm in range(1, nn):
        p0, p1 = p1, (fmpq(2 * mm + 1, mm + 1) * xx * p1 - fmpq(mm, mm + 1) * p0)
    return p1


def addto(d, key, P):
    d[key] = d.get(key, fmpq_poly([0])) + P


def load(name):                 # copied from t4_234_review.py
    if name == "state131":
        d = json.loads((HERE / "data/a2_state131_exact.json").read_text())
        c = fmpq(*map(int, d["exact_parameters"]["cl"].split("/")))
        chi = {}
        for (j, mm, kk), co in zip(d["canonical_order"], d["canonical_coefficients"]):
            addto(chi, (j, 2 * mm), fmpq(*map(int, co.split("/"))) * tp**kk)
        return c, chi
    fn = {"d2": "a2_nb_d2_exact.json", "Mpen2": "a2_nb_Mpen2_exact.json",
          "C1-N1-005": "c1n1_005_d2w_j7_n4_X3_mid180_exact.json",
          "C1-N1-007": "c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json"}[name]
    d = json.loads((HERE / "data" / fn).read_text())
    c = fmpq(*map(int, d.get("cl", d.get("cl_exact")).split("/")))
    chi = {}
    for g_ in d["generators"]:
        num, den = (g_["coef"].split("/") + ["1"])[:2]
        co = fmpq(int(num), int(den))
        sp_ = g_["spec"]
        if sp_[0] == "mono":
            T = tp**sp_[1]
        else:
            assert sp_[0] == "leg"
            T = tp**sp_[1] * legendre_shift(sp_[2])
        addto(chi, (g_["j"], 2 * g_["m"]), co * tp**g_["m"] * T)
    return c, chi


def build(c, chi):              # copied from t4_234_review.py
    delta = 1 - 1 / c
    beta = lambda j: -(3 + 1 / c - j * delta) / 2
    lapc = {}
    for (j, nn), P in chi.items():
        TP = Top(P, beta(j), 0)
        addto(lapc, (j, nn), Top(TP, beta(j), 0) - nn * nn * P)

    def dy_cos(cd, e):
        out = {}
        for (j, nn), P in cd.items():
            TP = Top(P, beta(j), e)
            addto(out, (j, nn + 1), fmpq(1, 2) * (TP - nn * P))
            if nn - 1 > 0:
                addto(out, (j, nn - 1), fmpq(-1, 2) * (TP + nn * P))
            elif nn - 1 < 0:
                addto(out, (j, 1), fmpq(1, 2) * (TP + nn * P))
        return out

    def dx_cos(cd, e):
        out = {}
        for (j, nn), P in cd.items():
            TP = Top(P, beta(j), e)
            addto(out, (j, nn + 1), fmpq(1, 2) * (TP - nn * P))
            addto(out, (j, abs(nn - 1)), fmpq(1, 2) * (TP + nn * P))
        return out

    rho3 = dy_cos(lapc, -2)
    psi2 = dy_cos(dx_cos(chi, 0), -1)
    t2 = tp * tp
    R, S = {}, {}
    for key, P in rho3.items():
        qq, rem = divmod(-P, t2)
        assert rem == 0
        if qq != 0:
            R[key] = qq
    for key, P in psi2.items():
        qq, rem = divmod(P, t2)
        assert rem == 0
        if qq != 0:
            S[key] = qq
    return delta, R, S


LJ = 2                          # W-jet length: sectors L = 0, 1


def wjet(P):                    # copied from t4_094_review.py (LJ = 2)
    out, Dp, fact = [], P, 1
    for l in range(LJ):
        out.append(fmpq((-1) ** l, fact) * Dp(fmpq(1)))
        Dp = Dp.derivative()
        fact *= l + 1
    return out


def binom_q(xq, kk):
    out = fmpq(1)
    for i in range(kk):
        out = out * (xq - i) / (i + 1)
    return out


def r_expansion(jets, beta):    # r W^beta sum_l p_l W^l = sum_L c_L r^(1 - 2 beta - 2L)
    return [sum((jets[l] * binom_q(-beta - l, L - l) for l in range(L + 1)), fmpq(0)) for L in range(LJ)]


def put(o, nn, v):
    if nn == 0 or v == 0:
        return
    if nn < 0:
        nn, v = -nn, -v
    o[nn] = o.get(nn, fmpq(0)) + v
    if o[nn] == 0:
        del o[nn]


def sin_cos(S_, C_):
    o = {}
    for a_, sa in S_.items():
        for b_, cb in C_.items():
            v = sa * cb / 2
            put(o, a_ + b_, v)
            put(o, a_ - b_, v)
    return o


def dsin(S_):
    return {nn: nn * v for nn, v in S_.items()}


def add(A_, B_, s=fmpq(1)):
    o = dict(A_)
    for nn, v in B_.items():
        put(o, nn, s * v)
    return o


def scale(A_, s):
    return {nn: s * v for nn, v in A_.items() if s * v != 0}


def poisson(Th, e):
    rhs = add(scale(sin_cos(Th, {1: fmpq(1)}), -e), sin_cos({1: fmpq(1)}, dsin(Th)))
    return {mm: v / ((e + 1)**2 - mm * mm) for mm, v in rhs.items()}


def Bterm(Psl, Thm_, el_, em_):
    return add(scale(sin_cos(Thm_, dsin(Psl)), -em_), scale(sin_cos(Psl, dsin(Thm_)), el_ + 1))


def l2(A_):
    return float(np.sqrt(np.pi * sum(float(v)**2 for v in A_.values())))



# =============================== (C) exact repair of 007, 013, 014 ===============================
LJ = 3                          # W-jet length: sectors L = 0, 1, 2


def load_file(fn):              # as in arith/t4_281_review.py
    dd = json.loads((HERE / "data" / fn).read_text())
    c_ = fmpq(*map(int, dd.get("cl", dd.get("cl_exact")).split("/")))
    chi_ = {}
    for g_ in dd["generators"]:
        num, den = (g_["coef"].split("/") + ["1"])[:2]
        co = fmpq(int(num), int(den))
        sp_ = g_["spec"]
        if sp_[0] == "mono":
            T = tp**sp_[1]
        else:
            assert sp_[0] == "leg"
            T = tp**sp_[1] * legendre_shift(sp_[2])
        addto(chi_, (g_["j"], 2 * g_["m"]), co * tp**g_["m"] * T)
    return c_, chi_


def sha(pth):
    return hashlib.sha256(Path(pth).read_bytes()).hexdigest()


def sectors(R_, S_, delta):
    Th_, Ps_ = {}, {}
    for src, dst in ((R_, Th_), (S_, Ps_)):
        for (j, nn), P_ in src.items():
            for L, v in enumerate(r_expansion(wjet(P_), (j + 1) * delta / 2)):
                if v != 0:
                    put(dst.setdefault((j + 1, L), {}), nn, v)
    return Th_, Ps_


def residuals(Th_, Ps_, keys, expo, c_):
    coef = {}
    for (K, L) in keys:
        o = scale(Th_.get((K, L), {}), c_ * expo(K, L) - 1)
        for K1 in range(1, K):
            for L1 in range(L + 1):
                K2, L2 = K - K1, L - L1
                if (K1, L1) in Ps_ and (K2, L2) in Th_:
                    o = add(o, Bterm(Ps_[(K1, L1)], Th_[(K2, L2)], expo(K1, L1), expo(K2, L2)))
        coef[(K, L)] = o
    return coef


T4D = Path("RUN_ROOT/theory_audit_T4/research/forced_integrable_tail/data")
T4SHA = {"007": "bad9b06a64a3f045e3de487d63793f8ec0c6b021a692c5e11cea91279ed5fcd6",
         "013": "5485a201200fe4cdd57560775c32c0e09938a06f352127a605a780dceaa1c0e4",
         "014": "b69aa6a844b89409b92c6e3c94de220289a6f6c486b7d5e3e6a8c91b1327999d"}
CANDS = [("007", "c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json"),
         ("013", "t4_281_inputs/c1n1_013_d2w_j7_n4_E2bal_pairU_cpu_m16_exact.json"),
         ("014", "t4_281_inputs/c1n1_014_d2w_j7_n4_E2bal_pairB_cpu_m16_exact.json")]
EXPECT = {"007": "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21",
          "013": "c07f87ddfe35e1fd82cfb86e01949749381aac7209a752c713dd01b48a478940",
          "014": "8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746"}
RES = {}
for name, fn in CANDS:
    t1 = time.monotonic()
    assert sha(HERE / "data" / fn) == EXPECT[name] and sha(T4D / f"{name}_tail_repair.json") == T4SHA[name]
    c_, chi = load_file(fn)
    assert c_ == cr
    gam = 1 / c_
    delta, R, S = build(c_, chi)
    expo = lambda K, L: 1 - K * delta - 2 * L
    allkeys = [(K, L) for K in range(1, 17) for L in range(LJ)]
    assert len({expo(*kk) for kk in allkeys}) == len(allkeys)
    keys = [kk for kk in allkeys if expo(*kk) >= gam - 4]
    Th, Ps = sectors(R, S, delta)
    F0 = residuals(Th, Ps, keys, expo, c_)
    # A1_m = p P_m(1) - P_m'(1), p = 2 gamma = (3 + gamma - 3 delta)/2, from my branch-3 polynomials
    pp = 2 * gam
    assert pp == (3 + gam - 3 * delta) / 2
    A1 = {}
    for (j, nn), P_ in chi.items():
        if j == 3:
            v = pp * P_(fmpq(1)) - P_.derivative()(fmpq(1))
            if v != 0:
                A1[nn // 2] = v
    mine = {}
    for m, v in A1.items():
        mine[(m, m + 4)] = -v
        mine[(m, m + 5)] = v
    ext = json.loads((T4D / f"{name}_tail_repair.json").read_text())
    theirs = {}
    for e_ in ext["potential_correction"]:
        j, m, k = e_["order"]
        assert j == 3
        fr = Fraction(e_["coefficient"])
        theirs[(m, k)] = fmpq(fr.numerator, fr.denominator)
    same_corr = mine == theirs
    # repaired state: generator polynomials plus (6) in branch 3, rebuilt from scratch
    chi2 = dict(chi)
    for m, v in A1.items():
        addto(chi2, (3, 2 * m), -v * tp**(m + 4) * (1 - tp))
    _, R2, S2 = build(c_, chi2)
    Th2, Ps2 = sectors(R2, S2, delta)
    F2 = residuals(Th2, Ps2, keys, expo, c_)
    k41_zero = not Th2.get((4, 1)) and not Ps2.get((4, 1))
    changed = sorted(kk for kk in set(Th) | set(Th2) | set(Ps) | set(Ps2)
                     if Th.get(kk, {}) != Th2.get(kk, {}) or Ps.get(kk, {}) != Ps2.get(kk, {}))
    lead_same = all(Th.get((K, 0), {}) == Th2.get((K, 0), {}) for K in range(1, 17))
    pois = all(poisson(Th2.get(kk, {}), expo(*kk)) == Ps2.get(kk, {}) for kk in allkeys if kk[0] <= 8)
    order = sorted(keys, key=lambda kk: -float(expo(*kk)))
    nz2 = [kk for kk in order if F2[kk]]
    zero_ge3 = all(not F2[kk] for kk in keys if expo(*kk) >= -3)
    n41 = len(Th.get((4, 1), {}))
    RES[name] = {"same_correction_as_c1t4": same_corr, "potential_modes": len(A1), "density_modes_41": n41,
                 "sectors_changed": changed, "ladder_unchanged": lead_same, "poisson_K_le_8": pois,
                 "41_zero_after": k41_zero, "zero_at_exponent_ge_minus3": zero_ge3,
                 "nonzero_after": [(kk, str(expo(*kk)), float(expo(*kk)), l2(F2[kk])) for kk in nz2],
                 "F90_unchanged": F2[(9, 0)] == F0[(9, 0)], "F12_unchanged": F2[(1, 2)] == F0[(1, 2)],
                 "F51_before": l2(F0[(5, 1)]), "F51_after": l2(F2[(5, 1)]),
                 "forced_90_norm": l2(scale(F2[(9, 0)], 1 / (1 - c_ * expo(9, 0)))), "seconds": time.monotonic() - t1}
    print("(C) %s: A1_m nonzero for %d modes; correction = c1-t4's stored potential_correction exactly: %s;"
          " Theta_(4,1) has %d sine modes" % (name, len(A1), same_corr, n41))
    print("     after (6): sectors changed %s; (4,1) density and stream zero: %s; ladder (K,0) unchanged: %s;"
          " stream = Poisson of density, K <= 8, L <= 2: %s" % (changed, k41_zero, lead_same, pois))
    print("     residual of R + eta exactly zero at every exponent >= -3: %s; nonzero at exponent >= gamma - 4: %s"
          % (zero_ge3, ", ".join("(%d,%d) %+.9f [%.6g]" % (kk + (float(expo(*kk)), l2(F2[kk]))) for kk in nz2)))
    print("     F_(9,0) unchanged: %s; F_(1,2) unchanged: %s; ||F_(5,1)|| before %.6g, after %.6g;"
          " forced (9,0) density F_(9,0)/(1 - c q2) norm %.6g; %.1f s"
          % (RES[name]["F90_unchanged"], RES[name]["F12_unchanged"], l2(F0[(5, 1)]), l2(F2[(5, 1)]),
             RES[name]["forced_90_norm"], time.monotonic() - t1))
    assert same_corr and k41_zero and lead_same and pois and zero_ge3 and nz2[0] == (9, 0)
    assert RES[name]["F90_unchanged"] and RES[name]["F12_unchanged"]
OUT["C"] = RES
(HERE / "data/t4_294_review_results.json").write_text(json.dumps(OUT, indent=1, default=str))
print("wrote data/t4_294_review_results.json; total %.1f s" % (time.monotonic() - T0))
