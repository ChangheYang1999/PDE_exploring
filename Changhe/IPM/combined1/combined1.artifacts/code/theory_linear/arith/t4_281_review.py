"""Independent review of T4-281 (c1-t4 research/compact_correction_tail/PROOF.md, sha256 0f256ccd...c89f8c): an exactly
compactly supported S1 L2 correction h forces F = (cX + U_R).grad R - R = O(r^(gamma-4)) (reviews/REVIEW_T4_281.md).

Run from artifacts/:  python3 -B arith/t4_281_review.py
Needs sympy, numpy, python-flint.

Parts:
  (A) sympy: the kernel (2) from the fundamental solution and the symbol; the local term -h/2 (angular mean of the
      symbol); polar form, the two columns of DK (orthogonal, length 1/(pi r^3)); d_y K = -(cos 3th, sin 3th)/(pi r^3)
      and its polar components; the Cauchy-Schwarz constants and 8/pi sqrt(pi/2) = 4 sqrt(2/pi).
  (B) FLOAT: h = y (1 - r^2)^4 on the unit disk: U[h] by polar quadrature of the kernel at several exterior points,
      against an FFT evaluation of the symbol, the bound 8/(pi r^3) int |Y||h| and the dipole term of remark R2.
  (C) exact (fmpq): density and stream of 007, 013, 014 from the c1-n1 generator files by my own constructor (copied
      from arith/t4_249_review.py), sectors (K, L), exponent 1 - K delta - 2L, L <= 2; every residual coefficient
      (T4-249 (10), products included) at exponents >= gamma - 4; the first nonzero one against the formula (4) of
      T4-281 and against c1-t4's stored coefficients (data/t4_281_inputs/t4_281_result.json); nonresonance of
      branches 1 to 16; the dipole test of remark R2 at the sector (1, 2), exponent gamma - 4.
Output: logs/t4_281_review.log, data/t4_281_review_results.json.
"""
import hashlib
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
x, y = sp.symbols("x y", real=True)
r, th, A_, X1, X2 = sp.symbols("r theta A xi1 xi2", positive=True)
Phi = -sp.log(sp.sqrt(x**2 + y**2)) / (2 * sp.pi)          # fundamental solution of -Delta
K1 = -sp.diff(Phi, x, y)                                     # symbol xi1 xi2/|xi|^2 = -d_xy (-Delta)^-1
K2 = sp.diff(Phi, x, 2)                                      # symbol -xi1^2/|xi|^2 = d_xx (-Delta)^-1
r2 = x**2 + y**2
assert sp.simplify(K1 - (-x * y / (sp.pi * r2**2))) == 0
assert sp.simplify(K2 - ((x**2 - y**2) / (2 * sp.pi * r2**2))) == 0
assert sp.simplify(sp.diff(Phi, x, 2) + sp.diff(Phi, y, 2)) == 0          # harmonic away from 0
ph = sp.Symbol("phi", real=True)
mean2 = sp.integrate(-sp.cos(ph)**2, (ph, 0, 2 * sp.pi)) / (2 * sp.pi)
mean1 = sp.integrate(sp.cos(ph) * sp.sin(ph), (ph, 0, 2 * sp.pi)) / (2 * sp.pi)
assert mean2 == sp.Rational(-1, 2) and mean1 == 0
for Kc in (K1, K2):                                          # zero angular mean on circles: p.v. kernel
    assert sp.simplify(sp.integrate(Kc.subs({x: r * sp.cos(th), y: r * sp.sin(th)}), (th, 0, 2 * sp.pi))) == 0
print("(A1) kernel (2): -d_xy and d_xx of -(log r)/(2 pi) give (-xy/(pi r^4), (x^2 - y^2)/(2 pi r^4)); symbol angular"
      " means 0 and -1/2 (the local term -h/2 of U2); both kernels have zero mean on circles")
