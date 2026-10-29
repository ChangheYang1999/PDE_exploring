"""Checks for the v7 revision of FULL_SPACE_PRESSURE.md (independent mathematical review, findings 20-26, 30, 31).

Single-threaded sympy / mpmath / numpy; prints PASS/FAIL lines and writes checks/docrev_P_check_output.json.
Reads (never writes) the frozen verifier records and one frozen export of the primary search.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import resource
resource.setrlimit(resource.RLIMIT_CPU, (110, 110))
import json, math, time, glob
import sympy as sp

t0 = time.process_time()
HERE = os.path.dirname(os.path.abspath(__file__))
LEAD = os.path.dirname(HERE)
VER = "<local>/e4/independent_validation"
D64 = ("numerical_search/candidates/"
       "T1_seed_cl0p74/L3/samples.npz")
results = {}


def report(name, ok, detail=""):
    results[name] = {"pass": bool(ok), "detail": str(detail)}
    print(("PASS " if ok else "FAIL ") + name + ((": " + str(detail)) if detail != "" else ""))


x, y, z = sp.symbols("x y z", real=True)
X = (x, y, z)

# ---------------- finding 22: d_i d_j (U_i U_j) versus tr(DU^2) ----------------
U = [sp.Function(n)(x, y, z) for n in ("U1", "U2", "U3")]
lhs = sum(sp.diff(U[i] * U[j], X[i], X[j]) for i in range(3) for j in range(3))
DU = sp.Matrix(3, 3, lambda i, j: sp.diff(U[i], X[j]))
divU = sum(sp.diff(U[i], X[i]) for i in range(3))
rhs = (DU * DU).trace() + 2 * sum(U[i] * sp.diff(divU, X[i]) for i in range(3)) + divU ** 2
report("F22 identity d_i d_j(U_i U_j) = tr(DU^2) + 2 U.grad div U + (div U)^2", sp.expand(lhs - rhs) == 0)
Uy = [x, y, z]
lhs_y = sum(sp.diff(Uy[i] * Uy[j], X[i], X[j]) for i in range(3) for j in range(3))
tr_y = (sp.Matrix(3, 3, lambda i, j: sp.diff(Uy[i], X[j])) ** 2).trace()
report("F22 U(y) = y: d_i d_j(U_i U_j) = 12, tr(DU^2) = 3", lhs_y == 12 and tr_y == 3, f"{lhs_y}, {tr_y}")

# interface examples: solid rotation inside / zero outside, and a rotation reversed across R = a
om, a_ = sp.symbols("omega a", positive=True)
Rr = sp.sqrt(x**2 + y**2 + z**2)
nvec = [x / Rr, y / Rr, z / Rr]
rot = [-om * y, om * x, 0]
acc = [sum(rot[k] * sp.diff(rot[i], X[k]) for k in range(3)) for i in range(3)]       # (U.grad)U
acc_rev = [sum(-rot[k] * sp.diff(-rot[i], X[k]) for k in range(3)) for i in range(3)]  # reversed rotation
mu_s = sp.symbols("mu")
on_sphere = {x: a_ * sp.sqrt(1 - mu_s**2), y: 0, z: a_ * mu_s}
F_solid = sp.simplify((0 - sum(acc[i] * nvec[i] for i in range(3))).subs(on_sphere))
F_rev = sp.simplify(sum((acc_rev[i] - acc[i]) * nvec[i] for i in range(3)).subs(on_sphere))
UN_rot = sp.simplify(sum(rot[i] * nvec[i] for i in range(3)))
report("F22 solid rotation inside, zero outside: J = 0, F = omega^2 a (1 - mu^2)",
       UN_rot == 0 and sp.simplify(F_solid - om**2 * a_ * (1 - mu_s**2)) == 0, F_solid)
report("F22 rotation reversed across the sphere: tangential jump, J = 0 and F = 0", F_rev == 0, F_rev)

# ---------------- finding 23: binary64 under/overflow ----------------
import numpy as np
with np.errstate(over="ignore", under="ignore"):
    u1075 = 0.5 ** 1075
    u1074 = 0.5 ** 1074
    p77 = np.float64(1e4) ** 77
    p78 = np.float64(1e4) ** 78
report("F23 0.5^1075 underflows to 0 in binary64 (0.5^1074 is the smallest subnormal)",
       u1075 == 0.0 and u1074 > 0.0, f"{u1075}, {u1074}")
report("F23 1e4^77 finite, 1e4^78 = inf (overflow threshold log10(max) = 308.25)",
       np.isfinite(p77) and np.isinf(p78), f"{p77}, {p78}, log10 max {math.log10(np.finfo(float).max):.4f}")
report("F23 smallest normal binary64 is 2^-1022", np.finfo(float).tiny == 2.0 ** -1022, np.finfo(float).tiny)
s_, R_, l_ = sp.symbols("s R l", positive=True)
report("F23 scaled powers: R^(-l-1) s^(l+2) = s (s/R)^(l+1), R^l s^(1-l) = s (R/s)^l",
       sp.simplify(sp.powsimp(R_**(-l_ - 1) * s_**(l_ + 2) - s_ * (s_ / R_)**(l_ + 1), force=True)) == 0
       and sp.simplify(sp.powsimp(R_**l_ * s_**(1 - l_) - s_ * (R_ / s_)**l_, force=True)) == 0)

# ---------------- Green formulas of the document ----------------
def green(src_in, src_out, l, d, R0=1):
    """Document's per-mode Green formula, n = 2l + d - 2, source src_in on (0, R0), src_out on (R0, oo); R > R0."""
    n = 2 * l + d - 2
    I = sp.integrate(s_**(l + d - 1) * src_in, (s_, 0, R0)) + sp.integrate(s_**(l + d - 1) * src_out, (s_, R0, R_))
    E = sp.integrate(s_**(1 - l) * src_out, (s_, R_, sp.oo))
    return sp.simplify((R_**(-l - d + 2) * I + R_**l * E) / n), I


