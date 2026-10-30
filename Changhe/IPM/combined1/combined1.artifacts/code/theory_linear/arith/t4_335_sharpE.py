"""Route T-B: a sharper constant in T4-335 (1) (c1-t4 research/moment_resolved_tail/PROOF.md, sha256 99aa80a9...6df),
and its effect on the reach of the closure inequality (CI) of T4-351 (research/endpoint_closure_inequality/PROOF.md,
sha256 85e01f1b...fc34). Write-up: notes/T2_TB_sharpE.md.

Run from artifacts/:  python3 -B -u arith/t4_335_sharpE.py
Needs sympy, numpy, python-flint (Arb).

Setting. q in (-5, -3) (q* = gamma - 4), h real C1 and centrally odd with
H_q(h) = max(sup (1+|X|)^-q |h|, sup (1+|X|)^(1-q) |grad h|) <= H, M = int Y h. At X = r e (|e| = 1, any r > 0) put
g(Z) = h(rZ)/(H r^q). Then (U[h](X) + DK(X) M)/(H r^q) = (0, -g(e)/2) + PV int [K(e - Z) + DK(e) Z] g(Z) dZ, and
|grad g(Z)| <= |Z|^(q-1), |g(Z)| <= |Z|^q/(-q) (the second from the first by integration along rays, part A5).
With vectors (v1, v2) written as v2 + i v1 and Z as w = z1 + i z2, K(Z) = 1/(2 pi w^2) (A1), and the folded kernel
  k(w) = (1/(4 pi)) [chi1(w)/(1 - w)^2 - chi2(w)/(1 + w)^2] - w/pi,  chi1 = 1{|w - 1| > rho1}, chi2 = 1{|w + 1| > rho1},
is odd and conjugation-symmetric. For a unit direction (written as Re(e^{-i beta} V)) and every rho1 in (0, 1):
  |Re(e^{-i beta} (U + DK M))|/(H r^q) <= (2/pi) N(rho1) + (F_beta(rho1) + |cos beta|/2)/(-q),
  N(rho1) = (1/(-q)) int_0^rho1 ((1 - s)^q - 1)/s ds,   F_beta = int |Re(e^{-i beta} k(w))| |w|^q dA.
At a point e = e^{i theta} the integral part is rotated by e^{-2 i theta} while the contact term is not, so the
bound for all points and directions is  E_new(rho1) = (2/pi) N(rho1) + (sup_beta F_beta + 1/2)/(-q).

Parts:
  (A) sympy, exact: kernel identity; folded Taylor series and the closed forms of its majorants; the Lipschitz
      near-region integral; the density bound from the gradient bound; angular integrals; mu and mu/(-q); the
      gradient of the homogeneous test functions of part (D).
  (B) Arb, rigorous: an upper bound on E_new(3/20) by log-polar cells on the first quadrant (t in [1/20, 2000]) with a
      mean-value bound per cell, analytic bounds for t < 1/20 and t > 2000, an Arb series for N with a tail bound,
      and a Lipschitz-in-beta adaptive bisection for sup_beta.
      Revision 2026-10-29 (after T4-385 repair 5): every conversion of a ball to a double is rounded outward
      (up(), math.nextafter), the Lipschitz constant and the interval bounds of the beta bisection stay Arb balls,
      and the reported E_new_upper is a double >= the upper end of the E_new ball.
  (C) FLOAT: midpoint values of the same quantity on a finer grid, for several rho1 (how much of (B) is slack).
  (D) FLOAT: lower bounds on the best constant from homogeneous centrally odd test functions g = sin(psi(phi))
      |w|^q/(-q), |psi'| <= -q, chosen by dynamic programming, evaluated with the exact near-region formula.
  (E) Arb and FLOAT: the reach of (CI) of T4-351 with the improved constants, for 007, 013, 014.
Output: logs/t4_335_sharpE.log, data/t4_335_sharpE_results.json.
"""
import hashlib
import json
import math
import time
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
import sympy as S
from flint import acb, arb, ctx

