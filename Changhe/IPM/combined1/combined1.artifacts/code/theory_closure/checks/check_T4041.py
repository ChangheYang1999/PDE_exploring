"""Independent check by c1-t1 of c1-t4 T4-041 (review R1-008 in nonlinear_closure/REVIEWS_v04.md).

Target: c1-t4/research/weighted_signed_compact/PROOF.md (sha256 1eeb2c06...), the weighted signed compact
remainder for w_R = (1 + |x|^2/R^2)^(-a/2), 0 < a < 2.

Part A (sympy, exact): symbol identity U2 + i U1 = -(I + B)/2; the kernel u from the Hessian of
  -log|z|/(2 pi) with contact terms -(1/2) delta in each diagonal entry; |u| and ||Du||_op of (5); the
  second-order identity for B_R; the odd antisymmetrization coefficient 1/4; the integrals in (6) and (7);
  the angular block formulas for f = z^3 exp(-|z|^2) and conj(z) exp(-|z|^2).
Part B (exact matrices): the operator identities Sym Q = P_rho + K_rho and K_b = S_b - b with random
  commuting skew-symmetric R1, R2 satisfying R1^2 + R2^2 = -I and random diagonal multipliers.
Part C (FLOAT): FFT check of the block formulas; the inner integral I0 = 2 pi (4 log 2 - 1) <= 68 pi;
  discretized weighted block norms against the bounds 1 + 2n/(n - a) and 3; random sampling of the
  pointwise kernel bounds of section 3 for a model coefficient; size of the crude bound (3).

Usage (from artifacts/checks):
  OMP_NUM_THREADS=1 python3 -B check_T4041.py > check_T4041.out
Needs sympy, numpy, scipy.
"""
import math
import warnings

import numpy as np
import sympy as sp
from scipy import integrate

warnings.filterwarnings("ignore", category=integrate.IntegrationWarning)  # C2 tolerance notices; the error is printed

print("=" * 100)
print("Part A. Exact symbolic checks")
print("=" * 100)
x1, x2, y1, y2, z1, z2 = sp.symbols("x1 x2 y1 y2 z1 z2", real=True)
k1, k2 = sp.symbols("xi1 xi2", real=True)
r, s, v = sp.symbols("r s v", positive=True)
a, d = sp.symbols("a delta", positive=True)

# A1. symbols: R_j <-> i xi_j/|xi|; U1 = -R1 R2 <-> xi1 xi2/|xi|^2; U2 = R1^2 <-> -xi1^2/|xi|^2
q2 = k1 ** 2 + k2 ** 2
sU1 = -(sp.I * k1) * (sp.I * k2) / q2
sU2 = (sp.I * k1) ** 2 / q2
sB = (sp.I * k1 + k2) / (sp.I * k1 - k2)          # (dx - i dy)/(dx + i dy)
lhs = sp.simplify(sU2 + sp.I * sU1 + (1 + sB) / 2)
print("A1. U2 + i U1 + (I + B)/2 has symbol", lhs, "; B symbol = (xi1 - i xi2)^2/|xi|^2:",
      sp.simplify(sB - (k1 - sp.I * k2) ** 2 / q2) == 0, "; |B symbol| = 1:",
      sp.simplify(sp.Abs(sB).rewrite(sp.sqrt)) == 1 or sp.simplify(sB * sp.conjugate(sB)) == 1)
assert lhs == 0

# A2. kernel of U away from 0 from Gamma = -log|z|/(2 pi); trace of the Hessian vanishes away from 0
Gam = -sp.log(sp.sqrt(z1 ** 2 + z2 ** 2)) / (2 * sp.pi)
H11, H12, H22 = sp.diff(Gam, z1, 2), sp.diff(Gam, z1, z2), sp.diff(Gam, z2, 2)
u = sp.Matrix([-2 * z1 * z2, z1 ** 2 - z2 ** 2]) / (2 * sp.pi * (z1 ** 2 + z2 ** 2) ** 2)
print("A2. -d1 d2 Gamma - u1 =", sp.simplify(-H12 - u[0]), "; d1^2 Gamma - u2 =", sp.simplify(H11 - u[1]),
      "; trace of Hessian away from 0 =", sp.simplify(H11 + H22))
