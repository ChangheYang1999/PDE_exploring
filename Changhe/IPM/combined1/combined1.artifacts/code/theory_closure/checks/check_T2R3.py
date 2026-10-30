"""Independent check by c1-t1 of c1-t2 T2-R3 (review R1-006 in nonlinear_closure/REVIEWS_v03.md).

Target: c1-t2/notes/T2_T4L2_sharp.md (sha256 46f927a1...), Theorem T2-R3 and the frameworks
FW-T-T4L2-sharp-v1 (w = (2^14, 2^18), s = 1/7744) and FW-T-T4L2-sharpw-v1 (w = (2^15, 2^20), s = 1/5184).

Part A is an exact rational certificate (fractions only, no special functions):
  m1 = sup_(s <= 2^-10) M_1/s <= (sqrt(pi)/2) Gamma((1 - SMAX)/2) <= pi/(2 (1 - SMAX)),
  because Gamma is increasing on [3/2 - SMAX/2, 3/2] (its minimum on (0, inf) is at 1.4616...) so
  Gamma((1 - SMAX)/2) = Gamma((3 - SMAX)/2) / ((1 - SMAX)/2) <= (sqrt(pi)/2) / ((1 - SMAX)/2);
  w1c = ||D omega||_inf = (8 sqrt 5/5) 6^(-3/5), so w1c^10 = 8^10/(5^5 6^6) (rational);
  pi in [333/106, 355/113]; sqrt 2 >= 141421/100000.
  Then the K entries of T2-R2 Proposition 8 (rows 0 to 2, scaled to the weights w), symmetric row sums,
  the Gram minors of G_w(mu), and the closure arithmetic (beta, eta, c_s r/2, slope margin).
Part B: arb cross-check of the same constants (tighter m1 from the Gamma function).
Part C: residual component requirements with outward roundings; conversion constants C_w.
Part D: T4-017 point-test gaps on the two balls (arb), N4 Cartesian witness intervals in data/.
Part E: FLOAT studies: exact PSD threshold mu*(w), continuous weight optimum of the G0 requirement,
  sensitivity to the L2 margin beta_L, and the joint-Gram variant (commutator form subtracted inside
  the Gram matrix instead of the row-sum bound).

Usage (from artifacts/checks):
  OMP_NUM_THREADS=1 python3 -B check_T2R3.py > check_T2R3.out
Needs python-flint, numpy, scipy.
"""
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from flint import arb, ctx
from scipy.linalg import eigh
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
ctx.prec = 200

SMAX = Q(1, 1024)
PI_LO, PI_HI = Q(333, 106), Q(355, 113)
SQRT2_LO = Q(141421, 100000)
assert SQRT2_LO ** 2 < 2
CAPS = dict(C=2, U1=6, U2=24, U3=160, R1=22, R2=32, R3=80, R4=2048)


def w1c_upper():
    """smallest q = n/10^7 with q^10 >= 8^10/(5^5 6^6)"""
    target = Q(8 ** 10, 5 ** 5 * 6 ** 6)
    n = int(1.2209960 * 10 ** 7) - 5
    while Q(n, 10 ** 7) ** 10 < target:
        n += 1
    return Q(n, 10 ** 7)


def constants_rational():
    m1 = PI_HI / (2 * (1 - SMAX))
    w1c = w1c_upper()
    return dict(m1=m1, w1c=w1c, k1u=m1, k1w=m1 + Q(8, 5), cru=Q(3, 2) * m1, crw=Q(3, 2) * m1 + Q(32, 15),
                c8=1 + w1c * 3 * PI_HI / 4, dtop=1 + w1c * PI_HI / 2)


def constants_arb():
    pi = arb.pi()
    m1 = pi.sqrt() / 2 * ((1 - arb(1) / 1024) / 2).gamma()
    w1c = 8 * arb(5).sqrt() / 5 * arb(6) ** (arb(-3) / 5)
    return dict(m1=m1, w1c=w1c, k1u=m1, k1w=m1 + arb(8) / 5, cru=arb(3) / 2 * m1, crw=arb(3) / 2 * m1 + arb(32) / 15,
                c8=1 + w1c * 3 * pi / 4, dtop=1 + w1c * pi / 2)


