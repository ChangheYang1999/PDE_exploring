"""Independent review of T4-094 (c1-t4 research/weighted_packet_audit/PROOF.md, sha256 351dcccc...ead94, section
"Scope of a gap and of a coefficient weight"): a nonzero differentiated leading density r^gamma G(theta), 0 < gamma < 1,
gives ||w D^2 rho||_inf = infinity for w ~ r^p, p > 2 - gamma (reviews/REVIEW_T4_094.md).

Run from artifacts/:  python3 -B arith/t4_094_review.py
Needs sympy, numpy, python-flint.  A few minutes on one core.

The polar fields are built from the source generators with the code of arith/t4_081_review.py (copied; the C1-N1-007
snapshot file is added to the file table):
  data/a2_state131_exact.json, data/a2_nb_d2_exact.json, data/a2_nb_Mpen2_exact.json (as in t4_081_review.py);
  data/c1n1_005_d2w_j7_n4_X3_mid180_exact.json, data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json
  (= candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json, sha256 ed496232...3d21);
  data/c1n1_005_sector_table.json, data/c1n1_007_sector_table.json (c1-n1 residual sector tables, read only for the
  comparison in part 2).
Representation (t = r^2/(1+r^2), W = 1 - t, delta = 1 - 1/c, a_j = (j+1) delta/2):
  rho = r sum W^(a_j) R_(j,n)(t) sin(n th),  psi = r^2 sum W^(a_j) S_(j,n)(t) sin(n th),  u = (-psi_y, psi_x).
Parts:
  (1) sympy: the polar Hessian of r^mu G(theta); falling factorials; the velocity profile of r^(1+gamma) Psi; the cap
      formulas; the k = 2 transport commutator; the 2 x 2 example of the same section; polar Hessian rules for the
      representation;
  (2) exact (fmpq): leading density and stream profiles of five candidates, the identity
      (T_(a0,0) T_(a0,1) R)(1) = gamma (gamma - 1) R(1), the exact far-field expansion of the residual F (leading
      exponent and angular vector), the weight thresholds;
  (3) arb: d_r^2 rho on the ray theta = pi/2 at large r (rigorous point values);
  (4) FLOAT map of lambda_min M_(q,w) (T4-092/T4-094 packet matrix) for power weights, including the endpoint
      p = 2 - gamma, with arb values at the grid minimizers; FLOAT sup of w |D^2 rho|.
Output: logs/t4_094_review.log, data/t4_094_review_results.json.
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from flint import arb, arb_poly, ctx, fmpq, fmpq_poly

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parents[1]
T0 = time.monotonic()
OUT = {}

# =============================== (1) sympy checks ===============================
x, y = sp.symbols("x y", real=True)
rs, th, mu_, g_ = sp.symbols("r theta mu gamma", positive=True)
Gf, Psif = sp.Function("G"), sp.Function("Psi")


def cart_hess_frob2(f):
    return sum(sp.diff(f, a, b) ** 2 for a in (x, y) for b in (x, y))


# (1a) |D^2 (r^mu G)|_F^2 = r^(2mu-4) [mu^2 (mu-1)^2 G^2 + 2 (mu-1)^2 G'^2 + (mu G + G'')^2]
claim = lambda mu, G: rs ** (2 * mu - 4) * ((mu * (mu - 1) * G) ** 2 + 2 * ((mu - 1) * sp.diff(G, th)) ** 2
                                             + (mu * G + sp.diff(G, th, 2)) ** 2)
pt = {x: sp.Rational(6, 5), y: sp.Rational(7, 10)}
for mu in (sp.Rational(5, 9), sp.Rational(2251799813685248, 4076476460239181)):
    for coefs in ({1: 1}, {3: 1}, {1: 1, 3: 2, 5: -sp.Rational(1, 3)}):
        rr = sp.sqrt(x**2 + y**2)
        f = sum(cf * rr ** (mu - n) * sp.im(sp.expand((x + sp.I * y) ** n)) for n, cf in coefs.items())
        G = sum(cf * sp.sin(n * th) for n, cf in coefs.items())
        lhs = cart_hess_frob2(f).subs(pt)
        rhs = claim(mu, G).subs({rs: sp.sqrt(sp.Rational(6, 5) ** 2 + sp.Rational(7, 10) ** 2),
                                 th: sp.atan2(sp.Rational(7, 10), sp.Rational(6, 5))})
        assert abs(sp.N(lhs - rhs, 50)) < 1e-40
print("(1a) |D^2 (r^mu G)|_F^2 = r^(2mu-4) [mu^2 (mu-1)^2 G^2 + 2 (mu-1)^2 G'^2 + (mu G + G'')^2]"
      " (checked against Cartesian Hessians, mu = 5/9 and 1/c_l, G with harmonics 1, 3, 5)")
print("     so |D^2 rho|_F >= |d_r^2 rho| = |gamma (gamma-1)| r^(gamma-2) |G| for the leading term")
# (1b) radial derivatives and falling factorials
for k in range(1, 6):
    assert sp.simplify(sp.diff(rs**mu_ * Gf(th), rs, k) - sp.ff(mu_, k) * rs ** (mu_ - k) * Gf(th)) == 0
gam131 = sp.Rational(2251799813685248, 4076476460239181)
assert all(sp.ff(gam131, k) != 0 for k in range(1, 9))
print("(1b) d_r^k (r^mu G) = mu (mu-1)...(mu-k+1) r^(mu-k) G; nonzero for mu = 1/c_l and k <= 8 (any non-integer mu, any k)")
print("     |D^k f|_F >= |D^k f[e_r,...,e_r]| = |d_r^k f| (contraction with a unit tensor)")
# (1c) velocity of psi = r^(1+gamma) Psi(theta): u_r = -psi_th/r, u_th = psi_r
psi_l = rs ** (1 + g_) * Psif(th)
ur_l, ut_l = -sp.diff(psi_l, th) / rs, sp.diff(psi_l, rs)
assert sp.simplify(ur_l + rs**g_ * sp.diff(Psif(th), th)) == 0 and sp.simplify(ut_l - (1 + g_) * rs**g_ * Psif(th)) == 0
print("(1c) psi = r^(1+gamma) Psi: (u_r, u_th) = r^gamma (-Psi', (1+gamma) Psi), nonzero iff Psi is nonzero")
# (1d) caps
c_, p_, q_, a0_ = sp.symbols("c p q a0", positive=True)
far = 1 + c_ + p_ * c_ - q_ * c_
assert sp.simplify(far.subs(p_, 2 - 1 / c_) - c_ * (3 - q_)) == 0
assert sp.simplify(far.subs(p_, 2 - 2 / c_).subs(q_, 2) - (c_ - 1)) == 0
M0 = (1 + c_) * sp.eye(2) - q_ * sp.diag(2 * c_ - 1, 1) + sp.diag(a0_, 0)
print("(1d) far-field limit 1 + c + p c - q c; at p = 2 - 1/c it is c (3 - q); at p = 2 - 2/c and q = 2 it is c - 1;"
      " origin M(0) =", M0.tolist())
# (1e) k = 2 transport commutator (Leibniz)
V1, V2, h = (sp.Function(nm)(x, y) for nm in ("V1", "V2", "h"))
Vd = lambda g: V1 * sp.diff(g, x) + V2 * sp.diff(g, y)
for a, b in ((x, x), (x, y), (y, y)):
    com = sp.diff(Vd(h), a, b) - Vd(sp.diff(h, a, b))
    want = (sp.diff(V1, a, b) * sp.diff(h, x) + sp.diff(V2, a, b) * sp.diff(h, y)
            + sp.diff(V1, a) * sp.diff(h, x, b) + sp.diff(V2, a) * sp.diff(h, y, b)
            + sp.diff(V1, b) * sp.diff(h, x, a) + sp.diff(V2, b) * sp.diff(h, y, a))
    assert sp.simplify(com - want) == 0
print("(1e) D^2 (V.Dh) - V.D D^2 h = D^2 V . Dh + 2 Sym(DV . D^2 h): the D^2 V coefficient meets the level-1 norm")
# (1f) the 2 x 2 example L = -a I + b J
aa, bb = sp.symbols("a b", positive=True)
Lm = sp.Matrix([[-aa, -bb], [bb, -aa]])
hv = sp.Matrix(sp.symbols("h1 h2", real=True))
assert sp.simplify((hv.T * Lm * hv)[0] + aa * (hv.T * hv)[0]) == 0
assert sp.simplify(Lm.T * Lm - (aa**2 + bb**2) * sp.eye(2)) == sp.zeros(2)
print("(1f) L = -a I + b J: <Lh, h> = -a |h|^2 and L^T L = (a^2 + b^2) I, so ||L^-1|| = (a^2 + b^2)^(-1/2)")
# (1g) polar Hessian rules for f = r^e W^beta P(t) sin(m th) (T = T_(beta,e), Top below):
#   f_rr = r^(e-2) W^beta T_(beta,e-1) T_(beta,e) P sin, d_r(f_th/r) = r^(e-2) W^beta m T_(beta,e-1) P cos,
#   f_r/r + f_thth/r^2 = r^(e-2) W^beta (T_(beta,e) P - m^2 P) sin; Cartesian = Q H Q^T, Q = [[cos, -sin], [sin, cos]]
tt = sp.symbols("t", positive=True)
Ppol = 2 - 3 * tt + 5 * tt**3
Tsym = lambda P, beta, e: (e - 2 * beta * tt) * P + 2 * tt * (1 - tt) * sp.diff(P, tt)
for e, beta, m in ((2, sp.Rational(7, 10), 2), (1, sp.Rational(3, 10), 3), (2, sp.Rational(9, 20), 4)):
    rr = sp.sqrt(x**2 + y**2)
    tx, Wx = rr**2 / (1 + rr**2), 1 / (1 + rr**2)
    f = rr**e * Wx**beta * Ppol.subs(tt, tx) * sp.sin(m * sp.atan2(y, x))
    Hc = sp.Matrix([[sp.diff(f, x, x), sp.diff(f, x, y)], [sp.diff(f, x, y), sp.diff(f, y, y)]]).subs(pt)
    r0 = sp.sqrt(sp.Rational(6, 5) ** 2 + sp.Rational(7, 10) ** 2)
    t0, th0 = r0**2 / (1 + r0**2), sp.atan2(sp.Rational(7, 10), sp.Rational(6, 5))
    pref = r0 ** (e - 2) * (1 - t0) ** beta
    TP = Tsym(Ppol, beta, e)
    Hrr = pref * Tsym(TP, beta, e - 1).subs(tt, t0) * sp.sin(m * th0)
    Hrt = pref * m * Tsym(Ppol, beta, e - 1).subs(tt, t0) * sp.cos(m * th0)
    Htt = pref * (TP - m**2 * Ppol).subs(tt, t0) * sp.sin(m * th0)
    Qm = sp.Matrix([[sp.cos(th0), -sp.sin(th0)], [sp.sin(th0), sp.cos(th0)]])
    Hp = Qm * sp.Matrix([[Hrr, Hrt], [Hrt, Htt]]) * Qm.T
    assert max(abs(sp.N(v, 50)) for v in (Hc - Hp)) < 1e-40
print("(1g) polar Hessian rules for r^e W^beta P(t) sin(m th) checked against Cartesian Hessians (3 cases)")
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
          "C1-N1-005": "c1n1_005_d2w_j7_n4_X3_mid180_exact.json",
          "C1-N1-007": "c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json"}[name]
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



# =============================== (2) exact profiles and expansions ===============================
CANDS = ["state131", "d2", "Mpen2", "C1-N1-005", "C1-N1-007"]
LJ = 4                                             # W-jet length (l = 0..3)


def wjet(P):
    """first LJ coefficients of P(1 - W) in powers of W (exact)"""
    out, D, fact = [], P, 1
    for l in range(LJ):
        out.append(fmpq((-1) ** l, fact) * D(fmpq(1)))
        D = D.derivative()
        fact *= l + 1
    return out


def jmul(A, B):
    return [sum((A[i] * B[l - i] for i in range(l + 1)), fmpq(0)) for l in range(LJ)]


def binom_q(xq, k):
    out = fmpq(1)
    for i in range(k):
        out = out * (xq - i) / (i + 1)
    return out


def r_expansion(jets, beta):
    """r W^beta sum_l p_l W^l = sum_L c_L r^(1 - 2 beta - 2L), W = r^-2 (1 + r^-2)^-1"""
    return [sum((jets[l] * binom_q(-beta - l, L - l) for l in range(L + 1)), fmpq(0)) for L in range(LJ)]


def addjet(d, key, J, s=fmpq(1)):
    old = d.get(key, [fmpq(0)] * LJ)
    d[key] = [o + s * v for o, v in zip(old, J)]


def qf(v):
    return float(v.p) / float(v.q) if abs(v.p) < 10**300 and v.q < 10**300 else float(arb(v))


def l2_circle(vec):                                # ||sum v_n sin n th||_(L2(0, 2 pi)) = sqrt(pi sum v_n^2)
    return (np.pi * sum(qf(v) ** 2 for v in vec.values())) ** 0.5


FIELDS = {}
P2 = {}
for name in CANDS:
    t1 = time.monotonic()
    c, chi, a0src = load(name)
    delta, R, S = build(c, chi)
    gam = 1 / c
    assert delta == 1 - gam and 0 < gam < 1
    aj = lambda j: (j + 1) * delta / 2
    FIELDS[name] = (c, delta, R, S)
    # (2a) leading density and stream profiles (K = 1, l = 0): rho ~ r^gamma G, psi ~ r^(1+gamma) Psi
    G = {n: P(fmpq(1)) for (j, n), P in R.items() if j == 0 and P(fmpq(1)) != 0}
    Psi = {n: P(fmpq(1)) for (j, n), P in S.items() if j == 0 and P(fmpq(1)) != 0}
    assert G and Psi
    for (j, n), P in R.items():
        if j == 0:
            Q = Top(Top(P, aj(0), 1), aj(0), 0)
            assert Q(fmpq(1)) == gam * (gam - 1) * P(fmpq(1))
    Gpi2 = sum((v * (1 if (n - 1) % 4 == 0 else -1) for n, v in G.items()), fmpq(0))
    # density expansion: rho = sum_K r W^(K delta/2) ...; jets per (K, n)
    rhoJ = {}
    for (j, n), P in R.items():
        addjet(rhoJ, (j + 1, n), wjet(P))
    rho_exp = {}
    for (K, n), J in rhoJ.items():
        for L, v in enumerate(r_expansion(J, K * delta / 2)):
            if v != 0:
                rho_exp.setdefault((K, L), {})[n] = v
    # residual F = c r rho_r + u_r rho_r + u_th rho_th / r - rho, every term r W^(K delta/2) P sin(n th)
    FJ = {}
    TRJ, RJ = {}, {}
    for (j, n), P in R.items():
        TRJ[(j, n)], RJ[(j, n)] = wjet(Top(P, aj(j), 1)), wjet(P)
        addjet(FJ, (j + 1, n), [c * a - b for a, b in zip(TRJ[(j, n)], RJ[(j, n)])])
    SJ, TSJ = {}, {}
    for (i, m), P in S.items():
        SJ[(i, m)], TSJ[(i, m)] = wjet(P), wjet(Top(P, aj(i), 2))
    for (i, m) in S:
        for (j, n) in R:
            K = i + j + 2
            A = [-m * v for v in jmul(SJ[(i, m)], TRJ[(j, n)])]        # coefficient of cos(m th) sin(n th)
            B = [n * v for v in jmul(TSJ[(i, m)], RJ[(j, n)])]         # coefficient of sin(m th) cos(n th)
            addjet(FJ, (K, n + m), [(a + b) / 2 for a, b in zip(A, B)])
            if n > m:
                addjet(FJ, (K, n - m), [(a - b) / 2 for a, b in zip(A, B)])
            elif m > n:
                addjet(FJ, (K, m - n), [(b - a) / 2 for a, b in zip(A, B)])
    F_exp = {}
    for (K, n), J in FJ.items():
        for L, v in enumerate(r_expansion(J, K * delta / 2)):
            if v != 0:
                F_exp.setdefault((K, L), {})[n] = v
    expo = lambda K, L: 1 - K * delta - 2 * L
    keys = sorted({k for k in F_exp}, key=lambda k: -qf(expo(*k)))
    # no two (K, L) sectors share an exponent in the computed range
    allk = [(K, L) for K in range(1, max(K for K, _ in FJ) + 1) for L in range(LJ)]
    assert len({expo(*k) for k in allk}) == len(allk)
    assert (1, 0) not in F_exp                     # c gamma - 1 = 0: the r^gamma sector of F vanishes identically
    KF, LF = keys[0]
    eF = expo(KF, LF)
    rkeys = sorted(rho_exp, key=lambda k: -qf(expo(*k)))
    assert rkeys[0] == (1, 0) and rho_exp[(1, 0)] == G
    P2[name] = dict(c=c, gamma=gam, delta=delta, G=G, Psi=Psi, Gpi2=Gpi2, rho_exp=rho_exp, F_exp=F_exp, eF=eF,
                    KF=KF, LF=LF, a0=a0src)
    print(f"(2) {name}: c = {qf(c):.15f}, gamma = 1/c = {qf(gam):.12f}; {len(R)} density and {len(S)} stream keys;"
          f" {len(G)} nonzero modes of G; ||G||_(L2(0,2pi)) = {l2_circle(G):.10f}, G(pi/2) = {qf(Gpi2):.10f};"
          f" ||Psi|| = {l2_circle(Psi):.10f} [{time.monotonic() - t1:.0f} s]")
    print(f"    G_1, G_3, G_5 = {qf(G.get(1, fmpq(0))):.12f}, {qf(G.get(3, fmpq(0))):.12f}, {qf(G.get(5, fmpq(0))):.12f};"
          f" Psi_1, Psi_3 = {qf(Psi.get(1, fmpq(0))):.12f}, {qf(Psi.get(3, fmpq(0))):.12f}")
    print(f"    identity (T_(a0,0) T_(a0,1) R_(0,n))(1) = gamma (gamma - 1) R_(0,n)(1) exact for all n;"
          f" gamma (gamma - 1) = {qf(gam * (gam - 1)):.12f}")
    print(f"    density sectors (K, l) in order: " + ", ".join(f"({K},{L}) {qf(expo(K, L)):+.6f}" for K, L in rkeys[:5]))
    print(f"    residual sectors (K, l) in order (exact zero sectors omitted): "
          + ", ".join(f"({K},{L}) {qf(expo(K, L)):+.6f} [{l2_circle(F_exp[(K, L)]):.6g}]" for K, L in keys[:6]))
    print(f"    leading residual exponent e_F = {qf(eF):+.9f} = 1 - {KF} delta - {2 * LF} (sector (K, l) = ({KF}, {LF}),"
          f" c1-n1 label (h, q) = ({KF - 1}, {LF}))")

# comparison with the c1-n1 sector tables and with the state 131 value of REVIEW_T4_058 C1
CMP = {}
for name, fn in (("C1-N1-005", "c1n1_005_sector_table.json"), ("C1-N1-007", "c1n1_007_sector_table.json")):
    tab = json.loads((HERE / "data" / fn).read_text())
    d = P2[name]
    assert fmpq(*map(int, tab["cl_exact"].split("/"))) == d["c"]
    nz = zz = 0
    worst = 0.0
    for row in tab["rows"]:
        e = fmpq(*map(int, row["exponent_exact"].split("/")))
        hit = [(K, L) for K, L in [(K, L) for K in range(1, 40) for L in range(LJ)] if 1 - K * d["delta"] - 2 * L == e]
        if not hit:
            print(f"    {name}: table exponent {row['exponent']:+.6f} not of the form 1 - K delta - 2l with l <= 3")
            continue
        sec = d["F_exp"].get(hit[0], {})
        if row["status"] == "EXACT-ZERO":
            assert not sec, (name, hit[0])
            zz += 1
        else:
            nrm = l2_circle(sec)
            rel = abs(nrm - row["full_circle_L2"]) / row["full_circle_L2"]
            relc = max(abs(qf(sec.get(int(n), fmpq(0))) - v) / max(1.0, abs(v))
                       for n, v in row["coefficients_float"].items())
            worst = max(worst, rel, relc)
            nz += 1
    th0 = tab["Theta0_float"]
    relG = max(abs(qf(d["G"].get(int(n), fmpq(0))) - v) / abs(v) for n, v in th0.items())
    CMP[name] = dict(zero_rows=zz, nonzero_rows=nz, worst_rel=worst, Theta0_rel=relG)
    print(f"    {name} vs c1-n1 sector table: {zz} EXACT-ZERO rows are exactly zero here, {nz} nonzero rows agree"
          f" (worst relative difference of norms and listed coefficients {worst:.1e}); G vs Theta0_float:"
          f" worst relative difference {relG:.1e} over the {len(th0)} listed modes")
    assert worst < 1e-9
d = P2["state131"]
assert (d["KF"], d["LF"]) == (2, 0) and d["eF"] == 2 / d["c"] - 1
n10 = l2_circle(d["F_exp"][(2, 0)])
print(f"    state131: e_F = b = 2/c - 1 exactly; ||E_10||_(L2(0,2pi)) = {n10:.14f} (REVIEW_T4_058 C1: 0.18207889107113)")
assert abs(n10 - 0.18207889107113) < 1e-12
sameG = {nm: P2[nm]["G"] == P2["state131"]["G"] for nm in CANDS}
print("    G equal to the state 131 profile (exact): " + ", ".join(f"{nm} {v}" for nm, v in sameG.items()))

# (2b) threshold table (single power weight omega ~ r^p, leading-order bookkeeping)
print("(2b) weight thresholds for omega ~ <r>^p (background: sharp, from the nonzero leading term; residual: integrability"
      " of the leading residual sector)")
print(f"    {'candidate':10s} | gamma    | ||w D^2 rho||_inf, ||w D^2 u||_inf, ||D(w^2 grad rho)/w||_inf finite iff p <= 2 - gamma"
      f" | ||w D^3 .||_inf iff p <= 3 - gamma | e_F | ||w D^2 F||_2 iff p < 1 - e_F | ||w D^3 F||_2 iff p < 2 - e_F")
THR = {}
for name in CANDS:
    d = P2[name]
    g, eF = qf(d["gamma"]), qf(d["eF"])
    THR[name] = dict(gamma=g, p_bg2=2 - g, p_bg3=3 - g, p_bg4=4 - g, eF=eF, p_P2=1 - eF, p_Q3=2 - eF)
    print(f"    {name:10s} | {g:.6f} | {2 - g:.6f} | {3 - g:.6f} | {eF:+.6f} | {1 - eF:.6f} | {2 - eF:.6f}")
OUT["part2"] = {nm: dict(c=str(P2[nm]["c"]), gamma=str(P2[nm]["gamma"]), eF=str(P2[nm]["eF"]),
                         sector=[P2[nm]["KF"], P2[nm]["LF"]], G_norm=l2_circle(P2[nm]["G"]), G_pi2=qf(P2[nm]["Gpi2"]),
                         Psi_norm=l2_circle(P2[nm]["Psi"]), leading_F_norm=l2_circle(P2[nm]["F_exp"][(P2[nm]["KF"], P2[nm]["LF"])]),
                         thresholds=THR[nm], same_G_as_state131=sameG[nm]) for nm in CANDS}
OUT["part2_compare"] = CMP


# =============================== (3) arb: d_r^2 rho on the ray theta = pi/2 ===============================
ctx.prec = 256
print("(3) arb at 256 bits: d_r^2 rho(r, pi/2) = sum r^-1 W^(a_j) (T_(a_j,0) T_(a_j,1) R_(j,n))(t) sin(n pi/2);"
      " limit gamma (gamma - 1) G(pi/2) r^(gamma - 2)")
RAY = {}
for name in CANDS:
    c, delta, R, S = FIELDS[name]
    gam = 1 / c
    aj = lambda j: (j + 1) * delta / 2
    QQ = {key: Top(Top(P, aj(key[0]), 1), aj(key[0]), 0) for key, P in R.items()}
    lim = P2[name]["gamma"] * (P2[name]["gamma"] - 1) * P2[name]["Gpi2"]
    rows = []
    for e10 in (1, 2, 4, 6, 8):
        rq = fmpq(10) ** e10
        tq, Wq_ = rq * rq / (1 + rq * rq), 1 / (1 + rq * rq)
        tot = arb(0)
        for (j, n), Q in QQ.items():
            sgn = 1 if (n - 1) % 4 == 0 else -1
            tot += sgn * arb(Q(tq)) * arb(Wq_) ** arb(aj(j)) / arb(rq)
        scaled = tot * arb(rq) ** (2 - arb(gam))
        r32 = tot * arb(rq) ** arb(fmpq(3, 2))
        rows.append(dict(r=f"1e{e10}", d2rho=tot.str(12, radius=False), scaled=scaled.str(12, radius=False),
                         r32=r32.str(10, radius=False), rad=float(tot.rad())))
        print(f"    {name:10s} r = 1e{e10}: d_r^2 rho = {tot.str(12, radius=True)};  r^(2-gamma) d_r^2 rho ="
              f" {scaled.str(12, radius=False)} (limit {qf(lim):.12f});  r^(3/2) |d_r^2 rho| = {abs(r32).str(10, radius=False)}")
        assert tot.rad() < 1e-30 * abs(tot.mid()) + 1e-60
    RAY[name] = dict(limit=qf(lim), rows=rows)
OUT["part3"] = RAY
print(f"    r^(3/2) |d_r^2 rho| ~ |gamma (gamma - 1) G(pi/2)| r^(gamma - 1/2), gamma - 1/2 = {qf(P2['state131']['gamma']) - 0.5:.6f}:"
      " unbounded, with doubling only at r ~ 2^(1/(gamma - 1/2))")


# =============================== (4) FLOAT cap map lambda_min M_(q,w) and sup w |D^2 rho| ===============================
# M_(q,w) = (1 + c + V.D log w) I - q (c I + Sym Du) + A, A = [[rho_y, -rho_x/2], [-rho_x/2, 0]] (T1_check.py Part D,
# TP-4); w = (1 + r^2/R^2)^(p/2), V.D log w = p V.X/(R^2 + r^2), V.X = c r^2 + r u_r.
# Per-mode radial values in arb (prec 192), angular sums in numpy; arb re-evaluation at every grid minimizer.
ctx.prec = 192
KDEC = 40
RGRID = [None] + [(k, ) for k in range(-3 * KDEC, 6 * KDEC + 1)]          # None = origin; else r = 10^(k/KDEC)
NTH = 181
TH = np.linspace(0.0, np.pi / 2, NTH)                                        # theta_i = i pi/360
PIa = arb.pi()


def r_arb(g):
    return arb(0) if g is None else arb(10) ** (arb(g[0]) / KDEC)


# q = 0 is the L^2 level: lambda_min = 1 + c + V.D log w - theta(X), theta = (|grad rho| - rho_y)/2 (the pointwise
# packet rate of the signed L^2 estimate; its grid minimum bounds 1 + c - sup theta from above)
QS = [(fmpq(0), "0"), (fmpq(2), "2"), (fmpq(2) + fmpq(1, 1024), "2+2^-10"), (fmpq(5, 2), "5/2")]


def weights_for(gam):
    W = [("unweighted", fmpq(0), fmpq(1)), ("omega_2 = (1 + 4 r^2)^(2/5)", fmpq(4, 5), fmpq(1, 2))]
    for plab, pv in (("2 - 2 gamma", 2 - 2 * gam), ("1", fmpq(1)), ("6/5", fmpq(6, 5)), ("7/5", fmpq(7, 5)),
                     ("2 - gamma", 2 - gam), ("3/2", fmpq(3, 2))):
        for Rv in (fmpq(1, 4), fmpq(1, 2), fmpq(1), fmpq(2)):
            W.append((f"p = {plab}, R = {Rv}", pv, Rv))
    return W


QUANT = ("rr", "rt", "ur", "Hrr", "Hrt", "Htt", "Grr", "Grt", "Gtt")
CAPS = {}
for name in CANDS:
    t1 = time.monotonic()
    c, delta, R, S = FIELDS[name]
    gam = 1 / c
    aj = lambda j: (j + 1) * delta / 2
    modes = sorted({n for _, n in list(R) + list(S)})
    mi = {n: i for i, n in enumerate(modes)}
    polys = {}                                                              # (quantity, mode) -> [(j, poly, r-power)]
    for (j, n), P in R.items():
        a = aj(j)
        T1 = Top(P, a, 1)
        polys.setdefault(("rr", n), []).append((j, T1, 0))
        polys.setdefault(("rt", n), []).append((j, n * P, 0))
        polys.setdefault(("Grr", n), []).append((j, Top(T1, a, 0), -1))
        polys.setdefault(("Grt", n), []).append((j, n * Top(P, a, 0), -1))
        polys.setdefault(("Gtt", n), []).append((j, T1 - n * n * P, -1))
    for (j, n), P in S.items():
        a = aj(j)
        T2 = Top(P, a, 2)
        polys.setdefault(("ur", n), []).append((j, -n * P, 1))
        polys.setdefault(("Hrr", n), []).append((j, Top(T2, a, 1), 0))
        polys.setdefault(("Hrt", n), []).append((j, n * Top(P, a, 1), 0))
        polys.setdefault(("Htt", n), []).append((j, T2 - n * n * P, 0))
    apolys = {k: [(j, arb_poly([arb(cf) for cf in P.coeffs()]), e) for j, P, e in v] for k, v in polys.items()}
    jmax = max(j for j, _ in list(R) + list(S))
    TAB = {qn: [[arb(0)] * len(modes) for _ in RGRID] for qn in QUANT}
    for ig, g in enumerate(RGRID):
        ra = r_arb(g)
        ta, Wa = (arb(0), arb(1)) if g is None else (ra * ra / (1 + ra * ra), 1 / (1 + ra * ra))
        Wp = [Wa ** arb(aj(j)) for j in range(jmax + 1)]
        for (qn, n), lst in apolys.items():
            if g is None and qn[0] == "G":
                continue
            tot = arb(0)
            for j, Pa, e in lst:
                v = Pa(ta) * Wp[j]
                if e == 1:
                    v = v * ra
                elif e == -1:
                    v = v / ra
                tot += v
            TAB[qn][ig][mi[n]] = tot
    maxrad = max(max(float(v.rad()) for v in row) for qn in QUANT for row in TAB[qn])
    F = {qn: np.array([[float(v.mid()) for v in row] for row in TAB[qn]]) for qn in QUANT}
    sinM = np.sin(np.outer(modes, TH))
    cosM = np.cos(np.outer(modes, TH))
    rv = np.array([0.0] + [10 ** (g[0] / KDEC) for g in RGRID[1:]])
    RG = rv[:, None] * np.ones(NTH)[None, :]
    co, si = np.cos(TH)[None, :], np.sin(TH)[None, :]
    rho_r, rho_t = F["rr"] @ sinM, F["rt"] @ cosM
    u_r = F["ur"] @ cosM
    hrr, hrt, htt = F["Hrr"] @ sinM, F["Hrt"] @ cosM, F["Htt"] @ sinM
    rho_x, rho_y = co * rho_r - si * rho_t, si * rho_r + co * rho_t
    pxx = co**2 * hrr - 2 * co * si * hrt + si**2 * htt
    pyy = si**2 * hrr + 2 * co * si * hrt + co**2 * htt
    pxy = co * si * hrr + (co**2 - si**2) * hrt - co * si * htt
    cf = qf(c)
    S11, S22, S12 = cf - pxy, cf + pxy, (pxx - pyy) / 2                   # c I + Sym Du, u = (-psi_y, psi_x)
    VX = cf * RG**2 + RG * u_r
    spread0 = float(max(np.ptp(a[0]) for a in (rho_x, rho_y, pxx, pyy, pxy)))
    # min over the grid (r > 0) of V.X/r^2 = c + u_r/r (FLOAT): positive means no stagnation point of V on the grid and
    # every orbit crosses each circle outward (notes/T2_localized_BL2.md, section 7 item 2)
    vxr = VX[1:] / RG[1:] ** 2
    iv, kv = np.unravel_index(np.argmin(vxr), vxr.shape)
    vx_min = dict(min=float(vxr[iv, kv]), r=float(rv[1 + iv]), theta=float(TH[kv]))
    # theta(X) = (|grad rho| - rho_y)/2 on the grid (FLOAT): its maximum, for the q = 0 rows
    thX = (np.sqrt(rho_x**2 + rho_y**2) - rho_y) / 2
    it, kt = np.unravel_index(np.argmax(thX), thX.shape)
    theta_max = dict(max=float(thX[it, kt]), r=float(rv[it]), theta=float(TH[kt]))
    res = {}
    for wlab, pv, Rv in weights_for(gam):
        pf, Rf = qf(pv), qf(Rv)
        dl = pf * VX / (Rf**2 + RG**2)
        for qv, qlab in QS:
            qn_ = qf(qv)
            m11 = 1 + cf + dl - qn_ * S11 + rho_y
            m22 = 1 + cf + dl - qn_ * S22
            m12 = -qn_ * S12 - rho_x / 2
            lm = (m11 + m22) / 2 - np.sqrt(((m11 - m22) / 2) ** 2 + m12**2)
            i, k = np.unravel_index(np.argmin(lm), lm.shape)
            # arb value at the minimizing grid point (rigorous upper bound on the TP-4 cap for this weight)
            g = RGRID[i]
            ra = r_arb(g)
            tha = PIa * k / 360
            sn = [(arb(n) * tha).sin() for n in modes]
            cs = [(arb(n) * tha).cos() for n in modes]
            dot = lambda qn, trig: sum((TAB[qn][i][mi[n]] * trig[mi[n]] for n in modes), arb(0))
            a_rr, a_rt, a_ur = dot("rr", sn), dot("rt", cs), dot("ur", cs)
            a_hrr, a_hrt, a_htt = dot("Hrr", sn), dot("Hrt", cs), dot("Htt", sn)
            C, Sn = tha.cos(), tha.sin()
            a_rx, a_ry = C * a_rr - Sn * a_rt, Sn * a_rr + C * a_rt
            a_xx = C * C * a_hrr - 2 * C * Sn * a_hrt + Sn * Sn * a_htt
            a_yy = Sn * Sn * a_hrr + 2 * C * Sn * a_hrt + C * C * a_htt
            a_xy = C * Sn * a_hrr + (C * C - Sn * Sn) * a_hrt - C * Sn * a_htt
            ca, qa = arb(c), arb(qv)
            vx = ca * ra * ra + ra * a_ur
            dla = arb(pv) * vx / (arb(Rv) ** 2 + ra * ra)
            b11 = 1 + ca + dla - qa * (ca - a_xy) + a_ry
            b22 = 1 + ca + dla - qa * (ca + a_xy)
            b12 = -qa * (a_xx - a_yy) / 2 - a_rx / 2
            lam = (b11 + b22) / 2 - (((b11 - b22) / 2) ** 2 + b12**2).sqrt()
            assert abs(float(lam.mid()) - float(lm[i, k])) < 1e-9 * max(1.0, abs(float(lm[i, k])))
            far = 1 + cf + pf * cf - qn_ * cf
            res[(wlab, qlab)] = dict(weight=wlab, p=str(pv), R=str(Rv), q=str(qv), float_min=float(lm[i, k]),
                                     arb_upper=float(lam.upper()), arb=lam.str(10, radius=True), r=float(rv[i]),
                                     theta=float(TH[k]), x=float(rv[i] * np.cos(TH[k])), y=float(rv[i] * np.sin(TH[k])),
                                     far_limit=far, at_rmax=float(lm[-1].min()))
    # sup w |D^2 rho|_F (FLOAT; r from 1e-3 to 1e6)
    grr, grt, gtt = F["Grr"][1:] @ sinM, F["Grt"][1:] @ cosM, F["Gtt"][1:] @ sinM
    d2f = np.sqrt(grr**2 + 2 * grt**2 + gtt**2).max(axis=1)                # max over theta at each r
    rr1 = rv[1:]
    sups = {}
    for wlab, pv, Rv in weights_for(gam):
        pf, Rf = qf(pv), qf(Rv)
        wd = (1 + rr1**2 / Rf**2) ** (pf / 2) * d2f
        i = int(np.argmax(wd))
        sups[wlab] = dict(sup=float(wd[i]), r_at_sup=float(rr1[i]), at_1e4=float(wd[np.argmin(abs(rr1 - 1e4))]),
                          at_1e6=float(wd[-1]))
    # leading-order check of the far field: r^(2 - gamma) max_theta |D^2 rho|_F at r = 1e6 vs the profile formula (1a)
    gf = qf(gam)
    Gc = {n: qf(v) for n, v in P2[name]["G"].items()}
    thf = np.linspace(0, np.pi / 2, 4001)
    G0 = sum(v * np.sin(n * thf) for n, v in Gc.items())
    G1 = sum(n * v * np.cos(n * thf) for n, v in Gc.items())
    G2 = sum(-n * n * v * np.sin(n * thf) for n, v in Gc.items())
    prof = np.sqrt((gf * (gf - 1) * G0) ** 2 + 2 * ((gf - 1) * G1) ** 2 + (gf * G0 + G2) ** 2).max()
    lead = float(d2f[-1] * rr1[-1] ** (2 - gf))
    CAPS[name] = dict(caps=list(res.values()), sup_wD2rho=sups, profile_max=float(prof), r2mg_D2rho_1e6=lead,
                      maxrad=maxrad, origin_spread=spread0, VX_over_r2_min=vx_min, theta_grid_max=theta_max)
    print(f"(4) {name}: {len(modes)} modes, {len(RGRID)} radii x {NTH} angles; largest arb radius in the radial tables"
          f" {maxrad:.1e}; theta-spread of the Cartesian first and second derivatives at r = 0: {spread0:.1e}"
          f" [{time.monotonic() - t1:.0f} s]")
    print(f"    min V.X/r^2 = c + u_r/r on the grid (FLOAT): {vx_min['min']:.6f} at r = {vx_min['r']:.3g}, th = {vx_min['theta']:.3f};"
          f" max theta(X) on the grid (FLOAT): {theta_max['max']:.6f} at r = {theta_max['r']:.3g}, th = {theta_max['theta']:.3f}")
    print(f"    far field: r^(2-gamma) max_th |D^2 rho|_F at r = 1e6 = {lead:.8f};"
          f" max_th sqrt(g^2 (g-1)^2 G^2 + 2 (g-1)^2 G'^2 + (g G + G'')^2) = {prof:.8f}")
    print(f"    {'weight':30s} | " + " | ".join(f"q = {lab:>8s}: min (arb upper) @ r, far limit" for _, lab in QS))
    for wlab, pv, Rv in weights_for(gam):
        cells = []
        for _, qlab in QS:
            e = res[(wlab, qlab)]
            cells.append(f"{e['float_min']:+.6f} ({e['arb_upper']:+.6f}) @ r={e['r']:.3g}, th={e['theta']:.3f}; {e['far_limit']:+.4f}")
        print(f"    {wlab:30s} | " + " | ".join(cells))
    print(f"    sup w |D^2 rho|_F on 1e-3 <= r <= 1e6 (FLOAT; value at r = 1e4 and at r = 1e6):")
    for wlab, v in sups.items():
        print(f"    {wlab:30s}  sup {v['sup']:.6f} @ r = {v['r_at_sup']:.3g};  r = 1e4: {v['at_1e4']:.6f};  r = 1e6: {v['at_1e6']:.6f}")
    del TAB, F
# validation against the c1-t4 / c1-t1 state 131 values (T1_check.out Part D)
e = CAPS["state131"]["caps"]
get = lambda wl, ql: next(v for v in e if v["weight"] == wl and v["q"] == ql)
print("    state131 check: omega_2, q = 2:", get("omega_2 = (1 + 4 r^2)^(2/5)", "2")["float_min"],
      "@", (round(get("omega_2 = (1 + 4 r^2)^(2/5)", "2")["x"], 3), round(get("omega_2 = (1 + 4 r^2)^(2/5)", "2")["y"], 3)),
      "(T1_check: 0.6115039188528522 at (250.891, 250.891))")
OUT["part4"] = CAPS

print(f"total {time.monotonic() - T0:.0f} s")
(HERE / "data/t4_094_review_results.json").write_text(json.dumps(OUT, indent=1, default=str))
print("wrote data/t4_094_review_results.json")
