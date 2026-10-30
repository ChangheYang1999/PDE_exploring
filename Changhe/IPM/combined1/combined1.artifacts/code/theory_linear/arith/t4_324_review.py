"""Checks for reviews/REVIEW_T4_324.md (c1-t4 research/homogeneous_tail_surgery/PROOF.md, T4-324).

A  exact exponents q1, q2, q3, potential homogeneities a1, a2, condition (1), H_m != 0, 1 - c q != 0, and the
   exponent inequalities of Section 4 (fractions); sympy check of formula (4) and of the polar density formula.
B  exact (fmpq): my constructor of REVIEW_T4_294 (arith/t4_294_review.py, executed up to its part C loop) on the raw
   c1-n1 file of 007 gives Theta_(4,1) and F_(9,0). B1 = F_(4,1)/(1 - c q1) and B2 = F_(9,0)/(1 - c q2). My forward
   density map (the polar formula, checked in A) applied to c1-t4's stored potentials must give B1 and B2 exactly,
   and their stored densities; my own descending solve must give their potentials; at q1, p_m = -A1_m.
C  FLOAT (mpmath): C_(0,0) = ||h_1||_2 for the second (q2) cutoff with the cutoff of the PROOF.
"""
import hashlib
import json
import random
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import fmpq

sys.set_int_max_str_digits(0)
T0 = time.time()
HERE = Path(__file__).resolve().parents[1]
SRC = Path("RUN_ROOT/theory_audit_T4/research/homogeneous_tail_surgery")
T295 = Path("RUN_ROOT/theory_audit_T4/research/forced_integrable_tail/data/007_tail_repair.json")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(SRC / "PROOF.md") == "966279c233b843e49d321764be482ccaf4ddd01436f23b421d1ea49aaae8aa27"
DREP = SRC / "data/007_homogeneous_repairs.json"
assert sha(DREP) == "66ce47c8ba9cfb07cae14507cd0b2960ff9cd758f3f3e97755b671fc10e4f60c"
assert sha(T295) == "bad9b06a64a3f045e3de487d63793f8ec0c6b021a692c5e11cea91279ed5fcd6"
OUT = {}

# ---------------- A: exact exponents and formula (4)
c = Fr(4076476460239181, 2**51)
g = 1 / c
dl = 1 - g
q1, q2, q3 = -1 - 4 * dl, 1 - 9 * dl, -1 - 5 * dl
a1, a2 = q1 + 3, q2 + 3
assert q1 == Fr(-11375183046454913, 4076476460239181) and q2 == Fr(-12345613358746216, 4076476460239181)
assert q3 == 5 * g - 6 == 1 - 5 * dl - 2                       # q3 is the exponent of sector (5,1)
assert q1 - dl == q3 < q2 and 2 * q1 - 1 < q2 and q2 - dl < q3 and 2 * q2 - 1 < q3 and q1 + q2 - 1 < q3
assert q2 - dl == 1 - 10 * dl                                   # sector (10,0)
assert g - 4 < q3 < q2 < -3 < q1 < -2
assert 0 < a1 < 2 and -2 < a2 < 0


def Hm(a, m):
    return -a * a * (a - 2) if m == 0 else -(a * a - 4 * m * m) * (a - 2 - 2 * m) / 2


def Jm(a, m):
    return (a * a - 4 * m * m) * (a - 2 + 2 * m) / 2


for a, M in ((a1, 39), (a2, 89)):
    assert a != 0 and all(a != 2 * m and a != -2 * m for m in range(1, M + 1))
    assert all(Hm(a, m) != 0 for m in range(M + 1))
assert 1 - c * q1 != 0 and 1 - c * q2 != 0
OUT["A"] = {"q1": str(q1), "q2": str(q2), "q3": str(q3), "a1": str(a1), "a2": str(a2),
            "a1_float": float(a1), "a2_float": float(a2), "one_minus_cq1": float(1 - c * q1),
            "one_minus_cq2": float(1 - c * q2), "one_minus_cq3": float(1 - c * q3)}
