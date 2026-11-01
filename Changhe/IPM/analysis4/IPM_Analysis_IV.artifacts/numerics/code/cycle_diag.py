"""Signed-vector diagnostics of the period-3 cycle of the canonical 2/3 log series (astra referee, 15:00Z):
for x_n = F_n (density) and G_n (stream), as float arrays over (log column q, mode index i) with zero padding of new columns/modes,
  a_n = <x_(n-3), x_n> / ||x_(n-3)||_2^2,   e_n = ||x_n - a_n x_(n-3)||_2 / ||x_n||_2,   e1_n = the same residual in l1 relative to ||x_n||_1,
in two alignments: raw mode indices, and resonance-shifted (x_(n-3)[q][i-1] against x_n[q][i]: the resonant frequency moves by one mode index per period).
Fixed-reference projections per residue class s = n mod 3: v_s = x_(n_ref(s)) / ||.||_2 (first order >= n_ref0 in the class), aligned by the
resonance shift (n - n_ref)/3: b_n = <v_s, x_n>, w_n = x_n - b_n v_s, reported as ||w_n||_2 / ||x_n||_2 and the period ratios b_n / b_(n-3).
Column migration: mean column index weighted by the column l1 masses and the mass fraction in the newest 5 columns (from the stored statistics).
usage: cycle_diag.py CKPT n0 n1 [n_ref0=333]"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from logff import *
L = LogFarField.load(sys.argv[1]); R = L.R
n0, n1 = int(sys.argv[2]), int(sys.argv[3]); nref0 = int(sys.argv[4]) if len(sys.argv) > 4 else 333
def to_float_matrix(cols, scale_log10):
    """columns of arb balls -> float matrix (q, i) of midpoints divided by 10^scale_log10"""
    Q = len(cols); I = max(len(c) for c in cols); M = np.zeros((Q, I))
    sc = arb(10) ** (-scale_log10)
    for q, c in enumerate(cols):
        for i, x in enumerate(c):
            M[q, i] = R.to_float(x * sc)
    return M
def pad(A, shape):
    B = np.zeros(shape); B[:A.shape[0], :A.shape[1]] = A; return B
def shift_modes(A, k):
    """shift mode index by k (A[q][i] -> position i + k), zero fill"""
    B = np.zeros_like(A)
    if k >= 0: B[:, k:] = A[:, :A.shape[1] - k] if k < A.shape[1] else 0
    else: B[:, :A.shape[1] + k] = A[:, -k:]
    return B
cache = {}
def vec(n, which):
    key = (n, which)
    if key not in cache:
        cols = L.f[n] if which == 'F' else L.g[n]; stats = L.stats[n]
        scale = max(stats['log10_col_l1']) if which == 'F' else max(stats['log10_gcol_l1'])
        cache[key] = (to_float_matrix(cols, scale), scale)
    return cache[key]
print(f"{'n':>4} {'cls':>3} {'which':>5} {'a_n raw':>11} {'e2 raw':>8} {'e1 raw':>8} {'a_n shift':>11} {'e2 shift':>9} {'e1 shift':>9} {'|w|/|x| ref':>12} {'b_n/b_(n-3)':>12} {'meancol':>8} {'new5':>6}")
refs = {}
for n in range(n0, n1 + 1):
    if n not in L.f or n - 3 not in L.f: continue
    for which in ('F', 'G'):
        A, sa = vec(n - 3, which); B, sb = vec(n, which)
        shape = (max(A.shape[0], B.shape[0]), max(A.shape[1], B.shape[1]) + 1)
        A = pad(A, shape) * 10.0 ** (sa - sb); B = pad(B, shape)        # both now in units of 10^sb
        out = []
        for align in (0, 1):
            As = shift_modes(A, align)
            a = float((As * B).sum() / (As * As).sum()); res = B - a * As
            out += [a, float(np.linalg.norm(res) / np.linalg.norm(B)), float(np.abs(res).sum() / np.abs(B).sum())]
        s = n % 3
        if (s, which) not in refs and n >= nref0:
            refs[(s, which)] = (n, B / np.linalg.norm(B), sb, None)
        wn = bn_ratio = float('nan')
        if (s, which) in refs:
            nr, V, sr, bprev = refs[(s, which)]; k = (n - nr) // 3
            Vs = pad(shift_modes(pad(V, (max(V.shape[0], B.shape[0]), max(V.shape[1], B.shape[1]) + k + 1)), k), (max(V.shape[0], B.shape[0]), max(V.shape[1], B.shape[1]) + k + 1))
            Bp = pad(B, Vs.shape); b = float((Vs * Bp).sum()); w = Bp - b * Vs; wn = float(np.linalg.norm(w) / np.linalg.norm(Bp))
            bn = b * 10.0 ** sb      # absolute scale (log10 units handled by the ratio below)
            if bprev is not None: bn_ratio = bn / bprev
            refs[(s, which)] = (nr, V, sr, bn)
        st = L.stats[n]; cl = np.array(st['log10_col_l1'] if which == 'F' else st['log10_gcol_l1']); cl = cl[np.isfinite(cl)]
        w = 10.0 ** (cl - cl.max()); meancol = float((w * np.arange(len(w))).sum() / w.sum()); new5 = float(w[-5:].sum() / w.sum())
        print(f"{n:4d} {s:3d} {which:>5} {out[0]:+11.3e} {out[1]:8.3f} {out[2]:8.3f} {out[3]:+11.3e} {out[4]:9.3f} {out[5]:9.3f} {wn:12.3f} {bn_ratio:+12.3e} {meancol:8.2f} {new5:6.3f}", flush=True)
