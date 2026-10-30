"""Independent check of the residual identity of c1-n4 research/candidate017_dual_residual_replay/PROOF.md
(c1-coord NOTES_FOR_TEAM 17:47Z item 2): for psi = u(r) sin(n theta) and F_n = f(r) sin(n theta),

  Rn^2 = Qn + 2 n^2 (b - p) + n^2 (a + d),   Rn = ||r (F_n + Delta psi)||_2,

with d = ||grad psi||^2, p = int F_n psi, Qn = ||r F_n||^2, A_Fn = -r f cos(n theta) e_theta/n,
Z = -u' sin(n theta) e_r - (r u'' + u') cos(n theta) e_theta/n, a = ||Z||^2, b = <A_Fn, Z>; and the hypotheses used
by its proof (integration by parts in y = log r, the gradient completion H(Delta psi) = ||grad psi||_2).
Checked (sympy, exact):
  (A) for generic n, u, f: Z = A_(Delta psi) - grad psi; div A_Fn = F_n (polar form); ||A_Fn||^2 = Qn/n^2 after the
      theta integration; r^2 Delta psi = (v'' - n^2 v) sin(n theta) with v(y) = u(e^y);
  (B) for generic n, u, f, the r-integrands after the theta integration: the cross term 2 int r^2 F_n Delta psi is
      exactly 2 n^2 (b - p), pointwise in r (no integration by parts); and the integrand of ||r Delta psi||^2 minus
      that of n^2 (a + d) is -2 pi n^2 d/dr (r u u'), so Rn^2 = Qn + 2 n^2 (b - p) + n^2 (a + d) - 2 pi n^2 [r u u']
      from 0 to infinity;
  (C) for six members of the trial family u = r^3 (1 + r^2)^(-beta) (r^2/(1 + r^2))^k (3 + 2k - n even and >= 0,
      beta > 3/2), by sympy limits: r u u' -> 0 at 0 and at infinity, and the integrands of d, a and ||r Delta psi||^2
      are bounded at 0 and O(r^(5 - 4 beta)) at infinity; at beta = 3/2 (n = 1, k = 0) r u u' still tends to 0, but
      d diverges logarithmically;
  (D) three exact examples (n = 1 with k = -1, n = 1 with k = 0, n = 3) with sources not built from the test:
      Rn^2 computed directly equals Qn + 2 n^2 (b - p) + n^2 (a + d); the integrals are exact (each term
      c r^m (1 + r^2)^-sigma by the beta function, each term required to converge on its own); one Rn^2 is also
      compared with an mpmath quadrature (FLOAT, a numerical observation);
  (E) one example with a known Riesz representative, F = -Delta(w sin theta), w = r (1 + r^2)^-2, and the mode-1
      test u = r (1 + r^2)^(-3/2) of REVIEW_T4_469 3.2: the bounds (2)
      max(0, sqrt(d) - Rn/n, |p|/sqrt(d)) <= H(F) <= sqrt(d) + Rn/n hold exactly, and H(F + Delta psi) =
      ||grad((w - u) sin theta)||_2 <= Rn/n (the single-mode Hardy bound for the residual).
Not checked: the 017 source, its projection, the saved vectors or any Arb total of c1-n4; no peer code is run.

Run from artifacts/:  python3 -B -u arith/n4_017_residual_identity.py
Takes no arguments. Output: stdout (logs/n4_017_residual_identity.log by the README command),
data/n4_017_residual_identity_results.json.
"""
import json
import sys
import time
from pathlib import Path

import sympy as sp

if len(sys.argv) != 1:
    sys.exit("usage: n4_017_residual_identity.py (no arguments)")
T0 = time.time()
HERE = Path(__file__).resolve().parents[1]
FAILS, N_ = [], [0]


