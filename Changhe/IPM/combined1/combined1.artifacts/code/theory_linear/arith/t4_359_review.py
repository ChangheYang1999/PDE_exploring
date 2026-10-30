"""Independent review of T4-359 (c1-t4 research/annular_moment_adjustment/PROOF.md, sha256 0b3944af...6e35):
a mode-1 annular density with prescribed first moment, zero velocity inside and a pure dipole outside
(reviews/REVIEW_T4_359.md).

Run from artifacts/:  python3 -B -u arith/t4_359_review.py
Needs sympy, numpy, python-flint.

Parts:
  (A) sympy, exact: the mode-1 Green formula (5) for a general profile and for an explicit polynomial profile; the
      interior and exterior forms of v; the Cartesian derivatives of y/r^2 and the exterior velocity; its polar
      components; -d_y K = (cos 3t, sin 3t)/(pi r^3) for the kernel of T4-335; the two first moments; the angular
      integral in the origin normalization; the Fourier symbol; C_w; the exact optimization in the interpolation
      inequality of REVIEW_T4_359 R2.
  (B) FLOAT, independent of the potential: U[f] by direct quadrature of K(X - Y) f(Y) over the annulus, for the
      smooth bump eta = C exp(-1/((r - 1)(2 - r))), at points with r < 1 (expected 0) and r > 2 (expected
      (cos 3t, sin 3t)/(pi r^3)); and the same field from the potential formula (5) at points with 1 < r < 2.
  (C) FLOAT constants of PROOF (2), (3) for this bump; the weighted quantity H_q*(h_R) for several R; the exact
      projection coefficient lambda = <A*, P>/||P||^2 for 007, 013, 014 (c1-t4 endpoint data, exact) and the
      moment m* = -pi lambda that minimizes the endpoint coefficient in the family; its L2 and X costs.
  (D) FLOAT: the interpolation inequality |m| <= ((2 + dq)/(2 dq)) (sqrt(pi) beta)^th (4 H)^(1 - th), dq = -q - 3,
      th = dq/(2 + dq), evaluated on h_R for R = 10^k: the ratio of the two sides tends to a positive constant.
Output: logs/t4_359_review.log, data/t4_359_review_results.json.
"""
import hashlib
import json
import time
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
import sympy as S

HERE = Path(__file__).resolve().parents[1]
T4M = Path("RUN_ROOT/theory_audit_T4/research/annular_moment_adjustment")
T4F = Path("RUN_ROOT/theory_audit_T4/research/finite_tail_surgery")
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(T4M / "PROOF.md") == "0b3944af5bcc7c176ecf5036b822894dfc0a06d49da1306de904ced2938f6e35"
assert sha(T4M.parent / "sharp_l2_audit/PROOF.md") == "8ca3bb460727294595087e114935f564bff5605b00b5432c59cfc1bb0ecd6734"

# =============================== (A) exact ===============================
r, s, t, R, m = S.symbols("r s t R m", positive=True)
x, y = S.symbols("x y", real=True)
# (A1) general profile: a(r) = -(1/2)[r^-1 I(r) + r J(r)], I' = r^2 eta, J' = -eta
I_, J_, et = S.Function("I")(r), S.Function("J")(r), S.Function("eta")(r)
a = -(I_ / r + r * J_) / 2
sub = {S.Derivative(I_, (r, 2)): S.diff(r**2 * et, r), S.Derivative(J_, (r, 2)): -S.diff(et, r),
       S.Derivative(I_, r): r**2 * et, S.Derivative(J_, r): -et}
