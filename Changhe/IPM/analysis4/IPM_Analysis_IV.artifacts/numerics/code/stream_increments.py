"""Stream and density increments for a canonical log-series log: N_n = sum_k ||g_{n,k}||_l1 (stream), M_n (density);
increments i_n = log10 N_n - log10 N_{n-1}; 9-order window means ending at n, overall and by residue class of n mod 3.
usage: stream_increments.py LOG [n0] [every]"""
import json, sys, math
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
st = {r['n']: r for r in rows if 'n' in r and 'log10_gcol_l1' in r}
n0 = int(sys.argv[2]) if len(sys.argv) > 2 else 180; every = int(sys.argv[3]) if len(sys.argv) > 3 else 10
def lsum(cols):
    fin = [c for c in cols if c > -1e9]; m = max(fin); return math.log10(sum(10 ** (c - m) for c in fin)) + m
LN = {n: lsum(st[n]['log10_gcol_l1']) for n in st}; LM = {n: st[n]['log10_sum_cols'] for n in st}
print(f"{'n':>4} {'log10 N_n':>10} {'incr N':>8} {'9-mean N':>9} {'class0':>8} {'class1':>8} {'class2':>8} {'9-mean M':>9}")
for n in sorted(st):
    if n < n0 or (n % every and n != max(st)): continue
    if n - 9 not in LN: continue
    inc = {m: LN[m] - LN[m - 1] for m in range(n - 8, n + 1) if m - 1 in LN}
    incM = {m: LM[m] - LM[m - 1] for m in range(n - 8, n + 1) if m - 1 in LM}
    cls = [sum(v for m, v in inc.items() if m % 3 == r) / max(1, sum(1 for m in inc if m % 3 == r)) for r in range(3)]
    print(f"{n:4d} {LN[n]:10.2f} {inc[n]:8.4f} {sum(inc.values())/len(inc):9.4f} {cls[0]:8.4f} {cls[1]:8.4f} {cls[2]:8.4f} {sum(incM.values())/len(incM):9.4f}")
