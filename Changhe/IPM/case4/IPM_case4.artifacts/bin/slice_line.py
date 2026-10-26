#!/usr/bin/env python3
"""Summarize the end of one slice of an 860 campaign root for the WORKLOG: completion record, slice_end event, guard result, supervisor lines, and (if present)
the next slice's continuation row and slice_start event. Reader only. Usage: slice_line.py <campaign-root> <slice-number>"""
import json, sys, glob, hashlib, time
from pathlib import Path
root = Path(sys.argv[1]); n = int(sys.argv[2])
cf = sorted(glob.glob(str(root/'slice_completion'/('slice_%04d_*.json' % n))))
if not cf: print('no completion record for slice', n); sys.exit(0)
c = json.loads(Path(cf[-1]).read_text()); csha = hashlib.sha256(Path(cf[-1]).read_bytes()).hexdigest()
rid = c['guard_run_id']; res = root/'guard_session'/'runs'/rid/'result.json'; r = json.loads(res.read_text()) if res.exists() else {}
seq = c.get('slice_end_event_sequence'); ev = json.loads((root/'commits'/('event_%08d.json' % seq)).read_text())['trial'] if seq else {}
srow = [json.loads(l) for l in (root/'slices.jsonl').read_text().splitlines() if l.strip()]
srow = [x for x in srow if x.get('slice') == n and x.get('guard_run_id') == rid]
if srow and not c.get('seconds'): c['seconds'] = srow[-1].get('seconds')
sup = [l for l in (root/'supervisor.log').read_text().splitlines() if ('slice %d ' % n) in l or rid in l]
print('SLICE %d END (event %s; %s): status %s, reason "%s", %d trials this slice (totals %d trials, %d accepted); objective %r, J_abs independent %r; worker time %.1f s, solver cpu increment %.1f s; modules unchanged at end: %s; completion record %s (sha256 %s...); guard run %s: success %s, returncode %s, stop_reasons %s, wall %.1f s, peak family RSS %.0f MiB.'
      % (n, seq, c.get('utc'), c.get('status'), c.get('slice_end_reason'), c.get('trials_this_slice') or 0, c.get('trials') or 0, c.get('accepted') or 0, c.get('objective'), c.get('J_abs_independent'), c.get('seconds') or 0.0, ev.get('solver_cpu_seconds_increment') or 0.0, ev.get('module_sha256_at_import_equal_at_end'), Path(cf[-1]).name, csha[:8], rid, r.get('success'), r.get('returncode'), r.get('stop_reasons'), r.get('wall_seconds') or 0.0, r.get('peak_family_rss_mib') or 0.0))
print('supervisor.log lines:'); [print('   ', l[:300]) for l in sup]
# next slice
starts = [json.loads(Path(p).read_text()) for p in sorted(glob.glob(str(root/'commits'/'event_*.json')))[-6:]]
for e in starts:
    t = e.get('trial') or {}
    if t.get('kind') == 'slice_start' and t.get('slice') == n+1:
        print('SLICE %d START event %d: guard_run_id %s, workers %s, seconds_budget %s, reserve floor %s, root_weight_check %s' % (n+1, t.get('event_sequence'), t.get('guard_run_id'), t.get('workers'), t.get('seconds_budget'), t.get('reserve_seconds_floor'), (t.get('root_weight_check') or {}).get('passed') if isinstance(t.get('root_weight_check'), dict) else t.get('root_weight_check')))
    if t.get('kind') == 'assessment' and t.get('slice') == n+1:
        print('ASSESSMENT BINDING event %d: reason %s, accepted %s, failed %s, scientific_stop %s, output %s' % (t.get('event_sequence'), t.get('reason'), t.get('accepted'), t.get('failed'), t.get('scientific_stop'), t.get('output')))
cont = (root/'continuations.jsonl').read_text().splitlines()
if cont:
    cr = json.loads(cont[-1]); ct = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(cr['epoch']))
    print('last continuation row (%s): trials %s, residual_difference_norm %r, tolerance %r, bitwise %s, orphans %s, trajectory rows %s, committed_proposals %s, verification %s...' % (ct, cr.get('trials'), cr.get('residual_difference_norm'), cr.get('tolerance'), cr.get('bitwise'), (cr.get('reconciliation') or {}).get('orphans'), ((cr.get('reconciliation') or {}).get('trajectory') or {}).get('rows'), (cr.get('reconciliation') or {}).get('committed_proposals'), (cr.get('verification_sha256') or '')[:8]))
hb = json.loads((root/'HEARTBEAT.json').read_text()); print('heartbeat:', {k: hb.get(k) for k in ('phase', 'slice', 'trials', 'accepted', 'phase_trial', 'utc', 'pid', 'guard_run_id')})