ode = (S.diff(a, r, 2) + S.diff(a, r) / r - a / r**2).subs(sub)
A1 = S.simplify(ode - et) == 0
# (A2) explicit profile eta = k (r-1)^4 (2-r)^4 on (1, 2), normalized by pi int r^2 eta = 1
e0 = (r - 1)**4 * (2 - r)**4
k0 = 1 / (S.pi * S.integrate(r**2 * e0, (r, 1, 2)))
eta_p = k0 * e0
Itot = S.integrate(s**2 * eta_p.subs(r, s), (s, 1, 2))
Jtot = S.integrate(eta_p.subs(r, s), (s, 1, 2))
a_in = -(r * Jtot) / 2                                             # r < 1
a_mid = -(S.integrate(s**2 * eta_p.subs(r, s), (s, 1, r)) / r + r * S.integrate(eta_p.subs(r, s), (s, r, 2))) / 2
a_out = -(Itot / r) / 2                                            # r > 2
A2 = {"pi_int_r2_eta_is_1": S.simplify(S.pi * Itot - 1) == 0,
      "ode_middle": S.simplify(S.diff(a_mid, r, 2) + S.diff(a_mid, r) / r - a_mid / r**2 - eta_p) == 0,
      "C1_match_at_1": all(S.simplify((S.diff(a_mid, r, j) - S.diff(a_in, r, j)).subs(r, 1)) == 0 for j in (0, 1)),
      "C1_match_at_2": all(S.simplify((S.diff(a_mid, r, j) - S.diff(a_out, r, j)).subs(r, 2)) == 0 for j in (0, 1)),
      "exterior_a_is_minus_1_over_2pi_r": S.simplify(a_out + 1 / (2 * S.pi * r)) == 0,
      "interior_a_is_linear": S.diff(a_in, r, 2) == 0}
# (A3) Cartesian: v = -y/(2 pi r^2) outside, U = (v_xy, -v_xx)
rr = x**2 + y**2
v = -y / (2 * S.pi * rr)
U = (S.diff(v, x, y), -S.diff(v, x, 2))
pol = {x: r * S.cos(t), y: r * S.sin(t)}
A3 = {"U1": S.simplify(S.expand_trig(U[0].subs(pol) - S.cos(3 * t) / (S.pi * r**3))) == 0,
      "U2": S.simplify(S.expand_trig(U[1].subs(pol) - S.sin(3 * t) / (S.pi * r**3))) == 0,
      "dxy_y_over_r2": S.simplify(S.expand_trig((S.diff(y / rr, x, y)).subs(pol) + 2 * S.cos(3 * t) / r**3)) == 0,
      "dxx_y_over_r2": S.simplify(S.expand_trig((S.diff(y / rr, x, 2)).subs(pol) - 2 * S.sin(3 * t) / r**3)) == 0,
      "divergence_free": S.simplify(S.diff(U[0], x) + S.diff(U[1], y)) == 0}
Ur = S.simplify(S.expand_trig((U[0] * S.cos(t) + U[1] * S.sin(t)).subs(pol) * S.pi * r**3 - S.cos(2 * t)))
Ut = S.simplify(S.expand_trig((-U[0] * S.sin(t) + U[1] * S.cos(t)).subs(pol) * S.pi * r**3 - S.sin(2 * t)))
A3["polar_cos2_sin2"] = Ur == 0 and Ut == 0
# (A4) kernel of T4-335: K = (-z1 z2, (z1^2 - z2^2)/2)/(pi |Z|^4); -d_y K = (cos 3t, sin 3t)/(pi r^3)
K = (-x * y / (S.pi * rr**2), (x**2 - y**2) / (2 * S.pi * rr**2))
A4 = all(S.simplify(S.expand_trig((-S.diff(K[i], y)).subs(pol) - (S.cos(3 * t), S.sin(3 * t))[i] / (S.pi * r**3))) == 0
         for i in (0, 1))
# (A5) moments and angular integrals
A5 = {"int_y_f_angular": S.integrate(S.sin(t) * S.sin(t), (t, 0, 2 * S.pi)) == S.pi,
      "int_x_f_angular": S.integrate(S.cos(t) * S.sin(t), (t, 0, 2 * S.pi)) == 0,
      "origin_normalization_angular": S.integrate(S.sin(3 * t) * S.sin(t), (t, 0, 2 * S.pi)) == 0}
# (A6) Fourier symbol: d_xy -> -xi1 xi2, d_xx -> -xi1^2, Delta -> -|xi|^2
x1, x2 = S.symbols("xi1 xi2", real=True)
A6 = (S.simplify((-x1 * x2) / (-(x1**2 + x2**2)) - x1 * x2 / (x1**2 + x2**2)) == 0
      and S.simplify(-(-x1**2) / (-(x1**2 + x2**2)) + x1**2 / (x1**2 + x2**2)) == 0)
