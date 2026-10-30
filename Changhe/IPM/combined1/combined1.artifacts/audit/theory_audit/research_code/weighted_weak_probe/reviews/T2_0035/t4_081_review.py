"""Independent review of T4-081 corrected (c1-t4 research/weighted_weak_probe/PROOF.md, sha256 91dd4069...0156): the
weak distance test in the decreasing weighted space H_a = L2((1+|X|^2)^(-a) dX), and an independent reproduction of
its numbers T4-085 (a = 1) and T4-088 (a = 6/5) (reviews/REVIEW_T4_081.md).

Run from artifacts/:  python3 -B arith/t4_081_review.py
Needs sympy, python-flint.  A few minutes on one core.

Independence.  The polar fields are built here from the source generator lists (not from c1-t4's canonical files):
  data/a2_state131_exact.json   = R6/source/analysis2/IPM_Analysis_II.artifacts/certificates/P18_weight_radius/
                                  state131_exact.json (canonical triples a_jmk);
  data/a2_nb_d2_exact.json      = R6/source/analysis2/IPM_Analysis_II.artifacts/numerics/data/nb_d2_exact.json;
  data/a2_nb_Mpen2_exact.json   = R6/source/analysis2/IPM_Analysis_II.artifacts/numerics/data/nb_Mpen2_exact.json;
  data/c1n1_005_d2w_j7_n4_X3_mid180_exact.json = R6/c1-shared/candidate_snapshots/C1-N1-005-d2w-j7-x3/
                                  d2w_j7_n4_X3_mid180_exact.json.
The derivative algebra, the pairing formula (derived here from the weak equation), the beta integrals (expanded in t,
recurrence in the first argument; c1-t4 expands in W) and the radius formula are coded independently. The fields are
checked against the CONFIRMED-N4 Cartesian point intervals in data/t4_017_cartesian_witnesses.json (d2 at (0, 1),
Mpen2 at (0, 2)), against the exact a0 of state 131, and against the CONFIRMED point value F(0, 1/4) = -1.4096814 of
C1-N1-005 (N4-076, T4-082). Only at the end are c1-t4's stored values (copies in data/t4_081_verification/) read, for an
overlap comparison.

Parts:
  (1) sympy: the weak identity, the derivative of phi_k, the bounds (5), (6) and H_0 = 1, the polar measure, the
      angular integrals, and the polar derivative rules used in (2);
  (2) exact polar fields from the generators; exact checks;
  (3) arb: I_k, A_k, B_k, C_k, H_k and the radius (4) at a = 1 (C_U = 2, T4-054) and a = 6/5 (C_U = 808233/500000,
      TP-2 rational certificate, CONFIRMED by T4-072), compared with c1-t4's stored values; a k scan.
"""
import json
import sys
import time
from pathlib import Path

import sympy as sp
from flint import arb, arb_poly, ctx, fmpq, fmpq_poly

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parents[1]
T0 = time.monotonic()

# =============================== (1) sympy checks ===============================
x, y = sp.symbols("x y", real=True)
c_, k_ = sp.symbols("c k", positive=True)
rr = x**2 + y**2
ts, Ws = rr / (1 + rr), 1 / (1 + rr)
psi_b, zeta, h_, rho_, phi_ = (sp.Function(nm)(x, y) for nm in ("psi_b", "zeta", "h", "rho", "phi"))
ub = (-sp.diff(psi_b, y), sp.diff(psi_b, x))           # background velocity, divergence free
Uh = (-sp.diff(zeta, y), sp.diff(zeta, x))             # U[h], divergence free
V = (c_ * x + ub[0], c_ * y + ub[1])
full = (V[0] + Uh[0]) * sp.diff(rho_ + h_, x) + (V[1] + Uh[1]) * sp.diff(rho_ + h_, y) - (rho_ + h_)
F = V[0] * sp.diff(rho_, x) + V[1] * sp.diff(rho_, y) - rho_
div = lambda a, b: sp.diff(a, x) + sp.diff(b, y)
form2 = F + div(V[0] * h_, V[1] * h_) - (2 * c_ + 1) * h_ + Uh[0] * sp.diff(rho_, x) + Uh[1] * sp.diff(rho_, y) \
    + div(h_ * Uh[0], h_ * Uh[1])