HERE = Path(__file__).resolve().parents[1]
T4R = Path("RUN_ROOT/theory_audit_T4/research/moment_resolved_tail")
T4C = Path("RUN_ROOT/theory_audit_T4/research/endpoint_closure_inequality")
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(T4R / "PROOF.md") == "99aa80a9b5ce0474e26c8a53e53218b2b1bb628f0283eab5eb62b4aeefead6df"
assert sha(T4C / "PROOF.md") == "85e01f1bfab61b078138120f3ec6011b76ace5cd45d7436d7cdd5ca35251fc34"

# =============================== (A) exact ===============================
z1, z2, t, s, u, rho, phi, bet = S.symbols("z1 z2 t s u rho phi beta", real=True)
qs_ = S.Symbol("q", negative=True)
w = S.Symbol("w")
K1 = -z1 * z2 / (S.pi * (z1**2 + z2**2)**2)
K2 = (z1**2 - z2**2) / (2 * S.pi * (z1**2 + z2**2)**2)
fz = 1 / (2 * S.pi * (z1 + S.I * z2)**2)
A1 = S.simplify(S.re(S.expand_complex(fz)) - K2) == 0 and S.simplify(S.im(S.expand_complex(fz)) - K1) == 0
kf = (1 / (1 - w)**2 - 1 / (1 + w)**2) / (4 * S.pi) - w / S.pi
ser = S.series(kf, w, 0, 18).removeO()
A2 = S.expand(ser - sum((n + 1) * w**n / (2 * S.pi) for n in range(3, 18, 2))) == 0
maj = (1 / (1 - t)**2 - 1 / (1 + t)**2) / (4 * S.pi) - t / S.pi        # sum_{n odd >= 3} (n+1) t^n/(2 pi)
A3 = {"majorant_closed_form": S.simplify(maj - (2 * t**3 - t**5) / (S.pi * (1 - t**2)**2)) == 0,
      "rest_after_cubic": S.simplify(maj - 2 * t**3 / S.pi - t**5 * (3 - 2 * t**2) / (S.pi * (1 - t**2)**2)) == 0,
      "cubic_coefficient_2_over_pi": S.simplify(ser.coeff(w, 3) - 2 / S.pi) == 0}
lip = ((1 - s)**qs_ - 1) / (-qs_)
A4 = {"d_ds": S.simplify(S.diff(lip, s) - (1 - s)**(qs_ - 1)) == 0, "at_0": lip.subs(s, 0) == 0}
dens = (1 + rho)**qs_ / (-qs_)
A5 = {"d_drho": S.simplify(S.diff(dens, rho) + (1 + rho)**(qs_ - 1)) == 0,
      "limit_inf_q=-7/2": S.limit(dens.subs(qs_, S.Rational(-7, 2)), rho, S.oo) == 0}
# int_0^{2 pi} |cos n phi| dphi = 4, summed over the 2n + 1 pieces between consecutive zeros (2j + 1) pi/(2n)
A6 = {"abs_cos_%d" % n: sum(abs(S.integrate(S.cos(n * phi), (phi, a_, b_))) for a_, b_ in
                            zip([0] + [(2 * j + 1) * S.pi / (2 * n) for j in range(2 * n)],
                                [(2 * j + 1) * S.pi / (2 * n) for j in range(2 * n)] + [2 * S.pi])) == 4
      for n in (1, 2, 3)}
qt = S.Rational(-7, 2)
mu_t = 4 * S.integrate(rho**2 * (1 + rho)**qt, (rho, 0, S.oo))
A7 = {"mu_formula_q=-7/2": S.simplify(mu_t - 8 / ((-qt - 1) * (-qt - 2) * (-qt - 3))) == 0}
psi = S.Function("psi")(phi)
gT = S.sin(psi) * rho**qs_ / (-qs_)
gr, gp = S.diff(gT, rho), S.diff(gT, phi) / rho
A8 = S.simplify(gr**2 + gp**2 - rho**(2 * qs_ - 2) * (qs_**2 * S.sin(psi)**2 + S.cos(psi)**2 * S.diff(psi, phi)**2) / qs_**2) == 0
OUT["A"] = {"A1_kernel_identity": A1, "A2_folded_series_to_w17": A2, "A3": A3, "A4_lipschitz_integral": A4,
            "A5_density_from_gradient": A5, "A6_angular": A6, "A7": A7, "A8_test_gradient": A8}
flat = [A1, A2, A8] + list(A3.values()) + list(A4.values()) + list(A5.values()) + list(A6.values()) + list(A7.values())
assert all(flat)
print("(A) all exact checks pass:", json.dumps(OUT["A"]))

