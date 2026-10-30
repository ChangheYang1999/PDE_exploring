"""Independent review of T4-014 (c1-t4 research/exterior_tail_witness/PROOF.md, sha256 8f3d5dff...30e5).

Run from artifacts/:  python3 -B arith/t4_014_review.py [--no-float]
Needs sympy, python-flint, numpy, scipy.  About 1.5 min with --no-float, about 3 min with the FLOAT part (scipy may print
IntegrationWarnings for the narrow layer bumps; they are FLOAT noise and the asserted tolerances still hold).

Rigorous part (sympy exact, arb at 256 bits):
  (1) the exterior Dirichlet witness v_n of (6), (7): it solves (8), v_n(T) = 0, sign of v_n/a_n, for symbolic n, sigma;
  (2) the radial integral of (9) and the Dirichlet energy equal a_n^2 T^(-2 sigma)/(2 sigma (n + sigma)^2) (both
      n > sigma and n < sigma, and n = sigma);
  (3) the canonical Poisson solution of section 3 solves the mode equation, and the truncated norm (5);
  (4) sharpness (new): the extension F* = -Delta phi (exterior forcing plus the single layer -v_n'(T) on r = T) has
      Poisson potential exactly phi and squared norm exactly K, so (2) is the minimum over all extensions;
  (5) the six-branch sector of A2 P27 (exact sine coefficients e_m from data/a2_p25_nb_stableA2_exact.annular.json,
      copied from A2 certificates/P25_admissible_tail_gap; sigma = 7 delta - 3): effective amplitude of (2), the
      necessary onset (4) at the D(b) H tolerance of the T1 model, against the Hardy-proxy onset of that model;
      (5b) the 6-, 7-, 8-branch sectors from c1-n4's exact recursion (data/n4_forcing_sin_6_8.json): exact agreement of
      the 6-branch vector with A2, and the necessary onsets at the H tolerances of theory_v01 section 5.
FLOAT part:
  (6) direct radial Poisson energies for random interiors and for relative remainders (checks (2), (10) without the
      duality argument), and the dilation law of section 5 for a smooth cutoff.
"""
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import sympy as sp
from flint import arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]


def A(x):
    x = Q(x)
    return arb(x.numerator) / x.denominator


r, t, T = sp.symbols("r t T", positive=True)
sg, p = sp.symbols("sigma p", positive=True)


def mode_op(v, n):
    return -sp.diff(v, r, 2) - sp.diff(v, r) / r + n**2 * v / r**2


# ---------------- (1) the witness ----------------
print("(1) exterior Dirichlet witness, a_n = 1:")
nn = sp.symbols("n", positive=True)
v_gen = (r**(-sg) - T**(nn - sg) * r**(-nn)) / (nn**2 - sg**2)
res = sp.simplify(mode_op(v_gen, nn) - r**(-2 - sg))
print("    (8) defect for symbolic n != sigma:", res, "; v_n(T) =", sp.simplify(v_gen.subs(r, T)))
assert res == 0 and sp.simplify(v_gen.subs(r, T)) == 0
v_log = r**(-nn) * sp.log(r / T) / (2 * nn)
res = sp.simplify(mode_op(v_log, nn) - r**(-2 - nn))
print("    (8) defect for n = sigma (logarithmic case (7)):", res, "; v_n(T) =", sp.simplify(v_log.subs(r, T)))
assert res == 0
# limit of (6) as sigma -> n equals (7)
# numerator and denominator of (6) both vanish at sigma = n; l'Hopital in sigma:
num, den = r**(-sg) - T**(nn - sg) * r**(-nn), nn**2 - sg**2
assert sp.simplify(num.subs(sg, nn)) == 0 and den.subs(sg, nn) == 0
lim = sp.simplify((sp.diff(num, sg) / sp.diff(den, sg)).subs(sg, nn))
print("    limit of (6) as sigma -> n minus (7):", sp.simplify(sp.expand_log(lim - v_log, force=True)))
assert sp.simplify(sp.expand_log(lim - v_log, force=True)) == 0
# sign: v/a = r^-n (r^(n-sigma) - T^(n-sigma))/((n - sigma)(n + sigma)); with x = r/T > 1 and k = n - sigma != 0,
# (x^k - 1)/k > 0 for both signs of k.  Exact check on the representation:
x, k = sp.symbols("x k", positive=True)
dpos, dneg = sp.simplify(sp.diff(x**k - 1, x)), sp.simplify(sp.diff((x**(-k) - 1) / (-k), x))
print("    sign: (x^k - 1)/k (n > sigma) and (x^-k - 1)/(-k) (n < sigma) vanish at x = 1 and have x-derivatives",
      dpos, "and", dneg, "> 0, so v_n/a_n > 0 on r > T")
