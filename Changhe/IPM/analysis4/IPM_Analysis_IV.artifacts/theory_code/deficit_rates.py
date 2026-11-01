"""Empirical growth rate of fixed logarithmic deficits at delta = 2/3, f_1 = amp*sin(theta) (lead).
Reads a long-double log (fields n, lcol = log10 of the l1 norms of the t^q columns of f_n at amplitude amp) and prints,
for residue r (n = 3k + r) and deficit d (q = k - 1 - d), the per-block increment of log10(q! ||[t^q] f_n||) at unit
amplitude, averaged over the last W blocks ending at k. Compare with log10 lambda = log10(157/129600) = -2.9168 (d = 0,
proved) and the proved upper bound log10((d+1) lambda).
Usage: deficit_rates.py file.jsonl amp r W"""
import sys, json, math
rows = {}
for l in open(sys.argv[1]):
    d = json.loads(l)
    rows[d['n']] = d
amp, r, W = float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
la = math.log10(amp)
lam = math.log10(157 / 129600)


def val(k, d):
    n = 3 * k + r
    q = k - 1 - d
    if n not in rows or q < 0 or q >= len(rows[n]['lcol']):
        return None
    v = rows[n]['lcol'][q]
    if v is None or v == float('-inf'):
        return None
    return v - n * la + math.lgamma(q + 1) / math.log(10)


ks = sorted(set((n - r) // 3 for n in rows if (n - r) % 3 == 0))
kmax = max(ks)
DS = [0, 1, 2, 3, 5, 8, 10, 15, 20, 25, 30, 40, 50, 60]
print('r=%d, increments per block (3 orders) of log10(q! c_q), q = k-1-d, window %d blocks' % (r, W))
print('bound log10((d+1)lambda):', ' '.join('d%d:%.3f' % (d, lam + math.log10(d + 1)) for d in DS))
print('k    ' + ' '.join('%7s' % ('d%d' % d) for d in DS))
for k in range(20, kmax + 1, 10):
    out = []
    for d in DS:
        a, b = val(k, d), val(k - W, d)
        out.append('%7.3f' % ((a - b) / W) if a is not None and b is not None else '     --')
    print('%-4d ' % k + ' '.join(out))
print('values log10(q! c_q) at unit amplitude')
for k in range(20, kmax + 1, 10):
    out = []
    for d in DS:
        a = val(k, d)
        out.append('%7.1f' % a if a is not None else '     --')
    print('%-4d ' % k + ' '.join(out))
