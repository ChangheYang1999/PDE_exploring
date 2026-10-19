"""Verifier scratch: compare two vaudit JSONs (fit A against base B) region by region.
Usage: python3 cmp_fit.py A.json B.json [L]   (L in physical units for the band locations; default 7.651424601381517)
Prints N_f (flux) and N_v maxima, ratios A/B, and the N_v argmax (r in L, theta) for every region present in both, then
h(P) - 1 and c_l of each."""
import sys, json
A, B = (json.load(open(f)) for f in sys.argv[1:3])
L = float(sys.argv[3]) if len(sys.argv) > 3 else 7.651424601381517
ra = {r['region']: r for r in A['residual']}; rb = {r['region']: r for r in B['residual']}
print('%-34s %10s %10s %6s | %10s %10s %6s | NvA at (r/L, th)   NvB at' % ('region', 'NfA', 'NfB', 'rat', 'NvA', 'NvB', 'rat'))
for k in ra:
    if k not in rb: continue
    a, b = ra[k], rb[k]
    print('%-34s %10.3e %10.3e %6.3f | %10.3e %10.3e %6.3f | %9.4g %.4f  %9.4g %.4f' % (
        k[:34], a['flux_max'], b['flux_max'], a['flux_max'] / b['flux_max'], a['Nv_max'], b['Nv_max'], a['Nv_max'] / b['Nv_max'],
        a['Nv_argmax_r'] / L, a['Nv_argmax_theta'], b['Nv_argmax_r'] / L, b['Nv_argmax_theta']))
only = [k for k in ra if k not in rb]
for k in only:
    a = ra[k]
    print('%-34s %10.3e %10s %6s | %10.3e (A only)  at %9.4g %.4f' % (k[:34], a['flux_max'], '-', '-', a['Nv_max'], a['Nv_argmax_r'] / L, a['Nv_argmax_theta']))
for lab, X in (('A', A), ('B', B)):
    v = X['vcand']
    print('%s: hP-1 %+.3e  c_l %.10f  x* %.6f  file %s' % (lab, v['hP'] - 1, v['c_l'], v['x_star'], v['file']))
