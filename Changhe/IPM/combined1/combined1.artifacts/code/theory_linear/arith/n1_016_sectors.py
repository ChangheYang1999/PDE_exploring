"""Independent reproduction of the far-field sector flags of C1-N1-016-legqs25-quot013 (c1-coord NOTES_FOR_TEAM
07:04Z item 4 (b); c1-t1 ACK item 6 asks for the sectors (4,1), (9,0), (5,1), (1,2) and the far-field form of the
legqs generators). Write-up: notes/N1_016_SECTORS.md.

Run from artifacts/:  OMP_NUM_THREADS=1 python3 -B -u arith/n1_016_sectors.py
Needs python-flint and numpy.

Parts:
  (A) exact: the expansion at W = 1/(1 + r^2) = 0 of every legqs generator profile
      t^m ts^w us^Q P_n(2 ts - 1), ts = r^2/(R0^2 + r^2), us = 1 - ts = R0^2 W/(1 + (R0^2 - 1) W):
      the coefficients of W^0 .. W^(Q-1) vanish and that of W^Q is R0^(2Q).
  (B) exact: my constructor (copied from arith/t4_294_review.py, itself copied from t4_249_review.py) on the mono and
      leg generators; density and stream sectors K <= 16, L <= 2; nonresonance; Poisson; Theta_0 against state 131;
      every residual coefficient at exponent >= gamma - 4 and at (10,0), (6,1), (7,1), (8,1), products included.
  (C) comparisons: c1-n1 sector_table.json (floats) and c1-n4 N4-242 direct.json (exact sine coefficients).
  (D) consequences: T4-281 formula (3) at (4,1), the REVIEW_T4_281 R2 dipole test at (1,2), the T4-294 forced tail,
      the T4-295 coefficients A1_m, and the T4-295 repair (6) applied to 016 and rebuilt from scratch.
Output: logs/n1_016_sectors.log, data/n1_016_sectors_results.json.
"""
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from flint import fmpq, fmpq_poly

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parents[1]
T0 = time.monotonic()
OUT = {}
IN = HERE / "data/n1_016_inputs"
GEN = "quot013_legqs25_m9to15_cpu_m16_exact.json"
SHA = {GEN: "a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42",
       "sector_table.json": "c8241fef3410dbca2322d15264a386fcfc26c1b5922621b93a08c9495000dde8",
       "n4_242_direct.json": "502ed0004bdf6d35a4e42ec16ea21daf8efc3fe7adcbe52695a70093acfb60f3"}


def sha(pth):
    return hashlib.sha256(Path(pth).read_bytes()).hexdigest()


for fn_, h_ in SHA.items():
    assert sha(IN / fn_) == h_, fn_
assert sha(HERE / "data/a2_state131_exact.json") == "8b52b460866d620c452edcfa3f9181481a1966b0de35f9d7dc38e46ff35342b8"
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


# =============================== settings for (B) to (D) ===============================
LJ = 3                          # W-jet length: sectors L = 0, 1, 2
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



# =============================== (A) far-field form of the legqs generators ===============================
D = json.loads((IN / GEN).read_text())
c = fmpq(*map(int, D["cl_exact"].split("/")))
assert c == fmpq(4076476460239181, 2251799813685248)
gam = 1 / c
GENS = D["generators"]
Wv = fmpq_poly([0, 1])


def trunc(P, N):
    return fmpq_poly([P[k] for k in range(N)])


def inv_series(P, N):           # 1/P mod W^N, P(0) != 0
    b = [fmpq(0)] * N
    b[0] = 1 / P[0]
    for k in range(1, N):
        b[k] = -sum((P[i] * b[k - i] for i in range(1, k + 1)), fmpq(0)) / P[0]
    return fmpq_poly(b)


def pow_trunc(P, e, N):
    out = fmpq_poly([1])
    for _ in range(e):
        out = trunc(out * P, N)
    return out


def compose_trunc(Pt, S, N):    # Pt(S(W)) mod W^N, Horner
    out = fmpq_poly([0])
    for k in range(Pt.degree(), -1, -1):
        out = trunc(out * S, N) + Pt[k]
    return out


