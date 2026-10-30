"""Check for revision 2 of reviews/REVIEW_T4_469.md: the counterexample of c1-t4 T4-475
(research/divergence_free_upper_review_acceptance/PROOF.md, section "One necessary-condition wording is false") to the
sentence "r Delta psi is in L^2 exactly when beta_min > 3/2" of REVIEW_T4_469 section 1.5.

Example: n = 3, u = r^3 (1+r^2)^(-3/2) (1 - t) with t = r^2/(1+r^2), which equals r^3 (1+r^2)^(-5/2). Written as two
terms in T4-469's form, both have beta = 3/2, but the sum decays like r^-2. Checked exactly (sympy):
  - the two forms agree; the profile is smooth at the origin (r^3 sin(3 theta) = Im (x + i y)^3);
  - for F = -Delta psi, psi = u sin(3 theta): d/pi = 5/12, a/pi = 25/432, M2/pi = int r^3 f^2 dr / 9 = 205/432 = d + a
    (T4-475's values), so grad psi and r Delta psi are in L^2;
  - each of the two terms alone has u ~ const at infinity and int r^3 f^2 dr and d infinite (log divergent), so the
    sufficient condition on the ungrouped terms is not necessary for their sum.
No c1-t4 code is executed. Read only: the T4-475 PROOF.md (sha256 asserted).

Run from artifacts/:  python3 -B -u arith/review_t4_469_rev2.py
Takes no arguments. Needs sympy. Output: stdout (logs/review_t4_469_rev2.log by the README command),
data/review_t4_469_rev2_results.json.
"""
import hashlib
import json
import sys
import time
from pathlib import Path

import sympy as sp

if len(sys.argv) != 1:
    sys.exit("usage: review_t4_469_rev2.py (no arguments)")
T0 = time.time()
HERE_ = Path(__file__).resolve().parents[1]
SRC = HERE_.parent.parent / "c1-t4/research/divergence_free_upper_review_acceptance/PROOF.md"
PIN = "5f3dbd5fd86235ef97212a2ed460c927d82f435ccdc8c2f54a212f52269fe63c"
FAILS, N_ = [], [0]


def check(msg, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


check("sha256 of T4-475 PROOF.md is %s...%s" % (PIN[:8], PIN[-8:]),
      hashlib.sha256(SRC.read_bytes()).hexdigest() == PIN)
text = SRC.read_text()
check("T4-475 states the example u=r^3(1+r^2)^(-3/2)(1-t)=r^3(1+r^2)^(-5/2), t=r^2/(1+r^2), n=3",
      "u=r^3(1+r^2)^(-3/2)(1-t)=r^3(1+r^2)^(-5/2)" in text and "t=r^2/(1+r^2)" in text and "take n=3" in text)
r = sp.symbols("r", positive=True)
X, Y = sp.symbols("x y", real=True)
n = 3
t = r ** 2 / (1 + r ** 2)
terms = [r ** 3 * (1 + r ** 2) ** sp.Rational(-3, 2), -r ** 3 * (1 + r ** 2) ** sp.Rational(-3, 2) * t]
u = terms[0] + terms[1]
check("r^3 (1+r^2)^(-3/2) (1 - t) = r^3 (1+r^2)^(-5/2); both ungrouped terms are r^(3+2k) (1-t)^(3/2) times a "
      "polynomial in t (k = 0; P = 1 and P = -t), so beta_min = 3/2",
      sp.simplify(u - r ** 3 * (1 + r ** 2) ** sp.Rational(-5, 2)) == 0)
check("r^3 sin(3 theta) = 3 x^2 y - y^3 = Im (x + i y)^3 (smooth at the origin)",
      sp.expand(sp.im(sp.expand((X + sp.I * Y) ** 3)) - (3 * X ** 2 * Y - Y ** 3)) == 0)


def energies(u):
    f = sp.simplify(-(sp.diff(u, r, 2) + sp.diff(u, r) / r - n ** 2 * u / r ** 2))
    vp = r * sp.diff(u, r)
    vpp = r * sp.diff(vp, r)
    q = lambda e: sp.integrate(sp.simplify(e), (r, 0, sp.oo))
    return f, {"d": q((sp.diff(u, r) ** 2 + n ** 2 * u ** 2 / r ** 2) * r), "a": q((vp ** 2 + vpp ** 2 / n ** 2) / r),
               "M2": q(r ** 3 * f ** 2) / n ** 2}


f, E = energies(u)
check("u = r^3 (1+r^2)^(-5/2), n = 3: d/pi = %s, a/pi = %s, M2/pi = %s = d + a (T4-475: 5/12, 25/432, 205/432)"
      % (E["d"], E["a"], E["M2"]),
      E["d"] == sp.Rational(5, 12) and E["a"] == sp.Rational(25, 432) and E["M2"] == sp.Rational(205, 432)
      and E["M2"] == E["d"] + E["a"])
check("u = O(r^-2) at infinity: lim r^2 u = 1", sp.limit(r ** 2 * u, r, sp.oo) == 1)
div = []
for i, u0 in enumerate(terms):
    f0 = sp.simplify(-(sp.diff(u0, r, 2) + sp.diff(u0, r) / r - n ** 2 * u0 / r ** 2))
    lim_u = sp.limit(u0, r, sp.oo)
    lim_f = sp.limit(r ** 4 * f0 ** 2, r, sp.oo)            # r^3 f^2 ~ lim_f / r
    lim_d = sp.limit(r ** 2 * (sp.diff(u0, r) ** 2 + n ** 2 * u0 ** 2 / r ** 2), r, sp.oo)   # d integrand ~ lim_d / r
    div.append((lim_u, lim_f, lim_d))
check("each ungrouped term alone: u -> %s and %s; r^3 f^2 ~ c/r with c = %s and %s; the d integrand ~ c'/r with c' = %s "
      "and %s; all c, c' nonzero, so int r^3 f^2 dr and d diverge logarithmically for each term"
      % (div[0][0], div[1][0], div[0][1], div[1][1], div[0][2], div[1][2]),
      all(lu != 0 and lf != 0 and ld != 0 and lf.is_finite and ld.is_finite for lu, lf, ld in div))
el = time.time() - T0
print("%d checks, %d FAIL, %.2f s" % (N_[0], len(FAILS), el))
OUT = {"input": {"c1-t4/research/divergence_free_upper_review_acceptance/PROOF.md": PIN},
       "example": "n = 3, u = r^3 (1+r^2)^(-5/2)", "d_over_pi": str(E["d"]), "a_over_pi": str(E["a"]),
       "M2_over_pi": str(E["M2"]), "single_term_limits": [[str(x) for x in d] for d in div],
       "checks": N_[0], "fails": FAILS, "elapsed_s": round(el, 2)}
(HERE_ / "data/review_t4_469_rev2_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
sys.exit(1 if FAILS else 0)
