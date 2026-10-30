"""Independent check by c1-t1 of c1-t4 T4-060 (review R1-012 in nonlinear_closure/REVIEWS_v08.md), and the c1-t1
extension TP-4 (principal matrix bound for weighted H^q energies).

Target: c1-t4/research/origin_regularity_obstruction/PROOF.md (sha256 1e59a48b...): for a normalized S1 reference
(c + d_y u2(0) = 1), if Re<Lh, h>_(H^q) <= -beta ||h||_(H^q)^2 on smooth compact S1 tests with c[h] = 0 (q > 2),
then beta <= c + 1 - q.

Part A (sympy, exact; my own code written from the statements of the target):
  A1. expansion (4): (1 + |eta + N e2|^2)^(q/2) = N^q + q N^(q-1) eta_2 + N^(q-2) (quadratic in eta) + ...;
  A2. the N^(2q) coefficient of Re<J^q (V.D - 1) e^(iNy) a, J^q e^(iNy) a>: cross terms cancel, leaving
      (V.Da) a - a^2 + q (d_y V_y) a^2 pointwise; (V.Da) a + (div V/2) a^2 = div(V a^2)/2 and div V = 2c;
  A3. general direction omega and weight: the same coefficient is q omega^T (DV) omega a^2 + ... pointwise, and the
      Poisson bracket of m = W(x) |xi|^(2q) with V.xi equals m (2q xi^T DV xi/|xi|^2 - V.D log W); for any symbol even
      in xi_1 and homogeneous of degree 2q, the origin value at xi = e2 with diagonal DV(0) is 2q m d_y V_y;
  A4. symbol of U at e2 + eta/N: vanishes at eta = 0, |U1| <= |xi_1|/|xi|, |U2| <= xi_1^2/|xi|^2;
  A5. c[g] = 1 for g = -4 y eta(r): radial particular solution Psi = -r^3/2 and -d_1^2 d_2 (Psi sin th) = 1;
  A6. the case 4 interval: 9/5 < c < 37/20 (exact c of state131), 2 - c > 3/20, c - 1.
Part B (arb, 320 bits; own evaluator of the exact state131 potential, as in check_T4047.py): origin data rho_y(0),
  Du(0), the normalization residual c + d_y u2(0) - 1, and the origin principal matrix
  M_q(0) = (1 + c) I - q Sym DV(0) + A(0), A = [[rho_y, -rho_x/2], [-rho_x/2, 0]] (= -M0 of T4-047).
Part C (FLOAT, FFT on a periodic box): S1 vertical packets a sin(N y) and horizontal packets a_o cos(N x) on the
  state131 background, H^q energy quotients of the transport and coupling parts against the predicted limits (6).
Part D (FLOAT map, TP-4): inf over a polar grid of lambda_min(M_(q,w)(x)), M_(q,w) = (1 + c + V.D log w) I
  - q Sym DV + A, for q in {0, 2, 2 + 2^-10, 5/2, 3} and weights w = (1 + r^2/R^2)^(p/2) (p = 0 unweighted) and the
  A2 weight omega_2 = (1 + 4 r^2)^(2/5); arb re-evaluation of the minimizing grid points.
Part E (sympy and FLOAT): the A2 energy matrices (B1), (B4), (B5), (B6) and (W2) are exactly M_(q,w) for
  (q, w) = (-1, 1), (1, 1), (2, omega), (3, omega), (1, omega_1); the A2 P95 closed forms in potential derivatives;
  the grid infima of lambda_min on state131 against the A2 floors.

Usage (from artifacts/checks):
  OMP_NUM_THREADS=1 python3 -B check_T4060.py > check_T4060.out
Needs sympy, numpy, python-flint. Input data/state131_exact.json (copy of the A2 P1_source file).
"""
import json
import math
import time
from fractions import Fraction as Fr
from math import comb
from pathlib import Path

import flint
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
flint.ctx.prec = 320
T_START = time.time()

print("=" * 100)
print("Part A. Exact symbolic checks")
print("=" * 100)
q, e, N = sp.symbols("q epsilon N", positive=True)
eta1, eta2 = sp.symbols("eta1 eta2", real=True)
# A1. (1 + |eta + N e2|^2)^(q/2) = N^q (1 + 2 eta2/N + (1 + |eta|^2)/N^2)^(q/2); expand in e = 1/N
base = (1 + 2 * e * eta2 + e ** 2 * (1 + eta1 ** 2 + eta2 ** 2)) ** (q / 2)
ser = sp.series(base, e, 0, 3).removeO()
c0, c1, c2 = [sp.simplify(ser.coeff(e, k)) for k in range(3)]
print("A1. (1 + |eta + N e2|^2)^(q/2) / N^q = 1 + e*(", c1, ") + e^2*(", sp.factor(c2), ") + O(e^3), e = 1/N")
assert c0 == 1 and sp.simplify(c1 - q * eta2) == 0
assert sp.Poly(sp.expand(c2), eta1, eta2).total_degree() == 2
print("    so J^q(e^{iNy} a) = e^{iNy}(N^q a - i q N^(q-1) d_y a) + O(N^(q-2)) (eta2 <-> -i d_y), as in (4)")

