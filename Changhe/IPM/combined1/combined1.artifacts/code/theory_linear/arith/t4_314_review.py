"""Checks for reviews/REVIEW_T4_314.md (c1-t4 research/far_out_tail_repair/PROOF.md, T4-314).

A  exact exponents of the campaign specialization (fractions).
B  sympy: velocity identities and the Fourier symbol of h -> v; scaling h_L(X) = L^q h_1(X/L) and the dilation
   commutation of X.grad at random rational points; polar density of -r^s cos(2 m theta) and its leading coefficients.
C  exact r^q profile of h_L for 007 from the stored A1_m (c1-t4 data, read in place); FLOAT (mpmath) constants
   C_(0,0) = ||h_1||_2 and C_(1,0) = || |X| h_1 ||_2 for the cutoff of the PROOF, and a sampled sup of the profile.
"""
import hashlib
import json
import random
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import sympy as sp

T0 = time.time()
SRC = Path("RUN_ROOT/theory_audit_T4/research/far_out_tail_repair")
HERE = Path(__file__).resolve().parents[1]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(SRC / "PROOF.md") == "d0160e7250906bfbc432a9ec8399b54601129b4364d9a96ebb4664450f73b83b"
D007 = SRC / "data/007_tail_repair.json"
assert sha(D007) == "bad9b06a64a3f045e3de487d63793f8ec0c6b021a692c5e11cea91279ed5fcd6"
OUT = {}

# ---------------- A: exact exponents
c = Fr(4076476460239181, 2**51)
g = 1 / c
dl = 1 - g
q = 4 * g - 5
e9 = 1 - 9 * dl
mixed = q + g - 1
quad = 2 * q - 1
assert q == Fr(-11375183046454913, 4076476460239181) and q == -1 - 4 * dl
assert e9 == Fr(-12345613358746216, 4076476460239181)
assert -3 < q < -2 and 4 * g < 3            # q < -2 is used in remark R2 (Hdot^-1)
assert mixed == 5 * g - 6 and g > Fr(1, 2) and quad < mixed < e9 < -3
assert c * q - 1 == 3 - 5 * c and 5 * c - 3 > 0
EXPS = {"L2 (beta 0, k 0)": q + 1, "|X| h (beta 1, k 0), Hdot^-1 via Hardy": q + 2,
        "graded (beta 11/5, k 2)": q + Fr(6, 5), "sharp exterior (beta 8/5, k 2)": q + Fr(3, 5),
        "omega = (1 + 4 r^2)^(2/5) (beta 4/5, k 2)": q - Fr(1, 5), "w2 = 1 + r^2/R^2 (beta 2, k 2)": q + 1,
        "residual linear": q + 1, "residual mixed": q + g, "residual quadratic": 2 * q,
        "E_a threshold a = q + 1": q + 1}
assert all(v < 0 for v in EXPS.values())
OUT["A"] = {"q": str(q), "q_float": float(q), "e9": str(e9), "mixed": str(mixed), "quad": str(quad),
            "exponents": {k: [str(v), float(v)] for k, v in EXPS.items()}}
print("A  q = %s = %.15f; e9 = %.12f; mixed 5g - 6 = %.12f; quad 2q - 1 = %.12f; c q - 1 = 3 - 5c = %.12f"
      % (q, float(q), float(e9), float(mixed), float(quad), float(c * q - 1)))
for k, v in EXPS.items():
    print("   exponent %-44s %.12f" % (k, float(v)))

# ---------------- B: sympy identities
x, y, L, s = sp.symbols("x y L s", real=True)
X1, X2 = sp.symbols("xi1 xi2", real=True)
chi = sp.Function("chi")(x, y)
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2)
h = -sp.diff(lap(chi), y)
psi = sp.diff(chi, x, y)
v = (-sp.diff(psi, y), sp.diff(psi, x))
div = sp.simplify(sp.diff(v[0], x) + sp.diff(v[1], y))
curl = sp.simplify(sp.diff(v[1], x) - sp.diff(v[0], y) - (-sp.diff(h, x)))
assert div == 0 and curl == 0
# Fourier: d_x -> i xi1, d_y -> i xi2 acting on chi^
I = sp.I
hh = -(I * X2) * (-(X1**2 + X2**2))
vh = (-(I * X2) * (I * X1) * (I * X2), (I * X1) * (I * X1) * (I * X2))
# canonical IPM: div U = 0, curl U = -d_x rho  =>  U^ = (xi1 xi2, -xi1^2)/|xi|^2 rho^
can = (X1 * X2 / (X1**2 + X2**2), -X1**2 / (X1**2 + X2**2))
assert all(sp.simplify(vh[i] - can[i] * hh) == 0 for i in range(2))
assert sp.simplify(I * X1 * can[0] + I * X2 * can[1]) == 0
assert sp.simplify(I * X1 * can[1] - I * X2 * can[0] - (-(I * X1))) == 0
print("B1 div v = 0, curl v = -d_x h for generic chi; v^ = (xi1 xi2, -xi1^2)/|xi|^2 h^, the canonical symbol: True")

