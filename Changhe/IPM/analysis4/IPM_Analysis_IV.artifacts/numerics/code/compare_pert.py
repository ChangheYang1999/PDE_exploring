"""Sensitivity diagnostic (verifier V364): per-order differences between the boundary-perturbed continuation (LOG_A) and the midpoint
continuation (LOG_B) of the canonical 2/3 log series: log10 M_n, log10 N_n, log10(N/M) differences and the largest difference over the
log10 column norms. usage: compare_pert.py LOG_A LOG_B [n_from n_to]"""
import json, sys, math
def lse(v):
    v = [x for x in v if x is not None and x > -1e300]; m = max(v); return m + math.log10(sum(10.0 ** (x - m) for x in v))
def rows(path):
    st = {}
    for l in open(path):
        if not l.strip(): continue
        d = json.loads(l)
        if 'n' in d and 'log10_col_l1' in d: st[d['n']] = d
    return st
A, B = rows(sys.argv[1]), rows(sys.argv[2]); a0 = int(sys.argv[3]) if len(sys.argv) > 3 else min(A); a1 = int(sys.argv[4]) if len(sys.argv) > 4 else max(A)
print(f"{'n':>4} {'log10 M (pert)':>15} {'dM = pert-mid':>14} {'dN':>11} {'d(N/M)':>10} {'max col diff':>13} {'rad pert':>9}")
for n in range(a0, a1 + 1):
    if n in A and n in B:
        a, b = A[n], B[n]; Ma, Mb = lse(a['log10_col_l1']), lse(b['log10_col_l1']); Na, Nb = lse(a['log10_gcol_l1']), lse(b['log10_gcol_l1'])
        cols = [x - y for x, y in zip(a['log10_col_l1'], b['log10_col_l1']) if x > -1e300 and y > -1e300]
        print(f"{n:4d} {Ma:15.4f} {Ma - Mb:+14.2e} {Na - Nb:+11.2e} {(Na - Ma) - (Nb - Mb):+10.2e} {max(abs(c) for c in cols):13.2e} {a.get('log10_rad_over_max', float('nan')):9.1f}")
