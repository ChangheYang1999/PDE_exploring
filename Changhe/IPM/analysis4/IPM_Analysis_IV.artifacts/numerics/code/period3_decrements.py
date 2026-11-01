"""3-order decrements of the plain sums of the canonical 2/3 log series (period-3 cycle, section 5.11b (b3)):
for every class-0 order n (n = 0 mod 3) in [n_from, n_to - 3] print log10 M_(n+3) - log10 M_n and the same for N (stream),
and the root tests at n_to. Plain sums are recomputed from the per-column l1 fields when the sum fields are absent.
usage: period3_decrements.py LOG n_from n_to"""
import json, sys, math
def lse(v):
    v = [x for x in v if x is not None and x > -1e300]; m = max(v); return m + math.log10(sum(10.0 ** (x - m) for x in v))
st = {}
for l in open(sys.argv[1]):
    if not l.strip(): continue
    d = json.loads(l)
    if 'n' not in d or 'log10_col_l1' not in d: continue
    d['M'] = d.get('log10_sum_cols') if d.get('log10_sum_cols') is not None else lse(d['log10_col_l1'])
    d['N'] = d.get('log10_sum_gcols') if d.get('log10_sum_gcols') is not None else (lse(d['log10_gcol_l1']) if 'log10_gcol_l1' in d else None)
    st[d['n']] = d          # later rows win
a, b = int(sys.argv[2]), int(sys.argv[3])
for n in range(a, b - 2):
    if n % 3 == 0 and n in st and n + 3 in st:
        dN = f"{st[n+3]['N'] - st[n]['N']:+.3f}" if st[n]['N'] is not None and st[n+3]['N'] is not None else 'n/a'
        print(f"{n} -> {n+3}: M {st[n+3]['M'] - st[n]['M']:+.3f}   N {dN}")
if b in st:
    print(f"root tests at {b}: density {10 ** (st[b]['M'] / b):.4f}, stream {10 ** (st[b]['N'] / b):.4f} (log10 M {st[b]['M']:.3f}, log10 N {st[b]['N']:.3f})")
