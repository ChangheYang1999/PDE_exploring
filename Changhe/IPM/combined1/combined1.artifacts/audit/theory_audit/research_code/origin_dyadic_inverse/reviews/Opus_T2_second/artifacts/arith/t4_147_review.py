"""Independent check of T4-147 (c1-t4 research/origin_dyadic_inverse/APPLICATION_007.md and code/check_007.py) and of
the exponent algebra of T4-145/T4-146 (c1-t2 reviews/REVIEW_T4_146.md).

Run from artifacts/:  python3 -B arith/t4_147_review.py
A few seconds on one core. Output: logs/t4_147_review.log and data/t4_147_review_results.json.
Parts:
  (1) sympy: alpha_h - alpha_v = 2q(c-1) - a0; under (3) alpha_h <= (2c-1)(q-3) and B < 0 for q < 3;
      d/ds of (d-s)^2 s(1+s) and its root s_star; derivative of (1+c-ca)/(1+a).
  (2) origin conditions of C1-N1-007-d2w-j7-e2bal from the c1-n1 generator list in data/ (own Legendre conversion
      and polar differentiation, code copied from arith/weighted_weak_sharp.py; not c1-t4's canonical file or
      reproduce.py): smoothness orders of every rho and psi mode, a0, strain, c + strain = 1, a0 >= 5c - 4, and
      agreement with the a0 enclosure stored by c1-t4.
  (3) H(c-1): the closed form (19) in arb, and an upper bound by subdivision that does not use (19).
  (4) the seven-cell cover (20) recomputed from the mode-1 and mode-3 norms (copies of the c1-t4 files in
      data/t4_147_inputs/, sha256 checked against the hashes recorded by check_007.py), plus the same cells with
      modes 1..15 (information only).
  (5) remark: the combined ceiling from M >= max(1/(c-1-s), 1/beta_inf(a)) (T4-146 and T4-097 together).
"""
import json
import sys
import time
from hashlib import sha256
from pathlib import Path

import sympy as sp
from flint import arb, ctx, fmpq, fmpq_poly

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parents[1]
T0 = time.monotonic()
OUT = {}

# =============================== (1) sympy ===============================
q_, c_, a0_, s_, d_, a_ = sp.symbols("q c a0 s d a", real=True)
alpha_v = q_ - c_ - 1
alpha_h = q_ * (2 * c_ - 1) - c_ - 1 - a0_
assert sp.expand(alpha_h - alpha_v - (2 * q_ * (c_ - 1) - a0_)) == 0
# a0 >= 5c - 4: alpha_h <= alpha_h|_(a0 = 5c - 4) = (2c - 1)(q - 3)
assert sp.expand(alpha_h.subs(a0_, 5 * c_ - 4) - (2 * c_ - 1) * (q_ - 3)) == 0
# B = 2q(c-1) - a0 <= 2q(c-1) - 5c + 4 < 6(c-1) - 5c + 4 = c - 2 for q < 3, c > 1
assert sp.expand((2 * q_ * (c_ - 1) - 5 * c_ + 4).subs(q_, 3) - (c_ - 2)) == 0
# q = 2 + s: alpha_v = s + 1 - c
assert sp.expand(alpha_v.subs(q_, 2 + s_) - (s_ + 1 - c_)) == 0
f2 = (d_ - s_) ** 2 * s_ * (1 + s_)
assert sp.expand(sp.diff(f2, s_) - (d_ - s_) * (-4 * s_**2 + (2 * d_ - 3) * s_ + d_)) == 0
sstar = (2 * d_ - 3 + sp.sqrt((2 * d_ - 3) ** 2 + 16 * d_)) / 8
assert sp.simplify(sp.expand(4 * sstar**2 + (3 - 2 * d_) * sstar - d_)) == 0
cl = (1 + c_ - c_ * a_) / (1 + a_)
assert sp.simplify(sp.diff(cl, a_) + (1 + 2 * c_) / (1 + a_) ** 2) == 0
print("(1) sympy: alpha_h - alpha_v = 2q(c-1) - a0; a0 = 5c-4 gives alpha_h = (2c-1)(q-3); B|_(q=3, a0=5c-4) = c - 2;")
print("    d/ds (d-s)^2 s(1+s) = (d-s)(-4s^2 + (2d-3)s + d), s_star solves 4s^2 + (3-2d)s - d = 0;"
      " d/da (1+c-ca)/(1+a) = -(1+2c)/(1+a)^2")

# =============================== (2) origin conditions from the generator list ===============================
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


def load(fn):
    d = json.loads((HERE / "data" / fn).read_text())
    c = fmpq(*map(int, d.get("cl", d.get("cl_exact")).split("/")))
    chi = {}
    for g in d["generators"]:
        num, den = (g["coef"].split("/") + ["1"])[:2]
        co = fmpq(int(num), int(den))
        sp_ = g["spec"]
        if sp_[0] == "mono":
            T = tp**sp_[1]
        else:
            assert sp_[0] == "leg"
            T = tp**sp_[1] * legendre_shift(sp_[2])
        addto(chi, (g["j"], 2 * g["m"]), co * tp**g["m"] * T)
    return c, chi


