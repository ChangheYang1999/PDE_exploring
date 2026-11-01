"""Mass of the logarithmic coefficients by distance to the Poisson diagonal (lead).
For a saved long-double array h (axis 0: complex Fourier frequency -M..M, axis 1: power q of t = log r) at order n and
delta = A/B, unit amplitude amp, split the l1 mass of each column [t^q] by the upward Poisson factor
  density (odd m):  s = |m| + 3 - n delta,      stream (even m):  s = |m| + 2 - n delta,
into the bands |s| <= q/4, q/4 < |s| <= q, |s| > q (for q = 0: |s| <= 2 and |s| > 2).
Usage: diag_decomp.py A B amp dir n1 n2 ...   (reads dir/F_n.npy, dir/G_n.npy)."""
import sys, math
import numpy as np
A, B, amp, d = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
delta = A / B
for n in map(int, sys.argv[5:]):
    for name, sh in (('F', 3.0), ('G', 2.0)):
        try:
            h = np.load('%s/%s_%d.npy' % (d, name, n))
        except FileNotFoundError:
            continue
        M = (h.shape[0] - 1) // 2
        m = np.abs(np.arange(-M, M + 1)).astype(float)
        s = m + sh - n * delta
        lam = np.log10(amp) * n
        absh = np.abs(h).astype(np.float64) if False else np.abs(h)
        rows = []
        for q in range(h.shape[1]):
            col = absh[:, q]
            tot = col.sum()
            if tot == 0:
                continue
            if q == 0:
                bands = [col[np.abs(s) <= 2].sum(), 0 * tot, col[np.abs(s) > 2].sum()]
            else:
                bands = [col[np.abs(s) <= q / 4].sum(), col[(np.abs(s) > q / 4) & (np.abs(s) <= q)].sum(), col[np.abs(s) > q].sum()]
            lt = float(np.log10(tot)) - lam
            lfact = lt + math.lgamma(q + 1) / math.log(10)
            # mass-weighted mean of s
            ms = float((col * s).sum() / tot)
            rows.append((q, lt, lfact, [float(b / tot) for b in bands], ms))
        qmax = max(rows, key=lambda r: r[2])[0]
        print('%s n=%d  deg=%d  argmax_q q!c_q = %d' % (name, n, h.shape[1] - 1, qmax))
        for r in rows:
            if r[0] in (0, 1, 2, 5, 10) or r[0] % 10 == 0 or r[0] == qmax or r[0] >= h.shape[1] - 3:
                print('  q=%3d log10 c_q=%9.3f log10 q!c_q=%9.3f  near=%.3f mid=%.3f far=%.3f  mean s=%7.2f' %
                      (r[0], r[1], r[2], r[3][0], r[3][1], r[3][2], r[4]))
