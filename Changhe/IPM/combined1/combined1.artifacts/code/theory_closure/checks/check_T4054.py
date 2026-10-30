"""Independent check by c1-t1 of c1-t4 T4-054 (review R1-010 in nonlinear_closure/REVIEWS_v06.md).

Target: c1-t4/research/sharp_weighted_velocity/PROOF.md (sha256 5c3bdfe1...), the sharp odd Beurling bound
||w B w^-1|| = (2+a)/(2-a) on complex centrally odd L2, w_R = (1 + |x|^2/R^2)^(-a/2), 0 < a < 2, and the
velocity bound ||w U[h]|| <= 2/(2-a) ||w h|| for real odd h.

Part A (sympy, exact; my own code written from the statements of the target):
  A1. general-n polar blocks: (d_x + i d_y)(g e^{i n th}) and (d_x - i d_y)(g e^{i n th}), the endpoint choices,
      the t-line form (3), and explicit d-bar solves for z^5 e^{-r^2} (n = 4) and conj(z)^3 e^{-r^2} (n = -4).
  A2. the weighted ODEs (5) and (6) from the integral definitions, for a generic weight.
  A3. the integrated identities (7), (8), (9), (10) in terms of the independent quantities ||H'||^2,
      Re<H',H> (= 0), Re<H', p H> (arbitrary) and int p^j |H|^2; Young constants 1/(n-a), 1/k.
  A4. p(t) for w_R, K_n decreasing, central oddness -> n even, (1 + K_2)/2 = 2/(2-a), the n = 1 even-sector
      constant, and the symbol identity U2 + i U1 = -(I + B)/2.
Part B (FLOAT, not proofs):
  B1. discretized weighted future block applied to random inputs with p from w_R: residual of (9) and the
      sign of K^2||F||^2 - ||G||^2; past block contraction.
  B2. the sharpness packets of section 4: ratio ||G_L||/||F_L|| and agreement of the forward integral with H_L.
  B3. new: the velocity constant on real S1 inputs (h = sum_{m odd} g_m(r) sin(m theta)). Far-field multiplier
      constant sup_tau ||M(tau)||/sqrt 8 and a discretized full weighted operator, both against 2/(2-a).
Part C (exact rationals; new, rigorous given the block bounds of T4-054): on real S1 inputs,
  ||w U[h]|| <= sqrt(rho/8) ||w h||, where rho bounds the norm of the infinite tridiagonal matrix A^T A built from
  ||future block n|| <= K_n and ||past block|| <= 1; rho is certified by a Collatz-Wielandt (Schur) test with a
  rational positive vector, exactly for a in {6/5, 13/10, 7/5, 3/2, 19/10}.

Usage (from artifacts/checks):
  OMP_NUM_THREADS=1 python3 -B check_T4054.py > check_T4054.out
Needs sympy, numpy, scipy.
"""
import math
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from scipy.sparse.linalg import LinearOperator, svds

print("=" * 100)
print("Part A. Exact symbolic checks")
print("=" * 100)
r, s, v, t, tau = sp.symbols("r s v t tau", positive=True)
th = sp.symbols("theta", real=True)
n = sp.symbols("n", integer=True)
gf = sp.Function("g")
# A1. polar forms: d_x + i d_y = e^{i th}(d_r + (i/r) d_th), d_x - i d_y = e^{-i th}(d_r - (i/r) d_th)
X, Y = sp.symbols("X Y", real=True)
G_ = gf(r) * sp.exp(sp.I * n * th)
plus = sp.exp(sp.I * th) * (sp.diff(G_, r) + sp.I / r * sp.diff(G_, th))
minus = sp.exp(-sp.I * th) * (sp.diff(G_, r) - sp.I / r * sp.diff(G_, th))
chk_p = sp.simplify(plus - sp.exp(sp.I * (n + 1) * th) * (sp.diff(gf(r), r) - n * gf(r) / r))
chk_m = sp.simplify(minus - sp.exp(sp.I * (n - 1) * th) * (sp.diff(gf(r), r) + n * gf(r) / r))
print("A1. (d_x + i d_y)(g e^{in th}) = e^{i(n+1)th}(g' - n g/r):", chk_p == 0,
      "; (d_x - i d_y)(g e^{in th}) = e^{i(n-1)th}(g' + n g/r):", chk_m == 0)
