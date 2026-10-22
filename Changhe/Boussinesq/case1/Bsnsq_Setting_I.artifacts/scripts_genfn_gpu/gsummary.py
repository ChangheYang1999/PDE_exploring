"""Summary table of genfn LM states: python3 gsummary.py <npz...> [--at it1,it2,...] ; prints J, Kw, m, se, l, tmin, its, final obj / grid max / rms / a0, and the values at selected iterations."""
import sys, json, numpy as np
files = [a for a in sys.argv[1:] if not a.startswith('--')]
at = [int(v) for v in sys.argv[sys.argv.index('--at') + 1].split(',')] if '--at' in sys.argv else []
print('%-28s %4s %4s %2s %6s %5s %6s %4s | %10s %10s %10s %9s | %s' % ('state', 'J', 'Kw', 'm', 'se', 'l', 'tmin', 'its', 'obj', 'gridmax', 'rms', 'a0', 'at its ' + ','.join(map(str, at)) + ': obj / gridmax / a0'))
for f in files:
    try:
        d = np.load(f)
    except Exception as e:
        print(f, 'unreadable', e); continue
    h = json.loads(str(d['hist'])) if 'hist' in d.files else []
    last = h[-1] if h else {}
    se = float(d['se']) if 'se' in d.files else 1.0; l = float(d['l']) if 'l' in d.files else 1.0; tmin = float(d['tmin']) if 'tmin' in d.files else float('nan')
    sel = []
    for it in at:
        rec = [r for r in h if r['it'] == it]
        sel.append('%.3e/%.2e/%.2f' % (rec[0]['obj'], rec[0]['maxres'], rec[0]['a0']) if rec else '-')
    print('%-28s %4d %4d %2d %6.3f %5.2f %6.3f %4d | %10.3e %10.3e %10.3e %9.3f | %s' % (f.split('/')[-1][:28], int(d['J']), int(d['Kw']), int(d['m']) if 'm' in d.files else 3, se, l, tmin, len(h),
          last.get('obj', float('nan')), last.get('maxres', float('nan')), last.get('rms', float('nan')), float(d['a0']), '  '.join(sel)))
