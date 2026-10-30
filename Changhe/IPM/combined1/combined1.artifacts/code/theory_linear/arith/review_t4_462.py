"""Reciprocal check of c1-t4 T4-462 (weight-uniform Gram budgets: exact AM-GM elimination of w1 and w2; TEAM_NOTE_v239).

(A) inputs: PROOF.md, verification/result.json (sha256 asserted as printed in TEAM_NOTE_v239), data/parameters.json.
(B) the algebra of PROOF.md (4)-(6), symbolically with sympy: the determinant expansion, the substitution identity
    (5), 9z + S^2/z - 6S = (3z - S)^2/z, 36E + 60 O a + 25 a^2 = 1440 p + (6O + 5a)^2, and det G = 0 with a positive
    definite leading 2x2 block at the stated equality point.
(C) cross-check with c1-t2's own WU3 cell bound (arith/h18_wu_sharp.py, text up to 'ROWS = [' executed unchanged, sha256
    asserted): on degenerate cells [mu, mu] its minimum over w1 equals T4-462's closed form W(mu) at 9 points per row.
(D) own certification of the seven ceilings of data/parameters.json by exact rational cell bounds, not by Bernstein form:
    on [mu_a, mu_b] the right side of (8) is at most 4 mu_b^3 c(mu_a) p(mu_a) a(mu_a)^2 / (27 k u^2 (1440 p(mu_b) +
    (6O + 5a(mu_b))^2)), since p, a, c decrease in mu; cells are bisected until every leaf is below bound^2. Also: a
    lower witness of the supremum of (8) (exact value at a float argmax), a second bisection certificate that the
    supremum is below witness (1 + 2e-7), so its square root is known to relative 1e-7, the relative excess of each
    stated bound over it, the gain factors over the exact registered family
    ceilings (data/family_ceilings_exact_results.json), the 007 factors and the H18 factors, all by exact rational
    comparison; and the constants of PROOF.md (10)-(11) equal c1-t2's K00 and A' + B'.

Run from artifacts/:  python3 -B -u arith/review_t4_462.py
Takes no arguments. Needs python-flint and sympy. Reads, read only: ../../c1-t4/research/weight_uniform_gram_audit/
{PROOF.md, verification/result.json (sha256 asserted), data/parameters.json, code/check.py (sha256 recorded, never
executed)}, arith/h18_wu_sharp.py and the files it pins, data/family_ceilings_exact_results.json.
Output: stdout (logs/review_t4_462.log by the README command), data/review_t4_462_results.json.
"""
import hashlib
import json
import math
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

if len(sys.argv) != 1:
    sys.exit("usage: review_t4_462.py (no arguments)")
T0 = time.time()
HERE_ = Path(__file__).resolve().parents[1]
SH = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
WS = HERE_ / "arith/h18_wu_sharp.py"
H_WS = "a4f9f9f0191b9209a3da426f9347865418186f490423736b53649f35087f1197"
assert SH(WS) == H_WS, "h18_wu_sharp.py changed"
src_ws = WS.read_text()
ns = {"__file__": str(WS), "__name__": "h18_wu_sharp_prefix"}
exec(compile(src_ws[:src_ws.index("ROWS = [")], str(WS), "exec"), ns)
check, N_, FAILS, arb = ns["check"], ns["N_"], ns["FAILS"], ns["arb"]
D462 = HERE_.parent.parent / "c1-t4/research/weight_uniform_gram_audit"
PIN = {"PROOF.md": "3c871d7f9ef82ba6b6fb925cf73a31cda678805cadc2c8a91f9659b2e2f3030c",
       "verification/result.json": "61803920bea366913555ebb213ac40b466d370b1c92dd5cfe9cc9b67b9895450"}
for k, h in PIN.items():
    check("(A) sha256 of T4-462 %s is %s...%s (TEAM_NOTE_v239)" % (k, h[:8], h[-8:]), SH(D462 / k) == h)