# =============================== (B) Arb upper bound ===============================
ctx.prec = 64
PI = arb.pi()
cA = arb(4076476460239181) / arb(2)**51
qA = 1 / cA - 4
aA = -qA
RHO1 = Fr(3, 20)
rho1 = arb(RHO1.numerator) / RHO1.denominator
t0A, TA = arb(1) / 20, arb(2000)
NT, NPH, SUB = 2000, 500, 8


def N_arb(r1):
    """(1/a) sum_{k>=1} (a)_k r1^k/(k k!) with a = -q > 1; for k >= K the term ratio is <= r1 (a + K)/(K + 1)."""
    p, tot, K = aA * r1, arb(0), 300
    for k in range(1, K + 1):
        term = p / k
        tot += term
        p = p * (aA + k) * r1 / (k + 1)
    th = r1 * (aA + K) / (K + 1)
    assert th < 1
    tail = term * th / (1 - th)
    return (tot + arb(0, tail.upper())) / aA


NA = N_arb(rho1)
near = (8 / PI) * t0A**(qA + 5) / (qA + 5) + 2 * 3 / (1 - t0A**2)**2 * t0A**(qA + 7) / (qA + 7)
tailA = (4 / PI) * TA**(qA + 3) / (-qA - 3) + (TA / (TA - 1))**2 * TA**qA / aA
assert t0A < 1 - rho1 and TA > 1 + rho1
le = np.linspace(np.log(1 / 20), np.log(2000), NT + 1)
tfl = np.exp(le)
tfl[0], tfl[-1] = 1 / 20, 2000.0
assert np.all(np.diff(tfl) > 0)
tE = [arb(float(x)) for x in tfl]
tE[0], tE[-1] = t0A, TA
dph = PI / 2 / NPH
phE = [dph * j for j in range(NPH + 1)]


def cell(ta, tb, pa, pb):
    """Mean-value data for one polar cell: weight, and (Re k, Im k, slack) for each branch that can occur."""
    tm, pm = (ta + tb) / 2, (pa + pb) / 2
    rad = (tb - ta) / 2 + tb * (pb - pa) / 2
    W = (pb - pa) * (tb**(qA + 2) - ta**(qA + 2)) / (qA + 2)
    wc = acb(tm * pm.cos(), tm * pm.sin())
    a_, b_ = 1 - wc, 1 + wc
    d1, d2 = abs(a_), abs(b_)
    ib = 1 / (b_ * b_)
    br = []
    if not (d1 + rad < rho1):                     # the cell may meet |w - 1| > rho1: branch chi1 = 1
        assert d1 - rad > 0
        ia = 1 / (a_ * a_)
        k = (ia - ib) / (4 * PI) - wc / PI
        kp = (ia / a_ + ib / b_) / (2 * PI) - 1 / PI
        M2 = 3 / (2 * PI) * ((d1 - rad)**-4 + (d2 - rad)**-4)
        br.append((k.real, k.imag, rad * (abs(kp) + rad * M2), abs(k)))
    if not (d1 - rad > rho1):                     # the cell may meet |w - 1| < rho1: branch chi1 = 0
        k = -ib / (4 * PI) - wc / PI
        kp = (ib / b_) / (2 * PI) - 1 / PI
        M2 = 3 / (2 * PI) * (d2 - rad)**-4
        br.append((k.real, k.imag, rad * (abs(kp) + rad * M2), abs(k)))
    return W, br, rad


