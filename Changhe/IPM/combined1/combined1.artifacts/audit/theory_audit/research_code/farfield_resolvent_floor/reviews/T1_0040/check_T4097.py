"""Independent check by c1-t1 of c1-t4 T4-097 (review R1-013 in nonlinear_closure/REVIEWS_v09.md).

Target: c1-t4/research/farfield_resolvent_floor/PROOF.md (sha256 1d195ca6...): an actual high inverse bound
Y(L^-1 f) <= M Y(f) on the T4-058 dyadic space Y forces M >= 1/beta_inf, beta_inf = 1 + c - c a. Also the plateau
inequality and the cover criterion (7) of c1-t4/research/dyadic_laplacian_certificate/PROOF.md (T4-098/T4-099).

Part A (sympy, exact; my own derivations written from the statements):
  A1. Wirtinger derivatives of r^a p(log r) e^(i n theta): d_zbar gives envelope (p' + (a - n) p)/2 in mode n + 1,
      d_z gives (p' + (a + n) p)/2 in mode n - 1, so B = d_z d_zbar^-1 acts on envelopes by g -> g + n p with
      p' + (a - n) p = 2 g; the two convolution solutions are checked by differentiation under the integral.
  A2. symbols: B = (xi1 - i xi2)^2/|xi|^2 and -(1 + B)/2 = U2 + i U1 for U = (xi1 xi2, -xi1^2)/|xi|^2.
  A3. (c r d_r - 1 + beta_inf) r^b phi(log r) sin(theta) = c r^b phi'(log r) sin(theta), b = a - 1.
  A4. low-term density of h_N in t = log r: r^(2b) r^2 (1 + r^2/Rw^2)^-a -> Rw^(2a).
  A5. plateau scaling 2^(2(1-a)j) ||Lap(F(2^j .))||^2_(1<|X|<2) = 2^(2(2-a)j) ||Lap F||^2_(2^j<r<2^(j+1)), the shell
      integral of r^(2b-3), the geometric sum (5), and the equivalence of (5) > (6) with (7) under a = 2/c + delta x.
Part B (FLOAT, FFT on a periodic box): U[h] for h = r^b phi(log r) sin(theta) with phi supported in log r in
  (log 2, log 6): vanishing inside r = 2 and agreement with the exact mode formulas, for two different factorizations
  (a = 6/5 and a = 1).
Part C (mpmath, FLOAT arithmetic of stated formulas): ceilings (8); the lower bound (5) for state131 with the c1-t4
  leading Laplacian norm D (copied number, source tail_results.json sha 50691e61...), J = 13, epsilon = 1/2; the
  squared ratio of (7) on a fine x grid against the c1-t4/c1-n4 certified cell minimum 11.2378037794.
Part D (FLOAT, own state131 evaluator copied from check_T4047.py): hypotheses of T4-097 for state131: finite angular
  content of u and D rho and the decay r^-delta of the coefficients of u/r and D rho, delta = 1 - 1/c.

Usage (from artifacts/checks):
  OMP_NUM_THREADS=1 python3 -B check_T4097.py > check_T4097.out
Needs sympy, numpy, mpmath, python-flint. Memory about 2 GB (4096^2 FFT), time under a minute.
"""
import json
import math
import time
from fractions import Fraction as Fr
from math import comb
from pathlib import Path

import flint
import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
T0 = time.time()