assert sp.simplify(sp.expand(full - form2)) == 0
# integrated form: phi * (2) = [F phi - h(V.Dphi + (2c+1)phi) + phi U.Drho - h U.Dphi] + divergence
rest = F * phi_ - h_ * (V[0] * sp.diff(phi_, x) + V[1] * sp.diff(phi_, y) + (2 * c_ + 1) * phi_) \
    + phi_ * (Uh[0] * sp.diff(rho_, x) + Uh[1] * sp.diff(rho_, y)) - h_ * (Uh[0] * sp.diff(phi_, x) + Uh[1] * sp.diff(phi_, y))
divterm = div(phi_ * (V[0] + Uh[0]) * h_, phi_ * (V[1] + Uh[1]) * h_)
assert sp.simplify(sp.expand(phi_ * form2 - rest - divterm)) == 0
print("(1a) (V+U[h]).D(rho+h) - (rho+h) = F + div(Vh) - (2c+1)h + U[h].D rho + div(h U[h])  (div V = 2c, div U = 0)")
print("     phi * (2) = F phi - h[(2c+1)phi + V.Dphi] + phi U[h].D rho - h U[h].Dphi + div(...): the tested identity")

phik = y * ts**k_ * Ws**2
Dphi = (sp.diff(phik, x), sp.diff(phik, y))
claim = (2 * y * x * ts**(k_ - 1) * Ws**3 * (k_ * Ws - 2 * ts),
         ts**k_ * Ws**2 + 2 * y * y * ts**(k_ - 1) * Ws**3 * (k_ * Ws - 2 * ts))
assert all(sp.simplify(Dphi[i] - claim[i]) == 0 for i in range(2))
rdr = sp.simplify(x * Dphi[0] + y * Dphi[1] - phik * (1 + 2 * k_ * (1 - ts) - 4 * ts))
assert rdr == 0
Lk = (2 * c_ + 1) * phik + c_ * (x * Dphi[0] + y * Dphi[1])
assert sp.simplify(Lk - phik * (3 * c_ + 1 + 2 * c_ * k_ * (1 - ts) - 4 * c_ * ts)) == 0
assert sp.simplify(rr * Ws / ts - 1) == 0
print("(1b) D phi_k = t^k u0^2 e_y + 2 y X t^(k-1) u0^3 (k u0 - 2t); X.D phi_k = phi_k (1 + 2k(1-t) - 4t);"
      " L_k = phi_k ell_k")
print("     |yX| u0/t <= r^2 u0/t = 1, so |D phi_k| <= t^k u0^2 (1 + 2k u0 + 4t)   (5)")
# H_0: |D phi_0|^2/u0^4 = 1 + 8 s (2t - 1) with s = y^2 u0 in [0, t]
D0 = (sp.diff(y * Ws**2, x), sp.diff(y * Ws**2, y))
sq = sp.simplify((D0[0]**2 + D0[1]**2) / Ws**4 - (1 + 8 * y**2 * Ws * (2 * ts - 1)))
assert sq == 0
tt = sp.symbols("t", positive=True)
assert sp.factor(1 - (1 - tt) * (4 * tt - 1)**2) == tt * (4 * tt - 3)**2
print("(1c) |D phi_0|^2/u0^4 = 1 + 8 s (2t - 1), s = y^2 u0 in [0, t]: angular max (1-t)^(4-2a) max(1, (4t-1)^2);")
print("     1 - (1-t)(4t-1)^2 = t (4t-3)^2 >= 0, so (1-t)^(2-a)|4t-1| <= (1-t)^(1/2)|4t-1| <= 1 for a <= 3/2: H_0 = 1")
jj, bb = sp.symbols("j b", positive=True)
g = jj * sp.log(tt) + bb * sp.log(1 - tt)
assert sp.simplify(sp.diff(g, tt).subs(tt, jj / (jj + bb))) == 0
print("     sup_[0,1] t^j (1-t)^b is attained at t = j/(j+b): S(j,b) as in (6)")
rs, th = sp.symbols("r theta", positive=True)
tr = rs**2 / (1 + rs**2)
assert sp.simplify(sp.diff(tr, rs) - 2 * rs * (1 - tr)**2) == 0 and sp.simplify(rs**2 - tr / (1 - tr)) == 0
print("(1d) dt = 2 r u0^2 dr, r^2 = t/u0: r dr = dt/(2 u0^2), r^3 dr = t dt/(2 u0^3)")
for n_, m_ in ((1, 2), (3, 2), (3, 4), (5, 4), (1, 4), (3, 6)):
    i1 = sp.integrate(sp.sin(n_ * th) * sp.sin(m_ * th) * sp.cos(th), (th, 0, 2 * sp.pi))
    i2 = sp.integrate(sp.sin(n_ * th) * sp.cos(m_ * th) * sp.sin(th), (th, 0, 2 * sp.pi))
    if abs(n_ - m_) == 1:
        assert i1 == sp.pi / 2 and i2 == sp.sign(n_ - m_) * sp.pi / 2
    else:
        assert i1 == 0 and i2 == 0