tB = time.monotonic()
rows = []                    # per radial row: W_row/dph-independent lists of single-branch (Re, Im) and summed slack
extra = []                   # subcells of crossing cells: (W, branches)
lipB = arb(0)
slack_single = arb(0)
n_cells, n_cross, n_sub = 0, 0, 0
for i in range(NT):
    ta, tb = tE[i], tE[i + 1]
    REs, IMs = [], []
    Wrow = None
    for j in range(NPH):
        W, br, rad = cell(ta, tb, phE[j], phE[j + 1])
        n_cells += 1
        if Wrow is None:
            Wrow = W
        if len(br) == 1:
            re_, im_, sl, ak = br[0]
            REs.append(re_)
            IMs.append(im_)
            slack_single += W * 2 * sl
            lipB += W * 2 * ak
        else:
            n_cross += 1
            for ii in range(SUB):
                sa = ta + (tb - ta) * ii / SUB
                sb = ta + (tb - ta) * (ii + 1) / SUB if ii + 1 < SUB else tb
                for jj in range(SUB):
                    qa = phE[j] + (phE[j + 1] - phE[j]) * jj / SUB
                    qb = phE[j] + (phE[j + 1] - phE[j]) * (jj + 1) / SUB if jj + 1 < SUB else phE[j + 1]
                    Ws, brs, _ = cell(sa, sb, qa, qb)
                    n_sub += 1
                    extra.append((Ws, brs))
                    lipB += Ws * 2 * (brs[0][3] if len(brs) == 1 else (brs[0][3] + brs[1][3] + abs(brs[0][3] - brs[1][3])) / 2)
    rows.append((REs, IMs, Wrow))
print("(B) %d cells (%d crossing |w - 1| = rho1, split into %d subcells), setup %.1f s"
      % (n_cells, n_cross, n_sub, time.monotonic() - tB))


def mx(x, y):
    return (x + y + abs(x - y)) / 2


def up(x):
    """A double >= every point of the ball x (outward rounding of the float conversion)."""
    return math.nextafter(float(x.upper()), math.inf)


def Ub(be):
    """Rigorous upper bound on F_beta: 2 int_Q1 (|Re(e^{-i b} k)| + |Re(e^{i b} k)|) |w|^q + near + tail."""
    cb, sb = be.cos(), be.sin()
    tot = arb(0)
    for REs, IMs, Wrow in rows:
        sr = arb(0)
        for re_, im_ in zip(REs, IMs):
            x, y = cb * re_, sb * im_
            sr += abs(x + y) + abs(x - y)
        tot += Wrow * sr
    tot += slack_single
    for Ws, brs in extra:
        v1 = [abs(cb * b[0] + sb * b[1]) + b[2] for b in brs]
        v2 = [abs(cb * b[0] - sb * b[1]) + b[2] for b in brs]
        m1 = v1[0] if len(v1) == 1 else mx(v1[0], v1[1])
        m2 = v2[0] if len(v2) == 1 else mx(v2[0], v2[1])
        tot += Ws * (m1 + m2)
    return 2 * tot + near + tailA


LAM = 2 * lipB               # |d/d beta| of the cell sum is <= 2 sum 2 W |k_c| (both conjugate terms, both half planes)
cache = {}


def ub_at(k_, den):
    key = (k_, den)
    if key not in cache:
        cache[key] = Ub(PI / 2 * k_ / den).upper()
    return cache[key]


# adaptive bisection on [0, pi/2] in dyadic units: sup over [b_a, b_b] <= (U(b_a) + U(b_b))/2 + LAM (b_b - b_a)/2.
# Each interval bound is an Arb ball; only the refinement decision uses doubles. The final sup is the largest outward
# rounded double up(bound) over the accepted intervals, so supF >= sup_beta F_beta.
tB2 = time.monotonic()
LAMu = up(LAM)
work = [(k_, 16) for k_ in range(16)]
done = []
best = max(up(ub_at(k_, 16)) for k_ in range(17))
TOL = 0.02
while work:
    k_, den = work.pop()
    ua, ubv = ub_at(k_, den), ub_at(k_ + 1, den)
    boundA = (ua + ubv) / 2 + LAM * (PI / 2 / den) / 2
    best = max(best, up(ua), up(ubv))
    if up(boundA) <= best + TOL or den >= 2**14:
        done.append((k_, den, boundA))
    else:
        work += [(2 * k_, 2 * den), (2 * k_ + 1, 2 * den)]
supF_float = max(up(b) for _, _, b in done)
supF = arb(supF_float)                          # exact double, >= every accepted interval bound
grid_vals = sorted(((k_ / den, float(v)) for (k_, den), v in cache.items()), key=lambda z: z[0])
arg = max(grid_vals, key=lambda z: z[1])
E_new = (2 / PI) * NA + (supF + arb(1) / 2) / aA
E_dir0 = (2 / PI) * NA + (arb(cache[(0, 16)]) * (1 + arb(2)**-50) + arb(1) / 2) / aA
print("    N(3/20) = %s, near (t < 1/20) = %s, tail (t > 2000) = %s, slack of single cells = %s, LAM = %.4f"
      % (NA.str(10), near.str(8), tailA.str(8), slack_single.str(8), LAMu))
