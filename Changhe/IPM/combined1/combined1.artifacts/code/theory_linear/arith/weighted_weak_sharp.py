"""Sharpened weighted weak-distance test (c1-t2; review W4 of T4-081, notes/T2_weighted_weak_sharp.md).

Run from artifacts/:  python3 -B arith/weighted_weak_sharp.py
Needs sympy, mpmath, python-flint.  Several minutes on one core.

Same setting as T4-081 (c1-t4 research/weighted_weak_probe/PROOF.md, AUDITED recommendation in
reviews/REVIEW_T4_081.md): w = (1+|X|^2)^(-a/2), m = ||w h||_2, ||w U[h]||_2 <= C_U m, phi = r W^2 P(t) sin(theta)
with t = r^2/(1+r^2), W = 1 - t.  For every such phi (P a polynomial; P = t^k is T4-081's phi_k):
    |int F phi| <= D(phi) m + C_U H(phi) m^2,
    D(phi) = ||M_phi / w||_2 + C_U ||phi |D rho| / w||_2,   M_phi = (2c+1) phi + V.D phi,
    H(phi) = sup |D phi| / w^2,
hence m >= 2|I|/(D + sqrt(D^2 + 4 C_U H |I|)).  T4-081 uses the upper bounds A_k + B_k >= ||M/w||,
C_k >= ||phi |D rho|/w|| (y^2 <= r^2) and (5)/(6) for H.  Here all three are evaluated exactly (arb):
  (i)   ||M_phi/w||^2 = (pi/2) int t^(2k+1) W^(1-a) sum_n (delta_(n,1) ell_k + sum_j W^(a_j) Q_(j,n))^2 dt;
  (ii)  ||phi |D rho|/w||^2 = (1/2) int t^(2k+1) sum W^(1-a+a_i+a_j) [TR_i TR_j alpha(n,m) + n m R_i R_j beta(n,m)] dt,
        alpha(n,m) = int sin^2 sin(n th) sin(m th), beta(n,m) = int sin^2 cos(n th) cos(m th);
  (iii) H(phi) = sup_t W^(2-a) max(|P|, |T_(2,1) P|) (exact angular maximum), bounded above on a geometric W grid.
Then phi is optimized over spans of phi_k (Gram matrices; Lagrange direction (G_M + mu G_C)^(-1) f, mu scanned in
FLOAT), and the radius is re-evaluated rigorously (arb) for the exact rational coefficient vector found.

The fields are built from the source generators exactly as in arith/t4_081_review.py (code copied unchanged);
data/ as there.  Output: logs/weighted_weak_sharp.log and data/weighted_weak_sharp_results.json.
Parts:
  (1) sympy: alpha, beta tables; the u.D phi mode formula; |D phi|^2 = W^4 (P_r^2 sin^2 + P^2 cos^2) form;
  (2) fields (copied code) and checks;
  (3) single-k sharpened values against T4-081's at the same k (arb), with a FLOAT 2D quadrature cross-check;
  (4) span-optimized test functions (arb).
"""
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import arb, arb_poly, ctx, fmpq, fmpq_poly

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parents[1]
T0 = time.monotonic()

# =============================== (1) sympy checks ===============================
th = sp.symbols("theta", real=True)


def a4(n, m):   # alpha(n, m) / (pi/4) for n, m >= 1
    return 2 * (n == m) - (abs(n - m) == 2) + (n + m == 2)


def b4(n, m):   # beta(n, m) / (pi/4) for n, m >= 1
    return 2 * (n == m) - (abs(n - m) == 2) - (n + m == 2)


for n in range(1, 10, 2):
    for m in range(1, 10, 2):
        al = sp.integrate(sp.expand(sp.sin(th) ** 2 * sp.sin(n * th) * sp.sin(m * th), trig=True), (th, 0, 2 * sp.pi))
        be = sp.integrate(sp.expand(sp.sin(th) ** 2 * sp.cos(n * th) * sp.cos(m * th), trig=True), (th, 0, 2 * sp.pi))
        assert sp.simplify(al - sp.pi * a4(n, m) / 4) == 0 and sp.simplify(be - sp.pi * b4(n, m) / 4) == 0
print("(1a) int sin^2 sin(n th) sin(m th) = (pi/4)(2[n=m] - [|n-m|=2] + [n+m=2]),"
      " int sin^2 cos(n th) cos(m th) = (pi/4)(2[n=m] - [|n-m|=2] - [n+m=2])  (odd n, m <= 9 checked)")