t1 = time.monotonic()
lq = [g_ for g_ in GENS if g_["spec"][0] == "legqs"]
ok_lq, Qs, R0s = True, set(), set()
for g_ in lq:
    w_, n_, Qd, R0 = map(int, g_["spec"][1:])
    Qs.add(Qd)
    R0s.add(R0)
    N = Qd + 2
    R02 = fmpq(R0)**2
    us = trunc(R02 * Wv * inv_series(1 + (R02 - 1) * Wv, N), N)
    ts = 1 - us
    Y = trunc(pow_trunc(1 - Wv, g_["m"], N) * pow_trunc(ts, w_, N), N)
    Y = trunc(Y * pow_trunc(us, Qd, N), N)
    Y = trunc(Y * compose_trunc(legendre_shift(n_), ts, N), N)
    ok_lq = ok_lq and all(Y[k] == 0 for k in range(Qd)) and Y[Qd] == R02**Qd and legendre_shift(n_)(fmpq(1)) == 1
OUT["A"] = {"legqs_count": len(lq), "Q_values": sorted(Qs), "R0_values": sorted(R0s), "jets_vanish_below_Q": ok_lq,
            "branches": sorted({g_["j"] for g_ in lq}), "m_values": sorted({g_["m"] for g_ in lq})}
print("(A) %d legqs generators, branches %s, m in %s, Q in %s, R0 in %s: in W = 1/(1 + r^2) every profile"
      " t^m ts^w us^Q P_n(2 ts - 1) is R0^(2Q) W^Q + O(W^(Q+1)) (exact): %s; %.1f s"
      % (len(lq), OUT["A"]["branches"], OUT["A"]["m_values"], sorted(Qs), sorted(R0s), ok_lq, time.monotonic() - t1))
assert ok_lq and min(Qs) >= LJ
print("    so these generators enter only potential, density and stream sectors with L >= %d; the residual"
      " sectors with L <= 2 (all those at exponent >= gamma - 4) do not see them" % min(Qs))

# =============================== (B) constructor on the mono and leg generators ===============================
t1 = time.monotonic()
chi = {}
kinds = {}
for g_ in GENS:
    sp_ = g_["spec"]
    kinds[sp_[0]] = kinds.get(sp_[0], 0) + 1
    if sp_[0] == "legqs":
        continue
    num, den = (g_["coef"].split("/") + ["1"])[:2]
    co = fmpq(int(num), int(den))
    if sp_[0] == "mono":
        T = tp**sp_[1]
    else:
        assert sp_[0] == "leg"
        T = tp**sp_[1] * legendre_shift(sp_[2])
    addto(chi, (g_["j"], 2 * g_["m"]), co * tp**g_["m"] * T)
jmax = max(j for (j, _) in chi)
delta, R, S = build(c, chi)
expo = lambda K, L: 1 - K * delta - 2 * L
nonres = all(((i - j) * delta / 2).q != 1 for i in range(1, 17) for j in range(1, i))
allkeys = [(K, L) for K in range(1, 17) for L in range(LJ)]
assert nonres and len({expo(*kk) for kk in allkeys}) == len(allkeys)
thr = gam - 4
EXTRA = [(10, 0), (6, 1), (7, 1), (8, 1)]  # below gamma - 4; compared with c1-n1 and N4-242
keys = [kk for kk in allkeys if expo(*kk) >= thr] + EXTRA
Th, Ps = sectors(R, S, delta)
pois = all(poisson(Th.get(kk, {}), expo(*kk)) == Ps.get(kk, {}) for kk in allkeys if kk[0] <= jmax + 1)
F = residuals(Th, Ps, keys, expo, c)
c131, chi131 = load("state131")
_, R131, S131 = build(c131, chi131)
Th131, _ = sectors(R131, S131, 1 - 1 / c131)
th0_same = c131 == c and Th131[(1, 0)] == Th[(1, 0)]
order = sorted(keys, key=lambda kk: -float(expo(*kk)))
nz = [kk for kk in order if F[kk]]
zero = [kk for kk in order if not F[kk]]
OUT["B"] = {"generator_kinds": kinds, "jmax": jmax, "nonresonance_1_16": nonres, "poisson": pois,
            "theta0_equals_state131": th0_same, "zero": zero,
            "nonzero": [(kk, str(expo(*kk)), float(expo(*kk)), l2(F[kk]), max(F[kk])) for kk in nz],
            "seconds": time.monotonic() - t1}