# scaling at random rational points, with a concrete smooth test potential (not compactly supported, generic angle)
qs = sp.Rational(q.numerator, q.denominator)
r2 = x**2 + y**2
chi1 = -(r2 ** ((qs + 3) / 2)) * (x**2 * y**2 + 3 * x**4) / r2**2 * sp.exp(-r2 / 7)
h1 = -sp.diff(lap(chi1), y)
v1 = (-sp.diff(sp.diff(chi1, x, y), y), sp.diff(sp.diff(chi1, x, y), x))
chiL = L ** (qs + 3) * chi1.subs({x: x / L, y: y / L}, simultaneous=True)
hL = -sp.diff(lap(chiL), y)
vL = (-sp.diff(sp.diff(chiL, x, y), y), sp.diff(sp.diff(chiL, x, y), x))
cs = sp.Rational(c.numerator, c.denominator)
linL = cs * (x * sp.diff(hL, x) + y * sp.diff(hL, y)) - hL
lin1 = cs * (x * sp.diff(h1, x) + y * sp.diff(h1, y)) - h1
random.seed(314)
mp.mp.dps = 50
fL = [sp.lambdify((x, y, L), e, "mpmath") for e in (hL, vL[0], vL[1], linL)]
f1 = [sp.lambdify((x, y), e, "mpmath") for e in (h1, v1[0], v1[1], lin1)]
qm = mp.mpf(q.numerator) / q.denominator
worst = mp.mpf(0)
for _ in range(4):
    px, py, pl = (mp.mpf(random.randint(5, 40)) / 7, mp.mpf(random.randint(-40, 40)) / 9,
                  mp.mpf(random.randint(11, 60)) / 10)
    for FL, F1 in zip(fL, f1):
        av, bv = FL(px, py, pl), pl**qm * F1(px / pl, py / pl)
        worst = max(worst, abs(av - bv) / max(abs(bv), mp.mpf(10) ** -30))
assert worst < 1e-40
print("B2 h_L = L^q h_1(X/L), v_L = L^q v_1(X/L), (cX.grad - 1) h_L = L^q [(cY.grad - 1) h_1](X/L) at 4 random"
      " rational points (50 digits): max relative difference %s" % mp.nstr(worst, 3))
# polar density of -r^s cos(2 m theta)
r, th = sp.symbols("r theta", positive=True)
for m in range(4):
    chim = -(r2 ** (s / 2)) * sp.chebyshevt(2 * m, x / sp.sqrt(r2))      # = -r^s cos(2 m theta)
    hm = -sp.diff(lap(chim), y)
    pred = (s**2 - 4 * m**2) * r2 ** ((s - 3) / 2) / 2 * (
        (s - 2 - 2 * m) * sp.sin((2 * m + 1) * sp.atan2(y, x)) - (s - 2 + 2 * m) * sp.sin((2 * m - 1) * sp.atan2(y, x)))
    fd_ = sp.lambdify((x, y, s), hm - pred, "mpmath")
    for pt in [(mp.mpf(3) / 2, mp.mpf(5) / 7), (mp.mpf(-2) / 3, mp.mpf(9) / 4)]:
        for sv in [mp.mpf(1) / 5, mp.mpf(7) / 6]:
            assert abs(fd_(pt[0], pt[1], sv)) < 1e-30
print("B3 -d_y Lap(-r^s cos(2 m theta)) = (s^2 - 4 m^2) r^(s-3)/2 [(s - 2 - 2m) sin((2m+1) theta)"
      " - (s - 2 + 2m) sin((2m-1) theta)], m = 0..3: True")
OUT["B"] = {"identities": True, "scaling_max_rel": float(worst), "polar_density": True}

# ---------------- C: 007 profile (exact) and constants (FLOAT)
dat = json.loads(D007.read_text())
A1 = {int(t["m"]): Fr(t["A1"]) for t in dat["moment_checks"]}
assert sorted(A1) == list(range(40)) and all(A1.values())
sq = q + 3
prof = {}
for m, a in A1.items():
    k = a * (sq**2 - 4 * m * m) / 2
    for n, co in ((2 * m + 1, sq - 2 - 2 * m), (2 * m - 1, -(sq - 2 + 2 * m))):
        if n < 0:
            n, co = -n, -co
        prof[n] = prof.get(n, Fr(0)) + k * co
prof = {n: b for n, b in prof.items() if b != 0}
mp.mp.dps = 30
pn2 = mp.pi * sum(mp.mpf(b.numerator) / b.denominator * mp.mpf(b.numerator) / b.denominator for b in prof.values())
pnorm = mp.sqrt(pn2)
F41 = (5 * mp.mpf(c.numerator) / c.denominator - 3) * pnorm
grid = [2 * mp.pi * j / 20000 for j in range(20000)]
bs = [(n, mp.mpf(b.numerator) / b.denominator) for n, b in sorted(prof.items())]
sup = max(abs(sum(b * mp.sin(n * t) for n, b in bs)) for t in grid[:5000])   # odd sines: |.| has period pi/2 symmetry
print("C1 007: r^q profile of h_L for r >= 2L has %d odd sine modes (top %d); circle norm (int_0^2pi)^(1/2) = %s;"
      " (5c - 3) x norm = %s; sampled sup over [0, pi/2) = %s"
      % (len(prof), max(prof), mp.nstr(pnorm, 12), mp.nstr(F41, 12), mp.nstr(sup, 10)))

