"""profile_table.py: the fixed-c_l profile on the 375 x m <= 150 basis at equal budget (lead NOTES 2026-10-19T00:25:51Z): rows fxm2g (d = -2e-3),
s2g (X2, -1e-3), seg3g (F2, free, 0), fxu2g (+2e-3), fxu3g (+3e-3), fxv24g (+2.4e-2) as far as they exist; L2 objective from the chain logs (final check),
quick_scan_fit values at 32768 x 640 (TAG_scan.json or TAG_scan_32768x640.json). Usage: python3 profile_table.py"""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
rows = [('fxn24g', -2.4e-2), ('fxn16g', -1.6e-2), ('fxn8g', -8e-3), ('fxn4g', -4e-3), ('fxm2g', -2e-3), ('s2g', -1e-3), ('seg3g', 0.0), ('fxu2g', 2e-3), ('fxu3g', 3e-3), ('fxv24g', 2.4e-2)]
F2 = None
out = []
for tag, d in rows:
    log = os.path.join(H, tag, tag + '.log')
    if not os.path.exists(log): continue
    ch = {}; cl = None; done = False
    for l in open(log):
        if not l.startswith('{'): continue
        o = json.loads(l)
        if o.get('event') == 'check': ch[2500 * (o['outer'] - 1) + o['it']] = o['actual']; cl = o['cl']
        if o.get('event') == 'end': done = True
    if not ch: continue
    last = max(ch); L2 = ch[last]
    prev = [k for k in sorted(ch) if k <= last - 1000]
    chg = (L2 / ch[prev[-1]] - 1) * 100 if prev else float('nan')
    scan = None
    for fn in (os.path.join(H, tag, tag + '_scan_32768x640.json'), os.path.join(H, tag, tag + '_scan.json')):
        if os.path.exists(fn): scan = json.load(open(fn)); break
    if tag == 'seg3g': F2 = L2
    out.append((tag, d, cl, L2, last, chg, done, scan))
print('%-7s %8s %13s %12s %6s %7s %5s | %10s %10s %10s %10s %10s %10s %9s %9s' % ('row', 'd', 'c_l', 'L2', 'its', 'dL2/1k', 'done', 'wholebox', 'xstrip', 'lobe', 'N_v 2-10', '10-100', '100-1e3', 'h(P)-1', 'x*'))
for tag, d, cl, L2, last, chg, done, scan in out:
    b = scan['bands'] if scan else None
    print('%-7s %+8.1e %13.10f %12.6e %6d %+6.2f%% %5s | %10.3e %10.3e %10.3e %10.3e %10.3e %10.3e %+9.1e %9.6f' % (
        tag, d, cl, L2, last, chg, done, b['all/all']['max'] if b else float('nan'), b['2<=r<=10/x_strip']['max'] if b else float('nan'),
        b['2<=r<=10/middle']['max'] if b else float('nan'), b['2<=r<=10/all']['N4_max'] if b else float('nan'), b['10<=r<=100/all']['max'] if b else float('nan'),
        b['100<=r<=1000/all']['max'] if b else float('nan'), (scan['hP'] - 1) if scan else float('nan'), scan['xstar'] if scan else float('nan')))
if F2:
    print('L2 / F2 (%.6e):' % F2, ', '.join('%s %.3f' % (t, L2 / F2) for t, d, cl, L2, last, chg, done, scan in out))