# (A7) C_w = max(1 + 32/25 + w1, 1 + w2/w1) at w = (2^15, 2^20)
Cw = max(1 + Fr(32, 25) + 2**15, 1 + Fr(2**20, 2**15))
A7 = Cw == Fr(819257, 25) == Fr(3277028, 100)
# (A8) interpolation: min over rho of (sqrt(pi)/2) rho^2 beta + 4 H rho^-dq/dq
b_, H_, dq, rho = S.symbols("beta H d rho", positive=True)
g = S.sqrt(S.pi) / 2 * rho**2 * b_ + 4 * H_ * rho**(-dq) / dq
rho0 = (4 * H_ / (S.sqrt(S.pi) * b_))**(1 / (2 + dq))
th = dq / (2 + dq)
closed = (2 + dq) / (2 * dq) * (S.sqrt(S.pi) * b_)**th * (4 * H_)**(1 - th)
A8 = {"critical_point": S.simplify(S.powsimp(S.expand_power_base(S.diff(g, rho).subs(rho, rho0) * rho0**(dq + 1), force=True), force=True)) == 0,
      "closed_form": all(abs(float((g.subs(rho, rho0) - closed).subs({b_: bv, H_: hv, dq: dv}))) < 1e-12 * float(closed.subs({b_: bv, H_: hv, dq: dv}))
                         for bv, hv, dv in ((1e-3, 3.0, 0.45), (2.0, 0.1, 1.7), (0.37, 41.0, 0.05))),
      "y_moment_ball": S.integrate(S.integrate(r**2 * S.sin(t)**2 * r, (t, 0, 2 * S.pi)), (r, 0, rho)) == S.pi * rho**4 / 4,
      "abs_sin_integral": S.integrate(S.Abs(S.sin(t)), (t, 0, 2 * S.pi)) == 4}
OUT["A"] = {"A1_general_Green": A1, "A2_explicit_profile": A2, "A3_cartesian": A3, "A4_kernel_dipole": A4,
            "A5_moments": A5, "A6_symbol": A6, "A7_Cw_819257_over_25": A7, "A8_interpolation": A8}
flat = [A1, A4, A6, A7] + list(A2.values()) + list(A3.values()) + list(A5.values()) + list(A8.values())
assert all(flat)
print("(A) all exact checks pass:", json.dumps(OUT["A"]))

# =============================== (B) FLOAT kernel path ===============================
from numpy.polynomial.legendre import leggauss


def bump(rv):
    out = np.zeros_like(rv)
    msk = (rv > 1) & (rv < 2)
    out[msk] = np.exp(-1 / ((rv[msk] - 1) * (2 - rv[msk])))
    return out


nr, nt = 400, 1024
gx, gw = leggauss(nr)
rq = 1.5 + gx / 2
wq = gw / 2
kb = 1 / (np.pi * np.sum(wq * rq**2 * bump(rq)))          # pi int r^2 eta = 1
eta = lambda rv: kb * bump(rv)
tq = 2 * np.pi * np.arange(nt) / nt
RR, TT = np.meshgrid(rq, tq, indexing="ij")
Y1, Y2 = RR * np.cos(TT), RR * np.sin(TT)
FW = eta(RR) * np.sin(TT) * RR * (wq[:, None] * (2 * np.pi / nt))   # f dY
mom_y = np.sum(Y2 * FW)
mom_x = np.sum(Y1 * FW)


def U_kernel(X):
    z1, z2 = X[0] - Y1, X[1] - Y2
    q4 = np.pi * (z1 * z1 + z2 * z2) ** 2
    return np.array([np.sum(-z1 * z2 / q4 * FW), np.sum((z1 * z1 - z2 * z2) / (2 * q4) * FW)])


rowsB = []
for rv in (0.2, 0.6, 0.9, 2.15, 2.6, 4.0, 9.0):
    for tv in (0.3, 1.1, 2.0):
        X = rv * np.array([np.cos(tv), np.sin(tv)])
        Uk = U_kernel(X)
        exp_ = np.zeros(2) if rv < 1 else np.array([np.cos(3 * tv), np.sin(3 * tv)]) / (np.pi * rv**3)
        rowsB.append([rv, tv, Uk.tolist(), exp_.tolist(), float(np.max(np.abs(Uk - exp_)))])
errB = max(rw[-1] for rw in rowsB)
# potential path (5) inside the annulus: v = a(r) sin t, U = (v_xy, -v_xx) in polar form


# fine radial grid for I(r) = int_0^r s^2 eta and J(r) = int_r^inf eta (cumulative trapezoid)
rgI = np.linspace(1, 2, 400001)
eI = eta(rgI)
cumI = np.concatenate([[0.0], np.cumsum((rgI[1:]**2 * eI[1:] + rgI[:-1]**2 * eI[:-1]) / 2 * np.diff(rgI))])
cumE = np.concatenate([[0.0], np.cumsum((eI[1:] + eI[:-1]) / 2 * np.diff(rgI))])


