"""Markdown table for section 5.11b: orders n_from..n_to of the reset-radii continuation (NEW log) against the first, precision-trimmed
continuation (OLD log): log10 M_n, log10 N_n, log10(N/M), class n mod 3, increment of log10 M_n, hump maximum over k >= 1 of log10(k! c_k/c_0)
with its k*, log10 of the norm-relative radius of the new run, the old midpoint values and their radii, and the differences new - old.
usage: table_511b.py NEW_LOG OLD_LOG n_from n_to"""
import json, sys, math
def load(path):
    st = {}
    for l in open(path):
        if not l.strip(): continue
        d = json.loads(l)
        if 'n' in d and 'log10_col_l1' in d: st[d['n']] = d
    return st
def lse(v):
    v = [x for x in v if x is not None and x > -1e300]; m = max(v); return m + math.log10(sum(10.0 ** (x - m) for x in v))
def hump(cols):
    best = None
    for k, c in enumerate(cols):
        if k == 0 or c is None or c < -1e300: continue
        val = c - cols[0] + math.lgamma(k + 1) / math.log(10)
        if best is None or val > best[0]: best = (val, k)
    return best
new, old = load(sys.argv[1]), load(sys.argv[2]); a, b = int(sys.argv[3]), int(sys.argv[4])
print('| n | class | log10 M_n (new) | incr | log10 N_n (new) | log10 N/M | hump max (k*) | log10 rad (new) | log10 M_n (old) | log10 rad (old) | new - old (M) |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
prev = None
for n in range(a, b + 1):
    if n not in new: continue
    r = new[n]; M = lse(r['log10_col_l1']); N = lse(r['log10_gcol_l1']); h = hump(r['log10_col_l1'])
    rad = r.get('log10_rad_over_max'); inc = f'{M - prev:+.3f}' if prev is not None else ''
    o = old.get(n); oM = lse(o['log10_col_l1']) if o else None; orad = o.get('log10_rad_over_max') if o else None
    print(f"| {n} | {n % 3} | {M:.3f} | {inc} | {N:.3f} | {N - M:+.3f} | {h[0]:+.2f} ({h[1]}) | {rad:.1f} | " + (f"{oM:.3f} | {orad:.1f} | {M - oM:+.1e} |" if o else "| | |"))
    prev = M