def radial_op(u, l, d):
    return -sp.diff(u, R_, 2) - (d - 1) * sp.diff(u, R_) / R_ + l * (l + d - 2) * u / R_**2


# ---------------- finding 24: resonant 5D stream moment ----------------
aa, bb = sp.symbols("a b", real=True)
ok24 = True
details24 = []
for m in range(0, 6):
    n = 2 * m + 3
    phi_m, I = green(bb, aa * s_**(-m - 5), m, 5)
    C = sp.simplify(I - aa * sp.log(R_))          # int_0^R s^(m+4) eta_m ds = a log R + C
    target = R_**(-m - 3) * (aa / n * sp.log(R_) + C / n + aa / n**2)
    ok = sp.simplify(phi_m - target) == 0 and sp.simplify(radial_op(phi_m, m, 5) - aa * R_**(-m - 5)) == 0
    ok = ok and C.free_symbols <= {bb}
    ok24 = ok24 and ok
    details24.append(f"m={m}: C={C}")
report("F24 5D Green, eta_m = a R^(-m-5) outside the unit ball: phi_m = R^(-m-3)((a/n)log R + C/n + a/n^2), m = 0..5",
       ok24, "; ".join(details24))
# symbolic degree: exterior term alone
mm = sp.symbols("m", positive=True)
ext = sp.integrate(s_**(1 - mm) * aa * s_**(-mm - 5), (s_, R_, sp.oo), conds="none")
report("F24 exterior term for symbolic m: R^m int_R^oo s^(1-m) a s^(-m-5) ds / n = (a/n^2) R^(-m-3)",
       sp.simplify(R_**mm * ext / (2 * mm + 3) - aa / (2 * mm + 3)**2 * R_**(-mm - 3)) == 0)
