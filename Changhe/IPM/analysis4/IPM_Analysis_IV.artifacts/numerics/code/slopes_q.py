"""Lead request (q), 07:31Z (plain sums recomputed from the per-column l1 fields when the live log lacks them): per-order log10 N_n (stream plain sum), log10 M_n (density plain sum), their ratio log10(N/M), and
27-order least-squares regression slopes of log10 M_n and log10 N_n ending at given orders. Works on a regenerated log (fields
log10_sum_cols and log10_sum_gcols present). usage: slopes_q.py LOG n_from n_to end1,end2,..."""
import json, sys, math
import numpy as np
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
def _lse10(v):
    v = [x for x in v if x is not None and x > -1e300]
    if not v: return None
    m = max(v); return m + math.log10(sum(10.0 ** (x - m) for x in v))
st = {}
for r in rows:                      # later rows (resumed runs) override earlier ones for the same order
    if 'n' not in r: continue
    if 'log10_sum_cols' not in r and 'log10_col_l1' in r: r['log10_sum_cols'] = _lse10(r['log10_col_l1'])
    if 'log10_sum_gcols' not in r and 'log10_gcol_l1' in r: r['log10_sum_gcols'] = _lse10(r['log10_gcol_l1'])
    if r.get('log10_sum_cols') is not None and r.get('log10_sum_gcols') is not None: st[r['n']] = r
n_from, n_to = int(sys.argv[2]), int(sys.argv[3]); ends = [int(x) for x in sys.argv[4].split(',')]
print(f"{'n':>4} {'log10 M_n':>10} {'log10 N_n':>10} {'log10 N/M':>10} {'midpoint_only':>13}")
for n in range(n_from, n_to + 1):
    if n in st:
        r = st[n]; print(f"{n:4d} {r['log10_sum_cols']:10.3f} {r['log10_sum_gcols']:10.3f} {r['log10_sum_gcols']-r['log10_sum_cols']:10.3f} {str(r.get('midpoint_only')):>13}")
print('27-order regression slopes (per order) ending at n:')
for e in ends:
    ns = [n for n in range(e - 26, e + 1) if n in st]
    if len(ns) < 27: print(f"  end {e}: only {len(ns)} orders available"); continue
    x = np.array(ns, float); M = np.array([st[n]['log10_sum_cols'] for n in ns]); N = np.array([st[n]['log10_sum_gcols'] for n in ns])
    sM = np.polyfit(x, M, 1)[0]; sN = np.polyfit(x, N, 1)[0]
    print(f"  end {e}: slope log10 M = {sM:.5f}, slope log10 N = {sN:.5f}, difference N-M = {sN-sM:+.5f}")
