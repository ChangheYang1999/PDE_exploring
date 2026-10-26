"""Observed-throughput ETA for an 860 campaign root (compute-budget time only; time to convergence is unknown and not estimated).
Reads commits/event_*.json: per-trial iteration_wall_seconds, acceptance, slice overheads (init/recover from slice_start to the first
trial, slice_end gaps), the supervisor cadence assessments (ledger). Usage: env/bin/python -B bin/eta_observed860.py <root> <out.json> [--slice-seconds 3300] [--reserve 900]"""
import json, glob, os, sys, statistics, time, hashlib
root = sys.argv[1]; out = sys.argv[2]
slice_s = float(sys.argv[sys.argv.index('--slice-seconds')+1]) if '--slice-seconds' in sys.argv else 3300.0
reserve = float(sys.argv[sys.argv.index('--reserve')+1]) if '--reserve' in sys.argv else 900.0
ev = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(root, 'commits', 'event_*.json')))]
trials = [e['trial'] for e in ev if isinstance(e.get('trial'), dict) and 'trial' in e['trial'] and 'accepted' in e['trial']]
iw = [t['iteration_wall_seconds'] for t in trials]; acc = [bool(t['accepted']) for t in trials]
starts = [e['trial'] for e in ev if e.get('trial', {}).get('kind') == 'slice_start']; ends = [e['trial'] for e in ev if e.get('trial', {}).get('kind') == 'slice_end']
# slice overhead: from the guard run start (run_start_epoch) to the slice_start commit epoch (init or recover), per slice
overhead = [s['epoch'] - s['run_start_epoch'] for s in starts if 'run_start_epoch' in s]
ledger = os.path.join(root, 'assessments', 'ledger.jsonl'); assess = [json.loads(l) for l in open(ledger) if l.strip()] if os.path.exists(ledger) else []
assess_s = [a.get('seconds') for a in assess if a.get('seconds')]
def radius_history(trials):
    """Radius and rejection history read from the commits (no static text): every trial whose radius_after differs from radius_before, and the rejected trials."""
    ch = [t for t in trials if t.get('radius_before') is not None and t.get('radius_after') is not None and t['radius_before'] != t['radius_after']]
    rej = [t['trial'] for t in trials if not t['accepted']]
    parts = ['trial %d: %.4e -> %.4e (%s, gain %.3f)' % (t['trial'], t['radius_before'], t['radius_after'], 'accepted' if t['accepted'] else 'rejected', t.get('gain_ratio') or 0.0) for t in ch]
    last = trials[-1] if trials else None
    return ('Trust radius history from the %d trial commits: %d radius changes (%s); rejected trials %s; radius after trial %d: %.6e; every other trial held its radius.'
            % (len(trials), len(ch), '; '.join(parts) if parts else 'none', rej if rej else 'none', last['trial'] if last else -1, (last.get('radius_after') if last else 0.0) or 0.0))
res = {'root': root, 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'trials': len(trials), 'accepted': sum(acc), 'rejected': len(acc) - sum(acc),
       'iteration_wall_seconds': iw, 'slice_overhead_seconds': overhead, 'assessment_seconds': assess_s, 'slice_seconds': slice_s, 'reserve_seconds': reserve}
if iw:
    med = statistics.median(iw); mean = statistics.mean(iw); mx = max(iw)
    usable = slice_s - reserve
    # driver rule (campaign860.py line 662): a trial starts while elapsed + reserve <= budget (it stops when monotonic + reserve > deadline), i.e. while elapsed <= slice_s - reserve,
    # checked before each trial; simulated here with the mean observed overhead before the first start and the median wall for every iteration (fixed reserve; equality allowed, as in the driver)
    oh0 = statistics.mean(overhead) if overhead else 0.0
    tt = oh0; per_slice_trials_est = 0
    while tt <= usable and per_slice_trials_est < 12: per_slice_trials_est += 1; tt += med
    last_end = tt
    # observed slice 1: trials per guard wall
    res['iteration_wall_median'] = med; res['iteration_wall_mean'] = mean; res['iteration_wall_max'] = mx
    res['trials_per_slice_model'] = per_slice_trials_est
    slice_wall_est = last_end + 15.0 if per_slice_trials_est else None   # +15 s supervisor/cadence gap between slices
    res['slice_wall_estimate_seconds'] = slice_wall_est
    res['trials_per_hour_model'] = 3600.0 * per_slice_trials_est / slice_wall_est if slice_wall_est else None
    res['acceptance_rate_observed'] = sum(acc) / len(acc)
    for budget_h in (24, 48, 72):
        res['trials_in_%dh_model' % budget_h] = int(budget_h * res['trials_per_hour_model']) if res['trials_per_hour_model'] else None
    res['scope'] = ('Model from observed iteration walls (median) and the observed slice overhead; it predicts how many trials a compute budget buys, '
                    'not when or whether the optimizer converges. Cadence assessments (about %s s each, every significant improvement / slice boundary by the '
                    'supervisor rule) are extra. ' % (round(statistics.mean(assess_s)) if assess_s else 'n/a')) + radius_history(trials) + ' Later trials may be rejected and the walls may change with mesh refinement or box load.'
json.dump(res, open(out, 'w'), indent=1); print(json.dumps({k: v for k, v in res.items() if k not in ('scope',)}, indent=1)); print('wrote', out, hashlib.sha256(open(out,'rb').read()).hexdigest()[:16])