# non-resonant tails: the R^(-m-3) coefficient is (finite part of the interior moment)/n
ok_nr = True
for m in (0, 1, 2):
    n = 2 * m + 3
    for p in (sp.Rational(9, 2) + m, sp.Rational(13, 2) + m, sp.Rational(10, 3) + m):  # slower and faster than resonance
        phi_m, I = green(bb, aa * s_**(-p), m, 5)
        e = m + 5 - p
        if e > 0:
            FP = sp.limit(I - aa * R_**e / e, R_, sp.oo)
        else:
            FP = sp.limit(I, R_, sp.oo)
        rest = sp.simplify(phi_m - FP / n * R_**(-m - 3))
        # the rest must be a pure multiple of R^(2-p) (local tail term), with no R^(-m-3) part
        ok_nr = ok_nr and sp.simplify(rest * R_**(p - 2)).free_symbols <= {aa, bb}
report("F24 non-resonant tails a R^(-p): coefficient of R^(-m-3) = finite part of int_0^oo s^(m+4) eta_m / n", ok_nr)
# 3D analogue used by finding 20: f_l = k R^(-l-3) outside the unit ball gives (k/(2l+1)) R^(-l-1) log R
kk = sp.symbols("k", real=True)
P2, I2 = green(bb, kk * s_**(-5), 2, 3)
logc = sp.simplify(sp.expand(P2 * R_**3).coeff(sp.log(R_)))
report("F20 3D Green, f_2 = k R^-5 outside a ball: coefficient of R^-3 log R is k/5", sp.simplify(logc - kk / 5) == 0, logc)

# ---------------- finding 25: piecewise 5D potential 1 / R^-3 ----------------
phi_in, phi_out = sp.Integer(1), R_**-3
lap5 = lambda u: sp.diff(u, R_, 2) + 4 * sp.diff(u, R_) / R_
jump_val = (phi_out - phi_in).subs(R_, 1)
jump_der = (sp.diff(phi_out, R_) - sp.diff(phi_in, R_)).subs(R_, 1)
layer = -jump_der            # -Delta phi = eta_bulk - [d_R phi] delta(R - 1) - div([phi] n delta)
Rs = sp.symbols("Rs", positive=True)
dl = layer * sp.DiracDelta(s_ - 1)
rec_out = sp.simplify((Rs**-3 * sp.integrate(s_**4 * dl, (s_, 0, Rs)) + sp.integrate(s_ * dl, (s_, Rs, sp.oo))) / 3)
rec_out = sp.simplify(rec_out.subs(Rs, 2))
rec_in = sp.simplify((sp.Rational(1, 2)**-3 * sp.integrate(s_**4 * dl, (s_, 0, sp.Rational(1, 2)))
                      + sp.integrate(s_ * dl, (s_, sp.Rational(1, 2), sp.oo))) / 3)
# verifier interface formula, d = 5, l = 0
d_, l0 = 5, 0
I0 = -(1 * jump_der + (l0 + d_ - 2) * jump_val) / (2 * l0 + d_ - 2)
O0 = (l0 * jump_val - 1 * jump_der) / (2 * l0 + d_ - 2)
report("F25 phi = 1 (R <= 1), R^-3 (R > 1): harmonic on each piece, continuous, bulk inverse 0",
       lap5(phi_in) == 0 and sp.simplify(lap5(phi_out)) == 0 and jump_val == 0)
report("F25 distributional source is the single layer 3 delta(R - 1); Green formula with it returns phi",
       layer == 3 and rec_out == sp.Rational(1, 8) and rec_in == 1 and I0 == 1 and O0 == 1,
       f"layer {layer}, phi(2) {rec_out}, phi(1/2) {rec_in}, I0 {I0}, O0 {O0}")

# ---------------- finding 26: a source mode on another piece generates pressure on this piece ----------------
lh = 34
P_in = sp.simplify(R_**lh / (2 * lh + 1) * sp.integrate(s_**(1 - lh), (s_, 2, 3)))
report("F26 f_34 = 1 on 2 < R < 3 only: P_34 = c R^34 with c != 0 on R < 2", P_in != 0 and sp.degree(P_in, R_) == lh, P_in)

