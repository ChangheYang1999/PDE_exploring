"""Standing-request summary for the canonical 2/3 log run at a given order (lead's items (i), (n), (q)):
hump maxima max_{k>=1} log10(k! c_k/c_0) with k* (density, stream), column profile at k = 1, 10, ..., 60, plain log10 M_n, N_n, N/M,
9-order-window stream increments by residue class mod 3, weighted factorial norm W_n = log10 sum_q q! 12^q ||[t^q]F_n|| with its
10- and 30-order increments, 27-order regression slopes ending at n, and the midpoint-only flag.
usage: report_order.py LOG n [n_from]   (prints the per-order block for n_from..n and the summaries at n)"""
import json, sys, math
import numpy as np
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
def lse(v):
    v = [x for x in v if x is not None and x > -1e300]
    if not v: return None
    m = max(v); return m + math.log10(sum(10.0 ** (x - m) for x in v))
st = {}
for r in rows:
    if 'n' not in r or 'log10_col_l1' not in r: continue
    r['M'] = lse(r['log10_col_l1']); r['N'] = lse(r.get('log10_gcol_l1', []))
    st[r['n']] = r
n = int(sys.argv[2]); n_from = int(sys.argv[3]) if len(sys.argv) > 3 else n - 9
def hump(cols):
    best = (-1e9, None)
    for k, c in enumerate(cols):
        if k == 0 or c is None or c < -1e300: continue
        v = math.lgamma(k + 1) / math.log(10) + c - cols[0]
        if v > best[0]: best = (v, k)
    return best
def W(cols, w=12.0):
    return lse([math.lgamma(q + 1) / math.log(10) + q * math.log10(w) + c for q, c in enumerate(cols) if c is not None and c > -1e300])
print(f"{'n':>4} {'log10 M':>9} {'log10 N':>9} {'N/M':>7} {'hump F':>8} {'k*':>3} {'hump G':>8} {'k*':>3} {'deg':>4} {'W_F':>9} {'W_G':>9} {'mid-only':>8} {'rad':>7}")
for m in range(n_from, n + 1):
    if m not in st: continue
    r = st[m]; hf, kf = hump(r['log10_col_l1']); hg, kg = hump(r.get('log10_gcol_l1', [None]))
    print(f"{m:4d} {r['M']:9.3f} {r['N']:9.3f} {r['N']-r['M']:7.3f} {hf:8.3f} {kf:3d} {hg:8.3f} {kg:3d} {r['Kt']:4d} {W(r['log10_col_l1']):9.3f} {W(r['log10_gcol_l1']):9.3f} {str(r.get('midpoint_only')):>8} {r.get('log10_rad_over_max', float('nan')):7.2f}")
r = st[n]; cols = r['log10_col_l1']
print('profile log10(k! c_k/c_0) at k = 1, 10, 20, 30, 40, 50, 60, 70, 80 (density):',
      ' '.join(f"{(math.lgamma(k+1)/math.log(10) + cols[k] - cols[0]):.2f}" if k < len(cols) else '-' for k in [1,10,20,30,40,50,60,70,80]))
gc = r['log10_gcol_l1']
print('profile (stream):', ' '.join(f"{(math.lgamma(k+1)/math.log(10) + gc[k] - gc[0]):.2f}" if k < len(gc) else '-' for k in [1,10,20,30,40,50,60,70,80]))
# 9-window stream increments by class, ending at n, n-3, n-6
def win(e, key):
    inc = {m: st[m][key] - st[m-1][key] for m in range(e-8, e+1) if m in st and m-1 in st}
    if len(inc) < 9: return None
    allm = np.mean(list(inc.values())); cl = [np.mean([v for m, v in inc.items() if m % 3 == c]) for c in (0,1,2)]
    return allm, cl
for e in [n-6, n-3, n]:
    w = win(e, 'N'); wm = win(e, 'M')
    if w: print(f"9-window ending {e}: stream mean {w[0]:.3f} (class0 {w[1][0]:.3f}, class1 {w[1][1]:.3f}, class2 {w[1][2]:.3f}); density mean {wm[0]:.3f}")
for span in (10, 30):
    if n - span in st:
        wf = (W(st[n]['log10_col_l1']) - W(st[n-span]['log10_col_l1'])) / span; wg = (W(st[n]['log10_gcol_l1']) - W(st[n-span]['log10_gcol_l1'])) / span
        mf = (st[n]['M'] - st[n-span]['M']) / span; mg = (st[n]['N'] - st[n-span]['N']) / span
        print(f"{span}-order increments per order ending {n}: W_F {wf:.4f}, W_G {wg:.4f}; plain M {mf:.4f}, N {mg:.4f}")
ns = [m for m in range(n-26, n+1) if m in st]
if len(ns) == 27:
    x = np.array(ns, float); sM = np.polyfit(x, [st[m]['M'] for m in ns], 1)[0]; sN = np.polyfit(x, [st[m]['N'] for m in ns], 1)[0]
    print(f"27-order regression slopes ending {n}: M {sM:.5f}, N {sN:.5f}, difference {sN-sM:+.5f}")