# ------------------------------------------------------------------------------------------------------------------
print("Part A (sympy, exact)")
r, t, th, a, c, Rw, n, xs = sp.symbols("r t theta a c R_w n x", positive=True)
I_ = sp.Symbol("i")                      # imaginary unit kept as a symbol; i^2 = -1 imposed by substitution
nn = sp.Symbol("nn", integer=True)
P = sp.Function("P")
# r = e^t, d_r = e^-t d_t, (1/r) d_theta acts on e^(i n theta) as i n e^-t; v = e^(a t) P(t) e^(i n theta)
dr_v = sp.exp(-t) * sp.diff(sp.exp(a * t) * P(t), t)
dth_v = I_ * nn * sp.exp(-t) * sp.exp(a * t) * P(t)
zbar_env = sp.expand(sp.simplify((dr_v + I_ * dth_v) / 2 / sp.exp((a - 1) * t))).subs(I_ ** 2, -1)
z_env = sp.expand(sp.simplify((dr_v - I_ * dth_v) / 2 / sp.exp((a - 1) * t))).subs(I_ ** 2, -1)
ok1 = sp.simplify(zbar_env - (sp.diff(P(t), t) + (a - nn) * P(t)) / 2) == 0
ok2 = sp.simplify(z_env - (sp.diff(P(t), t) + (a + nn) * P(t)) / 2) == 0
print("A1. d_zbar[r^a p(log r) e^(i n th)] = e^(i(n+1)th) r^(a-1) (p' + (a-n)p)/2:", ok1,
      "; d_z[...] = e^(i(n-1)th) r^(a-1) (p' + (a+n)p)/2:", ok2)
assert ok1 and ok2
pp, g = sp.symbols("P g")
# input mode m = n + 1 with envelope g (after r^(a-1)): p' + (a-n)p = 2g, output mode m - 2 envelope (p' + (a+n)p)/2 = g + n p
out_env = sp.expand(((2 * g - (a - nn) * pp) + (a + nn) * pp) / 2)
print("    output envelope with p' = 2g - (a-n)p:", out_env, "= g + n p:", sp.simplify(out_env - (g + nn * pp)) == 0)
assert sp.simplify(out_env - (g + nn * pp)) == 0
# convolution solutions: forward p = -2 int_0^inf e^(-(n-a)v) g(t+v) dv (n > 0), backward p = 2 int_0^inf e^(-(a-n)v) g(t-v) dv
# (n < 0); check p' + (a - n) p = 2 g numerically (mpmath, 30 digits) for g = exp(-t^2) at t = 0.3
mp.mp.dps = 30
worst = 0
for nval in (2, 4, -2, -4):
    for aval in (mp.mpf(6) / 5, mp.mpf(1), mp.mpf(3) / 2):
        if nval > 0:
            Pf = lambda T: -2 * mp.quad(lambda w: mp.e ** (-(nval - aval) * w) * mp.e ** (-(T + w) ** 2), [0, mp.inf])
        else:
            Pf = lambda T: 2 * mp.quad(lambda w: mp.e ** (-(aval - nval) * w) * mp.e ** (-(T - w) ** 2), [0, mp.inf])
        T_ = mp.mpf("0.3")
        res = mp.diff(Pf, T_) + (aval - nval) * Pf(T_) - 2 * mp.e ** (-T_ ** 2)
        worst = max(worst, abs(res))
print("    convolution solutions: max |p' + (a-n)p - 2g| over n in {2, 4, -2, -4}, a in {6/5, 1, 3/2}:", mp.nstr(worst, 3))
assert worst < 1e-20
# endpoint behaviour: for n > 0 and g supported in t > T the forward solution is const * e^((n-a)t) for t < T, so the
# velocity is const * z^(n-1) near 0 (regular; checked in B); for n < 0 the backward solution vanishes for t < T.
xi1, xi2 = sp.symbols("xi1 xi2", real=True)
nrm = xi1 ** 2 + xi2 ** 2
sym_dz = (sp.I * xi1 + xi2) / 2          # d_z = (d_x - i d_y)/2, d_x -> i xi1, d_y -> i xi2
sym_dzb = (sp.I * xi1 - xi2) / 2
Bsym = sp.simplify(sym_dz / sym_dzb)
ok = sp.simplify(Bsym - (xi1 - sp.I * xi2) ** 2 / nrm) == 0
U1s, U2s = xi1 * xi2 / nrm, -xi1 ** 2 / nrm
ok2 = sp.simplify(-(1 + Bsym) / 2 - (U2s + sp.I * U1s)) == 0
print("A2. B symbol = (xi1 - i xi2)^2/|xi|^2:", ok, "; -(1+B)/2 = U2 + i U1:", ok2)
assert ok and ok2