assert dpos.is_positive and dneg.is_positive

# ---------------- (2) the energy identity ----------------
print("(2) radial integral of (9) and Dirichlet energy, a_n = 1:")
for label, nval, sval in (("n > sigma", sg + p, sg), ("n < sigma", nn, nn + p)):
    v = (r**(-sval) - T**(nval - sval) * r**(-nval)) / (nval**2 - sval**2)
    target = T**(-2 * sval) / (2 * sval * (nval + sval) ** 2)
    pair = sp.integrate(r**(-1 - sval) * v, (r, T, sp.oo), conds="none")
    print(f"    {label}: int_T^oo r^(-1-sigma) v dr - T^(-2 sigma)/(2 sigma (n+sigma)^2) =",
          sp.simplify(pair - target))
    assert sp.simplify(pair - target) == 0
# n = sigma: substitute r = T y; r^(-1-n) v(r) dr = T^(-2n) y^(-1-2n) log(y)/(2n) dy
y = sp.symbols("y", positive=True)
pair = T**(-2 * nn) * sp.integrate(y**(-1 - 2 * nn) * sp.log(y), (y, 1, sp.oo), conds="none") / (2 * nn)
target = T**(-2 * nn) / (2 * nn * (2 * nn) ** 2)
print("    n = sigma:", sp.simplify(pair - target))
assert sp.simplify(pair - target) == 0
# Dirichlet energy int (v'^2 + n^2 v^2/r^2) r dr on exact rational pairs, T = 1 and T = 3
for (n_, s_) in ((1, sp.Rational(2, 15)), (3, sp.Rational(2, 15)), (1, sp.Rational(5, 2)), (5, sp.Rational(1, 2)), (3, 3)):
    for TT in (1, 3):
        if n_ == s_:
            v = r**(-n_) * sp.log(r / TT) / (2 * n_)
        else:
            v = (r**(-s_) - sp.Integer(TT) ** (n_ - s_) * r**(-n_)) / (n_**2 - s_**2)
        en = sp.integrate((sp.diff(v, r) ** 2 + n_**2 * v**2 / r**2) * r, (r, TT, sp.oo))
        tg = sp.Integer(TT) ** (-2 * s_) / (2 * s_ * (n_ + s_) ** 2)
        assert sp.simplify(en - tg) == 0, (n_, s_, TT)
print("    Dirichlet energy = radial pairing = T^(-2 sigma)/(2 sigma (n+sigma)^2) exactly for (n, sigma) in"
      " (1, 2/15), (3, 2/15), (1, 5/2), (5, 1/2), (3, 3), T in {1, 3}")

# ---------------- (3) Poisson solution and the truncated norm ----------------
f = sp.Function("f")
s = sp.symbols("s", positive=True)
u_n = (r**(-nn) * sp.Integral(f(s) * s**(nn + 1), (s, 0, r)) + r**nn * sp.Integral(f(s) * s**(1 - nn), (s, r, sp.oo))) / (2 * nn)
res = sp.simplify(mode_op(u_n, nn) - f(r))
print("(3) Poisson formula of section 3: mode equation defect =", res)
assert res == 0
for label, nval, sval in (("n > sigma", sg + p, sg), ("n < sigma", nn, nn + p)):
    inner = sp.integrate(t**(nval - 1 - sval), (t, T, r), conds="none")
    tr = sp.integrate(r**(-nval - 1 - sval) * inner, (r, T, sp.oo), conds="none") / nval
    target = T**(-2 * sval) / (2 * sval * nval * (nval + sval))
    print(f"    {label}: (1/n) int r^(-n-1-sigma) int_T^r t^(n-1-sigma) - T^(-2 sigma)/(2 sigma n (n+sigma)) =",
          sp.simplify(tr - target))
    assert sp.simplify(tr - target) == 0
tr = T**(-2 * nn) * sp.integrate(y**(-2 * nn - 1) * sp.log(y), (y, 1, sp.oo), conds="none") / nn   # r = T y
assert sp.simplify(tr - T**(-2 * nn) / (2 * nn * nn * 2 * nn)) == 0
print("    n = sigma: agrees.  Ratios: (5)/(2) per mode = (n+sigma)/n; Hardy proxy^2/(5) per mode = n(n+sigma).")