OUT = {"inputs": {"arith/h18_wu_sharp.py": H_WS}}
for k in list(PIN) + ["data/parameters.json", "code/check.py"]:
    OUT["inputs"]["c1-t4/research/weight_uniform_gram_audit/" + k] = SH(D462 / k)
PR = (D462 / "PROOF.md").read_text()
PAR = json.loads((D462 / "data/parameters.json").read_text())
RES = json.loads((D462 / "verification/result.json").read_text())
check("(A) T4-462 result.json: 320 checks, verdict begins 'CONFIRMED all seven necessary ceilings'",
      RES["check_count"] == 320 and RES["verdict"].startswith("CONFIRMED all seven necessary ceilings"))
for qq in ("G(mu)=[[m2-mu,-O,-5],[-O,w1*(m1-mu)-40,-3*w1],", "[-5,-3*w1,w2*(beta-mu)]] is positive semidefinite, O=347/10.",
           "det G=w2*c*z-[9p*w1^2+(30O+25a)*w1-1000].", "9z^2+(18E+30O*a+25a^2)z+(3E+5O*a)^2.",
           "w2 >= [1440p+(6O+5a)^2]/(c*p*a^2) =: W(mu).", "||h||2^2 < 4mu^3*c*p*a^2/[27*k*u^2*(1440p+(6O+5a)^2)].",
           "K=2dtop+6c8+24(cr+2k1)+32k1.", "v=(4/5)q0+q0*(1+4W*M*sigma)+(19/5)P0."):
    check("(A) PROOF.md quote '%s'" % qq, qq in PR)

# ---------------------------------------------------------------- (B) the algebra, symbolically
p, a, c, w1, w2, z = sp.symbols("p a c w1 w2 z", positive=True)
O = sp.Rational(347, 10)
G = sp.Matrix([[p, -O, -5], [-O, w1 * a - 40, -3 * w1], [-5, -3 * w1, w2 * c]])
E = 40 * p + O**2
zz = p * (a * w1 - 40) - O**2
br = 9 * p * w1**2 + (30 * O + 25 * a) * w1 - 1000
check("(B) (4): det G = w2 c z - [9 p w1^2 + (30 O + 25 a) w1 - 1000] with z = p q - O^2 = p a w1 - E (sympy)",
      sp.expand(G.det() - (w2 * c * zz - br)) == 0 and sp.expand(zz - (p * a * w1 - E)) == 0 and 30 * O == 1041)
S = 3 * E + 5 * O * a
w1z = (z + E) / (p * a)
check("(B) (5): bracket(w1 = (z + E)/(p a)) * p a^2 = 9 z^2 + (18E + 30 O a + 25 a^2) z + (3E + 5 O a)^2 (sympy)",
      sp.expand(br.subs(w1, w1z) * p * a**2 - (9 * z**2 + (18 * E + 30 * O * a + 25 * a**2) * z + S**2)) == 0)
check("(B) (6): 9z + S^2/z - 6S = (3z - S)^2/z and 6S + 18E + 30 O a + 25 a^2 = 1440 p + (6O + 5a)^2 (sympy)",
      sp.simplify(9 * z + S**2 / z - 6 * S - (3 * z - S)**2 / z) == 0
      and sp.expand(6 * S + 18 * E + 30 * O * a + 25 * a**2 - (1440 * p + (6 * O + 5 * a)**2)) == 0)
Wmu = (1440 * p + (6 * O + 5 * a)**2) / (c * p * a**2)
w1s = (2 * E + 5 * O * a / 3) / (p * a)
Gs = G.subs({w1: w1s, w2: Wmu})
check("(B) at w1 = (2E + 5 O a/3)/(p a), w2 = W: z = S/3, det G = 0, leading 2x2 minor = z > 0 (sympy)",
      sp.simplify(zz.subs(w1, w1s) - S / 3) == 0 and sp.simplify(Gs.det()) == 0
      and sp.simplify(Gs[:2, :2].det() - S / 3) == 0)

# ---------------------------------------------------------------- (C) cross-check with c1-t2's WU3 cell minimum
w2lo3 = ns["w2lo3"]


