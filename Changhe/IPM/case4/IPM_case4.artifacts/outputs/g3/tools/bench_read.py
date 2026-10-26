"""Bench record reader for the G3 bench step (numerics lane, new file outside the manifest). Prints the runner result.json fields, bench.json sha256 and
checks, per-configuration medians, the three memory peaks (row-sample peak, configuration-sampler peak, guard whole-run peak) and their maximum (lead 13:34Z,
14:06Z; verifier 13:51Z), assessment statistics and the per-trial estimate, as inputs for the ETA. Usage: bench_read.py <session_dir> <bench.json> [parent_rss.jsonl]"""
import json, sys, os, glob, hashlib, time, math
sess, bj = sys.argv[1], sys.argv[2]; prss = sys.argv[3] if len(sys.argv) > 3 else None
guard_peak = None
for r in sorted(glob.glob(os.path.join(sess, 'runs', '*_g3_bench'))):
    p = os.path.join(r, 'result.json')
    if not os.path.exists(p): print(r, 'NO result.json'); continue
    d = json.load(open(p)); guard_peak = d.get('peak_family_rss_mib')
    for k in ['run_id', 'success', 'returncode', 'stop_reasons', 'wall_seconds', 'peak_family_rss_mib']: print('result %s: %r' % (k, d.get(k)))
    print('result started %s finished %s' % (time.strftime('%H:%M:%SZ', time.gmtime(d['started_time'])), time.strftime('%H:%M:%SZ', time.gmtime(d['finished_time']))))
    if os.path.exists(bj): mt = os.path.getmtime(bj); print('bench.json mtime inside interval:', d['started_time'] <= mt <= d['finished_time'])
if not os.path.exists(bj): print('bench.json MISSING'); sys.exit(0)
b = open(bj, 'rb').read(); print('bench.json sha256', hashlib.sha256(b).hexdigest(), 'bytes', len(b)); j = json.loads(b)
print('passed', j.get('passed'), 'began', j.get('began_utc'), 'finished', j.get('finished_utc'))
checks = j.get('checks') or []; print('checks', len(checks), 'failing', [c['check'] for c in checks if c.get('passed') is not True])
for c in checks: print('  %-70s %-20s %s' % (c.get('check'), str(c.get('value'))[:20], 'PASS' if c.get('passed') is True else 'FAIL'))
row_peaks = []; samp_peaks = []
for key, v in (j.get('runs') or {}).items():
    if v.get('failed'): print('RUN', key, 'FAILED', v.get('reason'), (v.get('stderr_tail') or '')[-300:]); continue
    st = v['stats']; print('RUN', key, 'configuration', v['configuration'], 'child_wall_s', round(v.get('child_wall_s') or 0), 'A_shape', v.get('A_shape'))
    for k in ['fun', 'jacobian_warm', 'jacobian_rebuild', 'svd', 'trust', 'kkt', 'lift', 'condition_sums', 'chart', 'stationarity', 'integral', 'io']:
        s = st.get(k) or {}; w = s.get('wall_s') or {}; print('   %-16s n=%-2s median %10.3f min %10.3f max %10.3f  (%s)' % (k, v['counts'].get(k), w.get('median') or float('nan'), w.get('min') or float('nan'), w.get('max') or float('nan'), v.get('calls_timed_of_total', {}).get(k)))
    for x in v['rows'].get('fun', []): print('      fun row: wall %.2f label %s' % (x['wall_s'], x.get('label')))
    for x in v['rows'].get('integral', []): print('      integral row: wall %.2f J_abs %r error %r accuracy %r tol %r' % (x['wall_s'], x.get('J_abs'), x.get('error_abs'), x.get('accuracy_passed'), x.get('acceptance_tolerance')))
    rp = v.get('peak_family_rss_sum_mib'); sp = v.get('child_peak_family_rss_sum_mib_from_parent'); row_peaks.append(rp or 0); samp_peaks.append(sp or 0)
    print('   memory: row peak PSS %.0f / RSS sum %.0f MiB; child sampler peak PSS %.0f / RSS sum %.0f MiB; this process ru_maxrss %.0f MiB' % (v.get('peak_family_pss_mib') or 0, rp or 0, v.get('child_peak_family_pss_mib_from_parent') or 0, sp or 0, v.get('peak_rss_mib_this_process') or 0))
print('assessment_stats', json.dumps(j.get('assessment_stats'), default=str)[:1500])
for i, a in enumerate(j.get('assessments') or []): print('  assessment %d: wall %.1f cpu %.1f rc %r mode %r failed %r peak PSS %.0f RSS sum %.0f' % (i, a['wall_s'], a['cpu_s'], a.get('returncode'), a.get('mode'), a.get('failed'), a.get('peak_family_pss_mib') or 0, a.get('peak_family_rss_sum_mib') or 0))
for i, a in enumerate(j.get('spot_checks') or []): print('  spot %d: wall %.1f cpu %.1f rc %r mode %r failed %r' % (i, a['wall_s'], a['cpu_s'], a.get('returncode'), a.get('mode'), a.get('failed')))
print('per_trial_estimate_s', json.dumps(j.get('per_trial_estimate_s'), default=str)[:1200])
print('memory_basis_for_G4_limit', json.dumps(j.get('memory_basis_for_G4_limit'), default=str)[:800])
ass_peaks = [a.get('peak_family_rss_sum_mib') or 0 for a in (j.get('assessments') or [])+(j.get('spot_checks') or [])]
cands = {'row_sample_peak_rss_sum': max(row_peaks or [0]), 'configuration_sampler_peak_rss_sum': max(samp_peaks or [0]), 'assessment_sampler_peak_rss_sum': max(ass_peaks or [0]), 'guard_whole_run_peak_family_rss': guard_peak or 0}
mx = max(cands.values()); print('MEMORY PEAKS (MiB, RSS-sum measure):', cands); print('maximum', mx, '1.3x', math.ceil(1.3*mx), 'placeholder rule max(163840, ceil(1.3x)) =', max(163840, math.ceil(1.3*mx)))
if prss and os.path.exists(prss):
    rows = [json.loads(l) for l in open(prss) if l.strip()]; rows = [r for r in rows if not r.get('ended')]
    if rows: print('parent sampler: max parent_rss %.0f VmHWM %.0f max descendants %d max desc sum %.0f max parent+desc %.0f' % (max(r['parent_rss_mib'] for r in rows), max(r['parent_peak_rss_mib'] for r in rows), max(r['descendants'] for r in rows), max(r['descendants_rss_sum_mib'] for r in rows), max(r['parent_rss_mib']+r['descendants_rss_sum_mib'] for r in rows)))