# ---------------- (4) sharpness of (2) ----------------
# F* = a r^(-2-sigma) 1_(r>T) sin(n theta) + mu delta(r - T) sin(n theta), with the radial measure t dt.
nv, sv = sg + p, sg
vD = (r**(-sv) - T**(nv - sv) * r**(-nv)) / (nv**2 - sv**2)
mu = -sp.diff(vD, r).subs(r, T)
print("(4) layer density mu = -v_n'(T) =", sp.simplify(mu), " (= -T^(-1-sigma)/(n+sigma))")
assert sp.simplify(mu + T**(-1 - sv) / (nv + sv)) == 0
# Poisson potential of F* for r < T and r > T
u_in = r**nv * (sp.integrate(t**(-2 - sv) * t**(1 - nv), (t, T, sp.oo), conds="none") + mu * T * T**(-nv)) / (2 * nv)
u_out = (r**(-nv) * (sp.integrate(t**(-2 - sv) * t**(nv + 1), (t, T, r), conds="none") + mu * T * T**nv)
         + r**nv * sp.integrate(t**(-2 - sv) * t**(1 - nv), (t, r, sp.oo), conds="none")) / (2 * nv)
print("    Poisson potential of F*: inside r < T:", sp.simplify(u_in), "; outside minus v_n:", sp.simplify(u_out - vD))
assert sp.simplify(u_in) == 0 and sp.simplify(u_out - vD) == 0
print("    so ||F*||_H^2 = pi int F* phi = pi int_T^oo a r^(-2-sigma) v_n r dr + pi mu T v_n(T) = K exactly:"
      " (2) is attained, it is the minimum over all extensions in H of the exterior data (1).")

# ---------------- (5) the six-branch sector ----------------
z = json.loads((HERE / "data/a2_p25_nb_stableA2_exact.annular.json").read_text())
e = {int(m): Q(vq) for m, vq in z["leading_sine_coefficients"].items()}
assert all(m > 0 and m % 2 == 1 for m in e)
c = Q(4076476460239181, 2**51)
delta = 1 - 1 / c
sigma_q = 7 * delta - 3                                    # F ~ r^(1 - 7 delta) = r^(-2 - sigma)
sig = A(sigma_q)
pi = arb.pi()
A2 = pi * sum((A(vq) ** 2 for vq in e.values()), arb(0))
S2 = sum((A(vq) ** 2 / (m + sig) ** 2 for m, vq in e.items()), arb(0))
S5 = sum((A(vq) ** 2 / (m * (m + sig)) for m, vq in e.items()), arb(0))
Aeff = (pi * S2).sqrt()
Atr = (pi * S5).sqrt()
print("(5) six-branch leading residual sector (A2 P27 e_m, 70 odd modes up to", max(e), "): sigma = 7 delta - 3 =",
      sig.str(12))
print("    A = sqrt(pi sum e_m^2) =", A2.sqrt().str(15), " (A2: 3081.27440111579...)")
print("    A_eff = sqrt(pi sum e_m^2/(m+sigma)^2) =", Aeff.str(12), "; A_eff/A =", (Aeff / A2.sqrt()).str(8))
print("    A_tr = sqrt(pi sum e_m^2/(m(m+sigma))) =", Atr.str(12), " (exact truncated model (5))")
mshare = {m: float((A(vq) ** 2 * pi / A2).mid().str(12, radius=False)) for m, vq in e.items()}
top = sorted(mshare.items(), key=lambda kv: -kv[1])[:5]
print("    largest shares of A^2:", ", ".join(f"m={m}: {sh:.4f}" for m, sh in top), "; share of m = 1:", f"{mshare[1]:.3e}")
tau = A(Q(12726, 10**13))                                   # T1 model D(b) H tolerance 1.2726e-9
two_s = 2 * sig
proxy = (A2.sqrt() / (tau * two_s.sqrt())) ** (1 / sig)
nec = (Aeff / (tau * two_s.sqrt())) ** (1 / sig)
trunc = (Atr / (tau * two_s.sqrt())) ** (1 / sig)
l10 = arb(10).log()
for name, val in (("Hardy proxy onset (T1 model, D(b))", proxy), ("necessary onset (4) with the mode weights of (2)", nec),
                  ("exact onset for the truncated model (5)", trunc)):
    print(f"    {name}: log10 T = {(val.log() / l10).str(8)}")
print("    the necessary onset is smaller than the proxy onset by the factor (A/A_eff)^(1/sigma) = 10^"
      + ((proxy / nec).log() / l10).str(6))
assert (nec.log() / l10) > 80
print("    (3) with N = max m =", max(e), "would use A/(N + sigma) =", (A2.sqrt() / (max(e) + sig)).str(8),
      "instead of A_eff: the mode-weighted form (2) is needed for this sector")