TS_, S_, g_ = sp.symbols("TS S g", real=True)
for m in (2, 4, 6):
    lhs = -m * S_ * g_ * sp.cos(m * th) * sp.sin(th) + TS_ * sp.sin(m * th) * sp.cos(th)
    rhs = sp.Rational(1, 2) * ((TS_ - m * S_ * g_) * sp.sin((m + 1) * th) + (TS_ + m * S_ * g_) * sp.sin((m - 1) * th))
    assert sp.simplify(sp.expand_trig(lhs - rhs)) == 0
print("(1b) u_r phi_r + u_th phi_th/r per psi mode m: -m S g cos(m th) sin th + TS sin(m th) cos th"
      " = (1/2)[(TS - m S g) sin((m+1)th) + (TS + m S g) sin((m-1)th)]")
x, y = sp.symbols("x y", real=True)
kk = sp.symbols("k", positive=True)
rr = x**2 + y**2
ts, Ws = rr / (1 + rr), 1 / (1 + rr)
phik = y * ts**kk * Ws**2
Dp = (sp.diff(phik, x), sp.diff(phik, y))
gk = 1 + 2 * kk * Ws - 4 * ts
sin2 = y**2 / rr
assert sp.simplify((Dp[0] ** 2 + Dp[1] ** 2) - ts ** (2 * kk) * Ws**4 * (1 + (gk**2 - 1) * sin2)) == 0
print("(1c) |D phi_k|^2 = t^(2k) W^4 (1 + (g_k^2 - 1) sin^2 th), g_k = 1 + 2kW - 4t: exact angular max"
      " W^2 t^k max(1, |g_k|); for phi = r W^2 P sin th the same with |P|, |T_(2,1) P|")
r_ = sp.symbols("r", positive=True)
tt = sp.symbols("t", positive=True)
tr = r_**2 / (1 + r_**2)
Pt = 2 - 3 * tt + 5 * tt**3 + tt**7
T21 = (1 - 4 * tt) * Pt + 2 * tt * (1 - tt) * sp.diff(Pt, tt)
phi_r = sp.diff(r_ * (1 - tr) ** 2 * Pt.subs(tt, tr), r_)
assert sp.simplify(phi_r - (1 - tr) ** 2 * T21.subs(tt, tr)) == 0
print("     d_r (r W^2 P(t)) = W^2 T_(2,1) P, T_(2,1) P = (1 - 4t) P + 2t(1-t) P'")

# =============================== (2) exact polar fields (copied from arith/t4_081_review.py) ===============================
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
    c, chi, a0src = load(name)
    delta, R, S = build(c, chi)
    a0 = sum((P(0) for (j, n), P in R.items() if n == 1), fmpq(0))
    norm8 = c + 2 * sum((P(0) for (j, n), P in S.items() if n == 2), fmpq(0)) - 1
    assert norm8 == 0 and (a0src is None or a0 == a0src)
    assert all(n % 2 == 1 for _, n in R) and all(n % 2 == 0 and n >= 2 for _, n in S)
    FIELDS[name] = (c, delta, R, S)
    if name in ("d2", "Mpen2"):
        rw = wit["C1-A2-" + name]
        pf = point_fields(c, delta, R, S, fmpq(rw["point"][1]), arb.pi() / 2)
        assert pf["F"].overlaps(arb(rw["fields"]["residual"])) and pf["u_r"].overlaps(arb(rw["fields"]["u2"]))
    print(f"(2) {name}: c = {c}; rho modes {len(R)}, psi modes {len(S)}, max poly degree"
          f" {max(P.degree() for P in list(R.values()) + list(S.values()))}; normalization exact"
          + ("; F, u2 overlap the CONFIRMED-N4 point intervals" if name in ("d2", "Mpen2") else ""))

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