print("A  q1 = %.12f, q2 = %.12f, q3 = 5g - 6 = %.12f, q2 - delta = 1 - 10 delta = %.12f; a1 = %.12f, a2 = %.12f;"
      " 1 - c q = %.9f, %.9f, %.9f; condition (1) and H_m != 0 for M = 39 (a1), 89 (a2): True"
      % (float(q1), float(q2), float(q3), float(q2 - dl), float(a1), float(a2), float(1 - c * q1),
         float(1 - c * q2), float(1 - c * q3)))

x, y, d, s = sp.symbols("x y d s", real=True)
r2 = x**2 + y**2
th = sp.atan2(y, x)
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2)
random.seed(324)
mp.mp.dps = 40
for n in range(7):
    base = r2 ** (d / 2) * sp.chebyshevt(n, x / sp.sqrt(r2))           # r^d cos(n theta)
    rhs4 = r2 ** ((d - 1) / 2) * (-(d - n) * sp.sin((n + 1) * th) + (d + n) * sp.sin((n - 1) * th)) / 2
    f4 = -sp.diff(base, y) - rhs4
    fl = sp.lambdify((x, y, d), f4, "mpmath")
    for _ in range(3):
        px, py, dv = (mp.mpf(random.randint(1, 30)) / 7, mp.mpf(random.randint(-30, 30)) / 11,
                      mp.mpf(random.randint(-40, 40)) / 13)
        assert abs(fl(px, py, dv)) < 1e-30
    # density of r^s cos(n theta), n = 2m: sin((n+1)) coefficient H_m and sin((n-1)) coefficient J_m (n >= 2)
    if n % 2 == 0:
        m = n // 2
        hm = -sp.diff(lap(base.subs(d, s)), y)
        Hs = -s * s * (s - 2) if m == 0 else -(s * s - 4 * m * m) * (s - 2 - 2 * m) / 2
        Js = (s * s - 4 * m * m) * (s - 2 + 2 * m) / 2
        pred = r2 ** ((s - 3) / 2) * (Hs * sp.sin((n + 1) * th) + (Js * sp.sin((n - 1) * th) if m else 0))
        fd_ = sp.lambdify((x, y, s), hm - pred, "mpmath")
        for _ in range(3):
            px, py, sv = (mp.mpf(random.randint(1, 30)) / 7, mp.mpf(random.randint(-30, 30)) / 11,
                          mp.mpf(random.randint(-40, 40)) / 23)
            assert abs(fd_(px, py, sv)) < 1e-28
print("A  (4): -d_y[r^d cos(n theta)] = r^(d-1)[-(d-n) sin((n+1) theta) + (d+n) sin((n-1) theta)]/2, n = 0..6, and"
      " -d_y Lap[r^s cos(2m theta)] = r^(s-3)[H_m sin((2m+1) theta) + J_m sin((2m-1) theta)], m = 0..3, at random"
      " rational points (40 digits): True")


def forward(a, pot):            # density of r^a sum_m p_m cos(2 m theta), as odd sine coefficients (exact)
    out = {}
    for m, p in pot.items():
        for n, co in ((2 * m + 1, Hm(a, m)), (2 * m - 1, Jm(a, m) if m else 0)):
            if co and p:
                out[n] = out.get(n, 0) + co * p
    return {n: v for n, v in out.items() if v != 0}


def solve(a, B):                # my descending substitution
    M = (max(B) - 1) // 2
    p, nxt = {}, 0
    for m in range(M, -1, -1):
        p[m] = (B.get(2 * m + 1, 0) - (Jm(a, m + 1) * nxt if m < M else 0)) / Hm(a, m)
        nxt = p[m]
    return {m: v for m, v in p.items() if v != 0}