# radius at which the bound (2) for this sector equals the uniform degree-limited family bound of A2 P27, 2.67750e-7
p27 = A(Q(267750, 10**12))
T_eq = (Aeff / (two_s.sqrt() * p27)) ** (1 / sig)
print("    (2) equals the A2 P27 uniform family bound ||F||_H > 2.67750e-7 at onset T = 10^" + (T_eq.log() / l10).str(6))
# with relative remainder eps the necessary onset is multiplied by (1 - eps)^(1/sigma)
for eps in (Q(1, 2), Q(9, 10)):
    print(f"    with relative remainder eps = {eps} in (10): log10 T_nec = {((nec * (1 - A(eps)) ** (1 / sig)).log() / l10).str(8)}")

# (5b) the 6-, 7- and 8-branch sectors from c1-n4's exact recursion (data/n4_forcing_sin_6_8.json, extracted by
# arith/extract_sector_vectors.py); the index-6 vector must agree exactly with the A2 P25 vector used above.
zn = json.loads((HERE / "data/n4_forcing_sin_6_8.json").read_text())
assert Q(zn["cl"]) == c
e6 = {int(m): Q(vq) for m, vq in zn["branches"]["6"]["forcing_sin"].items()}
print("(5b) c1-n4 index-6 sine vector equals the A2 P25 vector exactly:", e6 == e)
assert e6 == e
tols = (("T1 model D(b)", Q(12726, 10**13)), ("FW-T-TB-rebal-v1", Q(18332, 10**12)),
        ("FW-T-TB-graded-v1 (i)", Q(35378, 10**12)), ("FW-T-TB-graded-v1 (ii)", Q(31820, 10**12)),
        ("FW-T-TB-sharp-v1", Q(21259, 10**11)))
print("    necessary onsets log10 T_min = log10[(A_w/(tau sqrt(2 sigma)))^(1/sigma)] with the H tolerances tau of"
      " theory_v01 section 5; A_w = A/(1 + sigma) (theory_v01 N = 1), A/(N + sigma) (N = max m) and A_eff (exact (2)):")
for j in ("6", "7", "8"):
    bj = zn["branches"][j]
    ej = {int(m): Q(vq) for m, vq in bj["forcing_sin"].items()}
    sj = A(-2 - Q(bj["residual_exponent"]))
    Aj = (pi * sum((A(vq) ** 2 for vq in ej.values()), arb(0))).sqrt()
    Aej = (pi * sum((A(vq) ** 2 / (m + sj) ** 2 for m, vq in ej.items()), arb(0))).sqrt()
    Nj = max(ej)
    shares = sorted(((m, float((A(vq) ** 2 * pi / Aj**2).mid().str(10, radius=False))) for m, vq in ej.items()),
                    key=lambda kv: -kv[1])[:3]
    print(f"    branches {j}: sigma = {sj.str(10)}, A = {Aj.str(12)}, N = {Nj}, A_eff = {Aej.str(12)},"
          f" A_eff/A = {(Aej / Aj).str(6)}; largest shares " + ", ".join(f"m={m}: {q:.3f}" for m, q in shares))
    for name, tq in tols:
        tt = A(tq) * (2 * sj).sqrt()
        vals = [((Aw / tt).log() / l10 / sj) for Aw in (Aj / (1 + sj), Aj / (Nj + sj), Aej)]
        print(f"      {name:24s} tau = {float(tq):.4e}: N = 1: {vals[0].str(5)}, N = {Nj}: {vals[1].str(5)},"
              f" exact (2): {vals[2].str(6)}")

if "--no-float" in sys.argv:
    print("done (FLOAT checks skipped)")
    sys.exit(0)

# ---------------- (6) FLOAT: direct radial Poisson energies ----------------
import numpy as np
from scipy.integrate import quad

rng = np.random.default_rng(14)


def energy(n, f_in, T_, a_, sig_, f_out_rel=None):
    """pi/n int_0^oo f(r) r^(1-n) int_0^r f(t) t^(n+1) dt dr, f = f_in on (0, T), a r^(-2-sig)(1 + rel(r)) outside."""
    if f_out_rel is None:
        f_out = lambda rr: a_ * rr ** (-2 - sig_)
    else:
        f_out = lambda rr: a_ * rr ** (-2 - sig_) * (1 + f_out_rel(rr))
    f_full = lambda rr: f_in(rr) if rr < T_ else f_out(rr)
    I = lambda rr: quad(lambda tt: f_full(tt) * tt ** (n + 1), 0, rr, points=[T_] if rr > T_ else None, limit=400)[0]
    inner = quad(lambda rr: f_in(rr) * rr ** (1 - n) * I(rr), 0, T_, limit=200)[0]
    # exterior in u = log r, truncated at r = T e^60 (tail below 1e-6 relative for sig >= 0.13)
    outer = quad(lambda uu: f_out(T_ * np.exp(uu)) * (T_ * np.exp(uu)) ** (2 - n) * I(T_ * np.exp(uu)), 0, 60, limit=400)[0]
    return np.pi / n * (inner + outer)


