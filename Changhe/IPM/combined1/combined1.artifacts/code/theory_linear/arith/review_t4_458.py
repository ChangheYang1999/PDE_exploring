"""Independent check of c1-t4 T4-458 (candidate 001 has no stationary correction in its affine L2 class; TEAM_NOTE_v234).

Two routes, neither using the hand formulas (3)-(6) of the proof:
(B) exact Wirtinger calculus. Each leading potential term a r^d cos(n theta) is written as (a/2)(z^A zb^B + z^B zb^A),
    A = (d+n)/2, B = (d-n)/2 (exact rationals), with d/dz z^A zb^B = A z^(A-1) zb^B, d/dzb = B z^A zb^(B-1),
    d/dx = d/dz + d/dzb, d/dy = i(d/dz - d/dzb), X.grad = z d/dz + zb d/dzb. rho = -d_y Delta chi, u = (-chi_xyy, chi_xxy).
    The leading density G_0 (exponent gamma), the leading stream-derived velocity and the residual coefficient E at
    exponent q = 2 gamma - 1 are computed and compared with T4-458's data/leading_coefficients.json and with N4's
    first_nonzero_sector (source/N4_result.json).
(C) direct evaluation. chi is evaluated from the 860 raw generators, chi = sum coef H_m (1+s)^(p_j-m) T(t), t = s/(1+s),
    T = t^h or t^w P_n(2t-1), as a bivariate Taylor polynomial of total degree 4 at (r cos th, r sin th) in Arb (1536
    bits), so all derivatives up to order 4 are exact up to Arb radii. Then F = (c0 x + u1) rho_x + (c0 y + u2) rho_y - rho
    is compared with r^q E(th), rho with r^gamma G_0 and X.grad rho with gamma r^gamma G_0, at r = 10^4, 10^6, 10^8,
    10^10 and 12 angles. The relative deviation should fall like
    r^-delta (delta = 1 - gamma, next sector (2,0)); this is FLOAT evidence for the exact claim F = r^q E + o(r^q), not a
    proof of it.

Run from artifacts/:  python3 -B -u arith/review_t4_458.py
Takes no arguments. Needs python-flint. Reads, read only, in place: ../../c1-t4/research/candidate001_affine_exclusion/
{PROOF.md, source/raw.json (sha256 asserted), data/leading_coefficients.json, source/N4_result.json,
verification/result.json, code/check.py, source/annular_PROOF.md, source/generator_PROOF.md (sha256 recorded)}.
Output: stdout (logs/review_t4_458.log by the README command), data/review_t4_458_results.json.
"""
import hashlib
import json
import math
import sys
import time
from collections import defaultdict
from fractions import Fraction as Fr
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: review_t4_458.py (no arguments)")
t0 = time.time()
HERE = Path(__file__).resolve().parents[1]
D458 = HERE.parent.parent / "c1-t4/research/candidate001_affine_exclusion"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
N_, FAILS = [0], []
OUT = {"inputs": {}}


