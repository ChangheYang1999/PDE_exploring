"""V58: summary of a forward state with its post logs (v43_gfix, v50_axis, v59_kstop, v59_tstop): m1, axis law rows on both half-axes,
log G(+-inf), Delta_z (k = 1 at r_min, tail-corrected), C, 2 log k(e^-9), and the pick asymmetry D(d) at the tracer stops.
Usage: python3 tests/v58_show.py STATE (path without .npz)"""
import sys, json
T = sys.argv[1]
s = [l for l in open(T + '.log') if l.startswith('SUMMARY')]
print('state', T, 'm1', round(json.loads(s[0][8:])['final']['m1'], 6) if s else None)
for l in open(T + '.log'):
    if 'err_fullT' in l and 'final' not in l:
        last = l.strip()
try: print('last iter line:', last[:200])
except NameError: pass
ax = [json.loads(l) for l in open(T + '_axis.log') if l.startswith('{')][0]
for h in ('upper', 'lower'):
    a = ax['axis'][h]
    print(h, 'log_G_axis', a['log_G_axis'], 'range t in [0, 9.5]', a['logh_over_k2_range_t_0_9p5'])
    print('   t      log h/k^2   slope     pred      log k     g_thth     beta')
    for r in a['rows_t_logh_over_k2_slope_predslope_logk_gthth_beta']:
        print('   %-6g %-10g  %-9g %-9g %-9g %-10g %g' % tuple(r))
print('Delta_z (upper - lower in v50 sign):', ax['log_G_upper_minus_lower'], ' axis - mean:', ax.get('axis_minus_mean'))
k = json.load(open(T + '_v59kstop.log'))
for h in ('upper', 'lower'):
    print('kstop', h, 'C', k[h]['C_fit'], 'resid', k[h]['fit_resid_rel'], '2logk(-9)', k[h]['two_logk_true_at']['-9'], '2logk(-6)', k[h]['two_logk_true_at']['-6'])
print('kstop Dz rmin-norm', k['Dz_rmin_norm'], 'tail-corrected', k['Dz_tail_corrected'])
t = json.load(open(T + '_v59tstop.log'))
print('tstop mean', t['mean_cos_gt_0p05'], 'bulk change', t['bulk_max_abs_change_cos_gt_0p3_minus9_to_deepest'])
for d, v in t['D_d_by_stop'].items():
    print('  D(%s)' % d, v)
nz = t['near_zeros']
for lab in sorted(nz, key=float):
    if 85 <= float(lab) <= 91 or 265 <= float(lab) <= 271:
        print('  label', lab, nz[lab]['logGt'], 'stop angle', nz[lab]['stop_angle'])
