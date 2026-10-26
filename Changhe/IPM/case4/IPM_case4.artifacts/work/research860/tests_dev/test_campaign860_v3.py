"""Development regression fixtures for the pending campaign860 v3 driver (F1, F6, F12, F13, F14, F18, F19, F20, F21, F22, SPEC v9.3 section 11 items).
Mock numerics (no production mesh, no optimizer); the real chart/basis helpers are imported for canonical export and widths. Run under the guard:
  bin/grun.sh devcamp env/bin/python -B outputs/dev_v9/pending/tests_dev/test_campaign860_v3.py <out.json>"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, os, sys, time, math
from pathlib import Path
from types import SimpleNamespace
PEND = Path(__file__).resolve().parents[1]; LANE = next(p for p in PEND.parents if (p/'work'/'research860'/'basis860.py').exists())   # lane root found by walking up (works for the pending set and for copies)
sys.path.insert(0, str(LANE/'work/research860')); sys.path.insert(0, str(LANE/'work/tools')); sys.path.insert(0, str(PEND))
import numpy as np
import campaign860 as cm
from fractions import Fraction
from absolute_common import digest, npz
OUT = Path(sys.argv[1]).resolve(); ROOT = OUT.parent/('devcamp_%d' % time.time_ns()); ROOT.mkdir(parents=True)
res = {'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'driver_version': cm.VERSION, 'driver_sha256': digest(PEND/'campaign860.py'), 'source': str(PEND/'campaign860.py'), 'source_sha256': digest(PEND/'campaign860.py'), 'script_sha256': digest(Path(__file__).resolve()), 'cases': {}}   # E10
def record(name, ok, **info): res['cases'][name] = {'passed': bool(ok), **info}; print(name, 'PASS' if ok else 'FAIL', json.dumps(info, default=str)[:300], flush=True)
# ---------------- mocks ----------------
N = 6; rng = np.random.default_rng(3)
P0 = np.zeros(60); P0[0] = 1.8089923602744993; P0[1:5] = [3.47, -0.0585, 0., 0.]; HIGH0 = np.zeros(800); R0 = np.array([1., -2., .125, 4., -.5, .25])*1e-3
KNOBS = {'prediction_factor': 1.0, 'decrease_factor': 0.3, 'cond': 1e-30, 'fault_in_fun': False, 'lift_cl': None, 'nan_prediction': False, 'lift_raise': False, 'validate_raise': False, 'model_raises_nonfinite': False, 'free_cl': 0., 'mu_none': False, 'trial_objective': None}
class MockModel:
    def __init__(self): self.root = np.ones(N); self.mesh = SimpleNamespace(size=N, weights=np.full(N, math.pi*cm.A_REF**2/2)); self.calls = 0
    def fun(self, P, g):
        self.calls += 1
        if KNOBS['fault_in_fun'] and self.calls == 2: raise cm.ProcessFault('phase trial_fun: injected fault')      # second call of a resumed slice = the first trial evaluation
        if KNOBS.get('model_raises_nonfinite') and self.calls == 2: raise ValueError('Nonfinite residual/Jacobian')   # S2: the frozen Model860 raises this exact message
        if KNOBS.get('trial_objective') is not None and self.calls >= 2: return R0*math.sqrt(2*KNOBS['trial_objective']/float(R0@R0))   # C18 fixtures: trial residual with objective exactly J_trial (0 or 2e-252)
        d = float(np.sum(np.abs(P-P0)))          # low coordinates only; the 800 high coordinates do not change the mock residual
        return R0*math.exp(-1e2*d)             # slow monotone decrease with the distance from the seed (a realistic trial changes J by a small fraction)
    def jacobian(self, P, g): return rng.normal(size=(N, 860))
    def condition_sums(self, P, g): return np.full(N, KNOBS['cond'])
    def cache_record(self): return {}
    def clear_cache(self): pass
class MockChart:
    def __init__(self, P): self.base = np.asarray(P, float).copy(); self.base_tangent = np.zeros((60, 55)); self.base_tangent[1:56, :] = np.eye(55)*1e-3; self.free = np.zeros((60, 55)); self.free[1:56, :] = np.eye(55)*1e-3; self.free[0, 0] = KNOBS.get('free_cl', 0.); self.geometry_diagnostics = {}
    def lift_delta(self, q):
        P = self.base.copy(); P[1:56] += 1e-3*np.asarray(q)
        if KNOBS['lift_cl'] is not None: P[0] = KNOBS['lift_cl']
        if KNOBS.get('lift_raise'): raise np.linalg.LinAlgError('singular corrector (injected)')
        self.last_diagnostics = {'version': 'mock', 'iterations': [{'iteration': 0, 'constraint_norm': 1e-13, 'max_abs': 1e-14}], 'final': {'max_abs': 1e-14}}
        return P
def mock_hp(P, precision=70):
    a = 14.7677299906064821+float(np.sum(P[1:5]))*1e-3
    return {'coefficients_decimal': ['-3.611632420753814241569187726598932770153']+[repr(float(x)) for x in P[1:]], 'jets': {'a': repr(a), 'b': '-1.9114346882852563', 'c': '-3.0365562924598995', 'h': repr(P[0]-1)},
            'constraints': [1e-14]*5, 'max_abs': 1e-14, 'a0': a, 'physical_bounds': True, 'constraints_decimal': ['1e-14']*5, 'center_abs': 0., 'poisson_max_abs': 0.}
class MockFactors:
    def __init__(self, A, r): self.s = np.linspace(1, 2, 855); self.diagnostic_rank = 855; self.rank_floor = 1e-16; self.r = r
    def stationarity(self): return {'full_range_projected_residual_relative': 1.}
    def step(self, radius):
        # consistent with MockModel.fun and MockChart.lift_delta: the trial moves 55 coordinates by 1e-3 * 1e-3 * min(radius, 1), so d grows by 55e-6 min(radius, 1)
        # and J_trial = J exp(-2e4 * 55e-6 min(radius, 1)); the prediction is that decrease divided by 1.05 (gain ratio 1.05)
        J = float(self.r@self.r/2); dec = J*(1-math.exp(-2e2*55e-6*min(radius, 1.))); pred = float('nan') if KNOBS['nan_prediction'] else dec/1.05*KNOBS['prediction_factor']
        return np.full(855, 1e-3)*min(radius, 1.), {'actual_matrix_predicted_decrease': pred, 'lagrange_multiplier': (None if KNOBS.get('mu_none') else 0.)}
class MockIntegrator:
    def __init__(self, epoch, workers=1): self.record = epoch
    def validate(self, P, g, coarse_r=None, predicted_reduction=None, reference=None):
        if KNOBS.get('validate_raise'): raise RuntimeError('injected integrator failure')
        J = float(coarse_r@coarse_r/2); return {'schema': 'mock', 'J_abs': J, 'error_abs': 1e-30, 'accuracy_passed': True, 'requires_refinement': False}
epoch_file = ROOT/'epoch.json'; epoch_file.write_text(json.dumps({'meshes': {'training': {'path': 'mock-train', 'fingerprint': 'fp-train'}, 'refined': {'path': 'mock-refined', 'fingerprint': 'fp-ref'}}})+'\n')
cm.make_model = lambda mesh, workers, threads=1: MockModel()
cm.C = SimpleNamespace(Chart860=MockChart, hp_report=mock_hp)
cm.feasible_matrix = lambda J, chart, column_scales=None: (rng.normal(size=(N, 855)), np.ones(855) if column_scales is None else np.asarray(column_scales))
REAL_KKT = cm.actual_matrix_kkt
cm.DenseTrustModel = MockFactors; cm.actual_matrix_kkt = lambda A, r, step, sub: 0.
cm.Integrator860 = MockIntegrator
cm.epoch_record = lambda: (json.loads(epoch_file.read_text()), {'epoch_path': str(epoch_file), 'epoch_sha256': digest(epoch_file)})
cm.FrozenLogMesh = SimpleNamespace(load=lambda path: SimpleNamespace(fingerprint='fp-train' if 'train' in path else 'fp-ref', size=N))
cm.verify_binding = lambda manifest, directory, slice_number, check_source=True: {'record_sha256': 'mock-verification', 'record_path': 'mock'}
cm.provenance = lambda: {'mock': True}
cm.HB_INTERVAL = 0.002
seed_json = ROOT/'seed.json'; seed_npz = ROOT/'seed.npz'; manifest = ROOT/'manifest.json'
seed_json.write_text(json.dumps({'P_raw_chart_hex': [float(v).hex() for v in P0], 'high_hex': [float(v).hex() for v in HIGH0]})); npz(seed_npz, P=P0, high=HIGH0, residual=R0)
COV = [{'set': 'T2.6c_finite_v92', 'covered': True, 'count': 19, 'reason': None}, {'set': 'T2.6x_parameter_values', 'covered': True, 'count': 4, 'reason': None}, {'set': 'T2.6d', 'covered': False, 'count': None, 'reason': 'mock: embedded configuration equal to the batch shape'}, {'set': 'T3.6_diagnosed_points', 'covered': True, 'count': 0, 'reason': None}, {'set': 'near_y_axis_training_nodes_v913', 'covered': True, 'count': 4, 'reason': None}]
src_step = ROOT/'kappa_step.json'; src_step.write_text('{"passed": true}\n'); src_kappa = ROOT/'kappa_source.json'; src_kappa.write_text('{"kappa": 2048.0}\n')
SRC = {'source_step_json': str(src_step), 'source_step_json_sha256': digest(src_step), 'source_kappa_json': str(src_kappa), 'source_kappa_json_sha256': digest(src_kappa)}
kappa_file = ROOT/'kappa_calibration_typed.json'; kappa_file.write_text(json.dumps({'kappa': 2048., 'rho_max': 0.2, 'coverage': COV, 'definition': 'mock', **SRC})+'\n')
import kappa860
manifest.write_text(json.dumps({'files': [{'path': str(kappa_file.resolve().relative_to(kappa860.LANE)), 'sha256': digest(kappa_file)}], 'frozen_181_closure': []})+'\n')
def args(root, **kw):
    a = dict(root=str(root), seed_json=str(seed_json), seed_npz=str(seed_npz), manifest=str(manifest), label='dev', seconds=600., workers=1, threads=1, resume=False, initial_radius=None, max_trials=2, reserve_seconds=0., kappa_file=str(kappa_file), override_stop=False, override_reason=None, release_ref=None, config_change_reason=None, skip_assessment_gate=True, budget_renewal_reason=None, benchmark_record=None)
    a.update(kw); return SimpleNamespace(**a)
def commits(root): return [json.loads(p.read_text()) for p in sorted((root/'commits').glob('event_*.json'))]
def fresh(name): r = ROOT/name; r.mkdir(); cm.STOP = False; cm.HB_STOP.clear(); cm.HB_SNAP.clear(); KNOBS.update(prediction_factor=1.0, decrease_factor=0.3, cond=1e-30, fault_in_fun=False, lift_cl=None, nan_prediction=False, lift_raise=False, validate_raise=False, model_raises_nonfinite=False, free_cl=0., mu_none=False, trial_objective=None); return r
os.environ['IPM_RESOURCE_RUN'] = (_artifact_root + "/outputs/test_fixtures/mockrun/20261024T000000Z_1_dev_slice")
# ---- A: initialize + 2 trials, normal slice end, resume (F18 a/b, F12)
r = fresh('A'); st = cm.run(args(r)); cs = commits(r); kinds = [c['trial'].get('kind', 'trial') for c in cs]
comp = sorted((r/'slice_completion').glob('*.json')); last = cs[-1]['post_state']; cache = json.loads((r/'state.json').read_text())
record('A_normal_slice', st == 'checkpointed_slice' and kinds == ['initialization_from_seed', 'slice_start', 'trial', 'trial', 'slice_end'] and last['accepted'] == 2 and cache == last and len(comp) == 1 and comp[0].name == 'slice_0001_20261024T000000Z_1_dev_slice.json', status=st, kinds=kinds, accepted=last['accepted'])
cm.HB_STOP.clear(); st2 = cm.run(args(r, resume=True, max_trials=1)); cs2 = commits(r); kinds2 = [c['trial'].get('kind', 'trial') for c in cs2][len(cs):]
record('A_resume_after_normal_end', st2 == 'checkpointed_slice' and kinds2 == ['slice_start', 'trial', 'slice_end'] and cs2[-1]['post_state']['slices'] == 2, kinds_added=kinds2, status=st2, slices=cs2[-1]['post_state']['slices'], accepted=cs2[-1]['post_state']['accepted'], last_trial_failure=[c['trial'].get('failure') for c in cs2 if c['trial'].get('kind', 'trial') == 'trial'][-1])
# ---- B: STOP file -> stopped_by_request -> resume (F18 c)
r = fresh('B'); (r/'STOP').write_text('x'); st = cm.run(args(r)); (r/'STOP').unlink(); cm.HB_STOP.clear(); st2 = cm.run(args(r, resume=True, max_trials=1))
record('B_stop_file_then_resume', st == 'stopped_by_request' and st2 == 'checkpointed_slice', first=st, second=st2)
# ---- C: fault inside a trial after the proposal: no slice_end; resume commits slice_interrupted and an interrupted outcome (F1, F18 d, F19)
r = fresh('C'); cm.run(args(r, max_trials=1)); KNOBS['fault_in_fun'] = True; cm.HB_STOP.clear(); exc = None
try: cm.run(args(r, resume=True, max_trials=1))
except cm.ProcessFault as e: exc = str(e)
cs = commits(r); last_kind = cs[-1]['trial'].get('kind', 'trial'); KNOBS['fault_in_fun'] = False; cm.HB_STOP.clear()
# the fault was raised before the proposal snapshot (fun raised), so inject an orphan proposal by hand to exercise F1 as well
orphan = r/'trial_proposals'/'trial_00000002_999.json'; orphan.parent.mkdir(exist_ok=True); npz(orphan.with_suffix('.npz'), P=P0, high=HIGH0, residual=R0)
orphan.write_text(json.dumps({'trial': 2, 'arrays_path': str(orphan.with_suffix('.npz')), 'arrays_sha256': digest(orphan.with_suffix('.npz')), 'P_sha256': 'p', 'high_sha256': 'h', 'residual_sha256': 'r', 'radius_before': 1., 'base_candidate_sha256': 'x'})+'\n')
st3 = cm.run(args(r, resume=True, max_trials=1)); cs3 = commits(r); kinds3 = [c['trial'].get('kind', 'trial') for c in cs3]
interrupted = [c for c in cs3 if c['trial'].get('kind') == 'slice_interrupted']; outc = orphan.with_suffix('.outcome.json')
record('C_fault_then_resume_slice_interrupted', exc is not None and last_kind == 'slice_start' and len(interrupted) == 1 and kinds3.count('slice_interrupted') == 1 and outc.exists() and json.loads(outc.read_text())['status'] == 'interrupted_by_process_fault' and st3 == 'checkpointed_slice',
       exception=exc, last_kind_before_resume=last_kind, kinds=kinds3, orphans=interrupted[0]['trial']['reconciliation']['orphans'] if interrupted else None)
# ---- D: outcome written but not committed (F19)
r = fresh('D'); cm.run(args(r, max_trials=1)); prop = r/'trial_proposals'/'trial_00000002_777.json'; npz(prop.with_suffix('.npz'), P=P0, high=HIGH0, residual=R0)
prop.write_text(json.dumps({'trial': 2, 'arrays_path': str(prop.with_suffix('.npz')), 'arrays_sha256': digest(prop.with_suffix('.npz')), 'P_sha256': 'p', 'high_sha256': 'h', 'residual_sha256': 'r', 'radius_before': 1.})+'\n')
oc = prop.with_suffix('.outcome.json'); oc.write_text(json.dumps({'trial': 2, 'accepted': True, 'status': 'accepted'})+'\n'); before = oc.read_bytes()
state = json.loads((r/'state.json').read_text()); rec = cm.reconcile(r, state); kinds = [o['kind'] for o in rec['orphans']]; recon = prop.with_suffix('.reconciliation.json')
record('D_outcome_not_committed', kinds == ['outcome_written_but_not_committed'] and oc.read_bytes() == before and recon.exists() and json.loads(recon.read_text())['status'] == 'outcome_written_but_not_committed' and state['accepted'] == 1, orphan_kinds=kinds, accepted_from_commits=state['accepted'])
# ---- E: damaged trajectory rebuilt atomically (F20)
r = fresh('E'); cm.run(args(r, max_trials=1)); traj = r/'trajectory.jsonl'; traj.write_text(traj.read_text()+'{"event_sequence":'); state = json.loads((r/'state.json').read_text())
r1 = cm.reconcile(r, state); lines1 = traj.read_text().splitlines(); r2 = cm.reconcile(r, state); lines2 = traj.read_text().splitlines()
ok = all(json.loads(l) for l in lines2) and len(lines2) == len(commits(r)) and r1['trajectory']['previous_state'] == 'damaged' and r1['trajectory']['damaged_copy'] and Path(r1['trajectory']['damaged_copy']).exists() and r2['trajectory']['previous_state'] == 'identical'
record('E_trajectory_rebuilt', ok, first=r1['trajectory'], second=r2['trajectory'])
# ---- F: NaN prediction -> committed precision-floor stop; recover returns it; a new run refuses (F22)
r = fresh('F'); cm.run(args(r, max_trials=1)); KNOBS['nan_prediction'] = True; cm.HB_STOP.clear(); st = cm.run(args(r, resume=True, max_trials=1)); cs = commits(r)
stop = [c for c in cs if c['trial'].get('kind') == 'scientific_stop']; diag = json.loads(Path(stop[0]['trial']['diagnosis_path']).read_text()) if stop else {}
cm.HB_STOP.clear(); KNOBS['nan_prediction'] = False; refused = None
try: cm.run(args(r, resume=True, max_trials=1))
except SystemExit as e: refused = str(e)
record('F_nan_prediction_committed_floor_stop', st == 'model_reduction_at_precision_floor' and len(stop) == 1 and diag.get('predicted_decrease') is None and diag.get('predicted_decrease_nonfinite') == 'nan' and cs[-1]['trial'].get('kind') == 'slice_end' and cs[-1]['post_state']['status'] == 'model_reduction_at_precision_floor' and refused is not None,
       status=st, diagnosis={k: diag.get(k) for k in ('predicted_decrease', 'predicted_decrease_nonfinite', 'predicted_decrease_classification')}, refused=refused)
# ---- G: tampered epoch and tampered scales are refused (F13, F6)
r = fresh('G'); cm.run(args(r, max_trials=1)); epoch_file.write_text(json.dumps({'meshes': {'training': {'path': 'mock-train', 'fingerprint': 'fp-train'}, 'refined': {'path': 'mock-refined', 'fingerprint': 'fp-ref'}}, 'relative_accuracy': .25})+'\n'); e1 = None
cm.HB_STOP.clear()
try: cm.run(args(r, resume=True, max_trials=1))
except ValueError as e: e1 = str(e)
epoch_file.write_text(json.dumps({'meshes': {'training': {'path': 'mock-train', 'fingerprint': 'fp-train'}, 'refined': {'path': 'mock-refined', 'fingerprint': 'fp-ref'}}})+'\n')
r = fresh('G2'); cm.run(args(r, max_trials=1)); sc = np.ones(855); sc[17] = 2.; npz(r/'coordinate_map.npz', column_scales=sc, initial_core_tangent=np.zeros((60, 55))); e2 = None; cm.HB_STOP.clear()
try: cm.run(args(r, resume=True, max_trials=1))
except ValueError as e: e2 = str(e)
record('G_epoch_and_scale_tamper_refused', e1 is not None and 'F13' in e1 and e2 is not None and 'F6' in e2, epoch=e1, scales=e2)
# ---- H: widths nulls at the topic 31 / topic 33 points (F14)
w31 = cm.widths({'jets': {'a': '4', 'b': '0', 'c': '0'}}); w33 = cm.widths({'jets': {'a': '1.25', 'b': '0', 'c': '0'}})
record('H_widths_nulls', w31['W_x'] is None and w31['W_y'] is None and w31['l'] is None and w33['eta'] is None and 'W_x' in w31['reasons'], w31=w31['reasons'])
# ---- I: heartbeat thread plus main-thread writes at high rate (F21), HEARTBEAT.json valid at the end
r = fresh('I'); st = cm.run(args(r, max_trials=25)); hb = json.loads((r/'HEARTBEAT.json').read_text()); partials = list(r.glob('HEARTBEAT.json.*partial'))
record('I_heartbeat_single_writer', st == 'checkpointed_slice' and hb.get('note') == 'slice end' and not partials and json.loads((r/'state.json').read_text())['trials'] == 25, status=st, hb_note=hb.get('note'), trials=json.loads((r/'state.json').read_text())['trials'], leftover_partials=len(partials))
# ---- J: exceptional parameter after acceptance (SPEC v9.3 section 11) and rounding-bound floor stop
r = fresh('J'); KNOBS['lift_cl'] = 2.0; st = cm.run(args(r, max_trials=3)); cs = commits(r)
record('J_exceptional_parameter_after_acceptance', st == 'exceptional_parameter_requires_rank_treatment' and cs[-1]['post_state']['accepted'] == 1 and cs[-1]['trial'].get('kind') == 'slice_end', status=st, trials=cs[-1]['post_state']['trials'])
r = fresh('J2'); KNOBS['cond'] = 1e20; st = cm.run(args(r, max_trials=1)); cs = commits(r); stop = [c for c in cs if c['trial'].get('kind') == 'scientific_stop']; diag = json.loads(Path(stop[0]['trial']['diagnosis_path']).read_text()) if stop else {}
record('J2_rounding_bound_floor_stop', st == 'model_reduction_at_precision_floor' and diag.get('reason') == 'rounding_bound' and diag.get('B_ref', 0) > 0, status=st, reason=diag.get('reason'), B_ref=diag.get('B_ref'))
# ---- L: v9.12 (f): a generic exception inside validate is a process fault; a LinAlgError from the lift is a 'lift:' rejection
r = fresh('L'); cm.run(args(r, max_trials=0)); KNOBS['validate_raise'] = True; exc = None; cm.HB_STOP.clear()
try: cm.run(args(r, resume=True, max_trials=1))
except cm.ProcessFault as e: exc = str(e)
KNOBS['validate_raise'] = False; cm.HB_STOP.clear(); r2 = fresh('L2'); KNOBS['lift_raise'] = True; st = cm.run(args(r2, max_trials=1)); cs = commits(r2); fail = [c['trial'].get('failure') for c in cs if c['trial'].get('kind', 'trial') == 'trial']
record('L_fault_vs_rejection_classification', exc is not None and 'RuntimeError' in exc and 'validation' in exc and st == 'checkpointed_slice' and fail and fail[0].startswith('lift: LinAlgError'), fault=exc, lift_failure=fail)
# ---- M / C6 / A(d): fail-closed assessment gate (lead 10:50Z item B; verifier 09:04Z, 10:2xZ) and the driver's spot_only refusal
def gate_setup(name):
    r = fresh(name); cm.run(args(r, max_trials=1)); cm.HB_STOP.clear(); st = json.loads((r/'state.json').read_text()); led = r/'assessments'/'ledger.jsonl'; led.parent.mkdir(exist_ok=True); return r, st, led
def full_output(st, **over):
    d = {'completeness_v913': {'mode': 'full', 'is_full_assessment': True, 'failed': False}, 'origin_truncation_monitor': {'scientific_stop': False}, 'rf_reference_spot_check': {'scientific_stop': False},
         'P_sha256': cm.array_hash(np.asarray(st['P'], float)), 'high_sha256': cm.array_hash(np.asarray(st['high'], float)), 'tight_independent_integral': {'J_abs': st['validation']['J_abs'], 'accuracy_passed': True}}
    for k, v in over.items():
        if isinstance(v, dict) and isinstance(d.get(k), dict): d[k].update(v)
        else: d[k] = v
    return d
def row_for(st, outp, **over):
    row = {'candidate_sha256': st['candidate_sha256'], 'output': str(outp), 'output_sha256': digest(outp), 'returncode': 0, 'reason': 'first_assessment_of_campaign', 'J_abs': st['validation']['J_abs'], 'accepted': st['accepted'], 'mode': 'full', 'failed': False}
    row.update(over); return {k: v for k, v in row.items() if v is not ...}
def gate_run(r):
    cm.HB_STOP.clear(); code = None; status = None
    try: status = cm.run(args(r, resume=True, max_trials=1, skip_assessment_gate=False))
    except SystemExit as e: code = str(e)
    cs = commits(r); ev = [c['trial'] for c in cs if c['trial'].get('kind') == 'assessment']; final = json.loads((r/'state.json').read_text())
    return code, status, ev, final
def gate_case(name, output_dict=None, row_over=None, raw_output_text=None):
    r, st, led = gate_setup(name); outp = r/'assessments'/'assessment_fixture.json'
    if raw_output_text is not None: outp.write_text(raw_output_text)
    else: outp.write_text(json.dumps((output_dict or full_output)(st))+'\n')
    row = row_for(st, outp, **(row_over(st, outp) if row_over else {})); led.write_text(json.dumps(row)+'\n'); return (st,)+gate_run(r)
st, code, status, ev, final = gate_case('M1')
record('M1_good_full_row_counts_slice_runs', code is None and status == 'checkpointed_slice' and len(ev) == 1 and ev[0]['counts_for_gate'] is True and ev[0]['record_valid'] is True and ev[0]['scientific_stop'] is False and final['assessment_reference']['output'].endswith('assessment_fixture.json') and final['assessment_gate']['due'] is False, code=code, status=status, ref=final.get('assessment_reference'))
st, code, status, ev, final = gate_case('M2', lambda st: full_output(st, rf_reference_spot_check={'scientific_stop': True}))
record('M2_output_stop_committed_and_refused', code == '4' and len(ev) == 1 and ev[0]['scientific_stop'] is True and ev[0]['counts_for_gate'] is False and ev[0]['sources'] == ['rf_reference_spot_check'] and final['status'] == 'assessment_scientific_stop', code=code, sources=ev[0]['sources'] if ev else None)
st, code, status, ev, final = gate_case('M3', lambda st: full_output(st, P_sha256='0'*64))
record('M3_foreign_output_never_counts_never_stops', code == '4' and len(ev) == 1 and ev[0]['foreign'] is True and ev[0]['counts_for_gate'] is False and ev[0]['scientific_stop'] is False and final['status'] != 'assessment_scientific_stop' and final['assessment_gate']['due'] is True and final['assessment_gate']['ledger_rows'] == 1 and final['assessment_gate']['rows_counting'] == 0 and final['assessment_gate']['row_reports'][0]['foreign'] is True, code=code, status=final['status'], reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M4', row_over=lambda st, outp: {'output': ...})
record('M4_row_without_output_key_never_counts_never_suppresses', code == '4' and len(ev) == 0 and final['assessment_gate']['due'] is True and final['assessment_gate']['ledger_rows'] == 1 and final['assessment_gate']['rows_counting'] == 0 and 'no output key' in final['assessment_gate']['row_reports'][0]['reason'] and final['status'] != 'assessment_scientific_stop', code=code, reports=final['assessment_gate']['row_reports'])
st, code, status, ev, final = gate_case('M5', row_over=lambda st, outp: {'returncode': False})
record('M5_returncode_False_refused_typed', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and 'not the int 0' in ev[0]['refusal_reason'], code=code, reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M6', lambda st: full_output(st, completeness_v913={'failed': ''}))
record('M6_failed_empty_string_untyped_refused', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and 'untyped' in ev[0]['refusal_reason'], code=code, reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M7', row_over=lambda st, outp: {'returncode': 5})
record('M7_exit_5_row_refused', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and 'returncode 5' in ev[0]['refusal_reason'], code=code, reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M8', row_over=lambda st, outp: {'returncode': 2, 'output': str(outp.with_name('never_written.json'))})
record('M8_rc2_missing_output_refused', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and 'missing' in ev[0]['refusal_reason'], code=code, reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M9', raw_output_text='')
record('M9_empty_output_unreadable_refused', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and 'unreadable' in ev[0]['refusal_reason'], code=code, reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M10', lambda st: {'completeness_v913': {'mode': 'spot_only', 'is_full_assessment': False, 'failed': False, 'partial_record_spot_only': True}, 'rf_reference_spot_check': {'scientific_stop': False}, 'P_sha256': cm.array_hash(np.asarray(st['P'], float)), 'high_sha256': cm.array_hash(np.asarray(st['high'], float))})
record('M10_spot_only_record_refused_first_with_own_reason', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and ev[0]['refusal_reason'].startswith('spot_only_record_not_a_full_assessment') and ev[0]['sources'] == ['spot_only_record_not_a_full_assessment'] and ev[0]['mode'] == 'spot_only', code=code, reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M14', raw_output_text='{"completeness_v913": {"mode": "full", "is_full_assessment": true, "failed": false}, "rf_reference_spot_check": {"scientific_stop": false, "worst_ratio": NaN}}\n')
record('M14_output_with_bare_NaN_token_unreadable_stop', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and 'nonfinite JSON token' in ev[0]['refusal_reason'], code=code, reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M15', raw_output_text='{"completeness_v913": {"mode": "full", "is_full_assessment": true, "failed": false}, "rf_reference_spot_check": {"scientific_stop": false, "worst_ratio": 1e999}}\n')
record('M15_output_with_overflowing_number_1e999_unreadable_stop', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and 'nonfinite JSON number' in ev[0]['refusal_reason'], code=code, reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M12', lambda st: {k: v for k, v in full_output(st).items() if k != 'tight_independent_integral'})
record('M12_full_record_without_tight_integral_refused', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and ev[0]['refusal_reason'].startswith('full_record_without_passed_tight_integral') and ev[0]['sources'] == ['full_record_without_passed_tight_integral'], code=code, reason=ev[0].get('refusal_reason') if ev else None)
st, code, status, ev, final = gate_case('M13', lambda st: full_output(st, tight_independent_integral={'accuracy_passed': False}))
record('M13_full_record_with_integral_accuracy_False_refused', code == '4' and len(ev) == 1 and ev[0]['record_valid'] is False and ev[0]['scientific_stop'] is True and ev[0]['refusal_reason'].startswith('full_record_without_passed_tight_integral'), code=code, reason=ev[0].get('refusal_reason') if ev else None)
# M11: foreign rows only do not suppress (due stays true); a counting row followed by foreign rows still counts
r, st, led = gate_setup('M11'); o1 = r/'assessments'/'foreign.json'; o1.write_text(json.dumps(full_output(st, P_sha256='1'*64, high_sha256='2'*64))+'\n'); o2 = r/'assessments'/'good.json'; o2.write_text(json.dumps(full_output(st))+'\n')
led.write_text(json.dumps(row_for(st, o1, candidate_sha256='f'*64))+'\n'); code1, status1, ev1, final1 = gate_run(r)
led.write_text(json.dumps(row_for(st, o1, candidate_sha256='f'*64))+'\n'+json.dumps(row_for(st, o2))+'\n'+json.dumps(row_for(st, o1, candidate_sha256='f'*64))+'\n'); code2, status2, ev2, final2 = gate_run(r)
record('M11_foreign_rows_do_not_suppress_counting_row_counts', code1 == '4' and final1['assessment_gate']['due'] is True and ev1[0]['foreign'] is True and code2 is None and status2 == 'checkpointed_slice' and final2['assessment_gate']['rows_counting'] == 1 and final2['assessment_reference']['output'] == str(o2), code1=code1, code2=code2, status2=status2)
# ---- C18 (verifier 09:25Z, lead item D): J_trial = 0 and J_trial = 2e-252 stop BEFORE validation and acceptance; nothing accepted, incumbent unchanged
for tag, Jt in (('C18a_zero', 0.), ('C18b_2e-252', 2e-252)):
    r = fresh(tag); KNOBS['trial_objective'] = Jt; st = cm.run(args(r, max_trials=1)); cs = commits(r); kinds = [c['trial'].get('kind', 'trial') for c in cs]; final = json.loads((r/'state.json').read_text())
    init = cs[0]['post_state']; stop_ev = [c['trial'] for c in cs if c['trial'].get('kind') == 'scientific_stop']; trial_ev = [c for c in cs if c['trial'].get('kind', 'trial') == 'trial']
    diag = json.loads(Path(stop_ev[0]['diagnosis_path']).read_text()) if stop_ev else {}
    snaps = sorted(p.name for p in (r/'snapshots').glob('accepted_*'))
    record('%s_precision_floor_stop_before_acceptance' % tag, st == 'model_reduction_at_precision_floor' and kinds.index('scientific_stop') < kinds.index('trial') and final['accepted'] == 0 and final['objective'] == init['objective'] and final['candidate_sha256'] == init['candidate_sha256'] and snaps == [] and diag.get('reason') == 'trial_underflow' and isinstance(diag.get('trial_objective'), float) and abs(diag['trial_objective']-Jt) <= 1e-12*Jt and diag['trial_objective'] < 1e-250 and trial_ev and trial_ev[0]['trial']['accepted'] is False and trial_ev[0]['trial'].get('precision_floor_stop') is True and 'validation_seconds' not in trial_ev[0]['trial'] and 'complete_trial_proposal' not in trial_ev[0]['trial'] and final['rejected'] == 0,
           status=st, kinds=kinds, accepted=final['accepted'], objective_unchanged=final['objective'] == init['objective'], snapshots=snaps, diag_reason=diag.get('reason'))
KNOBS['trial_objective'] = None
# ---- E4 (lead item 11 / fix-check 2): qualified-pair refusals and the positive case, with the benchmark record bound in the campaign's manifest
manifest_e4 = ROOT/'manifest_e4.json'; bench_ok = ROOT/'bench_ok.json'; bench_failed = ROOT/'bench_failed.json'; bench_unbound = ROOT/'bench_unbound.json'
bench_ok.write_text(json.dumps({'passed': True, 'runs': {'w2_t1': {'configuration': {'workers': 2, 'cache_threads': 1}}, 'w1_t1': {'configuration': {'workers': 1, 'cache_threads': 1}}}})+'\n')
bench_failed.write_text(json.dumps({'passed': False, 'runs': {'w2_t1': {'configuration': {'workers': 2, 'cache_threads': 1}}}})+'\n'); bench_unbound.write_text(bench_ok.read_text())
m0 = json.loads(manifest.read_text()); m0['files'] += [{'path': str(bench_ok.resolve().relative_to(cm.LANE)), 'sha256': digest(bench_ok)}, {'path': str(bench_failed.resolve().relative_to(cm.LANE)), 'sha256': digest(bench_failed)}]; manifest_e4.write_text(json.dumps(m0)+'\n')
r = fresh('E4'); cm.run(args(r, max_trials=1, manifest=str(manifest_e4))); outcomes = {}
for label, rec_path in (('unbound', bench_unbound), ('failed', bench_failed), ('ok', bench_ok)):
    cm.HB_STOP.clear()
    try: outcomes[label] = 'status:'+str(cm.run(args(r, resume=True, max_trials=1, manifest=str(manifest_e4), workers=2, threads=1, config_change_reason='fixture E4', benchmark_record=str(rec_path))))
    except ValueError as e: outcomes[label] = 'ValueError:'+str(e)
    except SystemExit as e: outcomes[label] = 'SystemExit:'+str(e)
cs = commits(r); cc = [c['trial'] for c in cs if c['trial'].get('kind') == 'configuration_change']
record('E4_qualified_pairs_refusals_and_positive', outcomes['unbound'].startswith('ValueError') and 'not bound' in outcomes['unbound'] and outcomes['failed'].startswith('ValueError') and 'did not pass' in outcomes['failed'] and outcomes['ok'] == 'status:checkpointed_slice' and len(cc) == 1 and cc[0]['benchmark_record_sha256'] == digest(bench_ok) and cc[0]['workers'] == [1, 2], outcomes=outcomes)
# ---- N: v9.12 (k): exceptional seed c_l is a committed stop at initialization, not a raise
r = fresh('N'); P0[0] = 2.0; seed_json.write_text(json.dumps({'P_raw_chart_hex': [float(v).hex() for v in P0], 'high_hex': [float(v).hex() for v in HIGH0]})); npz(seed_npz, P=P0, high=HIGH0, residual=R0)
st = cm.run(args(r, max_trials=1)); cs = commits(r); kinds = [c['trial'].get('kind', 'trial') for c in cs]
P0[0] = 1.8089923602744993; seed_json.write_text(json.dumps({'P_raw_chart_hex': [float(v).hex() for v in P0], 'high_hex': [float(v).hex() for v in HIGH0]})); npz(seed_npz, P=P0, high=HIGH0, residual=R0)
record('N_init_exceptional_committed_stop', st == 'exceptional_parameter_requires_rank_treatment' and kinds == ['initialization_from_seed', 'scientific_stop'], status=st, kinds=kinds)
# ---- O: v9.12 (d): kappa validation (below 2048, inconsistent rho, unbound sha)
bad = ROOT/'kappa_bad.json'; outcomes = {}
for name, content in (('low', {'kappa': 1000., 'rho_max': 0.1, 'coverage': COV, **SRC}), ('inconsistent', {'kappa': 2048., 'rho_max': 600., 'coverage': COV, **SRC}), ('nocoverage', {'kappa': 2048., 'rho_max': 0.1, **SRC}), ('untyped', {'kappa': 2048., 'rho_max': 0.1, 'coverage': {'T2.6c': 1, 'T2.6x': 1, 'T2.6d': 1, 'T3.6': 1, 'near_y_axis': 1}, **SRC}), ('negative_rho', {'kappa': 2048., 'rho_max': -1., 'coverage': COV, **SRC}), ('badhash', {'kappa': 2048., 'rho_max': 0.1, 'coverage': COV, **dict(SRC, source_step_json_sha256='0'*64)}), ('unbound', {'kappa': 2048., 'rho_max': 0.1, 'coverage': COV, **SRC})):
    bad.write_text(json.dumps(content)+'\n')
    try: cm.load_kappa(SimpleNamespace(kappa_file=str(bad), manifest=str(manifest))); outcomes[name] = 'accepted'
    except ValueError as e: outcomes[name] = str(e)[:40]
record('O_kappa_validation', all(v != 'accepted' for v in outcomes.values()) and cm.load_kappa(SimpleNamespace(kappa_file=str(kappa_file), manifest=str(manifest)))['kappa'] == 2048., outcomes=outcomes)
# ---- P (C2): NaN KKT residual is the committed KKT scientific stop
r = fresh('P'); saved_kkt = cm.actual_matrix_kkt; cm.actual_matrix_kkt = lambda A, r_, step, sub: float('nan'); st = cm.run(args(r, max_trials=1)); cm.actual_matrix_kkt = saved_kkt; cs = commits(r)
stop = [c for c in cs if c['trial'].get('kind') == 'scientific_stop']
record('P_nan_kkt_stops', st == 'full_matrix_trust_subproblem_inaccuracy_requires_diagnosis' and len(stop) == 1 and cs[-1]['trial'].get('kind') == 'slice_end', status=st)
# ---- Q (C3): a nonfinite replay difference fails recovery
r = fresh('Q'); cm.run(args(r, max_trials=1)); state = json.loads((r/'state.json').read_text())
with np.load(state['arrays_path'], allow_pickle=False) as z: arrs = {k: z[k] for k in z.files}
arrs['residual'] = arrs['residual'].copy(); arrs['residual'][0] = float('nan'); npz(state['arrays_path'], **arrs)
state['arrays_sha256'] = digest(state['arrays_path']); last = sorted((r/'commits').glob('event_*.json'))[-1]; lc = json.loads(last.read_text()); lc['post_state']['arrays_sha256'] = state['arrays_sha256']; last.write_text(json.dumps(lc)+'\n'); (r/'state.json').write_text(json.dumps(lc['post_state'])+'\n')
cm.HB_STOP.clear(); e3 = None
try: cm.run(args(r, resume=True, max_trials=1))
except ValueError as e: e3 = str(e)
record('Q_nonfinite_replay_refused', e3 is not None and 'did not reproduce' in e3, error=e3)
# ---- R (C4): stale or missing cache: slice number from the last commit, cache rebuilt
r = fresh('R'); cm.run(args(r, max_trials=1)); (r/'state.json').unlink(); cm.HB_STOP.clear(); st = cm.run(args(r, resume=True, max_trials=1)); cs = commits(r)
record('R_missing_cache_rebuilt_slice_from_commit', st == 'checkpointed_slice' and cs[-1]['post_state']['slices'] == 2 and (r/'state.json').exists(), slices=cs[-1]['post_state']['slices'])
# ---- S (C9): heartbeats are written during a slow initialize (heartbeat starts before initialize/recover)
r = fresh('S'); saved_mm = cm.make_model
class SlowModel(MockModel):
    def fun(self, P, g): time.sleep(0.05); return MockModel.fun(self, P, g)
cm.make_model = lambda mesh, workers, threads=1: SlowModel(); cm.HB_INTERVAL = 0.005; st = cm.run(args(r, max_trials=1)); cm.make_model = saved_mm; cm.HB_INTERVAL = 0.002
hb = json.loads((r/'HEARTBEAT.json').read_text()); kinds = [c['trial'].get('kind', 'trial') for c in commits(r)]
record('S_heartbeat_before_initialize', st == 'checkpointed_slice' and hb.get('note') == 'slice end' and kinds[0] == 'initialization_from_seed', hb_phase_keys=sorted(k for k in hb if k in ('phase', 'slice', 'status')))
# ---- T (B3): a loaded module changed after import stops for diagnosis at slice end
r = fresh('T'); saved_ic = cm.IMPORT_CLOSURE; fake = json.loads(json.dumps(saved_ic)); k0 = sorted(fake['files'])[0]; fake['files'][k0] = '0'*64; cm.IMPORT_CLOSURE = fake; st = cm.run(args(r, max_trials=1)); cm.IMPORT_CLOSURE = saved_ic; cs = commits(r)
record('T_module_change_detected_at_slice_end', st == 'frozen_code_changed_requires_diagnosis' and (r/'STOPPED_FOR_DIAGNOSIS').exists() and cs[-1]['trial'].get('changed_modules') == [k0], status=st, changed=cs[-1]['trial'].get('changed_modules'))
# ---- U (S2): the frozen model's ValueError('Nonfinite residual/Jacobian') inside a trial is the documented 'nonfinite:' rejection, not a fault
r = fresh('U'); cm.run(args(r, max_trials=0)); KNOBS['model_raises_nonfinite'] = True; cm.HB_STOP.clear(); st = cm.run(args(r, resume=True, max_trials=1)); KNOBS['model_raises_nonfinite'] = False
cs = commits(r); fails = [c['trial'].get('failure') for c in cs if c['trial'].get('kind', 'trial') == 'trial']
record('U_model_nonfinite_is_rejection', st == 'checkpointed_slice' and fails and fails[-1].startswith('nonfinite: trial residual (model860 raised') and cs[-1]['post_state']['rejected'] == 1, status=st, failure=fails[-1] if fails else None)
# ---- V (S3): a c_l-bound violation of the uncorrected trial point is labelled 'bound: lower c_l' and counted (v9.11 (1)), and the boundary classification fires after two
r = fresh('V'); KNOBS['free_cl'] = -1e9; st = cm.run(args(r, max_trials=2)); KNOBS['free_cl'] = 0.; cs = commits(r); trials = [c for c in cs if c['trial'].get('kind', 'trial') == 'trial']
bnd = [c['trial'].get('bound_violated') for c in trials]; cnt = cs[-1]['post_state'].get('cl_bound_rejections_total'); bs_ = cs[-1]['trial'].get('boundary_state', {})
record('V_cl_bound_rejection_labelled_and_counted', bnd == ['bound: lower c_l', 'bound: lower c_l'] and cnt == 2 and bs_.get('is_boundary_state') is True and bs_.get('cl_bound_rejections_in_last_12') == 2 and 'dJ_mesh_d_cl_along_named_direction' in bs_, bound_violated=bnd, total=cnt, boundary=bool(bs_.get('is_boundary_state')))
# ---- W (S4): a missing/nonfinite trust multiplier is the (g) KKT stop, not a fault
r = fresh('W'); KNOBS['mu_none'] = True; mock_kkt = cm.actual_matrix_kkt; cm.actual_matrix_kkt = REAL_KKT; st = cm.run(args(r, max_trials=1)); cm.actual_matrix_kkt = mock_kkt; KNOBS['mu_none'] = False; cs = commits(r); stop = [c for c in cs if c['trial'].get('kind') == 'scientific_stop']
diag = json.loads(Path(stop[0]['trial']['diagnosis_path']).read_text()) if stop else {}
record('W_nonfinite_multiplier_is_kkt_stop', st == 'full_matrix_trust_subproblem_inaccuracy_requires_diagnosis' and 'nonfinite multiplier' in str(diag.get('subproblem', {}).get('kkt_value_classification', '')), status=st, classification=diag.get('subproblem', {}).get('kkt_value_classification'))
# ---- X (S7): refusals exit with code 4
r = fresh('X'); cm.run(args(r, max_trials=1)); (r/'STOPPED_FOR_DIAGNOSIS').write_text('x'); cm.HB_STOP.clear(); code = None
try: cm.run(args(r, resume=True, max_trials=1))
except SystemExit as e: code = e.code
record('X_refusal_exit_code_4', code == 4, code=code)
# ---- Y (v9.16): boundary metrics on the actual seed chart: A = I, r = t gives derivative +1 and ||Qg|| at rounding level
import chart860 as RC
seedj = json.loads(Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.json')).read_text()); Pseed = np.array([float.fromhex(h) for h in seedj['P_raw_chart_hex']])
real_chart = RC.Chart860(Pseed); scales1 = np.ones(855); tvec = np.r_[real_chart.base_tangent[0, :]*scales1[:55], np.zeros(800)]
mY = cm.boundary_metrics(np.eye(855), tvec, tvec)
record('Y_boundary_metrics_identity_seed_chart', abs(mY['dJ_mesh_d_cl']-1.) < 1e-12 and mY['Qg_norm'] < 1e-12*mY['t_norm'] and np.count_nonzero(real_chart.base_tangent[0, :]) == 55, dJ=mY['dJ_mesh_d_cl'], Qg_norm=mY['Qg_norm'], t_norm=mY['t_norm'], nonzero_entries=int(np.count_nonzero(real_chart.base_tangent[0, :])))
# ---- Z (v9.16): random A and r against an explicit orthonormal basis of ker(t^T)
rngZ = np.random.default_rng(42); AZ = rngZ.normal(size=(50, 855)); rZ = rngZ.normal(size=50); mZ = cm.boundary_metrics(AZ, rZ, tvec)
Qfull, _ = np.linalg.qr(np.column_stack([tvec, rngZ.normal(size=(855, 854))])); Qker = Qfull[:, 1:]        # orthonormal basis of ker(t^T)
gZ = AZ.T@rZ; Qg_explicit = Qker@(Qker.T@gZ); AQ_explicit = np.linalg.norm(AZ@Qker)
record('Z_boundary_metrics_vs_explicit_kernel_basis', abs(mZ['Qg_norm']-np.linalg.norm(Qg_explicit)) < 1e-9*np.linalg.norm(gZ) and abs(mZ['AQ_frobenius']-AQ_explicit) < 1e-9*np.linalg.norm(AZ) and abs(mZ['tangential_indicator']-np.linalg.norm(Qg_explicit)/(AQ_explicit*np.linalg.norm(rZ))) < 1e-9 and abs(mZ['dJ_mesh_d_cl']-(gZ@tvec)/(tvec@tvec)) < 1e-12*abs(mZ['dJ_mesh_d_cl']), Qg=mZ['Qg_norm'], Qg_explicit=float(np.linalg.norm(Qg_explicit)), AQ=mZ['AQ_frobenius'], AQ_explicit=float(AQ_explicit))
# ---- AA (D3 (f)): the exact rational a_000 of the seed agrees with decimal_center at 90 digits
from exactcheckpoint860 import exact_canonical
from decimal import Decimal, localcontext
Hseed = np.array([float.fromhex(h) for h in seedj['high_hex']]); aX, xrec = exact_canonical(Pseed, Hseed); dc = cm.B.decimal_center(Pseed[0], Pseed, 90)
with localcontext() as cx:
    cx.prec = 100; a000_frac = Fraction(xrec['a000_exact']); diff = abs(Decimal(a000_frac.numerator)/Decimal(a000_frac.denominator)-Decimal(dc['analytic_c0']))
record('AA_exact_a000_vs_decimal_center_90', float(diff) < 1e-85 and len(aX) == 860 and len(xrec['canonical_serialization_sha256']) == 64, difference=float(diff), a000_float=xrec['a000_float'], sha=xrec['canonical_serialization_sha256'][:16])
# ---- K: sanitizer
d = cm.durable({'a': float('nan'), 'b': [1., float('inf'), {'c': float('-inf')}], 'n': np.float64(2.5), 'i': np.int64(3)})
record('K_sanitizer', d == {'a': None, 'a_nonfinite': 'nan', 'b': [1., {'nonfinite': '+inf'}, {'c': None, 'c_nonfinite': '-inf'}], 'n': 2.5, 'i': 3}, value=d)
res['passed'] = all(c['passed'] for c in res['cases'].values()); res['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()); res['fixture_root'] = str(ROOT)
OUT.write_text(json.dumps(res, indent=1, default=str)+'\n'); print('ALL PASSED' if res['passed'] else 'SOME FAILED')
