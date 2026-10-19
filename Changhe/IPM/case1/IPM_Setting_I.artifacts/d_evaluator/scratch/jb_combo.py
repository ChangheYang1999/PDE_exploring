"""Band-pair correlations for a vjband json: remainder (after a quadratic in theta0) of J against low+mid, mid+top, low+top, and
the fraction of J-remainder variance left after a least-squares fit by the three band remainders. Usage: python3 jb_combo.py f.json [eps]"""
import sys, json, numpy as np
d = json.load(open(sys.argv[1])); eps = sys.argv[2] if len(sys.argv) > 2 else '0.03'
rows = [r for r in d['rows'] if r['fam'] == 'A']
t = np.array([r['theta0'] for r in rows]); o = np.argsort(t); t = t[o]
V = {b: np.array([r[eps][b] for r in rows])[o] for b in ('J', 'low', 'mid', 'top', 'high')}
Q = np.vander(t - t.mean(), 3)
rem = {b: v - Q @ np.linalg.lstsq(Q, v, rcond=None)[0] for b, v in V.items()}
cor = lambda a, b: float(np.corrcoef(a, b)[0, 1])
out = []
for name, parts in (('low+mid', ('low', 'mid')), ('mid+top', ('mid', 'top')), ('low+top', ('low', 'top'))):
    s = sum(rem[p] for p in parts)
    out.append('%s rms %.3e corr %+.2f' % (name, np.sqrt(np.mean(s ** 2)), cor(s, rem['J'])))
print(sys.argv[1].split('/')[-1], 'eps', eps, '|', ' | '.join(out))