print("     int sin(n th) sin(m th) cos th = pi/2 and int sin(n th) cos(m th) sin th = sign(n-m) pi/2 for |n-m| = 1,"
      " else 0 (checked on sample pairs; product-to-sum in general)")

# polar rules on r^e W^beta P(t) cos(n theta), checked against Cartesian derivatives at a rational point
ee, be = -1, sp.Rational(7, 10)
Pt = 2 - 3 * tt + 5 * tt**3
nn = 3
Wr = 1 / (1 + rs**2)
expr = rs**ee * Wr**be * Pt.subs(tt, tr) * sp.cos(nn * th)
Top_s = lambda P, b, e: (e - 2 * b * tt) * P + 2 * tt * (1 - tt) * sp.diff(P, tt)
TP = Top_s(Pt, be, ee)
lap_claim = rs**(ee - 2) * Wr**be * (Top_s(TP, be, ee) - nn**2 * Pt).subs(tt, tr) * sp.cos(nn * th)
dy_claim = sp.Rational(1, 2) * rs**(ee - 1) * Wr**be * ((TP - nn * Pt).subs(tt, tr) * sp.sin((nn + 1) * th)
                                                       - (TP + nn * Pt).subs(tt, tr) * sp.sin((nn - 1) * th))
dx_claim = sp.Rational(1, 2) * rs**(ee - 1) * Wr**be * ((TP - nn * Pt).subs(tt, tr) * sp.cos((nn + 1) * th)
                                                       + (TP + nn * Pt).subs(tt, tr) * sp.cos((nn - 1) * th))
dr_, dth_ = (lambda f: sp.diff(f, rs)), (lambda f: sp.diff(f, th))
lap = dr_(dr_(expr)) + dr_(expr) / rs + dth_(dth_(expr)) / rs**2
dy = sp.sin(th) * dr_(expr) + sp.cos(th) / rs * dth_(expr)
dxx = sp.cos(th) * dr_(expr) - sp.sin(th) / rs * dth_(expr)
pt = {rs: sp.Rational(7, 5), th: sp.Rational(3, 10)}
for got, want in ((lap, lap_claim), (dy, dy_claim), (dxx, dx_claim)):
    assert abs(sp.N((got - want).subs(pt), 40)) < 1e-30
print("(1e) polar rules (T = T_(beta,e) = r d/dr on r^e W^beta P): Delta -> r^(e-2) W^beta (T^2 - n^2)P cos(n th);")
print("     d_y -> (1/2) r^(e-1) W^beta [(T-n)P sin((n+1)th) - (T+n)P sin((n-1)th)]; d_x -> same with cos and +")
print("     (checked against Cartesian derivatives at r = 7/5, th = 3/10 for e = -1, beta = 7/10, n = 3)")

# =============================== (2) exact polar fields ===============================
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


def load(name):
    if name == "state131":
        d = json.loads((HERE / "data/a2_state131_exact.json").read_text())
        c = fmpq(*map(int, d["exact_parameters"]["cl"].split("/")))
        chi = {}
        for (j, m, kk), co in zip(d["canonical_order"], d["canonical_coefficients"]):
            addto(chi, (j, 2 * m), fmpq(*map(int, co.split("/"))) * tp**kk)
        return c, chi, fmpq(*map(int, d["exact_parameters"]["a0"].split("/")))
    fn = {"d2": "a2_nb_d2_exact.json", "Mpen2": "a2_nb_Mpen2_exact.json",
          "C1-N1-005": "c1n1_005_d2w_j7_n4_X3_mid180_exact.json"}[name]
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
    return c, chi, None


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
        assert beta(j) + 2 == (j + 1) * delta / 2          # r^-3 W^beta = r W^(beta+2) t^-2, beta + 2 = a_j
    return delta, R, S


ctx.prec = 768
pi = arb.pi()


def A(q):
    q = fmpq(q) if not isinstance(q, fmpq) else q
    return arb(q.p) / arb(q.q)


