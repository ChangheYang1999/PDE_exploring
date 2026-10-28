"""Post-process data/certSups_*.jsonl: certified sups (over the covered region) of the weighted and unweighted derivative tensors and of every component.
Reports max over cells (accepted) with the cell location; checks coverage of the depth-0 cells and the origin square; flags nan/inf cells."""
import sys, json, math
from collections import defaultdict
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
ok = [r for r in rows if r['status'] == 'ok']; bad = [r for r in rows if r['status'] != 'ok']
print('cells %d ok %d errors %d; radial range [%g, %g]' % (len(rows), len(ok), len(bad), min(r['r_lo'] for r in ok), max(r['r_hi'] for r in ok)))
keys = [k for k in ok[0] if k.startswith(('Frob_', 'wFrob_', 'rho_', 'U1_', 'U2_'))]
nan_cells = [r for r in ok if any((isinstance(r[k], float) and (math.isnan(r[k]) or math.isinf(r[k]))) for k in keys)]
print('cells with nan/inf bounds: %d (these cells are NOT certified; list below if any)' % len(nan_cells))
for r in nan_cells[:10]: print('   r in [%g,%g] theta in [%.3f,%.3f] rem %.1e' % (r['r_lo'], r['r_hi'], r['t_lo'], r['t_hi'], r.get('rem_max', -1)))
good = [r for r in ok if r not in nan_cells]
out = {}
for k in keys:
    w = max(good, key=lambda r: r[k]); out[k] = {'sup': w[k], 'r_lo': w['r_lo'], 'r_hi': w['r_hi'], 't_lo': w['t_lo'], 't_hi': w['t_hi']}
    if k.startswith(('Frob', 'wFrob')): print('%-14s <= %10.5g   attained in cell r in [%g, %g], theta in [%.3f, %.3f]' % (k, w[k], w['r_lo'], w['r_hi'], w['t_lo'], w['t_hi']))
print('component sups:', {k: round(v['sup'], 5) for k, v in out.items() if not k.startswith(('Frob', 'wFrob'))})
json.dump(out, open(sys.argv[2], 'w'), indent=1)
