"""Strict T4 verdict reader (numerics lane, new file outside the manifest). Prints the runner result.json fields, the t4.json sha256,
passed flag, failing check names, the T4.5 rows and the dilation sidecar quantities (my_squared_norms/2 for the topic-17 comparison,
lead NOTES 13:19Z item 2). Usage: python t4_verdict_read.py <session_dir> <t4.json>"""
import json, sys, os, glob, hashlib, time
sess, t4 = sys.argv[1], sys.argv[2]
runs = sorted(glob.glob(os.path.join(sess, 'runs', '*_g3_t4')))
print('run dirs:', runs)
for r in runs:
    p = os.path.join(r, 'result.json')
    if not os.path.exists(p): print(r, 'NO result.json'); continue
    d = json.load(open(p))
    keys = ['run_id', 'success', 'returncode', 'stop_reasons', 'started_time', 'finished_time', 'wall_seconds', 'peak_family_rss_mib', 'command', 'worker_pid', 'supervisor_pid']
    for k in keys: print('  %s: %r' % (k, d.get(k)))
    if d.get('started_time') and d.get('finished_time'):
        print('  started %s finished %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(d['started_time'])), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(d['finished_time']))))
        if os.path.exists(t4):
            mt = os.path.getmtime(t4); print('  t4.json mtime %r inside interval: %r' % (mt, d['started_time'] <= mt <= d['finished_time']))
    sj = os.path.join(r, 'step_json_sha256.txt')
    if os.path.exists(sj): print('  runner step_json_sha256.txt:', open(sj).read().strip())
if not os.path.exists(t4): print('t4.json MISSING'); sys.exit(0)
b = open(t4, 'rb').read(); print('t4.json sha256', hashlib.sha256(b).hexdigest(), 'bytes', len(b))
j = json.loads(b)
print('passed:', j.get('passed'), 'finished_utc:', j.get('finished_utc'))
checks = j.get('checks') or []; names = [c.get('check') for c in checks]
print('checks:', len(checks), 'unique names:', len(set(names)) == len(names), 'all passed identity True:', all(c.get('passed') is True for c in checks))
fail = [c.get('check') for c in checks if c.get('passed') is not True]; print('failing:', fail)
for c in checks: print('  %-75s %-28s %s' % (c.get('check'), str(c.get('value'))[:28], 'PASS' if c.get('passed') is True else 'FAIL'))
rows = j.get('T4.5') or []
print('T4.5 rows:', len(rows))
for r in rows:
    print('  %-28s %-8s best %.3e thr %.0e all-steps %-5s steps %d C5max %s ratios %s' % (r['direction'], r['kind'], r['best_relative_error'], r['threshold'], r['passed_all_completed_steps_baseline'], r['steps_completed'], r.get('lifted_point_C5_max'), r.get('convergence_ratios_consecutive_steps')))
dil = j.get('dilation') or {}
msn = dil.get('my_squared_norms') or {}; ref = dil.get('verifier_topic17_reference') or {}
print('dilation sidecar: my_squared_norms (J_mesh scale, = 2 x H-norm^2):', msn)
print('  divided by 2 (comparable to topic 17 H-norm^2):', {k: v/2 for k, v in msn.items()})
print('  topic17 reference: projected %r leak %r exact %r' % (ref.get('weighted_residual_derivative_squared_norm_projected'), ref.get('weighted_residual_derivative_squared_norm_leak'), ref.get('weighted_residual_derivative_squared_norm_exact')))
for k in ['dJ_along_projected_D_per_unit_logL', 'dJ_along_exact_FD_column', 'dJ_along_k26_leak', 'cosine_projected_vs_exact', 'exact_minus_projected_column_norm', 'exact_minus_projected_minus_k26_norm', 'low_projection_residual_rel', 'VT_D_weakest_3', 'smallest_singular', 'median_singular', 'A_Ds_norm_over_Ds_norm_scaled_metric', 'k26_leakage_coefficients']:
    print('  %s: %r' % (k, dil.get(k)))
cr = j.get('cache_record') or {}
for k in ['cache_builds', 'cache_build_seconds', 'jacobian_seconds', 'origin_series_seconds', 'assembly_seconds', 'evaluation_cache_hits', 'fun_calls']: print('  cache_record %s: %r' % (k, cr.get(k)))