print("(B) generators %s; mono and leg ones in branches j <= %d; (i - j) delta/2 not an integer for 1 <= j < i <= 16:"
      " %s; stream = Poisson of density for K <= %d, L <= 2: %s; Theta_0 = state 131's exactly (same c): %s"
      % (kinds, jmax, nonres, jmax + 1, pois, th0_same))
print("    residual coefficients at exponent >= gamma - 4 = %.12f and at (10,0), (6,1), (7,1), (8,1): exactly zero %s"
      % (float(thr), ", ".join("(%d,%d)" % kk for kk in zero)))
print("    nonzero: %s; %.1f s" % ("; ".join("(%d,%d) %+.12f [circle L2 norm %.10g, top harmonic %d]"
                                         % (kk + (float(expo(*kk)), l2(F[kk]), max(F[kk]))) for kk in nz),
                                  time.monotonic() - t1))

# =============================== (C) comparisons ===============================
fq = lambda v_: fmpq(*map(int, (str(v_).split("/") + ["1"])[:2]))
byexp = {expo(*kk): kk for kk in keys}
st = json.loads((IN / "sector_table.json").read_text())
cmp_n1 = []
for row in st["rows"]:
    e_ = fq(row["exponent_exact"])
    kk = byexp.get(e_)
    if kk is None:
        cmp_n1.append((row["exponent"], "not in my key list"))
        continue
    mine_zero = not F[kk]
    rel = abs(l2(F[kk]) - row["full_circle_L2"]) / max(row["full_circle_L2"], 1e-300) if not mine_zero else 0.0
    cmp_n1.append((kk, row["status"], mine_zero == (row["status"] == "EXACT-ZERO"), rel))
n1_ok = all(len(x) == 4 and x[2] and x[3] < 1e-12 for x in cmp_n1)
n4 = json.loads((IN / "n4_242_direct.json").read_text())
cmp_n4 = []
for s_ in n4["sectors"]:
    e_ = fq(s_["exponent"])
    kk = byexp.get(e_)
    theirs = {int(k_): fq(v_) for k_, v_ in s_["sine_coefficients"].items() if fq(v_) != 0}
    cmp_n4.append((kk, str(e_), kk is not None and theirs == F[kk]))
n4_ok = all(x[2] for x in cmp_n4)
OUT["C"] = {"c1n1_sector_table": cmp_n1, "c1n1_all_agree_rel_1e-12": n1_ok, "n4_242_exact": cmp_n4,
            "n4_242_all_equal": n4_ok}
print("(C) c1-n1 sector_table.json: %d rows, zero/nonzero status and circle norms agree (relative < 1e-12): %s"
      % (len(cmp_n1), n1_ok))
print("    c1-n4 N4-242 direct.json: %d sectors, exact sine coefficients equal mine: %s (sectors %s)"
      % (len(cmp_n4), n4_ok, ", ".join("(%d,%d)" % x[0] if x[0] else x[1] for x in cmp_n4)))

# =============================== (D) consequences ===============================
D41 = {}
for (j, nn), P in R.items():
    if j == 3:
        put(D41, nn, -2 * delta * P(fmpq(1)) - P.derivative()(fmpq(1)))