def W_exact(mu, m2, m1, bL):
    pp, aa, cc = m2 - mu, m1 - mu, bL - mu
    return (1440 * pp + (6 * Fr(347, 10) + 5 * aa)**2) / (cc * pp * aa**2)


ok, worst = True, 0.0
for row in PAR["rows"]:
    m2, m1, bL = Fr(row["m2"]), Fr(row["m1"]), Fr(row["beta"])
    for kk in range(1, 10):
        mu = m2 * Fr(kk, 10)
        mine = w2lo3(mu, mu, m2, m1, bL)
        th = W_exact(mu, m2, m1, bL)
        rel = abs(float(((mine - ns["A_"](th)) / ns["A_"](th)).mid()))
        worst = max(worst, rel)
        ok &= rel < 1e-60
check("(C) c1-t2 WU3 minimum over w1 on degenerate cells equals T4-462's W(mu) at 9 points of each of the 7 rows "
      "(max relative difference %.1e)" % worst, ok)

# ---------------------------------------------------------------- (D) the seven ceilings, own exact cell bounds
k, u = Fr(PAR["K_lower"]), Fr(PAR["cU_lower"])
check("(D) T4-462 k = 39068/100 < K00 lower end and u = 15871/10000 < A' + B' lower end (c1-t2 constants; (10)-(11) "
      "are the same formulas term by term)", ns["A_"](k) < ns["K_lo"] and ns["A_"](u) < ns["cU_lo"]
      and k == Fr(39068, 100) and u == Fr(15871, 10000))
check("(D) T4-462 Arb values K = %s, v = %s agree with c1-t2's K00, A' + B' to 1e-60"
      % (RES["K"][:14], RES["v"][:12]), abs(float((arb(RES["K"]) - ns["K00"]).mid())) < 1e-60
      and abs(float((arb(RES["v"]) - (ns["Ap"] + ns["Bp"])).mid())) < 1e-60)
FC = json.loads((HERE_ / "data/family_ceilings_exact_results.json").read_text())["ceilings"]


def fam_sq(name):
    m = FC[name]
    mu0, C, cU, sw = Fr(m["mu0"]), Fr(m["C"]), Fr(m["c_U"]), Fr(m["sqrt_W2"])
    return 4 * mu0**3 / (27 * C * cU**2 * sw**2)


def f8(mu, m2, m1, bL):
    pp, aa, cc = m2 - mu, m1 - mu, bL - mu
    return 4 * mu**3 * cc * pp * aa**2 / (27 * k * u**2 * (1440 * pp + (6 * Fr(347, 10) + 5 * aa)**2))


D007, LEAST = Fr(PAR["d007"]), Fr(PAR["old_H18_minimum"])
O10 = Fr(347, 10)


def cell_ub(ma, mb, m2, m1, bL):
    pa_, aa_, ca_ = m2 - ma, m1 - ma, bL - ma
    pb_, ab_ = m2 - mb, m1 - mb
    return 4 * mb**3 * ca_ * pa_ * aa_**2 / (27 * k * u**2 * (1440 * pb_ + (6 * O10 + 5 * ab_)**2))


def certify(target, m2, m1, bL):
    """adaptive bisection: True if every leaf has its exact cell upper bound below target and the leaves cover [0, m2]"""
    todo, leaves, maxdepth, ok_cert = [(Fr(0), m2, 0)], [], 0, True
    while todo:
        ma, mb, dep = todo.pop()
        if cell_ub(ma, mb, m2, m1, bL) < target:
            leaves.append((ma, mb))
            maxdepth = max(maxdepth, dep)
        elif dep < 48:
            mid = (ma + mb) / 2
            todo += [(ma, mid, dep + 1), (mid, mb, dep + 1)]
        else:
            ok_cert = False
            break
    leaves.sort()
    cover = ok_cert and leaves[0][0] == 0 and leaves[-1][1] == m2 and all(
        leaves[i][1] == leaves[i + 1][0] for i in range(len(leaves) - 1))
    return cover, len(leaves), maxdepth


