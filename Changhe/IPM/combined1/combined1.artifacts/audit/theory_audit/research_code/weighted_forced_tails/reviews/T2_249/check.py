"""Independent review of T4-249 (c1-t4 research/weighted_forced_tails/PROOF.md, sha256 fbd41043...d1c9): weighted
correction classes E_a = L2((1 + r^2)^(-a) dX), -2 < a <= 1 + gamma, force the tail ladder (reviews/REVIEW_T4_249.md).

Run from artifacts/:  python3 -B arith/t4_249_review.py
Needs sympy, numpy, python-flint.

Parts:
  (A) sympy: U2 + i U1 = -(1 + m)/2 with m = (xi1 - i xi2)^2/|xi|^2; conj(m)(xi1, xi2) = m(xi1, -xi2) (the reflection
      used for the reciprocal weight); the constant (1 + (2 + b)/(2 - b))/2 = 2/(2 - b); frozen-coefficient symbols of
      the radial blocks of B for a local weight exponent p (future and past blocks); exponent bookkeeping of
      sections 2 to 4 of the PROOF.
  (B) FLOAT: operator norms of discretized radial blocks of B on the t = log r line, weighted by
      w_(+-b)(t) = (1 + e^(2t))^(-+b/2), against (|n| + b)/(|n| - b) and 1.
  (C) exact (fmpq): N_a and the retained ladder at the run value of c for a list of a; the finite closure Ebar of
      section 5 for a sample exponent set, its closure property and the fact that a non-ladder exponent receives no
      ladder x ladder product.
  (D) exact (fmpq): far-field sectors (K, L), exponent 1 - K delta - 2L, of density and stream of the five
      candidates (code of t4_234_review.py and t4_094_review.py), the angular equation (1) in every sector, and
      the coefficients (10) of the PROOF for L = 0, 1; the largest nonzero one gives the exclusion range
      -2 < a <= q* + 1. Compared with the residual sectors of REVIEW_T4_094 part (2) (different code path).
Output: logs/t4_249_review.log, data/t4_249_review_results.json.
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from flint import fmpq, fmpq_poly

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parents[1]
T0 = time.monotonic()
OUT = {}

# =============================== (A) sympy ===============================
x1, x2, xi, p, b, n, k, a = sp.symbols("xi1 xi2 xi p b n k a", real=True)
m = (x1 - sp.I * x2)**2 / (x1**2 + x2**2)
U1, U2 = x1 * x2 / (x1**2 + x2**2), -x1**2 / (x1**2 + x2**2)
assert sp.simplify(U2 + sp.I * U1 + (1 + m) / 2) == 0
assert sp.simplify(sp.conjugate(m) - m.subs(x2, -x2)) == 0
assert sp.simplify((1 + (2 + b) / (2 - b)) / 2 - 2 / (2 - b)) == 0
print("(A1) U2 + i U1 = -(1 + m)/2; conj(m)(xi1, xi2) = m(xi1, -xi2); (1 + (2+b)/(2-b))/2 = 2/(2-b)")
# future block (n > 0), local weight w ~ e^(-p t): G = F - 2n int_0^inf e^(-(n-p)v) F(t+v) dv
fut = 1 - 2 * n / (n - p - sp.I * xi)
past = 1 - 2 * k / (k + p + sp.I * xi)            # past block (n = -k < 0): G = F - 2k int e^(-(k+p)v) F(t-v) dv
fut2 = sp.simplify(sp.expand(fut * sp.conjugate(fut)))
past2 = sp.simplify(sp.expand(past * sp.conjugate(past)))
assert sp.simplify(fut2 - ((n + p)**2 + xi**2) / ((n - p)**2 + xi**2)) == 0
assert sp.simplify(past2 - ((k - p)**2 + xi**2) / ((k + p)**2 + xi**2)) == 0
print("(A2) frozen block symbols, |.|^2: future ((n+p)^2 + xi^2)/((n-p)^2 + xi^2), past ((k-p)^2 + xi^2)/((k+p)^2 + xi^2)")
print("     decreasing weight (0 <= p <= b): future max (n+b)/(n-b) at xi = 0, past <= 1;"
      " reciprocal weight (-b <= p <= 0): future <= 1, past max (k+b)/(k-b): the mirror image, as duality says")
# exponent bookkeeping (q = exponent, a = weight): int_1^oo r^(2q - 2a + 1) dr at sample points
rr = sp.Symbol("r", positive=True)
for aa_ in (sp.Rational(-19, 10), sp.Rational(-1, 3), sp.Rational(2, 3), sp.Rational(3, 2)):
    qa = aa_ - 1                                    # threshold q = a - 1 diverges, q = a - 1 - 1/10 converges
    assert sp.integrate(rr**(2 * qa - 2 * aa_ + 1), (rr, 1, sp.oo)) == sp.oo
    assert sp.integrate(rr**(2 * (qa - sp.Rational(1, 10)) - 2 * aa_ + 1), (rr, 1, sp.oo)).is_finite
print("(A3) r^q Theta in E_a near infinity iff 2q - 2a + 1 < -1 iff q < a - 1; W.grad R = O(r^(gamma-4)) is in E_a iff"
      " gamma - 4 < a - 1, true for a > -2 since gamma < 1 (O(r^-2) alone would need a > gamma - 2)")
print("     necessity: corrections / L^(e_j+1) have exponents a - (e_j+1) <= 0, a + gamma - 1 - (e_j+1) <= gamma - 1,"
      " 2a - 2 - (e_j+1) <= a - 2 < 0; uniqueness exponents gamma - 1 and max(a, 0) - 2 < 0")
print("(A) done, %.1f s" % (time.monotonic() - T0))

# =============================== (B) FLOAT radial blocks ===============================
hstep = 0.02
tgrid = np.arange(-10.0, 40.0, hstep)
NT = len(tgrid)
DT = tgrid[:, None] - tgrid[None, :]


def block_matrix(nn, bexp):
    """weighted radial block of B for n = nn on L2(dt), weight (1 + e^(2t))^(-bexp/2), trapezoid rule"""
    lw = -bexp / 2 * np.logaddexp(0.0, 2 * tgrid)          # log w
    ratio = np.exp(lw[:, None] - lw[None, :])               # w(t_i)/w(t_j)
    if nn > 0:                                              # future: j > i, v = t_j - t_i
        K = np.where(DT < 0, np.exp(nn * DT), 0.0)
    else:                                                   # past: j < i, v = t_i - t_j
        K = np.where(DT > 0, np.exp(nn * DT), 0.0)
    K = K + 0.5 * np.eye(NT)
    return np.eye(NT) - 2 * abs(nn) * hstep * K * ratio


rowsB = []
for bexp in (0.5, 1.0, 1.5, 1.9):
    for nn in (2, -2, 4, -4):
        M = block_matrix(nn, bexp)
        Mt = block_matrix(-nn, -bexp)                       # reciprocal weight, mirrored block
        tdiff = float(np.max(np.abs(Mt - M.T)) / np.max(np.abs(M)))
        val = float(np.linalg.norm(M, 2))
        bound = (abs(nn) + bexp) / (abs(nn) - bexp) if nn > 0 else 1.0
        rowsB.append((bexp, nn, val, bound, tdiff))
        del M, Mt
print("(B) FLOAT radial block norms on t in [-10, 40), step 0.02, %d nodes; weight w_b = (1 + e^(2t))^(-b/2);"
      " the block n of w_(-b) is the transpose of the block -n of w_b (relative max difference printed), so its norm"
      " is the same" % NT)
for bb, nn, val, bound, tdiff in rowsB:
    print("     b = %.1f, n = %+d: norm %.6f, bound %.6f, ratio %.6f; w_(-b) block n = %+d: transpose, difference %.1e"
          % (bb, nn, val, bound, val / bound, -nn, tdiff))
print("     trapezoid symbol at p = 0, xi = 0: |1 - n h coth(n h/2)| = %.6f (n = 2), %.6f (n = 4)"
      % tuple(abs(1 - nn * hstep / np.tanh(nn * hstep / 2)) for nn in (2, 4)))
OUT["B"] = rowsB
print("(B) done, %.1f s" % (time.monotonic() - T0))

# =============================== (C) exact ladder and closure ===============================
c_run = fmpq(4076476460239181, 2**51)
gam = 1 / c_run
dq = 1 - gam


def ladder(e):
    s = (1 - e) / dq
    return s.q == 1 and s.p >= 1


rowsC = []
for aa in (fmpq(-19, 10), fmpq(-3, 2), fmpq(-1), fmpq(-1, 2), fmpq(0), fmpq(1, 2), fmpq(1), 2 * gam, fmpq(6, 5), 1 + gam):
    Na = int(((2 - aa) / dq).floor())
    ret = [1 - (j + 1) * dq for j in range(Na)]
    assert all(e >= aa - 1 for e in ret) and 1 - (Na + 1) * dq < aa - 1
    rowsC.append((float(aa), Na, [float(e) for e in ret]))
    print("(C1) a = %+.6f: N_a = %d, retained ladder exponents %s" % (float(aa), Na, ", ".join("%.6f" % float(e)
                                                                                         for e in ret)))
aa = fmpq(-19, 10)
E = [gam, gam - 2, fmpq(-13, 10), fmpq(-1)]
D = sorted({1 - e for e in E})
sums = {fmpq(0)}
frontier = {fmpq(0)}
while frontier:
    new = {s + d for s in frontier for d in D if s + d <= 2 - aa} - sums
    sums |= new
    frontier = new
sums.discard(fmpq(0))
Ebar = sorted({1 - s for s in sums}, reverse=True)
assert all(e in Ebar for e in E) and all(aa - 1 <= e <= gam for e in Ebar)
for e in Ebar:
    for f in Ebar:
        if e + f - 1 >= aa - 1:
            assert e + f - 1 in Ebar
nonl = [e for e in Ebar if not ladder(e)]
for qv in nonl:
    for e in Ebar:
        f = qv + 1 - e
        if f in Ebar:
            assert e > qv and f > qv and not (ladder(e) and ladder(f))
print("(C2) a = -19/10, E = {gamma, gamma - 2, -13/10, -1}: Ebar has %d exponents in [a - 1, gamma], closed under"
      " e + f - 1 >= a - 1; %d non-ladder exponents, none is e + f - 1 with e, f both on the ladder, and all products"
      " use e, f > q" % (len(Ebar), len(nonl)))
OUT["C"] = {"Na": rowsC, "Ebar_size": len(Ebar), "nonladder": len(nonl)}
print("(C) done, %.1f s" % (time.monotonic() - T0))

# =============================== (D) exact candidate sectors ===============================
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


T094 = {   # REVIEW_T4_094 part (2), logs/t4_094_review.log lines 14, 20, 26, 32, 38: first nonzero residual sectors
    "state131": [((2, 0), 0.182079), ((3, 0), 4.25282), ((4, 0), 33.2925), ((5, 0), 103.915), ((1, 1), 111.64),
                 ((6, 0), 111.985)],
    "d2": [((7, 0), 3081.27), ((8, 0), 4331.16), ((4, 1), 142588.0), ((9, 0), 15155.6)],
    "Mpen2": [((7, 0), 3081.27), ((3, 1), 1021.96), ((8, 0), 4331.16), ((4, 1), 137891.0), ((9, 0), 15155.6)],
    "C1-N1-005": [((4, 1), 68190.4), ((9, 0), 35192.4)],
    "C1-N1-007": [((4, 1), 4905.09), ((9, 0), 35192.4)],
}
RES = {}
KMAX = 9
for name in ["state131", "d2", "Mpen2", "C1-N1-005", "C1-N1-007"]:
    t1 = time.monotonic()
    c, chi = load(name)
    delta, R, S = build(c, chi)
    assert c == c_run
    expo = lambda K, L: 1 - K * delta - 2 * L
    Th, Ps = {}, {}
    for src, dst in ((R, Th), (S, Ps)):
        for (j, nn), P in src.items():
            for L, v in enumerate(r_expansion(wjet(P), (j + 1) * delta / 2)):
                if v != 0:
                    put(dst.setdefault((j + 1, L), {}), nn, v)
    keys = [(K, L) for K in range(1, KMAX + 1) for L in range(LJ)]
    assert len({expo(*kk) for kk in keys}) == len(keys)
    pois = all(poisson(Th.get(kk, {}), expo(*kk)) == Ps.get(kk, {}) for kk in keys)
    coef = {}
    for (K, L) in keys:
        qv = expo(K, L)
        o = scale(Th.get((K, L), {}), c * qv - 1)
        for K1 in range(1, K):
            for L1 in range(L + 1):
                K2, L2 = K - K1, L - L1
                if (K1, L1) in Ps and (K2, L2) in Th:
                    o = add(o, Bterm(Ps[(K1, L1)], Th[(K2, L2)], expo(K1, L1), expo(K2, L2)))
        coef[(K, L)] = o
    order = sorted(keys, key=lambda kk: -float(expo(*kk)))
    nz = [kk for kk in order if coef[kk]]
    first = nz[0]
    qstar = expo(*first)
    dens_nl = [kk for kk in order if kk[1] == 1 and Th.get(kk)]
    cmp_ = []
    for kk, val in T094[name]:
        mine = l2(coef[kk])
        cmp_.append((kk, val, mine, abs(mine / val - 1)))
        assert abs(mine / val - 1) < 1e-5
    RES[name] = {"sectors_nonzero": [(kk, float(expo(*kk)), l2(coef[kk])) for kk in nz],
                 "first": first, "qstar": str(qstar), "a_excluded_up_to": float(qstar + 1),
                 "poisson_all_sectors": pois, "density_L1_nonzero": dens_nl, "compare_T4_094": cmp_,
                 "seconds": time.monotonic() - t1}
    print("(D) %-9s (1) holds exactly in all %d sectors (K <= %d, L <= 1): %s" % (name, len(keys), KMAX, pois))
    print("     coefficients (10), exactly zero: %s"
          % ", ".join("(%d,%d)" % kk for kk in order if not coef[kk]))
    print("     nonzero, by exponent: %s" % ", ".join("(%d,%d) %+.6f [%.6g]" % (kk + (float(expo(*kk)), l2(coef[kk])))
                                                  for kk in nz))
    print("     nonzero density sectors with L = 1: %s" % (", ".join("(%d,%d)" % kk for kk in dens_nl) or "none"))
    print("     largest nonzero coefficient at (%d,%d), q* = %.9f: E_a class excluded for -2 < a <= q* + 1 = %.9f;"
          " agreement with REVIEW_T4_094 sector norms (relative) %s; %.1f s"
          % (first + (float(qstar), float(qstar + 1), "%.1e" % max(t[3] for t in cmp_), time.monotonic() - t1)))
OUT["D"] = RES
(HERE / "data/t4_249_review_results.json").write_text(json.dumps(OUT, indent=1, default=str))
print("wrote data/t4_249_review_results.json; total %.1f s" % (time.monotonic() - T0))