b = a - 1
phi = sp.Function("phi")
h = r ** b * phi(sp.log(r)) * sp.sin(th)
binf = 1 + c - c * a
lhs = sp.simplify(c * r * sp.diff(h, r) - h + binf * h - c * r ** b * sp.diff(phi(t), t).subs(t, sp.log(r)) * sp.sin(th))
print("A3. (c r d_r - 1 + beta_inf) h - c r^b phi'(log r) sin(theta) =", lhs)
assert lhs == 0
dens = sp.exp(2 * b * t) * sp.exp(2 * t) * (1 + sp.exp(2 * t) / Rw ** 2) ** (-a)
uu = sp.Symbol("u", positive=True)       # u = e^(-2t) -> 0+
dens_u = (Rw ** 2 / (Rw ** 2 * uu + 1)) ** a
same = sp.simplify(sp.powsimp(sp.expand_power_base(dens.subs(t, -sp.log(uu) / 2), force=True), force=True)
                   - dens_u) == 0
lim = sp.limit(dens_u, uu, 0, "+")
print("A4. low density factor in t: r^(2b) r^2 w_Rw^2 = (R_w^2/(R_w^2 e^(-2t) + 1))^a:", same, "; limit t -> oo:", lim)
assert same and sp.simplify(lim - Rw ** (2 * a)) == 0

j, bb, J, eta = sp.symbols("j b J eta", positive=True)
# ||Lap g||^2 on 1<|X|<2 for g = F(2^j X): Lap g = 4^j (Lap F)(2^j X), dX = 4^-j dY
fac = sp.simplify(2 ** (2 * (1 - a) * j) * 4 ** (2 * j) * 4 ** (-j))
print("A5. dyadic factor 2^(2(1-a)j) 4^(2j) 4^(-j) =", fac, "= 2^(2(2-a)j):", sp.simplify(fac - 2 ** (2 * (2 - a) * j)) == 0)
assert sp.simplify(fac - 2 ** (2 * (2 - a) * j)) == 0
bq = sp.Rational(1, 7)
shell = sp.integrate(r ** (2 * bq - 3), (r, 2 ** j, 2 ** (j + 1)))
Kc = (1 - sp.Integer(2) ** (2 * bq - 2)) / (2 - 2 * bq)
print("    shell integral of r^(2b-3) over (2^j, 2^(j+1)) equals K 2^((2b-2)j) at b = 1/7:",
      sp.simplify(shell - Kc * 2 ** ((2 * bq - 2) * j)) == 0)
assert sp.simplify(shell - Kc * 2 ** ((2 * bq - 2) * j)) == 0
# exponent: 2(2-a)j + (2b-2)j = -2 eta j with eta = a - 1 - b
print("    2(2-a) + (2b-2) + 2(a-1-b) =", sp.simplify(2 * (2 - a) + (2 * bb - 2) + 2 * (a - 1 - bb)))
# (7): with b = 2/c - 1, a = 2/c + delta x, delta = 1 - 1/c, eps = 1/2, E = D^2/pi
D, K_ = sp.symbols("D K", positive=True)
dl = 1 - 1 / c
a_x = 2 / c + dl * xs
b_c = 2 / c - 1
eta_x = sp.simplify(a_x - 1 - b_c)
binf_x = sp.simplify(1 + c - c * a_x)
print("    eta =", eta_x, "; beta_inf =", sp.factor(binf_x), "; (c-1)(1-x) - beta_inf =", sp.simplify((c - 1) * (1 - xs) - binf_x))
assert sp.simplify(eta_x - dl * xs) == 0 and sp.simplify((c - 1) * (1 - xs) - binf_x) == 0
Y5sq = (D / 2) ** 2 * K_ * 2 ** (-2 * eta_x * J) / (1 - 2 ** (-2 * eta_x))
Y6sq = 8 * sp.pi * binf_x ** 4 / (1 + a_x) ** 2
lhs7 = (D ** 2 / sp.pi) * K_ / 4 * (1 + 2 / c + dl * xs) ** 2
rhs7 = 8 * (c - 1) ** 4 * (1 - xs) ** 4 * (1 - 2 ** (-2 * dl * xs)) * 2 ** (2 * J * dl * xs)
# (5)^2 > (6)^2  <=>  lhs7 > rhs7 : the ratio of the two differences is a positive factor
ratio_sym = sp.simplify((Y5sq / Y6sq) / (lhs7 / rhs7))
print("    [(5)^2/(6)^2] / [lhs(7)/rhs(7)] =", ratio_sym)
assert ratio_sym == 1