def build(c, chi):
    delta = 1 - 1 / c
    beta = lambda j: -(3 + 1 / c - j * delta) / 2       # W^(-p_j)
    lapc = {}
    for (j, n), P in chi.items():                        # e = 0 -> -2
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

    rho3 = dy_cos(lapc, -2)                                # -rho, at e = -3
    psi2 = dy_cos(dx_cos(chi, 0), -1)                      # psi = chi_xy, at e = -2
    t2 = tp * tp
    R, S = {}, {}
    for key, P in rho3.items():
        q, rem = divmod(-P, t2)
        assert rem == 0, ("rho not divisible by t^2", key)
        if q != 0:
            R[key] = q
    for key, P in psi2.items():
        q, rem = divmod(P, t2)
        assert rem == 0, ("psi not divisible by t^2", key)
        if q != 0:
            S[key] = q
    for j in {j for j, _ in list(R) + list(S)}:
        assert beta(j) + 2 == (j + 1) * delta / 2
    return delta, R, S


def val(P):                     # t-adic valuation of a nonzero polynomial
    k = 0
    while P.coeffs()[k] == 0:
        k += 1
    return k


SNAP = "c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json"
snap_sha = sha256((HERE / "data" / SNAP).read_bytes()).hexdigest()
assert snap_sha == "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21"   # T4-108 snapshot hash
c, chi = load(SNAP)
delta, R, S = build(c, chi)
# rho = r sum W^(a_j) R_jn(t) sin(n th), psi = r^2 sum W^(a_j) S_jn(t) sin(n th), t = r^2/(1+r^2), W = 1 - t.
# r t^k sin(n th) = r^(2k+1) sin(n th)(1+r^2)^(-k) is smooth iff 2k + 1 >= n; r^2 t^k sin(n th) iff 2k + 2 >= n.
assert all(n % 2 == 1 for _, n in R) and all(n % 2 == 0 and n >= 2 for _, n in S)
assert all(2 * val(P) + 1 >= n for (j, n), P in R.items())
assert all(2 * val(P) + 2 >= n for (j, n), P in S.items())
a0 = sum((P(0) for (j, n), P in R.items() if n == 1), fmpq(0))
strain = 2 * sum((P(0) for (j, n), P in S.items() if n == 2), fmpq(0))
assert 1 < c < 2 and c + strain == 1 and a0 >= 5 * c - 4 and a0 > 0
ctx.prec = 512
A = lambda x: arb(x.p) / arb(x.q)
stored = json.loads((HERE / "data/t4_147_inputs/candidate007_origin_cover.json").read_text())
assert A(a0).overlaps(arb(stored["a0"])) and fmpq(*map(int, stored["c"].split("/"))) == c
assert fmpq(*map(int, stored["strain"].split("/"))) == strain
print(f"(2) C1-N1-007 snapshot sha256 {snap_sha[:16]}... (T4-108 hash): c = {c}; rho modes {len(R)}, psi modes {len(S)};"
      f" every rho mode r t^k sin(n th) has 2k+1 >= n and every psi mode 2k+2 >= n (smooth at 0)")
print(f"    a0 = rho_y(0) = {A(a0).str(25)}; strain = d_y u2(0) = {strain}; c + strain = 1 exactly;"
      f" a0 - (5c - 4) = {A(a0 - 5 * c + 4).str(20)} > 0; overlaps the c1-t4 a0 enclosure; strain equal")
print("    hence V(0) = 0, DV(0) = diag(2c-1, 1), grad rho(0) = (0, a0): the second-order Taylor part of psi is 2 S(0) x y")
OUT["origin"] = dict(snapshot_sha256=snap_sha, c=str(c), a0=A(a0).str(40, radius=True), strain=str(strain),
                     a0_minus_5c_minus_4=A(a0 - 5 * c + 4).str(30, radius=True))

# =============================== (3) H(c-1) ===============================
d = c - 1
da = A(d)
ss = (2 * da - 3 + ((2 * da - 3) ** 2 + 16 * da).sqrt()) / 8
Hc = (da - ss) * (4 * arb.pi() * ss * (1 + ss)).sqrt()
Hup = fmpq(57, 50)
assert Hc < A(Hup) and abs(4 * ss * ss + (3 - 2 * da) * ss - da) < arb(10) ** -100
# subdivision bound not using (19): on [s0, s1] in (0, d), (d - s) sqrt(4 pi s(1+s)) <= (d - s0) sqrt(4 pi s1(1+s1))
NSUB = 4096
sub = arb(0)
for i in range(NSUB):
    s0, s1 = d * fmpq(i, NSUB), d * fmpq(i + 1, NSUB)
    v = A(d - s0) * (4 * arb.pi() * A(s1) * A(1 + s1)).sqrt()
    sub = v if v.upper() > sub.upper() else sub