# cutoff zeta and radial derivatives of f = -zeta r^s
rr = sp.symbols("rr", positive=True)
b1 = sp.exp(-1 / (rr - 1))
b2 = sp.exp(-1 / (2 - rr))
zeta = b1 / (b1 + b2)
sS = sp.Rational(sq.numerator, sq.denominator)
f = -zeta * rr**sS
fd = [f] + [sp.diff(f, rr, j) for j in (1, 2, 3)]
fl = [sp.lambdify(rr, e, "mpmath") for e in fd]
am = [(m, mp.mpf(a.numerator) / a.denominator) for m, a in sorted(A1.items())]


def modes(rv):
    f0, f1, f2, f3 = [F(rv) for F in fl]
    out = {}
    for m, a in am:
        gm = f2 + f1 / rv - 4 * m * m * f0 / rv**2
        gp = f3 + f2 / rv - f1 / rv**2 - 4 * m * m * (f1 / rv**2 - 2 * f0 / rv**3)
        for n, co in ((2 * m + 1, (gp - 2 * m * gm / rv) / 2), (2 * m - 1, -(gp + 2 * m * gm / rv) / 2)):
            if n < 0:
                n, co = -n, -co
            out[n] = out.get(n, 0) - a * co
    return out


# consistency: at r = 2 the modes equal the exterior profile times 2^q (zeta = 1 to all orders there)
md2 = modes(mp.mpf("1.99999999"))
rel = max(abs(md2.get(n, 0) - mp.mpf(b.numerator) / b.denominator * mp.mpf("1.99999999") ** mp.mpf(float(q)))
          for n, b in prof.items()) / max(abs(mp.mpf(b.numerator) / b.denominator) for b in prof.values())
print("C2 annulus modes at r = 2 - 1e-8 against the exterior profile: max relative difference %s" % mp.nstr(rel, 3))
assert rel < 1e-6


def integrand(rv, wpow):
    return mp.pi * sum(val * val for val in modes(rv).values()) * rv ** (1 + wpow)


t1 = time.time()
ann0 = mp.quad(lambda rv: integrand(rv, 0), [1, 1.25, 1.5, 1.75, 2])
ann1 = mp.quad(lambda rv: integrand(rv, 2), [1, 1.25, 1.5, 1.75, 2])
qf = mp.mpf(q.numerator) / q.denominator
ext0 = pn2 * mp.mpf(2) ** (2 * qf + 2) / (-2 * qf - 2)
ext1 = pn2 * mp.mpf(2) ** (2 * qf + 4) / (-2 * qf - 4)
C00 = mp.sqrt(ann0 + ext0)
C10 = mp.sqrt(ann1 + ext1)
Leps = {e: (C00 / e) ** (1 / (-qf - 1)) for e in (mp.mpf("1e-3"), mp.mpf("1e-6"))}
Lh = {e: (C10 / e) ** (1 / (-qf - 2)) for e in (mp.mpf("1e-3"), mp.mpf("1e-6"))}
print("C3 (quadrature %.1f s) C_(0,0) = %s (annulus %s, exterior %s); C_(1,0) = %s (annulus %s, exterior %s)"
      % (time.time() - t1, mp.nstr(C00, 10), mp.nstr(mp.sqrt(ann0), 10), mp.nstr(mp.sqrt(ext0), 10),
         mp.nstr(C10, 10), mp.nstr(mp.sqrt(ann1), 10), mp.nstr(mp.sqrt(ext1), 10)))
for e in Leps:
    print("   ||h_L||_2 < %s needs L > %s; the Hardy bound ||h_L||_H <= L^(q+2) C_(1,0) < %s needs L > %s"
          % (mp.nstr(e, 2), mp.nstr(Leps[e], 8), mp.nstr(e, 2), mp.nstr(Lh[e], 8)))
OUT["C"] = {"profile_modes": len(prof), "profile_top": max(prof), "profile_norm": float(pnorm),
            "five_c_minus_3_times_norm": float(F41), "sampled_sup": float(sup), "C00": float(C00),
            "C10": float(C10), "C00_annulus": float(mp.sqrt(ann0)), "C00_exterior": float(mp.sqrt(ext0)),
            "L_for_L2": {mp.nstr(e, 2): float(Leps[e]) for e in Leps},
            "L_for_Hdot-1_bound": {mp.nstr(e, 2): float(Lh[e]) for e in Lh}}
OUT["elapsed"] = time.time() - T0
(HERE / "data/t4_314_review_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("done, %.1f s" % (time.time() - T0))