# =============================== (3) sharpened single-k test ===============================
g0, g1 = fmpq_poly([1, -4]), fmpq_poly([2, -2])          # g_k = 1 + 2k(1-t) - 4t = g0 + k g1
SHARP = {}
for name in CANDS:
    st = time.monotonic()
    c, delta, R, S = FIELDS[name]
    aj = lambda j: (j + 1) * delta / 2
    # X[p][n][key]: coefficient of k^p in the sin(n th) mode of M/(r t^k W^2); W exponent key * delta/2
    X = {0: {}, 1: {}}
    addto(X[0].setdefault(1, {}), 0, fmpq_poly([3 * c + 1, -4 * c]))     # ell_k = (3c+1-4ct) + k 2c(1-t)
    addto(X[1].setdefault(1, {}), 0, fmpq_poly([2 * c, -2 * c]))
    for (j, m), P in S.items():
        TS = Top(P, aj(j), 2)
        for n, sg in ((m + 1, -1), (m - 1, 1)):
            addto(X[0].setdefault(n, {}), j + 1, fmpq(1, 2) * (TS + sg * m * P * g0))
            addto(X[1].setdefault(n, {}), j + 1, fmpq(1, 2) * (sg * m * P * g1))
    Xa = {p: {n: {key: to_arb(P) for key, P in d.items()} for n, d in X[p].items()} for p in (0, 1)}
    E = {(0, 0): {}, (0, 1): {}, (1, 1): {}}
    for n in set(Xa[0]) | set(Xa[1]):
        for (p, q), Ed in E.items():
            for k1, P1 in Xa[p].get(n, {}).items():
                for k2, P2 in Xa[q].get(n, {}).items():
                    Ed[k1 + k2] = Ed.get(k1 + k2, arb_poly([])) + P1 * P2
    byn = {}
    for (j, n), P in R.items():
        byn.setdefault(n, []).append((j, to_arb(P), to_arb(Top(P, aj(j), 1))))
    Ec = {}
    for n, lst in byn.items():
        for m in (n - 2, n, n + 2):
            if m < 1 or m not in byn:
                continue
            al, be = a4(n, m), b4(n, m)
            for i, Ri, TRi in lst:
                for j, Rj, TRj in byn[m]:
                    Ec[i + j] = Ec.get(i + j, arb_poly([])) + TRi * TRj * al + Ri * Rj * (n * m * be)
    SHARP[name] = (E, Ec)
    print(f"(3) {name}: exact M and C forms prepared in {time.monotonic() - st:.1f} s")


def GM(name, a, k1, k2):
    """<M_k1/w, M_k2/w> (exact)."""
    c, delta, R, S = FIELDS[name]
    E, _ = SHARP[name]
    tot = arb(0)
    for key in set(E[(0, 0)]) | set(E[(0, 1)]) | set(E[(1, 1)]):
        P = E[(0, 0)].get(key, arb_poly([])) + E[(0, 1)].get(key, arb_poly([])) * (k1 + k2) \
            + E[(1, 1)].get(key, arb_poly([])) * (k1 * k2)
        b = 1 - a + key * delta / 2
        assert b > -1
        tot += integ(P, k1 + k2 + 1, b)
    return pi / 2 * tot


def GC(name, a, k1, k2):
    """<phi_k1 D rho/w, phi_k2 D rho/w> (exact, sin^2 kept)."""
    c, delta, R, S = FIELDS[name]
    _, Ec = SHARP[name]
    return pi / 8 * sum((integ(P, k1 + k2 + 1, 1 - a + (J + 2) * delta / 2) for J, P in Ec.items()), arb(0))


def pairing(name, k):
    c, delta, lin, N0, N1, Eu, Er = PREP[name]
    cA = A(c)
    ell = arb_poly([3 * cA + 1 + 2 * cA * k, -2 * cA * k - 4 * cA])
    lin_v = -pi / 2 * sum((integ(P * ell, k + 1, (j + 1) * delta / 2 - 1) for j, P in lin.items()), arb(0))
    non_v = pi / 4 * sum((integ(N0[J] + N1[J] * k, k + 1, (J + 2) * delta / 2 - 1) for J in N0), arb(0))
    return lin_v + non_v


def umax(vals):
    """Exact upper endpoint of the largest of the balls (comparisons of exact points are decided)."""
    best = None
    for v in vals:
        u = v.upper()
        if best is None or u > best:
            best = u
    return arb(best)


def Wgrid(lo_exp=-48, ratio=fmpq(1001, 1000)):
    pts = [fmpq(1, 2 ** (-lo_exp))]
    while pts[-1] < 1:
        nxt = pts[-1] * ratio
        pts.append(min(nxt, fmpq(1)))
    return pts


WG = Wgrid()