assert sp.simplify(-H12 - u[0]) == 0 and sp.simplify(H11 - u[1]) == 0 and sp.simplify(H11 + H22) == 0
# contact: the angular average of the symbol of R1^2 is -1/2 (so the contact term is -(1/2) delta, R1 R2 has none)
th = sp.symbols("theta", real=True)
avg11 = sp.integrate(-sp.cos(th) ** 2, (th, 0, 2 * sp.pi)) / (2 * sp.pi)
avg12 = sp.integrate(-sp.cos(th) * sp.sin(th), (th, 0, 2 * sp.pi)) / (2 * sp.pi)
print("    angular mean of symbol of R1^2 =", avg11, "; of R1 R2 =", avg12,
      "(the p.v. kernels have zero angular mean, so these are the contact coefficients)")
assert avg11 == sp.Rational(-1, 2) and avg12 == 0

# A3. (5): |u| = 1/(2 pi |z|^2), ||Du||_op = 1/(pi |z|^3)
Du = u.jacobian([z1, z2])
nz = z1 ** 2 + z2 ** 2
DtD = sp.simplify(Du.T * Du)
print("A3. |u|^2 (2 pi |z|^2)^2 =", sp.simplify((u.T * u)[0] * (2 * sp.pi * nz) ** 2),
      "; Du^T Du (pi |z|^3)^2 =", sp.simplify(DtD * sp.pi ** 2 * nz ** 3).tolist())
assert sp.simplify((u.T * u)[0] * (2 * sp.pi * nz) ** 2) == 1
assert sp.simplify(DtD * sp.pi ** 2 * nz ** 3 - sp.eye(2)) == sp.zeros(2)

# A4. second-order cancellation B = (t-1)(Ax - Ay) + (t-1)^2/t Ay, with B = (t-1)Ax + (1/t - 1)Ay
t, Ax, Ay = sp.symbols("t A_x A_y", positive=True)
print("A4. second-order identity:", sp.simplify((t - 1) * Ax + (1 / t - 1) * Ay - ((t - 1) * (Ax - Ay) + (t - 1) ** 2 / t * Ay)) == 0)

# A5. odd antisymmetrization: kernel k(x,y) = (1/2) B(x,y).u(x-y) with B(x,-y) = B(x,y), u even:
#     on odd inputs k -> (k(x,y) - k(x,-y))/2 = (1/4) B.(u(x-y) - u(x+y)); the result is odd in x and y
uf = sp.Lambda((z1, z2), u)
print("A5. u is even:", sp.simplify(uf(-z1, -z2) - uf(z1, z2)) == sp.zeros(2, 1),
      "; coefficient (1/2)(1/2) = 1/4 by construction; oddness of u(x-y) - u(x+y) in x:",
      sp.simplify((uf(-x1 - y1, -x2 - y2) - uf(-x1 + y1, -x2 + y2)) + (uf(x1 - y1, x2 - y2) - uf(x1 + y1, x2 + y2)))
      == sp.zeros(2, 1))

# A6. integrals: int_{<x> > 2<y>} <x>^(2a-6) dx (in rho = <x>, dx = 2 pi rho drho), int |y|^2 <y>^(-4-2 delta) dy,
#     int <x>^(-2-2 delta) dx
Y = sp.symbols("Y", positive=True)  # Y = <y> >= 1
rho = sp.symbols("rho", positive=True)
I_far = sp.integrate(rho ** (2 * a - 6) * 2 * sp.pi * rho, (rho, 2 * Y, sp.oo), conds="none")
I_far_claim = sp.pi * 4 ** (a - 2) * Y ** (2 * a - 4) / (2 - a)
I_y = sp.integrate(r ** 2 * (1 + r ** 2) ** (-2 - d) * 2 * sp.pi * r, (r, 0, sp.oo), conds="none")
I_c = sp.integrate((1 + r ** 2) ** (-1 - d) * 2 * sp.pi * r, (r, 0, sp.oo), conds="none")
print("A6. far x-integral minus claim at sample a in (0,2):",
      [sp.N((I_far - I_far_claim).subs({a: av, Y: 3})) for av in (sp.Rational(1, 2), sp.Rational(7, 5), sp.Rational(19, 10))])
