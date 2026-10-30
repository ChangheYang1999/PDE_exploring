"""Independent review of T4-242 (c1-t4 research/weighted_hessian_second_moment/PROOF.md, sha256 82e9f46b...ade6e):
||w2 D2 U[h]||_2 <= (1 + sqrt(6))/2 ||w2 D2 h||_2, w2 = 1 + r^2/R^2, with the sharp moment bound
||r^2 D2 B h||_2^2 <= 6 ||r^2 D2 h||_2^2 for real centrally odd h (reviews/REVIEW_T4_242.md).

Run from artifacts/:  python3 -B arith/t4_242_review.py
Needs sympy, numpy, scipy.

Parts:
  (A) exact (sympy): dbar B = d; polar forms of d, dbar and of d^2, d dbar, dbar^2 on f(r) e^(i m theta); the tensor
      identity |D2 v|^2 = 4(|d^2 v|^2 + 2|d dbar v|^2 + |dbar^2 v|^2) for complex v; the Mellin shift and Q_m; the
      multiplier (5) and its modulus; Q_(m-2) <= Q_m; the certificate (6); Q_1, Q_3 and the paired ratio 6; the even
      mode ratio Q_2(0)/Q_0(0); the IPM symbol U2 + i U1 = -(1 + B)/2; w2^2 and the constant comparison;
      review remark R2: the certificate 5 q(M) - q(M+2) >= 0 for M >= 3 and the S1 bound 63/32;
  (B) exact (sympy): canonical mode solutions of (3) near the origin for f = r^|m| (1 + r^2);
  (C) FLOAT: FFT check of (2), (7) and of the R2 bound on S1 test functions, and comparison of the FFT ratios with
      the mode-level prediction for h = y exp(-r^2/2) (illustration, not proof);
  (D) FLOAT: the sharpness family of Section 2 (ratio tends to 6), and the best S1 constant of (7) from the coupled
      mode forms, truncated to odd modes 1..N (lower bounds for the S1 constant; illustration).
Output: logs/t4_242_review.log.
"""
import time

import numpy as np
import scipy.linalg as sla
import sympy as sp
from scipy import integrate

T0 = time.monotonic()

# =============================== (A) exact identities ===============================
x1, x2 = sp.symbols("xi1 xi2", real=True)
I = sp.I
d_sym = I * (x1 - I * x2) / 2                     # symbol of d = (d_x - i d_y)/2
db_sym = I * (x1 + I * x2) / 2                    # symbol of dbar = (d_x + i d_y)/2
B_sym = (x1 - I * x2)**2 / (x1**2 + x2**2)
assert sp.simplify(db_sym * B_sym - d_sym) == 0
r, th = sp.symbols("r theta", positive=True)
m = sp.Symbol("m", integer=True)
f = sp.Function("f")
X, Y = sp.symbols("X Y", real=True)


def polar_d(expr, conj):         # d = e^(-i th)/2 (d_r - (i/r) d_th), dbar = e^(i th)/2 (d_r + (i/r) d_th)
    s = 1 if conj else -1
    return sp.exp(s * I * th) / 2 * (sp.diff(expr, r) + s * I / r * sp.diff(expr, th))


def rad(shifts, e):              # product of (D + a), D = r d_r, applied to e
    for a_ in shifts:
        e = r * sp.diff(e, r) + a_ * e
    return e


v = f(r) * sp.exp(I * m * th)
checks = {
    "d^2": (polar_d(polar_d(v, False), False), sp.exp(I * (m - 2) * th) * rad([m, m - 2], f(r)) / (4 * r**2)),
    "d dbar": (polar_d(polar_d(v, True), False), sp.exp(I * m * th) * rad([m, -m], f(r)) / (4 * r**2)),
    "dbar^2": (polar_d(polar_d(v, True), True), sp.exp(I * (m + 2) * th) * rad([-m, -m - 2], f(r)) / (4 * r**2)),
}
for k_, (lhs, rhs) in checks.items():
    assert sp.simplify(sp.expand(lhs - rhs)) == 0, k_
