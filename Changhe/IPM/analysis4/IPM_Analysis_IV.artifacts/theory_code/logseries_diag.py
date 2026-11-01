"""Diagnostics for the canonical logarithmic series (lead). Runs the unmodified recursion of code/logseries.py
(double) or code/logseries_ld.py (x87 long double), with f_1 = amp*sin(theta), writing the basic per-order column
norms while running (out_basic) and, at the end, per order n (out_diag):
  lcol   : log10 of the l1 norm over frequency of each t-power coefficient of f_n,
  lgcol  : the same for the stream g_n,
  lnear  : log10 of the density l1 mass per t-power in the near-resonant channels, i.e. density frequencies 2j-1 that
           feed a nonresonant stream mode j with |2j + P_n| < 1 (the small first-order Poisson factor),
  lborel : log of sum over those channels and t-powers of k! |v|^(-k) |a_{2j-1,k}|, v = 2j + P_n (natural log),
  cent   : l1-weighted mean |frequency| / n of each t-power coefficient of f_n.
Unit-amplitude values: subtract n*log10(amp) from every log10 field (lborel: n*log(amp)).
Usage: logseries_diag.py d|ld A B N amp out_basic.jsonl out_diag.jsonl"""
import sys, json, time, math
import numpy as np
from fractions import Fraction
sys.path.insert(0, 'code')

mode, A, Bd, N, amp, out_basic, out = (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),
                                       float(sys.argv[5]), sys.argv[6], sys.argv[7])
if mode == 'ld':
    import logseries_ld as LS
else:
    import logseries as LS
dl = Fraction(A, Bd)
open(out_basic, 'w').close()
open(out, 'w').close()


def l10(x):
    return float(np.log10(x)) if x > 0 else None


def stats_for(n, f, g):
    M = f.shape[0] // 2
    freqs = np.arange(-M, M + 1)
    Pn = 2 - n * dl
    K = f.shape[1]
    near = [0] * K
    lborel = -math.inf
    w = np.abs(f)
    for idx in range(M + 1, 2 * M + 1):
        l = int(freqs[idx])
        j = (l + 1) // 2
        v = 2 * j + Pn
        if v == 0 or abs(v) >= 1:
            continue
        a = w[idx, :] * 2  # real sine amplitude = 2|c_l|
        vf = abs(float(v))
        for k in range(K):
            x = a[k]
            near[k] = near[k] + x
            if x > 0:
                lv = float(np.log(x)) + math.lgamma(k + 1) - k * math.log(vf)
                if lborel == -math.inf:
                    lborel = lv
                else:
                    hi, lo = max(lborel, lv), min(lborel, lv)
                    lborel = hi + math.log1p(math.exp(lo - hi))
    cent = []
    af = np.abs(freqs)
    for k in range(K):
        s = w[:, k].sum()
        cent.append(float((w[:, k] * af).sum() / s / n) if s > 0 else 0.0)
    return dict(lnear=[l10(x) for x in near], lborel=lborel, cent=cent,
                lgcol=[l10(x) for x in np.abs(g).sum(axis=0)], lcol=[l10(x) for x in w.sum(axis=0)])


t0 = time.time()
F, G, st, res = LS.run(A, Bd, {1: amp}, N, out=out_basic)
print('run time', time.time() - t0, flush=True)
with open(out, 'a') as fh:
    for n in range(2, N + 1):
        d = stats_for(n, F[n], G[n])
        d.update(n=n)
        fh.write(json.dumps(d) + '\n')
print('done', time.time() - t0, flush=True)
