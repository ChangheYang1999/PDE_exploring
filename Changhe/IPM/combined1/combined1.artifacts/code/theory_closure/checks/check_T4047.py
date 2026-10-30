"""Independent check by c1-t1 of c1-t4 T4-047 (review R1-011 in nonlinear_closure/REVIEWS_v07.md).

Target: c1-t4/research/principal_energy_obstruction/PROOF.md (sha256 e603f562...): if
Re<(L_w + C) phi, phi> <= -beta ||phi||^2 on the compact smooth S1 core, with C compact, then
beta <= c + 1 - Lambda, Lambda = ess sup lambda, lambda = b + (|D rho| - rho_y)/2, b = -V.D log w.

Part A (sympy, exact; my own code written from the statements of the target):
  A1. principal symbol of h -> U[h].D rho in the unit direction xi is xi^T M0 xi, M0 = [[-rho_y, rho_x/2], [rho_x/2, 0]];
  A2. largest eigenvalue of M = b I + M0 is lambda; A3. reflection covariance M(SX) = S M(X) S under S1 parities;
  A4. contact kernel: d_1^2 d_2 (log r/(2 pi)) = sin(3 theta)/(pi r^3), so c[h] = (1/pi) int sin(3 theta) h r^-3 for h
      supported away from 0; A5. b = a V.X/(R^2 + r^2) for w_R.
Part B (FLOAT, FFT on a periodic box; not proofs):
  B1. contact formula against the FFT value of d_y U2[h](0); B2. the packet limit (4); B3. the packet quotient
      Re<L_w phi_n, phi_n>/||phi_n||^2 for S1-reflected packets on the state131 background, against the predicted limit
      -(c+1) + <xi^T M xi>_(chi^2), for a = 0 and a = 6/5.
Part C (my own field evaluator for the exact state131 potential, python-flint arb balls, 320 bits; rigorous point values):
  C1. validation against the A2 stored point enclosures (data/state131_field_points.json, copied from
      r6/source/analysis2/.../P1_source); C2. reproduction of the seven T4-047 weighted points (data/T4047_points.json,
      copied from c1-t4/research/principal_energy_obstruction/verification/points.json).
Part D (state131 obstruction map in (a, R)): arb fields on a polar grid (r up to 1e8); for each a in
  {0, 1, 11/10, 6/5, 13/10, 7/5, 3/2, 31/20, 8/5} and R = 2^e, e = -4..12, the sampled max of lambda - (c+1). Every
  positive sampled entry is re-evaluated in arb at its exact grid point (D2): a positive ball is a certified
  obstruction (Lambda > c + 1). Nonpositive entries are FLOAT (a sampled sup is not an upper bound for Lambda).

Evaluator: chi = sum_{j,m} Re(z^(2m) G_jm(q)), q = |z|^2, G_jm(q) = sum_k coeff q^(k-m) (1+q)^(p_j - k),
p_j = (3 + gamma - j(1 - gamma))/2, gamma = 1/c; rho = -d_y Lap chi, u = (-chi_xyy, chi_xxy). Derivatives by exact
Wirtinger monomial algebra (d_z q = zbar) and the exact recursion for G^(n) described at the evaluator.

Usage (from artifacts/checks):
  OMP_NUM_THREADS=1 python3 -B check_T4047.py > check_T4047.out
Needs sympy, numpy, python-flint.
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
x1, x2, rx, ry, bb = sp.symbols("xi1 xi2 rho_x rho_y b", real=True)
q2 = x1 ** 2 + x2 ** 2
symU = sp.Matrix([-(sp.I * x1) * (sp.I * x2) / q2, (sp.I * x1) ** 2 / q2])      # U = (-R1 R2, R1^2), R_j <-> i xi_j/|xi|
prin = sp.simplify((symU[0] * rx + symU[1] * ry).subs(q2, 1))
M0 = sp.Matrix([[-ry, rx / 2], [rx / 2, 0]])
quad = sp.expand((sp.Matrix([[x1, x2]]) * M0 * sp.Matrix([x1, x2]))[0])
print("A1. symbol of U: (xi1 xi2, -xi1^2)/|xi|^2 =", list(symU), "; principal symbol of U[.].D rho on |xi| = 1:", sp.expand(prin),
      "; xi^T M0 xi =", quad, "; equal:", sp.simplify(sp.expand(prin) - quad.subs(x2 ** 2, 1 - x1 ** 2)) == 0
      or sp.simplify(sp.expand(prin) - quad) == 0)
assert sp.simplify(sp.expand(sp.simplify(symU[0] * rx + symU[1] * ry) * q2) - quad) == 0
M = bb * sp.eye(2) + M0
ev = list(M.eigenvals().keys())
lam = bb + (sp.sqrt(rx ** 2 + ry ** 2) - ry) / 2
print("A2. eigenvalues of M = b I + M0:", ev, "; largest equals b + (|D rho| - rho_y)/2:",
      any(sp.simplify(e - lam) == 0 for e in ev))
assert any(sp.simplify(e - lam) == 0 for e in ev)
# A3. S1 parities: rho even in x, odd in y => rho_x odd in x, odd in y; rho_y even, even; V.X even, even (w radial) => b even
Sx, Sy = sp.diag(-1, 1), sp.diag(1, -1)
Mx = sp.Matrix([[bb - ry, -rx / 2], [-rx / 2, bb]])      # M at (-x, y): rho_x -> -rho_x, rho_y, b unchanged
My = sp.Matrix([[bb - ry, -rx / 2], [-rx / 2, bb]])      # M at (x, -y): rho_x -> -rho_x, rho_y, b unchanged
print("A3. M(S_x X) - S_x M S_x =", list(sp.simplify(Mx - Sx * M * Sx)), "; M(S_y X) - S_y M S_y =",
      list(sp.simplify(My - Sy * M * Sy)))
assert sp.simplify(Mx - Sx * M * Sx) == sp.zeros(2) and sp.simplify(My - Sy * M * Sy) == sp.zeros(2)
X, Yv = sp.symbols("x y", real=True)
rr, th = sp.symbols("r theta", positive=True)
G = sp.log(X ** 2 + Yv ** 2) / (4 * sp.pi)
k3 = sp.diff(G, X, 2, Yv, 1)
k3p = sp.simplify(k3.subs({X: rr * sp.cos(th), Yv: rr * sp.sin(th)}))
print("A4. d_1^2 d_2 (log r/(2 pi)) - sin(3 theta)/(pi r^3) =", sp.simplify(sp.expand_trig(k3p - sp.sin(3 * th) / (sp.pi * rr ** 3))),
      "; kernel odd under X -> -X, and U2 = R1^2 = -d_1^2 Lap^-1, so d_y U2[h](0) = (1/pi) int sin(3 theta) h r^-3 dX")
assert sp.simplify(sp.expand_trig(k3p - sp.sin(3 * th) / (sp.pi * rr ** 3))) == 0
aS, RS = sp.symbols("a R", positive=True)
V1, V2 = sp.symbols("V1 V2", real=True)
lw = -aS / 2 * sp.log(1 + (X ** 2 + Yv ** 2) / RS ** 2)
bexpr = -(V1 * sp.diff(lw, X) + V2 * sp.diff(lw, Yv))
print("A5. b = -V.D log w_R - a (V.X)/(R^2 + r^2) =", sp.simplify(bexpr - aS * (V1 * X + V2 * Yv) / (RS ** 2 + X ** 2 + Yv ** 2)))
assert sp.simplify(bexpr - aS * (V1 * X + V2 * Yv) / (RS ** 2 + X ** 2 + Yv ** 2)) == 0

# ------------------------------------------------------------------------------------------------------------------
# Evaluator (own code). G_jm(q) = sum_k coeff q^(k-m) (1+q)^(p_j-k) = (1+q)^(p_j-m) P_jm(v), P_jm(v) = sum_k coeff v^(k-m).
# Derivatives: G^(n)(q) = (1+q)^(p_j-m-n) Q_n(v) with Q_0 = P and Q_(n+1) = (p_j-m-n) Q_n + (1-v) Q_n' (exact rationals),
# since dv/dq = (1+q)^-2. Q_n is evaluated by Horner in v for v <= 1/2 and in s = 1 - v = 1/(1+q) otherwise
# (exact re-expansion), in arb ball arithmetic (python-flint, 320 bits): every field value is a rigorous enclosure
# at the exact binary-rational input point.
data = json.loads((HERE / "data/state131_exact.json").read_text())
c_fr = Fr(data["exact_parameters"]["cl"])
gam = Fr(data["exact_parameters"]["gamma"])
assert gam == 1 / c_fr
pj = {j: (3 + gam - j * (1 - gam)) / 2 for j in range(4)}
Pv = {}
for (j, m, k), val in zip(data["canonical_order"], data["canonical_coefficients"]):
    assert k >= m and 0 <= j <= 3 and 0 <= m <= 9
    Pv.setdefault((j, m), [Fr(0)] * 40)
    Pv[(j, m)][k - m] += Fr(val)


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
    e = [Fr(0)] * len(Q)
    for i, cf in enumerate(Q):
        for l in range(i + 1):
            e[l] += cf * comb(i, l) * (-1) ** l
    return trim(e)


GQ = {}
for (j, m), P in Pv.items():
    Qs = Qseq(P, pj[j] - m)
    GQ[(j, m)] = (Qs, [to_s(Q) for Q in Qs])
fq = lambda fr: flint.arb(flint.fmpq(fr.numerator, fr.denominator))
GQa = {key: ([[fq(cf) for cf in Q] for Q in Qs], [[fq(cf) for cf in Q] for Q in Ss]) for key, (Qs, Ss) in GQ.items()}
GQf = {key: ([np.array([float(cf) for cf in Q[::-1]]) for Q in Qs], [np.array([float(cf) for cf in Q[::-1]]) for Q in Ss])
       for key, (Qs, Ss) in GQ.items()}
pja = {j: fq(pj[j]) for j in range(4)}
cond_v = max(sum(abs(float(cf)) * 0.5 ** i for i, cf in enumerate(Q)) for Qs, _ in GQ.values() for Q in Qs)
cond_s = max(sum(abs(float(cf)) * 0.5 ** i for i, cf in enumerate(Q)) for _, Ss in GQ.values() for Q in Ss)


def Dz(e):
    out = {}
    for (a, b, k), (cr, ci) in e.items():
        if a > 0:
            t = (a - 1, b, k); o = out.get(t, (0, 0)); out[t] = (o[0] + a * cr, o[1] + a * ci)
        t = (a, b + 1, k + 1); o = out.get(t, (0, 0)); out[t] = (o[0] + cr, o[1] + ci)
    return out


def Dzb(e):
    out = {}
    for (a, b, k), (cr, ci) in e.items():
        if b > 0:
            t = (a, b - 1, k); o = out.get(t, (0, 0)); out[t] = (o[0] + b * cr, o[1] + b * ci)
        t = (a + 1, b, k + 1); o = out.get(t, (0, 0)); out[t] = (o[0] + cr, o[1] + ci)
    return out


def add(e, f, s=1):
    out = dict(e)
    for t, (cr, ci) in f.items():
        o = out.get(t, (0, 0)); out[t] = (o[0] + s * cr, o[1] + s * ci)
    return {t: v for t, v in out.items() if v != (0, 0)}


def times_i(e):
    return {t: (-ci, cr) for t, (cr, ci) in e.items()}


def neg(e):
    return {t: (-cr, -ci) for t, (cr, ci) in e.items()}


# monomials z^a zbar^b G^(k)(q): d_z q = zbar, d_zbar q = z; d_x = d_z + d_zbar, d_y = i (d_z - d_zbar), Lap = 4 d_z d_zbar
Dx = lambda e: add(Dz(e), Dzb(e))
Dy = lambda e: times_i(add(Dz(e), Dzb(e), -1))
Lap = lambda e: {t: (4 * cr, 4 * ci) for t, (cr, ci) in Dz(Dzb(e)).items()}
OPS = {}
for mm in range(10):
    e0 = {(2 * mm, 0, 0): (1, 0)}
    lap = Lap(e0)
    OPS[mm] = {"rho": neg(Dy(lap)), "rho_x": neg(Dx(Dy(lap))), "rho_y": neg(Dy(Dy(lap))),
               "u1": neg(Dx(Dy(Dy(e0)))), "u2": Dx(Dx(Dy(e0)))}
NAMES = ("rho", "rho_x", "rho_y", "u1", "u2")
AMAX = max(a for ops in OPS.values() for e in ops.values() for (a, b, k) in e) + 1


def horner(cs, t):
    acc = cs[-1]
    for cf in reversed(cs[:-1]):
        acc = acc * t + cf
    return acc


def to_arb(x):
    if isinstance(x, Fr):
        return fq(x)
    if isinstance(x, float):
        return flint.arb(x)          # exact: a double is a binary rational
    return x


def fields_arb(x, y):
    """rigorous enclosures of rho, rho_x, rho_y, u1, u2 of state131 at the exact point (x, y)"""
    x = to_arb(x); y = to_arb(y)
    q = x * x + y * y
    oq = 1 + q
    s = 1 / oq
    v = q * s
    use_s = float(v.mid()) > 0.5
    t = s if use_s else v
    Lq = oq.log()
    Pj = {j: (Lq * pja[j]).exp() for j in range(4)}
    spow = [flint.arb(1)]
    for _ in range(14):
        spow.append(spow[-1] * s)
    z = flint.acb(x, y); zb = flint.acb(x, -y)
    zp = [flint.acb(1)]; zbp = [flint.acb(1)]
    for _ in range(AMAX):
        zp.append(zp[-1] * z); zbp.append(zbp[-1] * zb)
    out = {nm: flint.arb(0) for nm in NAMES}
    for (j, m), (Qa, Sa) in GQa.items():
        cs = Sa if use_s else Qa
        gk = [Pj[j] * spow[m + k] * horner(cs[k], t) for k in range(5)]
        for nm in NAMES:
            tot = flint.acb(0)
            for (a, b, k), (cr, ci) in OPS[m][nm].items():
                tot += flint.acb(cr, ci) * zp[a] * zbp[b] * gk[k]
            out[nm] += tot.real
    return out


def fields_np(x, y):
    """the same formulas in float64 (FLOAT; accuracy is reported against fields_arb)"""
    x = np.asarray(x, float); y = np.asarray(y, float)
    z = x + 1j * y; zb = np.conj(z); q = x * x + y * y; s = 1 / (1 + q); v = q * s
    use_s = v > 0.5
    lq = np.log1p(q)
    out = {nm: np.zeros_like(x) for nm in NAMES}
    zp = [np.ones_like(z)]
    for _ in range(AMAX):
        zp.append(zp[-1] * z)
    zbp = [np.conj(w) for w in zp]
    for (j, m), (Qf, Sf) in GQf.items():
        gk = [np.exp((float(pj[j]) - m - k) * lq) * np.where(use_s, np.polyval(Sf[k], s), np.polyval(Qf[k], v))
              for k in range(5)]
        for nm in NAMES:
            tot = np.zeros_like(z)
            for (a, b, k), (cr, ci) in OPS[m][nm].items():
                tot += complex(cr, ci) * zp[a] * zbp[b] * gk[k]
            out[nm] += tot.real
    return out


def lam_arb(f, x, y, a, R):
    """lambda = b + (|D rho| - rho_y)/2 with b = a (V.X)/(R^2 + r^2), V = cX + u, all in arb"""
    x = to_arb(x); y = to_arb(y); a = to_arb(a); R = to_arb(R)
    r2 = x * x + y * y
    bval = a * (c_a * r2 + x * f["u1"] + y * f["u2"]) / (R * R + r2)
    gr2 = f["rho_x"] ** 2 + f["rho_y"] ** 2
    return bval + (gr2.sqrt() - f["rho_y"]) / 2


def amax_abs(e):
    return float(abs(e).upper())


def ball(e):
    return f"{float(e.mid()):+.15e} (radius {float(e.rad()):.1e})"


c_a = fq(c_fr)
c_f = float(c_fr)

print()
print("=" * 100)
print("Part C. Own evaluator for the exact state131 potential (python-flint arb, 320 bits; rigorous point enclosures)")
print("=" * 100)
print(f"    bases: Horner in v for v <= 1/2, in s = 1/(1+q) for v > 1/2; float condition numbers sum |coef| 2^-i:"
      f" v basis {cond_v:.2e}, s basis {cond_s:.2e}")
ref = json.loads((HERE / "data/state131_field_points.json").read_text())
worst = {nm: 0.0 for nm in NAMES}
worst_rad = 0.0
overlap = True
worst_res = 0.0
for rec in ref["points"]:
    xq, yq = Fr(rec["x"]), Fr(rec["y"])
    f = fields_arb(xq, yq)
    for nm in NAMES:
        refv = flint.arb(rec["fields"][nm])
        d = f[nm] - refv
        overlap &= d.contains(0)
        worst[nm] = max(worst[nm], amax_abs(d) / max(1.0, abs(float(refv.mid()))))
        worst_rad = max(worst_rad, float(f[nm].rad()) / max(1.0, abs(float(f[nm].mid()))))
    res = (c_a * fq(xq) + f["u1"]) * f["rho_x"] + (c_a * fq(yq) + f["u2"]) * f["rho_y"] - f["rho"]
    d = res - flint.arb(rec["fields"]["residual"])
    overlap &= d.contains(0)
    worst_res = max(worst_res, amax_abs(d))
print("C1. the 8 A2 stored point enclosures (data/state131_field_points.json): every own ball overlaps the A2 ball:", overlap)
print("    max relative |own - A2| per field:", ", ".join(f"{nm} {worst[nm]:.1e}" for nm in NAMES),
      f"; own relative ball radius <= {worst_rad:.1e}; profile residual (cX + u).D rho - rho: |own - A2| <= {worst_res:.1e}")
assert overlap and max(worst.values()) < 1e-55 and worst_res < 1e-55
t47 = json.loads((HERE / "data/T4047_points.json").read_text())
print("C2. the seven T4-047 weighted points (on the x axis, where rho_x = 0); lambda - (c+1) as rigorous balls:")
print("        a |     R |     x | rho_y (own, mid)   | lambda - (c+1) own                          | overlaps T4-047 ball | > 0")
c2_ok = True
for row in t47["rows"]:
    a = Fr(row["a"]); R = Fr(row["R"]); xv = Fr(row["point"][0]); yv = Fr(row["point"][1])
    f = fields_arb(xv, yv)
    exc = lam_arb(f, xv, yv, a, R) - (c_a + 1)
    their = flint.arb(row["excess_over_c_plus_one"])
    ok = (exc - their).contains(0) and exc > 0
    c2_ok &= ok
    print(f"    {str(a):>5} | {str(R):>5} | {str(xv):>5} | {float(f['rho_y'].mid()):18.12f} | {ball(exc):>43} |"
          f" {str((exc - their).contains(0)):>20} | {exc > 0}")
assert c2_ok

print()
print("=" * 100)
print("Part B. FLOAT checks on a periodic box (not proofs)")
print("=" * 100)
Lb, N = 12.0, 1024
xs = -Lb + (2 * Lb / N) * np.arange(N)
dx = xs[1] - xs[0]
XX, YY = np.meshgrid(xs, xs, indexing="ij")
kk = 2 * np.pi * np.fft.fftfreq(N, dx)
K1, K2 = np.meshgrid(kk, kk, indexing="ij")
KQ = K1 ** 2 + K2 ** 2
KQ[0, 0] = 1.0
RR = np.hypot(XX, YY)
TH = np.arctan2(YY, XX)


def bump(s):
    return np.where(np.abs(s) < 1, np.exp(-1 / np.maximum(1e-300, 1 - s * s)), 0.0)


# B1. contact formula, h = g(r) sin(3 theta) with g supported in 1 < r < 3
gr = bump(RR - 2.0)
hS = gr * np.sin(3 * TH)
hh = np.fft.fft2(hS)
dyU2 = np.real(np.fft.ifft2(1j * K2 * (-(K1 ** 2) / KQ) * hh))
i0 = N // 2
fft_val = dyU2[i0, i0]
formula = np.sum(np.where(RR > 0.5, np.sin(3 * TH) * hS / np.maximum(RR, 1e-9) ** 3, 0.0)) * dx * dx / np.pi
print(f"B1. contact term c[h] = d_y U2[h](0): FFT {fft_val:.8f}; (1/pi) int sin(3 theta) h r^-3 = {formula:.8f};"
      f" relative difference {abs(fft_val - formula) / abs(formula):.2e} (periodic images and quadrature)")
assert abs(fft_val - formula) / abs(formula) < 1e-3

# B2/B3 packets on the state131 background (float64 fields, accuracy reported in D0)


def packet_terms(x0, y0, rad, xi, nfreq, a, R):
    """S1-reflected packet phi; returns quotient Re<L_w phi, phi>/||phi||^2, predicted limit, and the (4) error"""
    imgs = [(1, 1, 1.0), (-1, 1, 1.0), (1, -1, -1.0), (-1, -1, -1.0)]
    phi = np.zeros_like(XX)
    chi2 = []
    for sx, sy, sg in imgs:
        cx, cy = sx * x0, sy * y0
        ch = bump(np.hypot(XX - cx, YY - cy) / rad)
        phase = nfreq * (sx * xi[0] * (XX - cx) + sy * xi[1] * (YY - cy))
        phi += sg * ch * np.cos(phase)
        chi2.append((ch ** 2, (sx * xi[0], sy * xi[1])))
    mask = np.abs(phi) > 0
    mask = np.zeros_like(XX, bool)
    for ch2, _ in chi2:
        mask |= ch2 > 0
    f = fields_np(XX[mask], YY[mask])
    wv = (1 + RR ** 2 / R ** 2) ** (-a / 2)
    h = phi / wv
    hh = np.fft.fft2(h)
    hx = np.real(np.fft.ifft2(1j * K1 * hh))[mask]
    hy = np.real(np.fft.ifft2(1j * K2 * hh))[mask]
    U1 = np.real(np.fft.ifft2((K1 * K2 / KQ) * hh))[mask]
    U2 = np.real(np.fft.ifft2(-(K1 ** 2 / KQ) * hh))[mask]
    Xm, Ym = XX[mask], YY[mask]
    V1 = c_f * Xm + f["u1"]
    V2 = c_f * Ym + f["u2"]
    Lh = V1 * hx + V2 * hy - h[mask] + U1 * f["rho_x"] + U2 * f["rho_y"]
    quot = np.sum(wv[mask] * Lh * phi[mask]) / np.sum(phi[mask] ** 2)
    bv = a * (V1 * Xm + V2 * Ym) / (R ** 2 + Xm ** 2 + Ym ** 2)
    pred_num, pred_den = 0.0, 0.0
    for ch2, (e1, e2) in chi2:
        c2 = ch2[mask]
        qf = (bv - f["rho_y"]) * e1 * e1 + f["rho_x"] * e1 * e2 + bv * e2 * e2
        pred_num += np.sum(c2 * qf); pred_den += np.sum(c2)
    pred = -(c_f + 1) + pred_num / pred_den
    # (4) for the first image: R_j f_n + xi_j chi sin(n xi.X) -> 0
    ch = bump(np.hypot(XX - x0, YY - y0) / rad)
    ph = nfreq * (xi[0] * (XX - x0) + xi[1] * (YY - y0))
    fn = ch * np.cos(ph)
    fh = np.fft.fft2(fn)
    err = 0.0
    for jj, Kj in ((0, K1), (1, K2)):
        Rf = np.real(np.fft.ifft2(1j * Kj / np.sqrt(KQ) * fh))
        err += np.sum((Rf + xi[jj] * ch * np.sin(ph)) ** 2)
    err = math.sqrt(err / np.sum(fn ** 2))
    return quot, pred, err


x0, y0, rad = 1.0, 0.8, 0.35
f0a = fields_arb(x0, y0)
f0 = {nm: float(f0a[nm].mid()) for nm in NAMES}
for a, R in ((0.0, 1.0), (1.2, 1.0)):
    r2 = x0 * x0 + y0 * y0
    b0 = a * (c_f * r2 + x0 * f0["u1"] + y0 * f0["u2"]) / (R * R + r2)
    Mloc = np.array([[b0 - f0["rho_y"], f0["rho_x"] / 2], [f0["rho_x"] / 2, b0]])
    evals, evecs = np.linalg.eigh(Mloc)
    xi = evecs[:, -1]
    outs, qs = [], []
    for nf in (8, 16, 32, 64):
        quot, pred, err = packet_terms(x0, y0, rad, xi, nf, a, R)
        qs.append(quot)
        outs.append(f"n = {nf}: quotient {quot:+.5f}, (4) error {err:.3f}")
    print(f"B3. a = {a}, R = {R}, X0 = ({x0}, {y0}), xi = top eigenvector of M(X0) (lambda(X0) = {evals[-1]:.5f}):")
    print("      " + "; ".join(outs))
    print(f"      Richardson (1/n^2) from n = 32, 64: {qs[-1] + (qs[-1] - qs[-2]) / 3:+.5f}; predicted limit"
          f" -(c+1) + <xi^T M xi>_chi^2 = {pred:+.5f}; -(c+1) + lambda(X0) = {-(c_f + 1) + evals[-1]:+.5f}")
    assert abs(qs[-1] + (qs[-1] - qs[-2]) / 3 - pred) < 0.02

print()
print("=" * 100)
print("Part D. The (a, R) map of the T4-047 obstruction for state131 (sampled sup over a polar grid)")
print("=" * 100)
t0 = time.time()
rg = np.unique(np.concatenate([np.logspace(-2, 8, 251), [1.0, 1.5, 2.625, 5.0, 11.0, 23.0, 135.0]]))
tg = np.linspace(0, np.pi / 2, 25)
pts = [(float(r * math.cos(t)), float(r * math.sin(t)), r, t) for r in rg for t in tg]
PF = []
for (px, py, r, t) in pts:
    PF.append(fields_arb(px, py))
arr = {nm: np.array([float(f[nm].mid()) for f in PF]) for nm in NAMES}
rad_rel = max(float(f[nm].rad()) / max(1.0, abs(float(f[nm].mid()))) for f in PF for nm in NAMES)
PXv = np.array([p[0] for p in pts]); PYv = np.array([p[1] for p in pts]); RGv = np.array([p[2] for p in pts])
THv = np.array([p[3] for p in pts])
print(f"D0. {len(pts)} grid points (r in [1e-2, 1e8], 251 log-spaced values plus the T4-047 abscissae; theta in [0, pi/2],"
      f" 25 values), arb fields in {time.time() - t0:.1f} s, max relative ball radius {rad_rel:.1e}")
probe = [i for i in range(len(pts)) if RGv[i] in (rg[0], rg[60], rg[100], rg[130], rg[180]) and THv[i] in (tg[0], tg[12], tg[24])]
fl = fields_np(PXv[probe], PYv[probe])
ferr = max(abs(fl[nm][ii] - arr[nm][i]) / max(1.0, abs(arr[nm][i])) for ii, i in enumerate(probe) for nm in NAMES)
print(f"    float64 evaluator (used only in Part B) against arb on {len(probe)} probe points with r up to {rg[180]:.3g}:"
      f" max relative error {ferr:.1e}")
thX = (np.hypot(arr["rho_x"], arr["rho_y"]) - arr["rho_y"]) / 2
VX = c_f * RGv ** 2 + PXv * arr["u1"] + PYv * arr["u2"]
i1 = int(np.argmax(thX))
i2 = int(np.argmax(VX / RGv ** 2))
print(f"    sampled sup of theta_X = (|D rho| - rho_y)/2: {thX[i1]:.6f} at r = {RGv[i1]:.4g}, theta = {THv[i1]:.4f};"
      f" c + 1 = {c_f + 1:.6f}")
print(f"    sampled sup of (V.X)/r^2 = c + (X.u)/r^2: {VX[i2] / RGv[i2] ** 2:.6f} at r = {RGv[i2]:.4g}, theta = {THv[i2]:.4f};"
      f" 2c - 1 = {2 * c_f - 1:.6f} (the value at the origin along the x axis, d_x u1(0) = c - 1)")
for rr_ in (1e4, 1e6, 1e8):
    sel = np.isclose(RGv, rr_, rtol=1e-9)
    print(f"    at r = {rr_:.0e}: max over theta of theta_X = {thX[sel].max():.2e}, of |(X.u)/r^2| ="
          f" {np.abs((VX / RGv ** 2 - c_f)[sel]).max():.2e} (r^(gamma-1) = {rr_ ** (float(gam) - 1):.2e})")
print(f"    lemma (far field): every term of u has homogeneity degree <= 2 p_0 - 3 = gamma and of D rho degree <= gamma - 1,"
      f" so lambda -> a c as r -> oo for every R; hence Lambda(a, R) >= a c, and a c > c + 1 iff a > 1 + 1/c = {1 + 1 / c_f:.6f}")
AL = [Fr(0), Fr(1), Fr(11, 10), Fr(6, 5), Fr(13, 10), Fr(7, 5), Fr(3, 2), Fr(31, 20), Fr(8, 5)]
EX = list(range(-4, 13))
print("D1. sampled max over the grid of lambda - (c+1), R = 2^e (rows a, columns e); a positive entry is then re-evaluated")
print("    in arb at the maximizing grid point (D2):")
print("        e:" + "".join(f"{e:>7}" for e in EX))
cert = []
summary = []
for a in AL:
    af = float(a)
    row = []
    for e in EX:
        R = 2.0 ** e
        lamg = af * VX / (R * R + RGv ** 2) + thX
        i = int(np.argmax(lamg))
        ex = lamg[i] - (c_f + 1)
        row.append(ex)
        if ex > 0:
            cert.append((a, e, i, ex))
    print(f"    {str(a):>5}:" + "".join(f"{v:+7.3f}" for v in row))
    summary.append((a, row))
print("D2. arb re-evaluation of every positive entry at its maximizing grid point (exact binary point, exact a and R):")
ncert, nfail = 0, 0
first_free = {}
for a, e, i, ex in cert:
    f = PF[i]
    exa = lam_arb(f, PXv[i], PYv[i], a, Fr(2) ** e) - (c_a + 1)
    if exa > 0:
        ncert += 1
    else:
        nfail += 1
        print(f"    a = {a}, e = {e}: not certified, arb {ball(exa)}")
print(f"    certified lambda(X) - (c+1) > 0 (hence Lambda > c + 1, an obstruction by T4-047) for {ncert} of {len(cert)} entries")
assert nfail == 0
print("D3. summary per a, R = 2^e (the obstructed side is certified by D2; the unobstructed side is FLOAT):")
for a, row in summary:
    pos = [e for e, v in zip(EX, row) if v > 0]
    negs = [e for e, v in zip(EX, row) if v <= 0]
    best = min(row)
    eb = EX[row.index(best)]
    lim = float(a) * c_f
    pr = f"{pos[0]}..{pos[-1]}" if pos else "none"
    nr = f"{negs[0]}..{negs[-1]}" if negs else "none"
    print(f"    a = {str(a):>5}: certified obstruction for e in {pr}; no sampled obstruction for e in {nr};"
          f" rigorous c + 1 - Lambda <= c + 1 - a c = {c_f + 1 - lim:+.4f} for every R;"
          f" sampled c + 1 - Lambda at R = 2^12: {-row[-1]:+.4f}")
print(f"Total time {time.time() - T_START:.1f} s")