pol_sub = {X: r * sp.cos(th), Y: r * sp.sin(th)}
poly = X**2 * Y + I * X * Y**3                    # polar forms agree with the Cartesian ones on a test polynomial
for conj, cart in ((False, (sp.diff(poly, X) - I * sp.diff(poly, Y)) / 2),
                   (True, (sp.diff(poly, X) + I * sp.diff(poly, Y)) / 2)):
    assert sp.simplify(sp.expand((polar_d(poly.subs(pol_sub, simultaneous=True), conj)
                                  - cart.subs(pol_sub, simultaneous=True)).rewrite(sp.exp))) == 0
a, b, c = sp.symbols("a b c")                     # a = v_xx, b = v_xy, c = v_yy, complex
d2, db2, ddb = (a - 2 * I * b - c) / 4, (a + 2 * I * b - c) / 4, (a + c) / 4
cj = sp.conjugate
assert sp.expand(a * cj(a) + 2 * b * cj(b) + c * cj(c)
                 - 4 * (d2 * cj(d2) + 2 * ddb * cj(ddb) + db2 * cj(db2))) == 0
print("(A1) dbar B = d; on f(r) e^(i m theta): d^2, d dbar, dbar^2 = r^-2 (D+m-2)(D+m) f/4, r^-2 (D-m)(D+m) f/4,"
      " r^-2 (D-m-2)(D-m) f/4 times e^(i(m-2)theta), e^(i m theta), e^(i(m+2)theta); |D2 v|^2 = 4(|d^2 v|^2"
      " + 2|d dbar v|^2 + |dbar^2 v|^2) for complex v: exact")
tau, u = sp.symbols("tau u", real=True)
mm = sp.Symbol("m", real=True)
t = sp.Symbol("t", real=True)
Ft = sp.Function("F")
for a_ in (-3, 0, 2, sp.Symbol("alpha")):         # (D + a)(e^(-t) F) = e^(-t) (D + a - 1) F, D = d/dt, r = e^t
    e0 = sp.exp(-t) * Ft(t)
    assert sp.simplify(sp.diff(e0, t) + a_ * e0 - sp.exp(-t) * (sp.diff(Ft(t), t) + (a_ - 1) * Ft(t))) == 0
kap = -1 + I * tau                                # D on f -> kappa on F
fac = lambda s1_, s2_: sp.expand((kap + s1_) * (kap + s2_) * cj((kap + s1_) * (kap + s2_)))
Qsum = fac(mm - 2, mm) + 2 * fac(-mm, mm) + fac(-mm - 2, -mm)
Q = 4 * (mm**4 + 10 * mm**2 + 5 + (2 * mm**2 + 6) * u + u**2)
assert sp.expand(Qsum - Q.subs(u, tau**2)) == 0
sq = lambda a_: a_**2 + u
assert sp.expand(sq(mm + 1) * sq(mm + 3) + 2 * sq(mm - 1) * sq(mm + 1) + sq(mm - 1) * sq(mm - 3) - Q) == 0
mu = (mm - 1 + I * tau) / (1 - mm + I * tau)
assert sp.simplify(mu * cj(mu) - 1) == 0
# (D - m + 2) g = (D + m) f  ->  (kappa - m + 2) Ghat = (kappa + m) Fhat
assert sp.simplify((kap + mm) / (kap - mm + 2) - mu) == 0
M = sp.Symbol("M", real=True)
q = lambda MM: MM**4 + 10 * MM**2 + 5 + (2 * MM**2 + 6) * u + u**2
assert sp.factor(q(M) - q(M - 2)) == sp.factor(4 * (M - 1) * (M**2 + (M - 2)**2 + 10 + 2 * u))
cert = (M - 1) * (10 * M**3 + 2 * M**2 + 78 * M + 6) + (20 * M**2 - 8 * M + 52) * u + 10 * u**2
assert sp.expand(11 * q(M) - q(M + 2) - cert) == 0
assert sp.discriminant(20 * M**2 - 8 * M + 52, M) < 0
Qv = lambda mv, uv: Q.subs({mm: mv, u: uv})
assert Qv(1, 0) == 64 and Qv(3, 0) == 704 and Qv(-1, 0) == 64 and (Qv(-1, 0) + Qv(3, 0)) / (2 * Qv(1, 0)) == 6
assert q(3).subs(u, 0) == 11 * q(1).subs(u, 0)
print("(A2) Mellin: (D + a) f -> (D + a - 1) F with F = e^t f(e^t), so D -> kappa = -1 + i tau, and the three-term"
      " energy is Q_m(tau^2) = 4[m^4 + 10 m^2 + 5 + (2m^2 + 6)u + u^2] (also in the PROOF's factored form);"
      " (kappa + m)/(kappa - m + 2) = (m - 1 + i tau)/(1 - m + i tau) of modulus 1; q(M) - q(M-2) ="
      " 4(M - 1)(M^2 + (M-2)^2 + 10 + 2u); 11 q(M) - q(M+2) = certificate (6), discriminant of its u coefficient"
      " < 0, equality at M = 1, u = 0; Q_1(0) = 64, Q_3(0) = 704, paired ratio 6: exact")
