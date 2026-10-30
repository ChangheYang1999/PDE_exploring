"""Independent checks by c1-t1 of two c1-t4 items (reviews R1-004, R1-005 in
nonlinear_closure/REVIEWS_v02.md).

R1-004  T4-017 (c1-t4/research/symmetry_point_witness/PROOF.md, sha256 f9344e90...):
        (a) FLOAT sanity check of the parity-projected gradient evaluation constant
            (1/2)[C1^2 - G_s''(2|y|)] <= C1^2/2 for |y| >= 1/2, via the Bessel formula (6)
            and via direct quadrature of the Fourier integral;
        (b) exact rational check of the relaxations in section 4 (pi > 3, also pi > 333/106);
        (c) application of the improved point bound (2) to the N4 Cartesian point intervals
            (data/N4_cartesian_witnesses.json, copied from c1-t4) for the uniform scalar-gap
            family (mu <= 3/10), for the FW-T-TB-rebal-v1 ball and for the FW-T-TB-graded-v1
            instance box, plus the uniform graded-family coefficient.
R1-005  T4-013 rational box (c1-t4 graded_closure_audit/verification/rational_box.json):
        reproduction with c1-t1's own gamma_map (artifacts/graded_calc/graded_calc.py) in
        mpmath interval arithmetic, and the feedback condition q0 < mH sqrt(m0) of the T4-013
        theorem for the c1-t1 instance of graded_instance.py.

Usage (from artifacts/checks):
  OMP_NUM_THREADS=1 python3 -B check_T4013_T4017.py > check_T4013_T4017.out
Needs mpmath and python-flint.
"""
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "graded_calc"))
sys.dont_write_bytecode = True
from graded_calc import gamma_map  # noqa: E402

ctx.prec = 256


def ivs(x):
    """midpoint of an mpmath iv interval as a float string"""
    return mp.nstr(mp.mpf(str(x.mid).strip("[]").split(",")[0]), 15)


def A(q):
    q = Q(q)
    return arb(q.numerator) / q.denominator


print("=== R1-004 (a): FLOAT check of the parity-projected constant ===")
mp.mp.dps = 30
for s in (mp.mpf(2) ** -18, mp.mpf(2) ** -16, mp.mpf(5) * 2 ** -18, mp.mpf(1) / 4, mp.mpf(1) / 2):
    C1sq = 1 / (8 * mp.pi * s * (1 + s))
    for y in (mp.mpf(1) / 2, mp.mpf(1), mp.mpf(2)):
        r = 2 * y
        # formula (6): -G'' = (r/2)^s/(4 pi Gamma(2+s)) [K_s(r) - r K_{1-s}(r)]
        mGpp = (r / 2) ** s / (4 * mp.pi * mp.gamma(2 + s)) * (mp.besselk(s, r) - r * mp.besselk(1 - s, r))
        # direct: G(r) = 1/(4 pi Gamma(2+s)) int_0^inf t^s exp(-t - r^2/(4t)) dt, differentiate numerically
        G = lambda rr: mp.quad(lambda t: t ** s * mp.exp(-t - rr ** 2 / (4 * t)), [0, 1, mp.inf]) / (4 * mp.pi * mp.gamma(2 + s))
        mGpp_num = -mp.diff(G, r, 2)
        const = (C1sq + mGpp) / 2  # (1/2)[C1^2 - G''] since mGpp = -G''
        print(f"s={mp.nstr(s, 6):>10} y={mp.nstr(y, 3):>4}  -G''(2y) formula={mp.nstr(mGpp, 10):>16} numeric={mp.nstr(mGpp_num, 10):>16}"
              f"  sign ok={mGpp <= 0}  ratio const/(C1^2/2)={mp.nstr(const / (C1sq / 2), 10)}")
# direct Fourier quadrature of (2pi)^-2 int xi_y^2 cos^2(y xi_y) (1+|xi|^2)^(-2-s) at s=1/4, y=1
mp.mp.dps = 20
s = mp.mpf(1) / 4
y = mp.mpf(1)
inner = lambda eta: mp.quad(lambda xi: (1 + xi ** 2 + eta ** 2) ** (-2 - s), [-mp.inf, 0, mp.inf])
# inner integral in closed form: int_R (c + xi^2)^(-2-s) dxi = c^(-3/2-s) sqrt(pi) Gamma(3/2+s)/Gamma(2+s), c = 1 + eta^2
inner = lambda eta: (1 + eta ** 2) ** (-mp.mpf(3) / 2 - s) * mp.sqrt(mp.pi) * mp.gamma(mp.mpf(3) / 2 + s) / mp.gamma(2 + s)
# cos^2 = (1 + cos(2 y eta))/2; the nonoscillatory half in closed form (Beta integral), the oscillatory half by quadosc
nonosc = mp.sqrt(mp.pi) * mp.gamma(mp.mpf(3) / 2 + s) / mp.gamma(2 + s) * mp.beta(mp.mpf(3) / 2, s) / 2
osc = mp.quadosc(lambda eta: eta ** 2 * mp.cos(2 * y * eta) * inner(eta), [0, mp.inf], omega=2 * y)
direct = (nonosc + osc) / 2 * 2 / (4 * mp.pi ** 2)
C1sq = 1 / (8 * mp.pi * s * (1 + s))
r = 2 * y
mGpp = (r / 2) ** s / (4 * mp.pi * mp.gamma(2 + s)) * (mp.besselk(s, r) - r * mp.besselk(1 - s, r))
print(f"direct quadrature s=1/4,y=1: {mp.nstr(direct, 10)}  formula (1/2)[C1^2-G'']: {mp.nstr((C1sq + mGpp) / 2, 10)}  C1^2/2: {mp.nstr(C1sq / 2, 10)}")

