"""Accepted steps out of attempted, and the objective / maximum history at chosen iterations, from the 'hist' field of a saved state (gsolve_gpu.py /
gsolve_fbg.py records every accepted iteration with 'ntrial' = trial steps for that iteration, so attempted = sum ntrial). Usage: accepted.py STATE [its...]"""
import sys, json, numpy as np
f = sys.argv[1]; its = [int(a) for a in sys.argv[2:]] or [0, 200, 400, 599]
d = np.load(f, allow_pickle=True); h = json.loads(str(d['hist']))
rec = {int(r['it']): r for r in h if 'it' in r}
if not rec:
    print('%s: records (accepted) 0, attempted 0 (empty history: the run accepted no step; the state equals its init); beta %s a0 %s' % (f.split('/')[-1], float(d['beta']) if 'beta' in d.files else 3.0, float(d['a0']))); raise SystemExit(0)
acc = len(rec); att = sum(int(r.get('ntrial', 1)) for r in h if 'it' in r)
print('%s: records (accepted) %d, attempted (sum ntrial) %d, rejected %d; beta %s a0 %s' % (f.split('/')[-1], acc, att, att - acc, float(d['beta']) if 'beta' in d.files else 3.0, float(d['a0'])))
for k in its:
    r = rec.get(k) or (rec[max(rec)] if k >= max(rec) else None)
    if r: print('  it %3d: obj %.4e  maxres %.4e  maxRN %.4e%s' % (int(r['it']), r['obj'], r['maxres'], r.get('maxRN', float('nan')), ('  beta %.6f' % r['beta']) if 'beta' in r else ''))
if len(rec) >= 101:
    ks = sorted(rec); a, b = rec[ks[-101]], rec[ks[-1]]
    print('  last 100 its (%d -> %d): maxres %+.2f %%, obj %+.2f %%' % (a['it'], b['it'], 100 * (b['maxres'] / a['maxres'] - 1), 100 * (b['obj'] / a['obj'] - 1)))