def Hk_exact(k, a):
    """Upper bound of sup_t W^(2-a) t^k max(1, |1 + 2kW - 4t|) (angular maximum exact; W grid, monotone bounds)."""
    old = ctx.prec
    ctx.prec = 128
    b = A(2 - a)
    gW = lambda Wv: abs(-3 + (2 * k + 4) * Wv)              # g_k as a function of W (linear)
    vals = [A(WG[0]) ** b * umax([arb(1), gW(arb(0)), gW(A(WG[0]))])]   # W in [0, W_min], t^k <= 1
    for W0, W1 in zip(WG[:-1], WG[1:]):
        W0a, W1a = A(W0), A(W1)
        vals.append(W1a ** b * (1 - W0a) ** k * umax([arb(1), gW(W0a), gW(W1a)]))
    out = umax(vals)
    ctx.prec = old
    return out


def H_poly(coef, a):
    """Upper bound of sup_t W^(2-a) max(|P|, |T_(2,1) P|) for P = sum_k coef[k] t^k (exact rationals); mean value
    form on each W interval."""
    old = ctx.prec
    ctx.prec = 192
    P = fmpq_poly([0])
    for k, cq in coef.items():
        P += cq * tp**k
    TP = Top(P, 2, 1)
    polys = [(to_arb(Q_), to_arb(Q_.derivative())) for Q_ in (P, TP)]
    b = A(2 - a)
    W0a = A(WG[0])
    tb = arb(1 - W0a / 2, W0a / 2 * (1 + arb(2) ** -60))       # t in [1 - W_min, 1]
    vals = [W0a ** b * umax([abs(Pa(tb)) for Pa, _ in polys])]
    for W0, W1 in zip(WG[:-1], WG[1:]):
        tm = 1 - (W0 + W1) / 2
        rad = (W1 - W0) / 2
        tball = arb(A(tm), A(rad) * (1 + arb(2) ** -60))
        vals.append(A(W1) ** b * umax([abs(Pa(A(tm))) + A(rad) * abs(dPa(tball)) for Pa, dPa in polys]))
    out = umax(vals)
    ctx.prec = old
    return out


def radius(I, D, H, CU):
    Iabs = abs(I)
    return 2 * Iabs / (D + (D * D + 4 * CU * H * Iabs).sqrt())


def sharp_single(name, a, CU, k):
    I = pairing(name, k)
    Mn, Cn = GM(name, a, k, k).sqrt(), GC(name, a, k, k).sqrt()
    H = Hk_exact(k, a)
    if k == 0 and a <= fmpq(3, 2):
        H = arb(1)                                    # T4-081 (log 1c of t4_081_review): H_0 = 1 exactly
    D = Mn + CU * Cn
    return dict(pairing=I, M=Mn, C=Cn, D=D, H=H, m=radius(I, D, H, CU))


CASES = [(fmpq(1), A(2), "C_U = 2 (T4-054)"), (fmpq(6, 5), A(fmpq(808233, 500000)), "C_U = 808233/500000 (TP-2)")]
KREF = {"state131": [0, 1024, 32768], "d2": [0, 128, 192, 288], "Mpen2": [0, 64, 96, 512], "C1-N1-005": [0, 128]}
OUT = {"single": [], "span": []}
print("(3a) single k: T4-081 bound (A + B + C_U C_old, H by (6)) against the exact (i) ||M/w||, (ii) C, (iii) H")
for a, CU, cert in CASES:
    print(f"     a = {a}: {cert}")
    for name in CANDS:
        for k in KREF[name]:
            old = evaluate(name, a, CU, k)
            new = sharp_single(name, a, CU, k)
            assert new["pairing"].overlaps(old["pairing"])
            assert new["M"] < old["A"] + old["B_upper"] and new["C"] < old["C_upper"] and new["D"] < old["D"]
            assert new["H"].upper() <= old["gradient_sup_upper"].upper() * (1 + arb(2) ** -40)
            gain = new["m"].lower() / old["weighted_L2_radius_lower"].lower()
            print(f"       {name:10s} k={k:6d}  |I|={abs(new['pairing']).str(6)}  ||M/w||={new['M'].str(6)}"
                  f" (A+B {(old['A'] + old['B_upper']).str(6)})  C={new['C'].str(6)} (old {old['C_upper'].str(6)})"
                  f"  H<={new['H'].str(4)} (old {old['gradient_sup_upper'].str(4)})"
                  f"  m>={new['m'].lower().str(8, radius=False)} (old {old['weighted_L2_radius_lower'].lower().str(8, radius=False)},"
                  f" gain {gain.mid().str(4, radius=False)})")
            OUT["single"].append(dict(candidate=name, a=str(a), k=k, pairing=new["pairing"].str(30), M=new["M"].str(30),
                                      C=new["C"].str(30), H_upper=new["H"].str(20),
                                      m_lower=new["m"].lower().str(12, radius=False),
                                      t4_081_m_lower=old["weighted_L2_radius_lower"].lower().str(12, radius=False)))

