"""Per-order growth of a tuned run (section 5.13c): log10 ||f_n||_l1 and 10-order slopes at n = n0, n0+10, ..., N, the tuned H_n and response sigma_k
nearest below n, the mean slope over [n1, N] (straight-line growth constant A = 10^slope and apparent radius A^(1/delta)), and the smallest |sigma_k|.
usage: single_slopes.py TAG [n0=100] [n1=100]"""
import json, sys, os, math
from fractions import Fraction
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tag = sys.argv[1]; n0 = int(sys.argv[2]) if len(sys.argv) > 2 else 100; n1 = int(sys.argv[3]) if len(sys.argv) > 3 else 100
rows = [json.loads(l) for l in open(os.path.join(LANE, 'logs', tag + '.jsonl')) if l.strip()]
hdr = rows[0]; delta = Fraction(hdr['delta']); P = hdr['period']
st = {r['n']: r for r in rows if 'n' in r and 'log10_l1' in r}; N = max(st)
H = json.load(open(os.path.join(LANE, 'ckpt', tag + '_H.json')))
def mid(s): return float(s.strip('[').split(' +/-')[0])
sig = {int(k): mid(v) for k, v in H['sigma'].items()}; Hs = {int(k): v['mid'] for k, v in H['H'].items()}
print(f"{tag}: delta = {delta}, period {P}, N = {N}, f1 = {hdr['f1']}")
print('   n  log10|f_n|_1  10-order slope   nearest H_n (log10|H|)   sigma_k')
for n in range(n0, N + 1, 10):
    if n not in st or n - 10 not in st: continue
    s = (st[n]['log10_l1'] - st[n - 10]['log10_l1']) / 10
    hn = max((k for k in Hs if k <= n), default=None)
    htxt = f"H_{hn}: {math.log10(abs(Hs[hn])):8.3f}   sigma_{hn // P}: {sig[hn]:+.4e}" if hn else ''
    print(f"{n:5d} {st[n]['log10_l1']:12.3f} {s:+.4f}          {htxt}")
sl = (st[N]['log10_l1'] - st[n1]['log10_l1']) / (N - n1); A = 10 ** sl
print(f"mean slope {n1}..{N}: {sl:+.4f} per order -> A = {A:.4f}, apparent radius A^(1/delta) = {A ** float(1 / delta):.4g} (unit amplitude)")
print(f"root test ||f_N||^(1/N) = {10 ** (st[N]['log10_l1'] / N):.4f}; smallest |sigma_k| = {min(abs(v) for v in sig.values()):.4e} at n = {min(sig, key=lambda k: abs(sig[k]))}; sigma_k, k = 1..: " + ' '.join(f"{sig[k]:+.3e}" for k in sorted(sig)[:12]) + ' ...')
