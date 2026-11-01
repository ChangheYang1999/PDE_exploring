"""Lead request: per-deficit rates. For delta = 2/3 blocks n = 3k + r (r = 0, 1, 2), the top log degree is kappa_n = floor((n-1)/3) = k-1
for r = 1, 2 (k-1 for r=1,2; k-1 for r = 0 gives (3k-1)/3 -> k-1). Deficit d: column index q = kappa_n - d. Rate per block =
log10((q)! ||[t^q] f_{3(k+1)+r}||) - log10((q')! ||[t^{q'}] f_{3k+r}||) with q' = kappa_{3k+r} - d, q = kappa_{3k+3+r} - d.
usage: deficit_rates.py LOG r kmin kmax dmax"""
import json, sys, math
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]; st = {r['n']: r for r in rows if 'n' in r and 'log10_col_l1' in r}
r_ = int(sys.argv[2]); kmin = int(sys.argv[3]); kmax = int(sys.argv[4]); dmax = int(sys.argv[5])
def val(n, d):
    cols = st[n]['log10_col_l1']; kap = st[n]['Kt']; q = kap - d
    if q < 0 or q >= len(cols) or cols[q] < -1e9: return None
    return cols[q] + math.log10(math.factorial(q))
print(f"r = {r_}: rate per block (k -> k+1) of log10((kappa-d)! ||[t^(kappa-d)] f_n||), n = 3k + r")
hdr = 'd\\k ' + ' '.join(f'{k:6d}' for k in range(kmin, kmax)); print(hdr)
for d in range(0, dmax + 1, 4):
    line = f'{d:4d} '
    for k in range(kmin, kmax):
        n1, n2 = 3 * k + r_, 3 * (k + 1) + r_
        if n1 in st and n2 in st:
            v1, v2 = val(n1, d), val(n2, d)
            line += f'{(v2 - v1):6.2f} ' if (v1 is not None and v2 is not None) else '   -   '
        else: line += '   -   '
    print(line)