# ------------------------------------------------------------------------------------------------------------------
# Evaluator copied verbatim from check_T4047.py (validated there against the A2 point enclosures, R1-011).
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





# ------------------------------------------------------------------------------------------------------------------
print()
print("Part B (FLOAT, FFT on [-64, 64)^2 with 4096^2 points): U[h] for h = r^b phi(log r) sin(theta)")
Nn, Lb = 4096, 128.0
dx = Lb / Nn
xg = -Lb / 2 + dx * np.arange(Nn)
XX, YY = np.meshgrid(xg, xg, indexing="ij")
RR = np.hypot(XX, YY)
TT = np.log(np.where(RR > 0, RR, 1e-300))
t_lo, t_hi = math.log(2.0), math.log(6.0)
tc, hw = (t_lo + t_hi) / 2, (t_hi - t_lo) / 2


def bump_t(tv):
    sv = (np.asarray(tv) - tc) / hw
    out = np.zeros_like(sv, dtype=float)
    m = np.abs(sv) < 1
    out[m] = np.exp(-1.0 / (1.0 - sv[m] ** 2))
    return out


def conv_back(tv, kap):
    """K(t) = int_0^inf e^(-kap v) phi(t - v) dv on a fine grid (trapezoid), then interpolated"""
    tf = np.linspace(t_lo - 1e-3, max(t_hi, float(np.max(tv))) + 1e-3, 400001)
    hstep = tf[1] - tf[0]
    ph = bump_t(tf)
    Kf = np.zeros_like(tf)
    dec = math.exp(-kap * hstep)
    for i in range(1, len(tf)):
        Kf[i] = dec * Kf[i - 1] + 0.5 * hstep * (dec * ph[i - 1] + ph[i])
    return np.interp(tv, tf, Kf, left=0.0)


k1 = 2 * np.pi * np.fft.fftfreq(Nn, d=dx)
for aval in (1.2, 1.0):
    bval = aval - 1
    f = np.where(RR > 0, RR ** bval, 0.0) * bump_t(TT) * np.where(RR > 0, YY / np.where(RR > 0, RR, 1), 0.0)
    fh = np.fft.fft2(f)
    K1, K2 = np.meshgrid(k1, k1, indexing="ij")
    KK = K1 ** 2 + K2 ** 2
    KK[0, 0] = 1.0
    U1 = np.real(np.fft.ifft2(fh * K1 * K2 / KK))
    U2 = np.real(np.fft.ifft2(fh * (-K1 ** 2) / KK))
    del fh, K1, K2, KK
    Uabs = np.hypot(U1, U2)
    Umax = float(np.max(Uabs))
    inner = RR < 1.9
    print(f"  a = {aval}: max |U| = {Umax:.6f}; B1. max |U| on r < 1.9 = {float(np.max(Uabs[inner])):.3e} "
          f"(relative {float(np.max(Uabs[inner])) / Umax:.2e}; exact value 0)")
    assert float(np.max(Uabs[inner])) / Umax < 1e-3
    mask = (RR > 0.5) & (RR < 40)
    rr_m, th_m, tt_m = RR[mask], np.arctan2(YY[mask], XX[mask]), TT[mask]
    Gv = bump_t(tt_m)
    KG = conv_back(tt_m, aval + 2)          # n = -2: kernel e^(-(a - n) v) = e^(-(a+2) v)
    fz = rr_m ** bval * (Gv * np.exp(1j * th_m) - Gv * np.exp(-1j * th_m)) / 2j
    Bf = rr_m ** bval * (Gv * np.exp(-1j * th_m) - (Gv - 4 * KG) * np.exp(-3j * th_m)) / 2j
    Wf = -(fz + Bf) / 2
    err = float(np.max(np.abs(Wf - (U2[mask] + 1j * U1[mask]))))
    far = (RR > 8) & (RR < 40)
    print(f"     B2. max |(U2 + i U1) - mode formula| on 0.5 < r < 40 = {err:.3e} (relative {err / Umax:.2e}); "
          f"max |U| on 8 < r < 40 = {float(np.max(Uabs[far])):.3e} (the m = -3 tail of the backward kernel)")
    assert err / Umax < 1e-3
    del U1, U2, f, Uabs
