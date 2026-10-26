#!/usr/bin/env python3
"""Print the numerics WORKLOG line and the two document table rows for one committed trial event of an 860 campaign root.
Usage: trial_line.py <campaign-root> <event-number> [--seed-J <J_abs of the seed>]
Reads commits/event_<n>.json only (no numerical imports). The slice number is read from the latest slice_start event before it."""
import json, sys, glob, hashlib
from pathlib import Path
root = Path(sys.argv[1]); n = int(sys.argv[2]); seedJ = 4.2683726070956366e-09
if '--seed-J' in sys.argv: seedJ = float(sys.argv[sys.argv.index('--seed-J')+1])
ev = json.loads((root/'commits'/('event_%08d.json' % n)).read_text())
t = ev.get('trial') or {}
if not t: print('event', n, 'is not a trial commit:', ev.get('kind') or ev.get('type') or sorted(ev.keys())[:8]); sys.exit(0)
import os, time
sl = t.get('slice'); ep = t.get('epoch')
cutc = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(os.path.getmtime(root/'commits'/('event_%08d.json' % n))))
ps = ev.get('post_state') or {}
tv = t.get('trial_validation') or {}
acc = t.get('accepted'); J_ind = t.get('trial_J_abs_independent'); err = t.get('trial_error_abs')
Jb = t.get('objective_before'); Jt = t.get('objective_trial'); pred = t.get('predicted_decrease'); meas = t.get('actual_mesh_decrease'); gain = t.get('gain_ratio')
kkt = (t.get('subproblem') or {}).get('actual_matrix_KKT_relative'); tay = t.get('five_Taylor_max'); cons = (tv.get('five_Taylor_validation') or {}).get('constraints')
cl = t.get('trial_cl'); a0 = t.get('trial_a0'); pc = t.get('physical_changes') or {}
dcl = (pc.get('cl') or {}).get('absolute'); da0 = (pc.get('a0') or {}).get('absolute')
rb = t.get('radius_before'); ra = t.get('radius_after'); step = t.get('step_norm')
itw = t.get('iteration_wall_seconds'); trw = t.get('trial_wall_seconds'); mod = t.get('model_seconds'); tf = t.get('trial_fun_seconds'); val = t.get('validation_seconds')
cr = t.get('cache_record') or {}; rss = t.get('peak_rss_mib'); cpu = t.get('trial_cpu_seconds')
tot = t.get('trial'); acc_after = t.get('accepted_after'); rej = tot - acc_after
snap = root/'snapshots'/('accepted_%08d.json' % acc_after); snap_sha = hashlib.sha256(snap.read_bytes()).hexdigest() if snap.exists() else None
pct = 100.0*((J_ind if acc else Jb) - seedJ)/seedJ if (J_ind and Jb) else None   # the incumbent's J_abs after this trial: the trial point if accepted, objective_before if rejected
held = 'held' if (ra is not None and rb is not None and abs(ra-rb) <= 1e-12*abs(rb)) else ('doubled' if ra and rb and ra > rb else 'cut')
status = 'ACCEPTED' if acc else 'REJECTED'
line = ('TRIAL %d %s (event %d; G5 slice %s): objective %r -> %r, J_abs independent %r (error_abs %.2e; training - independent %.2e); predicted %r vs measured %r (gain %.8f); KKT rel %.2e; five-Taylor %r%s; c_l %r (%+.2e), a_0 %r (%+.2e); step norm %.6e (radius before %.6e; equality not asserted); radius before %.4e, after %.4e (%s). Walls: iteration %.2f s = model %.2f + trial_wall %.2f (trial_fun %.2f + validation %.2f + %.1f); cache builds %s (%.1f s), jacobian %.2f s, origin series %.2f s; peak rss %.1f MiB; trial cpu %.1f s. Totals %d trials, %d accepted, %d rejected. Best accepted snapshot accepted_%08d.json (sha256 %s), %.2f percent vs the seed. Events 1..%d.'
        % (tot, status, n, sl, Jb, Jt, J_ind, err or 0.0, (Jt or 0.0) - (J_ind or 0.0), pred, meas, gain or 0.0, kkt or 0.0, tay, (' (defects %s)' % ', '.join('%.2e' % c for c in cons)) if cons else '', cl, dcl or 0.0, a0, da0 or 0.0, step or 0.0, rb or 0.0, rb or 0.0, ra or 0.0, held,
           itw or 0.0, mod or 0.0, trw or 0.0, tf or 0.0, val or 0.0, (trw or 0.0) - (tf or 0.0) - (val or 0.0), cr.get('cache_builds'), cr.get('cache_build_seconds') or 0.0, cr.get('jacobian_seconds') or 0.0, cr.get('origin_series_seconds') or 0.0, rss or 0.0, cpu or 0.0,
           tot, acc_after, rej, acc_after, snap_sha, pct or 0.0, n))
print('WORKLOG:', line)
print()
print('NUM_REPORT row:')
print('  | %d | %s | %r | %.8e / %.8e | %.8f | %.1e | %.1e | %r | %r | %.2e (%s) | %.2f | %.2f | %.2f | %.2f | %.1e |' % (tot, sl, J_ind, pred or 0.0, meas or 0.0, gain or 0.0, kkt or 0.0, tay or 0.0, cl, a0, rb or 0.0, held, itw or 0.0, mod or 0.0, trw or 0.0, val or 0.0, err or 0.0))
print('RESULTS_860 row:')
print('| %d (G5) | %s | %s | %r | %.8f | %r | %r | %.2e (%s) |' % (tot, sl, 'accepted' if acc else 'rejected', J_ind, gain or 0.0, cl, a0, ra or 0.0, held))
print('OPT_LOG row:')
print('- %s TRIAL %d %s (event %d; slice %s): J_abs %.4e -> %r (gain %.3f, radius %s at %.2e); c_l %r, a_0 %r; five-Taylor %.2e; iteration %.1f s. Totals %d / %d / %d (%.2f percent vs the seed).' % (cutc, tot, status, n, sl, Jb or 0.0, J_ind, gain or 0.0, held, ra or 0.0, cl, a0, tay or 0.0, itw or 0.0, tot, acc_after, rej, pct or 0.0))
print('commit file mtime (UTC):', cutc, '; trial epoch field:', ep, '; kind:', t.get('kind'))