print("(A3) even mode m = 0 (excluded by central oddness): Q_2(u)/Q_0(u) = (61 + 14u + u^2)/(5 + 6u + u^2), value %s"
      " at u = 0, its maximum" % (Qv(2, 0) / Qv(0, 0)))
assert sp.simplify(Q.subs(mm, 2) / Q.subs(mm, 0) - (61 + 14 * u + u**2) / (5 + 6 * u + u**2)) == 0
assert sp.factor(sp.diff((61 + 14 * u + u**2) / (5 + 6 * u + u**2), u)) == sp.factor(
    -(8 * u**2 + 112 * u + 296) / (5 + 6 * u + u**2)**2)
# velocity ratios at tau = 0 (u = 0) for two single-pair families (limit L -> infinity of the Section 2 family):
# radial h (mode 0 -> output modes 0, -2): (Q_0 + Q_2)/(4 Q_0); cos(theta) h (f_1 = f_(-1), output modes 1, -1, -3
# with amplitudes 1, 2, 1): (Q_1 + 4 Q_1 + Q_3)/(4 * 2 Q_1); sin(theta) h (S1, output modes 1, -3): (Q_1 + Q_3)/(8 Q_1)
rad_U = (Qv(0, 0) + Qv(2, 0)) / (4 * Qv(0, 0))
cos_U = (5 * Qv(1, 0) + Qv(3, 0)) / (8 * Qv(1, 0))
sin_U = (Qv(1, 0) + Qv(3, 0)) / (8 * Qv(1, 0))
assert rad_U == sp.Rational(33, 10) and cos_U == 2 and sin_U == sp.Rational(3, 2)
assert sp.Rational(33, 10) > (7 + 2 * sp.sqrt(6)) / 4
print("(A3) velocity ratios ||r^2 D2 U||^2/||r^2 D2 h||^2 at u = 0: radial pair %s > (7 + 2 sqrt 6)/4 (so (7) and (1)"
      " fail without central oddness), cos(theta) pair %s, sin(theta) pair (S1) %s" % (rad_U, cos_U, sin_U))
R1s = -I * x1 / sp.sqrt(x1**2 + x2**2)
R2s = -I * x2 / sp.sqrt(x1**2 + x2**2)
assert sp.simplify(R1s**2 + I * (-R1s * R2s) + (1 + B_sym) / 2) == 0
Rr = sp.Symbol("R", positive=True)
assert sp.expand((1 + r**2 / Rr**2)**2 - (1 + 2 * r**2 / Rr**2 + r**4 / Rr**4)) == 0
K2 = ((1 + sp.sqrt(6)) / 2)**2
assert sp.Rational(5, 3) < K2 and 1 < K2 and sp.simplify(K2 - (7 + 2 * sp.sqrt(6)) / 4) == 0
print("(A4) U2 + i U1 = -(1 + B)/2 with U1 = -R1 R2, U2 = R1^2 (symbols); w2^2 = 1 + 2 r^2/R^2 + r^4/R^4;"
      " 1 < 5/3 < ((1 + sqrt 6)/2)^2 = (7 + 2 sqrt 6)/4 = %.7f: exact" % float(K2))