OUT["rows"] = []
for row in PAR["rows"]:
    m2, m1, bL, b = Fr(row["m2"]), Fr(row["m1"]), Fr(row["beta"]), Fr(row["bound"])
    cover, nleaves, maxdepth = certify(b**2, m2, m1, bL)
    # a lower witness of the supremum: golden-section search in floats, then exact evaluation of (8)
    lo_, hi_ = 0.0, float(m2)
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        x1, x2 = hi_ - g * (hi_ - lo_), lo_ + g * (hi_ - lo_)
        if float(f8(Fr(x1), m2, m1, bL)) < float(f8(Fr(x2), m2, m1, bL)):
            lo_ = x1
        else:
            hi_ = x2
    mu_s = Fr((lo_ + hi_) / 2)
    wit = f8(mu_s, m2, m1, bL)
    excess = 1 - math.sqrt(float(wit / b**2))
    # the supremum itself: certified below wit (1 + 2e-7), so sqrt(sup) lies in [sqrt(wit), sqrt(wit) (1 + 1e-7)]
    cov2, nl2, md2 = certify(wit * (1 + Fr(2, 10**7)), m2, m1, bL)
    pp, aa = m2 - mu_s, m1 - mu_s
    w1o = (2 * (40 * pp + O10**2) + 5 * O10 * aa / 3) / (pp * aa)
    w2o = W_exact(mu_s, m2, m1, bL)
    check("(D) %s: at the witness mu the AM-GM point w1* = %.1f >= 2, w2 = W(mu) = %.1f >= 1, so the side constraints "
          "w1 >= 2, w2 >= 1 do not bind there" % (row["label"], float(w1o), float(w2o)), w1o >= 2 and w2o >= 1)
    gain_ok = b**2 <= Fr(row["gain"])**2 * fam_sq(row["family"])
    fac_ok = D007 >= Fr(row["factor"]) * b
    h18_ok = ("old_H18_factor" not in row) or LEAST >= Fr(row["old_H18_factor"]) * b
    check("(D) %s: sup over mu of (8) < bound^2 by %d exact bisection leaves covering [0, m2] (depth <= %d); lower "
          "witness %.7e at mu = %.6f, so the bound %.4e lies %.2e (relative) above the supremum"
          % (row["label"], nleaves, maxdepth, math.sqrt(float(wit)), float(mu_s), float(b), excess),
          cover and wit < b**2 and 0 < excess < 3e-4)
    check("(D) %s: sup over mu of (8) < witness^2 (1 + 2e-7) by %d exact bisection leaves (depth <= %d), so the square "
          "root of the supremum lies in [%.7e, %.7e]" % (row["label"], nl2, md2, math.sqrt(float(wit)),
                                                        math.sqrt(float(wit)) * (1 + 1e-7)), cov2)
    check("(D) %s: gain %s over the exact %s ceiling, 007 factor %s%s (exact rational comparisons)"
          % (row["label"], row["gain"], row["family"], row["factor"],
             (", H18 factor %s" % row["old_H18_factor"]) if "old_H18_factor" in row else ""), gain_ok and fac_ok and h18_ok)
    OUT["rows"].append({"label": row["label"], "bound": row["bound"], "sup_lower_witness": "%.10e" % math.sqrt(float(wit)),
                        "argmax_mu": "%.8f" % float(mu_s), "relative_excess_of_bound": "%.3e" % excess,
                        "leaves": nleaves, "max_depth": maxdepth, "sup_certified_below_witness_times": "1+1e-7",
                        "sup_leaves": nl2, "sup_max_depth": md2})
c0 = Fr(4076476460239181, 2251799813685248)
check("(D) bL rows: beta = 1 + c0 = 6328276273924429/2251799813685248 and 57/20; 41069/10^10 < 1/1000/243",
      Fr(PAR["rows"][5]["beta"]) == 1 + c0 and Fr(PAR["rows"][6]["beta"]) == Fr(57, 20)
      and Fr(41069, 10**10) * 243 < Fr(1, 1000))
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N_[0], FAILS, round(time.time() - T0, 3)
(HERE_ / "data/review_t4_462_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N_[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
