"""Hump report for a canonical log-series log: for each order n >= n0 print the position k and value of
max_{k>=1} log10(k! c_k / c_0) (density) and the same for the stream columns, plus M_n^{1/n} and the log degree.
usage: hump_report.py LOG [n0] [every]"""
import json, sys, math
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
st = {r['n']: r for r in rows if 'n' in r and 'log10_col_l1' in r}
n0 = int(sys.argv[2]) if len(sys.argv) > 2 else 180; every = int(sys.argv[3]) if len(sys.argv) > 3 else 5
print(f"{'n':>4} {'deg':>3} {'M_n^(1/n)':>9} {'k*':>3} {'max log10(k!c_k/c_0)':>21} {'k*g':>3} {'max log10(k!g_k/g_0)':>21}  log10(k! c_k/c_0) at k = 1, 10, 20, 30, 40, 50, 60")
for n in sorted(st):
    if n < n0 or (n % every and n != max(st)): continue
    r = st[n]; cols = r['log10_col_l1']
    kc = [c + math.log10(math.factorial(k)) - cols[0] for k, c in enumerate(cols)]
    kstar = max(range(1, len(kc)), key=lambda k: kc[k]) if len(kc) > 1 else 0
    g = r.get('log10_gcol_l1'); 
    if g:
        kg = [c + math.log10(math.factorial(k)) - g[0] for k, c in enumerate(g)]; ks = max(range(1, len(kg)), key=lambda k: kg[k]) if len(kg) > 1 else 0
    else: kg, ks = None, None
    prof = ' '.join(f"{kc[k]:6.2f}" if k < len(kc) else '   -  ' for k in (1, 10, 20, 30, 40, 50, 60))
    print(f"{n:4d} {r['Kt']:3d} {10**(r['log10_sum_cols']/n):9.5f} {kstar:3d} {kc[kstar]:21.3f} {ks if ks is not None else -1:3d} {kg[ks] if kg else float('nan'):21.3f}  {prof}")