assert chk_p == 0 and chk_m == 0
print("    so with m = n + 1: g' - n g/r = f_m and (B f)_{m-2} = g' + n g/r = f_m + 2 n g/r")
# t-line form: F(t) = r f_m(r), r = e^t; n > 0: g = -r^n int_r^oo s^-n f_m ds; n < 0: g = r^n int_0^r s^-n f_m ds
Ff = sp.Function("F")
nn = sp.symbols("nn", positive=True)
# substitution s = e^(t+v) (n > 0) and s = e^(t-v) (n < 0); f_m(s) = F(log s)/s, ds = s dv
integrand_pos = sp.exp(nn * t) * sp.exp(-nn * (t + v)) * Ff(t + v) / sp.exp(t + v) * sp.exp(t + v)
integrand_neg = sp.exp(-nn * t) * sp.exp(nn * (t - v)) * Ff(t - v) / sp.exp(t - v) * sp.exp(t - v)
print("    n > 0: r^n s^-n f_m(s) ds =", sp.simplify(integrand_pos), "dv ;  n = -nn < 0:", sp.simplify(integrand_neg), "dv")
print("    hence G = r (B f)_{m-2} = F + 2 n g = F - 2n int_0^oo e^{-nv} F(t+v) dv (n > 0),"
      " F + 2n int_0^oo e^{nv} F(t-v) dv (n < 0): equation (3)")
assert sp.simplify(integrand_pos - sp.exp(-nn * v) * Ff(t + v)) == 0
assert sp.simplify(integrand_neg - sp.exp(-nn * v) * Ff(t - v)) == 0
# explicit d-bar solves
x1, x2 = sp.symbols("x1 x2", real=True)
z, zb, R2 = x1 + sp.I * x2, x1 - sp.I * x2, x1 ** 2 + x2 ** 2
for name, f, g_dir, mm in (("z^5 e^{-r^2}  (m = 5, n = 4) ", z ** 5 * sp.exp(-R2), -z ** 4 * sp.exp(-R2) / 2, 5),):
    res = sp.simplify(sp.diff(g_dir, x1) + sp.I * sp.diff(g_dir, x2) - f)
    out = sp.simplify(sp.diff(g_dir, x1) - sp.I * sp.diff(g_dir, x2))
    nv = mm - 1
    fm = r ** mm * sp.exp(-r ** 2)
    g_rad = -r ** nv * sp.integrate(s ** (-nv) * fm.subs(r, s), (s, r, sp.oo))
    out_rad = sp.simplify(fm + 2 * nv * g_rad / r)
    print(f"    {name}: d-bar residual {res}; direct output {sp.factor(out)}; radial formula (m-2 coefficient) {sp.factor(out_rad)}")
    assert res == 0 and sp.simplify(out_rad - r ** 3 * (r ** 2 - 4) * sp.exp(-r ** 2)) == 0
    assert sp.simplify(out - z ** 3 * (R2 - 4) * sp.exp(-R2)) == 0
# n = -4: f = conj(z)^3 e^{-r^2}, m = -3; g = r^-4 int_0^r s^4 f_m(s) ds with f_m = r^3 e^{-r^2}; check by the polar operators
fm = r ** 3 * sp.exp(-r ** 2)
g_rad = r ** (-4) * sp.integrate(s ** 4 * fm.subs(r, s), (s, 0, r))
res_rad = sp.simplify(sp.diff(g_rad, r) + 4 * g_rad / r - fm)       # g' - n g/r with n = -4
out_rad = sp.simplify(fm - 8 * g_rad / r)
print("    conj(z)^3 e^{-r^2} (m = -3, n = -4): radial ODE residual", res_rad, "; g regular at 0:",
      sp.limit(g_rad, r, 0) == 0, "; output (mode -5 coefficient)", sp.simplify(out_rad))