# ---------------- finding 30: elliptic-integral convention of the direct Newton kernel ----------------
import mpmath as mp
mp.mp.dps = 30
ok30 = True
worst = mp.mpf(0)
for (r, rho, dz) in ((0.3, 1.7, 0.4), (2.0, 0.5, -1.1), (1.0, 1.0, 0.05)):
    r, rho, dz = mp.mpf(r), mp.mpf(rho), mp.mpf(dz)
    ang = mp.quad(lambda t: 1 / mp.sqrt(r**2 + rho**2 - 2 * r * rho * mp.cos(t) + dz**2), [0, mp.pi, 2 * mp.pi])
    m = 4 * r * rho / ((r + rho)**2 + dz**2)
    Kdef = mp.quad(lambda t: (1 - m * mp.sin(t)**2) ** mp.mpf(-0.5), [0, mp.pi / 2])
    closed = 4 * Kdef / mp.sqrt((r + rho)**2 + dz**2)
    err = max(abs(ang - closed) / abs(ang), abs(Kdef - mp.ellipk(m)) / Kdef)
    worst = max(worst, err)
report("F30 int_0^2pi dtheta/|x - y| = 4 K(m)/sqrt((r+rho)^2+dz^2) with K(m) = int_0^(pi/2)(1 - m sin^2 t)^(-1/2) dt",
       worst < mp.mpf(10)**-20, mp.nstr(worst, 3))
report("F30 prefactor: (1/(4 pi)) * rho * 4 K/sqrt(...) = (1/pi) rho K/sqrt(...)", sp.Rational(1, 4) / sp.pi * 4 == 1 / sp.pi)

# ---------------- finding 20: the c = 3/5, l = 2 example ----------------
f2 = sp.Rational(-125460142, 437653125)
report("F20 arithmetic f_2/5 = -125460142/2188265625", f2 / 5 == sp.Rational(-125460142, 2188265625), f2 / 5)
ff = open(os.path.join(LEAD, "FAR_FIELD_ANALYSIS.md")).read().replace("\n", " ")
same = ("-125460142/437653125" in ff and "log coefficient f_2/5" in ff and "c_l = 3/5" in ff
        and "A = 0.42 - 0.23 mu - 0.04 mu^2" in ff and "B = 0.34 + 0.19 mu + 0.13 mu^2" in ff)
report("F20 FAR_FIELD_ANALYSIS.md states the same example (A, B, f_2, f_2/5)", same)

# independent Cartesian recomputation of f_2 (leading field, first correction, cross source)
alpha = sp.Rational(2, 3)
muR = z / Rr
A = sp.Rational(42, 100) - sp.Rational(23, 100) * muR - sp.Rational(4, 100) * muR**2
B = sp.Rational(34, 100) + sp.Rational(19, 100) * muR + sp.Rational(13, 100) * muR**2
phi0 = Rr**(-alpha) * A
q0 = Rr**(-alpha - 1) * B
U0 = [-x * sp.diff(phi0, z) - y * q0, -y * sp.diff(phi0, z) + x * q0, 2 * phi0 + x * sp.diff(phi0, x) + y * sp.diff(phi0, y)]
D1 = [[sp.diff(U0[i], X[j]) for j in range(3)] for i in range(3)]
D2 = [[[sp.diff(D1[i][j], X[k]) for k in range(j, 3)] for j in range(3)] for i in range(3)]


def d2(i, j, k, vals):
    j, k = min(j, k), max(j, k)
    return vals[i][j][k - j]


# Pythagorean points on the unit sphere (y = 0), so all values are exact rationals
pts = []
for m in range(1, 9):
    for n in range(0, 9):
        if m == n or math.gcd(m, n) != 1:
            continue
        mu_v = sp.Rational(m * m - n * n, m * m + n * n)
        x_v = sp.Rational(2 * m * n, m * m + n * n)
        if mu_v not in [p[0] for p in pts]:
            pts.append((mu_v, x_v))
