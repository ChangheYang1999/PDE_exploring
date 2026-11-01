"""Absolute upward-channel Poisson transfer of the actual density (lead).
For saved long-double arrays F_n (axis 0: complex frequency -M..M, axis 1: power q of t) at delta = A/B, unit
amplitude amp, compute for each stream column j the absolute bound
  T_j = (1/2) sum_m sum_{q>=j} |F_{n,m,q}| q! / (j! |s_m|^{q-j+1}),   s_m = |m| + 3 - n delta (upward Poisson factor),
i.e. what the upward channel (d_t + s_m)^{-1} of the polynomial Poisson inverse can produce at most from the actual
F_n with no cancellation, and compare with the actual stream column norms ||[t^j] G_n||_l1. Also report the share of
T_0 coming from modes with |s_m| <= q/4 (near the diagonal).
Usage: poisson_transfer.py A B amp dir n1 n2 ..."""
import sys, math
import numpy as np
A, B, amp, d = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
delta = A / B
for n in map(int, sys.argv[5:]):
    F = np.load('%s/F_%d.npy' % (d, n)); G = np.load('%s/G_%d.npy' % (d, n))
    M = (F.shape[0] - 1) // 2
    m = np.abs(np.arange(-M, M + 1)).astype(np.longdouble)
    s = np.abs(m + 3 - np.longdouble(n * delta))
    aF = np.abs(F); aG = np.abs(G)
    K = F.shape[1]
    lam = np.log10(amp) * n
    print('n=%d  deg F=%d  min|s|=%.4f' % (n, K - 1, float(s[aF.sum(axis=1) > 0].min())))
    for j in (0, 1, 2, 5, 10, 20, 30, 40, 50):
        if j >= K:
            break
        T = np.longdouble(0); Tnear = np.longdouble(0); worst = (-1e9, None)
        for q in range(j, K):
            fac = np.exp(np.longdouble(math.lgamma(q + 1) - math.lgamma(j + 1)))
            w = aF[:, q] * fac / s ** (q - j + 1)
            T += w.sum()
            if q > 0:
                Tnear += w[s <= q / 4].sum()
            k = int(np.argmax(w))
            lw = float(np.log10(w[k])) if w[k] > 0 else -1e9
            if lw > worst[0]:
                worst = (lw, (q, int(m[k]), float(s[k])))
        T *= 0.5; Tnear *= 0.5
        gj = float(np.log10(aG[:, j].sum())) - lam if j < G.shape[1] else float('nan')
        print('  j=%2d log10 T_j=%9.3f actual G_j=%9.3f  ratio=%7.3f  near share=%.3e  worst (q,|m|,|s|)=%s' %
              (j, float(np.log10(T)) - lam, gj, float(np.log10(T)) - lam - gj, float(Tnear / T), worst[1]))