def K_entries(k, inv_sqrt_w1, inv_sqrt_w2, sqrt_w1_over_w2):
    """T2-R2 Proposition 8 rows 0..2 in the scaled components (P, sqrt(w1) a, sqrt(w2) b); caps (D)."""
    C, U1, U2, U3, R1, R2, R3, R4 = (CAPS[x] for x in ("C", "U1", "U2", "U3", "R1", "R2", "R3", "R4"))
    K = {}
    K[0, 0] = k["dtop"] * C + k["c8"] * U1 + (k["crw"] + 2 * k["k1w"]) * U2 + k["k1w"] * R2
    K[0, 1] = k["k1w"] * (U3 + 2 * R3) * inv_sqrt_w1
    K[0, 2] = k["k1w"] * R4 * inv_sqrt_w2
    K[1, 1] = C + U1 + (k["cru"] + k["k1u"]) * U2 + k["k1u"] * R2
    K[1, 2] = k["k1u"] * R3 * sqrt_w1_over_w2
    K[2, 2] = C + U1 + k["cru"] * U2 + k["k1u"] * R2
    return K


def row_sums(K):
    rs = []
    for i in range(3):
        t = K[i, i]
        for j in range(3):
            if j != i:
                t = t + (K.get((i, j), 0) + K.get((j, i), 0)) / 2
        rs.append(t)
    return rs


def gram(w1, w2, mu):
    return [[Q(1, 2) - mu, Q(-347, 10), Q(-5)],
            [Q(-347, 10), w1 * (Q(9, 10) - mu) - 40, -3 * w1],
            [Q(-5), -3 * w1, w2 * (2 - mu)]]


def minors(G):
    d1 = G[0][0]
    d2 = G[0][0] * G[1][1] - G[0][1] ** 2
    d3 = (G[0][0] * (G[1][1] * G[2][2] - G[1][2] * G[2][1]) - G[0][1] * (G[1][0] * G[2][2] - G[1][2] * G[2][0])
          + G[0][2] * (G[1][0] * G[2][1] - G[1][1] * G[2][0]))
    return d1, d2, d3


def pd(w1, w2, mu):
    return all(m > 0 for m in minors(gram(w1, w2, mu)))


def fmt(q, n=10):
    return f"{float(q):.{n}g}"


def ceil_sig(x, n):
    """outward (upward) decimal rounding of a positive Fraction to n significant digits"""
    e = math.floor(math.log10(float(x)))
    scale = Q(10) ** (n - 1 - e)
    v = x * scale
    c = v.numerator // v.denominator + (0 if v.denominator == 1 or v.numerator % v.denominator == 0 else 1)
    return Q(c) / scale


