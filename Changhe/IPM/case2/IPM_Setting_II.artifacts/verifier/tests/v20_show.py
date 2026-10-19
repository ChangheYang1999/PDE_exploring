import json, sys
lead = {}
for l in open('runs/joint_scan_05.log'):
    if ':' in l and l.split(':')[0].strip().isdigit() and 'kappa' in l:
        k = int(l.split(':')[0]); f = dict(kv.split('=') for kv in l.replace('(target 0.6667)', '').split(':')[1].split())
        lead[k] = (float(f['kappa']), float(f['3kw/c']))
for l in open(sys.argv[1]):
    d = json.loads(l)
    if 'val' in d: print('val a=%.1f c=%.5f kappa=%.4f kw3=%.4f wp0=%.5f/%.5f' % (d['val'], d['c'], d['kappa'], d['kw3'], d['wp0_up'], d['wp0_dn'])); continue
    if 'kappa' not in d: print('%2d c=%.4f <= 0' % (d['k'], d['c'])); continue
    k = d['k']; ld = lead.get(k, (float('nan'), float('nan')))
    side = ('+' if d['kappa'] > 2/3 else '-') + ('+' if d['kw3'] > 2/3 else '-')
    print('%2d c=%9.4f kappa=%8.4f kw3=%8.4f kw3ax=%8.4f minVr/r=%8.3f %s   lead kappa=%8.4f kw3=%8.4f' % (k, d['c_quad'], d['kappa'], d['kw3'], d['kw3_axis'], d['minVr_r'], side, ld[0], ld[1]))