assert res_rad == 0

# A2. weighted ODEs: H(t) = w(t) int_t^oo e^{-n(T-t)} F(T)/w(T) dT ; H' = (n - p) H - F with p = -(log w)'
T = sp.symbols("T", real=True)
wf = sp.Function("w", positive=True)
tt = sp.symbols("tt", real=True)
Hfut = wf(tt) * sp.Integral(sp.exp(-nn * (T - tt)) * Ff(T) / wf(T), (T, tt, sp.oo))
pw = -sp.diff(sp.log(wf(tt)), tt)
ode_f = sp.simplify(sp.diff(Hfut, tt) - ((nn - pw) * Hfut - Ff(tt)))
kk = sp.symbols("k", positive=True)
Hpast = wf(tt) * sp.Integral(sp.exp(-kk * (tt - T)) * Ff(T) / wf(T), (T, -sp.oo, tt))
ode_p = sp.simplify(sp.diff(Hpast, tt) - (Ff(tt) - (kk + pw) * Hpast))
print("A2. future: H' - ((n - p) H - F) =", sp.simplify(ode_f.doit()), "; past: H' - (F - (k + p) H) =", sp.simplify(ode_p.doit()))
assert sp.simplify(ode_f.doit()) == 0 and sp.simplify(ode_p.doit()) == 0
print("    then G = F - 2nH = -H' - (n+p)H (future) and G = F - 2kH = H' - (k-p)H (past), as in (5), (6)")
print("    Young: kernels <= e^{-(n-a)v} and e^{-kv}; int_0^oo e^{-(n-a)v} dv =",
      sp.integrate(sp.exp(-(nn - sp.Symbol('a', positive=True)) * v), (v, 0, sp.oo), conds="none"))

# A3. integrated identities with independent quantities
#   Xd = ||H'||^2, Y = Re<H',H> (= 0 for H in H^1), Z = Re<H', p H> (arbitrary), I0, I1, I2 = int p^j |H|^2
a, nq, k = sp.symbols("a n k", positive=True)
Xd, Y, Z, I0, I1, I2 = sp.symbols("Xd Y Z I0 I1 I2", real=True)


def sq(c_d, c_0, c_p):
    """|| c_d H' + (c_0 + c_p p) H ||^2 with real constants c_d, c_0, c_p"""
    return (c_d ** 2 * Xd + 2 * c_d * c_0 * Y + 2 * c_d * c_p * Z + c_0 ** 2 * I0 + 2 * c_0 * c_p * I1
            + c_p ** 2 * I2)


Fn = sq(-1, nq, -1)          # F = -H' + (n - p) H
Gn = sq(-1, -nq, -1)         # G = -H' - (n + p) H
Dn = sq(-1, a, -1)           # D = -H' + (a - p) H
id7 = sp.expand(Gn - Fn - 4 * nq * I1)
id8 = sp.expand(Fn - Dn - (nq - a) * ((nq + a) * I0 - 2 * I1))
Kn = (nq + a) / (nq - a)
id9 = sp.simplify(Kn ** 2 * Fn - Gn - 4 * nq * a / (nq - a) ** 2 * (Dn + (nq ** 2 - a ** 2) / a * (a * I0 - I1)))
print("A3. (7) G^2 - F^2 - 4n int p|H|^2 =", sp.factor(id7), "(a multiple of Re<H',H> = 0)")
print("    (8) F^2 - D^2 - (n-a) int (n+a-2p)|H|^2 =", sp.factor(id8))
print("    (9) K^2 F^2 - G^2 - 4na/(n-a)^2 [D^2 + ((n^2-a^2)/a) int (a-p)|H|^2] =", sp.factor(id9))
assert sp.simplify(id7.subs(Y, 0)) == 0 and sp.simplify(id8.subs(Y, 0)) == 0 and sp.simplify(id9.subs(Y, 0)) == 0
assert not id9.has(Z) and not id7.has(Z) and not id8.has(Z)
Fk = sq(1, k, 1)             # F = H' + (k + p) H
Gk = sq(1, -k, 1)            # G = H' - (k - p) H
id10 = sp.expand(Fk - Gk - 4 * k * I1)
print("    (10) F^2 - G^2 - 4k int p|H|^2 =", sp.factor(id10), "; Re<H', pH> (Z) cancels in all four identities")
assert sp.simplify(id10.subs(Y, 0)) == 0 and not id10.has(Z)
# Re<H',H> = 0 on H^1(R): (|H|^2)' = 2 Re(H' conj H) and |H|^2 in W^{1,1}(R) integrates to 0 (standard)