mp.mp.dps = 30
print()
print("=== R1-004 (b): exact rational relaxations of T4-017 section 4 ===")
import sympy as sp
mu_, s_ = sp.symbols("mu s", positive=True)
f = sp.sqrt(s_) * (mu_ - 4800 * s_) / 5
crit = sp.solve(sp.diff(f, s_), s_)
fmax = sp.simplify(f.subs(s_, crit[0]))
print("argmax s =", crit, " max =", fmax, " equals mu^(3/2)/900:", sp.simplify(fmax - mu_ ** sp.Rational(3, 2) / 900) == 0)
mu = Q(3, 10)
for name, pil in (("pi>3", Q(3)), ("pi>333/106", Q(333, 106))):
    # C1s r < mu/(20 sqrt(pi)): compare squares mu^2/(400 pi) < (87/10000)^2
    c1 = mu ** 2 / (400 * pil) < Q(87, 10000) ** 2
    # C0 r < mu^(3/2)/(1800 sqrt(pi)): squares mu^3/(1800^2 pi) < (53/10^6)^2
    c0 = mu ** 3 / (1800 ** 2 * pil) < Q(53, 1000000) ** 2
    pr = Q(53, 1000000) * Q(87, 10000) < Q(1, 2000000)
    print(f"{name}: C1s r bound {c1}, C0 r bound {c0}, product bound {pr}")
# exact value check of the C1s r chain: C1s r < [16 pi s(1+s)]^(-1/2) sqrt(s) mu/5 <= mu/(20 sqrt(pi))
print("C1s r chain: [16 pi s]^(-1/2) sqrt(s) mu/5 = mu/(20 sqrt(pi)) -> at mu=3/10:", float(3 / (200 * mp.sqrt(mp.pi))))

print()
print("=== R1-004 (c): application to N4 Cartesian point intervals ===")
data = json.loads((HERE / "data" / "N4_cartesian_witnesses.json").read_text())
PI = arb.pi()


def consts(s):
    s = A(s)
    C0 = 1 / (4 * PI * (1 + s)).sqrt()
    C1 = 1 / (8 * PI * s * (1 + s)).sqrt()
    C1s = 1 / (16 * PI * s * (1 + s)).sqrt()
    return C0, C1, C1s


def gap(F, V, G, C0, C1, r):
    rhs = (C1 * V + C0 * (1 + G)) * r + C0 * C1 * r * r
    return abs(F) - rhs


# uniform scalar-gap family, mu <= 3/10, rational constants (4)
for row in data["rows"]:
    fl = row["fields"]
    F, V, G = arb(fl["residual"]), arb(fl["velocity_norm"]), arb(fl["gradient_norm"])
    rhs4 = A(Q(87, 10000)) * V + A(Q(53, 1000000)) * (1 + G) + A(Q(1, 2000000))
    g4 = abs(F) - rhs4
    print(f"{row['candidate']:>12} {row['point']}: |F|={abs(F).mid().str(8)} |V|={V.mid().str(8)} |Drho|={G.mid().str(8)}"
          f"  gap(4)={g4.str(10)} strictly positive={g4 > 0}")
print()
# specific balls / boxes: (label, s, ball radius bound on ||h||_(H^(2+s)))
ng_inst = mp.sqrt(mp.mpf("2.022e-4") ** 2 + 2 * mp.mpf("3.347e-7") ** 2 + mp.mpf("1.899e-8") ** 2)
balls = [
    ("FW-A2-Db ball (s=2^-18, r=2^-16)", Q(1, 2 ** 18), A(Q(1, 2 ** 16))),
    ("FW-T-TB-rebal-v1 ball (s=2^-16, r=3*2^-15)", Q(1, 2 ** 16), A(Q(3, 2 ** 15))),
    ("FW-T-TB-graded-v1 instance (s=5*2^-18, n_g upper)", Q(5, 2 ** 18),
     (A(Q(2022, 10 ** 7)) ** 2 + 2 * A(Q(3347, 10 ** 10)) ** 2 + A(Q(1899, 10 ** 11)) ** 2).sqrt()),
    ("T4-013 rational box (s=1/50000)", Q(1, 50000),
     (A(Q(1, 5000)) ** 2 + 2 * A(Q(1, 3000000)) ** 2 + A(Q(1, 50000000)) ** 2).sqrt()),
]
for label, s, rb in balls:
    C0, C1, C1s = consts(s)
    print(label, " radius", rb.mid().str(8))
    for row in data["rows"]:
        fl = row["fields"]
        F, V, G = arb(fl["residual"]), arb(fl["velocity_norm"]), arb(fl["gradient_norm"])
        g_plain = gap(F, V, G, C0, C1, rb)
        g_sym = gap(F, V, G, C0, C1s, rb)
        print(f"   {row['candidate']:>12} {row['point']}: gap T4-007 constant={g_plain.str(8)} ({g_plain > 0}),"
              f" gap T4-017 constant={g_sym.str(8)} ({g_sym > 0})")