assert sub < A(Hup)
print(f"(3) s_star = {ss.str(20)}, H(c-1) = {Hc.str(20)} (closed form (19));"
      f" subdivision bound ({NSUB} cells, no closed form): H(c-1) <= {float(sub.upper()):.10f} < 57/50")
OUT["H"] = dict(s_star=ss.str(30, radius=True), H=Hc.str(30, radius=True), subdivision_upper=float(sub.upper()),
                H_upper="57/50")

# =============================== (4) seven-cell cover ===============================
HASH = {1: "4ab221a4d20c04f0b449601ae673cb9b71cbfdef88f80980a070b20b73669eb6",
        3: "9d6f00a63aeaa61e59b84528743105ca96661e4f3c34ef81b79e79730693c3fb"}
mode = {}
for n in (1, 3, 5, 7, 9, 11, 13, 15):
    p = HERE / f"data/t4_147_inputs/candidate007_mode{n}.json"
    if n in HASH:
        assert sha256(p.read_bytes()).hexdigest() == HASH[n]
    dd = json.loads(p.read_text())
    assert dd["angular_modes"] == [n]
    mode[n] = {fmpq(*(list(map(int, r["a"].split("/"))) + [1])[:2]): arb(r["projected_norm"]) for r in dd["rows"]}
cA = 1 + 1 / c
assert fmpq(3, 2) < cA < fmpq(7, 4)
edges = [fmpq(k, 4) for k in range(7)] + [cA]
rows = []
print("(4) cells [l, h], N evaluated at e (e = h, last e = 7/4 > 1 + 1/c); lower 5^((l-2)/2) N13(e), upper (57/50)(1+c-cl)/(1+l)")
for i, (l, h) in enumerate(zip(edges, edges[1:])):
    e = h if i < 6 else fmpq(7, 4)
    n13 = (mode[1][e] ** 2 + mode[3][e] ** 2).sqrt()
    nall = sum((mode[n][e] ** 2 for n in mode), arb(0)).sqrt()
    lo = arb(5) ** (A(l - 2) / 2)
    up = A(Hup * (1 + c - c * l) / (1 + l))
    up_exact = Hc * A((1 + c - c * l) / (1 + l))
    r13, rall = lo * n13 / up, lo * nall / up
    assert r13 > 1
    rows.append(dict(l=str(l), h=str(h), e=str(e), N13=n13.str(20, radius=True), ratio13=r13.str(15, radius=True),
                     ratio13_exactH=(lo * n13 / up_exact).str(15, radius=True), ratio_modes_1_15=rall.str(15, radius=True)))
    print(f"    [{str(l):>4s}, {str(h) if i < 6 else '1+1/c':>5s}] e = {str(e):4s}: N13 = {n13.str(12)}, ratio {r13.str(12)}"
          f" (with H itself {(lo * n13 / up_exact).str(10)}); modes 1..15: {rall.str(10)}")
OUT["cells"] = rows
print(f"    minimum ratio over the seven cells (57/50 ceiling): {min(float(arb(r['ratio13']).lower()) for r in rows):.15f}")

# =============================== (5) combined ceiling (remark) ===============================
# With C_U >= 1: Y(F) < beta/(1+a) * sup_(0<s<c-1) min(c-1-s, beta) sqrt(4 pi s(1+s)),  beta = 1 + c - c a.
# If beta >= c-1-s_star the sup is H(c-1); otherwise it is beta sqrt(4 pi (c-1-beta)(c-beta)) (attained at s = c-1-beta).
print("(5) combined ceiling / T4-146 ceiling (18) and / T4-097 ceiling sqrt(8 pi) beta^2/(1+a), FLOAT")
cf = float(c.p) / float(c.q)
import math
Hf = float(Hc.mid())
ssf = float(ss.mid())
comb = []
for af in (0.0, 0.5, 1.0, 1.2, 1.25, 1.3, 1.4, 1.5, 1.55):
    b = 1 + cf - cf * af
    if b <= 0:
        continue
    sup = Hf if b >= cf - 1 - ssf else b * math.sqrt(4 * math.pi * (cf - 1 - b) * (cf - b))
    c146, c097 = Hf * b / (1 + af), math.sqrt(8 * math.pi) * b * b / (1 + af)
    cc = b * sup / (1 + af)
    comb.append(dict(a=af, beta=b, combined=cc, T4_146=c146, T4_097=c097))
    print(f"    a = {af:4.2f}: beta = {b:.4f}; combined {cc:.5f}; T4-146 {c146:.5f}; T4-097 {c097:.5f}; ratios"
          f" {cc / c146:.4f}, {cc / c097:.4f}")
print(f"    switch point: beta = c - 1 - s_star = {cf - 1 - ssf:.6f}, a = {(1 + cf - (cf - 1 - ssf)) / cf:.6f}")
OUT["combined"] = comb
OUT["elapsed_seconds"] = time.monotonic() - T0
(HERE / "data/t4_147_review_results.json").write_text(json.dumps(OUT, indent=1))
print(f"done in {time.monotonic() - T0:.1f} s; wrote data/t4_147_review_results.json")