# review remark R2 (S1): 5 q(M) - q(M+2) >= 0 for M >= 3, and the Young bound
cert5 = 4 * (M - 3) * (M**3 + M**2 + 7 * M + 3) + (8 * M**2 - 8 * M + 16) * u + 4 * u**2
assert sp.expand(5 * q(M) - q(M + 2) - cert5) == 0
assert sp.discriminant(8 * M**2 - 8 * M + 16, M) < 0
aa, bb, l1, l2 = sp.symbols("a b lambda1 lambda2", nonnegative=True)
young = (1 + l1) * (aa + bb) + (1 + 1 / l1) * bb + (1 + l2) * bb + (1 + 1 / l2) * (11 * aa + 5 * bb)
yv = sp.expand(young.subs({l1: 1, l2: 4}))
assert yv == sp.Rational(63, 4) * aa + sp.Rational(61, 4) * bb
S1c = sp.Rational(63, 4) / 8
assert S1c == sp.Rational(63, 32) and sp.Rational(5, 3) < S1c < 2 < K2
print("(A5) R2: 5 q(M) - q(M+2) = 4(M - 3)(M^3 + M^2 + 7M + 3) + (8M^2 - 8M + 16)u + 4u^2 >= 0 for M >= 3 (equality"
      " at M = 3, u = 0); Young with lambda1 = 1, lambda2 = 4: P + N <= (63/4) a + (61/4) b, so the S1 squared"
      " constant of (7) is <= (63/4)/8 = 63/32 = %.6f (sqrt %.6f); 5/3 < 63/32 < 2 < %.6f: exact"
      % (float(S1c), float(sp.sqrt(S1c)), float(K2)))
print("(A) done, %.1f s" % (time.monotonic() - T0), flush=True)

# =============================== (B) canonical mode solutions ===============================
for mv in (5, 3, 1, -1, -3, -5):
    k_ = abs(mv)
    fr = r**k_ * (1 + r**2)
    rhs_ = sp.expand(rad([mv], fr))
    gp = sum(sp.Poly(rhs_, r).coeff_monomial(r**p) / (p - mv + 2) * r**p for p in (k_, k_ + 2))
    assert sp.simplify(rad([-mv + 2], gp) - rhs_) == 0
    assert sp.simplify(rad([-mv + 2], r**(mv - 2))) == 0
    print("(B) m = %2d, f = r^%d (1 + r^2): (D + m) f = %s, regular particular g = %s; homogeneous r^(%d)"
          % (mv, k_, rhs_, sp.factor(gp), mv - 2))
print("(B) m >= 3: the homogeneous solution grows at infinity, so the canonical g vanishes beyond supp f and is"
      " O(r^(m-2)) at 0; m = 1: g = f, homogeneous r^-1 singular; m = -M: g = O(r^(M+2)) at 0, c r^(-M-2) outside")