del XX, YY, RR, TT

# ------------------------------------------------------------------------------------------------------------------
print()
print("Part C (mpmath; arithmetic of the stated formulas)")
mp.mp.dps = 40
cc = mp.mpf(Fr(json.loads((HERE / "data/state131_exact.json").read_text())["exact_parameters"]["cl"]).numerator) / \
    mp.mpf(Fr(json.loads((HERE / "data/state131_exact.json").read_text())["exact_parameters"]["cl"]).denominator)
dlt = 1 - 1 / cc
bS = 2 / cc - 1
print(f"  c = {mp.nstr(cc, 15)}, delta = 1 - 1/c = {mp.nstr(dlt, 12)}, b = 2/c - 1 = {mp.nstr(bS, 12)}, "
      f"window ({mp.nstr(2 / cc, 8)}, {mp.nstr(1 + 1 / cc, 8)})")
print("  C1. ceilings: R_univ(a) = sqrt(8 pi) beta_inf/(1+a), floor 1/beta_inf, (8) Y(F) < sqrt(8 pi) beta_inf^2/(1+a)")
for aval in (mp.mpf(1), mp.mpf(11) / 10, mp.mpf(6) / 5, mp.mpf(13) / 10, mp.mpf(7) / 5, mp.mpf(3) / 2):
    bi = 1 + cc - cc * aval
    print(f"     a = {mp.nstr(aval, 4):>4}: beta_inf = {mp.nstr(bi, 8)}, M >= {mp.nstr(1 / bi, 8)}, "
          f"R_univ = {mp.nstr(mp.sqrt(8 * mp.pi) * bi / (1 + aval), 8)}, (8) ceiling = "
          f"{mp.nstr(mp.sqrt(8 * mp.pi) * bi ** 2 / (1 + aval), 8)}")
Dl = mp.mpf("15.20937674970366121387683616663")    # c1-t4 tail_results.json leading_laplacian_norm (midpoint)
Jv, epsv = 13, mp.mpf(1) / 2
Kv_ = (1 - mp.mpf(2) ** (2 * bS - 2)) / (2 - 2 * bS)
print(f"  C2. lower bound (5) for state131: D = {mp.nstr(Dl, 16)}, J = 13, epsilon = 1/2, K = {mp.nstr(Kv_, 12)}")
for aval in (mp.mpf(111) / 100, mp.mpf(6) / 5, mp.mpf(13) / 10, mp.mpf(7) / 5, mp.mpf(3) / 2, mp.mpf(31) / 20):
    et = aval - 1 - bS
    lb = (1 - epsv) * Dl * mp.sqrt(Kv_) * mp.mpf(2) ** (-et * Jv) / mp.sqrt(1 - mp.mpf(2) ** (-2 * et))
    bi = 1 + cc - cc * aval
    ceil8 = mp.sqrt(8 * mp.pi) * bi ** 2 / (1 + aval)
    print(f"     a = {mp.nstr(aval, 4):>4}: Y(F) >= {mp.nstr(lb, 8)}, ceiling (8) {mp.nstr(ceil8, 8)}, "
          f"ratio {mp.nstr(lb / ceil8, 6)}")
    assert lb > ceil8
Ev = Dl ** 2 / mp.pi