pts = sorted(pts)[:30]
flatU = [e for e in U0] + [e for row in D1 for e in row]
flat2 = [e for row in D2 for col in row for e in col]
def exact_evaluator(exprs):
    """Exact rational evaluation through common subexpressions (lambdify would print rationals as floats)."""
    reps, reduced = sp.cse(exprs)

    def ev(xv, yv, zv):
        env = {x: sp.nsimplify(xv), y: sp.nsimplify(yv), z: sp.nsimplify(zv)}
        for sym, e in reps:
            env[sym] = e.xreplace(env)
        return [r.xreplace(env) for r in reduced]
    return ev


fU = exact_evaluator(flatU + flat2)


def vals_at(mu_v, x_v):
    v = fU(x_v, 0, mu_v)
    u = v[0:3]
    du = [v[3 + 3 * i: 6 + 3 * i] for i in range(3)]
    it = iter(v[12:])
    dd = [[[next(it) for k in range(j, 3)] for j in range(3)] for i in range(3)]
    return u, du, dd


cache = {p: vals_at(*p) for p in pts}
musym = sp.symbols("mu")
g1 = sp.interpolate([(p[0], sum(cache[p][1][i][j] * cache[p][1][j][i] for i in range(3) for j in range(3))) for p in pts], musym)
deg_g1 = sp.degree(g1, musym)
leg = lambda poly, l: sp.Rational(2 * l + 1, 2) * sp.integrate(sp.expand(poly * sp.legendre(l, musym)), (musym, -1, 1))
pexp = 2 * alpha
Qmu = sum(leg(g1, l) / (l * (l + 1) - pexp * (pexp - 1)) * sp.legendre(l, musym) for l in range(deg_g1 + 1))
P1 = Rr**(-pexp) * Qmu.subs(musym, muR)
H1 = exact_evaluator([sp.diff(P1, X[i], X[j]) for i in range(3) for j in range(3)])
# check -Delta P1 = tr(DU0^2) at the sample points (values are exact rationals)
ok_q = all(sp.nsimplify(-(lambda h: h[0] + h[4] + h[8])(H1(p[1], 0, p[0])) - g1.subs(musym, p[0])) == 0 for p in pts)
ok_q = ok_q and all(v.is_Rational for p in pts[:2] for v in H1(p[1], 0, p[0]))
cross = []
for p in pts:
    u, du, dd = cache[p]
    h = H1(p[1], 0, p[0])
    # U1 = (U0.grad)U0 + grad P1, so D_j U1_i = d_j U0_k d_k U0_i + U0_k d_j d_k U0_i + d_i d_j P1
    DU1 = [[sum(du[k][j] * du[i][k] + u[k] * d2(i, j, k, dd) for k in range(3)) + h[3 * i + j] for j in range(3)] for i in range(3)]
    cross.append((p[0], 2 * sum(du[i][j] * DU1[j][i] for i in range(3) for j in range(3))))
g2 = sp.interpolate(cross, musym)
deg_g2 = sp.degree(g2, musym)
f2_cart = leg(g2, 2)
report("F20 Cartesian recomputation: -Delta P1 = tr(DU0^2) for the local pressure R^(-4/3) Q(mu)", ok_q and deg_g1 <= 6, f"deg {deg_g1}")
report("F20 Cartesian recomputation of the resonant quadrupole f_2 = -125460142/437653125",
       f2_cart == f2 and deg_g2 <= len(pts) - 4, f"f_2 = {f2_cart}, source degree {deg_g2}, {len(pts)} points")

# ---------------- added records: full-bandwidth pressure checks and the non-finite stored samples ----------------
rows = []
for f in sorted(glob.glob(os.path.join(VER, "report_audits", "pressure_bandwidth_published_*.json"))):
    rows.append(json.load(open(f))["row"])
