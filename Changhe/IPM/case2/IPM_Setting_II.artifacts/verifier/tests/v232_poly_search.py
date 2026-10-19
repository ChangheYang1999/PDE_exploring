"""V232: numerical counterexample search for Proposition 2.2 (extended): real polynomial solutions of
-Lap psi = rho_x, (lX + grad-perp psi).grad rho = rho, rho = x^2 + O(|X|^3), psi = O(|X|^2), deg rho <= N,
deg psi <= M = N + 1 (Proposition 2.2 gives M <= N + 1 for every l). Own implementation (numpy coefficient arrays;
not the lead analyst's or the referee's code). Under NR the degree-k transport condition (k <= N) is
D_k rho_k = 2x d_y psi_k - sum_{3<=j<=k-1} (-d_y psi_j d_x rho_(k+2-j) + d_x psi_j d_y rho_(k+2-j)),
D_k diagonal with entries i/2 + beta j - 1, so rho_k is determined by the harmonic parts h_k = a_k Re z^k + b_k Im z^k
of psi_k (k = 3..M); the unknowns are (a_k, b_k), and the equations are the conditions of degree N+1..N+M-2 with
rho_k = 0 there. Option x2: also require x^2 | rho (coefficients of y^k and x y^(k-1) in rho_k vanish).
Least squares (scipy, Levenberg-Marquardt) from random starts; reports the distinct solutions with small residual.
Deflation: the residual is multiplied by (1 + |u - u_triv|^(-pdef)) so that the (highly degenerate) known solution
repels the iteration; an endpoint with deflated residual near zero is a solution away from it.
Positive control (ctrl > 0): the system resid(u) - resid(u*) with u* = u_triv + a random vector of norm ctrl, which has
the root u*; the search must find it.
Usage: python3 v232_poly_search.py l N nstart seed pdef ctrl [x2]"""
import numpy as np, sys
from scipy.optimize import least_squares
l = float(sys.argv[1]); N = int(sys.argv[2]); ns = int(sys.argv[3]); seed = int(sys.argv[4]); pdef = float(sys.argv[5]); ctrl = float(sys.argv[6]); X2 = len(sys.argv) > 7
M = N + 1; beta = 2 * l - 0.5; K = N + M - 2
# homogeneous polynomial of degree k: array c[0..k], c[i] = coefficient of x^i y^(k-i)
def dx(c):
    k = len(c) - 1; return np.array([i * c[i] for i in range(1, k + 1)]) if k > 0 else np.zeros(1)
def dy(c):
    k = len(c) - 1; return np.array([(k - i) * c[i] for i in range(k)]) if k > 0 else np.zeros(1)
def mul(a, b):
    return np.convolve(a, b)
def bra(p, r):  # -p_y r_x + p_x r_y
    return -mul(dy(p), dx(r)) + mul(dx(p), dy(r))
def lap(c):
    k = len(c) - 1
    if k < 2: return np.zeros(1)
    out = np.zeros(k - 1)
    for i in range(k + 1):
        j = k - i
        if i >= 2: out[i - 2] += i * (i - 1) * c[i]
        if j >= 2: out[i] += j * (j - 1) * c[i]
    return out
PART = {}
for j in range(3, M + 2):  # particular: psi with c[j-1] = c[j] = 0, -Lap psi = F (degree j-2)
    A = np.zeros((j - 1, j - 1))
    for p in range(j - 1):
        e = np.zeros(j + 1); e[p] = 1; A[:, p] = -lap(e)
    PART[j] = np.linalg.inv(A)
def part(F, j):
    c = np.zeros(j + 1); c[:j - 1] = PART[j] @ F; return c
def harm(k):
    z = np.array([1.0 + 0j])
    for _ in range(k): z = np.convolve(z, np.array([1j, 1.0]))  # (y i + x): index i = power of x
    # convolve [1j, 1] means coefficient of x^0 is i (times y), of x^1 is 1: z = x + i y
    return z.real.copy(), z.imag.copy()
H = {k: harm(k) for k in range(3, M + 1)}
def Dinv(k):
    d = np.array([i / 2 + beta * (k - i) - 1 for i in range(k + 1)]); return d
DD = {k: Dinv(k) for k in range(3, N + 1)}
def resid(u):
    rho = {2: np.array([0, 0, 1.0])}; psi = {2: np.array([0, l - 0.5, 0])}
    out = []
    for k in range(3, K + 1):
        if k <= M:
            F = dx(rho[k - 1]) if (k - 1) in rho else np.zeros(k - 1)
            if len(F) != k - 1: F = np.zeros(k - 1)
            a, b = u[2 * (k - 3)], u[2 * (k - 3) + 1]
            psi[k] = part(F, k) + a * H[k][0] + b * H[k][1]
        S = np.zeros(k + 1)
        if k in psi: S = S - mul(np.array([0, 1.0]), dy(psi[k])) * 2 if False else S - 2 * np.concatenate([[0], dy(psi[k])])
        for j in range(3, k):
            m = k + 2 - j
            if j in psi and m in rho and m >= 3: S = S + bra(psi[j], rho[m])
        # equation: D_k rho_k + S = 0  (S collects -2x psi_k,y and the brackets)
        if k <= N:
            rho[k] = -S / DD[k]
            if X2: out.extend(rho[k][:2])  # coefficients of y^k and x y^(k-1)
        else:
            out.extend(S)
    return np.array(out)