print("    int |y|^2 <y>^(-4-2d) dy =", sp.simplify(sp.gammasimp(I_y)), "; claim pi/(d(d+1)); difference at d = 0.447611:",
      sp.N((I_y - sp.pi / (d * (d + 1))).subs(d, sp.Rational(447611, 10 ** 6))))
print("    int <x>^(-2-2d) dx =", sp.simplify(I_c), "; claim pi/d")
for av in (sp.Rational(1, 2), sp.Rational(7, 5), sp.Rational(19, 10)):
    assert abs(sp.N((I_far - I_far_claim).subs({a: av, Y: 3}))) < 1e-30
assert abs(sp.N((I_y - sp.pi / (d * (d + 1))).subs(d, sp.Rational(447611, 10 ** 6)))) < 1e-30
assert sp.simplify(I_c - sp.pi / d) == 0
# region facts: <x> > 2<y> implies |x| > sqrt 3, |y| < |x|/2, <x>/|x| <= 2/sqrt 3; (2/sqrt3)^3 * 8 = 64/(3 sqrt 3)
print("    far constant: (1/4) * 2 * 16/pi * (2/sqrt3)^3 = 64/(3 sqrt3 pi):",
      sp.simplify(sp.Rational(1, 4) * 2 * 16 / sp.pi * (2 / sp.sqrt(3)) ** 3 - 64 / (3 * sp.sqrt(3) * sp.pi)) == 0)
print("    away constant: (1/4) * 2 * 8/pi = 4/pi; near constant: (1/4) * 2/(2 pi) = 1/(4 pi)")
# |t-1| <= (4a/3) d/<x> on the near region: a zeta^(a-1) with zeta in [3/4, 5/4] <x>, so need (5/4)^(a-1) <= 4/3
# for 1 <= a < 2 and (4/3)^(1-a) <= 4/3 for 0 < a <= 1
print("    (5/4)^(a-1) <= 4/3 up to a =", sp.N(1 + sp.log(sp.Rational(4, 3)) / sp.log(sp.Rational(5, 4)), 8), "(> 2)")

# A7. angular blocks, exact: f = z^3 e^{-|z|^2} (m = 3, n = 2) and f = conj(z) e^{-|z|^2} (m = -1, n = -2)
#     formula: g' - n g/r = f_m, output (B f)_{m-2} = f_m + 2 n g/r, g decaying (n > 0) or regular at 0 (n < 0)
fm = r ** 3 * sp.exp(-r ** 2)
g = -r ** 2 * sp.integrate(s ** (-2) * fm.subs(r, s), (s, r, sp.oo))
out_pos = sp.simplify(fm + 4 * g / r)
fm2 = r * sp.exp(-r ** 2)
g2 = r ** (-2) * sp.integrate(s ** 2 * fm2.subs(r, s), (s, 0, r))
out_neg = sp.simplify(fm2 - 4 * g2 / r)
print("A7. n = 2 block output for z^3 e^{-r^2}:", out_pos, "; n = -2 block output for conj(z) e^{-r^2}:", out_neg)
# direct: B f = (dx - i dy) g with (dx + i dy) g = f; z^3 e^{-|z|^2}: g = -z^2 e^{-|z|^2}/2 ; output (z|z|^2 - 2z) e^{-|z|^2}
zc = x1 + sp.I * x2
gdir = -zc ** 2 * sp.exp(-(x1 ** 2 + x2 ** 2)) / 2
chk = sp.simplify(sp.diff(gdir, x1) + sp.I * sp.diff(gdir, x2) - zc ** 3 * sp.exp(-(x1 ** 2 + x2 ** 2)))
outdir = sp.simplify(sp.diff(gdir, x1) - sp.I * sp.diff(gdir, x2))
print("    direct d-bar solve residual:", chk, "; direct output:", sp.factor(outdir))
assert chk == 0 and sp.simplify(out_pos - (r ** 3 - 2 * r) * sp.exp(-r ** 2)) == 0

