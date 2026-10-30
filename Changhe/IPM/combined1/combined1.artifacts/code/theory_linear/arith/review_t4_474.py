"""Independent check of c1-t4 T4-474 (research/partial_mode_hardy_certificate/PROOF.md, TEAM_NOTE_v253): a complete
angular Hardy upper bound from a prefix of odd sine modes,
  H(F)^2 <= M2 <= B_N = S/N^2 + sum_(n odd < N) (1/n^2 - 1/N^2) S_n,  S = ||rF||_2^2,  S_n = pi int r^3 f_n^2 dr.

No c1-t4 code is executed; code/check.py is not imported. Read only (sha256 asserted): PROOF.md, code/check.py,
data/parameters.json, data/manifest.json, data/initial_sources.json, verification/result.json, and the files that
data/manifest.json binds (T4-467 and T4-472 results, T4-469 PROOF.md, ERRATA_v01.md and result.json, T4 mode_hardy_mellin
PROOF.md); for part G, T4-476 PROOF.md, verification/result.json and data/parameters.json.

Parts.
  A  input hashes, the manifest bindings, and the two candidate016 rationals against the T4-467 and T4-472 results.
  B  symbolic steps (sympy): only odd sine modes under the symmetry (even in x, odd in y); the polar energies S_n and
     ||A_F mode n||^2 = S_n/n^2; the coefficientwise form B_N = sum_n max(n^-2, N^-2) S_n, from which (2), (3),
     B_(N+2) <= B_N and (4) follow.
  C  the finite lists of data/parameters.json against verification/result.json (exact Fractions) and the omission
     counterexample.
  D  an infinite-mode source F = h(r) sgn(y), h = (1+r^2)^-3, with f_n = 4h/(pi n) for every odd n and the closed form
     A_F = -e_theta r h (pi - 2|theta|)/2: Fourier coefficients (sympy), the identity int A_F . grad phi = -int F phi
     on the whole plane for test functions of every symmetry class (exact), S, M2 and B_N (exact in pi; signs by mpmath
     interval arithmetic), and (5) with one mode-1 test (b exact; H_1^2 by quadrature, a numerical observation).
  E  the known-solution fixture F = -Delta(psi_1 + psi_3): S_n, d_n, a_n, b_n from the profiles (sympy), B_N for the odd
     cuts, and (5) reproducing the exact H(F)^2.
  F  the candidate016 arithmetic: the loss bounds U^2/N^2 of result.json, their strict displays, 47/1000 at N = 33.
  G  T4-476 (research/candidate016_prefix_hardy_audit, TEAM_NOTE_v255), the N = 9 specialization for candidate016:
     the composition of its saved exact mode endpoints q_n in [L_n, U_n] (n = 1, 3, 5, 7) with U, the T4-472 floor and
     the T4-467 component endpoints, recomputed in exact Fractions. Arithmetic only: the q_n endpoints, the field
     binding and the mode support are T4-476's premises and are not rechecked.

Run from artifacts/:  python3 -B -u arith/review_t4_474.py
Takes no arguments. Needs sympy and mpmath. Output: stdout (logs/review_t4_474.log by the README command),
data/review_t4_474_results.json.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import sympy as sp
from mpmath import iv

sys.set_int_max_str_digits(0)                     # T4-476 endpoints have about 4900-digit numerators
if len(sys.argv) != 1:
    sys.exit("usage: review_t4_474.py (no arguments)")
T0 = time.time()
HERE_ = Path(__file__).resolve().parents[1]
RES_DIR = HERE_.parent.parent / "c1-t4/research"
SRC = RES_DIR / "partial_mode_hardy_certificate"
SH = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
FAILS, N_ = [], [0]
OUT = {}


def check(msg, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


def zero(e):
    return sp.simplify(e) == 0


# ---------------------------------------------------------------- A: inputs
PIN = {"PROOF.md": "afd349a713799271446eb9f3ae4676af93227eebc18bc2fef2af9fc189aa9414",
       "code/check.py": "b88d0b552771947ecbbf14cb66b232741f1805a7b1c5d769911b9622e884d5b1",
       "data/parameters.json": "659210cd3824e5367dd5eea0d8b8a649c8242a78cebc415f6d8301dc8040ed05",
       "data/manifest.json": "28548e066aaa7e135aaf1bfd4dbd4e590415aafd1ee728c0f6da985e98409bdb",
       "data/initial_sources.json": "03189cd517df8c6ff2214552fa26dfde63df83bdb92298fedbc5ac9c7f59996f",
       "verification/result.json": "5eef39af9c96f1d14dc39b95c8e5eca9ff394af701ee7c46f87ca07224cb3524"}
print("A. inputs")
for k, h in PIN.items():
    check("sha256 of %s is %s...%s" % (k, h[:8], h[-8:]), SH(SRC / k) == h)
PAR = json.loads((SRC / "data/parameters.json").read_text())
RES = json.loads((SRC / "verification/result.json").read_text())
MAN = json.loads((SRC / "data/manifest.json").read_text())
check("result.json cites PROOF.md, code/check.py and data/manifest.json by their current sha256; %d checks; no candidate"
      " integral evaluated and no candidate H upper asserted" % RES["check_count"],
      RES["proof_sha256"] == PIN["PROOF.md"] and RES["checker_sha256"] == PIN["code/check.py"]
      and RES["manifest_sha256"] == PIN["data/manifest.json"] and RES["check_count"] == len(RES["checks"]) == 720
      and RES["candidate_integrals_evaluated"] is False and RES["candidate_H_upper_asserted"] is False)
bind_ok = all(SH(SRC / m["local"]) == m["sha256"] for m in MAN)
check("all %d manifest rows (T4-467 and T4-472 results, T4-469 PROOF/ERRATA/result, mode_hardy_mellin PROOF, own files)"
      " carry the current sha256 of the bound file" % len(MAN), bind_ok and len(MAN) == 10)
R467 = json.loads((RES_DIR / "candidate016_complete_forcing_audit/verification/result.json").read_text())
R472 = json.loads((RES_DIR / "candidate016_cross_archive_audit/verification/result.json").read_text())
U = Fr(PAR["rF_upper"])
check("rF upper U = %s equals T4-467 components/rF/strict_upper_exact and result.json" % PAR["rF_upper"],
      PAR["rF_upper"] == R467["components"]["rF"]["strict_upper_exact"] == RES["candidate016_rF_upper_exact"])
fl1, fl3 = Fr(R472["rows"][1]["strict_floor"]), Fr(R472["rows"][3]["strict_floor"])
I_low = Fr(PAR["cross_improvement_lower"])
check("cross improvement lower %s = T4-472 improvement_sum_strict_lower_exact = sum of its strict floors for b_1^2/a_1 and "
      "b_3^2/a_3 (cross rows n = %s and %s); decimal 0.238659156452557158875212 exactly"
      % (PAR["cross_improvement_lower"], R472["rows"][1]["n"], R472["rows"][3]["n"]),
      I_low == Fr(R472["improvement_sum_strict_lower_exact"]) == fl1 + fl3
      == Fr(RES["candidate016_cross_improvement_strict_lower_exact"])
      and [(str(R472["rows"][i]["n"]), R472["rows"][i]["kind"]) for i in (1, 3)] == [("1", "cross"), ("3", "cross")]
      and I_low == Fr("0.238659156452557158875212"))
OUT["A"] = {"inputs": {"c1-t4/research/partial_mode_hardy_certificate/" + k: h for k, h in PIN.items()},
            "manifest_rows": len(MAN)}

# ---------------------------------------------------------------- B: symbolic steps
print("B. symmetry, energies, coefficientwise form")
r, th = sp.symbols("r theta", positive=True)
n, m = sp.symbols("n m", positive=True, integer=True)
a_, b_ = sp.symbols("a b")
sub_d = lambda e: sp.expand(sp.expand_trig(e)).subs({a_: n * sp.pi, b_: n * th})
# x -> -x is theta -> pi - theta; y -> -y is theta -> -theta
ok = (zero(sub_d(sp.sin(a_ - b_)) - (-1) ** (n + 1) * sp.sin(n * th))
      and zero(sub_d(sp.cos(a_ - b_)) - (-1) ** n * sp.cos(n * th))
      and zero(sp.cos(-n * th) - sp.cos(n * th)) and zero(sp.sin(-n * th) + sp.sin(n * th)))
check("sin(n(pi - theta)) = (-1)^(n+1) sin(n theta), cos(n(pi - theta)) = (-1)^n cos(n theta), cos even, sin odd "
      "(integer n): oddness in y removes the constant and all cosine modes, evenness in x all even sine modes", ok)
ok = zero(sp.integrate(sp.sin(n * th) ** 2, (th, 0, 2 * sp.pi)) - sp.pi) and zero(
    sp.integrate(sp.cos(n * th) ** 2, (th, 0, 2 * sp.pi)) - sp.pi)
ok = ok and all(sp.integrate(sp.sin(i * th) * sp.sin(j * th), (th, 0, 2 * sp.pi)) == 0
                and sp.integrate(sp.cos(i * th) * sp.cos(j * th), (th, 0, 2 * sp.pi)) == 0
                for i in range(1, 12, 2) for j in range(1, 12, 2) if i != j)
check("int_0^(2 pi) sin^2(n theta) = int cos^2(n theta) = pi (generic n >= 1), and distinct odd frequencies 1..11 are "
      "orthogonal: ||r f_n sin(n theta)||^2 = pi int r^3 f_n^2 dr = S_n and ||r f_n cos(n theta)/n||^2 = S_n/n^2", ok)
Nn = sp.symbols("N", positive=True)
check("coefficient of S_n in B_N: 1/N^2 + (1/n^2 - 1/N^2) = 1/n^2 for n < N, 1/N^2 for n >= N; so B_N = sum_n "
      "max(n^-2, N^-2) S_n (odd n), M2 = sum_n n^-2 S_n", zero(1 / Nn ** 2 + (1 / n ** 2 - 1 / Nn ** 2) - 1 / n ** 2))
cuts = PAR["odd_cuts"]
coef = lambda N, k: Fr(1, k * k) if k < N else Fr(1, N * N)
ok = True
for N in cuts:
    for k in range(1, 4 * N + 8, 2):
        c = coef(N, k)
        ok = ok and c == max(Fr(1, k * k), Fr(1, N * N)) and Fr(0) <= c - Fr(1, k * k) <= Fr(1, N * N)
        ok = ok and coef(N + 2, k) - c == (0 if k <= N else Fr(1, (N + 2) ** 2) - Fr(1, N * N))
        ok = ok and (k >= N or Fr(1, k * k) - Fr(1, N * N) > 0) and (k > N or c == Fr(1, k * k))
check("for N in %s and odd n up to 4N + 7: B_N - M2 has coefficient max(n^-2, N^-2) - n^-2 in [0, N^-2] (zero for n <= N),"
      " so 0 <= B_N - M2 <= N^-2 sum_(n >= N + 2) S_n <= S/N^2, (2) and (3); B_(N+2) - B_N has coefficient 0 for n <= N and "
      "(N+2)^-2 - N^-2 < 0 for n >= N + 2, which is PROOF.md's (1/(N+2)^2 - 1/N^2)(S - sum_(n<=N) S_n); every "
      "coefficient of (4) is positive" % cuts, ok)

rr = sp.symbols("rho", positive=True)
I_rF = sp.integrate(1 / (rr * sp.log(rr) ** 2), (rr, 0, sp.Rational(1, 2)))
I_F = sp.integrate(1 / (rr * (-sp.log(rr))), (rr, sp.Rational(1, 100), sp.Rational(1, 2)))
I_F_lim = sp.limit(sp.integrate(1 / (rr * (-sp.log(rr))), (rr, sp.Symbol("e", positive=True), sp.Rational(1, 2))),
                   sp.Symbol("e", positive=True), 0, "+")
check("F in L^1_loc is a separate hypothesis: F = sgn(y) r^-2 |log r|^-1 on r < 1/2 (zero outside) has ||rF||^2 = "
      "2 pi int_0^(1/2) dr/(r log^2 r) = 2 pi (%s) finite, but int |F| dx = 2 pi int dr/(r |log r|) = %s; so F in L^1_loc "
      "is not implied by rF in L^2" % (sp.simplify(I_rF), I_F_lim),
      sp.simplify(I_rF - 1 / sp.log(2)) == 0 and I_F_lim == sp.oo and I_F.is_positive)

# ---------------------------------------------------------------- C: finite lists
print("C. finite energy lists")
B_of = lambda E, N: sum(coef(N, k) * v for k, v in E.items())
fix_res = {f["name"]: f for f in RES["fixtures"]}
ok, rows_c = True, {}
for fx in PAR["fixtures"]:
    E = {int(k): Fr(v) for k, v in fx["energies"].items()}
    S, M2 = sum(E.values()), sum(v / (k * k) for k, v in E.items())
    rf = fix_res[fx["name"]]
    ok = ok and Fr(rf["S"]) == S and Fr(rf["M2"]) == M2
    prev = None
    for pr in rf["prefixes"]:
        N = pr["N"]
        BN = S / (N * N) + sum((Fr(1, k * k) - Fr(1, N * N)) * v for k, v in E.items() if k < N)
        ok = ok and BN == B_of(E, N) == Fr(pr["B_N"]) and BN - M2 == Fr(pr["loss"]) and 0 <= BN - M2 <= S / (N * N)
        ok = ok and Fr(pr["directed_upper_fixture"]) >= BN and (prev is None or BN <= prev)
        prev = BN
    rows_c[fx["name"]] = {"S": str(S), "M2": str(M2)}
check("fixtures %s: S, M2, B_N and B_N - M2 for N in %s equal result.json exactly; (2), (3), monotonicity; each "
      "directed_upper_fixture >= B_N" % (", ".join(rows_c), [p["N"] for p in RES["fixtures"][0]["prefixes"]]), ok)
E = {int(k): Fr(v) for k, v in PAR["fixtures"][2]["energies"].items()}       # mixed 1, 3, 5, 7
S, M2 = sum(E.values()), sum(v / (k * k) for k, v in E.items())
Bom = S / 25 + sum((Fr(1, k * k) - Fr(1, 25)) * v for k, v in E.items() if k < 5 and k != 3)
Eh = {int(k): Fr(v) for k, v in PAR["fixtures"][1]["energies"].items()}      # high only
trunc = sum(v / (k * k) for k, v in Eh.items() if k < 5)
check("omission counterexample: mixed list, N = 5 with mode 3 left out of the prefix gives %s < M2 = %s; high-only list: "
      "the truncated sum %s < M2 = %s = B_5" % (Bom, M2, trunc, sum(v / (k * k) for k, v in Eh.items())),
      Bom < M2 and trunc < sum(v / (k * k) for k, v in Eh.items()) == B_of(Eh, 5))
OUT["C"] = {"fixtures": rows_c, "omission_mixed_N5": str(Bom), "mixed_M2": str(M2)}

# ---------------------------------------------------------------- D: an infinite-mode source
print("D. infinite-mode source F = h(r) sgn(y), h = (1 + r^2)^-3")
t = sp.symbols("t", real=True)
k_ = sp.symbols("k", nonnegative=True, integer=True)
beta = sp.simplify(2 / sp.pi * sp.integrate(sp.sin(n * t), (t, 0, sp.pi)))     # (1/pi) int sgn(t) sin(nt) over (-pi, pi)
alph = sp.simplify(sp.integrate(-sp.cos(n * t), (t, -sp.pi, 0)) + sp.integrate(sp.cos(n * t), (t, 0, sp.pi)))
gfun = (sp.pi - 2 * t) / 2                                                       # g(t) = (pi - 2|t|)/2 on t >= 0, even
gcos = sp.simplify(2 / sp.pi * sp.integrate(gfun * sp.cos(n * t), (t, 0, sp.pi)))
gmean = sp.integrate(gfun, (t, 0, sp.pi))
ok = (zero(beta.subs(n, 2 * k_ + 1) - 4 / (sp.pi * (2 * k_ + 1))) and zero(beta.subs(n, 2 * k_ + 2))
      and zero(alph) and zero(gcos.subs(n, 2 * k_ + 1) - 4 / (sp.pi * (2 * k_ + 1) ** 2))
      and zero(gcos.subs(n, 2 * k_ + 2)) and gmean == 0)
check("sgn(y) = sum_(n odd) 4 sin(n theta)/(pi n) (no cosine, no even modes), so f_n = 4h/(pi n) for every odd n; "
      "g(theta) = (pi - 2|theta|)/2 = sum_(n odd) 4 cos(n theta)/(pi n^2) (mean 0, no even modes); hence "
      "A_F = -e_theta r sum f_n cos(n theta)/n = -e_theta r h g(theta), the series converging uniformly", ok)
gpl = (sp.pi - 2 * t) / 2
gmi = (sp.pi + 2 * t) / 2
ok = (gpl.subs(t, sp.pi) == gmi.subs(t, -sp.pi) and gpl.subs(t, 0) == gmi.subs(t, 0)
      and sp.diff(gpl, t) == -1 and sp.diff(gmi, t) == 1)
check("g is continuous on the circle (g(pi) = g(-pi) = -pi/2, continuous at 0) with g' = -sgn(theta): the "
      "distributional theta-derivative has no point mass and (1/r) d_theta(-r h g) = h sgn(theta) = F", ok)
X, Yv = sp.symbols("x y", real=True)
h = (1 + r ** 2) ** -3
w4 = (1 + r ** 2) ** -4
polys = [sp.Integer(1), X, Yv, X * Yv, X ** 2 * Yv, Yv ** 3, X * Yv ** 2 + 2 * Yv,
         1 + X + 2 * Yv + 3 * X * Yv + X ** 2 * Yv - Yv ** 3 + X ** 3]
pol = lambda P: sp.expand(P.subs({X: r * sp.cos(t), Yv: r * sp.sin(t)}))


def th_int(e, g_on):
    """int over (-pi, pi) of e(t) times g(t) (g_on True) or sgn(t) (g_on False)"""
    if g_on:
        return sp.integrate(e * gmi, (t, -sp.pi, 0)) + sp.integrate(e * gpl, (t, 0, sp.pi))
    return -sp.integrate(e, (t, -sp.pi, 0)) + sp.integrate(e, (t, 0, sp.pi))


ok, vals = True, []
for P in polys:
    Pp = pol(P)
    dP = sp.expand(sp.diff(Pp, t))                                     # d_theta phi = (d_theta P) (1+r^2)^-4
    lhs = sp.integrate(sp.expand(-r * h * w4 * th_int(dP, True)), (r, 0, sp.oo))        # int A_theta d_theta phi dtheta dr
    rhs = -sp.integrate(sp.expand(r * h * w4 * th_int(Pp, False)), (r, 0, sp.oo))      # -int F phi r dtheta dr
    ok = ok and zero(lhs - rhs)
    vals.append(str(sp.nsimplify(sp.simplify(lhs))))
check("int A_F . grad phi dx = -int F phi dx exactly for phi = P(x, y) (1+r^2)^-4, P in {1, x, y, xy, x^2 y, y^3, "
      "xy^2 + 2y, 1 + x + 2y + 3xy + x^2 y - y^3 + x^3} (values %s): the identity holds on the whole plane, origin "
      "included, for an F with infinitely many modes (phi decays, grad phi in L^2 and F phi in L^1, so it extends from "
      "C_c^oo)" % ", ".join(vals), ok)
Ir = sp.integrate(r ** 3 * h ** 2, (r, 0, sp.oo))
S_ex = 2 * sp.pi * Ir
M2_ex = Ir * (sp.integrate(gmi ** 2, (t, -sp.pi, 0)) + sp.integrate(gpl ** 2, (t, 0, sp.pi)))
Sn = 16 * Ir / (sp.pi * n ** 2)                                         # S_n = pi int r^3 (4h/(pi n))^2 dr
s2 = sp.summation(1 / (2 * k_ + 1) ** 2, (k_, 0, sp.oo))
s4 = sp.summation(1 / (2 * k_ + 1) ** 4, (k_, 0, sp.oo))
ok = (Ir == sp.Rational(1, 40) and zero(S_ex - sp.pi / 20) and zero(M2_ex - sp.pi ** 3 / 240)
      and zero(16 * Ir / sp.pi * s2 - S_ex) and zero(16 * Ir / sp.pi * s4 - M2_ex))
check("int r^3 h^2 dr = 1/40; S = ||rF||^2 = pi/20 = sum_(n odd) S_n (angular Parseval, sum 1/n^2 = pi^2/8); M2 = "
      "||A_F||^2 = pi^3/240 = sum S_n/n^2 (sum 1/n^4 = pi^4/96)", ok)
iv.dps = 60
ipi = iv.pi
iS, iM2 = ipi / 20, ipi ** 3 / 240
Bvals, ok, prevB = {}, True, None
for N in cuts:
    P2 = sum(Fr(1, j * j) for j in range(1, N, 2))
    P4 = sum(Fr(1, j ** 4) for j in range(1, N, 2))
    # exact: B_N = S/N^2 + (2/(5 pi)) (P2 - P4 N^2)/N^2 ... written as S/N^2 + (2/(5 pi)) sum_(n<N) (1/n^2 - 1/N^2)/n^2
    BN_sym = sp.pi / 20 / N ** 2 + 2 / (5 * sp.pi) * (sp.Rational(P4.numerator, P4.denominator)
                                                       - sp.Rational(P2.numerator, P2.denominator) / N ** 2)
    tail = 2 / (5 * sp.pi) * ((sp.pi ** 2 / 8 - sp.Rational(P2.numerator, P2.denominator)) / N ** 2
                              - (sp.pi ** 4 / 96 - sp.Rational(P4.numerator, P4.denominator)))
    ok = ok and zero(BN_sym - sp.pi ** 3 / 240 - tail)
    iB = iS / N ** 2 + 2 / (5 * ipi) * (iv.mpf(P4.numerator) / P4.denominator
                                        - iv.mpf(P2.numerator) / P2.denominator / N ** 2)
    loss = iB - iM2
    ok = ok and loss.a > 0 and (iS / N ** 2 - loss).a > 0 and (prevB is None or (prevB - iB).a > 0)
    prevB = iB
    Bvals[N] = {"B_N": mp.nstr(mp.mpf(iB.mid), 15), "loss_over_S_N2": mp.nstr(mp.mpf((loss * N ** 2 / iS).mid), 6)}
check("B_N for N in %s: exact form in pi equals M2 + sum_(n >= N) (N^-2 - n^-2) S_n (sympy); interval arithmetic gives "
      "0 < B_N - M2 < S/N^2 and B decreasing; (B_N - M2)/(S/N^2) = %s (FLOAT)"
      % (cuts, ", ".join(Bvals[N]["loss_over_S_N2"] for N in cuts)), ok)
# (5) with the mode-1 fixture test psi = u sin(theta), u = r (1+r^2)^(-3/2)
u1 = r * (1 + r ** 2) ** sp.Rational(-3, 2)
f1 = 4 * h / sp.pi
b1 = sp.simplify(sp.pi * sp.integrate(sp.simplify(r * f1 * (r ** 2 * sp.diff(u1, r, 2) + r * sp.diff(u1, r))),
                                      (r, 0, sp.oo)))
vp = r * sp.diff(u1, r)
vpp = r * sp.diff(vp, r)
a1 = sp.simplify(sp.pi * sp.integrate(sp.simplify((vp ** 2 + vpp ** 2) / r), (r, 0, sp.oo)))
M21 = sp.pi * sp.integrate(r ** 3 * f1 ** 2, (r, 0, sp.oo))           # mode-1 part of M2
# H_1^2 = int F_1 Phi_1 with -Delta Phi_1 = f1 sin(theta): Phi_1 = (1/2)[r^-1 int_0^r s^2 f1 ds + r int_r^oo f1 ds]
s_ = sp.symbols("s", positive=True)
inner0 = sp.integrate((s_ ** 2 * f1.subs(r, s_)), (s_, 0, r))
inner1 = sp.integrate(f1.subs(r, s_), (s_, r, sp.oo))
Phi = (inner0 / r + r * inner1) / 2
mp.mp.dps = 40
Phi_f = sp.lambdify(r, Phi, "mpmath")
f1_f = sp.lambdify(r, f1, "mpmath")
H1sq = mp.pi * mp.quad(lambda x: f1_f(x) * Phi_f(x) * x, [0, 1, 10, mp.inf])
corr = M21 - b1 ** 2 / a1
check("(5) for this infinite-mode source with the mode-1 fixture test: a = %s, b = %s (exact); mode-1 part of M2 = %s; "
      "M2 - b^2/a = pi^3/240 - %s (FLOAT %s); quadrature H_1^2 = %s < M2_1 - b^2/a = %s (numerical observation; the "
      "modes n >= 3 enter H^2 and the bound with H_n^2 <= S_n/n^2)"
      % (a1, b1, M21, sp.simplify(b1 ** 2 / a1), mp.nstr(mp.mpf(sp.N(sp.pi ** 3 / 240 - b1 ** 2 / a1, 30)), 12),
         mp.nstr(H1sq, 12), mp.nstr(mp.mpf(sp.N(corr, 30)), 12)),
      zero(a1 - 3 * sp.pi / 8) and H1sq < mp.mpf(sp.N(corr, 40)) < mp.mpf(sp.N(M21, 40)))
OUT["D"] = {"source": "F = (1+r^2)^-3 sgn(y)", "S": "pi/20", "M2": "pi^3/240", "B_N": Bvals,
            "phi_pairings": vals, "mode1_test": {"a": str(a1), "b": str(b1), "M2_mode1": str(M21),
                                                 "H1sq_quadrature": mp.nstr(H1sq, 20)}}

# ---------------------------------------------------------------- E: known-solution fixture
print("E. known-solution fixture F = -Delta(psi_1 + psi_3)")
prof = {1: r * (1 + r ** 2) ** sp.Rational(-3, 2), 3: r ** 3 * (1 + r ** 2) ** -3}
vals_e = {}
for nn, u in prof.items():
    f = sp.simplify(-(sp.diff(u, r, 2) + sp.diff(u, r) / r - nn ** 2 * u / r ** 2))
    vp = r * sp.diff(u, r)
    vpp = r * sp.diff(vp, r)
    q = lambda e: sp.nsimplify(sp.integrate(sp.simplify(e), (r, 0, sp.oo)))
    vals_e[nn] = {"S": q(r ** 3 * f ** 2), "d": q((sp.diff(u, r) ** 2 + nn ** 2 * u ** 2 / r ** 2) * r),
                  "a": q((vp ** 2 + vpp ** 2 / nn ** 2) / r), "b": q(r * f * vpp) / nn ** 2}
v1, v3 = vals_e[1], vals_e[3]
M2e = v1["S"] + v3["S"] / 9
He = v1["d"] + v3["d"]
check("from the profiles (all values / pi): S_1 = %s, S_3 = %s, M2 = %s, d_1 + d_3 = H(F)^2 = %s, a_1 = %s, a_3 = %s, "
      "b_n = -a_n" % (v1["S"], v3["S"], M2e, He, v1["a"], v3["a"]),
      v1["S"] == sp.Rational(3, 4) and v3["S"] == sp.Rational(64, 35) and M2e == sp.Rational(1201, 1260)
      and He == sp.Rational(153, 280) and v1["a"] == sp.Rational(3, 8) and v3["a"] == sp.Rational(2, 63)
      and v1["b"] == -v1["a"] and v3["b"] == -v3["a"])
Ek = {1: Fr(3, 4), 3: Fr(64, 35)}
kfix = fix_res["known_solution_without_pi"]
ok = all(Fr(p["B_N"]) == B_of(Ek, p["N"]) for p in kfix["prefixes"]) and B_of(Ek, 1) == Fr(361, 140) and all(
    B_of(Ek, N) == Fr(1201, 1260) for N in cuts if N >= 3)
check("B_1 = S = 361/140, B_N = M2 = 1201/1260 for N >= 3 (equal to result.json); B_3 - a_1 - a_3 = %s = H(F)^2: (5) is "
      "an equality here" % (Fr(1201, 1260) - Fr(3, 8) - Fr(2, 63)),
      ok and Fr(1201, 1260) - Fr(3, 8) - Fr(2, 63) == Fr(153, 280))
OUT["E"] = {str(k): {kk: str(vv) for kk, vv in v.items()} for k, v in vals_e.items()}

# ---------------------------------------------------------------- F: candidate016 arithmetic
print("F. candidate016 arithmetic")
ok, rows_f = True, {}
for row in RES["candidate016_tail_loss_bounds"]:
    N = row["N"]
    L = U * U / (N * N)
    disp = Fr(row["display_strict_upper_exact"])
    ok = ok and Fr(row["loss_strict_upper_exact"]) == L and disp >= L and disp - L < Fr(1, 10 ** 11)
    rows_f[N] = str(disp)
d33 = Fr([x for x in RES["candidate016_tail_loss_bounds"] if x["N"] == 33][0]["display_strict_upper_exact"])
check("U^2/N^2 equals result.json's loss bound for N in %s; each display is above it by less than 1e-11; at N = 33 the "
      "display %s = 0.046888012202 < 47/1000 (S < U^2 since ||rF|| < U strictly)"
      % ([x["N"] for x in RES["candidate016_tail_loss_bounds"]], d33),
      ok and [x["N"] for x in RES["candidate016_tail_loss_bounds"]] == cuts and d33 == Fr("0.046888012202")
      and d33 < Fr(47, 1000) and Fr(PAR["tail_loss_upper_N33"]) == Fr(47, 1000))
check("arithmetic only: B_33 - (cross lower) <= M2 + U^2/1089 - %s < M2 - 0.19, so with sixteen accepted prefix "
      "certificates at N = 33 the T4-472 improvement outweighs the prefix loss" % float(I_low),
      U * U / 1089 - I_low < Fr(-19, 100))
OUT["F"] = {"loss_displays": rows_f, "U": PAR["rF_upper"], "cross_lower": PAR["cross_improvement_lower"]}

# ---------------------------------------------------------------- G: the T4-476 specialization (arithmetic only)
print("G. T4-476 (candidate016_prefix_hardy_audit): composition of its saved endpoints, arithmetic only")
SRC6 = RES_DIR / "candidate016_prefix_hardy_audit"
PIN6 = {"PROOF.md": "5c1350cf713e5ef5367b54e4a2fa528a2799ef514bd74536c4f66fe78c4e1635",
        "verification/result.json": "1c91f2e3507891bf04ec694147022c0c837fee06b0ab489f4dffab7833b08a37",
        "data/parameters.json": "fc101e9a5915224bfdd1b203313e847a6d8877188106fac13fdd37e2d470b4db"}
for k, h in PIN6.items():
    check("sha256 of T4-476 %s is %s...%s" % (k, h[:8], h[-8:]), SH(SRC6 / k) == h)
R6_ = json.loads((SRC6 / "verification/result.json").read_text())
P6 = json.loads((SRC6 / "data/parameters.json").read_text())
L6 = {int(m["n"]): Fr(m["q_lower_exact"]) for m in R6_["modes"]}
U6 = {int(m["n"]): Fr(m["q_upper_exact"]) for m in R6_["modes"]}
U2 = U * U
check("T4-476 prefix: modes %s = every odd n < 9 (N = 9), of %d positive odd frequencies (its premise; not rechecked "
      "here); 0 < L_n <= U_n; the omitted-energy upper U^2 - sum L_n is positive and equals tail_rF_square_upper_exact"
      % (sorted(L6), R6_["complete_mode_count"]),
      sorted(L6) == [1, 3, 5, 7] and R6_["prefix"] == 7 and all(0 < L6[k] <= U6[k] for k in L6)
      and U2 - sum(L6.values()) == Fr(R6_["tail_rF_square_upper_exact"]) > 0)
UM4 = U2 / 81 + sum((Fr(1, k * k) - Fr(1, 81)) * U6[k] for k in U6)        # PROOF.md (4) of T4-474
UMs = sum(U6[k] / (k * k) for k in U6) + (U2 - sum(L6.values())) / 81     # T4-476's split form
M2u = Fr(R6_["M2_upper_exact"])
fl = lambda x: mp.mpf(x.numerator) / x.denominator
check("M2_upper_exact of T4-476 equals T4-474 (4), U^2/81 + sum (1/n^2 - 1/81) U_n, exactly (= %s, FLOAT); "
      "T4-476's split form sum U_n/n^2 + (U^2 - sum L_n)/81 lies above it by sum (U_n - L_n)/81 = %s (FLOAT), as "
      "T4-476 states; both are >= B_9 >= M2 when L_n <= q_n <= U_n and S < U^2" % (mp.nstr(fl(M2u), 12),
                                                                              mp.nstr(fl(UMs - UM4), 4)),
      M2u == UM4 and UMs - UM4 == sum(U6[k] - L6[k] for k in U6) / 81 and UMs > UM4)
Hsq_up = Fr(R6_["improved_H_square_upper_exact"])
check("H^2 < M2_upper - (T4-472 cross floor) = improved_H_square_upper_exact; plain sqrt(M2_upper) < %s and improved "
      "sqrt < %s (squares compared exactly); M2_upper = %s, improved = %s (FLOAT)"
      % (P6["plain_H_upper"], P6["improved_H_upper"], mp.nstr(mp.mpf(float(M2u)), 10), mp.nstr(mp.mpf(float(Hsq_up)), 10)),
      Hsq_up == M2u - I_low and Fr(P6["improvement"]) == I_low and M2u < Fr(P6["plain_H_upper"]) ** 2
      and Hsq_up < Fr(P6["improved_H_upper"]) ** 2 and P6["plain_H_upper"] == "1.063013"
      and P6["improved_H_upper"] == "0.944107")
Slo = Fr(R467["components"]["rF"]["strict_lower_exact"]) ** 2
fr_lo, fr_up = sum(L6.values()) / U2, sum(U6.values()) / Slo
tail9 = (U2 - sum(L6.values())) / 81
check("energy split (rigorous under T4-476's premises): modes 1, 3, 5, 7 carry a fraction of S = ||rF||^2 in "
      "[%s, %s] (FLOAT), below 1/20; so the upper is dominated by its omitted-mode part "
      "(U^2 - sum L_n)/81 = %s of M2_upper = %s (FLOAT); a longer prefix lowers it (B_(N+2) <= B_N)"
      % (mp.nstr(fl(fr_lo), 6), mp.nstr(fl(fr_up), 6), mp.nstr(fl(tail9), 6), mp.nstr(fl(M2u), 6)),
      0 < fr_lo <= fr_up < Fr(1, 20) and Slo < U2)
OUT["G_energy_fraction_modes_1_to_7"] = [mp.nstr(fl(fr_lo), 10), mp.nstr(fl(fr_up), 10)]
C467 = R467["components"]
lo = {k: Fr(C467[k]["strict_lower_exact"]) for k in ("P2", "G1", "G0")}
up = {k: Fr(C467[k]["strict_upper_exact"]) for k in ("P2", "G1", "G0")}
Hlo = Fr(P6["H_lower"])
E2sq = lambda c, Hsq: c["P2"] ** 2 + 2 ** 14 * c["G1"] ** 2 + 2 ** 18 * c["G0"] ** 2 + Fr(20, 21) * 2 ** 18 * Hsq
check("E2^2 = P2^2 + 2^14 G1^2 + 2^18 G0^2 + (20/21) 2^18 H^2 (T4-476's stated weights) with the T4-467 strict "
      "component endpoints: upper with the improved H^2 upper equals E2_upper_square_exact and is < %s^2; "
      "H_lower_square_exact equals T4-472's and exceeds (%s)^2 by %s (FLOAT); lower with that H^2 lower is "
      "> %s^2 > %s^2 (007)"
      % (P6["E2_upper"], P6["H_lower"], mp.nstr(fl(Fr(R6_["H_lower_square_exact"]) - Hlo ** 2), 4), P6["E2_lower"],
         P6["baseline007_E2_upper"]),
      E2sq(up, Hsq_up) == Fr(R6_["E2_upper_square_exact"]) and E2sq(up, Hsq_up) < Fr(P6["E2_upper"]) ** 2
      and Fr(R6_["H_lower_square_exact"]) == Fr(R472["H_lower_square_exact"]) > Hlo ** 2
      and Fr(R472["H_strict_lower_exact"]) == Hlo
      and E2sq(lo, Fr(R6_["H_lower_square_exact"])) > E2sq(lo, Hlo ** 2) > Fr(P6["E2_lower"]) ** 2
      and Fr(P6["E2_lower"]) > Fr(P6["baseline007_E2_upper"]) and all(lo[k] < up[k] for k in lo))
OUT["G"] = {"inputs": {"c1-t4/research/candidate016_prefix_hardy_audit/" + k: h for k, h in PIN6.items()},
            "M2_upper_float": float(M2u), "UM_eq4_float": float(UM4), "improved_Hsq_upper_float": float(Hsq_up),
            "E2_upper_float": float(mp.sqrt(mp.mpf(float(E2sq(up, Hsq_up))))),
            "E2_lower_float": float(mp.sqrt(mp.mpf(float(E2sq(lo, Hlo ** 2)))))}

el = time.time() - T0
print("%d checks, %d FAIL, %.2f s" % (N_[0], len(FAILS), el))
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N_[0], FAILS, round(el, 2)
(HERE_ / "data/review_t4_474_results.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
sys.exit(1 if FAILS else 0)