e41 = expo(4, 1)
ok3 = D41 == Th.get((4, 1), {})
ok4 = F[(4, 1)] == scale(D41, c * e41 - 1)
Th0 = Th[(1, 0)]
Pd = add(scale(sin_cos(Th0, {2: fmpq(1)}), gam), sin_cos({2: fmpq(1)}, dsin(Th0)))
F12 = F[(1, 2)]
dot = lambda A_, B_: sum((v * B_.get(k_, fmpq(0)) for k_, v in A_.items()), fmpq(0))
lam = dot(F12, Pd) / dot(Pd, Pd)
resid = add(F12, Pd, -lam)
rel12 = float(np.sqrt(float(dot(resid, resid)) / float(dot(F12, F12))))
f12_lin = F12 == scale(Th.get((1, 2), {}), -4 * c)
pp = 2 * gam
A1 = {}
for (j, nn), P in chi.items():
    if j == 3:
        v = pp * P(fmpq(1)) - P.derivative()(fmpq(1))
        if v != 0:
            A1[nn // 2] = v
q2 = expo(9, 0)
# the T4-295 repair (6) applied to 016: chi + sum_m -A1_m t^(m+4)(1 - t) cos(2m th) in branch 3, rebuilt from scratch
chi2 = dict(chi)
for m, v in A1.items():
    addto(chi2, (3, 2 * m), -v * tp**(m + 4) * (1 - tp))
_, R2_, S2_ = build(c, chi2)
Th2, Ps2 = sectors(R2_, S2_, delta)
F2 = residuals(Th2, Ps2, keys, expo, c)
changed = sorted(kk for kk in set(Th) | set(Th2) | set(Ps) | set(Ps2)
                 if Th.get(kk, {}) != Th2.get(kk, {}) or Ps.get(kk, {}) != Ps2.get(kk, {}))
zero_ge3 = all(not F2[kk] for kk in keys if expo(*kk) >= -3)
nz2 = [kk for kk in order if F2[kk] and expo(*kk) >= thr]
OUT["D"] = {"formula3_41": ok3, "formula4_41": ok4, "modes_41": len(D41), "theta41_norm": l2(D41),
            "F41_norm": l2(F[(4, 1)]), "F12_eq_minus4c_theta12": f12_lin, "F12_norm": l2(F12), "dipole_norm": l2(Pd),
            "R2_rel_residual": rel12, "R2_lambda": float(lam), "A1_modes": len(A1),
            "A1_l2": float(np.sqrt(sum(float(v)**2 for v in A1.values()))),
            "forced_90_norm_if_41_cancelled": l2(scale(F[(9, 0)], 1 / (1 - c * q2))),
            "repair_sectors_changed": changed, "repair_zero_at_exponent_ge_minus3": zero_ge3,
            "repair_nonzero_ge_gamma_minus_4": [(kk, float(expo(*kk)), l2(F2[kk])) for kk in nz2],
            "repair_F90_unchanged": F2[(9, 0)] == F[(9, 0)], "repair_F12_unchanged": F2[(1, 2)] == F[(1, 2)]}
print("(D) (4,1): Theta_(4,1) = T4-281 formula (3) from my branch-3 density: %s (%d modes, circle norm %.10g);"
      " F_(4,1) = (c e - 1) Theta_(4,1): %s" % (ok3, len(D41), l2(D41), ok4))
print("    T4-294: an exact correction with H_q(h) < infinity at q = e_(4,1) = %.12f has the forced tail"
      " -r^q Theta_(4,1), circle norm %.10g" % (float(e41), l2(D41)))
print("    T4-295: A1_m = p P_m(1) - P_m'(1) of branch 3 nonzero for %d modes. With the repair (6) added and rebuilt:"
      " sectors changed %s; residual zero at every exponent >= -3: %s; nonzero at exponent >= gamma - 4: %s;"
      " F_(9,0), F_(1,2) unchanged: %s, %s; forced (9,0) density norm %.6g (REVIEW_T4_294 R2)"
      % (len(A1), changed, zero_ge3, ", ".join("(%d,%d) [%.6g]" % (kk + (l2(F2[kk]),)) for kk in nz2),
         OUT["D"]["repair_F90_unchanged"], OUT["D"]["repair_F12_unchanged"],
         OUT["D"]["forced_90_norm_if_41_cancelled"]))
print("    REVIEW_T4_281 R2 at (1,2): F_(1,2) = -4c Theta_(1,2): %s; norm %.10g; dipole profile norm %.6g; relative"
      " residual after the best multiple %.6f (lambda = %.6g), so not proportional"
      % (f12_lin, l2(F12), l2(Pd), rel12, float(lam)))
(HERE / "data/n1_016_sectors_results.json").write_text(json.dumps(OUT, indent=1, default=str))
assert pois and th0_same and n1_ok and n4_ok and ok3 and ok4 and f12_lin and rel12 > 0.5
assert [kk for kk in nz if expo(*kk) >= thr] == [(4, 1), (9, 0), (5, 1), (1, 2)]
assert zero_ge3 and nz2[0] == (9, 0) and changed == [(4, 1), (4, 2)]
print("wrote data/n1_016_sectors_results.json; total %.1f s" % (time.monotonic() - T0))
