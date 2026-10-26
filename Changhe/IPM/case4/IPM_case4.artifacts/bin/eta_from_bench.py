"""Benchmark-based ETA for the 860 campaign (SPEC section 16; PROMPT section 4). Reads the G3 bench record (bench860_v3 step JSON, production pair
w8_t4) or a single child record, takes the per-kind wall medians and the driver sequence (bench860.py per_trial_estimate_s; lead/verifier treatment of
18:26Z to 18:32Z: the warm-Jacobian median measures cache retrieval, so the accepted trial uses the FIRST warm row as the one fresh-assembly observation),
simulates the slice schedule of campaign860.py (startup: cold fun + epoch Jacobian assembly + SVD; trials until the remaining slice time is below the
reserve max(900 s, 1.5 x the largest trial wall); max trials per slice) for given slice lengths and acceptance rates, adds the section 13 assessment
cadence (seed, halvings, every 100 accepted, end; wall from the bench full assessments), and converts a wall-clock window into a trial budget.
It estimates TIME TO SPEND A COMPUTE BUDGET only. Time to convergence is unknown and is not estimated.
Usage: eta_from_bench.py <bench.json or child record> <out.json> [--child] [--slice 3300,6000] [--max-trials 12] [--reserve 900]
       [--assess-wall S] [--spot-wall S] [--window-start UTC] [--window-end UTC[,UTC...]] [--n-assess N] [--label TXT]"""
