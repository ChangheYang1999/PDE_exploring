"""Erratum check for reviews/CHECK_N4_017_RESIDUAL_IDENTITY_T2.md remark R2 (found by c1-t4, TEAM_NOTE_v282;
accepted with the repair in T4-501, TEAM_NOTE_v283). The 18:07Z note (sha256 bc06d7d8...c2581595) bounded the cross
term by ||r F_n|| ||r Delta psi|| = sqrt(Qn (a + d)); since ||r Delta psi||^2 = n^2 (a + d) (Step 2), the product is
n sqrt(Qn (a + d)). Notation as in arith/n4_017_residual_identity.py; all values divided by pi.
Checked (sympy, exact termwise gamma-function integrals as in that script):
  (a) c1-t4's example n = 3, u = r^3 (1 + r^2)^-3, F_n = Delta(u sin 3 theta): its radial part is
      -48 r^3 (1 + r^2)^-5; d = 6/35, a = 2/63, Qn = cross = 64/35, sqrt(Qn (a + d)) = 64/105, so the old display
      fails by exactly 3 = n, while cross^2 = n^2 Qn (a + d) (equality in Cauchy-Schwarz, F_n = Delta psi);
  (b) there ||r Delta psi||^2 = n^2 (a + d), and the other two R2 bullets, n^2 b^2 <= Qn a and n^2 p^2 <= Qn d, hold;
  (c) for the three examples (D) of arith/n4_017_residual_identity.py: cross = n^2 (b - p) and
      cross^2 <= n^2 Qn (a + d), n^2 b^2 <= Qn a, n^2 p^2 <= Qn d.
No peer code is run.

Run from artifacts/:  python3 -B -u arith/n4_017_r2_erratum.py
Takes no arguments. Output: stdout (logs/n4_017_r2_erratum.log by the README command),
data/n4_017_r2_erratum_results.json.
"""
import json
import sys
import time
from pathlib import Path

import sympy as sp

if len(sys.argv) != 1:
    sys.exit("usage: n4_017_r2_erratum.py (no arguments)")
T0 = time.time()
HERE = Path(__file__).resolve().parents[1]
FAILS, N_ = [], [0]