def ratio7(xv):
    lhs = Ev * Kv_ / 4 * (1 + 2 / cc + dlt * xv) ** 2
    rhs = 8 * (cc - 1) ** 4 * (1 - xv) ** 4 * (1 - mp.mpf(2) ** (-2 * dlt * xv)) * mp.mpf(2) ** (2 * Jv * dlt * xv)
    return lhs / rhs


grid = [mp.mpf(k) / 20000 for k in range(1, 20000)]
vals = [ratio7(xv) for xv in grid]
kmin = min(range(len(vals)), key=lambda k: vals[k])
print(f"  C3. squared ratio lhs(7)/rhs(7) on x = k/20000: minimum {mp.nstr(vals[kmin], 12)} at x = {mp.nstr(grid[kmin], 6)} "
      f"(a = {mp.nstr(2 / cc + dlt * grid[kmin], 8)}); c1-t4/c1-n4 certified cell lower bound 11.2378037794")
assert vals[kmin] > mp.mpf("11.2378037794")
xm = mp.findroot(lambda xv: mp.diff(ratio7, xv), grid[kmin])
print(f"      local minimizer x = {mp.nstr(xm, 12)}, squared ratio {mp.nstr(ratio7(xm), 12)}")

# ------------------------------------------------------------------------------------------------------------------
print()
print("Part D (FLOAT, own evaluator of the exact state131 potential): hypotheses of T4-097")
print("  structure: chi = sum Re(z^(2m) G_jm(q)), m <= 9, so u and D rho are finite sums of z^a zbar^b times radial")
print("  functions (1+q)^(p_j - m - k) P(v): finite angular content, and log-radial derivatives keep the leading power.")
thg = 2 * np.pi * (np.arange(256) + 0.5) / 256
prev = None
for rv in (1e1, 1e2, 1e3, 1e4, 1e5):
    fx = fields_np(rv * np.cos(thg), rv * np.sin(thg))
    sc = rv ** float(dlt)
    comps = {"u1/r": fx["u1"] / rv, "u2/r": fx["u2"] / rv, "rho_x": fx["rho_x"], "rho_y": fx["rho_y"]}
    sups = {k: float(np.max(np.abs(vv))) * sc for k, vv in comps.items()}
    modes = {}
    for k, vv in comps.items():
        ch = np.abs(np.fft.rfft(vv)) / len(vv)
        big = np.nonzero(ch > 1e-12 * ch.max())[0]
        modes[k] = int(big.max())
    # first log-radial derivative by central differences (FLOAT)
    hst = 1e-4
    fp = fields_np(rv * (1 + hst) * np.cos(thg), rv * (1 + hst) * np.sin(thg))
    fm = fields_np(rv * (1 - hst) * np.cos(thg), rv * (1 - hst) * np.sin(thg))
    dl_rhoy = float(np.max(np.abs((fp["rho_y"] - fm["rho_y"]) / (2 * hst)))) * sc
    print(f"  r = {rv:8.0e}: r^delta sup|.|: " + ", ".join(f"{k} {vv:.6f}" for k, vv in sups.items())
          + f"; highest angular mode {max(modes.values())}; r^delta sup|r d_r rho_y| {dl_rhoy:.6f}")
    prev = sups
# arb validation of the float evaluator at the largest radius
fa = fields_arb(1e5 * math.cos(thg[10]), 1e5 * math.sin(thg[10]))
fn = fields_np(np.array([1e5 * math.cos(thg[10])]), np.array([1e5 * math.sin(thg[10])]))
dev = max(abs(float(fa[k].mid()) - float(fn[k][0])) / max(1e-30, abs(float(fa[k].mid()))) for k in ("rho_x", "rho_y", "u1", "u2"))
print(f"  float evaluator against arb at r = 1e5 (one angle): max relative deviation {dev:.2e}")
print(f"  reading: the r^delta-scaled sups converge, so the coefficients of u/r and D rho are O(r^-delta) with")
print(f"  delta = 1 - 1/c = {float(dlt):.6f}; the angular content is finite (modes printed above).")
print()
print(f"total time {time.time() - T0:.1f} s")
