"""SPEC section 13 assessment cadence (v8.2 cadence; v9.9 (b) R_f reference spot check stop propagated; version 2) for a campaign root (run by the supervisor between slices):
assess at the seed (before the first slice), at each accepted state whose J_abs <= half of the last assessed one, every 100 accepted
steps, and at the end (STOP present). Runs assess860.py on the incumbent snapshot; on a monitor scientific_stop writes STOPPED_FOR_DIAGNOSIS.
Version 3 (lead A(d), E1, N10, C6): the first test on a parsed output is the mode; a record that is not a full assessment is refused with its marker and ledger row
written (fsync) before any other field is read; every read of the output is guarded (a malformed record is a committed refusal, not a KeyError); the cadence criteria
(J_abs halved, every 100 accepted) use the last VALID full row, never an unvalidated rows[-1]. Exit 0 with the ledger row as the verdict.
Usage: assess_cadence860.py <campaign-root> <manifest> [workers]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, subprocess, sys, time, os, hashlib
from pathlib import Path
root = Path(sys.argv[1]); manifest = sys.argv[2]; workers = sys.argv[3] if len(sys.argv) > 3 else '8'
HERE = Path(__file__).resolve().parent; PY = sys.executable
state_path = root/'state.json'; led = root/'assessments'; led.mkdir(exist_ok=True); ledger = led/'ledger.jsonl'
rows = [json.loads(l) for l in ledger.read_text().splitlines() if l.strip()] if ledger.exists() else []      # S6: an unparsable line raises (never skipped)
def fsync_write(path, text, mode='w'):
    """N10: the ledger rows and STOPPED_FOR_DIAGNOSIS are authorities for the driver gate: written with fsync."""
    with open(path, mode) as f: f.write(text); f.flush(); os.fsync(f.fileno())
def _reject_nonfinite(token): raise ValueError('nonfinite JSON token %s in the assessment output' % token)
def _finite_float(s):
    v = float(s)
    if v != v or v in (float('inf'), float('-inf')): raise ValueError('nonfinite JSON number %s in the assessment output' % s)      # R5 item 4: 1e999 parses to inf without parse_constant
    return v
def strict_loads(text): return json.loads(text, parse_constant=_reject_nonfinite, parse_float=_finite_float)          # E9 (b) / R5: NaN, Infinity, -Infinity tokens and overflowing numbers are refused like a malformed output
def sanitize(value):
    """E9 (b): the ledger rows are authorities for the driver gate: nonfinite floats become null plus '<key>_nonfinite' (dicts) or {'nonfinite': kind} (lists); dumped with allow_nan=False."""
    import math as _m
    if isinstance(value, float): return value if _m.isfinite(value) else None
    if isinstance(value, dict):
        res = {}
        for k, v in value.items():
            if isinstance(v, float) and not _m.isfinite(v): res[k] = None; res[str(k)+'_nonfinite'] = 'nan' if _m.isnan(v) else ('+inf' if v > 0 else '-inf')
            else: res[k] = sanitize(v)
        return res
    if isinstance(value, (list, tuple)): return [({'nonfinite': 'nan' if _m.isnan(v) else ('+inf' if v > 0 else '-inf')} if isinstance(v, float) and not _m.isfinite(v) else sanitize(v)) for v in value]
    return value
def ledger_append(rec): fsync_write(ledger, json.dumps(sanitize(rec), allow_nan=False)+'\n', 'a')
def valid_full(row): return isinstance(row, dict) and row.get('failed') is False and row.get('mode') == 'full' and row.get('is_full_assessment') is True and type(row.get('returncode')) is int and row.get('returncode') == 0
if not state_path.exists():
    cand = Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.json')); reason = 'seed'; accepted = 0; J = None; J_mesh = None; cl_state = None
else:
    st = json.loads(state_path.read_text()); cand = Path(st['candidate_path']); accepted = st['accepted']; J = st['validation']['J_abs']; J_mesh = st.get('objective'); cl_state = float(st['P'][0])
    last = rows[-1] if rows else None; last_valid = next((x for x in reversed(rows) if valid_full(x)), None)                           # C6: cadence criteria use the last VALID full row, never an unvalidated rows[-1]
    import numpy as _np, hashlib as _hl
    P_sha = _hl.sha256(_np.ascontiguousarray(_np.asarray(st['P'], float)).tobytes()).hexdigest(); H_sha = _hl.sha256(_np.ascontiguousarray(_np.asarray(st['high'], float)).tobytes()).hexdigest()
    same = lambda row: row.get('candidate_sha256') == st['candidate_sha256'] or (row.get('P_sha256') == P_sha and row.get('high_sha256') == H_sha)
    if last is None: reason = 'first_assessment_of_campaign'
    elif (root/'STOP').exists() and not (same(last) and last.get('reason') == 'end'): reason = 'end'                              # S6: the end assessment runs on STOP
    elif same(last): reason = None                                                                                                 # the last row (valid or failed) is for this candidate: no repeat; a failed row is the driver's refusal
    elif last_valid is None: reason = 'no_valid_full_assessment_yet'
    elif J is not None and last_valid.get('J_abs') and J <= 0.5*last_valid['J_abs']: reason = 'J_abs_halved'
    elif accepted-(last_valid.get('accepted') or 0) >= 100: reason = 'every_100_accepted'
    elif (root/'STOP').exists(): reason = 'end'
    else: reason = None
if reason is None: print(json.dumps({'cadence': 'no assessment due'})); sys.exit(0)
out = led/('assessment_%s_%d.json' % (reason, time.time_ns()))
t0 = time.time(); rc = subprocess.run([PY, '-B', str(HERE/'assess860.py'), str(out), manifest, str(cand), workers], capture_output=True, text=True)
rec = {'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'reason': reason, 'cl': cl_state, 'J_mesh': J_mesh, 'J_mesh_minus_J_abs': ((J_mesh-J) if (J_mesh is not None and J is not None) else None), 'J_mesh_minus_J_abs_required': bool(cl_state is not None and cl_state < 4/3), 'candidate': str(cand), 'candidate_sha256': hashlib.sha256(cand.read_bytes()).hexdigest(), 'accepted': accepted, 'J_abs': J, 'output': str(out), 'returncode': rc.returncode, 'seconds': time.time()-t0}
def refuse(sources, why):
    """A(d)/E1: the refusal is committed (marker, then ledger row, both fsynced) before any other field of the output is read; the process exits 0 (the row is the verdict)."""
    rec.update(failed=True, scientific_stop=True, scientific_stop_sources=sources, refusal_reason=why)
    fsync_write(root/'STOPPED_FOR_DIAGNOSIS', '%s %s %s sha256 %s\n' % ('+'.join(sources), rec['utc'], out, (hashlib.sha256(out.read_bytes()).hexdigest() if out.exists() else 'missing')))
    ledger_append(rec); print(json.dumps(sanitize({k: v for k, v in rec.items() if k != 'stderr_tail'}), allow_nan=False)); sys.exit(0)
if rc.returncode == 0 and out.exists():
    rec['output_sha256'] = hashlib.sha256(out.read_bytes()).hexdigest()
    try:
        a = strict_loads(out.read_text())                                                                                              # E9 (b): strict parse
        if not isinstance(a, dict): raise ValueError('output is not a JSON object')
    except Exception as exc: rec['stderr_tail'] = rc.stderr[-2000:]; refuse(['unparsable_assessment_output'], '%s: %s' % (type(exc).__name__, exc))
    comp = a.get('completeness_v913'); comp = comp if isinstance(comp, dict) else {}; rec['mode'] = comp.get('mode'); rec['is_full_assessment'] = comp.get('is_full_assessment')
    if comp.get('mode') != 'full' or comp.get('is_full_assessment') is not True:                                                    # ruling 3 / A(d): the FIRST test; nothing else is read before the refusal is durable
        refuse(['spot_only_record_not_a_full_assessment' if comp.get('mode') == 'spot_only' else 'not_a_full_assessment'], 'mode %r, is_full_assessment %r: not a full assessment' % (comp.get('mode'), comp.get('is_full_assessment')))
    ti = a.get('tight_independent_integral')
    if not isinstance(ti, dict) or ti.get('accuracy_passed') is not True:                                                              # E7 (c): a full record needs the tight integral with accuracy_passed exactly True; refused before any other key is read
        refuse(['full_record_without_passed_tight_integral'], 'tight_independent_integral %s, accuracy_passed %r: not a complete full assessment (E7)' % ('missing' if not isinstance(ti, dict) else 'present', ti.get('accuracy_passed') if isinstance(ti, dict) else None))
    try:
        mon = a.get('origin_truncation_monitor') or {}; spot = a.get('rf_reference_spot_check') or {}; rec['origin_monitor_worst'] = mon.get('worst_band_relative'); rec['rf_spot_worst_ratio'] = spot.get('worst_ratio')
        rec['failed'] = comp.get('failed') is not False                                                                                # typed: anything but the boolean False is a failure
        rec['completeness'] = {k: comp.get(k) for k in ('missing_records', 'non_boolean_checks', 'false_checks', 'nonfinite_samples_total', 'kappa_failure', 'invalid_bound_inputs', 'snapshot_arrays_binding_failure')}   # E1: recorded (was swallowed by a comment)
        flags = {'origin_truncation_monitor': mon.get('scientific_stop'), 'rf_reference_spot_check': spot.get('scientific_stop')}
        untyped = [k for k, v in flags.items() if not isinstance(v, bool)]
        rec['scientific_stop'] = bool(rec['failed'] or untyped or any(v is True for v in flags.values()))
        rec['scientific_stop_sources'] = [k for k, v in flags.items() if v is True]+(['failed_assessment_v913a'] if rec['failed'] else [])+(['untyped_scientific_stop_flags: %s' % untyped] if untyped else [])
        rec['E_f_frozen'] = ((a.get('frozen32_maxima') or {}).get('E_f') or {}).get('value'); rec['E_rho_frozen'] = ((a.get('frozen32_maxima') or {}).get('E_rho') or {}).get('value'); rec['E1_L2'] = (((a.get('farfield') or {}).get('E') or {}).get('1') or {}).get('L2')
        rec['P_sha256'] = a.get('P_sha256'); rec['high_sha256'] = a.get('high_sha256')                                                # S6: content binding (the seed row binds to the campaign's initial snapshot by P/high)
        if rec.get('J_abs') is None and isinstance(a.get('tight_independent_integral'), dict): rec['J_abs'] = a['tight_independent_integral'].get('J_abs')   # S6: the seed row carries J_abs from the tight integral
    except Exception as exc: refuse(['malformed_assessment_output'], '%s: %s' % (type(exc).__name__, exc))
    if rec['scientific_stop']: fsync_write(root/'STOPPED_FOR_DIAGNOSIS', '%s %s %s sha256 %s\n' % ('+'.join(rec['scientific_stop_sources']), rec['utc'], out, rec['output_sha256']))
else:
    rec['stderr_tail'] = rc.stderr[-2000:]; rec['failed'] = True; rec['scientific_stop'] = True; rec['scientific_stop_sources'] = ['assessment_process_failed_v913a']; rec['output_exists'] = out.exists()
    fsync_write(root/'STOPPED_FOR_DIAGNOSIS', 'assessment_process_failed %s returncode %s\n' % (rec['utc'], rc.returncode))
ledger_append(rec)
print(json.dumps(sanitize({k: v for k, v in rec.items() if k != 'stderr_tail'}), allow_nan=False))