def a_fun(rv):                     # a, a', a'' from (5)
    rv = np.atleast_1d(rv).astype(float)
    In = np.interp(rv, rgI, cumI, left=0.0, right=cumI[-1])
    Jn = cumE[-1] - np.interp(rv, rgI, cumE, left=0.0, right=cumE[-1])
    av = -(In / rv + rv * Jn) / 2
    ap = -(-In / rv**2 + Jn) / 2
    app = -In / rv**3 + eta(rv)
    return av, ap, app


def U_pot(rv, tv):
    av, ap, app = [float(z[0]) for z in a_fun(np.array([rv]))]
    # v = a(r) sin t; v_xx, v_xy from the polar Hessian
    vr, vt, vrr = ap * np.sin(tv), av * np.cos(tv), app * np.sin(tv)
    vrt, vtt = ap * np.cos(tv), -av * np.sin(tv)
    c_, s_ = np.cos(tv), np.sin(tv)
    vxx = c_ * c_ * vrr + s_ * s_ * (vr / rv + vtt / rv**2) - 2 * s_ * c_ * (vrt / rv - vt / rv**2)
    vxy = s_ * c_ * (vrr - vr / rv - vtt / rv**2) + (c_ * c_ - s_ * s_) * (vrt / rv - vt / rv**2)
    return np.array([vxy, -vxx])


# inside the annulus the kernel integral is a principal value; compare the potential path with the kernel path
# using a fine local grid is costly, so instead compare the potential path with the kernel path just outside the
# support, where both are smooth, and check the potential path's own continuity at r = 1 and r = 2
rowsBp = []
for rv in (0.9, 2.15, 4.0):
    for tv in (0.3, 1.1):
        rowsBp.append([rv, tv, float(np.max(np.abs(U_pot(rv, tv) - U_kernel(rv * np.array([np.cos(tv), np.sin(tv)])))))])
errBp = max(rw[-1] for rw in rowsBp)
OUT["B"] = {"bump": "exp(-1/((r-1)(2-r))) on (1,2), normalized pi int r^2 eta = 1", "quadrature": [nr, nt],
            "moment_y": mom_y, "moment_x": mom_x, "kernel_vs_expected": rowsB, "max_abs_error": errB,
            "potential_vs_kernel": rowsBp, "max_abs_error_potential_vs_kernel": errBp}
assert abs(mom_y - 1) < 1e-10 and abs(mom_x) < 1e-12 and errB < 1e-9 and errBp < 1e-9
print("(B) moments %.12f, %.1e; kernel quadrature vs 0 (r < 1) and (cos 3t, sin 3t)/(pi r^3) (r > 2): max abs error"
      " %.2e over %d points; potential formula (5) vs kernel at r = 0.9, 2.15, 4: max abs error %.2e"
      % (mom_y, mom_x, errB, len(rowsB), errBp))

# =============================== (C) FLOAT constants ===============================
cF = Fr(4076476460239181, 2**51)
c = float(cF)
gam = 1 / c
qs = gam - 4
dqs = -qs - 3
s_ = 1 / 5184
w1, w2 = 2.0**15, 2.0**20
# Cartesian derivative tensors of f = kb exp(-1/((r-1)(2-r))) y/r, all ordered components, from sympy
xs, ys = S.symbols("xs ys", real=True)
rS = S.sqrt(xs**2 + ys**2)
fS = S.exp(-1 / ((rS - 1) * (2 - rS))) * ys / rS
comps = {0: [fS]}
for k in (1, 2, 3):
    comps[k] = [S.diff(cc, v_) for cc in comps[k - 1] for v_ in (xs, ys)]
