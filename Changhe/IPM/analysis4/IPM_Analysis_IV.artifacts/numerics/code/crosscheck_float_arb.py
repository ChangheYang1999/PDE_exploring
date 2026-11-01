"""Cross-check of the canonical 2/3 run (512-bit ball midpoints; orders >= 330 midpoint-only) against the full float64 run and its
amplitude-perturbed twin (f_1 = (1 + 1e-10) sin theta; exact normalized values identical, rounding patterns different).
Prints per order: log10 M_n, log10 N_n (arb), float - arb, twin(normalized) - float, and the float N/M.
usage: crosscheck_float_arb.py n_from n_to [arb_tag]   (default arb_tag log_sin1_c3_p512; use log_sin1_c3_from329 for the reset-radii continuation)"""
import json, math, sys
def lse(v):
    v = [x for x in v if x is not None and x > -1e300]; m = max(v); return m + math.log10(sum(10 ** (x - m) for x in v))
def load(tag):
    st = {}
    for l in open(f'logs/{tag}.jsonl'):
        if '"n"' not in l: continue
        r = json.loads(l)
        if 'log10_col_l1' in r and 'log10_gcol_l1' in r: st[r['n']] = (lse(r['log10_col_l1']), lse(r['log10_gcol_l1']), r.get('midpoint_only'))
    return st
arb = load(sys.argv[3] if len(sys.argv) > 3 else 'log_sin1_c3_p512'); ff = load('log23_full_float'); fp = load('log23_full_float_pert'); eps = math.log10(1.0000000001)
n0, n1 = int(sys.argv[1]), int(sys.argv[2])
print(f"{'n':>4} {'log10 M arb':>12} {'log10 N arb':>12} {'N/M arb':>8} | {'float-arb M':>12} {'float-arb N':>12} | {'twin-float M':>12} {'twin-float N':>12} | {'mid-only':>8}")
for n in range(n0, n1 + 1):
    a = arb.get(n); f = ff.get(n); p = fp.get(n)
    sa = f"{a[0]:12.3f} {a[1]:12.3f} {a[1]-a[0]:8.3f}" if a else f"{'-':>12} {'-':>12} {'-':>8}"
    sf = f"{f[0]-a[0]:+12.2e} {f[1]-a[1]:+12.2e}" if (a and f) else (f"{'(float only) M='+format(f[0],'.3f'):>25}" if f else f"{'-':>12} {'-':>12}")
    sp = f"{p[0]-n*eps-f[0]:+12.2e} {p[1]-n*eps-f[1]:+12.2e}" if (f and p) else f"{'-':>12} {'-':>12}"
    print(f"{n:4d} {sa} | {sf} | {sp} | {str(a[2]) if a else '-':>8}")