# =============================== (C) FFT check (FLOAT) ===============================
Ng, Lb = 1024, 32.0
xs = (np.arange(Ng) - Ng // 2) * (2 * Lb / Ng)
XX, YY = np.meshgrid(xs, xs, indexing="ij")
k1 = 2 * np.pi * np.fft.fftfreq(Ng, d=2 * Lb / Ng)
K1, K2g = np.meshgrid(k1, k1, indexing="ij")
kk = K1**2 + K2g**2
kk[0, 0] = 1.0
Bm = (K1 - 1j * K2g)**2 / kk
Bm[0, 0] = 0.0
U1m, U2m = K1 * K2g / kk, -K1**2 / kk             # -R1 R2 and R1^2 (real symbols); zero mode set to 0
U1m[0, 0] = U2m[0, 0] = 0.0
rr2 = XX**2 + YY**2
w4 = np.fft.ifftshift(rr2**2)


def hess(fh):                    # ordered Hessian components in real space (origin at index 0)
    return [np.fft.ifft2(-ka * kb * fh) for ka in (K1, K2g) for kb in (K1, K2g)]


def wnorm2(comps):
    return sum(np.sum(w4 * np.abs(cp)**2) for cp in comps)


def s1(g):                       # S1 symmetrization: even in x, odd in y
    return g(XX, YY) + g(-XX, YY) - g(XX, -YY) - g(-XX, -YY)


tests = {
    "y exp(-r^2/2)": YY * np.exp(-rr2 / 2),
    "x^2 y exp(-r^2/2) - y^3 exp(-r^2)": XX**2 * YY * np.exp(-rr2 / 2) - YY**3 * np.exp(-rr2),
    "S1 Gaussian at (1.5, 0.7), width 0.6": s1(lambda a_, b_: np.exp(-((a_ - 1.5)**2 + (b_ - 0.7)**2) / 0.36)),
    "S1 Gaussian at (3.0, 2.0), width 1.2": s1(lambda a_, b_: np.exp(-((a_ - 3.0)**2 + (b_ - 2.0)**2) / 1.44)),
    "S1 Gaussian at (0.4, 0.3), width 0.5": s1(lambda a_, b_: np.exp(-((a_ - 0.4)**2 + (b_ - 0.3)**2) / 0.25)),
}
res_C = {}
for name, h in tests.items():
    hh = np.fft.fft2(np.fft.ifftshift(h))
    in2 = wnorm2(hess(hh))
    rB = wnorm2(hess(Bm * hh)) / in2
    HU1, HU2 = hess(U1m * hh), hess(U2m * hh)
    rU = (wnorm2(HU1) + wnorm2(HU2)) / in2
    rUc = wnorm2(hess(-(1 + Bm) * hh / 2)) / in2
    imag = max(np.max(np.abs(cp.imag)) for cp in HU1 + HU2)
    res_C[name] = (rB, rU)
    assert rB <= 6 + 1e-6 and rU <= float(S1c) + 1e-6 and abs(rU / rUc - 1) < 1e-10
    print("(C) FLOAT FFT %-38s ||r^2 D2 B h||^2/||r^2 D2 h||^2 = %.6f (<= 6); ||r^2 D2 U||^2/||r^2 D2 h||^2 = %.6f"
          " (<= 63/32 <= %.4f; complex form agrees to %.1e; max |imag| of D2 U1, D2 U2 %.1e)"
          % (name, rB, rU, float(K2), abs(rU / rUc - 1), imag), flush=True)
# mode-level prediction for h = y exp(-r^2/2): b_1 = r exp(-r^2/2), |Fhat(tau)|^2 proportional to
# |Gamma(1 - i tau/2)|^2 = (pi tau/2)/sinh(pi tau/2)
Qf = lambda mv, tv: 4 * (mv**4 + 10 * mv**2 + 5 + (2 * mv**2 + 6) * tv**2 + tv**4)
Fh2 = lambda tv: (np.pi * tv / 2) / np.sinh(np.pi * tv / 2) if tv != 0 else 1.0
num = integrate.quad(lambda tv: (Qf(1, tv) + Qf(3, tv)) * Fh2(tv), 0, 80, limit=400)[0]
den = integrate.quad(lambda tv: Qf(1, tv) * Fh2(tv), 0, 80, limit=400)[0]
predB, predU = num / (2 * den), num / (8 * den)   # S1: mode -1 of h + B h cancels, so the U ratio is the B ratio / 4
rB1, rU1 = res_C["y exp(-r^2/2)"]
print("(C) mode-level prediction for y exp(-r^2/2): B ratio %.6f, U ratio %.6f (FFT %.6f, %.6f; relative differences"
      " %.1e, %.1e)" % (predB, predU, rB1, rU1, abs(predB / rB1 - 1), abs(predU / rU1 - 1)))
assert abs(predB / rB1 - 1) < 1e-3 and abs(predU / rU1 - 1) < 1e-3
print("(C) done, %.1f s" % (time.monotonic() - T0), flush=True)

# ============================ (D) sharpness family and the S1 constant of (7) (FLOAT) ============================
zq = np.linspace(-1, 1, 4001)
abump = np.zeros_like(zq)
inside = np.abs(zq) < 1
abump[inside] = np.exp(-1 / (1 - zq[inside]**2))
for Lv in (1, 4, 16, 64, 256):
    tg = np.linspace(0, 200 / Lv, 8001)
    ah = np.array([np.trapezoid(abump * np.cos(Lv * tv * zq), zq) for tv in tg])   # a even: real transform
    wgt = ah**2                                   # |Fhat|^2 = L^2 |ahat(L tau)|^2; L^2 cancels
    rB = np.trapezoid((Qf(1, tg) + Qf(3, tg)) * wgt, tg) / (2 * np.trapezoid(Qf(1, tg) * wgt, tg))
    print("(D1) FLOAT h = r^-1 a((log r - T)/L) sin(theta), a = exp(-1/(1 - z^2)), L = %3d: B ratio %.6f, U ratio"
          " %.6f" % (Lv, rB, rB / 4))


def s1_forms(tv, nmax):          # per-tau Hermitian forms on (A_1, A_3, ..., A_nmax): output sum_k Q_k |(h + Bh)_k|^2
    ns = list(range(1, nmax + 1, 2))           # and input 2 sum_n Q_n |A_n|^2 (S1: Fhat_(-n) = -A_n)
    idx = {n: i for i, n in enumerate(ns)}
    Out = np.zeros((len(ns), len(ns)), complex)
    In = np.diag([2.0 * Qf(n, tv) for n in ns]).astype(complex)

    def add(Qk, coeffs):
        vec = np.zeros(len(ns), complex)
        for n, cf in coeffs.items():
            if n in idx:
                vec[idx[n]] += cf
        Out[:, :] += Qk * np.outer(vec.conj(), vec)

    for n in ns:                 # output mode n >= 1: A_n + mu_(n+2) A_(n+2)
        add(Qf(n, tv), {n: 1.0, n + 2: (n + 1 + 1j * tv) / (-(n + 1) + 1j * tv)})
    for K_ in range(3, nmax + 3, 2):   # output mode -K: -(A_K + mu_(2-K) A_(K-2)); output mode -1 vanishes
        add(Qf(K_, tv), {K_: 1.0, K_ - 2: (-(K_ - 1) + 1j * tv) / ((K_ - 1) + 1j * tv)})
    return Out, In


taus = np.concatenate([np.linspace(0, 4, 161), np.linspace(4.1, 40, 360), [60, 100, 300, 1000]])
for nmax in (1, 3, 5, 9, 21, 41, 81):
    vals = [(sla.eigh(*s1_forms(tv, nmax), eigvals_only=True)[-1] / 4, tv) for tv in taus]
    top = max(vals)
    tail = vals[-1][0]
    assert top[0] <= float(S1c) + 1e-9
    print("(D2) FLOAT S1, odd modes 1..%2d: max over the tau grid of ||r^2 D2 U||^2/||r^2 D2 h||^2 = %.6f at tau ="
          " %.3f (sqrt %.6f); value at tau = 1000: %.6f; R2 bound 63/32 = 1.96875, T4-242 %.6f"
          % (nmax, top[0], top[1], np.sqrt(top[0]), tail, float(K2)), flush=True)
print("(D) done, %.1f s" % (time.monotonic() - T0), flush=True)
print("total %.1f s" % (time.monotonic() - T0))
