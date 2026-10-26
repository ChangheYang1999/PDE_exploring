"""Fixtures for assess_cadence860.py (lead A(d), A(e), E1, N10; verifier 10:46Z): the cadence is copied byte for byte into a temporary directory next to a STUB assess860.py
that writes a chosen record and exits with a chosen code, so the cadence's own control flow runs unchanged. Cases: a spot_only record (failed False), a failed spot_only
record, a full record missing frozen32_maxima (malformed), a good full record, an exit-1 process, an unparsable output. Expected: every refusal is committed as a ledger row
with a reason and STOPPED_FOR_DIAGNOSIS, the cadence exits 0 (the row is the verdict), no KeyError, the good record gives failed False and no marker, and rec['completeness']
is recorded (E1). Usage: test_cadence860_refusals.py <assess_cadence860.py path> <out.json>"""
import json, sys, subprocess, tempfile, hashlib, shutil, os
from pathlib import Path
src = Path(sys.argv[1]).resolve(); out_json = Path(sys.argv[2]).resolve()
STUB = r'''import json, sys, os
out = sys.argv[1]; mode = os.environ['CADENCE_STUB_MODE']
full = {'completeness_v913': {'mode': 'full', 'is_full_assessment': True, 'failed': False, 'missing_records': [], 'non_boolean_checks': [], 'false_checks': [], 'nonfinite_samples_total': 0},
        'origin_truncation_monitor': {'scientific_stop': False, 'worst_band_relative': 1e-15}, 'rf_reference_spot_check': {'scientific_stop': False, 'worst_ratio': 0.3},
        'frozen32_maxima': {'E_f': {'value': 1e-10}, 'E_rho': {'value': 2e-10}}, 'farfield': {'E': {'1': {'L2': 0.44}}}, 'P_sha256': 'p', 'high_sha256': 'h', 'tight_independent_integral': {'J_abs': 4.2e-9, 'accuracy_passed': True}}
spot = {'completeness_v913': {'mode': 'spot_only', 'is_full_assessment': False, 'failed': False, 'missing_records': [], 'non_boolean_checks': [], 'false_checks': [], 'nonfinite_samples_total': 0},
        'rf_reference_spot_check': {'scientific_stop': False, 'worst_ratio': 0.3}, 'P_sha256': 'p', 'high_sha256': 'h'}
if mode == 'spot': rec = spot
elif mode == 'spot_failed': rec = dict(spot, completeness_v913=dict(spot['completeness_v913'], failed=True, false_checks=['rf_spot_check_ratios_le_1']))
elif mode == 'full_good': rec = full
elif mode == 'full_malformed': rec = {k: v for k, v in full.items() if k != 'frozen32_maxima'}; rec['completeness_v913'] = dict(rec['completeness_v913'], missing_records=['frozen32_maxima'], failed=True)
elif mode == 'full_untyped_failed': rec = dict(full, completeness_v913=dict(full['completeness_v913'], failed=''))
elif mode == 'full_no_integral': rec = {k: v for k, v in full.items() if k != 'tight_independent_integral'}
elif mode == 'full_integral_failed': rec = dict(full, tight_independent_integral={'J_abs': 4.2e-9, 'accuracy_passed': False})
elif mode == 'nan_token': open(out, 'w').write('{"completeness_v913": {"mode": "full", "is_full_assessment": true, "failed": false}, "rf_reference_spot_check": {"scientific_stop": false, "worst_ratio": NaN}, "P_sha256": "p"}'); sys.exit(0)
elif mode == 'inf_number': open(out, 'w').write('{"completeness_v913": {"mode": "full", "is_full_assessment": true, "failed": false}, "rf_reference_spot_check": {"scientific_stop": false, "worst_ratio": 1e999}, "P_sha256": "p"}'); sys.exit(0)
elif mode == 'exit1': print('injected failure', file=sys.stderr); sys.exit(1)
elif mode == 'unparsable': open(out, 'w').write('{broken'); sys.exit(0)
json.dump(rec, open(out, 'w')); sys.exit(0)
'''
res = {'cadence_path': str(src), 'cadence_sha256': hashlib.sha256(src.read_bytes()).hexdigest(), 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'cases': {}}
def record(name, ok, **info): res['cases'][name] = {'passed': bool(ok), **info}; print(name, 'PASS' if ok else 'FAIL', json.dumps(info, default=str)[:300], flush=True)
with tempfile.TemporaryDirectory(dir=str(out_json.parent)) as td:
    td = Path(td); shutil.copy(src, td/'assess_cadence860.py'); (td/'assess860.py').write_text(STUB)
    assert hashlib.sha256((td/'assess_cadence860.py').read_bytes()).hexdigest() == res['cadence_sha256']
    def run(mode):
        root = td/('camp_'+mode); root.mkdir(); cand = root/'cand.json'; cand.write_text(json.dumps({'P_raw_chart_hex': [], 'high_hex': []}))
        (root/'state.json').write_text(json.dumps({'candidate_path': str(cand), 'accepted': 3, 'validation': {'J_abs': 4.2e-9}, 'objective': 4.2e-9, 'P': [1.8, 0.1], 'high': [0.0], 'candidate_sha256': hashlib.sha256(cand.read_bytes()).hexdigest()}))
        env = dict(os.environ, CADENCE_STUB_MODE=mode); p = subprocess.run([sys.executable, '-B', str(td/'assess_cadence860.py'), str(root), 'manifest.json', '1'], capture_output=True, text=True, env=env, cwd=str(td))
        rows = [json.loads(l) for l in (root/'assessments'/'ledger.jsonl').read_text().splitlines()] if (root/'assessments'/'ledger.jsonl').exists() else []
        return p, rows, (root/'STOPPED_FOR_DIAGNOSIS').exists(), ((root/'STOPPED_FOR_DIAGNOSIS').read_text() if (root/'STOPPED_FOR_DIAGNOSIS').exists() else None)
    p, rows, marker, mtext = run('spot')
    record('spot_only_record_refused_first_with_marker_and_row', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop') is True and rows[0].get('scientific_stop_sources') == ['spot_only_record_not_a_full_assessment'] and marker and 'spot_only_record_not_a_full_assessment' in mtext and 'E_f_frozen' not in rows[0] and 'KeyError' not in p.stderr, returncode=p.returncode, sources=rows[0].get('scientific_stop_sources') if rows else None, reason=rows[0].get('refusal_reason') if rows else None, stderr=p.stderr[-300:])
    p, rows, marker, mtext = run('spot_failed')
    record('failed_spot_only_record_refused', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop_sources') == ['spot_only_record_not_a_full_assessment'] and marker and 'KeyError' not in p.stderr, returncode=p.returncode, stderr=p.stderr[-300:])
    p, rows, marker, mtext = run('full_malformed')
    record('full_record_missing_frozen32_maxima_is_a_committed_refusal_not_a_KeyError', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop') is True and marker and 'KeyError' not in p.stderr and rows[0].get('completeness', {}).get('missing_records') == ['frozen32_maxima'], returncode=p.returncode, sources=rows[0].get('scientific_stop_sources') if rows else None, completeness=rows[0].get('completeness') if rows else None, stderr=p.stderr[-300:])
    p, rows, marker, mtext = run('full_good')
    record('good_full_record_row_failed_False_no_marker_completeness_recorded', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is False and rows[0].get('scientific_stop') is False and not marker and rows[0].get('mode') == 'full' and rows[0].get('is_full_assessment') is True and rows[0].get('completeness', {}).get('missing_records') == [] and rows[0].get('E_f_frozen') == 1e-10 and rows[0].get('returncode') == 0 and isinstance(rows[0].get('output_sha256'), str), returncode=p.returncode, row_keys=sorted(rows[0].keys()) if rows else None, stderr=p.stderr[-300:])
    p, rows, marker, mtext = run('full_untyped_failed')
    record('full_record_with_failed_empty_string_is_failed', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop') is True and marker, returncode=p.returncode, sources=rows[0].get('scientific_stop_sources') if rows else None)
    p, rows, marker, mtext = run('full_no_integral')
    record('full_record_without_tight_integral_refused_E7', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop_sources') == ['full_record_without_passed_tight_integral'] and marker and 'E_f_frozen' not in rows[0] and 'KeyError' not in p.stderr, returncode=p.returncode, reason=rows[0].get('refusal_reason') if rows else None)
    p, rows, marker, mtext = run('full_integral_failed')
    record('full_record_with_integral_accuracy_False_refused_E7', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop_sources') == ['full_record_without_passed_tight_integral'] and marker, returncode=p.returncode, reason=rows[0].get('refusal_reason') if rows else None)
    p, rows, marker, mtext = run('nan_token')
    raw = (Path(td)/'camp_nan_token'/'assessments'/'ledger.jsonl').read_text()
    record('output_with_bare_NaN_token_refused_ledger_has_no_bare_NaN_E9', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop_sources') == ['unparsable_assessment_output'] and 'nonfinite JSON token' in (rows[0].get('refusal_reason') or '') and marker and all(json.loads(l, parse_constant=lambda t: (_ for _ in ()).throw(ValueError(t))) is not None for l in raw.splitlines() if l.strip()), returncode=p.returncode, reason=rows[0].get('refusal_reason') if rows else None)
    p, rows, marker, mtext = run('inf_number')
    raw = (Path(td)/'camp_inf_number'/'assessments'/'ledger.jsonl').read_text()
    record('output_with_overflowing_number_1e999_refused_R5', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop_sources') == ['unparsable_assessment_output'] and 'nonfinite JSON number' in (rows[0].get('refusal_reason') or '') and marker and all(json.loads(l, parse_constant=lambda t: (_ for _ in ()).throw(ValueError(t))) is not None for l in raw.splitlines() if l.strip()), returncode=p.returncode, reason=rows[0].get('refusal_reason') if rows else None)
    p, rows, marker, mtext = run('exit1')
    record('process_exit_1_is_a_failed_row_with_marker', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop_sources') == ['assessment_process_failed_v913a'] and marker and 'assessment_process_failed' in mtext, returncode=p.returncode)
    p, rows, marker, mtext = run('unparsable')
    record('unparsable_output_is_a_committed_refusal', p.returncode == 0 and len(rows) == 1 and rows[0].get('failed') is True and rows[0].get('scientific_stop_sources') == ['unparsable_assessment_output'] and marker and 'KeyError' not in p.stderr, returncode=p.returncode, stderr=p.stderr[-300:])
res['passed'] = all(c['passed'] for c in res['cases'].values()); out_json.write_text(json.dumps(res, indent=1, default=str)+'\n'); print('ALL PASSED' if res['passed'] else 'SOME FAILED')