# FLOAT 2D quadrature cross-check of (i) and (ii): pointwise u.D phi and sin^2 |D rho|^2 on an angular grid (trapezoid,
# exact for these trigonometric polynomials), adaptive quadrature in t (scipy); polynomials evaluated in arb at the nodes
import numpy as np
from scipy.integrate import quad as squad


def fl_check(name, a, k):
    c, delta, R, S = FIELDS[name]
    cf, af = float(A(c).mid()), float(A(a).mid())
    modes = lambda Fd, e: [((j + 1) * float(A(delta).mid()) / 2, n, to_arb(P), to_arb(Top(P, (j + 1) * delta / 2, e)))
                           for (j, n), P in Fd.items()]
    Rl, Sl = modes(R, 1), modes(S, 2)
    NT = 4 * max(n for _, n in list(R) + list(S)) + 8
    thv = 2 * np.pi * np.arange(NT) / NT
    s1, c1 = np.sin(thv), np.cos(thv)
    nS = np.array([n for _, n, _, _ in Sl], dtype=float)
    nR = np.array([n for _, n, _, _ in Rl], dtype=float)
    CSm, SCm = np.cos(np.outer(nS, thv)) * s1, np.sin(np.outer(nS, thv)) * c1
    SRm, CRm = np.sin(np.outer(nR, thv)), np.cos(np.outer(nR, thv))

    def vals(lst, tv):
        ta = arb(tv)
        P = np.array([float(Pa(ta).mid()) for _, _, Pa, _ in lst])
        TP = np.array([float(TPa(ta).mid()) for _, _, _, TPa in lst])
        we = np.array([(1 - tv) ** e for e, _, _, _ in lst])
        return P * we, TP * we

    def fM(tv):
        Wv = 1 - tv
        g = 1 + 2 * k * Wv - 4 * tv
        ell = 3 * cf + 1 + 2 * cf * k * Wv - 4 * cf * tv
        Sv, TSv = vals(Sl, tv)
        br = ell * s1 - (nS * Sv * g) @ CSm + TSv @ SCm
        return tv ** (2 * k + 1) * Wv ** (1 - af) * np.mean(br * br) * np.pi

    def fC(tv):
        Wv = 1 - tv
        Rv, TRv = vals(Rl, tv)
        rr_, rt = TRv @ SRm, (nR * Rv) @ CRm
        return tv ** (2 * k + 1) * Wv ** (1 - af) * np.mean(s1 * s1 * (rr_ * rr_ + rt * rt)) * np.pi

    pts = [0.5, 0.9, 0.99, 0.999]
    out = []
    for fn in (fM, fC):
        val, err = squad(fn, 0, 1, points=pts, limit=400, epsabs=0, epsrel=1e-12)
        out.append(np.sqrt(val))
    return out


for k in (0, 288):
    st = time.monotonic()
    Mf, Cf = fl_check("d2", fmpq(1), k)
    Ma, Ca = GM("d2", fmpq(1), k, k).sqrt(), GC("d2", fmpq(1), k, k).sqrt()
    relM, relC = abs(Mf / float(Ma.mid()) - 1), abs(Cf / float(Ca.mid()) - 1)
    print(f"(3b) FLOAT 2D quadrature, d2, a = 1, k = {k}: ||M/w|| = {Mf:.12g} (arb {Ma.str(12)}), C = {Cf:.12g}"
          f" (arb {Ca.str(12)}); rel. diff {relM:.1e}, {relC:.1e} ({time.monotonic() - st:.0f} s)")
    assert relM < 1e-8 and relC < 1e-8

# =============================== (4) span optimization ===============================
BASIS = {"d2": [0, 16, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 384, 448, 512],
         "Mpen2": [0, 8, 16, 24, 32, 48, 64, 80, 96, 112, 128, 160, 192, 256],
         "C1-N1-005": [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 128],
         "state131": [0, 256, 1024, 2048, 4096, 8192, 16384, 32768]}