print("    %d evaluations of the beta bound (%.1f s); max grid value %.6f at beta = %.5f (pi/2 units); sup over [0, pi/2]"
      " <= %.6f" % (len(cache), time.monotonic() - tB2, arg[1], arg[0], supF_float))
print("    E_new(3/20) = (2/pi) N + (sup_beta F + 1/2)/(-q) <= %.6f (Arb upper end of %s); at beta = 0 alone %.6f"
      % (up(E_new), E_new.str(10), up(E_dir0)))
OUT["B"] = {"rho1": "3/20", "t0": "1/20", "T": 2000, "grid": [NT, NPH, SUB], "cells": n_cells, "crossing": n_cross,
            "subcells": n_sub, "N": NA.str(20), "near": near.str(12), "tail": tailA.str(12),
            "slack_single": slack_single.str(12), "LAM": LAMu, "beta_evaluations": len(cache),
            "beta_grid_values_[beta/(pi/2), upper]": grid_vals, "supF_upper": supF_float,
            "E_new_upper": up(E_new), "E_new_ball": E_new.str(20), "E_beta0_upper": up(E_dir0)}
E_up = up(E_new)

# =============================== (C) FLOAT midpoint values ===============================
c = 4076476460239181 / 2**51
qf = 1 / c - 4


def N_float(r1):
    ss = np.linspace(0, r1, 200001)[1:]
    vals = ((1 - ss)**qf - 1) / ss
    return float(np.trapezoid(np.concatenate([[-qf], vals]), np.linspace(0, r1, 200001))) / (-qf)


def F_float(r1, nt=6000, nph=1600, betas=np.linspace(0, np.pi / 2, 91)):
    le_ = np.linspace(np.log(0.05), np.log(2000), nt + 1)
    te_ = np.exp(le_)
    tm_ = np.exp((le_[1:] + le_[:-1]) / 2)
    pm_ = (np.arange(nph) + 0.5) * (np.pi / 2 / nph)
    W_ = ((te_[1:]**(qf + 2) - te_[:-1]**(qf + 2)) / (qf + 2))[:, None] * (np.pi / 2 / nph)
    w_ = tm_[:, None] * np.exp(1j * pm_)[None, :]
    k_ = ((np.abs(1 - w_) > r1) / (1 - w_)**2 - 1 / (1 + w_)**2) / (4 * np.pi) - w_ / np.pi
    nr = (8 / np.pi) * 0.05**(qf + 5) / (qf + 5)
    tl = (4 / np.pi) * 2000**(qf + 3) / (-qf - 3)
    return np.array([2 * np.sum((np.abs((np.exp(-1j * b) * k_).real) + np.abs((np.exp(1j * b) * k_).real)) * W_)
                     + nr + tl for b in betas]), betas


rowsC = []
for r1 in (0.10, 0.13, 0.15, 0.17, 0.20, 0.25):
    Fb, bs = F_float(r1)
    Nf = N_float(r1)
    rowsC.append({"rho1": r1, "N": Nf, "supF": float(Fb.max()), "argmax_beta": float(bs[np.argmax(Fb)]),
                  "minF": float(Fb.min()), "E": (2 / np.pi) * Nf + (Fb.max() + 0.5) / (-qf)})
    print("(C) FLOAT rho1 = %.2f: N = %.5f, sup_beta F = %.5f at beta = %.4f, min_beta F = %.4f, E = %.5f"
          % (r1, Nf, Fb.max(), bs[np.argmax(Fb)], Fb.min(), rowsC[-1]["E"]))
OUT["C"] = rowsC
assert abs([rw for rw in rowsC if rw["rho1"] == 0.15][0]["E"] - E_up) < 0.08