# A4. small facts
tq, Rq = sp.symbols("t R", positive=True)
p_wR = sp.simplify(-sp.diff(sp.log((1 + sp.exp(2 * tq) / Rq ** 2) ** (-a / 2)), tq))
print("A4. p(t) for w_R =", p_wR, "; equal to a e^{2t}/(R^2 + e^{2t}):",
      sp.simplify(p_wR - a * sp.exp(2 * tq) / (Rq ** 2 + sp.exp(2 * tq))) == 0, "(in [0, a))")
assert sp.simplify(p_wR - a * sp.exp(2 * tq) / (Rq ** 2 + sp.exp(2 * tq))) == 0
print("    dK_n/dn =", sp.factor(sp.diff(Kn, nq)), "< 0; central oddness: e^{i m pi} = -1 iff m odd, so n = m - 1 even;"
      " future n >= 2 > a")
print("    (1 + (2+a)/(2-a))/2 =", sp.simplify((1 + (2 + a) / (2 - a)) / 2), "; even sector n = 1: K_1 = (1+a)/(1-a), needs a < 1")
x1s, x2s = sp.symbols("xi1 xi2", real=True)
q2 = x1s ** 2 + x2s ** 2
sU1 = x1s * x2s / q2
sU2 = -x1s ** 2 / q2
sB = (x1s - sp.I * x2s) ** 2 / q2
print("    symbol U2 + i U1 + (1 + B)/2 =", sp.simplify(sU2 + sp.I * sU1 + (1 + sB) / 2))
assert sp.simplify(sU2 + sp.I * sU1 + (1 + sB) / 2) == 0
print("    T4-041 section 6 constant: D(1 + 2/(2-a)) -> 2D/(2-a); ratio (2/(2-a))/(1 + 2/(2-a)) = 2/(4-a):",
      sp.simplify((2 / (2 - a)) / (1 + 2 / (2 - a)) - 2 / (4 - a)) == 0,
      "; at a = 6/5:", sp.Rational(2) / (4 - sp.Rational(6, 5)), ", a = 7/5:", sp.Rational(2) / (4 - sp.Rational(7, 5)))

print()
print("=" * 100)
print("Part B. FLOAT checks (not proofs)")
print("=" * 100)


def p_of(tg, aa, R=1.0):
    return aa * np.exp(2 * tg) / (R ** 2 + np.exp(2 * tg))


def logw(tg, aa, R=1.0):
    return -(aa / 2) * np.log1p(np.exp(2 * tg) / R ** 2)


def future_H(F, tg, nv, aa, R=1.0):
    """H(t) = int_t^oo e^{-n(T-t)} (w(t)/w(T)) F(T) dT by the exact exponential-integrator recursion"""
    h = tg[1] - tg[0]
    lw = logw(tg, aa, R)
    H = np.zeros_like(F)
    for i in range(len(tg) - 2, -1, -1):
        e = math.exp(-nv * h + lw[i] - lw[i + 1])
        H[i] = e * H[i + 1] + 0.5 * h * (F[i] + e * F[i + 1])
    return H


def past_H(F, tg, kv, aa, R=1.0):
    h = tg[1] - tg[0]
    lw = logw(tg, aa, R)
    H = np.zeros_like(F)
    for i in range(1, len(tg)):
        e = math.exp(-kv * h + lw[i] - lw[i - 1])
        H[i] = e * H[i - 1] + 0.5 * h * (F[i] + e * F[i - 1])
    return H


