#!/usr/bin/env python3
"""Reader for HANDOFF_860.md sections 5 and 8: per-slice iteration walls, trial CPU, worker peak RSS, gain and radius history of an 860
campaign root, from commits/event_*.json only. Usage: handoff_walls.py <root> [--from-trial 14]"""
import json, glob, os, sys, statistics, time
root = sys.argv[1]; t0 = int(sys.argv[sys.argv.index('--from-trial')+1]) if '--from-trial' in sys.argv else 14
ev = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(root, 'commits', 'event_*.json')))]
tr = [e['trial'] for e in ev if isinstance(e.get('trial'), dict) and 'accepted' in e['trial'] and 'iteration_wall_seconds' in e['trial']]
print('read at', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'events', len(ev), 'trial commits', len(tr))
print('all trials: walls sorted descending (top 4):', sorted(((t['iteration_wall_seconds'], t['trial']) for t in tr), reverse=True)[:4])
g5 = [t for t in tr if t['trial'] >= t0]
print('trials %d..%d (%d trials): wall min %.2f max %.2f median %.2f; trial cpu %.0f to %.0f s; peak rss %.0f to %.0f MiB'
      % (t0, g5[-1]['trial'], len(g5), min(t['iteration_wall_seconds'] for t in g5), max(t['iteration_wall_seconds'] for t in g5),
         statistics.median(t['iteration_wall_seconds'] for t in g5), min(t['trial_cpu_seconds'] for t in g5), max(t['trial_cpu_seconds'] for t in g5),
         min(t['peak_rss_mib'] for t in g5), max(t['peak_rss_mib'] for t in g5)))
sl = {}
for t in g5: sl.setdefault(t['slice'], []).append(t)
for s in sorted(sl):
    w = [t['iteration_wall_seconds'] for t in sl[s]]; n = [t['trial'] for t in sl[s]]
    print('  slice %d: trials %d..%d (%d trials), walls %.2f to %.2f s, accepted %d' % (s, min(n), max(n), len(n), min(w), max(w), sum(bool(t['accepted']) for t in sl[s])))
acc = [t for t in tr if t['accepted']]; rej = [t for t in tr if not t['accepted']]
print('totals: %d trials, %d accepted, %d rejected (rejected trials %s)' % (len(tr), len(acc), len(rej), [t['trial'] for t in rej]))
g = [(t['trial'], t['gain_ratio']) for t in tr if t['trial'] >= 11]
print('gain ratios trials %d..%d: min %.3f (trial %d) max %.3f (trial %d)' % (g[0][0], g[-1][0], min(x[1] for x in g), min(g, key=lambda x: x[1])[0], max(x[1] for x in g), max(g, key=lambda x: x[1])[0]))
print('radius changes (trial: before -> after):')
for t in tr:
    if t['radius_before'] != t['radius_after']: print('   trial %d: %.6e -> %.6e (accepted %s, gain %.3f)' % (t['trial'], t['radius_before'], t['radius_after'], t['accepted'], t['gain_ratio']))
last = tr[-1]; print('last trial %d: J_abs independent %r, c_l %r, a_0 %r, five-Taylor max %r, radius after %r' % (last['trial'], last['trial_J_abs_independent'], last['trial_cl'], last['trial_a0'], last['five_Taylor_max'], last['radius_after']))
