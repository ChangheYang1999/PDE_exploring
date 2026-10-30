"""Closure calculator for the S1 a posteriori programme (lane c1-t1, T3).

Reproduces the thresholds of the analysis2 frameworks FW-A2-Db, FW-A2-Da, FW-A2-Dw1, FW-A2-Dw2 from their
proved constants (A2/S1_CLOSURE.md sections 7, 7a, 8), the optimal-s formula, the component thresholds of
NORM-A2-E2, and the sensitivity of the threshold to each constant.  Exact rationals (fractions) are used where the
quantity is rational; mpmath interval arithmetic (iv, 60 digits) for square roots and pi.  Scenario rows with
hypothetical constants are labelled HYPOTHETICAL: they are what-if evaluations of the same closure formula, not
theorems.

Usage:  python3 -B closure_calc.py  > closure_calc.out
"""
from fractions import Fraction as Fr
from mpmath import iv, mpf
iv.dps = 60

def I(x):
    if isinstance(x, Fr):
        return iv.mpf(x.numerator) / x.denominator
    return iv.mpf(x)

def cs_of(s):
    s = I(s)
    return 1 / (2 * iv.sqrt(iv.pi * s * (1 + s)))

def show(x):
    x = iv.mpf(x)
    return "[%.10g, %.10g]" % (float(x.a), float(x.b))

out = []
P = out.append

# ---------------------------------------------------------------- FW-A2-Db (Theorem D(b))
P("== FW-A2-Db: rate 1/10 - 4800 s - 5 N_s(k)/s^(1/2) under (B9c), 0 < s <= 1/1024")
s = Fr(1, 2**18); r = Fr(1, 2**16)
# s^(1/2) = 2^-9 exactly
rate = Fr(1, 10) - 4800 * s - 5 * r * 2**9
P("  s = 2^-18, r = 2^-16, rate on the ball = %s = %.12g (stated lower bound 873/20480 = %.12g)" % (rate, float(rate), 873/20480))
assert rate == Fr(873, 20480) and rate > Fr(1, 24)
KH = Fr(24); eta = r / KH
P("  K_H = 24, eta = r/24 = %s = %.13e" % (eta, float(eta)))
cs = cs_of(s); d = cs * I(r)
P("  c_s = %s, d = c_s r = %s (< 1/400 = 0.0025)" % (show(cs), show(d)))
q = d / (I(Fr(19, 5)) - d)
P("  contraction q = d/(19/5 - d) = %s (< 1/1000)" % show(q))
assert d.b < 0.0025 and q.b < 0.001
# component thresholds of NORM-A2-E2 at eta
f = 1 - 34 * s
P("  reverse comparison factor 1 - 34 s = %s" % f)
P("  necessary component bounds (each component alone, from N_s >= (1-34s) E_2):")
etaI = I(eta) / I(f)
comps = [("P2 = ||omega D^2 F||_2", 1), ("G1 = ||grad F||_2", 2**7), ("G0 = ||F||_2", 2**9),
         ("H  = ||F||_Hdot^-1", 2**9 * iv.sqrt(I(Fr(20, 21))))]
for name, wgt in comps:
    P("    %-26s <= %s" % (name, show(etaI / wgt)))

# ---------------------------------------------------------------- FW-A2-Da
P("\n== FW-A2-Da: rate 1/10 - 2^22 s - 128 N_s(k)/s^(1/2) under (B9), s = 2^-28, r = 2^-27")
s = Fr(1, 2**28); r = Fr(1, 2**27)
rate = Fr(1, 10) - 2**22 * s - 128 * r * 2**14
P("  rate = %s = %.12g (stated >= 11/160 = %.6g), K_H = 20, eta = r/20 = %.13e" % (rate, float(rate), 11/160, float(r/20)))
assert rate >= Fr(11, 160)

# ---------------------------------------------------------------- optimal s formula
P("\n== optimal (s, r) for rate mu0 - C_bg s - c_U N/s^(1/2):  eta*(s) = (mu0 - C_bg s)^2 s^(1/2)/(4 c_U),")
P("   maximal at s* = mu0/(5 C_bg), eta* = (16/25) mu0^2 (mu0/(5 C_bg))^(1/2)/(4 c_U) = (16/(100 sqrt 5)) mu0^(5/2) C_bg^(-1/2)/c_U")
def eta_opt(mu0, Cbg, cU, smax=None):
    mu0 = I(mu0); Cbg = I(Cbg); cU = I(cU)
    s = mu0 / (5 * Cbg)
    if smax is not None and s.b > I(smax).a:
        s = I(smax)
    mu = mu0 - Cbg * s
    e = mu**2 * iv.sqrt(s) / (4 * cU)
    rr = mu * iv.sqrt(s) / (2 * cU)
    return s, e, rr
s0, e0, r0 = eta_opt(Fr(1, 10), 4800, 5)
P("  D(b) constants: s* = %s, eta* = %s, r* = %s, c_s r* = %s" % (show(s0), show(e0), show(r0), show(cs_of(Fr(1,240000))*r0)))
P("  elasticities: d log eta*/d log mu0 = 5/2, d log eta*/d log C_bg = -1/2, d log eta*/d log c_U = -1")