rng = np.random.default_rng(20261028)
tg = np.arange(-20.0, 40.0, 0.001)
hh = tg[1] - tg[0]
for aa in (1.2, 1.4, 1.9):
    worst_sign, worst_res, worst_past = np.inf, 0.0, 0.0
    for rep in range(6):
        c0 = rng.uniform(-5, 20)
        wid = math.exp(rng.uniform(-1, 1))
        F = np.exp(-((tg - c0) / wid) ** 2) * np.cos(rng.uniform(0, 3) * tg + rng.uniform(0, 6))
        for nv in (2, 4):
            H = future_H(F, tg, nv, aa)
            pp = p_of(tg, aa)
            Hd = (nv - pp) * H - F
            G = F - 2 * nv * H
            Dv = -Hd + (aa - pp) * H
            K = (nv + aa) / (nv - aa)
            lhs = K ** 2 * np.sum(F ** 2) - np.sum(G ** 2)
            rhs = 4 * nv * aa / (nv - aa) ** 2 * (np.sum(Dv ** 2) + (nv ** 2 - aa ** 2) / aa * np.sum((aa - pp) * H ** 2))
            worst_res = max(worst_res, abs(lhs - rhs) / (K ** 2 * np.sum(F ** 2)))
            worst_sign = min(worst_sign, lhs / (K ** 2 * np.sum(F ** 2)))
        for kv in (2, 4):
            H = past_H(F, tg, kv, aa)
            G = F - 2 * kv * H
            worst_past = max(worst_past, math.sqrt(np.sum(G ** 2) / np.sum(F ** 2)))
    print(f"B1. a = {aa}: future blocks n = 2, 4 on random packets: max relative residual of (9) {worst_res:.2e},"
          f" min (K^2||F||^2 - ||G||^2)/(K^2||F||^2) = {worst_sign:.4f} (>= 0); past blocks k = 2, 4: max ||G||/||F|| = {worst_past:.6f} (<= 1)")
    assert worst_sign > -1e-6 and worst_past < 1 + 1e-6

# B2. sharpness packets
chi = lambda u: np.where(np.abs(u) < 1, np.exp(-1 / np.maximum(1e-300, 1 - u ** 2)), 0.0)
for aa in (1.2, 1.4):
    out = []
    for L in (2.0, 4.0, 6.0):
        tl = np.arange(L * L - L - 2, L * L + L + 6, 5e-4)
        HL = L ** -0.5 * chi((tl - L * L) / L)
        dHL = np.gradient(HL, tl)
        pp = p_of(tl, aa)
        FL = -dHL + (2 - pp) * HL
        GL = -dHL - (2 + pp) * HL
        Hint = future_H(FL, tl, 2, aa)
        agree = np.max(np.abs(Hint - HL)) / np.max(np.abs(HL))
        out.append(f"L = {L:.0f}: ratio {math.sqrt(np.sum(GL ** 2) / np.sum(FL ** 2)):.5f} (forward integral vs H_L {agree:.1e})")
    print(f"B2. a = {aa}, n = 2: " + "; ".join(out) + f"; limit (2+a)/(2-a) = {(2 + aa) / (2 - aa):.5f}")


# B3. velocity constant on real S1 inputs h = sum_{m odd >= 1} g_m(r) sin(m theta), g_m real.
#   f_{+-m} = +-g_m/(2i). Output modes of (I + B) h: j >= 1 odd: (g_j + B_{j+2} g_{j+2})/(2i) with the future block
#   n = j + 1; j = -1: f_{-1} + f_1 = 0; j <= -3: -(g_|j| + B_{j+2} g_{|j|-2})/(2i) with the past block k = |j| - 1.
#   ||h||^2 = pi sum ||g_m||^2, ||(I+B)h||^2 = 2 pi (1/4) S, ||U h||^2 = ||(I+B)h||^2/4, so
#   ||U h||^2/||h||^2 = S/(8 sum ||g_m||^2), where all norms are on the t line.
def farfield_matrix(aa, tv, M):
    """M(tau) for modes m = 1, 3, ..., 2M-1 with p = a (constant): T_n = -(n + a + i tau)/(n - a - i tau),
    P_k = (i tau - k + a)/(i tau + k + a)"""
    rows = []
    for idx in range(M):          # o_j, j = 2 idx + 1: g_j + T_{j+1} g_{j+2}
        j = 2 * idx + 1
        row = np.zeros(M, complex)
        row[idx] = 1
        if idx + 1 < M:
            nv = j + 1
            row[idx + 1] = -(nv + aa + 1j * tv) / (nv - aa - 1j * tv)
        rows.append(row)
    for idx in range(1, M + 1):   # p_j, j = 2 idx + 1 >= 3: g_j + P_{j-1} g_{j-2}
        j = 2 * idx + 1
        row = np.zeros(M, complex)
        if idx < M:
            row[idx] = 1
        kv = j - 1
        row[idx - 1] = (1j * tv - kv + aa) / (1j * tv + kv + aa)
        rows.append(row)
    return np.array(rows)