def floor_sig(x, n):
    e = math.floor(math.log10(float(x)))
    scale = Q(10) ** (n - 1 - e)
    v = x * scale
    return Q(v.numerator // v.denominator) / scale


print("=" * 100)
print("Part A. Exact rational certificate")
print("=" * 100)
kr = constants_rational()
print("rational upper bounds: m1 <= pi_hi/(2(1-SMAX)) =", fmt(kr["m1"], 12), "; w1c <=", fmt(kr["w1c"], 12),
      "(w1c^10 >= 8^10/(5^5 6^6) checked)")
for name in ("k1u", "k1w", "cru", "crw", "c8", "dtop"):
    print(f"  {name:>5} <= {fmt(kr[name], 12)}")
assert kr["w1c"] * kr["m1"] < Q(192, 100)
print("  w1c m1 <=", fmt(kr["w1c"] * kr["m1"], 12), "< 1.92")

FRAMEWORKS = [
    dict(name="FW-T-T4L2-sharp-v1", w1=Q(2 ** 14), w2=Q(2 ** 18), mu0=Q(259, 1000), mu_fail=Q(13, 50), Cp=401,
         s=Q(1, 7744), sqrt_s=Q(1, 88), r=Q(147, 200000), beta_lb=Q(1037, 10000), eta=Q(76219, 10 ** 9),
         inv_sqrt_w1=Q(1, 128), inv_sqrt_w2=Q(1, 512), sqrt_w1_over_w2=Q(1, 4), cs_r_half_claim=Q(912295, 10 ** 8),
         slope_claim=Q(6817, 10000)),
    dict(name="FW-T-T4L2-sharpw-v1", w1=Q(2 ** 15), w2=Q(2 ** 20), mu0=Q(97, 250), mu_fail=Q(389, 1000), Cp=397,
         s=Q(1, 5184), sqrt_s=Q(1, 72), r=Q(1351, 10 ** 6), beta_lb=Q(1557, 10000), eta=Q(4207, 2 * 10 ** 7),
         inv_sqrt_w1=1 / (128 * SQRT2_LO), inv_sqrt_w2=Q(1, 1024), sqrt_w1_over_w2=1 / (4 * SQRT2_LO),
         cs_r_half_claim=Q(137200, 10 ** 7), slope_claim=Q(6725, 10000)),
]

print()
print("T4-019 base Gram (weights 2^14, 2^18, mu = 1/4): leading minors",
      [str(m) for m in minors(gram(Q(2 ** 14), Q(2 ** 18), Q(1, 4)))], "(T4-019: 1/4, 144831/100, 1077858728/25)")
assert minors(gram(Q(2 ** 14), Q(2 ** 18), Q(1, 4))) == (Q(1, 4), Q(144831, 100), Q(1077858728, 25))

# reproduce the T2-R2 rows at (128, 512) for orientation (row 2 here has no H entry)
K0 = K_entries(kr, Q(1, 128), Q(1, 512), Q(1, 4))
print("T2-R2 weights (2^14, 2^18), rational K entries:", {f"K{i}{j}": fmt(v, 8) for (i, j), v in K0.items()})

for fw in FRAMEWORKS:
    print()
    print("-" * 100)
    print(fw["name"], f"w = ({fw['w1']}, {fw['w2']}), s = {fw['s']}, r = {fw['r']}, eta = {fw['eta']}")
    w1, w2, s, r = fw["w1"], fw["w2"], fw["s"], fw["r"]
    assert w1 >= 2 and w2 >= 1 and 0 < s <= SMAX and fw["sqrt_s"] ** 2 == s
    # Gram
    m_ok = minors(gram(w1, w2, fw["mu0"]))
    m_fail = minors(gram(w1, w2, fw["mu_fail"]))
    m_next = minors(gram(w1, w2, fw["mu0"] + Q(1, 1000)))
    print("  Gram leading minors at mu0 =", fw["mu0"], ":", [fmt(m, 8) for m in m_ok], "-> PD" if all(x > 0 for x in m_ok) else "-> NOT PD")
    print("  Gram leading minors at mu0 + 1/1000 =", fw["mu0"] + Q(1, 1000), ":", [fmt(m, 8) for m in m_next])
    print("  Gram leading minors at stated failing value", fw["mu_fail"], ":", [fmt(m, 8) for m in m_fail])
    assert all(x > 0 for x in m_ok)
    # exact threshold bracket by bisection on PD
    lo, hi = fw["mu0"], Q(1, 2)
    for _ in range(40):
        mid = (lo + hi) / 2
        if pd(w1, w2, mid):
            lo = mid
        else:
            hi = mid
    print(f"  PD threshold bracket: mu* in [{float(lo):.10f}, {float(hi):.10f}]")
    fw["mu_star"] = lo
    # commutator constant
    K = K_entries(kr, fw["inv_sqrt_w1"], fw["inv_sqrt_w2"], fw["sqrt_w1_over_w2"])
    rs = row_sums(K)
    print("  K entries (rational upper bounds):", {f"K{i}{j}": fmt(v, 8) for (i, j), v in K.items()})
    print("  symmetric row sums <=", [fmt(x, 10) for x in rs], "; claimed C' =", fw["Cp"])
    assert max(rs) <= fw["Cp"]
    print("  max row sum <= C':", max(rs) <= fw["Cp"], f"(slack {float(fw['Cp'] - max(rs)):.6f})")
    # closure arithmetic
    base = fw["mu0"] - fw["Cp"] * s
    beta = base - Q(8, 5) * r / fw["sqrt_s"]
    print("  mu0 - C' s =", base, "=", fmt(base, 10), "; beta = mu0 - C's - (8/5) r/sqrt(s) =", beta, "=", fmt(beta, 10))
    assert beta >= fw["beta_lb"]
    print("  beta >= stated lower bound", fw["beta_lb"], ": True; K_H = 1/beta_lb =", fmt(1 / fw["beta_lb"], 8))
    assert fw["eta"] <= fw["beta_lb"] * r
    print("  eta <= beta_lb r :", fw["eta"] <= fw["beta_lb"] * r, f"({fmt(fw['eta'], 8)} <= {fmt(fw['beta_lb'] * r, 8)});",
          "max admissible eta at this r =", fmt(beta * r, 10))
    # c_s r / 2 <= claim  <=>  r^2/(16 pi s (1+s)) <= claim^2  (use pi_lo)
    lhs = r * r / (16 * PI_LO * s * (1 + s))
    assert lhs <= fw["cs_r_half_claim"] ** 2
    print("  c_s r/2 <=", fmt(fw["cs_r_half_claim"], 8), ": True (exact, pi >= 333/106)")
    # slope: 7/10 - c_s r >= claim  <=>  c_s r <= 7/10 - claim
    t = Q(7, 10) - fw["slope_claim"]
    assert r * r / (4 * PI_LO * s * (1 + s)) <= t * t
    print("  slope margin 7/10 - c_s r >=", fmt(fw["slope_claim"], 6), ": True")
    fw["beta"] = beta

print()
print("=" * 100)
print("Part B. arb cross-check of the constants and row sums (200 bits)")
print("=" * 100)
ka = constants_arb()
for name in ("m1", "w1c", "k1u", "k1w", "cru", "crw", "c8", "dtop"):
    print(f"  {name:>5} in {ka[name].str(12, radius=False)}  (upper {ka[name].upper().str(12, radius=False)})")
for fw in FRAMEWORKS:
    w1, w2 = int(fw["w1"]), int(fw["w2"])
    K = K_entries(ka, 1 / arb(w1).sqrt(), 1 / arb(w2).sqrt(), (arb(w1) / w2).sqrt())
    rs = row_sums(K)
    print(f"  {fw['name']}: row sums upper", [x.upper().str(10, radius=False) for x in rs])
    assert all(x.upper() < fw["Cp"] for x in rs)

print()
print("=" * 100)
print("Part C. Residual component requirements and conversion constants")
print("=" * 100)
print("Necessary conditions from X_{s,w}(F) <= eta; 'outward' = rounded up (safe for a necessary bound),")
print("'inward' = rounded down (safe for a sufficient target).")
for fw in FRAMEWORKS:
    eta, s, w1, w2 = fw["eta"], fw["s"], fw["w1"], fw["w2"]
    print(" ", fw["name"])
    G0 = eta / (512 if w2 == 2 ** 18 else 1024)
    if w1 == 2 ** 14:
        G1_lo = G1_hi = eta / 128
    else:
        # eta / sqrt(2^15) = eta/(128 sqrt 2); bracket with sqrt 2 in [1.41421, 1.41422]
        G1_lo, G1_hi = eta / (128 * Q(141422, 100000)), eta / (128 * SQRT2_LO)
    P2raw = eta / (1 - kr["w1c"] * kr["m1"] * s)
    P2raw192 = eta / (1 - Q(192, 100) * s)
    print(f"    P(J^s F) <= eta = {fw['eta']} = {float(eta):.10e}")
    print(f"    G1(J^s F) <= eta/sqrt(w1) in [{float(G1_lo):.10e}, {float(G1_hi):.10e}]; outward 5 sig: {float(ceil_sig(G1_hi, 5)):.4e}; inward: {float(floor_sig(G1_lo, 5)):.4e}")
    print(f"    G0(J^s F) <= eta/sqrt(w2) = {G0} = {float(G0):.10e}; outward 5 sig: {float(ceil_sig(G0, 5)):.4e}; inward: {float(floor_sig(G0, 5)):.4e}")
    print(f"    raw P2(F) <= eta/(1 - w1c m1 s) <= eta/(1 - 1.92 s) = {float(P2raw192):.10e} (with w1c m1 bound: {float(P2raw):.10e});"
          f" outward 5 sig: {float(ceil_sig(P2raw192, 5)):.4e}")
    Cw = max(1 + Q(32, 25) + w1, 1 + w2 / w1, Q(1))
    print(f"    conversion constant C_w = max(1 + 32/25 + w1, 1 + w2/w1) = {fmt(Cw, 10)}; C_w^(s/2) = {math.exp(math.log(float(Cw)) * float(s) / 2):.7f};"
          f" 1.92 s = {float(Q(192, 100) * s):.4e}")

print()
print("T4-019 (FW-T-T4L2-v1) list for comparison: eta = 1/163840 =", f"{1 / 163840:.10e}", "; eta/128 =", f"{1 / 163840 / 128:.10e}",
      "; eta/512 =", f"{1 / 163840 / 512:.10e}")

print()
print("=" * 100)
print("Part D. T4-017 point-test gaps on the two balls (arb), witness intervals data/N4_cartesian_witnesses.json")
print("=" * 100)
data = json.loads((HERE / "data" / "N4_cartesian_witnesses.json").read_text())
PI = arb.pi()
for fw in FRAMEWORKS:
    sa = arb(fw["s"].numerator) / fw["s"].denominator
    ra = arb(fw["r"].numerator) / fw["r"].denominator
    C0 = 1 / (4 * PI * (1 + sa)).sqrt()
    C1s = 1 / (16 * PI * sa * (1 + sa)).sqrt()
    print(f"  {fw['name']}: C1s r = {(C1s * ra).str(10)}, C0 r = {(C0 * ra).str(10)}")
    for row in data["rows"]:
        fl = row["fields"]
        F, V, Gd = arb(fl["residual"]), arb(fl["velocity_norm"]), arb(fl["gradient_norm"])
        g = abs(F) - ((C1s * V + C0 * (1 + Gd)) * ra + C0 * C1s * ra * ra)
        print(f"    {row['candidate']:>12} {row['point']}: gap {g.str(8)}  excluded: {g > 0}")

print()
print("=" * 100)
print("Part E. FLOAT studies (not part of the certificate)")
print("=" * 100)
kf = {k: float(v.mid()) for k, v in ka.items()}


def Kf(w1, w2):
    K = K_entries(kf, 1 / math.sqrt(w1), 1 / math.sqrt(w2), math.sqrt(w1 / w2))
    return K, max(row_sums(K))


def mu_star(w1, w2, betaL=2.0):
    G0 = np.array([[0.5, -34.7, -5.0], [-34.7, 0.9 * w1 - 40, -3 * w1], [-5.0, -3 * w1, betaL * w2]])
    D = np.diag([1.0, w1, w2])
    return float(eigh(G0, D, eigvals_only=True)[0])


def eta_opt(w1, w2, betaL=2.0):
    mu = mu_star(w1, w2, betaL)
    if mu <= 0:
        return 0.0, mu, 0.0, 0.0
    _, Cp = Kf(w1, w2)
    s = min(mu / (5 * Cp), 1 / 1024)
    base = mu - Cp * s
    eta = base ** 2 * math.sqrt(s) / 6.4
    return eta, mu, Cp, s


for fw in FRAMEWORKS:
    w1, w2 = float(fw["w1"]), float(fw["w2"])
    eta, mu, Cp, s = eta_opt(w1, w2)
    print(f"  {fw['name']}: mu*(w) = {mu:.8f} (bisection bracket {float(fw['mu_star']):.8f}); row-sum C' = {Cp:.5f};"
          f" continuous optimum s = mu/(5C') = 1/{1 / s:.1f}, eta = {eta:.6e}, G0 = {eta / math.sqrt(w2):.6e}")


def negG0(x, betaL=2.0):
    w1, w2 = 2.0 ** x[0], 2.0 ** x[1]
    if w1 < 2 or w2 < 1:
        return 0.0
    eta, *_ = eta_opt(w1, w2, betaL)
    return -eta / math.sqrt(w2)


def negEta(x):
    w1, w2 = 2.0 ** x[0], 2.0 ** x[1]
    if w1 < 2 or w2 < 1:
        return 0.0
    return -eta_opt(w1, w2)[0]


for betaL in (2.0, 2.5, 3.0, 4.0):
    best = None
    for x0 in ([15.0, 20.0], [14.0, 18.0], [16.0, 21.0], [12.0, 16.0]):
        res = minimize(negG0, x0, args=(betaL,), method="Nelder-Mead", options=dict(xatol=1e-6, fatol=1e-16, maxiter=4000))
        if best is None or res.fun < best.fun:
            best = res
    w1, w2 = 2.0 ** best.x[0], 2.0 ** best.x[1]
    eta, mu, Cp, s = eta_opt(w1, w2, betaL)
    print(f"  best G0 requirement, beta_L = {betaL}: {-best.fun:.5e} at log2 w = ({best.x[0]:.3f}, {best.x[1]:.3f}), eta = {eta:.4e},"
          f" mu* = {mu:.4f}, C' = {Cp:.2f}, s = 1/{1 / s:.0f}")
best = None
for x0 in ([20.0, 26.0], [18.0, 24.0], [22.0, 28.0]):
    res = minimize(negEta, x0, method="Nelder-Mead", options=dict(xatol=1e-6, fatol=1e-16, maxiter=4000))
    if best is None or res.fun < best.fun:
        best = res
print(f"  largest eta over weights: {-best.fun:.4e} at log2 w = ({best.x[0]:.2f}, {best.x[1]:.2f}); G0 there = "
      f"{-best.fun / 2 ** (best.x[1] / 2):.3e}")

# joint Gram: replace (mu0 - C' s) by the largest mu with G_w(mu) - s Ksym (raw components) PSD
print()
print("  joint-Gram variant (FLOAT): largest m with G_w(0) - s Ksym_raw - m diag(1, w1, w2) PSD, compared with mu*(w) - C's")
for fw in FRAMEWORKS:
    w1, w2, s = float(fw["w1"]), float(fw["w2"]), float(fw["s"])
    K, Cp = Kf(w1, w2)
    S = np.zeros((3, 3))
    for (i, j), v in K.items():
        S[i, j] += v / 2
        S[j, i] += v / 2
    Dh = np.diag([1.0, math.sqrt(w1), math.sqrt(w2)])
    Sraw = Dh @ S @ Dh
    G0m = np.array([[0.5, -34.7, -5.0], [-34.7, 0.9 * w1 - 40, -3 * w1], [-5.0, -3 * w1, 2.0 * w2]])
    m_joint = float(eigh(G0m - s * Sraw, np.diag([1.0, w1, w2]), eigvals_only=True)[0])
    lam = float(np.linalg.eigvalsh(S)[-1])
    print(f"    {fw['name']}: mu* - C's = {mu_star(w1, w2) - Cp * s:.6f}; mu* - lambda_max(Ksym) s = {mu_star(w1, w2) - lam * s:.6f}"
          f" (lambda_max = {lam:.3f}); joint = {m_joint:.6f}")