def Wpow(Wv, e):
    return Wv ** A(e)


def point_fields(c, delta, R, S, rv, thv):
    """rho, rho_r, rho_th/r, u_r, u_th and F at a point (exact rational r, arb theta)."""
    tv, Wv = A(rv * rv / (1 + rv * rv)), A(1 / (1 + rv * rv))
    r = A(rv)
    rho = rr_ = rt = ur = ut = arb(0)
    for (j, n), P in R.items():
        aj = (j + 1) * delta / 2
        wv = Wpow(Wv, aj)
        rho += r * wv * A(P(fmpq(rv * rv, 1 + rv * rv))) * (n * thv).sin()
        rr_ += wv * A(Top(P, aj, 1)(fmpq(rv * rv, 1 + rv * rv))) * (n * thv).sin()
        rt += wv * n * A(P(fmpq(rv * rv, 1 + rv * rv))) * (n * thv).cos()
    for (j, n), P in S.items():
        aj = (j + 1) * delta / 2
        wv = Wpow(Wv, aj)
        ur += -r * wv * n * A(P(fmpq(rv * rv, 1 + rv * rv))) * (n * thv).cos()
        ut += r * wv * A(Top(P, aj, 2)(fmpq(rv * rv, 1 + rv * rv))) * (n * thv).sin()
    Fv = A(c) * r * rr_ + ur * rr_ + ut * rt - rho
    return dict(rho=rho, rho_r=rr_, rho_th_over_r=rt, u_r=ur, u_th=ut, F=Fv)


wit = {rw["candidate"]: rw for rw in json.loads((HERE / "data/t4_017_cartesian_witnesses.json").read_text())["rows"]}
CANDS = ["state131", "d2", "Mpen2", "C1-N1-005"]
FIELDS = {}
for name in CANDS:
    st = time.monotonic()
    c, chi, a0src = load(name)
    delta, R, S = build(c, chi)
    a0 = sum((P(0) for (j, n), P in R.items() if n == 1), fmpq(0))
    norm8 = c + 2 * sum((P(0) for (j, n), P in S.items() if n == 2), fmpq(0)) - 1
    js = sorted({j for j, _ in R})
    print(f"(2) {name}: c = {c}; rho branches j = {js}, rho modes {len(R)} (max n {max(n for _, n in R)}), psi modes"
          f" {len(S)} (max n {max(n for _, n in S)}); exact division by t^2 holds; built in {time.monotonic() - st:.1f} s")
    print(f"     a0 = sum_j R_(j,1)(0) = {A(a0).str(16)}; normalization c + d_y u2(0) - 1 = "
          + ("0 exactly" if norm8 == 0 else f"{A(norm8).str(5)} (exact rational, nonzero)"))
    if a0src is not None:
        assert a0 == a0src
        print("     a0 equals the exact source a0 of state 131")
    FIELDS[name] = (c, delta, R, S)
    half = arb.pi() / 2
    if name in ("d2", "Mpen2"):
        rw = wit["C1-A2-" + name]
        yv = fmpq(rw["point"][1])
        pf = point_fields(c, delta, R, S, yv, half)
        comp = {"rho": pf["rho"], "u2": pf["u_r"], "rho_y": pf["rho_r"], "residual": pf["F"]}
        for key, val in comp.items():
            ref = arb(rw["fields"][key])
            assert val.overlaps(ref), (name, key, val.str(20), ref.str(20))
        print(f"     at (0, {yv}): rho, u2, rho_y, F overlap the CONFIRMED-N4 intervals; F = {pf['F'].str(15)}")
    if name == "C1-N1-005":
        pf = point_fields(c, delta, R, S, fmpq(1, 4), half)
        assert abs(pf["F"] - A(fmpq(-14096814, 10**7))) < A(fmpq(1, 10**7))
        print(f"     F(0, 1/4) = {pf['F'].str(15)} (N4-076/T4-082: -1.4096814)")

# =============================== (3) the weighted weak test ===============================
_bcache = {}


def bseq(b, Mmax):
    """[B(M, b+1) for M = 0..Mmax] (index 0 unused), recurrence B(M+1, v) = B(M, v) M/(M+v)."""
    key = b
    have = _bcache.get(key)
    if have is not None and len(have) > Mmax:
        return have
    v = A(b + 1)
    assert b + 1 > 0
    seq = [arb(0), 1 / v]
    for M in range(1, Mmax):
        seq.append(seq[-1] * M / (M + v))
    _bcache[key] = seq
    return seq