pol = {x: r * sp.cos(th), y: r * sp.sin(th)}
Kp = [sp.simplify(Kc.subs(pol)) for Kc in (K1, K2)]
assert sp.simplify(Kp[0] + sp.sin(2 * th) / (2 * sp.pi * r**2)) == 0
assert sp.simplify(Kp[1] - sp.cos(2 * th) / (2 * sp.pi * r**2)) == 0
colr = [sp.diff(k_, r) for k_ in Kp]
colt = [sp.diff(k_, th) / r for k_ in Kp]
assert sp.simplify(colr[0] * colt[0] + colr[1] * colt[1]) == 0
assert sp.simplify(colr[0]**2 + colr[1]**2 - 1 / (sp.pi**2 * r**6)) == 0
assert sp.simplify(colt[0]**2 + colt[1]**2 - 1 / (sp.pi**2 * r**6)) == 0
dyK = [sp.simplify(sp.diff(Kc, y).subs(pol)) for Kc in (K1, K2)]
assert sp.simplify(dyK[0] + sp.cos(3 * th) / (sp.pi * r**3)) == 0
assert sp.simplify(dyK[1] + sp.sin(3 * th) / (sp.pi * r**3)) == 0
ur = sp.simplify(sp.cos(3 * th) * sp.cos(th) + sp.sin(3 * th) * sp.sin(th))
ut = sp.simplify(-sp.cos(3 * th) * sp.sin(th) + sp.sin(3 * th) * sp.cos(th))
assert sp.simplify(ur - sp.cos(2 * th)) == 0 and sp.simplify(ut - sp.sin(2 * th)) == 0
print("(A2) K = r^-2 (-sin 2th, cos 2th)/(2 pi); d_r K and r^-1 d_th K orthogonal, both of length 1/(pi r^3), so"
      " ||DK|| = 1/(pi r^3); d_y K = -(cos 3th, sin 3th)/(pi r^3), and (cos 3th, sin 3th) has polar components"
      " (cos 2th, sin 2th)")
I2 = sp.integrate(r**2 * r, (r, 0, A_)) * 2 * sp.pi
Iy2 = sp.integrate(sp.integrate(r**3 * sp.sin(th)**2, (th, 0, 2 * sp.pi)), (r, 0, A_))
assert sp.simplify(I2 - sp.pi * A_**4 / 2) == 0 and sp.simplify(Iy2 - sp.pi * A_**4 / 4) == 0
assert sp.simplify(8 / sp.pi * sp.sqrt(sp.pi / 2) - 4 * sp.sqrt(2 / sp.pi)) == 0
print("(A3) int_(|Y|<=A) |Y|^2 = pi A^4/2, int y^2 = pi A^4/4; (8/pi) sqrt(pi/2) = 4 sqrt(2/pi) = %.6f"
      % float(4 * sp.sqrt(2 / sp.pi)))
print("(A) done, %.1f s" % (time.monotonic() - T0))
OUT["A"] = "all identities exact"

# =============================== (B) FLOAT exterior field of a compact S1 test function ===============================
def Kxy(z1, z2):
    q = z1 * z1 + z2 * z2
    return -z1 * z2 / (np.pi * q * q), (z1 * z1 - z2 * z2) / (2 * np.pi * q * q)


