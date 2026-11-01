"""Per-order table of the canonical logarithmic series from a logff log: M_n = sum_k ||f_{n,k}||_l1, c_k = ||f_{n,k}||_l1,
k! c_k, t-degree, and M_n^{1/n}. usage: logseries_table.py LOG [every]  -> prints and writes notes/<tag>_table.json"""
import sys, os, json, math
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]; hdr = rows[0]
st = {r['n']: r for r in rows if 'n' in r and 'log10_col_l1' in r}; N = max(st); every = int(sys.argv[2]) if len(sys.argv) > 2 else 10
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); tag = os.path.basename(sys.argv[1]).replace('.jsonl', '')
out = []
print(f"{sys.argv[1]}: delta={hdr.get('delta')} c_l={hdr.get('c_l')} f1={hdr.get('f1')} N={N}; canonical normalization B_(n,j)(0) = 0")
print(f"{'n':>4} {'deg':>3} {'log10 M_n':>10} {'M_n^(1/n)':>9} {'log10 c_k (k=0..deg)':>50}  {'max_k log10(k! c_k/c_0)':>22} {'max_k log10(k! g_k/g_0)':>22}")
for n in sorted(st):
    r = st[n]; cols = r['log10_col_l1']; M = r['log10_sum_cols']
    kc = [c + math.log10(math.factorial(k)) - cols[0] for k, c in enumerate(cols) if c > -1e9]
    rec = {'n': n, 'deg': r['Kt'], 'log10_M_n': M, 'M_n_root': 10 ** (M / n), 'log10_c_k': cols, 'log10_kfact_c_k_over_c_0': kc, 'maxfreq': r['maxfreq'], 'rad_over_max': r.get('rad_over_max'), 'log10_rad_over_max': r.get('log10_rad_over_max')}
    if 'log10_gcol_l1' in r:
        g = r['log10_gcol_l1']; rec['log10_g_k'] = g; rec['g_deg'] = r.get('gKt'); rec['log10_kfact_g_k_over_g_0'] = [c + math.log10(math.factorial(k)) - g[0] for k, c in enumerate(g) if c > -1e9]
    out.append(rec)
    if n % every == 0 or n == N or n <= 3:
        gk = rec.get('log10_kfact_g_k_over_g_0', [])
        print(f"{n:4d} {r['Kt']:3d} {M:10.2f} {10**(M/n):9.5f} {' '.join(f'{c:6.2f}' for c in cols[:8]):>50}  {max(kc[1:]) if len(kc)>1 else float('nan'):22.3f} {max(gk[1:]) if len(gk)>1 else float('nan'):22.3f}")
json.dump({'header': hdr, 'rows': out, 'note': 'c_k = l1 norm over frequencies of the coefficient of (log r)^k in f_n; M_n = sum_k c_k; canonical normalization B_(n,j)(0) = 0 (free multipole constants zero)'}, open(os.path.join(LANE, 'notes', tag + '_table.json'), 'w'), indent=1)