print()
print("=" * 100)
print("Part B. Operator identities with exact rational matrices")
print("=" * 100)
rng = np.random.default_rng(20261028)
nb = 6                     # 6 blocks of size 2 -> 12 x 12
# exact orthogonal matrix via the Cayley transform of a rational skew matrix
Sk = sp.Matrix(2 * nb, 2 * nb, lambda i, j: 0)
for i in range(2 * nb):
    for j in range(i + 1, 2 * nb):
        val = sp.Rational(int(rng.integers(-9, 10)), 7)
        Sk[i, j], Sk[j, i] = val, -val
I12 = sp.eye(2 * nb)
O = (I12 - Sk) * (I12 + Sk).inv()
J = sp.Matrix([[0, -1], [1, 0]])
pyth = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)), (sp.Rational(8, 17), sp.Rational(15, 17)),
        (sp.Rational(7, 25), sp.Rational(24, 25)), (sp.Rational(20, 29), sp.Rational(21, 29)), (1, 0)]
R1b = sp.diag(*[c * J for c, _ in pyth])
R2b = sp.diag(*[s_ * J for _, s_ in pyth])
R1m, R2m = O * R1b * O.T, O * R2b * O.T
assert R1m * R2m == R2m * R1m and R1m.T == -R1m and R2m.T == -R2m and R1m ** 2 + R2m ** 2 == -I12
rx = sp.diag(*[sp.Rational(int(rng.integers(-20, 21)), 11) for _ in range(2 * nb)])
ry = sp.diag(*[sp.Rational(int(rng.integers(-20, 21)), 13) for _ in range(2 * nb)])
bb = sp.diag(*[sp.Rational(int(rng.integers(-20, 21)), 17) for _ in range(2 * nb)])
Qop = -rx * R1m * R2m + ry * R1m ** 2
SymQ = (Qop + Qop.T) / 2
Pr = R1m * ry * R1m - (R1m * rx * R2m + R2m * rx * R1m) / 2
comm = lambda X, Y_: X * Y_ - Y_ * X
Kr = comm(R1m, comm(R1m, ry)) / 2 - comm(R1m, comm(R2m, rx)) / 2
Kb = (comm(R1m, comm(R1m, bb)) + comm(R2m, comm(R2m, bb))) / 2
Sb = -(R1m * bb * R1m + R2m * bb * R2m)
print("B1. Sym Q = P_rho + K_rho exactly:", SymQ == Pr + Kr)
print("B2. K_b = S_b - b exactly (so b = S_b - K_b and K_eff = K_rho + D_R - K_b):", Kb == Sb - bb)
# principal form: <S_b phi, phi> + <P phi, phi> = sum b|R phi|^2 - rho_y |R1 phi|^2 + rho_x R1phi R2phi
ph = sp.Matrix([sp.Rational(int(rng.integers(-9, 10)), 5) for _ in range(2 * nb)])
X1v, X2v = R1m * ph, R2m * ph
form = (ph.T * (Sb + Pr) * ph)[0]
form2 = sum(bb[i, i] * (X1v[i] ** 2 + X2v[i] ** 2) - ry[i, i] * X1v[i] ** 2 + rx[i, i] * X1v[i] * X2v[i] for i in range(2 * nb))
print("B3. <(S_b + P_rho) phi, phi> = int [R1phi, R2phi] M_R [R1phi, R2phi]^T exactly:", sp.simplify(form - form2) == 0,
      "; sum ||R_j phi||^2 = ||phi||^2:", (X1v.T * X1v + X2v.T * X2v)[0] == (ph.T * ph)[0])
assert SymQ == Pr + Kr and Kb == Sb - bb and sp.simplify(form - form2) == 0
bq, px, py = sp.symbols("b rho_x rho_y", real=True)
M = sp.Matrix([[bq - py, px / 2], [px / 2, bq]])
ev = list(M.eigenvals().keys())
lam_claim = bq + (sp.sqrt(px ** 2 + py ** 2) - py) / 2
print("B4. eigenvalues of M_R:", ev, "; largest = b + (|D rho| - rho_y)/2:",
      any(sp.simplify(e - lam_claim) == 0 for e in ev))