# =============================== (D) FLOAT lower bounds from test functions ===============================
# g = sin(psi(phi)) |w|^q/(-q) with psi Lipschitz, |psi'| <= -q (A8: then |grad g| <= |w|^(q-1), |g| <= |w|^q/(-q)).
# The functional at e = 1 in the direction Re(e^{-i b} .): L = Re(e^{-i b} [-g(1)/2 + int_{|W|<rho1} f(-W) (g(1+W)
# - g(1)) dA + int k(w) g(w) dA]), f(-W) = 1/(2 pi W^2). Homogeneous g: the far part is int sigma(phi) Lam_b(phi) dphi.
r1D = 0.15
ntD, nphD = 12000, 3600
leD = np.linspace(np.log(1e-4), np.log(1e5), ntD + 1)
teD = np.exp(leD)
tmD = np.exp((leD[1:] + leD[:-1]) / 2)
WtD = (teD[1:]**(qf + 2) - teD[:-1]**(qf + 2)) / (qf + 2)          # int t^(q+1) dt per radial cell
phD = (np.arange(nphD) + 0.5) * (np.pi / nphD)                      # (0, pi); antiperiodic extension
dphD = np.pi / nphD


def Lam(b):
    out = np.zeros(nphD)
    for jj in range(0, nphD, 400):
        ww = tmD[:, None] * np.exp(1j * phD[jj:jj + 400])[None, :]
        kk = ((np.abs(1 - ww) > r1D) / (1 - ww)**2 - 1 / (1 + ww)**2) / (4 * np.pi) - ww / np.pi
        out[jj:jj + 400] = np.sum((np.exp(-1j * b) * kk).real * WtD[:, None], axis=0)
    return out


def near_part(sig_fun, b, ns=400, na=720):
    """int_{|W| < rho1} Re(e^{-i b} f(-W)) (g(1+W) - g(1)) dA for g = sig(arg) |w|^q (without the 1/(-q))."""
    sv = (np.arange(ns) + 0.5) * (r1D / ns)
    av = (np.arange(na) + 0.5) * (2 * np.pi / na)
    Wv = sv[:, None] * np.exp(1j * av)[None, :]
    z = 1 + Wv
    gz = sig_fun(np.angle(z)) * np.abs(z)**qf
    g1 = sig_fun(np.array([0.0]))[0]
    fw = 1 / (2 * np.pi * Wv**2)
    return float(np.sum((np.exp(-1j * b) * fw).real * (gz - g1) * sv[:, None]) * (r1D / ns) * (2 * np.pi / na))


def dp_best(Lv, b, psi0):
    """max over psi on the phi grid, psi(0+) near psi0, |dpsi| <= -q dphi, psi(pi) = -psi(0), of 2 sum sin(psi) Lv dphi."""
    step = -qf * dphD
    M = int(np.floor(np.pi / step)) + 1
    lv = -np.pi / 2 + step * np.arange(M)
    i0 = int(np.argmin(np.abs(lv - psi0)))
    iend = int(np.argmin(np.abs(lv + lv[i0])))
    val = np.full(M, -np.inf)
    val[i0] = 0.0
    back = np.zeros((nphD, M), dtype=np.int32)
    for jj in range(nphD):
        cand = np.stack([val, np.concatenate([[-np.inf], val[:-1]]), np.concatenate([val[1:], [-np.inf]])])
        arg_ = np.argmax(cand, axis=0)
        val = cand[arg_, np.arange(M)] + 2 * np.sin(lv) * Lv[jj] * dphD
        back[jj] = np.arange(M) - np.where(arg_ == 1, 1, np.where(arg_ == 2, -1, 0))
    path = np.zeros(nphD, dtype=np.int64)
    cur = iend
    for jj in range(nphD - 1, -1, -1):
        path[jj] = cur
        cur = back[jj][cur]
    return float(val[iend]), lv[path], lv[i0]


rowsD = []
for b in (0.0, 0.25, 0.5):
    Lv = Lam(b)
    for psi0 in (-np.pi / 2, np.pi / 2):
        far, psis, p0 = dp_best(Lv, b, psi0)
        sig_vals = np.sin(psis)

        def sig_fun(ang, sv_=sig_vals):
            ang = np.mod(ang, 2 * np.pi)
            sgn = np.where(ang < np.pi, 1.0, -1.0)
            idx = np.clip((np.mod(ang, np.pi) / dphD).astype(int), 0, nphD - 1)
            return sgn * sv_[idx]
        contact = -np.cos(b) * np.sin(p0) / 2
        nr_ = near_part(sig_fun, b)
        L = (far + contact + nr_) / (-qf)
        rowsD.append({"beta": b, "psi0": float(p0), "far": far, "contact": float(contact), "near": nr_, "L": float(L)})
        print("(D) FLOAT test, beta = %.2f, psi(0) = %+.4f: far %.5f, contact %+.5f, near %+.5f, value L = %.5f"
              % (b, p0, far, contact, nr_, L))
