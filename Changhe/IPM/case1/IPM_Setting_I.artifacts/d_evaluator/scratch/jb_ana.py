"""Reduce a vjband json (code/vjband.py): family-A J(theta0) by band; which band carries the oscillation in theta0.
Smooth part = least-squares quadratic in theta0 over the window; oscillation = remainder; report range and rms of the
remainder per band, and the correlation of each band remainder with the J remainder. Usage: python3 jb_ana.py f.json [eps]"""
import sys, json, numpy as np
d = json.load(open(sys.argv[1])); eps = sys.argv[2] if len(sys.argv) > 2 else '0.03'
rows = [r for r in d['rows'] if r['fam'] == 'A']
t = np.array([r['theta0'] for r in rows]); o = np.argsort(t); t = t[o]
B = ('J', 'low', 'mid', 'top', 'high')
V = {b: np.array([r[eps][b] for r in rows])[o] for b in B}
print(d['summary']['file'].split('/')[-1], 'Ktop', d['summary']['Ktop'], 'bands', d['summary']['bands'], 'eps', eps, 'nA', len(t))
print('sum check max |J - sum bands|: %.2e' % np.max(np.abs(V['J'] - V['low'] - V['mid'] - V['top'] - V['high'])))
X = np.vander(t - t.mean(), 3)
rem = {}
for b in B:
    c, *_ = np.linalg.lstsq(X, V[b], rcond=None); rem[b] = V[b] - X @ c
    print('%-4s value %+.3e .. %+.3e | remainder %+.3e .. %+.3e rms %.3e | corr with J remainder %+.2f' % (
        b, V[b].min(), V[b].max(), rem[b].min(), rem[b].max(), np.sqrt(np.mean(rem[b] ** 2)),
        np.corrcoef(rem[b], rem['J'])[0, 1] if b != 'J' else 1.0))
# sign changes of the J remainder: half period in theta0
s = np.where(np.diff(np.sign(rem['J'])) != 0)[0]
if len(s) > 1: print('J remainder sign changes at theta0', np.round(t[s], 4), 'mean half period %.4f' % np.mean(np.diff(t[s])))
for b in ('low', 'mid', 'top'):
    s = np.where(np.diff(np.sign(rem[b])) != 0)[0]
    if len(s) > 1: print('%s remainder mean half period %.4f (%d changes)' % (b, np.mean(np.diff(t[s])), len(s)))
