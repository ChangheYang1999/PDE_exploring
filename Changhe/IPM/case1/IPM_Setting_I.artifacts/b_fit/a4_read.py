# Lead (2026-10-18T17:00Z): A4 reading of a domain column against the base fit, lead fit-convention scans (quick_scan_fit.py).
# Rule (fixed 08:17Z, A4): the domains agree if the 2-10 and 10-100 N_f maxima are within a factor 1.5 of the base fit on the
# same basis and |h(P) - 1| < 1e-7. Printed for both scan grids; the verifier's audits decide (this is the lead cross-check).
import json, sys
base, dom = sys.argv[1], sys.argv[2]
for suf in ['_scan.json', '_scan960.json']:
    try:
        b = json.load(open(base + suf)); d = json.load(open(dom + suf))
    except FileNotFoundError as e:
        print('missing', e); continue
    print('%s%s vs %s%s: nr %d nt %d; c_l %.10f / %.10f; h(P)-1 %.2e / %.2e' % (dom, suf, base, suf, d['nr'], d['nt'], d['cl'], b['cl'], d['hP'] - 1, b['hP'] - 1))
    ok = abs(d['hP'] - 1) < 1e-7
    for band in ['2<=r<=10/all', '10<=r<=100/all', '0.1<=r<=2/all', '100<=r<=1000/all', '1000<=r<=R/all', 'all/all']:
        if band not in d['bands'] or band not in b['bands']:
            print('  %-18s missing' % band); continue
        x, y = d['bands'][band], b['bands'][band]
        ratio = x['max'] / y['max']; ratio4 = x['N4_max'] / y['N4_max']
        tag = ''
        if band in ('2<=r<=10/all', '10<=r<=100/all'):
            within = (1 / 1.5) <= ratio <= 1.5
            ok = ok and within
            tag = ' A4 %s' % ('within 1.5' if within else 'OUTSIDE 1.5')
        print('  %-18s N_f %.3e / %.3e (ratio %.3f) at r %.4g th %.4f | N_v %.3e / %.3e (ratio %.3f)%s' % (
            band, x['max'], y['max'], ratio, x['r_max'], x['theta_max'], x['N4_max'], y['N4_max'], ratio4, tag))
    print('  A4 (lead scans): %s' % ('AGREE' if ok else 'DO NOT AGREE'))