import argparse, json, math, statistics, time, calendar, hashlib
def med(v): v = [x for x in v if isinstance(x, (int, float)) and math.isfinite(x)]; return float(statistics.median(v)) if v else None
def parse_utc(s): return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
def fmt(t): return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t))
def hm(s): return '%d h %02d min' % (int(s//3600), int((s % 3600)//60))
def simulate(slice_s, startup, t_rej, t_acc, p_acc, reserve_floor, max_trials, overhead):
    """Deterministic expected-value schedule. campaign860.py:661-662: the trial loop ends as soon as monotonic()+reserve > deadline (reserve =
    max(floor, 1.5 x the largest iteration wall, state['iteration_wall_max_seconds']); the slice then commits slice_end and exits 0, and the supervisor
    (checkpointed_slice, sleep 5) starts the next slice, so the slice WALL is startup + trials, not the slice length. The reserve uses the accepted
    iteration (it includes the epoch-start Jacobian and SVD)."""
    t_trial = p_acc*t_acc+(1-p_acc)*t_rej; reserve = max(reserve_floor, 1.5*max(t_acc, t_rej)); t = startup; n = 0
    while n < max_trials and t+reserve <= slice_s: t += t_trial; n += 1   # F3(a): a trial starts only if the reserve still fits
    wall = t+overhead
    return {'slice_s': slice_s, 'startup_s': startup, 'trial_wall_s': t_trial, 'reserve_s': reserve, 'trials_per_slice': n, 'slice_wall_s': wall, 'unused_slice_s': slice_s-t,
            'duty_cycle': (n*t_trial)/wall if n else 0., 'trials_per_hour': 3600.*n/wall if n else 0.}
def main():
    ap = argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('out'); ap.add_argument('--child', action='store_true'); ap.add_argument('--slice', default='3300,5000,6000')
    ap.add_argument('--max-trials', type=int, default=12); ap.add_argument('--reserve', type=float, default=900.); ap.add_argument('--assess-wall', type=float); ap.add_argument('--spot-wall', type=float)
    ap.add_argument('--window-start'); ap.add_argument('--window-end', default='2026-10-26T03:05:00Z,2026-10-26T15:03:00Z'); ap.add_argument('--n-assess', type=int, default=4); ap.add_argument('--label', default='')
    ap.add_argument('--slice-overhead', type=float, default=60., help='supervisor + guard init + cadence check + Python import between slices (seconds)')
    a = ap.parse_args(); raw = open(a.record, 'rb').read(); d = json.loads(raw)
    if a.child: rec = d; src = {'kind': 'child record', 'sha256': hashlib.sha256(raw).hexdigest(), 'configuration': rec.get('configuration')}
    else:
        key = [k for k in d.get('runs', {}) if k.startswith('w8_t4') and not d['runs'][k].get('failed')]
        if not key: raise SystemExit('no completed production pair w8_t4 in %s' % a.record)
        rec = d['runs'][key[0]]; src = {'kind': 'bench step JSON', 'sha256': hashlib.sha256(raw).hexdigest(), 'passed': d.get('passed'), 'configuration': rec.get('configuration'), 'code_manifest_sha256': d.get('code_manifest_sha256')}
    rows = rec['rows']; m = {k: med([r['wall_s'] for r in v]) for k, v in rows.items()}
    fun_rows = rows['fun']; cold = fun_rows[0]['wall_s']; rebuild = [r['wall_s'] for r in fun_rows[1:] if r.get('cache_builds_delta')]; cached = [r['wall_s'] for r in fun_rows[1:] if not r.get('cache_builds_delta')]
    warm = rows['jacobian_warm']; w0 = warm[0]['wall_s']; retrieval = med([r['wall_s'] for r in warm[1:]])
    z = lambda k: m.get(k) or 0.
    fun_rebuild = med(rebuild) if rebuild else z('fun'); io = z('io')
    rejected = z('trust')+z('kkt')+z('lift')+fun_rebuild+z('condition_sums')+z('integral')+io
    accepted_recorded = rejected+z('chart')+z('jacobian_warm')+z('svd')+z('stationarity')+io
    accepted_assembly = rejected+z('chart')+w0+z('svd')+z('stationarity')+io
    startup = cold+w0+z('svd')+z('chart')     # epoch start at the incumbent: cache build (fun), Jacobian assembly, SVD, chart; process/guard/cadence overhead added per slice
    components = {'fun_cold_cache_build_s': cold, 'fun_cache_rebuild_median_s (c_l changed)': fun_rebuild, 'fun_cached_median_s': med(cached), 'jacobian_rebuild_median_s (cache + assembly)': z('jacobian_rebuild'),
                  'jacobian_first_warm_row_s (assembly at a cached key)': w0, 'jacobian_warm_retrieval_median_s (cached matrix)': retrieval, 'svd_median_s': z('svd'), 'trust_median_s': z('trust'), 'kkt_median_s': z('kkt'),
                  'lift_median_s': z('lift'), 'condition_sums_median_s': z('condition_sums'), 'chart_s': z('chart'), 'stationarity_median_s': z('stationarity'),
                  'integral_median_s': z('integral'), 'integral_min_s': min(r['wall_s'] for r in rows['integral']), 'integral_max_s': max(r['wall_s'] for r in rows['integral']), 'io_median_s': io}
    assess = None; spot = None
    if not a.child and d.get('assessments'):
        aw = [x['wall_s'] for x in d['assessments'] if x.get('returncode') == 0]; sw = [x['wall_s'] for x in d.get('spot_checks', []) if x.get('returncode') == 0]
        assess = {'median_s': med(aw), 'max_s': max(aw) if aw else None, 'n': len(aw)}; spot = {'median_s': med(sw), 'max_s': max(sw) if sw else None, 'n': len(sw)}
    assess_wall = a.assess_wall if a.assess_wall else (assess['max_s'] if assess and assess['max_s'] else None)
    spot_wall = a.spot_wall if a.spot_wall else (spot['max_s'] if spot and spot['max_s'] else None)
    slices = [float(s) for s in a.slice.split(',')]; rates = [0.25, 0.5, 0.75]
    schedule = [dict(simulate(s, startup, rejected, accepted_assembly, p, a.reserve, a.max_trials, a.slice_overhead), acceptance_rate=p) for s in slices for p in rates]
    t0 = parse_utc(a.window_start) if a.window_start else time.time(); windows = []
    for we in a.window_end.split(','):
        te = parse_utc(we); avail = te-t0; over = a.n_assess*(assess_wall or 0.)
        per_window = []
        for sc in schedule:
            usable = max(0., avail-over); n_slices = usable/sc['slice_wall_s']; trials = n_slices*sc['trials_per_slice']
            per_window.append({'slice_s': sc['slice_s'], 'acceptance_rate': sc['acceptance_rate'], 'trials_in_window': trials, 'accepted_in_window': trials*sc['acceptance_rate'], 'hours_per_100_trials': 100./sc['trials_per_hour'] if sc['trials_per_hour'] else None})
        windows.append({'window_end_utc': fmt(te), 'window_start_utc': fmt(t0), 'available_s': avail, 'available': hm(avail), 'assessment_overhead_s': over, 'n_assessments_assumed': a.n_assess, 'trial_budgets': per_window})
    out = {'schema': 'eta860_v1', 'utc': fmt(time.time()), 'label': a.label, 'source': src, 'assumptions': {
               'driver_sequence': 'rejected: trust + KKT + lift + trial fun (cache rebuild, c_l changes) + condition_sums + independent integral + I/O; accepted adds Chart860 + Jacobian ASSEMBLY (first warm row, one observation) + SVD + stationarity + I/O (bench860.py per_trial_estimate_s; lead 18:32Z treatment)',
               'slice_startup': 'cold cache build (first fun) + Jacobian assembly + SVD + chart; plus %.0f s process/guard/cadence overhead per slice' % a.slice_overhead, 'slice_end': 'campaign860.py:661-662: the loop breaks when the reserve no longer fits; slice wall = startup + trials + overhead (the slice length is only an upper bound)', 'reserve_rule': 'campaign860.py F3(a): a trial starts only if remaining slice time >= max(%.0f s, 1.5 x largest trial wall)' % a.reserve,
               'max_trials_per_slice': a.max_trials, 'acceptance_rates_are_hypothetical': 'no 860 trial has been accepted or rejected yet; the pilot measures the real rate', 'assessment_cadence': 'section 13: seed, each halving of J_abs, every 100 accepted, end; n_assess assumed per window',
               'convergence': 'NOT estimated: these figures are the time to spend a trial budget, not a time to convergence'},
           'per_component_s': components, 'per_trial_s': {'rejected': rejected, 'accepted_recorded_median_warm': accepted_recorded, 'accepted_with_first_warm_assembly': accepted_assembly, 'slice_startup_s': startup},
           'full_assessment_s': assess, 'spot_check_s': spot, 'assessment_wall_used_s': assess_wall, 'spot_wall_used_s': spot_wall, 'schedule': schedule, 'windows': windows}
    json.dump(out, open(a.out, 'w'), indent=1)
    cfg = src.get('configuration') or {}
    print('ETA inputs (%s, workers %s, cache threads %s)%s' % (src['kind'], cfg.get('workers'), cfg.get('cache_threads'), ' [%s]' % a.label if a.label else ''))
    print('| component | seconds |'); print('|---|---:|')
    for k, v in components.items(): print('| %s | %s |' % (k, '%.1f' % v if isinstance(v, (int, float)) else v))
    print('| rejected trial (driver sequence) | %.0f |' % rejected); print('| accepted trial, recorded (warm median = retrieval) | %.0f |' % accepted_recorded); print('| accepted trial, with one fresh Jacobian assembly | %.0f |' % accepted_assembly)
    print('| slice startup (cache build + Jacobian + SVD + chart), plus %.0f s overhead per slice | %.0f |' % (a.slice_overhead, startup))
    if assess: print('| full assessment at 8 workers (n=%d) median / max | %.0f / %.0f |' % (assess['n'], assess['median_s'] or 0, assess['max_s'] or 0))
    if spot: print('| spot check (n=%d) median / max | %.0f / %.0f |' % (spot['n'], spot['median_s'] or 0, spot['max_s'] or 0))
    print(); print('| slice s | acceptance rate | trials/slice | trial wall s | reserve s | slice wall s | duty cycle | trials/h | h per 100 trials |'); print('|---:|---:|---:|---:|---:|---:|---:|---:|---:|')
    for sc in schedule: print('| %.0f | %.2f | %d | %.0f | %.0f | %.0f | %.2f | %.2f | %s |' % (sc['slice_s'], sc['acceptance_rate'], sc['trials_per_slice'], sc['trial_wall_s'], sc['reserve_s'], sc['slice_wall_s'], sc['duty_cycle'], sc['trials_per_hour'], '%.1f' % (100/sc['trials_per_hour']) if sc['trials_per_hour'] else 'n/a'))
    for w in windows:
        print(); print('Window %s to %s: %s available; %d assessments assumed (%s each) = %s overhead' % (w['window_start_utc'], w['window_end_utc'], w['available'], a.n_assess, hm(assess_wall) if assess_wall else 'unknown', hm(w['assessment_overhead_s'])))
        print('| slice s | acceptance rate | trials in window | accepted in window |'); print('|---:|---:|---:|---:|')
        for b in w['trial_budgets']: print('| %.0f | %.2f | %.0f | %.0f |' % (b['slice_s'], b['acceptance_rate'], b['trials_in_window'], b['accepted_in_window']))
    print(); print('Time to convergence: unknown; not estimated.')
if __name__ == '__main__': main()
