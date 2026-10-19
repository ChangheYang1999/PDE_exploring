"""Compact summary of quick_scan JSON files: c_l, h(P)-1, flux/N4 max per band, near-P profile maxima."""
import json, sys
for fn in sys.argv[1:]:
    try:
        d = json.load(open(fn))
    except Exception as e:
        print(fn, 'ERR', e); continue
    b = d['bands']
    def g(k, q):
        v = b.get(k, {}); return v.get(q, float('nan'))
    print('%s nr=%d nt=%d cl=%.8f hP-1=%+.2e | 2-10 flux %.2e N4 %.2e | 0.1-2 %.2e | 10-100 %.2e | 100-1e3 %.2e | >1e3 %.2e | all rms %.2e' % (
        fn.split('/')[-1], d['nr'], d['nt'], d['cl'], d['hP'] - 1, g('2<=r<=10/all', 'max'), g('2<=r<=10/all', 'N4_max'),
        g('0.1<=r<=2/all', 'max'), g('10<=r<=100/all', 'max'), g('100<=r<=1000/all', 'max'), g('1000<=r<=R/all', 'max'),
        g('all/all', 'rms')))
    print('    nearP fd-log max by theta:', ' '.join('%.3f:%.2e' % (p['theta'], p['max']) for p in d.get('near_P_profiles', [])))