print()
print("=" * 100)
print("Part C. FLOAT checks (not proofs)")
print("=" * 100)
# C1. FFT check of the block formulas (B symbol (xi1 - i xi2)^2/|xi|^2)
N, L = 1024, 40.0
xs = (np.arange(N) - N // 2) * (2 * L / N)
X, Yg = np.meshgrid(xs, xs, indexing="ij")
Z = X + 1j * Yg
R2 = np.abs(Z) ** 2
kk = 2 * np.pi * np.fft.fftfreq(N, d=2 * L / N)
K1, K2 = np.meshgrid(kk, kk, indexing="ij")
KK = K1 ** 2 + K2 ** 2
KK[0, 0] = 1.0
symB = (K1 - 1j * K2) ** 2 / KK
symB[0, 0] = 0.0


def applyB(f):
    return np.fft.ifft2(symB * np.fft.fft2(f))


Rr = np.sqrt(R2)
for name, f, expected in [
    ("m = 3 (n = 2)  ", Z ** 3 * np.exp(-R2), Z * (R2 - 2) * np.exp(-R2)),
    ("m = -1 (n = -2)", np.conj(Z) * np.exp(-R2),
     np.conj(Z) ** 3 / np.where(Rr > 0, Rr, 1) ** 3 * np.where(Rr > 0, Rr * np.exp(-R2) - 2 * (1 - (1 + R2) * np.exp(-R2)) / np.where(Rr > 0, Rr, 1) ** 3, 0)),
    ("m = 1 (n = 0)  ", Z * np.exp(-R2), np.conj(Z) * np.exp(-R2)),
]:
    Bf = applyB(f)
    mask = (Rr > 0.05) & (Rr < 8)
    err = np.max(np.abs(Bf - expected)[mask]) / np.max(np.abs(expected)[mask])
    print(f"C1. block formula {name}: max relative deviation on 0.05 < r < 8 = {err:.2e}")

# C2. inner integral I0 = int |v(eta + q) - v(eta)|^4 d eta for |q| = 1, and the crude 68 pi
def integrand(rr, tt):
    e1, e2 = rr * math.cos(tt), rr * math.sin(tt)
    n1 = math.hypot(e1 + 1, e2)
    d1 = (e1 + 1) / n1 - math.cos(tt)
    d2 = e2 / n1 - math.sin(tt)
    return (d1 * d1 + d2 * d2) ** 2 * rr


I0, I0err = 0.0, 0.0
for lo_, hi_ in [(0, 0.5), (0.5, 0.999), (0.999, 1.001), (1.001, 2), (2, 50), (50, 5000)]:
    val, er = integrate.dblquad(lambda tt, rr: integrand(rr, tt), lo_, hi_, 0, 2 * math.pi, epsabs=1e-11, epsrel=1e-11)
    I0 += val
    I0err += er
tail = 0.0  # |v(eta+q)-v(eta)| ~ |sin|/r, tail int_{5000}^inf ~ 2 pi * (3/8)/r^3 ... negligible
print(f"C2. I0 numeric (r < 5000) = {I0:.10f} (+- {I0err:.1e}); 2 pi (4 log 2 - 1) = {2 * math.pi * (4 * math.log(2) - 1):.10f};"
      f" crude 68 pi = {68 * math.pi:.4f}; (4 log 2 - 1)/(8 pi) = {(4 * math.log(2) - 1) / (8 * math.pi):.6f}, 17/(4 pi) = {17 / (4 * math.pi):.6f}")


# C3. weighted block norms, discretized on t = log r in [-T, T], R = 1, trapezoid in v (FLOAT lower estimates)
def block_matrix(n, aa, T=14.0, h=0.01, shift=0.0):
    tg = np.arange(-T, T + h / 2, h) + shift
    M_ = len(tg)
    logw = -(aa / 2) * np.log1p(np.exp(2 * tg))
    A_ = np.eye(M_)
    idx = np.arange(M_)
    for k in range(M_):
        if n > 0:
            j = idx[k:]
            vv = tg[j] - tg[k]
        else:
            j = idx[:k + 1]
            vv = tg[k] - tg[j]
        wt = np.full(len(j), h)
        wt[0] = wt[-1] = h / 2
        A_[k, j] += 2 * n * np.exp(-abs(n) * vv) * np.exp(logw[k] - logw[j]) * wt * (-1 if n > 0 else 1)
    return A_


for aa in (1.2, 1.4, 1.5):
    rows = []
    for n in (2, 4, -2):
        A_ = block_matrix(n, aa, T=12.0, h=0.02)
        nrm = float(np.linalg.norm(A_, 2))
        bound = 1 + 2 * n / (n - aa) if n > 0 else 3.0
        asym = (n + aa) / (n - aa) if n > 0 else 1.0
        rows.append(f"n={n:+d}: discretized {nrm:.4f}, proof bound {bound:.4f}, far-field multiplier {asym:.4f}")
    print(f"C3. a = {aa}: " + "; ".join(rows))
    print(f"    (4) constant 1 + 2/(2-a) = {1 + 2 / (2 - aa):.4f}; with the far-field forward value it would be 2/(2-a) = {2 / (2 - aa):.4f}")
for aa in (1.2, 1.4):
    nrm = float(np.linalg.norm(block_matrix(2, aa, T=20.0, h=0.02, shift=10.0), 2))
    print(f"    n = 2, a = {aa}, longer interval t in [-10, 30]: discretized {nrm:.4f} (approaches the far-field value"
          f" {(2 + aa) / (2 - aa):.4f} from below; FLOAT, not a proof)")
A_ = block_matrix(1, 0.9, T=12.0, h=0.02)
print(f"    even sector n = 1, a = 0.9 (not used by T4-041): discretized {np.linalg.norm(A_, 2):.4f}, Young bound {1 + 2 / (1 - 0.9):.1f};"
      " blows up as a -> 1 (Muckenhoupt limit without oddness)")

# C4. pointwise kernel bounds of section 3 for a model coefficient A(X) = (<X>^-dl, X1 X2 <X>^(-2-dl)), R = 1
dl = 0.447611


def Afun(P):
    n2 = 1 + P[..., 0] ** 2 + P[..., 1] ** 2
    return np.stack([n2 ** (-dl / 2), P[..., 0] * P[..., 1] * n2 ** (-1 - dl / 2)], axis=-1)


def DAop(P, hh=1e-6):
    e1 = np.array([hh, 0.0])
    e2 = np.array([0.0, hh])
    c1 = (Afun(P + e1) - Afun(P - e1)) / (2 * hh)
    c2 = (Afun(P + e2) - Afun(P - e2)) / (2 * hh)
    Mx = np.stack([c1, c2], axis=-1)
    return np.linalg.norm(Mx, ord=2, axis=(-2, -1))


grid = np.exp(np.linspace(-6, 9, 600))
angs = np.linspace(0, 2 * np.pi, 181)
Pg = np.stack([np.outer(grid, np.cos(angs)), np.outer(grid, np.sin(angs))], axis=-1).reshape(-1, 2)
Pg = np.vstack([Pg, np.zeros((1, 2))])
br = np.sqrt(1 + (Pg ** 2).sum(-1))
C0m = 1.02 * float(np.max(np.linalg.norm(Afun(Pg), axis=-1) * br ** dl))
C1m = 1.02 * float(np.max(DAop(Pg) * br ** (1 + dl)))


def ukern(P):
    n2 = (P ** 2).sum(-1)
    return np.stack([-2 * P[..., 0] * P[..., 1], P[..., 0] ** 2 - P[..., 1] ** 2], axis=-1) / (2 * np.pi * n2[..., None] ** 2)


for aa in (1.2, 1.4, 1.9):
    Bnear = aa * (4 / 3) ** (2 + dl) * C1m + aa ** 2 * (4 / 3) ** (2 + aa + dl) * C0m
    Cnear, Caway = Bnear / (4 * np.pi), (4 / np.pi) * (2 ** aa + 1) * (1 + 2 ** dl) * C0m
    Ccomp, Cfar = max(Cnear, Caway), 64 * C0m / (3 * np.sqrt(3) * np.pi)
    worst = {"near": 0.0, "away": 0.0, "far": 0.0}
    for rep in range(40):
        rad1 = np.exp(rng.uniform(-5, 7, 50000))
        Px = np.stack([rad1 * np.cos(rng.uniform(0, 2 * np.pi, 50000)), rad1 * np.sin(rng.uniform(0, 2 * np.pi, 50000))], -1)
        mode = rep % 3
        if mode == 0:      # near: y close to x or -x
            bx = np.sqrt(1 + (Px ** 2).sum(-1))
            off = rng.standard_normal((50000, 2)) * (bx[:, None] * np.exp(rng.uniform(-8, np.log(0.25), (50000, 1))))
            Py = Px * rng.choice([-1, 1], (50000, 1)) + off
        elif mode == 1:    # comparable, random
            rad2 = rad1 * np.exp(rng.uniform(-0.7, 0.7, 50000))
            ang2 = rng.uniform(0, 2 * np.pi, 50000)
            Py = np.stack([rad2 * np.cos(ang2), rad2 * np.sin(ang2)], -1)
        else:              # far
            rad2 = rad1 * np.exp(rng.uniform(-10, -0.7, 50000))
            ang2 = rng.uniform(0, 2 * np.pi, 50000)
            Py = np.stack([rad2 * np.cos(ang2), rad2 * np.sin(ang2)], -1)
        bx = np.sqrt(1 + (Px ** 2).sum(-1))
        by = np.sqrt(1 + (Py ** 2).sum(-1))
        tt_ = (by / bx) ** aa
        Bv = (tt_ - 1)[:, None] * Afun(Px) + (1 / tt_ - 1)[:, None] * Afun(Py)
        Dv = 0.25 * np.abs((Bv * (ukern(Px - Py) - ukern(Px + Py))).sum(-1))
        comp = (by >= bx / 2) & (by <= 2 * bx)
        dd = np.minimum(np.linalg.norm(Px - Py, axis=-1), np.linalg.norm(Px + Py, axis=-1))
        near = comp & (dd <= bx / 4)
        away = comp & (dd > bx / 4)
        far = bx > 2 * by
        if near.any():
            worst["near"] = max(worst["near"], float(np.max(Dv[near] / (Cnear * bx[near] ** (-2 - dl)))))
        if away.any():
            worst["away"] = max(worst["away"], float(np.max(Dv[away] / (Caway * bx[away] ** (-2 - dl)))))
        if far.any():
            ny = np.linalg.norm(Py, axis=-1)
            worst["far"] = max(worst["far"], float(np.max(Dv[far] / (Cfar * ny[far] * bx[far] ** (aa - 3) * by[far] ** (-aa - dl)))))
    print(f"C4. a = {aa}, model C0 = {C0m:.4f}, C1 = {C1m:.4f}: largest sampled |D_R|/bound: near {worst['near']:.4f},"
          f" away {worst['away']:.4f}, far {worst['far']:.4f} (all must be <= 1)")
    assert max(worst.values()) <= 1

# C5. size of the crude bound (3) for delta = 0.447611 (state 131), as multiples of the coefficient constants
print("C5. crude HS bound (3), delta = 0.447611:")
for aa in (1.2, 1.4):
    for C0v, C1v in ((1.0, 1.0),):
        Bnear = aa * (4 / 3) ** (2 + dl) * C1v + aa ** 2 * (4 / 3) ** (2 + aa + dl) * C0v
        Cnear, Caway = Bnear / (4 * np.pi), (4 / np.pi) * (2 ** aa + 1) * (1 + 2 ** dl) * C0v
        Cfar = 64 * C0v / (3 * np.sqrt(3) * np.pi)
        comp_t = 4 * np.pi ** 2 * max(Cnear, Caway) ** 2 / dl
        far_t = 2 * Cfar ** 2 * np.pi ** 2 * 4 ** (aa - 2) / ((2 - aa) * dl * (dl + 1))
        print(f"    a = {aa}, C0 = C1 = 1: C_near = {Cnear:.4f}, C_away = {Caway:.4f}, C_far = {Cfar:.4f};"
              f" comparable term {comp_t:.2f}, far term {far_t:.2f}, HS <= {math.sqrt(comp_t + far_t):.2f} (scales linearly in C0, C1)")