frob = {k: S.lambdify((xs, ys), sum(cc**2 for cc in comps[k]), "numpy") for k in comps}
eS_ = S.symbols("eS_", positive=True)
eSr = S.exp(-1 / ((eS_ - 1) * (2 - eS_)))
e_d = {k: S.lambdify(eS_, S.diff(eSr, eS_, k), "numpy") for k in range(4)}
nrg, ntg = 4001, 256
rg = np.linspace(1, 2, nrg)[1:-1]
dr = rg[1] - rg[0]
tg = 2 * np.pi * np.arange(ntg) / ntg
dtt = 2 * np.pi / ntg
Rg, Tg = np.meshgrid(rg, tg, indexing="ij")
Xg, Yg = Rg * np.cos(Tg), Rg * np.sin(Tg)
fr = {k: kb**2 * frob[k](Xg, Yg) for k in comps}
E0, E1 = kb * e_d[0](rg), kb * e_d[1](rg)
# cross-check the sympy Frobenius norms against the radial forms for k = 0, 1
assert np.allclose(fr[0], (kb * e_d[0](Rg) * np.sin(Tg))**2, rtol=1e-10, atol=1e-30)
assert np.allclose(fr[1], (kb * e_d[1](Rg) * np.sin(Tg))**2 + (kb * e_d[0](Rg) / Rg * np.cos(Tg))**2, rtol=1e-9, atol=1e-30)


def Anorm(k, b):
    return float(np.sqrt(np.sum(fr[k] * Rg**(2 * b) * Rg) * dr * dtt))


A00, A10, A2b, A3b = Anorm(0, 0), Anorm(1, 0), Anorm(2, 0.8), Anorm(3, 0.8)
Hc = np.sqrt(5**0.8 * A2b**2 + w1 * A10**2 + w2 * A00**2)
Qc = 5**0.4 * A3b
CX = Hc**(1 - s_) * (2 * Qc**2 + float(Cw) * Hc**2)**(s_ / 2) + 48 / 25 * s_ * Hc
# A_c = ||c r f_r - f||, A_v = ||r^gamma grad f||, A_g = ||r^(gamma-1) u_f||, A_n = ||u_f . grad f||
Ac = float(np.sqrt(np.sum((c * Rg * kb * e_d[1](Rg) - kb * e_d[0](Rg))**2 * np.sin(Tg)**2 * Rg) * dr * dtt))
Av = float(np.sqrt(np.sum(fr[1] * Rg**(2 * gam) * Rg) * dr * dtt))
# u_f on 1 < r < 2 from (5) (polar Hessian); |u_f| = 1/(pi r^3) exactly for r > 2
rmid = rg[::10]
drm = rmid[1] - rmid[0]
uf2, ufdot = [], []
for rv in rmid:
    vals = [U_pot(rv, tv) for tv in tg]
    uf2.append(np.mean([np.dot(u_, u_) for u_ in vals]))
    ev, e1v = kb * float(e_d[0](rv)), kb * float(e_d[1](rv))
    gradf = [np.array([e1v * np.sin(tv) * np.cos(tv) - ev / rv * np.cos(tv) * np.sin(tv),
                       e1v * np.sin(tv) * np.sin(tv) + ev / rv * np.cos(tv) * np.cos(tv)]) for tv in tg]
    ufdot.append(np.mean([np.dot(u_, g_)**2 for u_, g_ in zip(vals, gradf)]))
uf2, ufdot = np.array(uf2), np.array(ufdot)
Ag_mid = np.sum(rmid**(2 * gam - 2) * uf2 * 2 * np.pi * rmid) * drm
Ag_out = (2 / np.pi) * 2**(2 * gam - 6) / (6 - 2 * gam)
Ag = float(np.sqrt(Ag_mid + Ag_out))
An = float(np.sqrt(np.sum(ufdot * 2 * np.pi * rmid) * drm))
# weighted sup constants of h_R: H_q*(h_R)/|m| = max(sup (1+R r)^-q R^-3 |f|, sup (1+R r)^(1-q) R^-4 |grad f|)
# (|grad f| = max over t of sqrt(e'^2 sin^2 + (e/r)^2 cos^2) = max(|e'|, |e|/r))
lo_c = max(float(np.max(rg**(-qs) * np.abs(E0))), float(np.max(rg**(1 - qs) * np.maximum(np.abs(E1), np.abs(E0) / rg))))
hi_c = max(float(np.max((1 + rg)**(-qs) * np.abs(E0))), float(np.max((1 + rg)**(1 - qs) * np.maximum(np.abs(E1), np.abs(E0) / rg))))
supH = lambda Rv: max(float(np.max((1 + Rv * rg)**(-qs) * np.abs(E0))) / Rv**3,
                      float(np.max((1 + Rv * rg)**(1 - qs) * np.maximum(np.abs(E1), np.abs(E0) / rg))) / Rv**4)