def check(msg, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


# functions in r and S = 1 + r^2 (dS/dr = 2r); each term c r^m S^-sigma integrated by
# int_0^oo r^m S^-sigma dr = Gamma(a) Gamma(sigma - a)/(2 Gamma(sigma)), a = (m + 1)/2, each term convergent on its own
r, S = sp.symbols("r S", positive=True)
D = lambda e: sp.diff(e, r) + 2 * r * sp.diff(e, S)
TERMWISE = [True]


def I0(e):
    tot = 0
    for t in sp.Add.make_args(sp.expand(e)):
        c, pw = sp.Integer(1), {r: 0, S: 0}
        for fac in sp.Mul.make_args(t):
            b_, e_ = fac.as_base_exp()
            if b_ in (r, S):
                pw[b_] += e_
            else:
                c *= fac
        a_, sg = (pw[r] + 1) / sp.Integer(2), -pw[S]
        if not (a_ > 0 and sg - a_ > 0 and c.is_Rational):
            TERMWISE[0] = False
            return sp.nan
        tot += c * sp.gamma(a_) * sp.gamma(sg - a_) / (2 * sp.gamma(sg))
    return sp.nsimplify(sp.simplify(tot))


check("integrator: int_0^oo r S^-2 dr = 1/2, int r^3 S^-3 dr = 1/4, int r^2 S^(-5/2) dr = 1/3",
      I0(r * S ** -2) == sp.Rational(1, 2) and I0(r ** 3 * S ** -3) == sp.Rational(1, 4)
      and I0(r ** 2 * S ** sp.Rational(-5, 2)) == sp.Rational(1, 3))


def parts(nn, uu, ff):          # all values divided by pi
    up_, upp_ = D(uu), D(D(uu))
    lap = upp_ + up_ / r - nn ** 2 * uu / r ** 2
    return {"d": I0(r * up_ ** 2 + nn ** 2 * uu ** 2 / r), "p": I0(r * ff * uu),
            "a": I0(r * (up_ ** 2 + (r * upp_ + up_) ** 2 / nn ** 2)),
            "b": I0(r ** 2 * ff * (r * upp_ + up_)) / nn ** 2, "Q": I0(r ** 3 * ff ** 2),
            "cross": I0(r ** 3 * ff * lap), "L": I0(r ** 3 * lap ** 2)}


def bounds(nn, P):
    return (P["cross"] == nn ** 2 * (P["b"] - P["p"]) and P["cross"] ** 2 <= nn ** 2 * P["Q"] * (P["a"] + P["d"])
            and nn ** 2 * P["b"] ** 2 <= P["Q"] * P["a"] and nn ** 2 * P["p"] ** 2 <= P["Q"] * P["d"])


# (a), (b) c1-t4's example
uu = r ** 3 * S ** -3
ff = sp.simplify(D(D(uu)) + D(uu) / r - 9 * uu / r ** 2)
check("(a) n = 3, u = r^3 S^-3: the radial part of Delta(u sin 3 theta) is -48 r^3 S^-5",
      sp.simplify(ff.subs(S, 1 + r ** 2) + 48 * r ** 3 * (1 + r ** 2) ** -5) == 0)
ff = -48 * r ** 3 * S ** -5
P = parts(3, uu, ff)
old = sp.sqrt(P["Q"] * (P["a"] + P["d"]))
check("(a) d = %s, a = %s, Qn = %s, cross = %s; sqrt(Qn (a + d)) = %s" % (P["d"], P["a"], P["Q"], P["cross"], old),
      TERMWISE[0] and P["d"] == sp.Rational(6, 35) and P["a"] == sp.Rational(2, 63) and P["Q"] == sp.Rational(64, 35)
      and P["cross"] == sp.Rational(64, 35) and old == sp.Rational(64, 105))
check("(a) the 18:07Z display fails: cross = 3 sqrt(Qn (a + d)) > sqrt(Qn (a + d)); the corrected bound holds with "
      "equality: cross^2 = n^2 Qn (a + d)",
      P["cross"] == 3 * old and P["cross"] > old and P["cross"] ** 2 == 9 * P["Q"] * (P["a"] + P["d"]))
check("(b) ||r Delta psi||^2 = %s = n^2 (a + d); p = -d = %s, b = a = %s; n^2 b^2 <= Qn a, n^2 p^2 <= Qn d"
      % (P["L"], P["p"], P["b"]),
      P["L"] == 9 * (P["a"] + P["d"]) and P["p"] == -P["d"] and P["b"] == P["a"] and bounds(3, P))
EX = {"t4_n3": {k: str(x) for k, x in P.items()}}
# (c) the examples (D) of arith/n4_017_residual_identity.py
for name, nn, uu, ff in (("n1_k-1", 1, r * S ** sp.Rational(-3, 2), r * S ** -3),
                         ("n1_k0", 1, r ** 3 * S ** -2, r * (1 - r ** 2) * S ** -3 / 3),
                         ("n3_k0", 3, r ** 3 * S ** -3, r ** 3 * S ** -4)):
    P = parts(nn, uu, ff)
    EX[name] = {k: str(x) for k, x in P.items()}
    check("(c) %s: cross = n^2 (b - p) = %s; cross^2 <= n^2 Qn (a + d), n^2 b^2 <= Qn a, n^2 p^2 <= Qn d (exact)"
          % (name, P["cross"]), TERMWISE[0] and all(x.is_Rational for x in P.values()) and bounds(nn, P))
el = time.time() - T0
print("%d checks, %d FAIL, %.2f s" % (N_[0], len(FAILS), el))
OUT = {"examples": EX, "checks": N_[0], "fails": FAILS, "elapsed_s": round(el, 2)}
(HERE / "data/n4_017_r2_erratum_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
sys.exit(1 if FAILS else 0)
