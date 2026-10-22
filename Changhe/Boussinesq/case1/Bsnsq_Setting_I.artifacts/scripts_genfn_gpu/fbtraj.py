"""Trajectory summary of a gsolve_fbg.py log: it, beta, a0, obj, maxres at given iterations, mean beta step over the last 50 saved records.
Usage: python3 fbtraj.py run.log [it1 it2 ...]"""
import sys, json, re
recs = [json.loads(l) for l in open(sys.argv[1]) if l.startswith('{"it"')]
its = [int(a) for a in sys.argv[2:]] or [0, 25, 50, 100, 150, 199]
by = {r['it']: r for r in recs}
print('%s: %d records; last it %d' % (sys.argv[1].split('/')[-1], len(recs), recs[-1]['it'] if recs else -1))
for i in its:
    r = by.get(i) or (recs[-1] if recs and i >= recs[-1]['it'] else None)
    if r: print('  it %3d: beta %.9f  a0 %.6f  obj %.5e  maxres %.4e  maxRN %.4e  maxdes %.3e' % (r['it'], r['beta'], r['a0'], r['obj'], r['maxres'], r.get('maxRN', float('nan')), r.get('maxdes', float('nan'))))
if len(recs) > 2:
    tail = recs[-11:] if len(recs) > 11 else recs
    db = (tail[-1]['beta'] - tail[0]['beta']) / (tail[-1]['it'] - tail[0]['it'])
    d0 = (recs[1]['beta'] - recs[0]['beta']) / (recs[1]['it'] - recs[0]['it'])
    print('  beta change total %+.3e; mean step per iteration: first interval %+.3e, last %d iterations %+.3e; ratio last/first %.2f' % (recs[-1]['beta'] - recs[0]['beta'], d0, tail[-1]['it'] - tail[0]['it'], db, db / d0 if d0 else float('nan')))
