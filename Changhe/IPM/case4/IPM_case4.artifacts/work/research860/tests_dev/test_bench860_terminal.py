"""Fixtures for bench860.terminal_ok / time_ok / sanitize / PssSampler (lead A(c), E2, E9, E11; verifier 10:48Z and 10:55Z): a good full record and a good spot record pass;
a spot record with completeness.failed True fails (both modes need failed exactly False); failed '' fails; a bool returncode fails; a record with zero periodic-loop samples
fails; SPEC v9.20 row_sampled_ok fixtures against the real sampler (first sample before the timer, exit read, long operations need two loop samples); negative or nonfinite wall/CPU fail; family-wide child read failures do not gate; the sampler's exit read is not counted as a loop sample; sanitize maps nonfinite
to null with a reason and the result dumps with allow_nan=False. Runs under the guard (bench860 imports basis860). Records the sha256 of bench860 and of this script (E10).
Usage: test_bench860_terminal.py <bench860.py path> <out.json>"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, sys, math, hashlib, tempfile, time, importlib.util
from pathlib import Path
import numpy as np
src = Path(sys.argv[1]).resolve(); out_json = Path(sys.argv[2]).resolve(); LANE = Path((_artifact_root))
sys.path.insert(0, str(LANE/'work/research860')); sys.path.insert(0, str(LANE/'work/tools')); sys.path.insert(0, str(src.parent))
spec = importlib.util.spec_from_file_location('bench860_under_test', str(src)); bm = importlib.util.module_from_spec(spec); spec.loader.exec_module(bm)
res = {'source': str(src), 'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(), 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'cases': {}}
def record(name, ok, **info): res['cases'][name] = {'passed': bool(ok), **info}; print(name, 'PASS' if ok else 'FAIL', json.dumps(info, default=str)[:260], flush=True)
with tempfile.TemporaryDirectory(dir=str(out_json.parent)) as td:
    o = Path(td)/'assess.json'; o.write_text('{"x": 1}\n'); sha = hashlib.sha256(o.read_bytes()).hexdigest()
    def rec(mode, **over):
        base = {'returncode': 0, 'output': str(o), 'output_sha256': sha, 'output_sha256_read_back': sha, 'wall_s': 12.5, 'cpu_s': 40.0, 'pss_samples': 26, 'pss_loop_samples': 25, 'pss_exit_samples': 1, 'pss_thread_first_sample_before_timer': True, 'pss_read_failures': 3, 'pss_parent_read_failed': False, 'mode': mode, 'is_full_assessment': mode == 'full', 'failed': False}
        base.update(over); return base
    record('good_full_record_passes', bm.terminal_ok(rec('full'), 'full') is True)
    record('good_spot_record_passes_with_child_read_failures_recorded_not_gated', bm.terminal_ok(rec('spot_only'), 'spot_only') is True)
    record('failed_spot_record_fails', bm.terminal_ok(rec('spot_only', failed=True), 'spot_only') is False)
    record('failed_empty_string_fails', bm.terminal_ok(rec('full', failed=''), 'full') is False)
    record('failed_missing_fails', bm.terminal_ok(rec('full', failed='missing'), 'full') is False)
    record('bool_returncode_False_fails', bm.terminal_ok(rec('full', returncode=False), 'full') is False)
    record('returncode_1_fails', bm.terminal_ok(rec('full', returncode=1), 'full') is False)
    record('zero_loop_samples_fails_even_with_exit_read', bm.terminal_ok(rec('full', pss_loop_samples=0, pss_samples=1), 'full') is False)
    record('terminal_first_sample_flag_False_fails', bm.terminal_ok(rec('full', pss_thread_first_sample_before_timer=False), 'full') is False)
    record('terminal_long_wall_needs_two_loop_samples', bm.terminal_ok(rec('full', pss_loop_samples=1), 'full') is False and bm.terminal_ok(rec('full', pss_loop_samples=2), 'full') is True)
    record('parent_self_read_failure_fails', bm.terminal_ok(rec('full', pss_parent_read_failed=True), 'full') is False)
    record('negative_wall_fails', bm.terminal_ok(rec('full', wall_s=-0.1), 'full') is False)
    record('nan_cpu_fails', bm.terminal_ok(rec('full', cpu_s=float('nan')), 'full') is False)
    record('inf_wall_fails', bm.terminal_ok(rec('full', wall_s=float('inf')), 'full') is False)
    record('bool_wall_fails', bm.terminal_ok(rec('full', wall_s=True), 'full') is False)
    record('mode_mismatch_fails', bm.terminal_ok(rec('spot_only'), 'full') is False and bm.terminal_ok(rec('full'), 'spot_only') is False)
    record('is_full_assessment_inconsistent_fails', bm.terminal_ok(rec('full', is_full_assessment=False), 'full') is False and bm.terminal_ok(rec('spot_only', is_full_assessment=True), 'spot_only') is False)
    record('sha_read_back_mismatch_fails', bm.terminal_ok(rec('full', output_sha256_read_back='0'*64), 'full') is False)
    o.write_text('{"x": 2}\n'); record('output_changed_after_record_fails', bm.terminal_ok(rec('full'), 'full') is False); o.write_text('{"x": 1}\n')
    record('missing_output_file_fails', bm.terminal_ok(rec('full', output=str(Path(td)/'nothing.json')), 'full') is False)
    record('time_ok_rules', bm.time_ok(0.) and bm.time_ok(3) and not bm.time_ok(-1e-9) and not bm.time_ok(float('nan')) and not bm.time_ok(True) and not bm.time_ok(None))
    with bm.PssSampler() as ps: time.sleep(1.2)
    record('sampler_counts_loop_and_exit_samples_separately', ps.loop_samples >= 2 and ps.exit_samples == 1 and ps.samples == ps.loop_samples+ps.exit_samples and ps.parent_failed is False, loop=ps.loop_samples, exit=ps.exit_samples, failures=ps.failures)
    # SPEC v9.20 / lead 11:27Z fixtures against the real PssSampler, timed() and row_sampled_ok
    _, row = bm.timed(lambda: 1)
    record('instant_block_through_real_timed_positive_loop_1_exit_1', bm.row_sampled_ok(row) is True and row['pss_loop_samples'] == 1 and row['pss_exit_samples'] == 1 and row['pss_thread_first_sample_before_timer'] is True and row['pss_parent_read_failed'] is False, row={k: row[k] for k in ('wall_s', 'pss_samples', 'pss_loop_samples', 'pss_exit_samples', 'pss_thread_first_sample_before_timer', 'pss_parent_read_failed')})
    record('zero_loop_sample_row_negative', bm.row_sampled_ok(dict(row, pss_loop_samples=0, pss_samples=1)) is False)
    record('wall_1p2_with_one_loop_sample_negative', bm.row_sampled_ok(dict(row, wall_s=1.2, pss_loop_samples=1)) is False and bm.row_sampled_ok(dict(row, wall_s=1.2, pss_loop_samples=2)) is True)
    record('failed_parent_read_row_negative', bm.row_sampled_ok(dict(row, pss_parent_read_failed=True)) is False)
    record('first_sample_flag_False_negative', bm.row_sampled_ok(dict(row, pss_thread_first_sample_before_timer=False)) is False and bm.row_sampled_ok(dict(row, pss_thread_first_sample_before_timer=None)) is False)
    record('exit_samples_not_one_negative', bm.row_sampled_ok(dict(row, pss_exit_samples=0)) is False and bm.row_sampled_ok(dict(row, pss_exit_samples=2)) is False and bm.row_sampled_ok(dict(row, pss_loop_samples=True)) is False)
    _, row2 = bm.timed(lambda: time.sleep(1.2))
    record('block_of_1p2_s_has_at_least_two_loop_samples', bm.row_sampled_ok(row2) is True and row2['pss_loop_samples'] >= 2 and row2['wall_s'] >= 1.0, loop=row2['pss_loop_samples'], wall=row2['wall_s'])
    record('sampling_statement_present_v922_wording', 'may not have been observed' in bm.SAMPLING_STATEMENT and 'observed peak' in bm.SAMPLING_STATEMENT and 'bounded only by' not in bm.SAMPLING_STATEMENT and 'falls inside' not in bm.SAMPLING_STATEMENT)
    s = bm.sanitize({'a': float('nan'), 'b': [1., float('inf'), {'c': float('-inf')}], 'd': np.float64(2.5), 'e': np.int64(3), 'f': np.array([1., float('nan')])})
    txt = json.dumps(s, allow_nan=False)
    record('sanitize_maps_nonfinite_to_null_with_reason_and_dumps_allow_nan_False', s['a'] is None and s['a_nonfinite'] == 'nan' and s['b'][1] == {'nonfinite': '+inf'} and s['b'][2]['c'] is None and s['b'][2]['c_nonfinite'] == '-inf' and s['d'] == 2.5 and s['e'] == 3 and s['f'][1] == {'nonfinite': 'nan'} and 'NaN' not in txt and 'Infinity' not in txt, value=s)
    p = Path(td)/'step.json'; bm.fsync_write_json(p, {'v': float('nan'), 'ok': True}); back = json.loads(p.read_text())
    record('fsync_write_json_sanitizes', back == {'v': None, 'v_nonfinite': 'nan', 'ok': True} and not p.with_name(p.name+'.partial').exists(), back=back)
res['passed'] = all(c['passed'] for c in res['cases'].values()); out_json.write_text(json.dumps(res, indent=1, default=str)+'\n'); print('ALL PASSED' if res['passed'] else 'SOME FAILED')
