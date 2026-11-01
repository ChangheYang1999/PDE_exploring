"""One-step linearization error of the canonical log recursion (astra referee, 15:00Z, item 2): at a stored order n, recompute the order-n density
from the stored lower orders with the pair sum restricted to min(i, n-i) <= L (same linear solve as the full step), and report
  eps_n(L) = || f_n - f_n^(L) ||_l1 / || f_n ||_l1   (midpoints; also the l1 share of the pairs with min(i, j) > L in the accumulated bilinear sum)
for L in a list. Pairs are accumulated in increasing m = min(i, n-i); the cumulative sums at the requested L are kept. usage: onestep_edge_error.py CKPT n L1,L2,..."""
import sys, os, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from logff import *
L = LogFarField.load(sys.argv[1]); R = L.R; n = int(sys.argv[2]); Ls = sorted(int(x) for x in sys.argv[3].split(','))
assert n in L.f and all(i in L.f and i in L.g for i in range(1, n)), 'need all lower orders'
def lin_solve(acc):
    lam = (n - 1) * (L.c_l - 1); x = col_scale(R, acc, 1 / lam); term = x
    for _ in range(len(acc) + 1):
        term = col_scale(R, col_T(R, term), L.c_l / lam)
        if all(R.is_zero(v) for a in term for v in a): break
        x = col_add(R, x, term)
    return col_trim(R, x)
def l1(cols):
    return sum(abs(R.to_float(v)) for a in cols for v in a)
def l1diff(A, B):
    tot = 0.0; Q = max(len(A), len(B))
    for q in range(Q):
        a = A[q] if q < len(A) else []; b = B[q] if q < len(B) else []; I = max(len(a), len(b))
        for i in range(I):
            x = a[i] if i < len(a) else R.zero; y = b[i] if i < len(b) else R.zero; tot += abs(R.to_float(x - y))
    return tot
t0 = time.time(); acc = None; snaps = {}; mass_in = {}
pairs = sorted(range(1, n), key=lambda i: (min(i, n - i), i))
fn = L.f[n]; fn_l1 = l1(fn); print(f'n = {n}, ||f_n||_l1 = {fn_l1:.6e} (log10 {math.log10(fn_l1):.4f}); pairs {len(pairs)}', flush=True)
done_L = set()
for idx, i in enumerate(pairs):
    j = n - i; m = min(i, j)
    Gi = L.g[i]; Fj = L.f[j]; Pi = L.p(i) + 1; pj = L.p(j)
    Gt = col_add(R, col_scale(R, Gi, Pi), col_T(R, Gi)); Ft = col_add(R, col_scale(R, Fj, pj), col_T(R, Fj))
    term = L._block_products(Gt, Fj, Gi, Ft)
    acc = term if acc is None else col_add(R, acc, term)
    nxt_m = min(pairs[idx + 1], n - pairs[idx + 1]) if idx + 1 < len(pairs) else None
    for Lv in Ls:
        if Lv not in done_L and (nxt_m is None or nxt_m > Lv) and m <= Lv:
            fL = lin_solve(acc); eps = l1diff(fn, fL) / fn_l1; done_L.add(Lv)
            print(f'  L = {Lv:3d}: pairs with min(i,j) <= L: {2 * Lv if 2 * Lv < n else n - 1:3d}; eps_n(L) = ||f_n - f_n^(L)||_1/||f_n||_1 = {eps:.4e}; ||f_n^(L)||_1/||f_n||_1 = {l1(fL) / fn_l1:.6f}   [{time.time() - t0:.0f} s]', flush=True)
fL = lin_solve(acc); print(f'  full: eps = {l1diff(fn, fL) / fn_l1:.3e} (consistency of the recomputation with the stored order; nonzero only by rounding/summation order)   [{time.time() - t0:.0f} s]')