def check(name, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- (A) inputs
PIN = {"PROOF.md": "771ad6b4af564e1b3a0acf1284184fd8f36c15d2dd090212370122d433789a3e",
       "source/raw.json": "8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7",
       "source/annular_PROOF.md": "ebf243859dc4e104c71f7414a95e9e38001be51ca65efe3e9abcb5e21f0ffcd4"}
for k, h in PIN.items():
    check("(A) sha256 of %s is %s...%s" % (k, h[:8], h[-8:]), sha(D458 / k) == h)
for k in list(PIN) + ["data/leading_coefficients.json", "source/N4_result.json", "verification/result.json",
                      "code/check.py", "source/generator_PROOF.md"]:
    OUT["inputs"]["c1-t4/research/candidate001_affine_exclusion/" + k] = sha(D458 / k)
RAW = json.loads((D458 / "source/raw.json").read_text())
LC = json.loads((D458 / "data/leading_coefficients.json").read_text())
N4 = json.loads((D458 / "source/N4_result.json").read_text())
PR = (D458 / "PROOF.md").read_text()
c0 = Fr(RAW["cl_exact"])
check("(A) c0 = 4076476460239181/2^51", c0 == Fr(4076476460239181, 2**51))
gam = 1 / c0
dlt = 1 - gam
q = 2 * gam - 1
check("(A) 0 < q < gamma < 1, q = 427123167131315/4076476460239181 (PROOF.md)",
      0 < q < gam < 1 and q == Fr(427123167131315, 4076476460239181) and "q=427123167131315/4076476460239181>0" in PR)
check("(A) raw format: 'T = t^h (mono) or t^w P_n(2t-1) (leg); p = (3+gamma-j lambda)/2', and generator_PROOF.md "
      "defines p_j = (3+gamma-j delta)/2 with delta = 1 - gamma",
      "T = t^h (mono) or t^w P_n(2t-1) (leg); p = (3+gamma-j lambda)/2" in RAW["format"]
      and "p_j=(3+gamma-j delta)/2" in (D458 / "source/generator_PROOF.md").read_text())
GEN = RAW["generators"]
okspec = len(GEN) == 860 and all(
    isinstance(g["m"], int) and g["m"] >= 0 and g["j"] in (0, 1, 2, 3)
    and ((g["spec"][0] == "mono" and len(g["spec"]) == 2) or (g["spec"][0] == "leg" and len(g["spec"]) == 3))
    and all(isinstance(x, int) and x >= 0 for x in g["spec"][1:]) for g in GEN)
check("(A) 860 generators, j in 0..3, m >= 0, specs ('mono', h) or ('leg', w, n) with nonnegative integers (no Q, R = 1)",
      okspec)


# Legendre polynomials, exact (Bonnet), as coefficient lists in the variable
def legendre(nmax):
    P = [[Fr(1)], [Fr(0), Fr(1)]]
    for k in range(1, nmax):
        a = [Fr(0)] + [(2 * k + 1) * x for x in P[k]]
        b = [k * x for x in P[k - 1]] + [Fr(0)] * 2
        P.append([(a[i] - b[i]) / (k + 1) for i in range(k + 2)])
    return P


NMAX = max(g["spec"][2] for g in GEN if g["spec"][0] == "leg")
LEG = legendre(NMAX)
check("(A) P_n(1) = 1 for n = 0..%d (own Bonnet recursion), so every T(1) = 1" % NMAX, all(sum(p) == 1 for p in LEG))
check("(A) PROOF.md conventions: 'Rj has symbol i xi_j/|xi|', 'u=(-chi_xyy,chi_xxy)', 'rho=-partial_y Delta chi'",
      all(x in PR for x in ("Rj has symbol i xi_j/|xi|", "u=(-chi_xyy,chi_xxy)", "rho=-partial_y Delta chi")))


# symbol identity: with rho = -d_y Delta chi, U[rho] = (-R1R2 rho, R1^2 rho) has the symbols of (-chi_xyy, chi_xxy).
# Gaussian rationals as pairs; i xi_j / |xi| enters only in pairs, so every symbol below is a Gaussian rational.
def gm(*zs):
    re, im = Fr(1), Fr(0)
    for a, b in zs:
        re, im = re * a - im * b, re * b + im * a
    return re, im


def symbol_ok(x1, x2):
    n2 = x1 * x1 + x2 * x2
    d1, d2 = (Fr(0), x1), (Fr(0), x2)                    # symbols of d_x, d_y
    rho = gm((Fr(-1), Fr(0)), d2, (-n2, Fr(0)))          # -d_y Delta
    U1 = gm((Fr(-1), Fr(0)), d1, d2, (1 / n2, Fr(0)), rho)  # -R1 R2: (i xi1/|xi|)(i xi2/|xi|)
    U2 = gm(d1, d1, (1 / n2, Fr(0)), rho)
    return U1 == gm((Fr(-1), Fr(0)), d1, d2, d2) and U2 == gm(d1, d1, d2)


check("(A) symbol identity U[-d_y Delta chi] = (-chi_xyy, chi_xxy) at xi = (1,2), (-3,5), (7/3,-1/2)",
      all(symbol_ok(Fr(a), Fr(b)) for a, b in ((1, 2), (-3, 5), (Fr(7, 3), Fr(-1, 2)))))

# ---------------------------------------------------------------- (B) exact Wirtinger calculus
# a function is a dict {(A, B): (re, im)} meaning sum (re + i im) z^A zb^B
def cadd(f, key, v):
    re, im = f.get(key, (Fr(0), Fr(0)))
    f[key] = (re + v[0], im + v[1])


def clean(f):
    return {k: v for k, v in f.items() if v[0] or v[1]}


def dz(f):
    g = {}
    for (A, B), (re, im) in f.items():
        if A:
            cadd(g, (A - 1, B), (A * re, A * im))
    return clean(g)


def dzb(f):
    g = {}
    for (A, B), (re, im) in f.items():
        if B:
            cadd(g, (A, B - 1), (B * re, B * im))
    return clean(g)


def add(f, g, s=1):
    h = dict(f)
    for k, v in g.items():
        cadd(h, k, (s * v[0], s * v[1]))
    return clean(h)


def mul_i(f):
    return {k: (-v[1], v[0]) for k, v in f.items()}


def dx(f):
    return add(dz(f), dzb(f))


def dy(f):
    return mul_i(add(dz(f), dzb(f), -1))


def prod(f, g):
    h = {}
    for (A1, B1), (r1, i1) in f.items():
        for (A2, B2), (r2, i2) in g.items():
            cadd(h, (A1 + A2, B1 + B2), (r1 * r2 - i1 * i2, r1 * i2 + i1 * r2))
    return clean(h)


def scal(f, a):
    return {k: (a * v[0], a * v[1]) for k, v in f.items()}


def is_real(f):
    return all(f.get((B, A)) == (v[0], -v[1]) for (A, B), v in f.items())


def to_trig(f, expo):
    """real function sum over (A,B) -> exponent expo (checked) and cos/sin coefficients by frequency."""
    cosc, sinc, ok = defaultdict(Fr), defaultdict(Fr), True
    for (A, B), (re, im) in f.items():
        ok &= (A + B == expo) and (A - B).denominator == 1
        k = int(A - B)
        # (re + i im) e^{ik th} -> real part re cos(k th) - im sin(k th), imaginary part must cancel with the conjugate
        cosc[abs(k)] += re
        sinc[abs(k)] += (-im if k > 0 else im) if k else 0
    return ok, {k: v for k, v in cosc.items() if v}, {k: v for k, v in sinc.items() if v}


Cj = {j: defaultdict(Fr) for j in range(4)}
for g in GEN:
    Cj[g["j"]][2 * g["m"]] += Fr(g["coef"])
lp = LC["leading_potential"]
check("(B) leading potential sums C_j (exact, own summation) equal T4-458 leading_potential for j = 0..3",
      all({str(n): str(v) for n, v in sorted(Cj[j].items()) if v} == lp[str(j)] for j in range(4)))


def chi_lead(j):
    d = 3 + gam - j * dlt
    f = {}
    for n, a in Cj[j].items():
        if a:
            cadd(f, ((d + n) / 2, (d - n) / 2), (a / 2, Fr(0)))
            cadd(f, ((d - n) / 2, (d + n) / 2), (a / 2, Fr(0)))
    return clean(f), d


lap = lambda f: scal(dz(dzb(f)), 4)
dens, strm, vel = {}, {}, {}
for j in (0, 1):
    ch, d = chi_lead(j)
    dens[j] = scal(dy(lap(ch)), -1)
    vel[j] = (scal(dx(dy(dy(ch))), -1), dx(dx(dy(ch))))
    strm[j] = dx(dy(ch))
okt, cc, sc = to_trig(dens[0], gam)
check("(B) rho_0 = -d_y Delta(r^(3+gamma) C_0) is real (conjugate-symmetric), exponent gamma, pure sine series",
      okt and not cc and is_real(dens[0]) and is_real(dens[1]) and is_real(strm[0]))
check("(B) G_0 sine coefficients equal T4-458 density['0'] exactly (%d modes, the lowest %d)" % (len(sc), min(sc)),
      {str(k): str(v) for k, v in sorted(sc.items())} == LC["density"]["0"])
check("(B) G_0 is nonzero", len(sc) > 0)
OUT["G0_modes"] = sorted(sc)
ok1, cc1, sc1 = to_trig(dens[1], q)
check("(B) G_1 (exponent q) equals T4-458 density['1'] exactly", ok1 and not cc1
      and {str(k): str(v) for k, v in sorted(sc1.items())} == LC["density"]["1"])
oks, ccs, scs = to_trig(strm[0], 1 + gam)
check("(B) psi_0 = chi_xy (exponent 1 + gamma) equals T4-458 stream['0'] exactly", oks and not ccs
      and {str(k): str(v) for k, v in sorted(scs.items())} == LC["stream"]["0"])
# u_0 from the potential directly, and the check u = (-psi_y, psi_x)
check("(B) u_0 = (-chi_xyy, chi_xxy) equals (-d_y psi_0, d_x psi_0)",
      vel[0][0] == scal(dy(strm[0]), -1) and vel[0][1] == dx(strm[0]))
# residual at exponent q: (c0 X.grad - 1) rho_1 + u_0 . grad rho_0
Xg = lambda f: clean({k: ((k[0] + k[1]) * v[0], (k[0] + k[1]) * v[1]) for k, v in f.items()})
lin = add(scal(Xg(dens[1]), c0), dens[1], -1)
nl = add(prod(vel[0][0], dx(dens[0])), prod(vel[0][1], dy(dens[0])))
okE, ccE, scE = to_trig(add(lin, nl), q)
lin0 = add(scal(Xg(dens[0]), c0), dens[0], -1)
check("(B) (c0 X.grad - 1) rho_0 = 0 exactly (c0 gamma = 1)", lin0 == {})
check("(B) the exponent-q residual is real, every term has exponent q; no cosine terms",
      okE and not ccE and is_real(add(lin, nl)))
check("(B) E sine coefficients equal T4-458 E10 exactly (modes %s)" % sorted(scE),
      {str(k): str(v) for k, v in sorted(scE.items())} == LC["E10"])
n4 = {int(k): Fr(v) for k, v in N4["first_nonzero_sector"]["sine_coefficients"].items()}
check("(B) E equals N4's first_nonzero_sector sine coefficients exactly; N4 label (h, q) = (1, 0), exponent q",
      {k: v for k, v in n4.items() if v} == dict(scE) and N4["first_nonzero_sector"]["h"] == 1
      and N4["first_nonzero_sector"]["q"] == 0 and Fr(N4["first_nonzero_sector"]["exponent"]) == q)
check("(B) E is nonzero; coefficient at mode 21 nonzero", scE.get(21, 0) != 0)
check("(B) E has no modes below 21 (the refit cancels modes 1..19 exactly)", min(scE) == 21)
E2 = sum(v * v for v in scE.values())
check("(B) sum of squared E coefficients equals T4-458 E10_sum_squares_exact", str(E2) == LC["E10_sum_squares_exact"])
OUT["E_modes"] = sorted(scE)
OUT["E_l2_angular_float"] = math.sqrt(float(E2) * math.pi)
# exponent labels: gamma - H delta - 2K; q <-> (1, 0) only; all other labels with H <= 7 lie strictly below q or vanish
labs = [(H, K) for H in range(8) for K in range(4)]
ex = {L: gam - L[0] * dlt - 2 * L[1] for L in labs}
check("(B) labels (H, K), H <= 7, K <= 3: distinct exponents; only (0, 0) lies above q, only (1, 0) equals q",
      len(set(ex.values())) == len(labs) and [L for L in labs if ex[L] > q] == [(0, 0)]
      and [L for L in labs if ex[L] == q] == [(1, 0)])
check("(B) the largest exponent below q is q - delta (label (2, 0)); gamma - 2 < q - delta",
      max(v for v in ex.values() if v < q) == q - dlt and gam - 2 < q - dlt)

# ---------------------------------------------------------------- (C) direct evaluation at large r (Arb, FLOAT evidence)
ctx.prec = 1536
DEG = 4
IDX = [(i, k) for t in range(DEG + 1) for i in range(t + 1) for k in [t - i]]
POS = {ik: n for n, ik in enumerate(IDX)}
PAIRS = [(POS[a], POS[b], POS[(a[0] + b[0], a[1] + b[1])]) for a in IDX for b in IDX if sum(a) + sum(b) <= DEG]


def smul(f, g):
    h = [arb(0)] * len(IDX)
    for a, b, c in PAIRS:
        h[c] += f[a] * g[b]
    return h


def sadd(f, g, s=1):
    return [x + s * y for x, y in zip(f, g)]


def sconst(v):
    return [arb(v)] + [arb(0)] * (len(IDX) - 1)


def sscal(f, a):
    return [a * x for x in f]


def spow(f, alpha):
    """(f)^alpha for f with positive constant term; alpha an arb."""
    v0 = f[0]
    eps = [arb(0)] + f[1:]
    out, ek, coef = sconst(0), sconst(1), arb(1)
    for k in range(DEG + 1):
        out = sadd(out, sscal(ek, coef * v0 ** (alpha - k)))
        coef = coef * (alpha - k) / (k + 1)
        ek = smul(ek, eps)
    return out


def F_at(r, th):
    x0, y0 = r * th.cos(), r * th.sin()
    X, Y = sconst(x0), sconst(y0)
    X[POS[(1, 0)]], Y[POS[(0, 1)]] = arb(1), arb(1)
    S = sadd(smul(X, X), smul(Y, Y))
    V = sadd(S, sconst(1))
    inv = spow(V, arb(-1))
    T = sadd(sconst(1), inv, -1)                       # t = s/(1+s) = 1 - 1/(1+s)
    Z = sadd(sscal(T, arb(2)), sconst(1), -1)          # 2t - 1
    Tp = [sconst(1)]
    for _ in range(6):
        Tp.append(smul(Tp[-1], T))
    Pn = [sconst(1), Z]
    for k in range(1, NMAX):
        Pn.append(sscal(sadd(sscal(smul(Z, Pn[k]), arb(2 * k + 1)), sscal(Pn[k - 1], arb(k)), -1), arb(1) / (k + 1)))
    # H_m = Re (x + i y)^(2m)
    Hre, Him, Hm = sconst(1), sconst(0), {0: sconst(1)}
    for k in range(1, 2 * 9 + 1):
        Hre, Him = sadd(smul(Hre, X), smul(Him, Y), -1), sadd(smul(Hre, Y), smul(Him, X))
        if k % 2 == 0:
            Hm[k // 2] = Hre
    grp = defaultdict(lambda: sconst(0))
    for g in GEN:
        sp = g["spec"]
        Tf = Tp[sp[1]] if sp[0] == "mono" else smul(Tp[sp[1]], Pn[sp[2]])
        cf = Fr(g["coef"])
        grp[(g["j"], g["m"])] = sadd(grp[(g["j"], g["m"])], sscal(Tf, arb(cf.numerator) / cf.denominator))
    chi = sconst(0)
    for (j, m), tf in grp.items():
        p = (3 + gam - j * dlt) / 2 - m
        chi = sadd(chi, smul(smul(Hm[m], spow(V, arb(p.numerator) / p.denominator)), tf))
    D = lambda i, k: chi[POS[(i, k)]] * math.factorial(i) * math.factorial(k)
    rho = -(D(2, 1) + D(0, 3))
    rx, ry = -(D(3, 1) + D(1, 3)), -(D(2, 2) + D(0, 4))
    u1, u2 = -D(1, 2), D(2, 1)
    c0a = arb(c0.numerator) / c0.denominator
    return (c0a * x0 + u1) * rx + (c0a * y0 + u2) * ry - rho, rho, x0 * rx + y0 * ry


qa = arb(q.numerator) / q.denominator
ga = arb(gam.numerator) / gam.denominator
Ef = lambda th: sum(arb(v.numerator) / v.denominator * (k * th).sin() for k, v in scE.items())
G0f = lambda th: sum(arb(v.numerator) / v.denominator * (k * th).sin() for k, v in sc.items())
THS = [arb(k) / 25 * arb.pi() for k in (1, 2, 3, 5, 7, 9, 11, 13, 14, 17, 19, 23)]
OUT["C"] = []
worst = {}
for e10 in (4, 6, 8, 10):
    r = arb(10) ** e10
    devs, gdevs, xdevs, rad = [], [], [], -1e9
    for th in THS:
        F, rho, xg = F_at(r, th)
        pred = r ** qa * Ef(th)
        devs.append(abs(float(((F - pred) / (r ** qa)).mid())))
        gdevs.append(abs(float(((rho / r ** ga) - G0f(th)).mid())))
        xdevs.append(abs(float(((xg / r ** ga) - ga * G0f(th)).mid())))
        rr = arb(F.rad()) / abs(arb(F.mid()))
        rad = max(rad, float((rr.log() / arb(10).log()).mid()) if rr > 0 else -1e9)
    scale = math.sqrt(float(E2))
    worst[e10] = max(devs) / scale
    OUT["C"].append({"r": "1e%d" % e10, "max_abs_dev_F_over_rq": max(devs), "relative_to_E_coefficient_norm": worst[e10],
                     "max_abs_dev_rho_over_rgamma_minus_G0": max(gdevs),
                     "max_abs_dev_Xgradrho_over_rgamma_minus_gammaG0": max(xdevs),
                     "max_log10_rel_arb_radius_of_F": round(rad, 1)})
    print("    r = 1e%d: max |F/r^q - E| = %.3e (%.3e of the coefficient norm of E); max |rho/r^gamma - G_0| = %.3e; "
          "max |X.grad rho/r^gamma - gamma G_0| = %.3e; log10 Arb relative radius of F <= %.1f"
          % (e10, max(devs), worst[e10], max(gdevs), max(xdevs), rad))
check("(C) FLOAT: Arb radii of F are below 1e-30 relative at every sample point",
      all(row["max_log10_rel_arb_radius_of_F"] < -30 for row in OUT["C"]))
check("(C) FLOAT: rho/r^gamma -> G_0 and X.grad rho/r^gamma -> gamma G_0 (input of (9) for c != c0): deviations "
      "decrease from r = 1e4 to 1e10 and are below 1e-3 at 1e10",
      all(OUT["C"][i + 1][k] < OUT["C"][i][k] for i in range(3) for k in ("max_abs_dev_rho_over_rgamma_minus_G0",
                                                                          "max_abs_dev_Xgradrho_over_rgamma_minus_gammaG0"))
      and OUT["C"][3]["max_abs_dev_rho_over_rgamma_minus_G0"] < 1e-3
      and OUT["C"][3]["max_abs_dev_Xgradrho_over_rgamma_minus_gammaG0"] < 1e-3)
check("(C) FLOAT: |F/r^q - E| relative to the coefficient norm of E is below 0.05 at r = 1e8 and 1e10 and decreases "
      "from r = 1e6 to 1e10", worst[8] < 0.05 and worst[10] < 0.05 and worst[10] < worst[8] < worst[6])
sl = (math.log10(worst[10]) - math.log10(worst[6])) / 4
OUT["C_decay_slope_per_decade"] = sl
check("(C) FLOAT: the deviation decays at %.4f decades per decade of r, within 0.05 of -delta = %.4f (next sector q - delta)"
      % (sl, -float(dlt)), abs(sl + float(dlt)) < 0.05)
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N_[0], FAILS, round(time.time() - t0, 3)
(HERE / "data/review_t4_458_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N_[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)