# ---------------- B: exact comparison with my constructor
t1 = time.time()
src294 = (HERE / "arith/t4_294_review.py").read_text()
assert sha(HERE / "arith/t4_294_review.py") == "229c9bd070a868ec627021c41f08967d61603af807d7d7d7f0616ca03a3b950c"
cut = src294.index("\nRES = {}\n")
ns = {"__file__": str(HERE / "arith/t4_294_review.py"), "__name__": "t4_294_prefix"}
exec(compile(src294[:cut], "t4_294_review.py (prefix)", "exec"), ns)
fn = "c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json"
assert ns["sha"](HERE / "data" / fn) == ns["EXPECT"]["007"]
c_, chi = ns["load_file"](fn)
assert c_ == fmpq(c.numerator, c.denominator)
delta, R, S = ns["build"](c_, chi)
expo = lambda K, L: 1 - K * delta - 2 * L
Th, Ps = ns["sectors"](R, S, delta)
F = ns["residuals"](Th, Ps, [(4, 1), (9, 0)], expo, c_)
tofr = lambda v: Fr(int(v.p), int(v.q))
Theta41 = {n: tofr(v) for n, v in Th[(4, 1)].items()}
F41 = {n: tofr(v) for n, v in F[(4, 1)].items()}
F90 = {n: tofr(v) for n, v in F[(9, 0)].items()}
assert F41 == {n: (c * q1 - 1) * v for n, v in Theta41.items()}
B1 = {n: v / (1 - c * q1) for n, v in F41.items()}
B2 = {n: v / (1 - c * q2) for n, v in F90.items()}
assert B1 == {n: -v for n, v in Theta41.items()}
print("B  my constructor (007, %.1f s): F_(4,1) = (c q1 - 1) Theta_(4,1) (%d modes, top %d); F_(9,0) has %d odd sine"
      " modes, top %d" % (time.time() - t1, len(F41), max(F41), len(F90), max(F90)))

dat = json.loads(DREP.read_text())
assert dat["candidate"] == "007" and Fr(dat["c_exact"]) == c
A1 = {int(t["m"]): Fr(t["A1"]) for t in json.loads(T295.read_text())["moment_checks"]}
res = {}
for rep, (K, L), q, a, Bmine in ((dat["repairs"][0], (4, 1), q1, a1, B1), (dat["repairs"][1], (9, 0), q2, a2, B2)):
    assert rep["sector"] == [K, L] and Fr(rep["q"]) == q and Fr(rep["potential_homogeneity"]) == a
    dens = {int(k): Fr(v) for k, v in rep["density"].items()}
    pot = {int(k): Fr(v) for k, v in rep["potential_cosine_coefficients"].items()}
    fwd = forward(a, pot)
    sol = solve(a, Bmine)
    chk = {"density_equals_mine": dens == Bmine, "forward_of_stored_potential_equals_mine": fwd == Bmine,
           "my_solve_equals_stored_potential": sol == pot, "n_density": len(dens), "top_density": max(dens),
           "n_potential": len(pot), "top_potential_m": max(pot),
           "density_norm": float(mp.sqrt(mp.pi * sum(mp.mpf(v.numerator) / v.denominator * mp.mpf(v.numerator)
                                                     / v.denominator for v in dens.values()))),
           "potential_l2": float(mp.sqrt(sum((mp.mpf(v.numerator) / v.denominator)**2 for v in pot.values())))}
    if (K, L) == (4, 1):
        chk["potential_equals_minus_A1"] = pot == {m: -v for m, v in A1.items()}
    res["%d,%d" % (K, L)] = chk
    print("B  (%d,%d): stored density = my B exactly: %s; forward map of stored potential = my B: %s; my descending"
          " solve = stored potential: %s; %d density modes (top %d), %d potential modes (m <= %d); density circle"
          " norm %.9g; potential l2 %.9g%s"
          % (K, L, chk["density_equals_mine"], chk["forward_of_stored_potential_equals_mine"],
             chk["my_solve_equals_stored_potential"], len(dens), max(dens), len(pot), max(pot),
             chk["density_norm"], chk["potential_l2"],
             "; p_m = -A1_m: %s" % chk["potential_equals_minus_A1"] if (K, L) == (4, 1) else ""))
    assert chk["density_equals_mine"] and chk["forward_of_stored_potential_equals_mine"]
    assert chk["my_solve_equals_stored_potential"]