print("B3. velocity constant ||w U w^-1|| on real S1 inputs (FLOAT):")
for aa in (0.0, 1.2, 1.4, 1.5, 1.9):
    best, best_tau, best_M = 0.0, None, None
    for M in (1, 2, 3, 4, 8, 32, 128):
        for tv in np.concatenate([np.linspace(0, 5, 501), np.linspace(5, 200, 391)]):
            val = np.linalg.norm(farfield_matrix(aa, tv, M), 2) / math.sqrt(8)
            if val > best:
                best, best_tau, best_M = val, tv, M
    m1 = max(np.linalg.norm(farfield_matrix(aa, tv, 2), 2) / math.sqrt(8) for tv in np.linspace(0, 5, 501))
    print(f"    a = {aa}: far-field sup_tau ||M(tau)||/sqrt 8 = {best:.5f} (at tau = {best_tau:.2f}, {best_M} modes;"
          f" modes 1, 3 only: {m1:.5f}); T4-054 bound 2/(2-a) = {2 / (2 - aa):.5f}; T4-041 bound 1 + 2/(2-a) = {1 + 2 / (2 - aa):.5f}")


def block_dense_clean(nv, aa, tg, R=1.0):
    h = tg[1] - tg[0]
    lw = logw(tg, aa, R)
    Mt = len(tg)
    A = np.eye(Mt)
    kv = abs(nv)
    for i in range(Mt):
        j = np.arange(i, Mt) if nv > 0 else np.arange(0, i + 1)
        vv = np.abs(tg[j] - tg[i])
        wt = np.full(len(j), h)
        wt[0] = wt[-1] = h / 2
        A[i, j] -= 2 * kv * np.exp(-kv * vv) * np.exp(lw[i] - lw[j]) * wt
    return A


for aa, R in ((1.2, 1.0), (1.4, 1.0)):
    tgd = np.arange(-6.0, 16.0, 0.02)
    Mmodes = 4
    Tb = {j: block_dense_clean(j + 1, aa, tgd, R) for j in range(1, 2 * Mmodes, 2)}       # future n = j + 1
    Pb = {j: block_dense_clean(-(j - 1), aa, tgd, R) for j in range(3, 2 * Mmodes + 2, 2)}  # past k = j - 1
    Nt = len(tgd)

    def mv(gvec):
        gs = gvec.reshape(Mmodes, Nt)
        outs = []
        for idx in range(Mmodes):
            j = 2 * idx + 1
            o = gs[idx].copy()
            if idx + 1 < Mmodes:
                o = o + Tb[j] @ gs[idx + 1]
            outs.append(o)
        for idx in range(1, Mmodes + 1):
            j = 2 * idx + 1
            o = Pb[j] @ gs[idx - 1]
            if idx < Mmodes:
                o = o + gs[idx]
            outs.append(o)
        return np.concatenate(outs)

    def rmv(yvec):
        ys = yvec.reshape(2 * Mmodes, Nt)
        gs = np.zeros((Mmodes, Nt))
        for idx in range(Mmodes):
            j = 2 * idx + 1
            gs[idx] += ys[idx]
            if idx + 1 < Mmodes:
                gs[idx + 1] += Tb[j].T @ ys[idx]
        for idx in range(1, Mmodes + 1):
            j = 2 * idx + 1
            yy = ys[Mmodes + idx - 1]
            gs[idx - 1] += Pb[j].T @ yy
            if idx < Mmodes:
                gs[idx] += yy
        return gs.reshape(-1)

    op = LinearOperator((2 * Mmodes * Nt, Mmodes * Nt), matvec=mv, rmatvec=rmv, dtype=float)
    sv = svds(op, k=1, return_singular_vectors=False, tol=1e-8)[0]
    print(f"    full weighted operator, a = {aa}, R = {R}, modes 1..{2 * Mmodes - 1}, t in [-6, 16]: discretized"
          f" ||w U w^-1|| on S1 = {sv / math.sqrt(8):.5f} (T4-054 bound {2 / (2 - aa):.5f})")