# simple closed-form tests: sigma = -cos(3 phi), -cos(phi) at beta = 0
for nm, sf in (("-cos 3phi", lambda a_: -np.cos(3 * a_)), ("-cos phi", lambda a_: -np.cos(a_))):
    Lv = Lam(0.0)
    far = float(2 * np.sum(sf(phD) * Lv) * dphD)
    contact = -sf(np.array([0.0]))[0] / 2
    nr_ = near_part(sf, 0.0)
    rowsD.append({"test": nm, "far": far, "contact": float(contact), "near": nr_, "L": (far + contact + nr_) / (-qf)})
    print("(D) FLOAT test sigma = %s at beta = 0: L = %.5f" % (nm, rowsD[-1]["L"]))
E_low = max(rw["L"] for rw in rowsD)
OUT["D"] = {"rho1_split": r1D, "rows": rowsD, "best_lower": E_low}
print("(D) best FLOAT lower value %.5f; Arb upper bound %.5f; ratio %.3f" % (E_low, E_up, E_up / E_low))

# =============================== (E) reach of (CI) ===============================
gA = 1 / cA
dA = 1 - gA
Dd = 1 - cA * (qA - dA)          # D_delta = 1 - c (q* - delta) = c (4 + delta), as in T4-351 and REVIEW_T4_335
pE = gA + 2                      # the leading stream r^p Psi, p = gamma + 2, Psi = sum b_n sin(n th)/(p^2 - n^2)
res335 = json.loads((HERE / "data/t4_335_review_results.json").read_text())
OUT["E"] = {}
budgets = {"scalar": 3.7930e-6, "graded": 4.5717e-4}
ep_sha = {"007": "bcd0e49225807ba313dfb86ec386b4d3d3411bdcb233072d5047e84cc27ec58b",
          "013": "3a2cf49c387db2fd95e7174a2b5f58103201857f01ba875e391b88714ab96471",
          "014": "8168bf8b326124bc720cc992a5fbe0300d9b1250eb9f4e862b0f2ce38b53b6ce"}
