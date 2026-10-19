"""Table of the one-at-a-time quadrature variations (runs/ray/vary_<tag>.json): per node |dU| (Euclidean) vs the export, and the maximum
normalized residual impact.  Usage: python3 src/vary_table.py runs/ray/vary_*.json"""
import sys, json, numpy as np
files = sys.argv[1:]
rows0 = json.load(open(files[0]))['rows']
X = [(r['x'], r['y']) for r in rows0]
print('%-10s | ' % 'variation' + ' '.join('%-9s' % ('(%.3g,%.3g)' % xy)[:9] for xy in X) + ' | max imp  time')
for f in files:
    d = json.load(open(f)); tag = f.split('vary_')[-1].replace('.json', '')
    assert [(r['x'], r['y']) for r in d['rows']] == X
    du = [np.hypot(*r['dU']) for r in d['rows']]; imp = max(r['impact'] for r in d['rows'])
    print('%-10s | ' % tag + ' '.join('%-9.1e' % v for v in du) + ' | %-8.1e' % imp)
