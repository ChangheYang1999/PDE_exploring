"""Independent review of T4-335 (c1-t4 research/moment_resolved_tail/PROOF.md, sha256 99aa80a9...eead6df): the
moment-resolved velocity bound (1)-(2), the endpoint forced-tail theorem (6)-(7), the moment compatibility (8)-(9) and
the exact angular data of Section 4 (reviews/REVIEW_T4_335.md).

Run from artifacts/:  python3 -B -u arith/t4_335_review.py
Needs sympy, mpmath, python-flint, numpy.

Parts:
  (A) sympy: the kernel K and its complex form 1/(2 pi z^2); |K|, |K'|, |K'''|; the Taylor remainder constant; the
      five region integrals of Section 1 as functions of q; -d_y K and its polar components; the pairing with the
      leading gradient; the dipole velocity rederived from the mode-1 potential (no kernel used); the radial
      integration of Section 2; the moment bound of remark R2.
  (B) arb: E_q at q* = gamma - 4 (six terms), epsilon = 9 delta - 4, the denominators of (7), the moment constant.
  (C) exact (fmpq/Fraction): for 007, 013, 014, my constructor (prefix of arith/t4_294_review.py) on the raw c1-n1
      generator files: Theta_(1,0), Theta_(1,2), F_(1,2), P, the projection coefficient, d^2 > 0, the determinant
      certificate; arb enclosures of d and d/(4c) against c1-t4's verification/result.json.
  (D) FLOAT: a test of (1) for h = y (1 + r^2)^-p + a3 Im(z^3) (1 + r^2)^(-p-1) at q = q*, with U[h] computed from
      the mode potentials (Green's function of each angular mode, mpmath quadrature), not from the kernel.
  (E) FLOAT, remark R3: H_min = d/(4c sqrt(2 pi)), G_lead from Theta_(1,0), and the radius r_sep beyond which (7) can
      separate the forced tail, with the L2(R2) mass beyond it, for E = E_q*, 10, 1, 1/2.
Output: logs/t4_335_review.log, data/t4_335_review_results.json.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from flint import arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 400
HERE = Path(__file__).resolve().parents[1]
T4R = Path("RUN_ROOT/theory_audit_T4/research/moment_resolved_tail")
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(T4R / "PROOF.md") == "99aa80a9b5ce0474e26c8a53e53218b2b1bb628f0283eab5eb62b4aeefead6df"
assert sha(T4R / "DOMAIN_ADDENDUM.md") == "ae54aec0c3bc9dcaca2995e0534126df3af4bbc0150a4231b75f388168a3afd2"

# =============================== (A) sympy ===============================
x, y = sp.symbols("x y", real=True)
r, t, s, rho = sp.symbols("r t s rho", positive=True)
q, m, c, H = sp.symbols("q m c H", real=True)
zz = x + sp.I * y
K1 = -x * y / (sp.pi * (x**2 + y**2) ** 2)
K2 = (x**2 - y**2) / (2 * sp.pi * (x**2 + y**2) ** 2)
# (A1) K2 + i K1 = 1/(2 pi z^2); |K| = 1/(2 pi |Z|^2); zero angular mean of both components
assert sp.simplify(K2 + sp.I * K1 - 1 / (2 * sp.pi * zz**2)) == 0
assert sp.simplify(K1**2 + K2**2 - 1 / (4 * sp.pi**2 * (x**2 + y**2) ** 2)) == 0
polar = {x: r * sp.cos(t), y: r * sp.sin(t)}
for Kc in (K1, K2):
    assert sp.simplify(sp.integrate(sp.simplify(Kc.subs(polar)), (t, 0, 2 * sp.pi))) == 0
# kernel = second derivatives of the log potential: d1 d2 (log r/(2 pi)) = K1-type, -d1^2 (log r/(2 pi)) = K2-type
lg = sp.log(x**2 + y**2) / (4 * sp.pi)
assert sp.simplify(sp.diff(lg, x, y) - K1) == 0 and sp.simplify(-sp.diff(lg, x, 2) - K2) == 0
w = sp.symbols("w")
f = 1 / (2 * sp.pi * w**2)
assert sp.simplify(sp.diff(f, w, 3) + 12 / (sp.pi * w**5)) == 0          # |K'''| = 12/(pi |z|^5)
assert sp.simplify(sp.diff(f, w) + 1 / (sp.pi * w**3)) == 0              # |K'| = 1/(pi |z|^3)
taylor_const = sp.Rational(1, 6) * 12 / (sp.pi * (r / 2) ** 5)
assert sp.simplify(taylor_const - 64 / (sp.pi * r**5)) == 0
print("(A1) K2 + i K1 = 1/(2 pi z^2), |K| = 1/(2 pi |Z|^2), zero angular means, K = (d1 d2, -d1^2)(log|X|/(2 pi)),"
      " |K'| = 1/(pi |z|^3), |K'''| = 12/(pi |z|^5), Taylor remainder 64/(pi r^5) |Y|^3")
# (A2) region integrals, -5 < q < -3 (checked at q = -7/2 symbolically and as functions of q for r > 0)
qq = sp.Rational(-7, 2)
I_ball = sp.integrate(1 / (2 * sp.pi * rho) * 2 * sp.pi * rho, (rho, 0, r / 2))
assert sp.simplify(I_ball - r / 2) == 0
terms = {}
terms["B(X,r/2)"] = (r / 2) ** (q - 1) * (r / 2)
terms["rest |Y|<=2r"] = 2 / (sp.pi * r**2) * (r / 2) ** q * 4 * sp.pi * r**2
far = (2 / sp.pi) * 2 * sp.pi * sp.integrate(rho ** (qq - 1), (rho, 2 * r, sp.oo))
assert sp.simplify(far - 2 ** (qq + 2) * r**qq / (-qq)) == 0
terms["|Y|>2r"] = 2 ** (q + 2) * r**q / (-q)
mom = 1 / (sp.pi * r**3) * 2 * sp.pi * sp.integrate(rho ** (qq + 2), (rho, r / 2, sp.oo))
assert sp.simplify(mom - 2 ** (-qq - 2) * r**qq / (-qq - 3)) == 0
terms["moment tail"] = 2 ** (-q - 2) * r**q / (-q - 3)
tay = 64 / (sp.pi * r**5) * 2 * sp.pi * sp.integrate(rho ** (qq + 4), (rho, 0, r / 2))
assert sp.simplify(tay - 2 ** (2 - qq) * r**qq / (qq + 5)) == 0
terms["Taylor remainder"] = 2 ** (2 - q) * r**q / (q + 5)
expect = {"B(X,r/2)": 2 ** (-q), "rest |Y|<=2r": 2 ** (3 - q), "|Y|>2r": 2 ** (q + 2) / (-q),
          "moment tail": 2 ** (-q - 2) / (-q - 3), "Taylor remainder": 2 ** (2 - q) / (q + 5)}
for k_, v in terms.items():
    assert sp.simplify(sp.powsimp(sp.expand_power_base(v / r**q, force=True), force=True) - expect[k_]) == 0, k_
print("(A2) the five region terms over H r^q are 2^-q, 2^(3-q), 2^(q+2)/(-q), 2^(-q-2)/(-q-3), 2^(2-q)/(q+5)"
      " (symbolic in q; the integrals at q = -7/2); with the contact term 1/2 this is E_q of (2)")
# (A3) -d_y K = (cos 3t, sin 3t)/(pi r^3); radial and angular components; pairing with the leading gradient
dyK = [sp.simplify((-sp.diff(Kc, y)).subs(polar)) for Kc in (K1, K2)]
assert sp.simplify(dyK[0] - sp.cos(3 * t) / (sp.pi * r**3)) == 0
assert sp.simplify(dyK[1] - sp.sin(3 * t) / (sp.pi * r**3)) == 0
er, et = (sp.cos(t), sp.sin(t)), (-sp.sin(t), sp.cos(t))
rad = sp.simplify(dyK[0] * er[0] + dyK[1] * er[1])
ang = sp.simplify(dyK[0] * et[0] + dyK[1] * et[1])
assert sp.simplify(rad - sp.cos(2 * t) / (sp.pi * r**3)) == 0 and sp.simplify(ang - sp.sin(2 * t) / (sp.pi * r**3)) == 0
gam = sp.symbols("gamma", positive=True)
Th = sp.Function("Theta")(t)
pair = m * (rad * gam * Th + ang * sp.diff(Th, t)) * r ** (gam - 1)
P_def = gam * sp.cos(2 * t) * Th + sp.sin(2 * t) * sp.diff(Th, t)
assert sp.simplify(pair - (m / sp.pi) * r ** (gam - 4) * P_def) == 0
print("(A3) -d_y K = (cos 3t, sin 3t)/(pi r^3), radial cos 2t/(pi r^3), angular sin 2t/(pi r^3); the dipole m(...)"
      " paired with r^(gamma-1)(gamma Theta e_r + Theta' e_t) is (m/pi) r^(gamma-4) P")
# (A4) independent path: the exterior mode-1 potential. For h = f(r) sin t with m = int y h = pi int r^2 f dr, the
# solution of Lap phi = h on mode 1 is phi(r) sin t, phi = -(1/2)[r^-1 int_0^r s^2 f + r int_r^inf f], so outside the
# support phi = -(m/(2 pi)) r^-1. With U = (d1 d2, -d1^2) Lap^-1 h (multiplier (xi1 xi2, -xi1^2)/|xi|^2):
Phi = -(m / (2 * sp.pi)) * y / (x**2 + y**2)
U1, U2 = sp.diff(Phi, x, y), -sp.diff(Phi, x, 2)
assert sp.simplify(U1.subs(polar) - (m / sp.pi) * sp.cos(3 * t) / r**3) == 0
assert sp.simplify(U2.subs(polar) - (m / sp.pi) * sp.sin(3 * t) / r**3) == 0
xi1, xi2 = sp.symbols("xi1 xi2", real=True)
sym_U = [(sp.I * xi1) * (sp.I * xi2) * (-1 / (xi1**2 + xi2**2)), -((sp.I * xi1) ** 2) * (-1 / (xi1**2 + xi2**2))]
assert sp.simplify(sym_U[0] - xi1 * xi2 / (xi1**2 + xi2**2)) == 0 and sp.simplify(sym_U[1] + xi1**2 / (xi1**2 + xi2**2)) == 0
fF = sp.Function("f")
nn = sp.symbols("n", positive=True, integer=True)
phin = -(1 / (2 * nn)) * (r ** (-nn) * sp.Integral(s ** (nn + 1) * fF(s), (s, 0, r))
                          + r**nn * sp.Integral(s ** (1 - nn) * fF(s), (s, r, sp.oo)))
ode = sp.diff(phin, r, 2) + sp.diff(phin, r) / r - nn**2 * phin / r**2 - fF(r)
assert sp.simplify(ode.doit()) == 0
print("(A4) potential path: Phi = -(m/(2 pi)) y/r^2 gives U = (m/pi)(cos 3t, sin 3t)/r^3, the same dipole without"
      " the kernel; the mode-n Green formula solves phi'' + phi'/r - n^2 phi/r^2 = f; symbols of (d1 d2, -d1^2) Lap^-1"
      " are (xi1 xi2, -xi1^2)/|xi|^2")
# (A5) radial integration of Section 2 and the moment bound of R2
p_ = sp.symbols("p", real=True)
hh = sp.Function("h")(r)
assert sp.simplify(c * r ** (1 + 1 / c) * sp.diff(r ** (-1 / c) * hh, r) - (c * r * sp.diff(hh, r) - hh)) == 0
pv = sp.Rational(-9, 2)
cv = sp.Rational(9, 5)
integ = -(1 / cv) * r ** (1 / cv) * sp.integrate(s ** (pv - 1 / cv - 1), (s, r, sp.oo))
assert sp.simplify(integ - (-r**pv / (1 - cv * pv))) == 0
assert sp.simplify(1 - c * (1 / c - 4) - 4 * c) == 0
mint = sp.integrate(rho**2 * (1 + rho) ** qq, (rho, 0, sp.oo))
assert sp.simplify(mint - 2 / ((-qq - 1) * (-qq - 2) * (-qq - 3))) == 0
assert sp.integrate(sp.Abs(sp.sin(t)), (t, 0, 2 * sp.pi)) == 4
print("(A5) d_r(r^-gamma h) = r^(-gamma-1)(c r h_r - h)/c; a source B r^p integrates to -B r^p/(1 - c p) (checked at"
      " p = -9/2, c = 9/5); 1 - c(gamma - 4) = 4c; int_0^inf rho^2 (1 + rho)^q = 2/((-q-1)(-q-2)(-q-3)) (q = -7/2);"
      " int |sin t| = 4, so |m| <= 8 H/((-q-1)(-q-2)(-q-3))")
print("(A) done, %.1f s" % (time.monotonic() - T0))

# =============================== (B) arb ===============================
cF = Fr(4076476460239181, 2**51)
gF = 1 / cF
dF = 1 - gF
qs = gF - 4
e10 = 1 - 10 * dF
epsF = qs - e10
assert qs == Fr(-14054106027271476, 4076476460239181) and qs == 1 - dF - 4 and -5 < qs < -3
assert epsF == 9 * dF - 4 and epsF == Fr(116183978028673, 4076476460239181) and epsF > 0
# no sector exponent 1 - K delta - 2L strictly between e_(10,0) and q* (K, L >= 0, finite check of the only candidates)
between = [(K, L) for K in range(0, 40) for L in range(0, 4) if e10 < 1 - K * dF - 2 * L < qs]
assert between == []
A = lambda F_: arb(F_.numerator) / F_.denominator
qa = A(qs)
two = arb(2)
six = [arb(1) / 2, two ** (-qa), two ** (3 - qa), two ** (qa + 2) / (-qa), two ** (-qa - 2) / (-qa - 3),
       two ** (2 - qa) / (qa + 5)]
E = sum(six, arb(0))
res = json.loads((T4R / "verification/result.json").read_text())
assert res["qstar_exact"] == "%d/%d" % (qs.numerator, qs.denominator)
E_c = arb(res["E_qstar"])
assert E.overlaps(E_c) and E > 133 and E < 134
dens = {"eps": epsF, "eta=delta": dF, "delta": dF, "4": Fr(4), "1-q*": 1 - qs}
den_vals = {k_: 1 - cF * (qs - v) for k_, v in dens.items()}
assert all(v > 1 for v in den_vals.values())
mconst = A(Fr(8)) / ((-qa - 1) * (-qa - 2) * (-qa - 3))
print("(B) q* = %s = %.12f; epsilon = 9 delta - 4 = %s = %.12f; no exponent in (e_(10,0), q*)"
      % (qs, float(qs), epsF, float(epsF)))
print("    E_q* = %s (c1-t4 overlaps: %s); terms %s" % (E.str(25), E.overlaps(E_c), [x_.str(12) for x_ in six]))
print("    denominators 1 - c(q* - x) of (7): %s (all > 1)" % {k_: float(v) for k_, v in den_vals.items()})
print("    moment constant 8/((-q*-1)(-q*-2)(-q*-3)) = %s" % mconst.str(15))
OUT["B"] = {"qstar": str(qs), "epsilon": str(epsF), "E_qstar": E.str(40), "E_overlaps_c1t4": bool(E.overlaps(E_c)),
            "six_terms": [x_.str(20) for x_ in six], "denominators": {k_: str(v) for k_, v in den_vals.items()},
            "moment_constant": mconst.str(20)}

# =============================== (C) exact angular data ===============================
src = (HERE / "arith/t4_294_review.py").read_text()
assert sha(HERE / "arith/t4_294_review.py") == "229c9bd070a868ec627021c41f08967d61603af807d7d7d7f0616ca03a3b950c"
ns = {"__file__": str(HERE / "arith/t4_294_review.py"), "__name__": "t4_294_prefix"}
print("(C) executing the prefix of arith/t4_294_review.py (its own (A), (B) lines follow, then my (C) rows)")
exec(compile(src[:src.index("\nRES = {}\n")], "t4_294_review.py (prefix)", "exec"), ns)
ctx.prec = 400
tofr = lambda v: Fr(int(v.p), int(v.q))
rd = lambda d: {int(k_): Fr(v) for k_, v in d.items()}
OUT["C"] = {}
for name, fn in ns["CANDS"]:
    t1 = time.monotonic()
    assert ns["sha"](HERE / "data" / fn) == ns["EXPECT"][name]
    c_, chi = ns["load_file"](fn)
    cc = tofr(c_)
    assert cc == cF
    delta, R, S = ns["build"](c_, chi)
    expo = lambda K, L: 1 - K * delta - 2 * L
    Th_, Ps_ = ns["sectors"](R, S, delta)
    allK1 = all(K >= 1 for K, L in Th_) and all(K >= 1 for K, L in Ps_)
    assert allK1
    Fs = ns["residuals"](Th_, Ps_, [(1, 2)], expo, c_)
    T10 = {n: tofr(v) for n, v in Th_[(1, 0)].items() if v != 0}
    T12 = {n: tofr(v) for n, v in Th_[(1, 2)].items() if v != 0}
    F12 = {n: tofr(v) for n, v in Fs[(1, 2)].items() if v != 0}
    assert F12 == {n: (cc * qs - 1) * v for n, v in T12.items()} and cc * qs - 1 == -4 * cc
    P = {}
    for n, b in T10.items():          # Theta = sum b_n sin(n t): gamma cos 2t sin nt + n sin 2t cos nt
        for mm, co in ((n + 2, (gF + n) / 2), (n - 2, (gF - n) / 2)):
            if mm < 0:
                mm, co = -mm, -co
            if mm:
                P[mm] = P.get(mm, 0) + co * b
    P = {n: v for n, v in P.items() if v != 0}
    dat = json.loads((T4R / f"data/{name}_endpoint.json").read_text())
    same = {k_: rd(dat[k_]) == mine for k_, mine in (("Theta0", T10), ("Theta12", T12), ("F12", F12), ("P", P))}
    assert all(same.values())
    ip = lambda u, v: sum(u.get(n, 0) * v.get(n, 0) for n in set(u) | set(v))     # L2(S1) pairing over pi
    lam = ip(F12, P) / ip(P, P)
    assert lam == Fr(dat["lambda"])
    resid = {n: F12.get(n, 0) - lam * P.get(n, 0) for n in set(F12) | set(P)}
    assert ip(resid, P) == 0 and rd(dat["projection_residual"]) == {n: v for n, v in resid.items() if v != 0}
    d2 = ip(F12, F12) - ip(F12, P) ** 2 / ip(P, P)
    assert d2 > 0 and d2 == ip(resid, resid)
    n1, n3 = dat["nonzero_determinant"]["modes"]
    det = F12.get(n1, 0) * P.get(n3, 0) - F12.get(n3, 0) * P.get(n1, 0)
    assert det != 0 and det == Fr(dat["nonzero_determinant"]["value"])
    dA = (arb(d2.numerator) / d2.denominator * arb.pi()).sqrt()
    floorA = dA / (4 * A(cc))
    normA = (arb(ip(F12, F12).numerator) / ip(F12, F12).denominator * arb.pi()).sqrt()
    row = [rw for rw in res["rows"] if rw["candidate"] == name][0]
    ov = dA.overlaps(arb(row["angular_distance"])) and floorA.overlaps(arb(row["forced_tail_angular_floor"]))
    assert ov
    fl = int(float(floorA.mid()))
    assert floorA > fl and floorA < fl + 1 and floorA > int(row["strict_integer_lower"])
    print("(C) %s (%.1f s): all sectors K >= 1; F_(1,2) = -4c Theta_(1,2); Theta0, Theta12, F12, P equal c1-t4's data:"
          " %s; lambda and projection residual equal; d^2 > 0; det at modes %s nonzero and equal; ||A|| = %s;"
          " d = %s; d/(4c) = %s (overlaps c1-t4: %s); floor %d > %s"
          % (name, time.monotonic() - t1, all(same.values()), (n1, n3), normA.str(12), dA.str(15), floorA.str(15),
             ov, fl, row["strict_integer_lower"]))
    OUT["C"][name] = {"all_K_ge_1": allK1, "maps_equal": same, "lambda_equal": True, "d2_positive": True,
                      "det_modes": [n1, n3], "norm_A": normA.str(20), "d": dA.str(25), "d_over_4c": floorA.str(25),
                      "overlaps_c1t4": ov, "integer_floor": fl, "c1t4_integer": row["strict_integer_lower"]}

# =============================== (D) FLOAT test of (1) ===============================
mp.mp.dps = 30
qd = mp.mpf(qs.numerator) / qs.denominator
pd = (1 - qd) / 2
a3 = mp.mpf(3)
fn_ = {1: lambda s_: s_ * (1 + s_**2) ** (-pd), 3: lambda s_: a3 * s_**3 * (1 + s_**2) ** (-pd - 1)}
dfn = {1: lambda s_: mp.diff(fn_[1], s_), 3: lambda s_: mp.diff(fn_[3], s_)}


def modepot(n, rr):
    I1 = mp.quad(lambda s_: s_ ** (n + 1) * fn_[n](s_), [0, min(rr, 1), rr] if rr > 1 else [0, rr])
    I2 = mp.quad(lambda s_: s_ ** (1 - n) * fn_[n](s_), [rr, 2 * rr, 10 * rr, mp.inf])
    ph = -(I1 / rr**n + rr**n * I2) / (2 * n)
    dph = (I1 / rr ** (n + 1) - rr ** (n - 1) * I2) / 2
    d2ph = fn_[n](rr) - dph / rr + n**2 * ph / rr**2
    return ph, dph, d2ph


# Cartesian Hessian of G = phi(r) sin(n t) from the polar Hessian: G_r = phi' sin nt, G_rr = phi'' sin nt,
# G_t = n phi cos nt, G_tt = -n^2 phi sin nt, G_rt = n phi' cos nt, and
#   G_xx = cos^2 t G_rr + sin^2 t (G_r/r + G_tt/r^2) - 2 sin t cos t (G_rt/r - G_t/r^2)
#   G_xy = sin t cos t (G_rr - G_r/r - G_tt/r^2) + cos 2t (G_rt/r - G_t/r^2)
def hess(ph, dph, d2ph, n, rr, tt):
    sn, cn, st, ct = mp.sin(n * tt), mp.cos(n * tt), mp.sin(tt), mp.cos(tt)
    Gr, Grr, Gt, Gtt, Grt = dph * sn, d2ph * sn, n * ph * cn, -n**2 * ph * sn, n * dph * cn
    Gxx = ct**2 * Grr + st**2 * (Gr / rr + Gtt / rr**2) - 2 * st * ct * (Grt / rr - Gt / rr**2)
    Gxy = st * ct * (Grr - Gr / rr - Gtt / rr**2) + (ct**2 - st**2) * (Grt / rr - Gt / rr**2)
    return Gxx, Gxy


# sanity: phi = r^n gives the harmonic Im z^n, whose Hessian is (Im n(n-1) z^(n-2), Re n(n-1) z^(n-2)); and a
# central finite difference of the polar expression for a non-harmonic phi = r^2 exp(-r)
for nv in (1, 3, 5):
    for rr, tt in ((mp.mpf("0.7"), mp.mpf("0.3")), (mp.mpf(4), mp.mpf("2.2"))):
        Gxx, Gxy = hess(rr**nv, nv * rr ** (nv - 1), nv * (nv - 1) * rr ** (nv - 2), nv, rr, tt)
        w2 = nv * (nv - 1) * (rr * mp.expj(tt)) ** (nv - 2)
        assert abs(Gxx - mp.im(w2)) < mp.mpf(10) ** -25 and abs(Gxy - mp.re(w2)) < mp.mpf(10) ** -25
        ph_ = lambda s_: s_**2 * mp.exp(-s_)
        Gf = lambda X, Y: ph_(mp.sqrt(X**2 + Y**2)) * mp.sin(nv * mp.atan2(Y, X))
        X0, Y0 = rr * mp.cos(tt), rr * mp.sin(tt)
        Gxx, Gxy = hess(ph_(rr), mp.diff(ph_, rr), mp.diff(ph_, rr, 2), nv, rr, tt)
        assert abs(Gxx - mp.diff(lambda X: Gf(X, Y0), X0, 2)) < mp.mpf(10) ** -15
        assert abs(Gxy - mp.diff(lambda X: mp.diff(lambda Y: Gf(X, Y), Y0), X0)) < mp.mpf(10) ** -15
print("(D) polar-to-Cartesian Hessian checked on Im z^n (n = 1, 3, 5) and by numerical differentiation")
mm_ = mp.pi * mp.quad(lambda s_: s_**2 * fn_[1](s_), [0, 1, 10, mp.inf])
# H_q(h) as a FLOAT sup on a grid (log-spaced r, 720 angles), with a 1 percent safety factor
rg = np.logspace(-3, 5, 1601)
tg = np.linspace(0, 2 * np.pi, 721)[:-1]
qf, pf, a3f = float(qd), float(pd), float(a3)
f1 = rg * (1 + rg**2) ** (-pf)
f3 = a3f * rg**3 * (1 + rg**2) ** (-pf - 1)
df1 = (1 + rg**2) ** (-pf) - 2 * pf * rg**2 * (1 + rg**2) ** (-pf - 1)
df3 = a3f * (3 * rg**2 * (1 + rg**2) ** (-pf - 1) - 2 * (pf + 1) * rg**4 * (1 + rg**2) ** (-pf - 2))
S1_, S3_, C1_, C3_ = np.sin(tg), np.sin(3 * tg), np.cos(tg), np.cos(3 * tg)
hv = np.abs(f1[:, None] * S1_ + f3[:, None] * S3_)
gv = np.sqrt((df1[:, None] * S1_ + df3[:, None] * S3_) ** 2 + ((f1[:, None] * C1_ + 3 * f3[:, None] * C3_) / rg[:, None]) ** 2)
Hq = 1.01 * max(((1 + rg) ** (-qf) * hv.max(axis=1)).max(), ((1 + rg) ** (1 - qf) * gv.max(axis=1)).max())
Eq = float(E.mid())
worst = 0.0
rows_D = []
for rr in [0.05, 0.2, 0.5, 1, 1.5, 2, 3, 5, 10, 30, 100, 1000, 10000]:
    rr = mp.mpf(rr)
    pots = {n: modepot(n, rr) for n in (1, 3)}
    for tt in [0.1, 0.4, 0.9, 1.3, 2.0, 2.7]:
        tt = mp.mpf(tt)
        hs = [hess(*pots[n], n, rr, tt) for n in (1, 3)]
        u1 = sum(h_[1] for h_ in hs)
        u2 = sum(-h_[0] for h_ in hs)
        e1 = u1 - mm_ * mp.cos(3 * tt) / (mp.pi * rr**3)
        e2 = u2 - mm_ * mp.sin(3 * tt) / (mp.pi * rr**3)
        ratio = float(mp.sqrt(e1**2 + e2**2) / (Eq * Hq * rr**qd))
        worst = max(worst, ratio)
        rows_D.append([float(rr), float(tt), ratio, float(mp.sqrt(e1**2 + e2**2) * rr ** (-qd)),
                       float(mp.sqrt(u1**2 + u2**2) * rr**3)])
big = [rw for rw in rows_D if rw[0] >= 1000]
print("(D) FLOAT: q = q*, p = %.6f, a3 = 3, m = %s, H_q(h) ~ %.6f (grid sup x 1.01), E_q* = %.6f" % (pf, mp.nstr(mm_, 12), Hq, Eq))
print("    max over 13 radii (0.05 to 1e4) x 6 angles of |U[h] + DK M|/(E_q* H r^q*) = %.4e (< 1: %s)" % (worst, worst < 1))
print("    r^-q*|U + DK M| at r = 1e3, 1e4 (bounded): %s; r^3 |U| at r = 1e4 vs m/pi = %.10f: %s"
      % ([round(rw[3], 6) for rw in big], float(mm_ / mp.pi), [round(rw[4], 10) for rw in rows_D if rw[0] == 10000]))
OUT["D"] = {"q": qf, "p": pf, "a3": 3, "m": float(mm_), "H_grid": Hq, "E_qstar": Eq, "worst_ratio": worst,
            "rows[r, t, ratio, r^-q |U+DKM|, r^3 |U|]": rows_D}
assert worst < 1

# =============================== (E) remark R3: what (7) can give =====================================
# H_q*(h) >= sup_theta r^-q* |h(r, .)| >= ||r^-q* h(r, .)||_L2(S1)/sqrt(2 pi) -> ||A + (m/pi) P||/(4c sqrt(2 pi))
# >= d/(4c sqrt(2 pi)) = H_min. G >= G_lead = max_theta |gamma Theta e_r + Theta' e_theta| (limit of (5)). Since (7)
# contains H E G r^-delta/D_delta >= H_min E G_lead r^-delta/D_delta, the L2(S1) lower bound d/(4c) - sqrt(2 pi) sup|e|
# r^-q* is positive only for r > r_sep = (E G_lead/D_delta)^(1/delta); beyond r_sep the forced tail carries L2(R2) mass
# at most (d/(4c))^2 r_sep^(2q*+2)/(-2q*-2). FLOAT, with a grid max for G_lead (a lower bound for G).
OUT["E"] = {}
Dd = float(den_vals["delta"])
dl = float(dF)
for name, fn in ns["CANDS"]:
    dat = json.loads((T4R / f"data/{name}_endpoint.json").read_text())
    T0m = {int(k_): mp.mpf(Fr(v).numerator) / Fr(v).denominator for k_, v in dat["Theta0"].items()}
    gd = mp.mpf(gF.numerator) / gF.denominator
    th = [2 * mp.pi * k_ / 20000 for k_ in range(20000)]
    Gl = max(mp.sqrt((gd * sum(b * mp.sin(n * x_) for n, b in T0m.items())) ** 2
                     + sum(n * b * mp.cos(n * x_) for n, b in T0m.items()) ** 2) for x_ in th)
    dq = float(mp.mpf(OUT["C"][name]["d_over_4c"].split(" ")[0].strip("[")))
    Hmin = dq / float(mp.sqrt(2 * mp.pi))
    rows = {}
    for Ev in (Eq, 10.0, 1.0, 0.5):
        rsep = (Ev * float(Gl) / Dd) ** (1 / dl)
        bmax = dq * rsep ** (qf + 1) / (-2 * qf - 2) ** 0.5
        rows["E=%.6g" % Ev] = {"r_sep": rsep, "beta_max": bmax}
    OUT["E"][name] = {"G_lead": float(Gl), "H_min": Hmin, "by_E": rows}
    print("(E) FLOAT %s: H_q*(h) >= H_min = d/(4c sqrt(2 pi)) = %.4f; G_lead = %.6f; (r_sep, beta_max) for E = E_q*, 10,"
          " 1, 1/2: %s" % (name, Hmin, float(Gl), ["(%.4g, %.4g)" % (v["r_sep"], v["beta_max"]) for v in rows.values()]))
OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_335_review_results.json").write_text(json.dumps(OUT, indent=1))
print("done, %.1f s" % (time.monotonic() - T0))