def integ(P, K, b):
    """int_0^1 t^K W^b P(t) dt for an arb_poly P (expanded in powers of t)."""
    co = P.coeffs()
    if not co:
        return arb(0)
    seq = bseq(b, K + len(co) + 1)
    return sum((co[l] * seq[K + l + 1] for l in range(len(co))), arb(0))


def to_arb(P):
    return arb_poly([A(q) for q in P.coeffs()]) if P.degree() >= 0 else arb_poly([])


PREP = {}
for name in CANDS:
    st = time.monotonic()
    c, delta, R, S = FIELDS[name]
    aj = lambda j: (j + 1) * delta / 2
    Ra = {key: to_arb(P) for key, P in R.items()}
    Sa = {key: to_arb(P) for key, P in S.items()}
    TRa = {(j, n): to_arb(Top(P, aj(j), 1)) for (j, n), P in R.items()}
    TSa = {(j, n): to_arb(Top(P, aj(j), 2)) for (j, n), P in S.items()}
    Eu, Er = {}, {}
    for Ed, Fa, TFa in ((Eu, Sa, TSa), (Er, Ra, TRa)):
        bymode = {}
        for (j, n) in Fa:
            bymode.setdefault(n, []).append(j)
        for n, lst in bymode.items():
            for i in lst:
                for l in lst:
                    term = Fa[(i, n)] * Fa[(l, n)] * (n * n) + TFa[(i, n)] * TFa[(l, n)]
                    Ed[i + l] = Ed.get(i + l, arb_poly([])) + term
    lin = {j: Ra[(j, 1)] for (j, n) in Ra if n == 1}
    N0, N1 = {}, {}
    for (j, m), Sp in Sa.items():
        for (i, n), Rp in Ra.items():
            if abs(n - m) != 1:
                continue
            sg = 1 if n > m else -1
            N0[i + j] = N0.get(i + j, arb_poly([])) + Rp * (Sp * arb_poly([1, -4]) * (sg * m) - TSa[(j, m)])
            N1[i + j] = N1.get(i + j, arb_poly([])) + Rp * Sp * arb_poly([2, -2]) * (sg * m)
    PREP[name] = (c, delta, lin, N0, N1, Eu, Er)
    print(f"(3) {name}: quadratic forms prepared in {time.monotonic() - st:.1f} s")


def Ssup(j, b):
    if j == 0:
        return arb(1)
    jA, bA = arb(j), A(b) if isinstance(b, fmpq) else arb(b)
    return (jA / (jA + bA)) ** jA * (bA / (jA + bA)) ** bA


def evaluate(name, a, CU, k):
    c, delta, lin, N0, N1, Eu, Er = PREP[name]
    cA = A(c)
    ell = arb_poly([3 * cA + 1 + 2 * cA * k, -2 * cA * k - 4 * cA])
    gk = arb_poly([1 + 2 * k, 4 - 2 * k])
    lin_v = -pi / 2 * sum((integ(P * ell, k + 1, (j + 1) * delta / 2 - 1) for j, P in lin.items()), arb(0))
    non_v = pi / 4 * sum((integ(N0[J] + N1[J] * k, k + 1, (J + 2) * delta / 2 - 1) for J in N0), arb(0))
    I = lin_v + non_v
    A2 = pi / 2 * integ(ell * ell, 2 * k + 1, 1 - a)
    B2 = pi / 2 * sum((integ(E * gk * gk, 2 * k + 1, 1 - a + (J + 2) * delta / 2) for J, E in Eu.items()), arb(0))
    C2 = pi / 2 * sum((integ(E, 2 * k + 1, 1 - a + (J + 2) * delta / 2) for J, E in Er.items()), arb(0))
    assert A2 > 0 and B2 > 0 and C2 > 0
    Av, Bv, Cv = A2.sqrt(), B2.sqrt(), C2.sqrt()
    D = Av + Bv + CU * Cv
    if k == 0 and a <= fmpq(3, 2):
        H = arb(1)
    else:
        H = Ssup(k, 2 - a) + 2 * k * Ssup(k, 3 - a) + 4 * Ssup(k + 1, 2 - a)
    Iabs = abs(I)
    rad = 2 * Iabs / (D + (D * D + 4 * CU * H * Iabs).sqrt())
    return dict(pairing=I, A=Av, B_upper=Bv, C_upper=Cv, D=D, gradient_sup_upper=H, weighted_L2_radius_lower=rad)


