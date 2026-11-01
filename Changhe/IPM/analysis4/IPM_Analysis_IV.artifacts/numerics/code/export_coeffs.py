"""Compact export of a checkpoint for the artifacts: per order n the odd-sine coefficients a_{n,k} as float64 after scaling by
10^{-log10_scale} (so that no under/overflow occurs), the scale, and the arb radius bound. Exact rationals are exported as
strings for n <= nexact. usage: export_coeffs.py CKPT OUT.json [--nmax N] [--nexact 8] [--log]"""
import sys, os, json, argparse, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
ap = argparse.ArgumentParser(); ap.add_argument('ckpt'); ap.add_argument('out'); ap.add_argument('--nmax', type=int, default=10**9); ap.add_argument('--nexact', type=int, default=0); ap.add_argument('--log', action='store_true')
args = ap.parse_args()
if args.log:
    from logff import LogFarField
    L = LogFarField.load(args.ckpt); R = L.R
    out = {'kind': 'log_series', 'delta': str(L.delta_exact), 'c_l': str(L.c_exact), 'ring': R.name, 'prec': getattr(R, 'prec', None), 'orders': {}}
    for n in sorted(L.f):
        if n > args.nmax: break
        cols = []
        for a in L.f[n]:
            l2a = [R.log2abs(x) for x in a]
            if not a or max(l2a) == -float('inf'): cols.append({'log10_scale': None, 'coeffs': [0.0] * len(a)}); continue
            im = int(np.argmax(l2a)); mx = a[im]; lg = R.log10abs(mx)
            cols.append({'log10_scale': lg, 'coeffs': [R.to_float(x / mx) for x in a]})
        out['orders'][n] = {'f_columns_t_power': cols, 'log10_rad_over_max': L.stats.get(n, {}).get('log10_rad_over_max')}
else:
    ff = FarField.load(args.ckpt); R = ff.R
    out = {'kind': 'pure_series', 'c_l': R.to_str(ff.c_l), 'delta': R.to_str(ff.delta), 'ring': R.name, 'prec': getattr(R, 'prec', None),
           'convention': 'f_n = sum_k a[k] sin((2k+1) theta); value = coeffs[k] * 10^log10_scale', 'orders': {}}
    for n in sorted(ff.f):
        if n > args.nmax: break
        a = ff.f[n]; l2a = [R.log2abs(x) for x in a]; im = int(np.argmax(l2a)); mx = a[im]; lg = R.log10abs(mx)
        rec = {'log10_scale': lg, 'coeffs': [R.to_float(x / mx) for x in a], 'log10_rad_over_max': ff.stats.get(n, {}).get('log10_rad_over_max')}
        if R.name == 'fmpq' and n <= args.nexact: rec['exact'] = [str(x) for x in a]
        out['orders'][n] = rec
json.dump(out, open(args.out, 'w'))
print('wrote', args.out, 'orders', len(out['orders']), 'size MB', os.path.getsize(args.out) / 1e6)