print("(6) FLOAT direct Poisson energies, mode n, sigma = 2/15, T = 1.5, a = 1, against K = pi T^(-2 sigma)/(2 sigma (n+sigma)^2):")
sig_f, T_, a_ = 2 / 15, 1.5, 1.0
for n in (1, 3):
    Kn = np.pi * T_ ** (-2 * sig_f) / (2 * sig_f * (n + sig_f) ** 2)
    rows = []
    for trial in range(4):
        cf = rng.normal(size=3) * 2.0
        f_in = lambda rr, cf=cf: (cf[0] * rr ** n + cf[1] * rr ** (n + 2) + cf[2] * rr ** (n + 4)) * np.exp(-rr)
        rows.append(energy(n, f_in, T_, a_, sig_f) / Kn)
    # near-layer interior: a narrow negative bump of total radial mass mu T just inside r = T
    mu_ = -T_ ** (-1 - sig_f) / (n + sig_f)
    for wdt in (0.05, 0.01):
        f_in = lambda rr, wdt=wdt: (mu_ * T_ / (wdt * T_)) * (rr > T_ - wdt) / rr
        rows.append(energy(n, f_in, T_, a_, sig_f) / Kn)
    tr = energy(n, lambda rr: 0.0, T_, a_, sig_f) / Kn
    print(f"    n = {n}: ||F||^2/K for 4 random interiors: " + ", ".join(f"{q:.4f}" for q in rows[:4])
          + f"; layer approximants (width 0.05, 0.01): {rows[4]:.5f}, {rows[5]:.5f}; truncated: {tr:.5f}"
          f" (exact (n+sigma)/n = {(n + sig_f) / n:.5f})")
    assert min(rows) > 1 - 1e-6 and abs(tr - (n + sig_f) / n) < 1e-5
# relative remainder (10): exterior a r^(-2-sigma)(1 + eps s(r)), |s| <= 1, zero interior or random interior
eps = 0.5
for n in (1, 3):
    Kn = np.pi * T_ ** (-2 * sig_f) / (2 * sig_f * (n + sig_f) ** 2)
    worst = np.inf
    for trial in range(3):
        ph = rng.uniform(0, 2 * np.pi)
        rel = lambda rr, ph=ph: -eps * (0.5 + 0.5 * np.cos(3 * np.log(rr) + ph))
        cf = rng.normal(size=2)
        f_in = lambda rr, cf=cf: (cf[0] * rr ** n + cf[1] * rr ** (n + 2)) * np.exp(-rr)
        worst = min(worst, np.sqrt(energy(n, f_in, T_, a_, sig_f, rel) / Kn))
    print(f"    remainder eps = {eps}, n = {n}: min ||F||/sqrt(K) over 3 trials = {worst:.4f} >= 1 - eps = {1 - eps}")
    assert worst >= 1 - eps
# section 5 dilation law with a smooth cutoff chi (0 on r <= 1, 1 on r >= 2)


def chi(rr):
    if rr <= 1:
        return 0.0
    if rr >= 2:
        return 1.0
    g = lambda y: np.exp(-1 / y) if y > 0 else 0.0
    return g(rr - 1) / (g(rr - 1) + g(2 - rr))


# the smooth part on (T, 2T) is the "interior" profile, the exact power holds beyond 2T
vals = [np.sqrt(energy(1, lambda rr, TT=TT: chi(rr / TT) * rr ** (-2 - sig_f), 2 * TT, 1.0, sig_f)) for TT in (1.0, 2.0, 4.0)]
print("    section 5: ||F_T||_H for T = 1, 2, 4 (mode 1, sigma = 2/15):", ", ".join(f"{q:.6f}" for q in vals),
      "; ratios", f"{vals[1] / vals[0]:.6f}, {vals[2] / vals[1]:.6f}", f"(2^-sigma = {2 ** -sig_f:.6f})")
assert abs(vals[1] / vals[0] - 2 ** -sig_f) < 1e-5
print("done")