CASES = [(fmpq(1), A(2), "C_U = 2/(2-a) = 2 (T4-054, AUDITED)"),
         (fmpq(6, 5), A(fmpq(808233, 500000)), "C_U = 808233/500000 (TP-2 rational certificate, CONFIRMED by T4-072)")]
T4FILE = {"state131": "state131", "d2": "d2", "Mpen2": "Mpen2", "C1-N1-005": "C1-N1-005-d2w-j7-x3"}
KS = [0, 128, 512, 1024]
best = {}
print("(3a) radius (4) at the c1-t4 k values; 'ovl' = all seven quantities overlap c1-t4's stored intervals")
for a, CU, cert in CASES:
    print(f"     a = {a}: {cert}")
    for name in CANDS:
        fn = HERE / f"data/t4_081_verification/{T4FILE[name]}_a{a.p}_{a.q}_2048.json"
        ref = {}
        if fn.exists():
            ref = {rw["k"]: rw for rw in json.loads(fn.read_text())["rows"]}
        for k in KS:
            vals = evaluate(name, a, CU, k)
            ov = "no c1-t4 value"
            if k in ref:
                ok = all(vals[key].overlaps(arb(ref[k][key])) for key in vals)
                assert ok, (name, a, k, {key: (vals[key].str(12), ref[k][key][:30]) for key in vals})
                ov = "ovl"
            print(f"       {name:10s} k={k:5d}  I={vals['pairing'].str(10)}  A={vals['A'].str(8)}  B<={vals['B_upper'].str(8)}"
                  f"  C<={vals['C_upper'].str(8)}  H<={vals['gradient_sup_upper'].str(6)}  m>={vals['weighted_L2_radius_lower'].str(10)}  {ov}")
            key = (name, str(a))
            if key not in best or vals["weighted_L2_radius_lower"].lower() > best[key][1].lower():
                best[key] = (k, vals["weighted_L2_radius_lower"])
print("(3b) strongest of the c1-t4 k values (lower endpoints, rounded down):")
for (name, a), (k, v) in best.items():
    print(f"     {name:10s} a = {a:4s}: ||w h||_2 > {v.lower().str(9, radius=False)} (k = {k})")
claims = {("d2", "1"): "0.0071933655", ("Mpen2", "1"): "0.0156668300", ("C1-N1-005", "1"): "0.0061687217",
          ("state131", "6/5"): "2.9157438e-5", ("d2", "6/5"): "0.0048295932", ("Mpen2", "6/5"): "0.0091651753",
          ("C1-N1-005", "6/5"): "0.0064650914"}
for key, txt in claims.items():
    assert best[key][1] > arb(txt), (key, txt)
print("     every T4-085/T4-088 stated bound is below the reproduced value: CONFIRMED")
print(f"(3c) k scan (same formulas; which k is best; time so far {time.monotonic() - T0:.0f} s)")
for a, CU, cert in CASES:
    for name in CANDS:
        row = []
        bk, bv = None, arb(0)
        for k in [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]:
            v = evaluate(name, a, CU, k)["weighted_L2_radius_lower"]
            row.append(f"{k}:{v.mid().str(4, radius=False)}")
            if v.lower() > bv.lower():
                bk, bv = k, v
        print(f"     a = {str(a):3s} {name:10s} best k = {bk:5d}, m > {bv.lower().str(6, radius=False)};  " + " ".join(row))
print("(3d) refined k scan (each k is a separate rigorous bound; lower endpoints rounded down)")
FINE = {"d2": [160, 192, 224, 256, 288, 320, 384], "Mpen2": [48, 64, 80, 96, 112, 128, 160, 192],
        "C1-N1-005": [0, 1, 2048, 3072, 4096, 6144, 8192], "state131": [2048, 4096, 8192, 16384, 32768]}
for a, CU, cert in CASES:
    for name in CANDS:
        bk, bv, row = None, arb(0), []
        for k in FINE[name]:
            v = evaluate(name, a, CU, k)["weighted_L2_radius_lower"]
            row.append(f"{k}:{v.lower().str(6, radius=False)}")
            if v.lower() > bv.lower():
                bk, bv = k, v
        print(f"     a = {str(a):3s} {name:10s} best k = {bk:5d}, m > {bv.lower().str(8, radius=False)};  " + " ".join(row))
print(f"done in {time.monotonic() - T0:.0f} s")
