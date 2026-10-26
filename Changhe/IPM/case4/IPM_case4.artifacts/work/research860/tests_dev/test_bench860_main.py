"""E5 (c) fixtures against the real bench860.main with child and provider doubles (no process, no scientific provider): subprocess.run is replaced by a double that writes
a chosen configuration child record and good assessment/spot records; Runtime and FrozenLogMesh.load are doubles. Cases: a good child record (positive: passed True);
the verifier's four structurally malformed records (only empty rows/counts/configuration; rows as a list; a missing fun count; a missing stats mapping); a stats value
that is not a dict; a nonzero child exit (control). Each negative must leave a step JSON with passed False and the reason recorded. Runs under the guard (bench860
imports basis860). Records the sha256 of bench860 and of this script (E10). Usage: fixture_bench860_main.py <bench860.py> <out.json>"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, sys, hashlib, tempfile, importlib.util, time, copy
from pathlib import Path
from types import SimpleNamespace
src = Path(sys.argv[1]).resolve(); out_json = Path(sys.argv[2]).resolve(); LANE = Path((_artifact_root))
sys.path.insert(0, str(LANE/'work/research860')); sys.path.insert(0, str(LANE/'work/tools')); sys.path.insert(0, str(src.parent))
spec = importlib.util.spec_from_file_location('bench860_main_under_test', str(src)); bm = importlib.util.module_from_spec(spec); spec.loader.exec_module(bm)
res = {'source': str(src), 'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(), 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'cases': {}}
def record(name, ok, **info): res['cases'][name] = {'passed': bool(ok), **info}; print(name, 'PASS' if ok else 'FAIL', json.dumps(info, default=str)[:300], flush=True)
def good_row(kind, i):
    r = {'wall_s': 0.5, 'cpu_s': 0.6, 'cpu_s_definition': 'double', 'peak_family_pss_mib': 100., 'peak_family_rss_sum_mib': 120., 'pss_samples': 2, 'pss_loop_samples': 1, 'pss_exit_samples': 1, 'pss_thread_first_sample_before_timer': True, 'pss_read_failures': 0, 'pss_parent_read_failed': False}
    if kind == 'integral': r.update(accuracy_passed=True, J_abs=4.2e-9, error_abs=1e-20)
    if kind == 'fun' and i > 0: r.update(cache_builds_delta=1)
    return r
def good_child():
    rows = {k: [good_row(k, i) for i in range(n)] for k, n in bm.PLANNED.items()}
    return {'configuration': {'workers': 8, 'cache_threads': 4, 'block_size': 4096, 'mode_block': 64}, 'rows': rows, 'cache_record': {}, 'A_shape': [90624, 855], 'peak_rss_mib_this_process': 500., 'peak_family_pss_mib': 100., 'peak_family_rss_sum_mib': 120.,
            'pss_read_failures': 0, 'pss_parent_read_failed': False, 'stats': {k: {'wall_s': {'median': 0.5, 'min': 0.5, 'max': 0.5, 'n': n}, 'cpu_s': {'median': 0.6}, 'peak_family_pss_mib': {'median': 100.}} for k, n in bm.PLANNED.items()},
            'counts': dict(bm.PLANNED), 'calls_total': dict(bm.PLANNED), 'calls_timed_of_total': {k: '%d timed of %d' % (n, n) for k, n in bm.PLANNED.items()}, 'planned_counts': dict(bm.PLANNED), 'child_import_closure': {}, 'child_cpu_total_s_rusage_self_plus_children': 1.0}
FULL = {'completeness_v913': {'mode': 'full', 'is_full_assessment': True, 'failed': False}, 'tight_independent_integral': {'J_abs': 4.2e-9, 'accuracy_passed': True}}
SPOT = {'completeness_v913': {'mode': 'spot_only', 'is_full_assessment': False, 'failed': False}}
class FakeRuntime:
    def __init__(self, root): pass
    def read(self, path): return {'epoch_path': 'double', 'meshes': {'training': {'path': 'double'}}}
bm.Runtime = FakeRuntime; bm.FrozenLogMesh = SimpleNamespace(load=lambda p: None)
def run_case(name, child_record, child_rc=0):
    with tempfile.TemporaryDirectory(dir=str(out_json.parent)) as td:
        out = Path(td)/'bench.json'
        def fake_run(cmd, env=None, capture_output=False, text=False):
            if '--child' in cmd:
                partial = Path(cmd[cmd.index('--child')+3])
                if child_rc == 0: partial.write_text(json.dumps(child_record)+'\n')
                return SimpleNamespace(returncode=child_rc, stdout='child double\n', stderr='' if child_rc == 0 else 'injected child failure\n')
            o = Path(cmd[3]); o.write_text(json.dumps(SPOT if '--spot-only' in cmd else FULL)+'\n'); return SimpleNamespace(returncode=0, stdout='', stderr='')
        bm.subprocess.run = fake_run; sys.argv = ['bench860.py', str(out), str(LANE/'outputs/dev_v9/tmp_manifest_kappa.json'), '8']
        exc = None
        try: bm.main()
        except BaseException as e: exc = type(e).__name__+': '+str(e)
        step = json.loads(out.read_text()) if out.exists() else None
        return exc, step
exc, step = run_case('good', good_child())
record('good_child_record_positive_control_passed_True', exc is None and step is not None and step['passed'] is True and not step['runs']['w8_t4'].get('failed') and len(step['assessments']) == 3 and len(step['spot_checks']) == 3, exc=exc, failing=[c['check'] for c in (step or {}).get('checks', []) if not c['passed']], step_passed=(step or {}).get('passed'))
cases = {'verifier_empty_mappings': {'rows': {}, 'counts': {}, 'configuration': {}}, 'verifier_rows_as_list': dict(good_child(), rows=[]), 'verifier_missing_fun_count': None, 'verifier_missing_stats': None, 'stats_not_a_dict': dict(good_child(), stats=[1, 2])}
g = good_child(); g['counts'].pop('fun'); cases['verifier_missing_fun_count'] = g
g2 = good_child(); g2.pop('stats'); cases['verifier_missing_stats'] = g2
expected_field = {'verifier_empty_mappings': 'rows', 'verifier_rows_as_list': 'rows', 'verifier_missing_fun_count': 'counts', 'verifier_missing_stats': 'stats', 'stats_not_a_dict': 'stats'}
for name, rec_ in cases.items():
    exc, step = run_case(name, rec_)
    reason = (step or {}).get('runs', {}).get('w8_t4', {}).get('reason')
    record('%s_step_json_written_passed_False_with_reason' % name, exc is None and step is not None and step['passed'] is False and step['runs']['w8_t4'].get('failed') is True and isinstance(reason, str) and 'schema validation' in reason and reason.endswith(expected_field[name]), exc=exc, reason=reason, step_passed=(step or {}).get('passed'))
exc, step = run_case('child_exit_3', good_child(), child_rc=3)
record('nonzero_child_exit_control_failed_record_passed_False', exc is None and step is not None and step['passed'] is False and step['runs']['w8_t4'].get('failed') is True and step['runs']['w8_t4'].get('returncode') == 3 and 'injected' in (step['runs']['w8_t4'].get('stderr_tail') or ''), exc=exc, reason=(step or {}).get('runs', {}).get('w8_t4', {}).get('reason'))
res['passed'] = all(c['passed'] for c in res['cases'].values()); out_json.write_text(json.dumps(res, indent=1, default=str)+'\n'); print('ALL PASSED' if res['passed'] else 'SOME FAILED')