# uniform graded family: m2 > 0 forces nu < (1/2 - 4708 s)/(A_s + B_s) <= 1/(2(127/50 + 9/5)); then
# C1s n_g = C1s sqrt(s) nu <= nu/(4 sqrt(pi)); C0 n_g <= C0 nu sqrt(s), s < 1/(2*4708)
nu_max = A(Q(1, 2)) / (A(Q(127, 50)) + A(Q(9, 5)))
c1coef = nu_max / (4 * PI.sqrt())
smax = A(Q(1, 2 * 4708))
c0coef = nu_max * smax.sqrt() / (4 * PI).sqrt()
print()
print("uniform graded family (only m2 > 0 used): coefficient of |V| <", c1coef.str(8), " of (1+|Drho|) <", c0coef.str(8))
for row in data["rows"]:
    fl = row["fields"]
    F, V, G = arb(fl["residual"]), arb(fl["velocity_norm"]), arb(fl["gradient_norm"])
    gu = abs(F) - (c1coef * V + c0coef * (1 + G) + c0coef * c1coef)
    print(f"   {row['candidate']:>12} {row['point']}: uniform graded gap={gu.str(8)} strictly positive={gu > 0}")

print()
print("=== R1-005: reproduction of the T4-013 rational box with c1-t1 gamma_map (mpmath iv, 60 digits) ===")
mp.iv.dps = 60
box = json.loads((HERE / "data" / "rational_box.json").read_text())
s = mp.iv.mpf(Q(box["s"]).numerator) / Q(box["s"]).denominator
rr = [mp.iv.mpf(Q(x).numerator) / Q(x).denominator for x in box["box"]]
ph = [mp.iv.mpf(Q(x).numerator) / Q(x).denominator for x in box["forcing_upper_bounds"]]
out = gamma_map(s, rr, ph, lib=mp.iv)
assert out is not None
Gam, mar = out
names = ["P", "a", "b", "H"]
for i, nm in enumerate(names):
    t4 = arb(box["Gamma"][i])
    mine = Gam[i]
    print(f"Gamma_{nm}: c1-t1 mid {ivs(mine)} width {ivs(mine.delta)}  T4 {t4.mid().str(15)}  slack positive={mine.b < rr[i].a}")
for k in ("m2", "m1", "m0", "mH", "nu"):
    print(f"  {k} = {ivs(mar[k])} (width {ivs(mar[k].delta)})")
q0 = 476 * s + mar["nu"]
print("  feedback q0 < mH sqrt(m0):", (q0.b < (mar["mH"] * mp.iv.sqrt(mar["m0"])).a), " denominator 1 - q0/(mH sqrt m0) =",
      ivs(1 - q0 / (mar["mH"] * mp.iv.sqrt(mar["m0"]))))
ng = mar["ng"]
d = ng / (2 * mp.iv.sqrt(mp.iv.pi * s * (1 + s)))
print("  d =", ivs(d), " contraction d/(19/5-d) =", ivs(d / (mp.iv.mpf(19) / 5 - d)))

print()
print("=== feedback condition for the c1-t1 instance (graded_instance.py box) ===")
s = mp.iv.mpf(5) / 2 ** 18
rr = [mp.iv.mpf("2.022e-4"), mp.iv.mpf("3.347e-7"), mp.iv.mpf("1.899e-8"), mp.iv.mpf("6.686e-8")]
ph = [mp.iv.mpf("27.8") * mp.iv.mpf(x) for x in ("6.358653e-7", "4.967698e-9", "1.241925e-9", "1.272594e-9")]  # graded_instance.py phi
Gam, mar = gamma_map(s, rr, ph, lib=mp.iv)
q0 = 476 * s + mar["nu"]
print("  slacks positive:", [g.b < r_.a for g, r_ in zip(Gam, rr)])
print("  q0 =", ivs(q0), " mH sqrt(m0) =", ivs(mar["mH"] * mp.iv.sqrt(mar["m0"])),
      " feedback holds:", q0.b < (mar["mH"] * mp.iv.sqrt(mar["m0"])).a)