gl, gw = np.polynomial.legendre.leggauss(160)
rho_ = (gl + 1) / 2
wr = gw / 2
phi_ = np.arange(512) * 2 * np.pi / 512
RR, PP = np.meshgrid(rho_, phi_, indexing="ij")
WW = (wr * rho_)[:, None] * (2 * np.pi / 512) * np.ones_like(PP)
Y1, Y2 = RR * np.cos(PP), RR * np.sin(PP)
H = Y2 * (1 - RR**2)**4
My = float(np.sum(Y2 * H * WW))
M1 = float(np.sum(RR * np.abs(H) * WW))
errMy, errM1 = abs(My - np.pi / 60), abs(M1 - 1 / 15)   # |sin| has kinks at nodes: M1 is only O(h^2) accurate
assert errMy < 1e-12 and errM1 < 1e-4
My, M1 = np.pi / 60, 1 / 15                             # exact values used below
Nf, Lf = 1024, 64.0
dx = Lf / Nf
g = (np.arange(Nf) - Nf // 2) * dx
GX, GY = np.meshgrid(g, g, indexing="ij")
GR2 = GX**2 + GY**2
Hg = np.where(GR2 < 1, GY * (1 - GR2)**4, 0.0)
xi = 2 * np.pi * np.fft.fftfreq(Nf, dx)
XI1, XI2 = np.meshgrid(xi, xi, indexing="ij")
Q2 = XI1**2 + XI2**2
Q2[0, 0] = 1.0
Hh = np.fft.fft2(Hg)
Uf1 = np.fft.ifft2(XI1 * XI2 / Q2 * Hh).real
Uf2 = np.fft.ifft2(-XI1**2 / Q2 * Hh).real
rowsB = []
print("(B) FLOAT, h = y (1 - r^2)^4 on |Y| <= 1 (A = 1): int y h = pi/60, int |Y||h| = 1/15 (exact; quadrature"
      " errors %.1e, %.1e)" % (errMy, errM1))
for (p1, p2) in [(2.0, 0.0), (0.0, 2.0), (1.5, 2.0), (0.0, 3.0), (3.0, 4.0), (6.0, 8.0)]:
    k1, k2 = Kxy(p1 - Y1, p2 - Y2)
    u = np.array([np.sum(k1 * H * WW), np.sum(k2 * H * WW)])
    i1, i2 = int(round(p1 / dx)) + Nf // 2, int(round(p2 / dx)) + Nf // 2
    uf = np.array([Uf1[i1, i2], Uf2[i1, i2]])
    rr_, tt_ = np.hypot(p1, p2), np.arctan2(p2, p1)
    dip = My / np.pi * rr_**-3 * np.array([np.cos(3 * tt_), np.sin(3 * tt_)])
    bound = 8 / (np.pi * rr_**3) * M1
    row = {"X": [p1, p2], "U_quad": u.tolist(), "U_fft": uf.tolist(),
           "fft_rel_diff": float(np.linalg.norm(u - uf) / np.linalg.norm(u)),
           "ratio_to_bound": float(np.linalg.norm(u) / bound),
           "dipole_rel_diff": float(np.linalg.norm(u - dip) / np.linalg.norm(u)),
           "dipole_remainder_times_r5": float(np.linalg.norm(u - dip) * rr_**5)}
    rowsB.append(row)
    print("    X = (%4.1f, %4.1f), r = %5.2f: |U| = %.6e, |U|/bound = %.5f, FFT rel. diff %.1e,"
          " (U - dipole)/|U| = %.2e,"
          " |U - dipole| r^5 = %.4e" % (p1, p2, rr_, np.linalg.norm(u), row["ratio_to_bound"], row["fft_rel_diff"],
                                         row["dipole_rel_diff"], row["dipole_remainder_times_r5"]))
assert all(rw["ratio_to_bound"] < 1 for rw in rowsB)
print("    the ratio to the bound tends to int y h/(8 int |Y||h|) = pi/32 = %.5f at every angle;"
      " the dipole remainder is O(r^-5) (second moments of an S1 function vanish)" % (np.pi / 32))
OUT["B"] = rowsB
print("(B) done, %.1f s" % (time.monotonic() - T0))

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


# =============================== (C) exact sectors of 007, 013, 014 ===============================
LJ = 3                          # W-jet length: sectors L = 0, 1, 2


def load_file(fn):              # the c1-n1 generator branch of load() in arith/t4_249_review.py
    d = json.loads((HERE / "data" / fn).read_text())
    c = fmpq(*map(int, d.get("cl", d.get("cl_exact")).split("/")))
    chi = {}
    jmax = 0
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
        jmax = max(jmax, g_["j"])
    return c, chi, jmax


def sha(p):
    return hashlib.sha256((HERE / "data" / p).read_bytes()).hexdigest()


def dot(A1, B1):
    return sum((v * B1.get(nn, fmpq(0)) for nn, v in A1.items()), fmpq(0))


c_run = fmpq(4076476460239181, 2**51)
ext = json.loads((HERE / "data/t4_281_inputs/t4_281_result.json").read_text())
extrow = {rw["candidate"]: rw for rw in ext["rows"]}
CANDS = [("007", "c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json"),
         ("013", "t4_281_inputs/c1n1_013_d2w_j7_n4_E2bal_pairU_cpu_m16_exact.json"),
         ("014", "t4_281_inputs/c1n1_014_d2w_j7_n4_E2bal_pairB_cpu_m16_exact.json")]
EXPECT = {"007": "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21",
          "013": "c07f87ddfe35e1fd82cfb86e01949749381aac7209a752c713dd01b48a478940",
          "014": "8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746"}
assert sha("t4_281_inputs/t4_281_result.json") == "e77b13367f9e10cd0e1040205e7ec0eeabba7176e9dffc1fa23a18d773fb223c"
RES = {}
for name, fn in CANDS:
    t1 = time.monotonic()
    assert sha(fn) == EXPECT[name]
    c, chi, jmax = load_file(fn)
    assert c == c_run and jmax <= 7
    delta, R, S = build(c, chi)
    gam = 1 / c
    thr = gam - 4
    expo = lambda K, L: 1 - K * delta - 2 * L
    nonres = all(((i - j) * delta / 2).q != 1 for i in range(1, 17) for j in range(1, i))
    allkeys = [(K, L) for K in range(1, 17) for L in range(LJ)]
    distinct = len({expo(*kk) for kk in allkeys}) == len(allkeys)
    assert nonres and distinct
    Th, Ps = {}, {}
    for src, dst in ((R, Th), (S, Ps)):
        for (j, nn), P in src.items():
            for L, v in enumerate(r_expansion(wjet(P), (j + 1) * delta / 2)):
                if v != 0:
                    put(dst.setdefault((j + 1, L), {}), nn, v)
    dkeys = [(K, L) for K in range(1, jmax + 2) for L in range(LJ)]
    pois = all(poisson(Th.get(kk, {}), expo(*kk)) == Ps.get(kk, {}) for kk in dkeys)
    keys = [kk for kk in allkeys if expo(*kk) >= thr]
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
    above = [kk for kk in order if expo(*kk) > thr]
    nz = [kk for kk in above if coef[kk]]
    first = nz[0]
    e41 = expo(4, 1)
    # formula (3) of T4-281 for branch ell = 4 (j = 3, a_3 = 2 delta) and formula (4)
    D41 = {}
    for (j, nn), P in R.items():
        if j == 3:
            put(D41, nn, -2 * delta * P(fmpq(1)) - P.derivative()(fmpq(1)))
    low_dens = [kk for kk in [(1, 1), (2, 1), (3, 1)] if Th.get(kk)]
    low_strm = [kk for kk in [(1, 1), (2, 1), (3, 1)] if Ps.get(kk)]
    f4 = scale(D41, c * e41 - 1)
    ok3 = D41 == Th.get((4, 1), {})
    ok4 = coef[(4, 1)] == f4
    er = extrow[name]
    fq = lambda v_: fmpq(*map(int, (v_.split("/") + ["1"])[:2]))
    ext_D = {int(k_): fq(v_) for k_, v_ in er["density_coefficients_exact"].items()}
    ext_F = {int(k_): fq(v_) for k_, v_ in er["residual_coefficients_exact"].items()}
    ext_e = fq(er["exponent_exact"])
    ext_thr = fq(er["exterior_threshold_exact"])
    same_ext = (ext_D == D41) and (ext_F == f4) and ext_e == e41 and ext_thr == thr
    # remark R2: the sector (1, 2) at exponent gamma - 4 against the dipole profile gamma cos(2th) Th0 + sin(2th) Th0'
    Th0 = Th[(1, 0)]
    Pd = add(scale(sin_cos(Th0, {2: fmpq(1)}), gam), sin_cos({2: fmpq(1)}, dsin(Th0)))
    F12 = coef[(1, 2)]
    assert expo(1, 2) == thr and F12 == scale(Th.get((1, 2), {}), -4 * c)
    lam = dot(F12, Pd) / dot(Pd, Pd)
    resid = add(F12, Pd, -lam)
    prop = not resid
    rel = float(np.sqrt(float(dot(resid, resid)) / float(dot(F12, F12)))) if F12 else 0.0
    RES[name] = {"jmax": jmax, "nonresonance_1_16": nonres, "poisson_all_sectors_L_le_2": pois,
                 "zero_above": [kk for kk in above if not coef[kk]],
                 "nonzero_above": [(kk, str(expo(*kk)), float(expo(*kk)), l2(coef[kk])) for kk in nz],
                 "first": first, "e41": str(e41), "gap": str(e41 - thr), "gap_float": float(e41 - thr),
                 "lower_density_L1_nonzero": low_dens, "lower_stream_L1_nonzero": low_strm,
                 "formula3": ok3, "formula4": ok4, "modes_41": len(D41), "agrees_with_c1t4": same_ext,
                 "R2_F12_norm": l2(F12), "R2_dipole_norm": l2(Pd), "R2_proportional": prop, "R2_rel_residual": rel,
                 "R2_lambda_float": float(lam), "seconds": time.monotonic() - t1}
    print("(C) %s (sha256 %s...): branches j <= %d; (i - j) delta/2 not an integer for 1 <= j < i <= 16: %s; stream"
          " sectors = Poisson of density sectors for K <= %d, L <= 2: %s"
          % (name, EXPECT[name][:8], jmax, nonres, jmax + 1, pois))
    print("     residual coefficients above gamma - 4 = %.9f, exactly zero: %s"
          % (float(thr), ", ".join("(%d,%d)" % kk for kk in above if not coef[kk])))
    print("     nonzero: %s" % ", ".join("(%d,%d) %+.9f [L2 norm on the circle %.6g]"
                                         % (kk + (float(expo(*kk)), l2(coef[kk]))) for kk in nz))
    print("     lower first descendants (K, 1), K <= 3: density nonzero %s, stream nonzero %s; first nonzero (%d,%d);"
          " Theta_(4,1) = formula (3): %s (%d modes); coefficient = (c e - 1) Theta_(4,1), formula (4): %s"
          % (low_dens or "none", low_strm or "none", first[0], first[1], ok3, len(D41), ok4))
    print("     e = %.12f, e - (gamma - 4) = %.12f; c1-t4 density and residual coefficients, exponent and threshold"
          " equal mine exactly: %s" % (float(e41), float(e41 - thr), same_ext))
    print("     R2: F_(1,2) = -4c Theta_(1,2), norm %.6g; dipole profile norm %.6g; proportional: %s, relative residual"
          " %.6f after the best multiple (lambda = %.6g); %.1f s"
          % (l2(F12), l2(Pd), prop, rel, float(lam), time.monotonic() - t1))
    assert first == (4, 1) and ok3 and ok4 and same_ext and not low_dens and not low_strm and pois
OUT["C"] = RES
(HERE / "data/t4_281_review_results.json").write_text(json.dumps(OUT, indent=1, default=str))
print("wrote data/t4_281_review_results.json; total %.1f s" % (time.monotonic() - T0))