mp.mp.dps = 80
print("(4) span-optimized phi = sum_k c_k phi_k (c rational; every value below is a rigorous arb bound for that c)")
for a, CU, cert in CASES:
    for name in CANDS:
        st = time.monotonic()
        Ks = BASIS[name]
        nK = len(Ks)
        f = [pairing(name, k) for k in Ks]
        Gm = [[None] * nK for _ in range(nK)]
        Gc = [[None] * nK for _ in range(nK)]
        for i in range(nK):
            for j in range(i, nK):
                Gm[i][j] = Gm[j][i] = GM(name, a, Ks[i], Ks[j])
                Gc[i][j] = Gc[j][i] = GC(name, a, Ks[i], Ks[j])
        Hs = [Hk_exact(k, a) if k > 0 else arb(1) for k in Ks]
        tomp = lambda v: mp.mpf(v.mid().str(70, radius=False))
        fM = mp.matrix([tomp(v) for v in f])
        GmM = mp.matrix([[tomp(v) for v in row] for row in Gm])
        GcM = mp.matrix([[tomp(v) for v in row] for row in Gc])
        HsM = [tomp(v) for v in Hs]
        CUf = tomp(CU)

        def fl_rad(cv):
            I = abs(sum(cv[i] * fM[i] for i in range(nK)))
            D = mp.sqrt((cv.T * GmM * cv)[0]) + CUf * mp.sqrt((cv.T * GcM * cv)[0])
            H = sum(abs(cv[i]) * HsM[i] for i in range(nK))
            return 2 * I / (D + mp.sqrt(D * D + 4 * CUf * H * I))

        bestv, bestc, bestmu = mp.mpf(0), None, None
        for e in range(-40, 41):
            mu = mp.mpf(10) ** (mp.mpf(e) / 10)
            cv = mp.lu_solve(GmM + mu * GcM, fM)
            v = fl_rad(cv)
            if v > bestv:
                bestv, bestc, bestmu = v, cv, mu
        # rational coefficients, max |c_k| = 1
        sc = max(abs(v) for v in bestc)
        cq = {Ks[i]: fmpq(int(mp.nint(bestc[i] / sc * mp.mpf(10) ** 30)), 10**30) for i in range(nK)}
        cA = [A(cq[k]) for k in Ks]
        I = sum((cA[i] * f[i] for i in range(nK)), arb(0))
        Mn = sum((cA[i] * cA[j] * Gm[i][j] for i in range(nK) for j in range(nK)), arb(0)).sqrt()
        Cn = sum((cA[i] * cA[j] * Gc[i][j] for i in range(nK) for j in range(nK)), arb(0)).sqrt()
        Htri = sum((abs(cA[i]) * Hs[i] for i in range(nK)), arb(0))
        H = Htri
        if max(Ks) <= 1024:
            Hp = H_poly(cq, a)
            if Hp.upper() < Htri.upper():
                H = Hp
        D = Mn + CU * Cn
        m = radius(I, D, H, CU)
        sgl = max((r_ for r_ in OUT["single"] if r_["candidate"] == name and r_["a"] == str(a)),
                  key=lambda r_: float(r_["m_lower"]))
        print(f"     a = {str(a):3s} {name:10s} basis {Ks[0]}..{Ks[-1]} ({nK}), mu = {mp.nstr(bestmu, 3)}: |I| = {abs(I).str(6)},"
              f" ||M/w|| = {Mn.str(6)}, C = {Cn.str(6)}, H <= {H.str(5)} (triangle {Htri.str(5)});"
              f" m >= {m.lower().str(8, radius=False)} (FLOAT search {mp.nstr(bestv, 8)}; best single k here"
              f" {sgl['m_lower'][:10]} at k = {sgl['k']}) [{time.monotonic() - st:.0f} s]")
        OUT["span"].append(dict(candidate=name, a=str(a), C_U=str(CU.mid().str(10, radius=False)), basis=Ks,
                                coefficients={str(k): str(cq[k]) for k in Ks}, pairing=I.str(30), M=Mn.str(30),
                                C=Cn.str(30), H_upper=H.str(20), m_lower=m.lower().str(12, radius=False)))
(HERE / "data/weighted_weak_sharp_results.json").write_text(json.dumps(OUT, indent=1))
print(f"done in {time.monotonic() - T0:.0f} s")
