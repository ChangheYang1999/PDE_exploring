"""Independent review of T4-234 (c1-t4 research/triangular_tail_equations/PROOF.md, sha256 b69f785a...c60b6a):
canonical cutoff velocity of finitely many homogeneous tails and the triangular equations for the nonintegrable
profiles (reviews/REVIEW_T4_234.md).

Run from artifacts/:  python3 -B arith/t4_234_review.py
Needs sympy, numpy, scipy, python-flint.

Parts:
  (A) sympy: symbol identities of U; the polar forms used in (1), (5), (8); c e_j - 1 = -j(c - 1) and
      e_l + e_m - 1 = e_(l+m+1); the potential-endpoint contract formulas of the PROOF (rho = -d_y Lap Phi,
      psi = d_x d_y Phi, Phi = r^d cos(n th)); the dilation weights; N at the run value of c.
  (B) FLOAT: the cutoff construction (6) for one tail r^gamma Theta: support and moments of g, decay of w, and the
      comparison of U[R] at a point inside r < 1 with the radially truncated Biot-Savart integrals of R.
  (C) exact (fmpq): for the five candidates of t4_094_review.py, the endpoint profiles Theta_j, Psi_j of the frozen
      potential data (full polynomial route of t4_094_review.py, not the endpoint contract), the angular Poisson
      equation (1), the sector coefficients E_j of (8), and the profiles predicted from Theta_0 alone by (4).
Output: logs/t4_234_review.log, data/t4_234_review_results.json.
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
x1, x2 = sp.symbols("xi1 xi2", real=True)
symU = sp.Matrix([x1 * x2 / (x1**2 + x2**2), -x1**2 / (x1**2 + x2**2)])
curl = sp.simplify(sp.I * x1 * symU[1] - sp.I * x2 * symU[0])
div = sp.simplify(sp.I * x1 * symU[0] + sp.I * x2 * symU[1])
mod2 = sp.simplify(symU[0]**2 + symU[1]**2)
assert sp.simplify(curl - (-sp.I * x1)) == 0 and div == 0 and sp.simplify(mod2 - x1**2 / (x1**2 + x2**2)) == 0
print("(A1) symbol of U: curl U = -d_x, div U = 0, |symbol|^2 = xi1^2/|xi|^2 <= 1")

r, th, e, el, em, cc, g = sp.symbols("r theta e e_l e_m c gamma", positive=True)
Psi, Theta, Psil, Thm = (sp.Function(n) for n in ("Psi", "Theta", "Psi_l", "Theta_m"))


def lap(f):
    return sp.diff(f, r, 2) + sp.diff(f, r) / r + sp.diff(f, th, 2) / r**2


def dx(f):
    return sp.cos(th) * sp.diff(f, r) - sp.sin(th) / r * sp.diff(f, th)


def dy(f):
    return sp.sin(th) * sp.diff(f, r) + sp.cos(th) / r * sp.diff(f, th)


psi = r**(e + 1) * Psi(th)
assert sp.simplify(lap(psi) - r**(e - 1) * (sp.diff(Psi(th), th, 2) + (e + 1)**2 * Psi(th))) == 0
rhs1 = r**(e - 1) * (-e * sp.cos(th) * Theta(th) + sp.sin(th) * sp.diff(Theta(th), th))
assert sp.simplify(-dx(r**e * Theta(th)) - rhs1) == 0
print("(A2) Lap(r^(e+1) Psi) = r^(e-1)[Psi'' + (e+1)^2 Psi] and -d_x(r^e Theta) = r^(e-1)[-e cos Theta + sin Theta']")
u1, u2 = -dy(psi), dx(psi)                        # grad-perp psi = (-psi_y, psi_x)
ur = sp.cos(th) * u1 + sp.sin(th) * u2
ut = -sp.sin(th) * u1 + sp.cos(th) * u2
assert sp.simplify(ur + r**e * sp.diff(Psi(th), th)) == 0 and sp.simplify(ut - (e + 1) * r**e * Psi(th)) == 0
curlu = sp.simplify(dx(u2) - dy(u1) - lap(psi))
assert curlu == 0
print("(A3) velocity (5): grad-perp(r^(e+1) Psi) = r^e[-Psi' e_r + (e+1) Psi e_theta]; curl = Lap psi")
psil = r**(el + 1) * Psil(th)
url = sp.cos(th) * (-dy(psil)) + sp.sin(th) * dx(psil)
utl = -sp.sin(th) * (-dy(psil)) + sp.cos(th) * dx(psil)
fm = r**em * Thm(th)
adv = url * sp.diff(fm, r) + utl * sp.diff(fm, th) / r
Blm = -em * sp.diff(Psil(th), th) * Thm(th) + (el + 1) * Psil(th) * sp.diff(Thm(th), th)
assert sp.simplify(adv - r**(el + em - 1) * Blm) == 0
print("(A4) u_l . grad(r^(e_m) Theta_m) = r^(e_l + e_m - 1) B_(l,m) with B of (2)")
jj, ll, mm = sp.symbols("j l m", integer=True, nonnegative=True)
dl = 1 - g
ej = lambda k: 1 - (k + 1) * dl
assert sp.simplify(r * sp.diff(r**ej(jj), r) / g - r**ej(jj) - (-jj * (1 / g - 1)) * r**ej(jj)) == 0
assert sp.simplify(ej(ll) + ej(mm) - 1 - ej(ll + mm + 1)) == 0
assert sp.simplify(ej(0) - g) == 0
print("(A5) c e_j - 1 = -j(c - 1) (c = 1/gamma), e_l + e_m - 1 = e_(l+m+1), e_0 = gamma")

dd = sp.Symbol("d")
cont = []
rng = np.random.default_rng(234)
for n in (0, 2, 4, 6, 8, 10):
    Phi = r**dd * sp.cos(n * th)
    rho_ = -dy(lap(Phi))
    psi_ = dx(dy(Phi))
    S = lambda k: sp.sin(k * th)
    rho_c = r**(dd - 3) * (-(dd**2 - n**2) * (dd - 2 - n) / 2 * S(n + 1) + (dd**2 - n**2) * (dd - 2 + n) / 2 * S(n - 1))
    psi_c = r**(dd - 2) * ((dd - n) * (dd - n - 2) / 4 * S(n + 2) - (dd + n) * (dd + n - 2) / 4 * S(n - 2))
    for _ in range(6):                                  # sin(-k th) = -sin(k th) and sin(0) = 0 are built in
        sub = {dd: sp.Rational(int(rng.integers(-40, 40)), 7), r: sp.Rational(int(rng.integers(5, 40)), 9),
               th: sp.Rational(int(rng.integers(1, 600)), 97)}
        assert abs(sp.N((rho_ - rho_c).subs(sub), 60)) < 1e-45 and abs(sp.N((psi_ - psi_c).subs(sub), 60)) < 1e-45
    cont.append(n)
print("(A6) contract formulas of the PROOF (density sin(n+-1), stream sin(n+-2), negative index reverses sign, index 0"
      " vanishes) agree with rho = -d_y Lap Phi, psi = d_x d_y Phi for Phi = r^d cos(n th), n =", cont,
      "(6 random rational points (d, r, theta) each, 60 digits, |difference| < 1e-45)", flush=True)
lam = sp.Symbol("lambda", positive=True)
assert sp.simplify(lam * (r / lam)**ej(jj) - (lam**dl)**(jj + 1) * r**ej(jj)) == 0
print("(A7) lambda rho(X/lambda): tail j is multiplied by (lambda^delta)^(j+1)")
c_run = fmpq(4076476460239181, 2**51)
dq = 1 - 1 / c_run
Nrun = int((2 / dq).floor())
ejs = [1 - (k + 1) * dq for k in range(Nrun + 1)]
print("(A8) run c = 4076476460239181/2^51: delta = %.12f, 2/delta = %.9f, N = %d; e_j ="
      % (float(dq), float(2 / dq), Nrun),
      ", ".join("%.9f" % float(v) for v in ejs), "(e_N < -1)")
assert Nrun == 4 and ejs[3] >= -1 > ejs[4]
print("     N = 4 exactly for 1/2 <= gamma < 3/5 (2/delta in [4, 5)); the PROOF states 1/2 < gamma < 3/5")
OUT["A"] = {"N_run": Nrun, "e_j": [str(v) for v in ejs]}
print("(A) done, %.1f s" % (time.monotonic() - T0))

# =============================== (B) FLOAT: cutoff construction ===============================
gam = float(1 / c_run)
eB = gam
TH = {1: 1.0, 3: 0.3}                                        # Theta = sin th + 0.3 sin 3 th
# Psi from (1): rhs coefficients
rhsB = {}
for n, a in TH.items():
    rhsB[n + 1] = rhsB.get(n + 1, 0) + a * (n - eB) / 2
    if n - 1 > 0:
        rhsB[n - 1] = rhsB.get(n - 1, 0) - a * (n + eB) / 2
PSB = {m: v / ((eB + 1)**2 - m * m) for m, v in rhsB.items()}
ThS = sum(a * sp.sin(n * th) for n, a in TH.items())
PsS = sum(a * sp.sin(m * th) for m, a in PSB.items())
chi_in = sp.exp(-1 / (r - 1)) / (sp.exp(-1 / (r - 1)) + sp.exp(-1 / (2 - r)))
gexpr = lap(chi_in * r**(eB + 1) * PsS) + dx(chi_in * r**eB * ThS)
gfun = sp.lambdify((r, th), gexpr, "numpy")
# check: outside the transition region g vanishes (chi = 1 there), via the closed form with chi = 1
assert abs(sp.N((lap(r**(eB + 1) * PsS) + dx(r**eB * ThS)).subs({r: 3.7, th: 0.9}))) < 1e-12
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(160)
rq = 1.5 + 0.5 * xg
wr = 0.5 * wg
nth = 512
tq = 2 * np.pi * np.arange(nth) / nth
RR, TT = np.meshgrid(rq, tq, indexing="ij")
GG = gfun(RR, TT)
dA = (wr * rq)[:, None] * (2 * np.pi / nth)
X1, X2 = RR * np.cos(TT), RR * np.sin(TT)
mom = {k: float(np.sum(GG * f * dA)) for k, f in (("1", 1), ("x", X1), ("y", X2), ("xy", X1 * X2))}
print("(B1) g = curl v + d_x R for Theta = sin th + 0.3 sin 3th, e = gamma: int g = %.2e, int x g = %.2e,"
      " int y g = %.2e,"
      " int xy g = %.6f" % (mom["1"], mom["x"], mom["y"], mom["xy"]))
OUT["B_moments"] = mom


def wfield(X):
    Z1, Z2 = X[0] - X1, X[1] - X2
    q = 2 * np.pi * (Z1**2 + Z2**2)
    return np.array([np.sum(-Z2 / q * GG * dA), np.sum(Z1 / q * GG * dA)])


dec = []
for R0 in (10.0, 20.0, 40.0, 80.0, 160.0, 320.0):
    X = R0 * np.array([np.cos(0.4), np.sin(0.4)])
    dec.append((R0, float(np.linalg.norm(wfield(X)) * R0**3)))
print("(B2) |w| r^3 at theta = 0.4:", ", ".join("r=%g: %.6f" % t for t in dec),
      "(w = O(r^-3): zero mean and zero first moments by parity; PROOF states O(r^-2))")
OUT["B_decay"] = dec
X0 = np.array([0.2, 0.3])
Ucan = -wfield(X0)                                    # v = 0 near X0 since chi = 0 there


def Kint(rnodes, rweights):
    RR2, TT2 = np.meshgrid(rnodes, tq, indexing="ij")
    Y1, Y2 = RR2 * np.cos(TT2), RR2 * np.sin(TT2)
    chv = np.where(RR2 >= 2, 1.0, 0.0)
    m = (RR2 > 1) & (RR2 < 2)
    ri = RR2[m]
    chv[m] = np.exp(-1 / (ri - 1)) / (np.exp(-1 / (ri - 1)) + np.exp(-1 / (2 - ri)))
    f = chv * RR2**eB * sum(a * np.sin(n * TT2) for n, a in TH.items())
    Z1, Z2 = X0[0] - Y1, X0[1] - Y2
    q = (Z1**2 + Z2**2)
    K1 = -Z1 * Z2 / (np.pi * q**2)
    K2 = (Z1**2 - Z2**2) / (2 * np.pi * q**2)
    dA2 = (rweights * rnodes)[:, None] * (2 * np.pi / nth)
    return np.array([np.sum(K1 * f * dA2), np.sum(K2 * f * dA2)])


acc = Kint(rq, wr)
rows = []
lo = 2.0
for Lk in range(1, 13):
    hi = 10.0**Lk
    if hi <= lo:
        continue
    edges = np.geomspace(lo, hi, 9)                   # log-spaced Gauss pieces
    for p_, q_ in zip(edges[:-1], edges[1:]):
        xs, ws = leggauss(40)
        nodes = (p_ + q_) / 2 + (q_ - p_) / 2 * xs
        acc = acc + Kint(nodes, (q_ - p_) / 2 * ws)
    lo = hi
    rows.append((Lk, float(acc[0]), float(acc[1]), float(np.linalg.norm(acc - Ucan))))
print("(B3) canonical U[R](X0), X0 = (0.2, 0.3): (%.10f, %.10f)" % tuple(Ucan))
for Lk, a1, a2, dlt in rows:
    print("     truncated Biot-Savart over 1 < |Y| < 10^%d: (%.10f, %.10f), distance %.3e" % (Lk, a1, a2, dlt))
OUT["B_trunc"] = {"Ucan": [float(v) for v in Ucan], "rows": rows}
print("(B) done, %.1f s" % (time.monotonic() - T0))

# =============================== (C) exact candidate profiles ===============================
tp = fmpq_poly([0, 1])
Wq = fmpq_poly([1, -1])


def Top(P, beta, e):
    return fmpq_poly([e, -2 * beta]) * P + 2 * tp * Wq * P.derivative()


def legendre_shift(n):          # P_n(2t - 1)
    xx = fmpq_poly([-1, 2])
    p0, p1 = fmpq_poly([1]), xx
    if n == 0:
        return p0
    for m in range(1, n):
        p0, p1 = p1, (fmpq(2 * m + 1, m + 1) * xx * p1 - fmpq(m, m + 1) * p0)
    return p1


def addto(d, key, P):
    d[key] = d.get(key, fmpq_poly([0])) + P


def load(name):                 # copied from t4_094_review.py
    if name == "state131":
        d = json.loads((HERE / "data/a2_state131_exact.json").read_text())
        c = fmpq(*map(int, d["exact_parameters"]["cl"].split("/")))
        chi = {}
        for (j, m, kk), co in zip(d["canonical_order"], d["canonical_coefficients"]):
            addto(chi, (j, 2 * m), fmpq(*map(int, co.split("/"))) * tp**kk)
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


def build(c, chi):              # copied from t4_094_review.py
    delta = 1 - 1 / c
    beta = lambda j: -(3 + 1 / c - j * delta) / 2       # W^(-p_j)
    lapc = {}
    for (j, n), P in chi.items():
        TP = Top(P, beta(j), 0)
        addto(lapc, (j, n), Top(TP, beta(j), 0) - n * n * P)

    def dy_cos(cd, e):
        out = {}
        for (j, n), P in cd.items():
            TP = Top(P, beta(j), e)
            addto(out, (j, n + 1), fmpq(1, 2) * (TP - n * P))
            if n - 1 > 0:
                addto(out, (j, n - 1), fmpq(-1, 2) * (TP + n * P))
            elif n - 1 < 0:
                addto(out, (j, 1), fmpq(1, 2) * (TP + n * P))
        return out

    def dx_cos(cd, e):
        out = {}
        for (j, n), P in cd.items():
            TP = Top(P, beta(j), e)
            addto(out, (j, n + 1), fmpq(1, 2) * (TP - n * P))
            addto(out, (j, abs(n - 1)), fmpq(1, 2) * (TP + n * P))
        return out

    rho3 = dy_cos(lapc, -2)
    psi2 = dy_cos(dx_cos(chi, 0), -1)
    t2 = tp * tp
    R, S = {}, {}
    for key, P in rho3.items():
        q, rem = divmod(-P, t2)
        assert rem == 0
        if q != 0:
            R[key] = q
    for key, P in psi2.items():
        q, rem = divmod(P, t2)
        assert rem == 0
        if q != 0:
            S[key] = q
    for j in {j for j, _ in list(R) + list(S)}:
        assert beta(j) + 2 == (j + 1) * delta / 2
    return delta, R, S


def put(o, n, v):
    if n == 0 or v == 0:
        return
    if n < 0:
        n, v = -n, -v
    o[n] = o.get(n, fmpq(0)) + v
    if o[n] == 0:
        del o[n]


def sin_cos(S, C):              # (sum S_a sin a th)(sum C_b cos b th) as a sine series
    o = {}
    for a, sa in S.items():
        for b, cb in C.items():
            v = sa * cb / 2
            put(o, a + b, v)
            put(o, a - b, v)
    return o


def dsin(S):
    return {n: n * v for n, v in S.items()}


def add(A, B, s=fmpq(1)):
    o = dict(A)
    for n, v in B.items():
        put(o, n, s * v)
    return o


def scale(A, s):
    return {n: s * v for n, v in A.items() if s * v != 0}


def poisson(Th, e):
    rhs = add(scale(sin_cos(Th, {1: fmpq(1)}), -e), sin_cos({1: fmpq(1)}, dsin(Th)))
    assert all(n % 2 == 0 for n in rhs)
    return {m: v / ((e + 1)**2 - m * m) for m, v in rhs.items()}


def Bterm(Psl, Thm_, el_, em_):
    return add(scale(sin_cos(Thm_, dsin(Psl)), -em_), scale(sin_cos(Psl, dsin(Thm_)), el_ + 1))


def l2(A):                      # L2(0, 2 pi) norm, float
    return float(np.sqrt(np.pi * sum(float(v)**2 for v in A.values())))


RES, PROF = {}, {}
for name in ["state131", "d2", "Mpen2", "C1-N1-005", "C1-N1-007"]:
    t1 = time.monotonic()
    c, chi = load(name)
    delta, R, S = build(c, chi)
    N = int((2 / delta).floor())
    e_ = [1 - (j + 1) * delta for j in range(N)]
    Th = [{n: P(fmpq(1)) for (jj_, n), P in R.items() if jj_ == j and P(fmpq(1)) != 0} for j in range(N)]
    Ps = [{n: P(fmpq(1)) for (jj_, n), P in S.items() if jj_ == j and P(fmpq(1)) != 0} for j in range(N)]
    row = {"c": str(c), "gamma": float(1 / c), "N": N, "e_j": [float(v) for v in e_]}
    pois = []
    for j in range(N):
        assert all(n % 2 == 1 for n in Th[j]) and all(n % 2 == 0 for n in Ps[j])
        pois.append(poisson(Th[j], e_[j]) == Ps[j])
    row["poisson_exact"] = pois
    Ej, pred = [], [Th[0]]
    PsP = [poisson(Th[0], e_[0])]
    for j in range(1, N):
        nl = {}
        for l in range(j):
            nl = add(nl, Bterm(Ps[l], Th[j - 1 - l], e_[l], e_[j - 1 - l]))
        E = add(scale(Th[j], -j * (c - 1)), nl)
        Ej.append({"j": j, "nonzero": len(E), "L2": l2(E), "maxabs": max([abs(float(v)) for v in E.values()] or [0.0]),
                   "freq": [min(E), max(E)] if E else []})
        nlp = {}
        for l in range(j):
            nlp = add(nlp, Bterm(PsP[l], pred[j - 1 - l], e_[l], e_[j - 1 - l]))
        pred.append(scale(nlp, 1 / (j * (c - 1))))
        PsP.append(poisson(pred[j], e_[j]))
    row["E"] = Ej
    row["harmonics"] = [(len(Th[j]), max(Th[j]) if Th[j] else 0) for j in range(N)]
    row["pred_equals_candidate"] = [pred[j] == Th[j] for j in range(N)]
    row["profile_L2"] = [l2(Th[j]) for j in range(N)]
    row["seconds"] = time.monotonic() - t1
    RES[name] = row
    PROF[name] = (c, Th)
    print("(C) %-9s c = %.12f gamma = %.9f N = %d; (1) exact for j = 0..%d: %s; candidate Theta_j harmonics"
          " (count, max): %s"
          % (name, float(c), float(1 / c), N, N - 1, all(pois), row["harmonics"]))
    for E in Ej:
        print("     E_%d: nonzero coefficients %d, L2 norm %.6e, max |coef| %.3e, sine frequencies %s"
              % (E["j"], E["nonzero"], E["L2"], E["maxabs"], E["freq"]))
    print("     Theta_j predicted from Theta_0 by (4) equals the candidate profile: %s; ||Theta_j||_L2 = %s; %.1f s"
          % (row["pred_equals_candidate"], ", ".join("%.6e" % v for v in row["profile_L2"]), row["seconds"]))
names = list(PROF)
same = {}
for a_ in names:
    for b_ in names:
        if a_ < b_:
            same[a_ + "|" + b_] = [PROF[a_][0] == PROF[b_][0]] + [PROF[a_][1][j] == PROF[b_][1][j] for j in range(4)]
print("(C) exact equality across candidates [same c, Theta_0, Theta_1, Theta_2, Theta_3]:")
for k, v in same.items():
    print("     %-22s %s" % (k, v))
RES["cross"] = same
OUT["C"] = RES
(HERE / "data/t4_234_review_results.json").write_text(json.dumps(OUT, indent=1, default=str))
print("wrote data/t4_234_review_results.json; total %.1f s" % (time.monotonic() - T0))
