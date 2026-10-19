#!/usr/bin/env python3
"""Table of the exit-angle sensitivity test (tests/pfwd_exit_sens.py outputs) across resolutions.
usage: python3 tests/pfwd_es_table.py runs/pfwd/par/ES256.out runs/pfwd/par/ES512.out [runs/pfwd/par/ES1024.out ...]
Per file: the polished base (defect, m1, D_ax, |F|, exits), then per direction: d theta_1 / d eps (deg per unit relative state change) at every eps, the eps at which the
slope departs from its small-eps value by more than 30 % (breakdown), the product band norms (plateau check) and, if present, the exit-change quantiles per band at eps 1e-6 and 1e-4."""
import sys, json
for fn in sys.argv[1:]:
    recs = [json.loads(l) for l in open(fn) if l.strip() and not l.startswith('{"polish"')]
    hdr = [r for r in recs if 'tag' in r][0]; base = [r for r in recs if r.get('polished')]
    print('\n==== %s  Nth %d (%s)' % (fn, hdr['Nth'], hdr['how']))
    if base:
        b = base[0]; print('  base: defect %.3g max / %.3g rms, converged %s, m1 %.6f, D_ax %s, D_ax_dir %s, |F| %s, R_reduced %s, c %s, psi_yy0 %.2e, exits %s, minVr_r %s' % (
            b['defect'], b['defect_rms'], b['converged'], b['m1'], b.get('D_ax'), b.get('D_ax_dir'), b.get('normF'), b.get('R_reduced'), b.get('c'), b['psi_yy0'], b['exits'], b.get('minVr_r')))
    dirs = sorted(set(r['dir'] for r in recs if 'dir' in r and 'eps' in r))
    for dn in dirs:
        rs = sorted([r for r in recs if r.get('dir') == dn and 'eps' in r], key=lambda r: r['eps'])
        if not rs: continue
        print('  direction %s:' % dn)
        print('    %-8s %12s %12s %14s %9s %9s %9s %9s %8s' % ('eps', 'dth1(deg)', 'dth2(deg)', 'dth1/eps', 'core', 'inner', 'mid', 'outer', 'even%'))
        s0 = rs[0]['dth1_per_eps']
        brk = None
        for r in rs:
            pb = r['prod_bands']; keys = list(pb.keys())
            if brk is None and s0 != 0 and abs(r['dth1_per_eps'] / s0 - 1) > 0.3: brk = r['eps']
            print('    %-8g %12.5f %12.5f %14.1f %9.3g %9.3g %9.3g %9.3g %8.3f' % (r['eps'], r['dth1'], r['dth2'], r['dth1_per_eps'], pb[keys[0]], pb[keys[1]], pb[keys[2]], pb[keys[3]], 100 * r['prod_even_frac']))
        print('    slope at the smallest eps %.1f deg per unit relative change (%.3f deg per 1e-3); breakdown (slope off by > 30 %%) at eps %s' % (s0, s0 * 1e-3, brk))
        for r in rs:
            q = r.get('exit_change_quantiles_deg')
            if q and r['eps'] in (1e-6, 1e-4, 1e-3):
                print('    exit-change quantiles (deg) at eps %g, quantiles %s:' % (r['eps'], q['quantiles']))
                for bk, vals in q['bands'].items():
                    if bk.endswith('switched'): continue
                    print('      band %-10s %s   switched cells %d' % (bk, ' '.join('%.2e' % v for v in vals), q['bands'][bk + '_switched']))