def check(msg, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


r, th, y = sp.symbols("r theta y", positive=True)
n = sp.symbols("n", positive=True, integer=True)
u, f = sp.Function("u")(r), sp.Function("f")(r)
up, upp = sp.diff(u, r), sp.diff(u, r, 2)
lap = lambda g: sp.diff(g, r, 2) + sp.diff(g, r) / r + sp.diff(g, th, 2) / r ** 2       # polar Laplacian
div = lambda Ar, At: sp.diff(r * Ar, r) / r + sp.diff(At, th) / r                     # polar divergence
psi = u * sp.sin(n * th)
Fn = f * sp.sin(n * th)
A_of = lambda g: (0, -r * g * sp.cos(n * th) / n)            # A_G for G = g(r) sin(n theta): (e_r, e_theta)
lap_psi_radial = sp.simplify(lap(psi) / sp.sin(n * th))
grad_psi = (sp.diff(psi, r), sp.diff(psi, th) / r)
A_lap = A_of(lap_psi_radial)
Z = (-up * sp.sin(n * th), -(r * upp + up) * sp.cos(n * th) / n)
check("(A) Z = A_(Delta psi) - grad psi (both polar components)",
      all(sp.simplify(A_lap[i] - grad_psi[i] - Z[i]) == 0 for i in range(2)))
check("(A) div A_Fn = F_n and div Z = 0",
      sp.simplify(div(*A_of(f)) - Fn) == 0 and sp.simplify(div(*Z)) == 0)
I_th = lambda e: sp.integrate(sp.expand(e), (th, 0, 2 * sp.pi))                         # theta integral
sq = lambda V: V[0] ** 2 + V[1] ** 2
Qn_i = sp.simplify(I_th((r * Fn) ** 2) * r)                                           # r-integrands
check("(A) after the theta integration: |A_Fn|^2 integrand = Qn integrand/n^2 = pi r^3 f^2/n^2",
      sp.simplify(I_th(sq(A_of(f))) * r - Qn_i / n ** 2) == 0 and sp.simplify(Qn_i - sp.pi * r ** 3 * f ** 2) == 0)
v = sp.Function("v")
yy = sp.symbols("yy", real=True)
uy = lambda e: e.subs(r, sp.exp(yy))
lhs = sp.simplify((r ** 2 * lap_psi_radial).subs(u, v(sp.log(r))).doit())
rhs = (sp.diff(v(yy), yy, 2) - n ** 2 * v(yy)).subs(yy, sp.log(r))
check("(A) r^2 Delta psi = (v'' - n^2 v) sin(n theta), v(y) = u(e^y)", sp.simplify(lhs - rhs) == 0)
# (B) integrands in r (measure dr)
d_i = sp.simplify(I_th(sq(grad_psi)) * r)
p_i = sp.simplify(I_th(Fn * psi) * r)
a_i = sp.simplify(I_th(sq(Z)) * r)
b_i = sp.simplify(I_th(A_of(f)[1] * Z[1]) * r)
R_i = sp.simplify(I_th((r * (Fn + lap(psi))) ** 2) * r)
cross_i = sp.simplify(I_th(r ** 2 * Fn * lap(psi)) * r)
check("(B) cross term: int r^2 F_n Delta psi integrand = n^2 (b - p) integrand, pointwise",
      sp.simplify(cross_i - n ** 2 * (b_i - p_i)) == 0)
lapsq_i = sp.simplify(I_th((r * lap(psi)) ** 2) * r)
bdry = -2 * sp.pi * n ** 2 * sp.diff(r * u * up, r)
check("(B) ||r Delta psi||^2 integrand - n^2 (a + d) integrand = -2 pi n^2 d/dr (r u u')",
      sp.simplify(sp.expand(lapsq_i - n ** 2 * (a_i + d_i) - bdry)) == 0)
check("(B) so the Rn^2 integrand = Qn + 2 n^2 (b - p) + n^2 (a + d) integrands - 2 pi n^2 d/dr (r u u')",
      sp.simplify(sp.expand(R_i - (Qn_i + 2 * n ** 2 * (b_i - p_i) + n ** 2 * (a_i + d_i)) - bdry)) == 0)
check("(B) the r-integrands: d = pi (r u'^2 + n^2 u^2/r), p = pi r f u, a = pi r (u'^2 + (r u'' + u')^2/n^2), "
      "b = (pi/n^2) r^2 f (r u'' + u')",
      sp.simplify(d_i - sp.pi * (r * up ** 2 + n ** 2 * u ** 2 / r)) == 0 and sp.simplify(p_i - sp.pi * r * f * u) == 0
      and sp.simplify(a_i - sp.pi * r * (up ** 2 + (r * upp + up) ** 2 / n ** 2)) == 0
      and sp.simplify(b_i - sp.pi / n ** 2 * r ** 2 * f * (r * upp + up)) == 0)


# (C) the trial family at the origin and at infinity
C_ok, C_rows = True, []
for nn, kk, bb in ((1, -1, sp.Rational(8, 5)), (1, -1, sp.Rational(5, 2)), (1, 0, 2), (3, 0, sp.Rational(7, 4)),
                   (3, 1, sp.Rational(8, 5)), (5, 1, 3)):
    uu = r ** 3 * (1 + r ** 2) ** (-bb) * (r ** 2 / (1 + r ** 2)) ** kk
    bt = r * uu * sp.diff(uu, r)
    l0, li = sp.limit(bt, r, 0), sp.limit(bt, r, sp.oo)
    # integrands of d, a and ||r Delta psi||^2: bounded at 0, and times r^(4 beta - 5) bounded at infinity, so
    # O(r^(5 - 4 beta)), integrable at infinity since 5 - 4 beta < -1 for beta > 3/2
    dd = r * sp.diff(uu, r) ** 2 + nn ** 2 * uu ** 2 / r
    aa = r * (sp.diff(uu, r) ** 2 + (r * sp.diff(uu, r, 2) + sp.diff(uu, r)) ** 2 / nn ** 2)
    ll = r ** 3 * (sp.diff(uu, r, 2) + sp.diff(uu, r) / r - nn ** 2 * uu / r ** 2) ** 2
    fin = [sp.limit(sp.simplify(e * r ** (4 * bb - 5)), r, sp.oo) for e in (dd, aa, ll)]
    near0 = [sp.limit(e, r, 0) for e in (dd, aa, ll)]
    ok = (l0 == 0 and li == 0 and all(x.is_finite for x in fin) and all(x.is_finite for x in near0)
          and 5 - 4 * bb < -1 and (3 + 2 * kk - nn) % 2 == 0 and 3 + 2 * kk - nn >= 0)
    C_rows.append({"n": nn, "k": kk, "beta": str(bb), "bdry_0": str(l0), "bdry_inf": str(li),
                   "lead_inf": [str(x) for x in fin]})
    C_ok = C_ok and ok
check("(C) trial family, (n, k, beta) = (1,-1,8/5), (1,-1,5/2), (1,0,2), (3,0,7/4), (3,1,8/5), (5,1,3): r u u' -> 0 "
      "at 0 and infinity; the d, a and ||r Delta psi||^2 integrands are bounded at 0 and O(r^(5 - 4 beta)) at infinity "
      "with 5 - 4 beta < -1", C_ok)
uu = r ** 3 * (1 + r ** 2) ** sp.Rational(-3, 2)
dd = r * sp.diff(uu, r) ** 2 + uu ** 2 / r
check("(C) at beta = 3/2 (n = 1, k = 0): r u u' -> 0 at infinity, but r (d integrand) -> 1, so d diverges "
      "(logarithmically); beta > 3/2 is needed for d, not for the boundary term",
      sp.limit(r * uu * sp.diff(uu, r), r, sp.oo) == 0 and sp.limit(sp.simplify(r * dd), r, sp.oo) == 1)

# (D), (E): exact integrals. Functions are written in r and S = 1 + r^2 (dS/dr = 2r); every term c r^m S^-sigma is
# integrated by int_0^oo r^m S^-sigma dr = Gamma(a) Gamma(sigma - a)/(2 Gamma(sigma)), a = (m + 1)/2, and each term
# is required to converge on its own (a > 0 and sigma - a > 0), so no cancellation between divergent terms is used.
S = sp.symbols("S", positive=True)
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


check("integrator: int_0^oo r S^-2 dr = 1/2, int r^3 S^-3 dr = 1/4, int S^-1 dr = pi/2, int r^2 S^(-5/2) dr = 1/3",
      I0(r * S ** -2) == sp.Rational(1, 2) and I0(r ** 3 * S ** -3) == sp.Rational(1, 4) and I0(S ** -1) == sp.pi / 2
      and I0(r ** 2 * S ** sp.Rational(-5, 2)) == sp.Rational(1, 3))


def parts(nn, uu, ff):          # all values divided by pi
    up_, upp_ = D(uu), D(D(uu))
    return {"d": I0(r * up_ ** 2 + nn ** 2 * uu ** 2 / r), "p": I0(r * ff * uu),
            "a": I0(r * (up_ ** 2 + (r * upp_ + up_) ** 2 / nn ** 2)),
            "b": I0(r ** 2 * ff * (r * upp_ + up_)) / nn ** 2,
            "Q": I0(r ** 3 * ff ** 2), "R2": I0(r ** 3 * (ff + upp_ + up_ / r - nn ** 2 * uu / r ** 2) ** 2)}


EX = {}
for name, nn, uu, ff in (("n1_k-1", 1, r * S ** sp.Rational(-3, 2), r * S ** -3),
                         ("n1_k0", 1, r ** 3 * S ** -2, r * (1 - r ** 2) * S ** -3 / 3),
                         ("n3_k0", 3, r ** 3 * S ** -3, r ** 3 * S ** -4)):
    P = parts(nn, uu, ff)
    rhs = P["Q"] + 2 * nn ** 2 * (P["b"] - P["p"]) + nn ** 2 * (P["a"] + P["d"])
    EX[name] = {k: str(x) for k, x in P.items()}
    check("(D) %s: Rn^2/pi = %s = Qn + 2 n^2 (b - p) + n^2 (a + d) (all /pi, rational: d %s, p %s, a %s, b %s, Qn %s)"
          % (name, P["R2"], P["d"], P["p"], P["a"], P["b"], P["Q"]),
          TERMWISE[0] and all(x.is_Rational for x in P.values()) and P["R2"] == rhs)
mp_ = __import__("mpmath")
mp_.mp.dps = 30
U1 = lambda z: z * (1 + z ** 2) ** mp_.mpf(-1.5)
Rq = mp_.quad(lambda x: x ** 3 * (x * (1 + x ** 2) ** -3 + mp_.diff(U1, x, 2) + mp_.diff(U1, x) / x - U1(x) / x ** 2)
              ** 2, [0, 1, mp_.inf])
R2a = sp.Rational(EX["n1_k-1"]["R2"])
check("(D) n1_k-1 cross-check by mpmath quadrature with numerical derivatives (a numerical observation, FLOAT): "
      "Rn^2/pi about %s, relative difference below 1e-15" % mp_.nstr(Rq, 18),
      abs(Rq - mp_.mpf(R2a.p) / R2a.q) < mp_.mpf(10) ** -15 * abs(Rq))
# (E) known Riesz representative: F = -Delta(w sin theta)
w = r * S ** -2
ff = sp.expand(-(D(D(w)) + D(w) / r - w / r ** 2))
uu = r * S ** sp.Rational(-3, 2)
P = parts(1, uu, ff)
H2 = I0(r * D(w) ** 2 + w ** 2 / r)
g = w - uu
res2 = I0(r * D(g) ** 2 + g ** 2 / r)
R2, d_, p_ = P["R2"], P["d"], P["p"]
ok_rat = TERMWISE[0] and all(x.is_Rational for x in (H2, res2, R2, d_, p_))
# exact comparisons of square roots of nonnegative rationals: sqrt(X) <= sqrt(Y) + sqrt(Z) iff X <= Y + Z or
# (X - Y - Z)^2 <= 4 Y Z; and |p|/sqrt(d) <= sqrt(H2) iff p^2 <= d H2
le_sum = lambda X, Y, Z: X <= Y + Z or (X - Y - Z) ** 2 <= 4 * Y * Z
check("(E) F = -Delta(w sin theta), w = r S^-2, psi = r S^(-3/2) sin theta (all /pi): H(F)^2 = %s, d = %s, p = %s, "
      "Rn^2 = %s; sqrt(d) - Rn <= H <= sqrt(d) + Rn and |p|/sqrt(d) <= H, exactly" % (H2, d_, p_, R2),
      ok_rat and le_sum(H2, d_, R2) and le_sum(d_, H2, R2) and p_ ** 2 <= d_ * H2)
check("(E) H(F + Delta psi)^2 = ||grad((w - u) sin theta)||^2 = %s <= Rn^2 = %s (n = 1)" % (res2, R2),
      ok_rat and res2 <= R2)
check("(E) Rn^2 = Qn + 2 (b - p) + (a + d) also here; H(F)^2 = 4/15, p = 32/105, H(g)^2 = 9/280 and Rn^2 = 1959/20020 "
      "(= ||A_g||^2 for n = 1) as in REVIEW_T4_469 3.2",
      R2 == P["Q"] + 2 * (P["b"] - P["p"]) + P["a"] + P["d"] and H2 == sp.Rational(4, 15)
      and p_ == sp.Rational(32, 105) and res2 == sp.Rational(9, 280) and R2 == sp.Rational(1959, 20020))
el = time.time() - T0
print("%d checks, %d FAIL, %.2f s" % (N_[0], len(FAILS), el))
OUT = {"trial_family_orders": C_rows, "examples": EX,
       "riesz_example": {"H2_over_pi": str(H2), "residual_H2_over_pi": str(res2), **{k: str(x) for k, x in P.items()}},
       "checks": N_[0], "fails": FAILS, "elapsed_s": round(el, 2)}
(HERE / "data/n4_017_residual_identity_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
sys.exit(1 if FAILS else 0)