# A2. leading real coefficient, vertical packet; real functions V1, V2, a of (x, y)
x, y = sp.symbols("x y", real=True)
V1, V2, a = [sp.Function(nm, real=True)(x, y) for nm in ("V1", "V2", "a")]
t = sp.symbols("t", positive=True)               # t = 1/N
Im_ = sp.symbols("i_")                          # imaginary unit kept as a symbol: all other symbols are real
cj = lambda ex: ex.subs(Im_, -Im_)               # complex conjugate


def re_(ex):
    """real part: reduce modulo i_^2 + 1 and keep the i_-free coefficient"""
    pe = sp.Poly(sp.expand(ex), Im_)
    return sp.expand(sum(cf * (-1) ** (k // 2) for (k,), cf in pe.terms() if k % 2 == 0))


VD = lambda f: V1 * sp.diff(f, x) + V2 * sp.diff(f, y)
b1 = Im_ / t * V2 * a + VD(a) - a               # (V.D - 1)(e^{iNy} a) = e^{iNy} b1
F = b1 - Im_ * q * t * sp.diff(b1, y)          # J^q / N^q, first two orders
G = a - Im_ * q * t * sp.diff(a, y)
prod = sp.expand(F * cj(G))
lead = sp.simplify(re_(prod.coeff(t, 0)))
target = VD(a) * a - a ** 2 + q * sp.diff(V2, y) * a ** 2
print("A2. Re of the N^(2q) coefficient minus [(V.Da) a - a^2 + q (d_y V_y) a^2] =", sp.simplify(lead - target))
assert sp.simplify(lead - target) == 0
print("    the N^(2q+1) coefficient is purely imaginary:", sp.simplify(re_(prod.coeff(t, -1))) == 0)
assert sp.simplify(re_(prod.coeff(t, -1))) == 0
cc = sp.symbols("c", positive=True)
psi = sp.Function("psi", real=True)(x, y)
Vc = (cc * x - sp.diff(psi, y), cc * y + sp.diff(psi, x))      # V = cX + u, u = grad^perp psi, div u = 0
divV = sp.simplify(sp.diff(Vc[0], x) + sp.diff(Vc[1], y))
idn = sp.simplify((Vc[0] * sp.diff(a, x) + Vc[1] * sp.diff(a, y)) * a + divV / 2 * a ** 2
                  - (sp.diff(Vc[0] * a ** 2, x) + sp.diff(Vc[1] * a ** 2, y)) / 2)
print("    div V =", divV, "; (V.Da) a + (div V/2) a^2 - div(V a^2)/2 =", idn, "=> int (V.Da) a = -c int a^2")
assert divV == 2 * cc and idn == 0

# A3. general direction omega (unit) and weight W = w^2: packet e^{iN omega.X} a
w1, w2 = sp.symbols("omega1 omega2", real=True)
Wf = sp.Function("W", positive=True)(x, y)
b1g = Im_ / t * (V1 * w1 + V2 * w2) * a + VD(a) - a
dom = lambda f: w1 * sp.diff(f, x) + w2 * sp.diff(f, y)
Fg = b1g - Im_ * q * t * dom(b1g)
Gg = a - Im_ * q * t * dom(a)
prodg = sp.expand(Fg * cj(Gg))
leadg = sp.simplify(re_(prodg.coeff(t, 0)))
DVq = (w1 * w1 * sp.diff(V1, x) + w1 * w2 * (sp.diff(V2, x) + sp.diff(V1, y)) + w2 * w2 * sp.diff(V2, y))
print("A3. general omega: Re N^(2q) coefficient - [(V.Da) a - a^2 + q (omega^T DV omega) a^2] =",
      sp.simplify(leadg - (VD(a) * a - a ** 2 + q * DVq * a ** 2)))
assert sp.simplify(leadg - (VD(a) * a - a ** 2 + q * DVq * a ** 2)) == 0
# with the weight W = w^2 in the integral: int W (V.Da) a = int W (-c + b) a^2, b = -V.D log w
idw = sp.simplify(Wf * (Vc[0] * sp.diff(a, x) + Vc[1] * sp.diff(a, y)) * a
                  - (-cc * Wf - (Vc[0] * sp.diff(Wf, x) + Vc[1] * sp.diff(Wf, y)) / 2) * a ** 2
                  - (sp.diff(Wf * Vc[0] * a ** 2, x) + sp.diff(Wf * Vc[1] * a ** 2, y)) / 2)
print("    weighted: W (V.Da) a - (-c W - V.DW/2) a^2 - div(W V a^2)/2 =", idw,
      "=> limit ratio -c - 1 + b + q omega^T Sym DV omega (b = -V.D log w)")
assert idw == 0
# Poisson bracket form
k1, k2 = sp.symbols("xi1 xi2", real=True)
m = Wf * (k1 ** 2 + k2 ** 2) ** q
Vxi = V1 * k1 + V2 * k2
pb = (sp.diff(m, k1) * sp.diff(Vxi, x) + sp.diff(m, k2) * sp.diff(Vxi, y)
      - sp.diff(m, x) * sp.diff(Vxi, k1) - sp.diff(m, y) * sp.diff(Vxi, k2))
xDVx = k1 * k1 * sp.diff(V1, x) + k1 * k2 * (sp.diff(V2, x) + sp.diff(V1, y)) + k2 * k2 * sp.diff(V2, y)
pb_t = m * (2 * q * xDVx / (k1 ** 2 + k2 ** 2) - (V1 * sp.diff(Wf, x) + V2 * sp.diff(Wf, y)) / Wf)
print("    Poisson bracket {W |xi|^(2q), V.xi} - m (2q xi^T DV xi/|xi|^2 - V.D log W) =", sp.simplify(pb - pb_t))
assert sp.simplify(pb - pb_t) == 0
mu1, mu2, mu3, d1v, d2v = sp.symbols("mu1 mu2 mu3 d1 d2", positive=True)
mani = mu1 * k1 ** 4 + mu2 * k1 ** 2 * k2 ** 2 + mu3 * k2 ** 4        # anisotropic q = 2 example
br0 = (sp.diff(mani, k1) * d1v * k1 + sp.diff(mani, k2) * d2v * k2).subs({k1: 0, k2: 1})
print("    anisotropic q = 2 symbol mu1 xi1^4 + mu2 xi1^2 xi2^2 + mu3 xi2^4, DV(0) = diag(d1, d2), at xi = e2:"
      " bracket/m =", sp.simplify(br0 / mani.subs({k1: 0, k2: 1})), "(= 2q d_y V_y, weights irrelevant at V(0) = 0)")
assert sp.simplify(br0 / mani.subs({k1: 0, k2: 1}) - 4 * d2v) == 0

# A4. U symbol near the vertical direction
xi1s, xi2s = sp.symbols("xi1 xi2", real=True)
U1s = xi1s * xi2s / (xi1s ** 2 + xi2s ** 2)
U2s = -xi1s ** 2 / (xi1s ** 2 + xi2s ** 2)
print("A4. U symbol at e2:", (U1s.subs({xi1s: 0, xi2s: 1}), U2s.subs({xi1s: 0, xi2s: 1})),
      "; |U1| <= |xi1|/|xi| (since |xi2| <= |xi|), |U2| = xi1^2/|xi|^2; on |eta| <= N/2: |xi| >= N/2, so |U1| <= 2|eta1|/N")
assert sp.simplify(xi1s ** 2 / (xi1s ** 2 + xi2s ** 2) - U1s ** 2 - (xi1s ** 2 / (xi1s ** 2 + xi2s ** 2)) ** 2) == 0

# A5. c[g] for g = -4 y eta(r), eta = 1 near 0: Lap psi = g, U2 = R1^2 = -d_1^2 Lap^-1, c[g] = -d_1^2 d_2 psi(0)
r = sp.symbols("r", positive=True)
Psi = -r ** 3 / 2
ode = sp.simplify(sp.diff(Psi, r, 2) + sp.diff(Psi, r) / r - Psi / r ** 2)
psi_loc = -(x ** 2 + y ** 2) * y / 2            # Psi(r) sin(theta) in Cartesian form
cg = -sp.diff(psi_loc, x, 2, y, 1)
print("A5. g = -4y near 0 (mode sin theta, radial part -4r): Psi = -r^3/2 solves Psi'' + Psi'/r - Psi/r^2 =", ode,
      "; harmonic remainder A r sin(theta) = A y has zero third derivatives; c[g] = -d_1^2 d_2 psi(0) =", cg)
assert sp.simplify(ode + 4 * r) == 0 and cg == 1
print("    consistent with the contact term -h_y(0)/4 of c[h] (R1-008): the sin(3 th) kernel annihilates the sin(th)"
      " mode, and -g_y(0)/4 =", -sp.Rational(-4) / 4)

# A6. exact c of state131
data = json.loads((HERE / "data/state131_exact.json").read_text())
c_fr = Fr(data["exact_parameters"]["cl"])
gam = Fr(data["exact_parameters"]["gamma"])
assert gam == 1 / c_fr
print(f"A6. c = {c_fr} = {float(c_fr):.13f}; 9/5 < c < 37/20: {Fr(9, 5) < c_fr < Fr(37, 20)}; 2 - c = {float(2 - c_fr):.6f}"
      f" > 3/20; c - 1 = {float(c_fr - 1):.6f}; rate caps c + 1 - q: q = 2: {float(c_fr - 1):.6f},"
      f" q = 2 + 2^-10: {float(c_fr - 1 - Fr(1, 1024)):.6f}, q = 5/2: {float(c_fr - Fr(3, 2)):.6f}, q = 3: {float(c_fr - 2):.6f}")
assert Fr(9, 5) < c_fr < Fr(37, 20)

# ------------------------------------------------------------------------------------------------------------------
# Evaluator (copied from check_T4047.py, with the four first derivatives of u added)
pj = {j: (3 + gam - j * (1 - gam)) / 2 for j in range(4)}
Pv = {}
for (j, mm_, k), val in zip(data["canonical_order"], data["canonical_coefficients"]):
    assert k >= mm_ and 0 <= j <= 3 and 0 <= mm_ <= 9
    Pv.setdefault((j, mm_), [Fr(0)] * 40)
    Pv[(j, mm_)][k - mm_] += Fr(val)


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def Qseq(P, beta, nmax=4):
    Qs = [trim(P)]
    for n in range(nmax):
        Q = Qs[-1]
        out = [Fr(0)] * (len(Q) + 1)
        for i, cf in enumerate(Q):
            out[i] += (beta - n) * cf
            if i >= 1:
                out[i - 1] += i * cf
                out[i] -= i * cf
        Qs.append(trim(out))
    return Qs


def to_s(Q):
    ev = [Fr(0)] * len(Q)
    for i, cf in enumerate(Q):
        for l in range(i + 1):
            ev[l] += cf * comb(i, l) * (-1) ** l
    return trim(ev)


GQ = {}
for (j, mm_), P in Pv.items():
    Qs = Qseq(P, pj[j] - mm_)
    GQ[(j, mm_)] = (Qs, [to_s(Q) for Q in Qs])
fq = lambda fr: flint.arb(flint.fmpq(fr.numerator, fr.denominator))
GQa = {key: ([[fq(cf) for cf in Q] for Q in Qs], [[fq(cf) for cf in Q] for Q in Ss]) for key, (Qs, Ss) in GQ.items()}
GQf = {key: ([np.array([float(cf) for cf in Q[::-1]]) for Q in Qs], [np.array([float(cf) for cf in Q[::-1]]) for Q in Ss])
       for key, (Qs, Ss) in GQ.items()}
pja = {j: fq(pj[j]) for j in range(4)}


def Dz(ex):
    out = {}
    for (aa, bb, k), (cr, ci) in ex.items():
        if aa > 0:
            tt = (aa - 1, bb, k); o = out.get(tt, (0, 0)); out[tt] = (o[0] + aa * cr, o[1] + aa * ci)
        tt = (aa, bb + 1, k + 1); o = out.get(tt, (0, 0)); out[tt] = (o[0] + cr, o[1] + ci)
    return out


def Dzb(ex):
    out = {}
    for (aa, bb, k), (cr, ci) in ex.items():
        if bb > 0:
            tt = (aa, bb - 1, k); o = out.get(tt, (0, 0)); out[tt] = (o[0] + bb * cr, o[1] + bb * ci)
        tt = (aa + 1, bb, k + 1); o = out.get(tt, (0, 0)); out[tt] = (o[0] + cr, o[1] + ci)
    return out


def add(ex, f, s=1):
    out = dict(ex)
    for tt, (cr, ci) in f.items():
        o = out.get(tt, (0, 0)); out[tt] = (o[0] + s * cr, o[1] + s * ci)
    return {tt: v for tt, v in out.items() if v != (0, 0)}


def times_i(ex):
    return {tt: (-ci, cr) for tt, (cr, ci) in ex.items()}


def neg(ex):
    return {tt: (-cr, -ci) for tt, (cr, ci) in ex.items()}


Dx = lambda ex: add(Dz(ex), Dzb(ex))
Dy = lambda ex: times_i(add(Dz(ex), Dzb(ex), -1))
Lap = lambda ex: {tt: (4 * cr, 4 * ci) for tt, (cr, ci) in Dz(Dzb(ex)).items()}
OPS = {}
for mm_ in range(10):
    e0 = {(2 * mm_, 0, 0): (1, 0)}
    lap = Lap(e0)
    u1 = neg(Dx(Dy(Dy(e0))))
    u2 = Dx(Dx(Dy(e0)))
    OPS[mm_] = {"rho": neg(Dy(lap)), "rho_x": neg(Dx(Dy(lap))), "rho_y": neg(Dy(Dy(lap))), "u1": u1, "u2": u2,
                "u1_x": Dx(u1), "u1_y": Dy(u1), "u2_x": Dx(u2), "u2_y": Dy(u2)}
    assert max(k for ex in OPS[mm_].values() for (_, _, k) in ex) <= 4
NAMES = tuple(OPS[0].keys())
AMAX = max(aa for ops in OPS.values() for ex in ops.values() for (aa, bb, k) in ex) + 1


def horner(cs, tv):
    acc = cs[-1]
    for cf in reversed(cs[:-1]):
        acc = acc * tv + cf
    return acc


def to_arb(v):
    if isinstance(v, Fr):
        return fq(v)
    if isinstance(v, (float, int)):
        return flint.arb(v)
    return v


def fields_arb(xv, yv):
    """rigorous enclosures of rho, its gradient, u and Du of state131 at the exact point (xv, yv)"""
    xv = to_arb(xv); yv = to_arb(yv)
    qq = xv * xv + yv * yv
    oq = 1 + qq
    s = 1 / oq
    v = qq * s
    use_s = float(v.mid()) > 0.5
    tv = s if use_s else v
    Lq = oq.log()
    Pj = {j: (Lq * pja[j]).exp() for j in range(4)}
    spow = [flint.arb(1)]
    for _ in range(14):
        spow.append(spow[-1] * s)
    z = flint.acb(xv, yv); zb = flint.acb(xv, -yv)
    zp = [flint.acb(1)]; zbp = [flint.acb(1)]
    for _ in range(AMAX):
        zp.append(zp[-1] * z); zbp.append(zbp[-1] * zb)
    out = {nm: flint.arb(0) for nm in NAMES}
    for (j, mm), (Qa, Sa) in GQa.items():
        cs = Sa if use_s else Qa
        gk = [Pj[j] * spow[mm + k] * horner(cs[k], tv) for k in range(5)]
        for nm in NAMES:
            tot = flint.acb(0)
            for (aa, bb, k), (cr, ci) in OPS[mm][nm].items():
                tot += flint.acb(cr, ci) * zp[aa] * zbp[bb] * gk[k]
            out[nm] += tot.real
    return out


def fields_np(xv, yv, names=NAMES):
    """the same formulas in float64 (FLOAT)"""
    xv = np.asarray(xv, float); yv = np.asarray(yv, float)
    z = xv + 1j * yv; qq = xv * xv + yv * yv; s = 1 / (1 + qq); v = qq * s
    use_s = v > 0.5
    lq = np.log1p(qq)
    out = {nm: np.zeros_like(xv) for nm in names}
    zp = [np.ones_like(z)]
    for _ in range(AMAX):
        zp.append(zp[-1] * z)
    zbp = [np.conj(wv) for wv in zp]
    for (j, mm), (Qf, Sf) in GQf.items():
        gk = [np.exp((float(pj[j]) - mm - k) * lq) * np.where(use_s, np.polyval(Sf[k], s), np.polyval(Qf[k], v))
              for k in range(5)]
        for nm in names:
            tot = np.zeros_like(z)
            for (aa, bb, k), (cr, ci) in OPS[mm][nm].items():
                tot += complex(cr, ci) * zp[aa] * zbp[bb] * gk[k]
            out[nm] += tot.real
    return out


c_a = fq(c_fr)
c_f = float(c_fr)

print()
print("=" * 100)
print("Part B. Origin data of state131 (arb, rigorous balls at the exact point 0)")
print("=" * 100)
f0 = fields_arb(Fr(0), Fr(0))


def ball(ex):
    return f"{float(ex.mid()):+.15e} (radius {float(ex.rad()):.1e})"


for nm in NAMES:
    print(f"    {nm:5s}(0) = {ball(f0[nm])}")
norm_res = c_a + f0["u2_y"] - 1
print("B1. normalization residual c + d_y u2(0) - 1 =", ball(norm_res), "; d_x u1(0) - (c - 1) =", ball(f0["u1_x"] - (c_a - 1)),
      "; F_y(0) = rho_y(0) (c + d_y u2(0) - 1) =", ball(f0["rho_y"] * norm_res))
assert abs(float(norm_res.mid())) < 1e-12 and (f0["u1_x"] + f0["u2_y"]).contains(0)
a0 = f0["rho_y"]
qcross = a0 / (2 * c_a - 2)
print(f"B2. a0 = rho_y(0) = {float(a0.mid()):.12f}; DV(0) = diag(2c - 1, 1) to the residual above.")
print("    origin principal matrix M_q(0) = (1 + c) I - q diag(2c - 1, 1) + diag(a0, 0):")
for qv in (Fr(0), Fr(2), Fr(2) + Fr(1, 1024), Fr(5, 2), Fr(3)):
    m11 = 1 + c_a - fq(qv) * (c_a + f0["u1_x"]) + a0
    m22 = 1 + c_a - fq(qv) * (c_a + f0["u2_y"])
    print(f"      q = {str(qv):>9}: M_q(0) = diag({float(m11.mid()):.6f}, {float(m22.mid()):.6f}); vertical entry"
          f" c + 1 - q d_yV_y(0) is the smaller one: {bool(m22 < m11)}")
print(f"    the horizontal entry stays larger while q < a0/(2c - 2) = {float(qcross.mid()):.6f}")
b5 = 3 - 3 * c_f + 10.30
print(f"    (B5) of transfer_checks/transfer_numbers.out prints diag(7.86904, 0.81032) from the rounded input a0 = 10.30:"
      f" 3 - 3c + 10.30 = {b5:.5f}; with the exact a0 the (1,1) entry is {float((3 - 3 * c_a + a0).mid()):.6f}")
assert abs(b5 - 7.86904) < 1e-5

print()
print("=" * 100)
print("Part C. FLOAT packet quotients in H^q on a periodic box (not proofs)")
print("=" * 100)
Lb, n = 1.0, 512
xs = -Lb + (2 * Lb / n) * np.arange(n)
dx = xs[1] - xs[0]
XX, YY = np.meshgrid(xs, xs, indexing="ij")
kk = 2 * np.pi * np.fft.fftfreq(n, dx)
K1, K2 = np.meshgrid(kk, kk, indexing="ij")
KQ = K1 ** 2 + K2 ** 2
KQ0 = KQ.copy(); KQ0[0, 0] = 1.0


def bump(sv):
    return np.where(np.abs(sv) < 1, np.exp(-1 / np.maximum(1e-300, 1 - sv * sv)), 0.0)


def win(sv):
    """smooth window: 1 for |s| <= 0.75, 0 for |s| >= 0.95"""
    tt = np.clip((np.abs(sv) - 0.75) / 0.2, 0, 1)
    f1 = np.where(tt < 1, np.exp(-1 / np.maximum(1e-300, 1 - tt)), 0.0)
    f2 = np.where(tt > 0, np.exp(-1 / np.maximum(1e-300, tt)), 0.0)
    return f1 / (f1 + f2)


cut = win(XX) * win(YY)
gfull = fields_np(XX, YY, names=("rho_x", "rho_y"))
eps, rd = 0.3, 0.2
amp_e = np.zeros_like(XX)
amp_o = np.zeros_like(XX)
for sx in (1, -1):
    for sy in (1, -1):
        bmp = bump(np.hypot(XX - sx * eps, YY - sy * eps) / rd)
        amp_e += bmp
        amp_o += sy * bmp
mask = (amp_e > 0)
fm = fields_np(XX[mask], YY[mask], names=("u1", "u2", "u1_x", "u2_y", "rho_y"))
V1m = c_f * XX[mask] + fm["u1"]
V2m = c_f * YY[mask] + fm["u2"]


def Eq(fh, gh, qv):
    return float(np.sum((1 + KQ) ** qv * np.real(fh * np.conj(gh))))


def quotients(hgrid, qv):
    hh = np.fft.fft2(hgrid)
    hx = np.real(np.fft.ifft2(1j * K1 * hh))
    hy = np.real(np.fft.ifft2(1j * K2 * hh))
    Th = np.zeros_like(hgrid)
    Th[mask] = V1m * hx[mask] + V2m * hy[mask] - hgrid[mask]
    U1 = np.real(np.fft.ifft2((K1 * K2 / KQ0) * hh))
    U2 = np.real(np.fft.ifft2(-(K1 ** 2 / KQ0) * hh))
    Ch = cut * (U1 * gfull["rho_x"] + U2 * gfull["rho_y"])
    den = Eq(hh, hh, qv)
    return Eq(np.fft.fft2(Th), hh, qv) / den, Eq(np.fft.fft2(Ch), hh, qv) / den


a2e = amp_e[mask] ** 2
a2o = amp_o[mask] ** 2
avg_dyVy = np.sum(a2e * (c_f + fm["u2_y"])) / np.sum(a2e)
avg_dxVx = np.sum(a2o * (c_f + fm["u1_x"])) / np.sum(a2o)
avg_rhoy = np.sum(a2o * fm["rho_y"]) / np.sum(a2o)
print(f"    box [-1, 1)^2, {n}^2 points; packets: four disks of radius {rd} centred at (+-{eps}, +-{eps});"
      f" amplitude averages <d_y V_y> = {avg_dyVy:.6f}, <d_x V_x> = {avg_dxVx:.6f}, <rho_y> = {avg_rhoy:.6f}")
worst_v, worst_h = 0.0, 0.0
for qv in (2.0, 2.5, 3.0):
    pred_v = -(c_f + 1) + qv * avg_dyVy
    pred_hT = -(c_f + 1) + qv * avg_dxVx
    pred_hC = -avg_rhoy
    rows = []
    rv, rh = {}, {}
    for Nf in (50, 100, 200, 400):
        tv_, cv_ = quotients(amp_e * np.sin(Nf * YY), qv)
        th_, ch_ = quotients(amp_o * np.cos(Nf * XX), qv)
        rv[Nf] = (tv_, cv_); rh[Nf] = (th_, ch_)
        rows.append(f"N = {Nf:3d}: vert T {tv_:+.5f} C {cv_:+.2e} | horiz T {th_:+.5f} C {ch_:+.5f}")
    ext_v = 2 * rv[400][0] - rv[200][0]
    ext_hT = 2 * rh[400][0] - rh[200][0]
    ext_hC = 2 * rh[400][1] - rh[200][1]
    print(f"C1. q = {qv}:")
    for rw in rows:
        print("      " + rw)
    print(f"      Richardson (2 f(400) - f(200)): vertical transport {ext_v:+.5f} vs (6) {pred_v:+.5f};"
          f" horizontal transport {ext_hT:+.5f} vs {pred_hT:+.5f}; horizontal coupling {ext_hC:+.5f} vs -<rho_y> {pred_hC:+.5f};"
          f" vertical coupling at N = 400: {rv[400][1]:+.2e} (-> 0 like 1/N)")
    worst_v = max(worst_v, abs(ext_v - pred_v))
    worst_h = max(worst_h, abs(ext_hT - pred_hT), abs(ext_hC - pred_hC))
print(f"    max |extrapolated - predicted|: vertical {worst_v:.2e}, horizontal {worst_h:.2e}")
assert worst_v < 2e-2 and worst_h < 5e-2
print(f"    as eps -> 0 the vertical limit tends to q d_yV_y(0) - c - 1 = q - c - 1 (Part B); at eps = {eps}"
      f" <d_y V_y> - 1 = {avg_dyVy - 1:+.4f}")

print()
print("=" * 100)
print("Part D. TP-4 map: inf_x lambda_min(M_(q,w)(x)) on state131 (FLOAT grid; arb at the minimizing points)")
print("=" * 100)
rg = np.concatenate([[0.0], np.logspace(-3, 8, 221)])
tg = np.linspace(0, np.pi / 2, 25)
RG, TG = np.meshgrid(rg, tg, indexing="ij")
XG, YG = RG * np.cos(TG), RG * np.sin(TG)
fg = fields_np(XG, YG)
S11 = c_f + fg["u1_x"]
S22 = c_f + fg["u2_y"]
S12 = (fg["u1_y"] + fg["u2_x"]) / 2
VX = c_f * RG ** 2 + XG * fg["u1"] + YG * fg["u2"]          # V.X


def lam_min_grid(qv, dlogw):
    """lambda_min of (1 + c + V.D log w) I - q S + A, A = [[rho_y, -rho_x/2], [-rho_x/2, 0]]"""
    m11 = 1 + c_f + dlogw - qv * S11 + fg["rho_y"]
    m22 = 1 + c_f + dlogw - qv * S22
    m12 = -qv * S12 - fg["rho_x"] / 2
    return (m11 + m22) / 2 - np.sqrt(((m11 - m22) / 2) ** 2 + m12 ** 2)


def lam_min_arb(qv, xv, yv, wkind, p, R):
    f = fields_arb(xv, yv)
    xa, ya = to_arb(xv), to_arb(yv)
    r2 = xa * xa + ya * ya
    vx = c_a * r2 + xa * f["u1"] + ya * f["u2"]
    if wkind == "power":
        dl = to_arb(p) * vx / (to_arb(R) ** 2 + r2)
    else:                                                    # omega_2 = (1 + 4 r^2)^(2/5)
        dl = fq(Fr(16, 5)) * vx / (1 + 4 * r2)
    qa = to_arb(qv)
    m11 = 1 + c_a + dl - qa * (c_a + f["u1_x"]) + f["rho_y"]
    m22 = 1 + c_a + dl - qa * (c_a + f["u2_y"])
    m12 = -qa * (f["u1_y"] + f["u2_x"]) / 2 - f["rho_x"] / 2
    return (m11 + m22) / 2 - (((m11 - m22) / 2) ** 2 + m12 ** 2).sqrt()


QS = [(0.0, "0"), (2.0, "2"), (2.0 + 2.0 ** -10, "2+2^-10"), (2.5, "5/2"), (3.0, "3")]
WEIGHTS = [("power", 0.0, 1.0, "unweighted")]
for p in (0.5, 0.8, 1.0, 1.5):
    for R in (1.0, 16.0):
        WEIGHTS.append(("power", p, R, f"(1 + r^2/R^2)^(p/2), p = {p}, R = {R:g}"))
WEIGHTS.append(("omega2", None, None, "A2 omega_2 = (1 + 4 r^2)^(2/5)"))
print("    rate cap beta <= inf_x lambda_min(M_(q,w)) (TP-4); far-field limit (1 + c) + p c - q c for power weights;"
      " origin value c + 1 - q (T4-060) for q <= 6.356")
print(f"    {'weight':42s} | " + " | ".join(f"q = {lab:>8s}" for _, lab in QS))
certs = []
for wkind, p, R, lab in WEIGHTS:
    if wkind == "power":
        dlw = p * VX / (R ** 2 + RG ** 2)
    else:
        dlw = 3.2 * VX / (1 + 4 * RG ** 2)
    cells = []
    for qv, qlab in QS:
        lm = lam_min_grid(qv, dlw)
        i, jx = np.unravel_index(np.argmin(lm), lm.shape)
        cells.append(f"{lm[i, jx]:+.4f} @ r={rg[i]:.2g}")
        certs.append((wkind, p, R, lab, qv, qlab, float(XG[i, jx]), float(YG[i, jx]), float(lm[i, jx]), float(rg[i])))
    print(f"    {lab:42s} | " + " | ".join(f"{cl:>19s}" for cl in cells))
print("D2. arb re-evaluation of every minimizing grid point (an upper bound on any admissible rate, rigorous given TP-4):")
nfail = 0
for wkind, p, R, lab, qv, qlab, xv, yv, lmf, rv in certs:
    if rv > 1e6:
        continue
    lb = lam_min_arb(Fr(qv) if qv != 2.0 + 2.0 ** -10 else Fr(2) + Fr(1, 1024), xv, yv, wkind,
                     Fr(p) if p is not None else None, Fr(R) if R is not None else None)
    ok = abs(float(lb.mid()) - lmf) < 1e-8
    nfail += (not ok)
    if qlab in ("2", "2+2^-10") or rv == 0.0:
        print(f"    {lab:42s} q = {qlab:>8s}: point ({xv:.6g}, {yv:.6g}) lambda_min = {ball(lb)}  float agrees: {ok}")
print("    float/arb disagreements:", nfail)
assert nfail == 0
print("D3. far field (TP-3(a) lemma: Du, D rho -> 0): lambda_min(M_(q,w)) -> 1 + c + p c - q c for power weights:")
for p in (0.0, 0.5, 0.8, 1.0, 1.5):
    print(f"    p = {p}: " + ", ".join(f"q = {lab}: {1 + c_f + p * c_f - qv * c_f:+.4f}" for qv, lab in QS))
print(f"    a positive far-field cap for q = 2 + s needs p > q - 1 - gamma = 1 + s - gamma ({1 - 1 / c_f:.6f} + s);"
      f" A2's omega_2 has p = 4/5 (limit {1 + c_f + 0.8 * c_f - 2 * c_f:.6f} at q = 2)")

print()
print("=" * 100)
print("Part E. The A2 energy matrices are the TP-4 packet matrices M_(q,w)")
print("=" * 100)
# E1 (sympy): generic potential chi with A2's conventions rho = -d_y Lap chi, u = (-chi_12, chi_21) (the evaluator above)
chi = sp.Function("chi", real=True)(x, y)
cd = lambda i, j: sp.diff(chi, x, i, y, j) if i + j > 0 else chi
u1s, u2s = -cd(1, 2), cd(2, 1)
rhos = -sp.diff(cd(2, 0) + cd(0, 2), y)
cl = sp.symbols("c_l", positive=True)
V1s, V2s = cl * x + u1s, cl * y + u2s
r2s = x ** 2 + y ** 2
SDV = sp.Matrix([[sp.diff(V1s, x), (sp.diff(V1s, y) + sp.diff(V2s, x)) / 2],
                 [(sp.diff(V1s, y) + sp.diff(V2s, x)) / 2, sp.diff(V2s, y)]])
SDU = SDV - cl * sp.eye(2)
Asym = sp.Matrix([[sp.diff(rhos, y), -sp.diff(rhos, x) / 2], [-sp.diff(rhos, x) / 2, 0]])
VDlog = lambda lw: V1s * sp.diff(lw, x) + V2s * sp.diff(lw, y)
Mqw = lambda qv, lw: (1 + cl + VDlog(lw)) * sp.eye(2) - qv * SDV + Asym
tt_ = r2s / (1 + r2s)
ee_ = (u1s * x + u2s * y) / r2s
lw1 = -sp.Rational(1, 10) * sp.log(1 + r2s)          # omega_1 = <r>^(-1/5)
lw2 = sp.Rational(2, 5) * sp.log(1 + 4 * r2s)         # omega_2 = omega = (1 + 4 r^2)^(2/5)
checks = [
    ("(B1) M = (2c + 1) I + sym DU + A", Mqw(-1, 0), (2 * cl + 1) * sp.eye(2) + SDU + Asym),
    ("(B4) M_1 = I - sym DU + A", Mqw(1, 0), sp.eye(2) - SDU + Asym),
    ("(B5) M_2 = (1 + c + V.D log omega) I - 2 sym DV + A", Mqw(2, lw2), (1 + cl + VDlog(lw2)) * sp.eye(2) - 2 * SDV + Asym),
    ("(B6) M_3 = (1 + c + V.D log omega) I - 3 sym DV + A", Mqw(3, lw2), (1 + cl + VDlog(lw2)) * sp.eye(2) - 3 * SDV + Asym),
    ("P95 M = (2c + 1) I + [[-2 chi22 - chi04, chi31], [chi31, chi22]]", Mqw(-1, 0),
     (2 * cl + 1) * sp.eye(2) + sp.Matrix([[-2 * cd(2, 2) - cd(0, 4), cd(3, 1)], [cd(3, 1), cd(2, 2)]])),
    ("P95 M_1 = [1 - t(c + e)/5] I + [[-chi04, chi13], [chi13, -chi22]] (W2, k = 1)", Mqw(1, lw1),
     (1 - tt_ * (cl + ee_) / 5) * sp.eye(2) + sp.Matrix([[-cd(0, 4), cd(1, 3)], [cd(1, 3), -cd(2, 2)]])),
    ("P95 M_2 = [1 - c + (16/5) t(c + e)/(1 + 3t)] I + [[chi22 - chi04, (3 chi13 - chi31)/2], [., -2 chi22]]", Mqw(2, lw2),
     (1 - cl + sp.Rational(16, 5) * tt_ * (cl + ee_) / (1 + 3 * tt_)) * sp.eye(2)
     + sp.Matrix([[cd(2, 2) - cd(0, 4), (3 * cd(1, 3) - cd(3, 1)) / 2], [(3 * cd(1, 3) - cd(3, 1)) / 2, -2 * cd(2, 2)]])),
]
print("E1. sympy, generic potential: M_(q,w) - (A2 matrix) = 0 for")
for lab, Mt, Ma in checks:
    dif = sp.simplify(Mt - Ma)
    ok = dif == sp.zeros(2, 2)
    print(f"    {lab}: {ok}")
    assert ok
print("    i.e. (B1) is q = -1 unweighted (the Hdot^-1 low energy), (B4) q = 1 unweighted, (W2) k = 1 is q = 1 with omega_1,"
      " (B5) = (W2) k = 2 is q = 2 with omega, (B6) is q = 3 with omega")
print("    origin values lambda_min = c + 1 - q (for q <= 6.356): c + 2, c, c, c - 1, c - 2 =",
      ", ".join(f"{v:.6f}" for v in (c_f + 2, c_f, c_f, c_f - 1, c_f - 2)), "(A2 P95: c + 2, c and c - 1 at the center)")
# E2 (FLOAT grid, arb at the minimizers): inf of lambda_min on state131 against the A2 floors
A2MAT = [("(B1) M, q = -1", -1.0, 0.0, None, Fr(19, 5)),
         ("(B4) M_1, q = 1", 1.0, 0.0, None, Fr(9, 10)),
         ("(W2) M_1, q = 1, omega_1", 1.0, -0.2, 1.0, Fr(1, 2)),
         ("(B5) M_2, q = 2, omega", 2.0, None, None, Fr(1, 2)),
         ("(B6) M_3, q = 3, omega", 3.0, None, None, Fr(-5, 4))]
print("E2. state131, inf over the Part D grid of lambda_min (FLOAT), arb value at the minimizing grid point, A2 floor:")
for lab, qv, p, R, floor in A2MAT:
    if p is None:
        dlw = 3.2 * VX / (1 + 4 * RG ** 2); wk, pa, Ra = "omega2", None, None
    else:
        dlw = p * VX / ((R if R else 1.0) ** 2 + RG ** 2); wk, pa, Ra = "power", Fr(p), Fr(R if R else 1)
    lm = lam_min_grid(qv, dlw)
    i, jx = np.unravel_index(np.argmin(lm), lm.shape)
    lb = lam_min_arb(Fr(qv), float(XG[i, jx]), float(YG[i, jx]), wk, pa, Ra)
    assert abs(float(lb.mid()) - lm[i, jx]) < 1e-8
    print(f"    {lab:28s}: inf {lm[i, jx]:+.6f} at r = {rg[i]:.3g}, theta = {tg[jx]:.3f}; arb {ball(lb)};"
          f" origin {lm[0, 0]:+.6f}; A2 floor {float(floor):+.4f}; packet cap minus floor {lm[i, jx] - float(floor):+.6f}")
print("    A2's certified (B5) cover gives lambda_min(M_2) >= 293619/500000 = 0.587238 on the whole plane (P96); the grid"
      " infimum above is consistent with it. P99's M_2 >= 0.620899 I holds only for r >= 10^4 and does not cover r = 355")
print(f"total time {time.time() - T_START:.1f} s")