four = [r for r in rows if r["stem"] in ("ladder_l2", "t1_seed74_l1", "t1_seed74_l2a", "ladder_l0_followup", "t1_seed74_l2")]
if len(four) == 5:
    last_p = max(r["levels"][-1]["change_from_previous"]["pressure"] for r in four)
    last_g = max(r["levels"][-1]["change_from_previous"]["gradient"] for r in four)
    direct = max(r["fine_direct_pressure_error"] for r in four)
    saved = max(r["saved_sample_max_error"] for r in four)
    above = all(lv["lmax"] >= r["bulk_source_degree_bound"] for r in four for lv in r["levels"])
    degs = sorted({lv["lmax"] for r in four for lv in r["levels"]})
    bounds = sorted({r["bulk_source_degree_bound"] for r in four})
    finite = all(r["saved_sample_finite_count"] == 765 and r["all_765_independent_pressures_and_gradients_finite"] for r in four)
    angular = all(2 * lv["nangle"] - 1 >= r["bulk_source_degree_bound"] + lv["lmax"] for r in four for lv in r["levels"])
    report("Records: five states, last-level changes <= 5e-12 (P) and 1.1e-12 (grad), direct Newton <= 1.4e-8, all levels >= bound, "
           "2n - 1 >= D + L at every level, 765/765 finite stored samples",
           last_p <= 5e-12 and last_g <= 1.1e-12 and direct <= 1.4e-8 and above and angular and finite
           and all(len(r["levels"]) == 3 for r in four),
           f"P {last_p:.3e}, grad {last_g:.3e}, direct {direct:.3e}, stored {saved:.3e}, degrees {degs}, bounds {bounds}")
else:
    report("Records: five full-bandwidth states found", False, len(four))
l3 = [r for r in rows if r["stem"] == "t1_seed74_l3"]
if l3:
    r = l3[0]
    report("Records: export with non-finite stored samples, full-bandwidth check",
           r["bulk_source_degree_bound"] == 88 and r["all_765_independent_pressures_and_gradients_finite"]
           and r["saved_sample_finite_count"] == 714,
           f"bound {r['bulk_source_degree_bound']}, degrees {[lv['lmax'] for lv in r['levels']]}, "
           f"last P {r['levels'][-1]['change_from_previous']['pressure']:.3e}, grad {r['levels'][-1]['change_from_previous']['gradient']:.3e}, "
           f"direct {r['fine_direct_pressure_error']:.3e}, stored {r['saved_sample_max_error']:.3e}")
if os.path.exists(D64):
    zf = np.load(D64)
    P, RR = zf["P"], zf["R"]
    bad = ~np.isfinite(P)
    dist = {f"{v:.6f}": [int(np.isposinf(P[bad & (RR == v)]).sum()), int(np.isneginf(P[bad & (RR == v)]).sum()),
                          int(np.isnan(P[bad & (RR == v)]).sum())] for v in np.unique(RR[bad])}
    report("Records: stored pressures 714 finite, 51 non-finite at three radii (+inf, -inf, NaN counts)",
           int((~bad).sum()) == 714 and len(dist) == 3, dist)
    # consistency only (not a proof of the cause): the non-finite radii are exactly those with (L + 1) log10 R > log10(max)
    lmax_f = math.log10(np.finfo(float).max)
    bad_R = set(np.unique(RR[bad]).tolist())
    Ls = [L for L in range(1, 200) if bad_R == {v for v in np.unique(RR).tolist() if (L + 1) * math.log10(v) > lmax_f}]
    report("Records: non-finite radii coincide with R^(L+1) overflow radii for some degree L (consistency, not cause)",
           len(Ls) > 0, f"L in {Ls[:1]}..{Ls[-1:]}" if Ls else "none")

results["cpu_seconds"] = time.process_time() - t0
with open(os.path.join(HERE, "docrev_P_check_output.json"), "w") as out:
    json.dump(results, out, indent=1)
n_fail = sum(1 for v in results.values() if isinstance(v, dict) and not v["pass"])
print(f"{len(results) - 1} checks, {n_fail} FAIL, cpu {results['cpu_seconds']:.1f} s")