print()
print("=" * 100)
print("Part C. Exact S1 velocity constant from the block bounds (rigorous given (9), (10))")
print("=" * 100)
print("  S1: h = sum_{m odd} g_m sin(m theta); with x_i = ||w g_(2i+1)|| (t line) the rows are")
print("  o_m = g_m + T_(m+1) g_(m+2) (m >= 1) and p_m = g_m + P_(m-1) g_(m-2) (m >= 3); the mode -1 output vanishes.")
print("  Triangle inequality with ||T_n|| <= K_n, ||P_k|| <= 1 gives S <= x^T A^T A x with A^T A tridiagonal:")
print("  d_0 = 2, d_i = 3 + K_(2i)^2 (i >= 1), e_i = 1 + K_(2i+2); and ||w U h||^2/||w h||^2 = S/(8 sum x_i^2).")


def certify_S1(aq, N=60, tail_c=Fr(1, 10 ** 9)):
    Kq = lambda nv: (nv + aq) / (nv - aq)
    d = lambda i: Fr(2) if i == 0 else 3 + Kq(2 * i) ** 2
    e = lambda i: 1 + Kq(2 * i + 2)
    Mf = np.zeros((N, N))
    for i in range(N):
        Mf[i, i] = float(d(i))
        if i + 1 < N:
            Mf[i, i + 1] = Mf[i + 1, i] = float(e(i))
    lam, vec = np.linalg.eigh(Mf)
    pv = np.abs(vec[:, -1])
    pv = pv / pv.max()
    v = [Fr(int(round(x * 10 ** 12)), 10 ** 12) + tail_c for x in pv]   # positive rational vector, tail value tail_c
    vt = lambda i: v[i] if i < N else tail_c
    rho = Fr(0)
    for i in range(N + 2):
        Mv = d(i) * vt(i) + e(i) * vt(i + 1) + (e(i - 1) * vt(i - 1) if i >= 1 else 0)
        rho = max(rho, Mv / vt(i))
    # i > N + 1: v constant, ratio e(i-1) + d(i) + e(i) = 5 + K_(2i)^2 + K_(2i) + K_(2i+2), decreasing in i
    tail_ratio = e(N + 1) + d(N + 2) + e(N + 2)
    assert tail_ratio <= rho and e(N) + d(N + 1) + e(N + 1) >= tail_ratio
    # rational upper bound for sqrt(rho/8)
    c_up = Fr(math.ceil(math.sqrt(float(rho / 8)) * 10 ** 6) + 1, 10 ** 6)
    assert c_up * c_up >= rho / 8
    return rho, c_up, float(lam[-1])


for aq in (Fr(6, 5), Fr(13, 10), Fr(7, 5), Fr(3, 2), Fr(19, 10)):
    rho, c_up, lamN = certify_S1(aq)
    a_f = float(aq)
    print(f"C1. a = {str(aq):>5}: Collatz-Wielandt rho <= {float(rho):.8f} (truncated lambda_max {lamN:.8f});"
          f" S1 velocity constant <= {float(c_up):.6f} (exact rational check); T4-054 bound 2/(2-a) = {2 / (2 - a_f):.6f};"
          f" ratio {float(c_up) / (2 / (2 - a_f)):.4f}")
