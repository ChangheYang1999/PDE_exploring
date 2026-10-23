"""Summary statistics over every checkpoint of a frozen independent checkpoint table (read-only).

Usage: python3 table_stats.py <CHECKPOINT_TABLE.tsv> <VALIDATION_COMPLETED.json>
For each table row the evaluation file is the successful one whose checkpoint hash starts with the row's prefix and
whose worst momentum value matches the row to 1e-6 relative. Prints JSON.
"""
import csv, json, sys
from collections import Counter

rows = list(csv.DictReader(open(sys.argv[1]), delimiter='\t'))
done = json.load(open(sys.argv[2]))
ev = {}
for e in done.values():
    if e.get('returncode') == 0:
        ev.setdefault(e['sha256'], []).append(e['output'])


def evaluation(row):
    want = float(row['worst_eps_m'])
    for h, outs in ev.items():
        if not h.startswith(row['sha256_prefix']):
            continue
        for o in outs:
            try:
                d = json.load(open(o))
            except Exception:
                continue
            got = d.get('assessment', {}).get('worst_momentum_relative')
            if got is not None and abs(got - want) <= 1e-6 * max(1.0, abs(want)):
                return h, o, d
    raise SystemExit('no matching evaluation for ' + row['sha256_prefix'])


out = dict(checkpoints=len(rows), worst_region=Counter(), per_row=[])
for r in rows:
    h, o, d = evaluation(r)
    m = d['model_metadata']['config']['model']
    rep = 'first' if m.get('feature_set') == 'dir_log' else 'second'
    a = d['angular']
    rec = dict(run=r['run'], sha=h, step=r['saved_step'], cl=float(r['c_l']), rep=rep, width=m.get('width'),
               worst=float(r['worst_eps_m']), region=r['worst_region'],
               tail=float(r['tail_nonlinear_relative']),
               affine=d['core_affine_fit']['relative_remainder'],
               dir_min=d['core_directional_dependence']['minimum_fraction'],
               vec_nonaxi=d['vector_group_average']['nonaxisymmetric_energy_fraction'],
               ring_n2=a['n2_fraction'], ring_nonaxi=a['nonaxisymmetric_fraction'], evidence=o)
    rec['n2_over_nonaxi'] = rec['ring_n2'] / rec['ring_nonaxi']
    out['per_row'].append(rec)
    out['worst_region'][r['worst_region']] += 1
P = out['per_row']
rng = lambda k, sel=lambda x: True: [min(x[k] for x in P if sel(x)), max(x[k] for x in P if sel(x))]
out['worst_range'] = rng('worst')
for k in ('affine', 'dir_min', 'vec_nonaxi', 'ring_n2', 'n2_over_nonaxi'):
    out[k + '_range'] = rng(k)
for rep in ('first', 'second'):
    out[f'tail_{rep}_primary'] = rng('tail', lambda x, rep=rep: x['rep'] == rep and x['cl'] < 0.5)
    out[f'tail_{rep}_050'] = rng('tail', lambda x, rep=rep: x['rep'] == rep and x['cl'] >= 0.5)
best = {}
for x in P:
    key = (x['rep'], x['width'], x['cl'])
    if key not in best or x['worst'] < best[key]['worst']:
        best[key] = x
out['best'] = [dict(rep=k[0], width=k[1], cl=k[2], run=v['run'], step=v['step'], worst=v['worst'],
                    region=v['region'], tail=v['tail'], sha=v['sha'][:16]) for k, v in sorted(best.items())]
prim = [x for x in P if 0.4 < x['cl'] < 0.5]
sel = min(prim, key=lambda x: x['worst'])
out['selected'] = dict(run=sel['run'], step=sel['step'], cl=sel['cl'], sha=sel['sha'], worst=sel['worst'],
                       evidence=sel['evidence'])
del out['per_row']
print(json.dumps(out, indent=1))