def check_pde(u):
    # rebuild and evaluate both PDEs at random points as an independent check
    rho = {2: np.array([0, 0, 1.0])}; psi = {2: np.array([0, l - 0.5, 0])}
    for k in range(3, M + 1):
        F = dx(rho[k - 1]) if (k - 1) in rho else np.zeros(k - 1)
        psi[k] = part(F, k) + u[2 * (k - 3)] * H[k][0] + u[2 * (k - 3) + 1] * H[k][1]
        if k <= N:
            S = -2 * np.concatenate([[0], dy(psi[k])])
            for j in range(3, k):
                m = k + 2 - j
                if m in rho and m >= 3: S = S + bra(psi[j], rho[m])
            rho[k] = -S / DD[k]
    def ev(c, X, Y):
        k = len(c) - 1; return sum(c[i] * X**i * Y**(k - i) for i in range(k + 1))
    rng = np.random.default_rng(1); P = rng.uniform(-0.7, 0.7, (50, 2)); h = 1e-4
    def R(X, Y): return sum(ev(c, X, Y) for c in rho.values())
    def S(X, Y): return sum(ev(c, X, Y) for c in psi.values())
    e1 = e2 = 0
    for X, Y in P:
        rx = (R(X + h, Y) - R(X - h, Y)) / (2 * h); ry = (R(X, Y + h) - R(X, Y - h)) / (2 * h)
        sx = (S(X + h, Y) - S(X - h, Y)) / (2 * h); sy = (S(X, Y + h) - S(X, Y - h)) / (2 * h)
        lp = (S(X + h, Y) + S(X - h, Y) + S(X, Y + h) + S(X, Y - h) - 4 * S(X, Y)) / h**2
        e1 = max(e1, abs(-lp - rx)); e2 = max(e2, abs((l * X - sy) * rx + (l * Y + sx) * ry - R(X, Y)))
    return e1, e2, {k: np.round(v, 6).tolist() for k, v in rho.items() if np.abs(v).max() > 1e-8}
u0 = np.zeros(2 * (M - 2)); u0[0] = -1 / 3  # the known solution psi_3 = -x^3/3
print('l %.6g beta %.6g N %d M %d unknowns %d equations %d x2 %s; |resid(trivial)| %.2e' % (l, beta, N, M, len(u0),
      len(resid(u0)), X2, np.linalg.norm(resid(u0))))
print('PDE check at the trivial point (max |E|, max |R| at 50 points, FD h 1e-4):', check_pde(u0)[:2])
rng = np.random.default_rng(seed); ends = []
resid0 = resid
if ctrl > 0:
    w = rng.normal(size=len(u0)); ustar = u0 + ctrl * w / np.linalg.norm(w); rstar = resid0(ustar)
    resid = lambda u: resid0(u) - rstar
    print('positive control: u* at distance %.3g, |resid0(u*)| %.3e' % (ctrl, np.linalg.norm(rstar)))
for t in range(ns):
    s = 10 ** rng.uniform(-1.5, 1)
    x0 = rng.normal(0, s, len(u0))
    try:
        r = least_squares(lambda u: resid(u) * (1 + np.linalg.norm(u - u0)**(-pdef)), x0, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
    except Exception as e:
        continue
    ends.append((np.linalg.norm(resid(r.x)), np.linalg.norm(r.x - u0), r.x))
f = np.array([e[0] for e in ends]); d = np.array([e[1] for e in ends])
print('starts %d; final residual quantiles min %.2e, 10%% %.2e, median %.2e, max %.2e' % (len(f), f.min(),
      np.quantile(f, 0.1), np.median(f), f.max()))
for lo, hi in ((0, 1e-12), (1e-12, 1e-9), (1e-9, 1e-6), (1e-6, 1e-3), (1e-3, np.inf)):
    sel = (f >= lo) & (f < hi)
    print('  residual in [%.0e, %.0e): %d endpoints, distance to the trivial point max %.2e' % (lo, hi, sel.sum(),
          d[sel].max() if sel.any() else 0))
cand = [e for e in ends if e[0] < 1e-8 and e[1] > 1e-3]
print('candidate nontrivial solutions (residual < 1e-8, distance > 1e-3): %d' % len(cand))
if ctrl > 0: print('control: endpoints within 1e-6 of u*: %d' % sum(np.linalg.norm(e[2] - ustar) < 1e-6 for e in ends))
for e in sorted(ends, key=lambda e: e[0])[:3] + cand[:5]:
    e1, e2, rh = check_pde(e[2])
    print('  resid %.2e dist %.2e  PDE check %.1e %.1e' % (e[0], e[1], e1, e2))
# local minima away from the trivial point (resid > 1e-6): smallest residuals and their distances
far = sorted([e for e in ends if e[1] > 1e-2], key=lambda e: e[0])[:5]
print('smallest residuals among endpoints at distance > 1e-2:', ['%.2e@%.2e' % (e[0], e[1]) for e in far])