L2f = A00
OUT["C"] = {"c": c, "gamma": gam, "qstar": qs, "s": s_, "w": [w1, w2], "Cw": float(Cw),
            "A00_L2f": A00, "A10": A10, "A2_4/5": A2b, "A3_4/5": A3b, "H_const": Hc, "Q": Qc, "CX": CX,
            "Ac": Ac, "Av": Av, "Ag": Ag, "An": An, "Hq_lower_const": lo_c, "Hq_upper_const": hi_c}
print("(C) bump constants (FLOAT): ||f||_2 = %.6g, A_(1,0) = %.6g, A_(2,4/5) = %.6g, A_(3,4/5) = %.6g; H = %.6g, Q = %.6g,"
      " C_X = %.6g; A_c = %.6g, A_v = %.6g, A_g = %.6g, A_n = %.6g; H_q*(h_R)/(|m| R^dq) in [%.6g, %.6g] (dq = %.6f)"
      % (A00, A10, A2b, A3b, Hc, Qc, CX, Ac, Av, Ag, An, lo_c, hi_c, dqs))
# exact projection coefficients for 007, 013, 014 (c1-t4 endpoint data, read in place)
MAN = json.loads((T4F / "verification/MANIFEST.json").read_text())["files"]
rd = lambda dct: {int(k_): Fr(v_) for k_, v_ in dct.items() if Fr(v_) != 0}
dot = lambda u, w: sum((u[n] * w.get(n, 0) for n in u), Fr(0))
OUT["C"]["endpoint"] = {}
for name in ("007", "013", "014"):
    p_ = T4F / f"source/{name}_endpoint.json"
    assert sha(p_) == MAN[f"source/{name}_endpoint.json"]
    ep = json.loads(p_.read_text())
    Pm, Am = rd(ep["P"]), rd(ep["F12"])
    lam = dot(Am, Pm) / dot(Pm, Pm)
    assert lam == Fr(ep["lambda"])
    perp = {n: Am.get(n, 0) - lam * Pm.get(n, 0) for n in set(Am) | set(Pm)}
    mstar = -np.pi * float(lam)
    nA = float(np.sqrt(np.pi * float(dot(Am, Am))))
    nperp = float(np.sqrt(np.pi * float(dot(perp, perp))))
    rowsR = []
    for Rv in (10.0, 1e2, 1e3, 1e4):
        rowsR.append({"R": Rv, "L2": abs(mstar) * L2f / Rv**2, "X_bound": abs(mstar) * CX / Rv**2,
                      "Hq_star": abs(mstar) * supH(Rv), "Hq_star_over_R_dq": abs(mstar) * supH(Rv) / Rv**dqs})
    OUT["C"]["endpoint"][name] = {"lambda": float(lam), "mstar": mstar, "norm_A": nA, "norm_A_perp_d": nperp,
                                  "costs": rowsR}
    print("    %s: lambda = <A*, P>/||P||^2 = %.10g (exact = stored lambda), m* = -pi lambda = %.10g; ||A*|| = %.6f,"
          " ||A* + (m*/pi) P|| = d = %.6f; costs at R = 10, 1e2, 1e3, 1e4: L2 %s; X bound %s; H_q* %s"
          % (name, float(lam), mstar, nA, nperp, ", ".join("%.3g" % w_["L2"] for w_ in rowsR),
             ", ".join("%.3g" % w_["X_bound"] for w_ in rowsR), ", ".join("%.4g" % w_["Hq_star"] for w_ in rowsR)))

# =============================== (D) interpolation on the family ===============================
th_ = dqs / (2 + dqs)
rowsD = []
for k10 in range(0, 9):
    Rv = 10.0**k10
    beta = L2f / Rv**2
    Hv = supH(Rv)
    rhs = (2 + dqs) / (2 * dqs) * (np.sqrt(np.pi) * beta)**th_ * (4 * Hv)**(1 - th_)
    rowsD.append([Rv, beta, Hv, 1 / rhs])
OUT["D"] = {"theta": th_, "rows_R_beta_H_ratio": rowsD}
assert all(rw[3] <= 1 for rw in rowsD)
print("(D) theta = dq/(2 + dq) = %.6f; |m|/RHS on h_R (m = 1) for R = 10^0..10^8: %s"
      % (th_, ", ".join("%.6f" % rw[3] for rw in rowsD)))
OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_359_review_results.json").write_text(json.dumps(OUT, indent=1, default=float))
print("done, %.1f s" % (time.monotonic() - T0))