assert res["4,1"]["potential_equals_minus_A1"]
OUT["B"] = res

# ---------------- C: FLOAT constant C_(0,0) for the q2 cutoff (chi_1 = zeta r^a2 P2)
mp.mp.dps = 30
pot2 = [(m, mp.mpf(v.numerator) / v.denominator) for m, v in
        sorted((int(k), Fr(v)) for k, v in dat["repairs"][1]["potential_cosine_coefficients"].items())]
rr = sp.symbols("rr", positive=True)
b1 = sp.exp(-1 / (rr - 1))
b2 = sp.exp(-1 / (2 - rr))
zeta = b1 / (b1 + b2)
f = zeta * rr ** sp.Rational(a2.numerator, a2.denominator)
fl = [sp.lambdify(rr, e, "mpmath") for e in [f] + [sp.diff(f, rr, j) for j in (1, 2, 3)]]


def modes(rv):
    f0, f1, f2, f3 = [Fn(rv) for Fn in fl]
    out = {}
    for m, pm in pot2:
        gm = f2 + f1 / rv - 4 * m * m * f0 / rv**2
        gp = f3 + f2 / rv - f1 / rv**2 - 4 * m * m * (f1 / rv**2 - 2 * f0 / rv**3)
        for n, co in ((2 * m + 1, (gp - 2 * m * gm / rv) / 2), (2 * m - 1, -(gp + 2 * m * gm / rv) / 2)):
            if n < 0:
                n, co = -n, -co
            out[n] = out.get(n, 0) - pm * co
    return out


B2m = {n: mp.mpf(v.numerator) / v.denominator for n, v in B2.items()}
q2m = mp.mpf(q2.numerator) / q2.denominator
rt = mp.mpf("1.99999999")
md2 = modes(rt)
rel = max(abs(md2.get(n, 0) - B2m[n] * rt**q2m) for n in B2m) / max(abs(v) for v in B2m.values())
assert rel < 1e-6
t2 = time.time()
ann0 = mp.quad(lambda rv: mp.pi * sum(v * v for v in modes(rv).values()) * rv, [1, 1.25, 1.5, 1.75, 2])
pn2 = mp.pi * sum(v * v for v in B2m.values())
ext0 = pn2 * mp.mpf(2) ** (2 * q2m + 2) / (-2 * q2m - 2)
C00 = mp.sqrt(ann0 + ext0)
Leps = {e: (C00 / e) ** (1 / (-q2m - 1)) for e in (mp.mpf("1e-3"), mp.mpf("1e-6"))}
print("C  q2 cutoff: annulus modes at r = 2 - 1e-8 against r^q2 B2: max relative difference %s; C_(0,0) = %s"
      " (annulus %s, exterior %s; quadrature %.1f s)"
      % (mp.nstr(rel, 3), mp.nstr(C00, 10), mp.nstr(mp.sqrt(ann0), 10), mp.nstr(mp.sqrt(ext0), 10), time.time() - t2))
for e in Leps:
    print("   ||h_L2||_2 < %s needs L2 > %s" % (mp.nstr(e, 2), mp.nstr(Leps[e], 8)))
OUT["C"] = {"C2_rel": float(rel), "C00": float(C00), "C00_annulus": float(mp.sqrt(ann0)),
            "C00_exterior": float(mp.sqrt(ext0)), "L2_for_L2norm": {mp.nstr(e, 2): float(Leps[e]) for e in Leps}}
OUT["elapsed"] = time.time() - T0
(HERE / "data/t4_324_review_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("done, %.1f s" % (time.time() - T0))
