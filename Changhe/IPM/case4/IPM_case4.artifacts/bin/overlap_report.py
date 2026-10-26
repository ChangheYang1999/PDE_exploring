#!/usr/bin/env python3
"""Read-only: the run's trial commits inside a time window (iteration walls, trial walls), the largest iteration wall of the root and the driver reserve it implies
(max(900, 1.5 x largest iteration wall), campaign860.py lines 659 and 790), and the trials per 5000 s slice that reserve allows at the median iteration wall.
Usage: overlap_report.py <campaign-root> <start utc or epoch> <end utc or epoch>"""
import sys, json, glob, os, time, statistics
root = sys.argv[1]
def ep(s):
    try: return float(s)
    except ValueError: return time.mktime(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ')) - time.timezone
t0, t1 = ep(sys.argv[2]), ep(sys.argv[3])
rows = []
for p in sorted(glob.glob(os.path.join(root, 'commits', 'event_*.json'))):
    mt = os.path.getmtime(p)
    e = json.load(open(p)); t = e.get('trial') or {}
    if t.get('kind') is not None or 'iteration_wall_seconds' not in t: continue
    end = ((e.get('post_state') or {}).get('last_epoch')) or mt; start = end - t['iteration_wall_seconds']       # the iteration interval [start, end]
    rows.append((start, end, mt, t))
print('all trial commits of the root are read; the iteration interval of each is reconstructed as [post_state.last_epoch - iteration_wall_seconds, post_state.last_epoch] (its start is 6 to 12 ms after trial.epoch, the recorded iteration start, because last_epoch is taken just before the commit); iterations whose interval intersects [%s, %s] are marked OVERLAP with the overlap seconds; only iterations ending within 3 h of the window are listed:' % (sys.argv[2], sys.argv[3]))
n_over = 0
for start, end, mt, t in rows:
    inter = max(0.0, min(end, t1) - max(start, t0))
    if inter <= 0 and (end < t0 - 10800 or end > t1 + 10800): continue
    inside = 'OVERLAP %.0f s of %.0f s' % (inter, end - start) if inter > 0 else ''
    n_over += inter > 0
    print('  trial %3d event %3d iteration %s to %s (%.1f s) trial_wall %.1f s model %.1f validation %.1f accepted %s %s' % (t['trial'], t['event_sequence'], time.strftime('%H:%M:%SZ', time.gmtime(start)), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(end)), t['iteration_wall_seconds'], t['trial_wall_seconds'], t.get('model_seconds') or 0, t.get('validation_seconds') or 0, t.get('accepted'), inside))
print('iterations overlapping the window: %d' % n_over)
st = json.load(open(os.path.join(root, 'state.json')))
wmax = st.get('iteration_wall_max_seconds'); reserve = max(900.0, 1.5 * (wmax or 0))
tr = [json.loads(l) for l in open(os.path.join(root, 'trajectory.jsonl')) if l.strip()]
walls = [r['iteration_wall_seconds'] for r in tr if 'iteration_wall_seconds' in r]
med = statistics.median(walls) if walls else float('nan')
print('state.json: trials %s accepted %s slices %s; largest iteration wall of the root %.1f s -> reserve %.1f s; median iteration wall %.1f s -> about %d trials per 5000 s slice (driver rule: a trial starts while elapsed + reserve <= budget; with a fixed reserve, constant walls equal to the median and one 185 s resume overhead this is 1 + floor((5000 - reserve - 185) / median), 0 if 5000 - reserve < 185; a reserve that changes inside a slice needs a start-by-start replay)' % (st.get('trials'), st.get('accepted'), st.get('slices'), wmax or 0, reserve, med, max(0, 1 + int((5000 - reserve - 185) // med)) if walls else 0))