for name in ("007", "013", "014"):
    ep = json.loads((T4R / f"data/{name}_endpoint.json").read_text())
    assert sha(T4R / f"data/{name}_endpoint.json") == ep_sha[name]
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    tharb = {n: arb(v_.numerator) / v_.denominator for n, v_ in th0.items()}
    Glow = sum(n * b_ for n, b_ in tharb.items())                                   # Theta'(0) (T4-351)
    # |U_lead| at theta = 0: U = ((p - 1) Psi'(0), 0); at theta = pi/2: U = (0, -(p Psi + Psi'')(pi/2))
    Vx = (pE - 1) * abs(sum(n * b_ / (pE**2 - n * n) for n, b_ in tharb.items()))
    Vy = abs(sum(b_ * (pE - n * n) * (arb(n) / 2).sin_pi() / (pE**2 - n * n) for n, b_ in tharb.items()))
    Vlow = math.nextafter(max(float(Vx.lower()), float(Vy.lower())), -math.inf)      # outward (downward)
    m_, r_ = res335["C"][name]["d_over_4c"].strip("[] ").split("+/-")
    B4c = arb(m_.strip(), r_.strip())
    Hmin_new = aA * B4c / (2 * PI).sqrt()
    # FLOAT grid maxima of the leading profiles (lower bounds for G and V)
    thg = np.linspace(0, 2 * np.pi, 20001)
    bn = {n: float(v_) for n, v_ in th0.items()}
    gF = 1 / c
    pF = gF + 2
    Th = sum(b_ * np.sin(n * thg) for n, b_ in bn.items())
    dTh = sum(n * b_ * np.cos(n * thg) for n, b_ in bn.items())
    Gl = float(np.max(np.sqrt((gF * Th)**2 + dTh**2)))
    Ps = sum(b_ * np.sin(n * thg) / (pF**2 - n * n) for n, b_ in bn.items())
    dPs = sum(n * b_ * np.cos(n * thg) / (pF**2 - n * n) for n, b_ in bn.items())
    d2Ps = sum(-n * n * b_ * np.sin(n * thg) / (pF**2 - n * n) for n, b_ in bn.items())
    cc, sn = np.cos(thg), np.sin(thg)
    vr, vt, vrr, vrt, vtt = pF * Ps, dPs, pF * (pF - 1) * Ps, pF * dPs, d2Ps      # at r = 1
    vxx = cc * cc * vrr + sn * sn * (vr + vtt) - 2 * sn * cc * (vrt - vt)
    vxy = sn * cc * (vrr - vr - vtt) + (cc * cc - sn * sn) * (vrt - vt)
    Vl = float(np.max(np.sqrt(vxy**2 + vxx**2)))
    Vx_f = float(np.sqrt(vxy[0]**2 + vxx[0]**2))
    assert abs(Vx_f - float(Vx.mid())) < 1e-9 * max(1, Vx_f) and Gl >= float(Glow.lower()) - 1e-9
    dqF = 1 - 1 / c
    DdF = float(Dd.mid())
    B = float(B4c.mid())
    out = {"G_low_Theta'(0)": Glow.str(15), "G_lead_grid": Gl, "V_theta0_Arb": Vx.str(15), "V_thetapi2_Arb": Vy.str(15),
           "V_low_Arb": Vlow, "V_lead_grid": Vl,
           "H_min_T4_351": B / np.sqrt(2 * np.pi), "H_min_new": float(Hmin_new.mid()), "rows": []}

    def reach(E, V, G, hfac):
        rs = (hfac * (V + E * G) / DdF)**(1 / dqF)
        cap = B * rs**(qf + 1) / np.sqrt(-2 * qf - 2)
        a_ = -2 * qf - 2
        exact = B * rs**(qf + 1) * np.sqrt(1 / a_ - 2 / (a_ + dqF) + 1 / (a_ + 2 * dqF))
        return rs, cap, exact
    for lab, E, V, hfac in (("T4-351 as published: E_q*, V = 0, H >= B/sqrt(2pi)", 133.0042547837, 0.0, 1.0),
                            ("E_q*, V = 0, H >= (-q) B/sqrt(2pi)", 133.0042547837, 0.0, -qf),
                            ("T4-335 (2) with A5: (E_q* - 2^-q)/(-q) + 2^-q, V = 0, new H_min", None, 0.0, -qf),
                            ("E_new, V = 0, new H_min", E_up, 0.0, -qf),
                            ("E_new, V = max(|U_lead(0)|, |U_lead(pi/2)|), new H_min", E_up, Vlow, -qf),
                            ("E_new, V = V_lead (grid max), new H_min", E_up, Vl, -qf),
                            ("E_low (FLOAT), V = V_lead, new H_min", E_low, Vl, -qf)):
        if E is None:
            E = (133.0042547837 - 2**(-qf)) / (-qf) + 2**(-qf)
        rs, cap, exact = reach(E, V, Gl, hfac)
        out["rows"].append({"case": lab, "E": E, "V": V, "r_sep": rs, "beta_cap": cap, "rhs_at_Hmin_delta_term": exact,
                            "cap_above_scalar": cap > budgets["scalar"], "cap_above_graded": cap > budgets["graded"]})
    OUT["E"][name] = out
    print("(E) %s: G >= Theta'(0) = %s (grid max %.6f); |U_lead(0)| = %s, |U_lead(pi/2)| = %s, grid max %.6f;"
          " H_min %.2f -> %.2f" % (name, Glow.str(10), Gl, Vx.str(10), Vy.str(10), Vl, out["H_min_T4_351"],
                                   out["H_min_new"]))
    for rw in out["rows"]:
        print("    %-58s E = %9.5f: r_sep = %.5g, beta_cap = %.4g, (CI) at H_min with the delta term only = %.4g"
              % (rw["case"], rw["E"], rw["r_sep"], rw["beta_cap"], rw["rhs_at_Hmin_delta_term"]))
OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_335_sharpE_results.json").write_text(json.dumps(OUT, indent=1, default=str))
print("done, %.1f s" % (time.monotonic() - T0))