# ---------------------------------------------------------------- FW-A2-Dw1 and Dw2
P("\n== FW-A2-Dw1: rate 1/20 - 2^23 s - 400 N/s^(1/2), s = 3*2^-31, r0 = 5*2^-32, eta = 2^-35")
s = Fr(3, 2**31); r = Fr(5, 2**32)
rate = I(Fr(1, 20)) - I(2**23 * s) - 400 * I(r) / iv.sqrt(I(s))
P("  rate = %s (stated >= 6283/245760 = %.10g > 1/40)" % (show(rate), 6283/245760))
assert rate.a > 6283/245760
P("  eta = r0/40 = %s = %.10e" % (r / 40, float(r / 40)))
low = 6 * 2**11 * I(r) / iv.sqrt(I(s))
P("  low contraction 6*2^11*r0/s^(1/2) = %s (stated 15/(16 sqrt 6) = %.10g)" % (show(low), 15/(16*6**0.5)))
P("  component weights of E^w: P2 x 1, P1 x 2^11, L x 2^26.5 = %.6g" % (2**26.5))
P("  necessary pointwise and low conditions (A2 section 7a): |F(X)| < 2^-44 (1+|X|^2/R^2)^(11/10) = %.3e (...), ||wF||_H < 2^-61 = %.3e" % (2.0**-44, 2.0**-61))
P("\n== FW-A2-Dw2: rate 1/20 - 2^13 s - 400 N/s^(1/2), s = 3*2^-21, r0 = 5*2^-27, eta = 2^-30")
s = Fr(3, 2**21); r = Fr(5, 2**27)
rate = I(Fr(1, 20)) - I(2**13 * s) - 400 * I(r) / iv.sqrt(I(s))
P("  rate = %s, eta = r0/40 = %.10e" % (show(rate), float(r / 40)))
s0, e0, r0 = eta_opt(Fr(1, 20), 2**13, 400, Fr(1, 2**12))
P("  optimal s for the Dw2 constants: s* = %s, eta* = %s (gain %.3f over 2^-30)" % (show(s0), show(e0), float(e0.a) * 2**30))

# ---------------------------------------------------------------- what-if table
P("\n== HYPOTHETICAL what-if thresholds of the same closure formula (not theorems)")
P("   %-58s %-14s %-14s %-12s" % ("scenario (mu0, C_bg, c_U)", "s*", "eta*", "gain vs 6.358e-7"))
base = 1 / 1572864
rows = [("D(b) as proved (1/10, 4800, 5)", Fr(1,10), 4800, 5),
        ("C_bg / 10 (1/10, 480, 5)", Fr(1,10), 480, 5),
        ("C_bg / 100 (1/10, 48, 5)", Fr(1,10), 48, 5),
        ("mu0 = 1/4 (1/4, 4800, 5)", Fr(1,4), 4800, 5),
        ("mu0 = 1/2 (1/2, 4800, 5)", Fr(1,2), 4800, 5),
        ("mu0 = 1/2, C_bg = 48, c_U = 1", Fr(1,2), 48, 1),
        ("mu0 = 0.638 (homogeneous far-field D^2 rate), C_bg 48, c_U 1", Fr(638,1000), 48, 1)]
for lab, m, C, c in rows:
    s0, e0, r0 = eta_opt(m, C, c)
    P("   %-58s %-14.4g %-14.4g %-12.4g" % (lab, float(s0.a), float(e0.a), float(e0.a) / base))
P("   (c_U = 5 is proved only for s <= 1/1024; rows with s* > 1/1024 also need a new rough-transport bound.)")

# ---------------------------------------------------------------- tail cost model (HEURISTIC)
P("\n== HEURISTIC tail-cost model: residual F = r^q a sin(m theta) on r >= T (single odd mode, amplitude a).")
P("   Exact radial integrals of the homogeneous profile; Hdot^-1 via the homogeneous potential phi = r^(q+2) a sin(m theta)/((q+2)^2 - m^2).")
import math
def tail_norms(q, a, m, T):
    # angular L2 norm of a sin(m th) over the full circle: a sqrt(pi)
    A = a * math.sqrt(math.pi)
    G0 = A * T**(q + 1) / math.sqrt(-2 * q - 2) if q < -1 else float('inf')
    G1 = A * math.sqrt(q * q + m * m) * T**q / math.sqrt(-2 * q) if q < 0 else float('inf')
    p = q + 2
    H = A * math.sqrt(p * p + m * m) / abs(p * p - m * m) * T**p / math.sqrt(-2 * p) if p < 0 else float('inf')
    return G0, G1, H
for (lab, q, Aang) in [("p_7 fixed sector of the six-branch family", 1 - 7 * (1 - 1/1.8103192102), 3081.27),
                       ("p_8 fixed sector of the seven-branch family", 1 - 8 * (1 - 1/1.8103192102), 9679.97)]:
    a = Aang / math.sqrt(math.pi)    # put the whole angular norm in mode m = 1
    P("  %s: q = %.4f, angular norm %.2f (all in mode 1)" % (lab, q, Aang))
    for T in [10, 1e2, 1e4, 1e8, 1e16]:
        G0, G1, H = tail_norms(q, a, 1, T)
        E2low = math.sqrt(2**14 * G1**2 + 2**18 * G0**2 + 2**18 * (20/21) * H**2)
        P("    T = %-8.0e  G1 = %.3e  G0 = %.3e  H = %.3e  low part of E_2 = %.3e  (ratio to 6.358e-7: %.2e)" % (T, G1, G0, H, E2low, E2low / base))
    # radius at which the low part alone equals the D(b) threshold
    p = q + 2
    P("    H(T) = threshold/512 needs T >= %.3e" % ((base / (512 * math.sqrt(20/21))) / (Aang * math.sqrt(p*p+1)/abs(p*p-1)/math.sqrt(-2*p)))**(1/p))
print("\n".join(out))
