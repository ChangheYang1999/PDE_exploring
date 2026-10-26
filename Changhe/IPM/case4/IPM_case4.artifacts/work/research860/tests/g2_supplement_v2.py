"""G2 supplement, version 2 (new file; lead ruling 09:2xZ): the check T2.6b_old_and_new_production_share_the_far_cancellation of g2_supplement.py (whose premise
predates the v7/v9 repairs) is replaced by (a) a gate on the new production R_f against hp50 at e^32 and e^44 (band ratio <= 1e-11) and (b) a diagnostic without
pass/fail recording the old route's band ratio and old/new. A --dry-run argument performs every import and the input setup, then exits 0 (guarded dev check
before a freeze). Version 1 text: G2 supplement (lead ruling 04:29Z): T2.7 all-generator production vs hp860 (>=50 digits), T2.6b Jacobian spot columns at e^24/e^32/e^44,
T3.4b fresh processes and 1/4/8 threads bitwise, T3.7b independent integrals at exact dilations, T3.8 widths baseline, T5 seed immutability.
Usage: g2_supplement_v2.py <out.json> <manifest.json> [workers] [--dry-run]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, os, subprocess, sys, time, gc
from decimal import Decimal, localcontext
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import basis860 as B, hp860 as H
from origin860 import generator_polynomial, field_series, ORIGIN_ORDER
from highprecision_origin import _fields, evaluate_series
from fields860 import residual as new_residual, fields as new_fields
from integrate860 import independent_integral
from spectral_basis import evaluate_modes
from model860 import production_generator_matrices      # the provider Model860 actually uses (scalar-exp low block, longdouble high block)
from fields860 import generator_matrices as stateless_generator_matrices
from absolute_common import read, ROOT, A_REF, digest, array_hash
from absolute_fields import prepare_candidate
from absolute_fields_v2 import residual as old_residual
from absolute_model import FrozenLogMesh
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'tools')); from runtime import Runtime
rt = Runtime(str(Path(__file__).resolve().parents[2]))
argv = [a for a in sys.argv[1:] if a != '--dry-run']; DRY = '--dry-run' in sys.argv
out_path = Path(argv[0]); manifest_path = Path(argv[1]); workers = int(argv[2]) if len(argv) > 2 else 8
out = {'schema': 'g2_supplement_v2', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'timings': {}, 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))     # SPEC v8 item 3
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
D = Decimal; FIELDS7 = ('f', 'fx', 'fy', 'psi', 'psix', 'psiy', 'ratio')
seed_dir = Path(((_artifact_root + "/outputs") + '/campaign860/seed')); seed = json.loads((seed_dir/'seed_860.json').read_text()); sd = np.load(seed_dir/'seed_860.npz')
P = sd['P'].copy(); high = sd['high'].copy(); r_seed = sd['residual'].copy(); cl_seed = float(P[0])
if DRY:
    prep_dry = B.prepare(cl_seed, P[1:], high); state_dry = rt.read(ROOT/'campaign/global181_v3/state.json'); epoch_dry = rt.read(state_dry['epoch_path']); FrozenLogMesh.load(epoch_dry['meshes']['training']['path'])
    print('DRY RUN OK: imports, seed, prepared state, epoch and mesh paths resolve', flush=True); raise SystemExit(0)
# ---------------- T2.7: production float values of all 860 generators vs hp860 at >= 50 digits
BANDS = [(0, .02), (.02, .1), (.1, 1), (1, 10), (10, 1e3), (1e3, math.exp(16)), (math.exp(16), 2.6e10)]
radii = [(1e-3, .0199), (.03, .095), (.2, .9), (2., 8.), (30., 900.), (3e3, 3e6), (1e7, 2.5e10)]
pts = []
for b, (ra, rb) in enumerate(radii):
    for r in (ra, rb):
        for th in (0., .7, math.pi/2):
            x = r*math.cos(th); y = r*math.sin(th)
            if th == math.pi/2: x = 0.
            if th == 0.: y = 0.
            pts.append((b, x, y))
out['T2.7_points'] = [{'band': b, 'x': x, 'y': y} for b, x, y in pts]
t27 = time.time(); summary = {}
for cl in (cl_seed, 2.5):
    xs = np.array([p[1] for p in pts]); ys = np.array([p[2] for p in pts]); small = np.hypot(xs, ys) <= .02; bands = np.array([p[0] for p in pts])
    # production direct values (r > 0.02) for all generators: low_matrices + evaluate_modes, with cl derivatives
    pm = production_generator_matrices(cl, xs[~small], ys[~small], True, False); sm = stateless_generator_matrices(cl, xs[~small], ys[~small], True, False)
    prod = {key: np.empty((len(pts), 860)) for key in FIELDS7}; dprod = {key: np.empty((len(pts), 860)) for key in FIELDS7}
    prodn = {key: np.empty((len(pts), 860)) for key in FIELDS7}; dprodn = {key: np.empty((len(pts), 860)) for key in FIELDS7}
    for key in FIELDS7:
        prod[key][~small] = pm[key]; dprod[key][~small] = pm['d_'+key]; prodn[key][~small] = sm[key]; dprodn[key][~small] = sm['d_'+key]
    # production origin-series values (r <= 0.02): per-generator polynomial fields (the same routines as production field_series)
    with localcontext() as ctx:
        ctx.prec = 90; L = D.from_float(cl)
        for col in range(860):
            kind, tr = ('low', B.LOW[col]) if col < 60 else ('high', B.HIGH[col-60])
            chi, dchi = generator_polynomial(kind, tr, L, ORIGIN_ORDER+4); ff = _fields(chi, ORIGIN_ORDER); dff = _fields(dchi, ORIGIN_ORDER)
            for key in FIELDS7:
                prod[key][small, col] = evaluate_series(ff[key], xs[small], ys[small]); dprod[key][small, col] = evaluate_series(dff[key], xs[small], ys[small])
                prodn[key][small, col] = prod[key][small, col]; dprodn[key][small, col] = dprod[key][small, col]      # origin series is provider independent
    # hp reference at 50 digits (own evaluator, frozen N_n) for every generator at every point, values and cl derivatives
    hp = {key: np.empty((len(pts), 860)) for key in FIELDS7}; dhp = {key: np.empty((len(pts), 860)) for key in FIELDS7}
    for i, (b, x, y) in enumerate(pts):
        for col in range(860):
            kind, tr = ('low', B.LOW[col]) if col < 60 else ('high', B.HIGH[col-60])
            g = H.generator_fields(kind, tr, cl, x, y, 50); dg = H.generator_fields(kind, tr, cl, x, y, 50, cl_derivative=True)
            for key in FIELDS7: hp[key][i, col] = float(g[key]); dhp[key][i, col] = float(dg[key])
    worst = 0.; worst_d = 0.; detail = {}; per_gen = np.zeros(860); per_gen_d = np.zeros(860); floor_only = set(); floor_cases = []; worst_numpy = 0.
    for key in FIELDS7:
        for b in range(len(BANDS)):
            sel = bands == b
            bmax = np.max(abs(hp[key][sel]), axis=0); scale = np.maximum(bmax, 1e-30); err = np.max(abs(prod[key][sel]-hp[key][sel]), axis=0); ratio = err/scale
            dbmax = np.max(abs(dhp[key][sel]), axis=0); dscale = np.maximum(dbmax, 1e-30); derr = np.max(abs(dprod[key][sel]-dhp[key][sel]), axis=0); dratio = derr/dscale
            # rule: |difference| <= 1e-11 * max(band_max, 1e-30). Every (generator, quantity, band) with band_max < 1e-30 is listed; those that would fail without the floor are listed separately.
            for g_ in np.flatnonzero(bmax < 1e-30): floor_cases.append([int(g_), key, b, float(bmax[g_]), float(err[g_])])
            for g_ in np.flatnonzero(dbmax < 1e-30): floor_cases.append([int(g_), 'dcl_'+key, b, float(dbmax[g_]), float(derr[g_])])
            for g_ in np.flatnonzero((bmax < 1e-30) & (err > 1e-11*np.maximum(bmax, 1e-300)) & (ratio <= 1e-11)): floor_only.add(int(g_))
            for g_ in np.flatnonzero((dbmax < 1e-30) & (derr > 1e-11*np.maximum(dbmax, 1e-300)) & (dratio <= 1e-11)): floor_only.add(int(g_))
            # stateless NumPy provider (diagnostic only)
            ratio_n = np.max(abs(prodn[key][sel]-hp[key][sel]), axis=0)/scale; dratio_n = np.max(abs(dprodn[key][sel]-dhp[key][sel]), axis=0)/dscale
            worst_numpy = max(worst_numpy, float(ratio_n.max()), float(dratio_n.max()))
            detail['%s_band%d' % (key, b)] = {'worst_ratio': float(ratio.max()), 'worst_generator': int(np.argmax(ratio)), 'worst_dcl_ratio': float(dratio.max()), 'worst_dcl_generator': int(np.argmax(dratio))}
            per_gen = np.maximum(per_gen, ratio); per_gen_d = np.maximum(per_gen_d, dratio); worst = max(worst, float(ratio.max())); worst_d = max(worst_d, float(dratio.max()))
    def gen_name(g_): return ('low', B.LOW[g_]) if g_ < 60 else ('high', B.HIGH[g_-60])
    blocks = {}
    for g_ in range(860):
        kind, tr = gen_name(g_); j = tr[2]; key_ = '%s_j%d' % (kind, j)
        blk = blocks.setdefault(key_, {'worst_field_ratio': 0., 'worst_field_generator': None, 'worst_dcl_ratio': 0., 'worst_dcl_generator': None, 'generators': 0})
        blk['generators'] += 1
        if per_gen[g_] > blk['worst_field_ratio']: blk['worst_field_ratio'] = float(per_gen[g_]); blk['worst_field_generator'] = [kind, list(tr)]
        if per_gen_d[g_] > blk['worst_dcl_ratio']: blk['worst_dcl_ratio'] = float(per_gen_d[g_]); blk['worst_dcl_generator'] = [kind, list(tr)]
    by_mn = {}
    for g_ in range(60, 860):
        m, n, j = B.HIGH[g_-60]; by_mn.setdefault('m%d_n%d' % (m, n), 0.); by_mn['m%d_n%d' % (m, n)] = max(by_mn['m%d_n%d' % (m, n)], float(per_gen[g_]), float(per_gen_d[g_]))
    summary['cl=%.4f' % cl] = {'provider_gated': 'model860.production_generator_matrices: basis860.generator_block in longdouble for all 860 generators (exact exponent differences, falling-factorial radial jets), rounded once; origin disk: production order-48 polynomials', 'rule': '|difference| <= 1e-11 * max(band_max, 1e-30)', 'worst_field_ratio': worst, 'worst_dcl_ratio': worst_d, 'stateless_numpy_provider_worst_ratio_diagnostic': worst_numpy, 'per_block': blocks, 'high_by_m_n_worst_ratio': by_mn, 'floor_only_generators': sorted(floor_only), 'band_max_below_floor_cases_count': len(floor_cases), 'band_max_below_floor_cases_generator_quantity_band_bandmax_err': floor_cases, 'detail_by_field_and_band': detail,
                               'per_generator_worst_ratio': per_gen.tolist(), 'per_generator_worst_dcl_ratio': per_gen_d.tolist()}
    check('T2.7_all_generators_fields_band_scaled_cl%.4f' % cl, worst, 1e-11); check('T2.7_all_generators_dcl_band_scaled_cl%.4f' % cl, worst_d, 1e-11)
out['T2.7'] = summary; out['timings']['T2.7_s'] = time.time()-t27
# ---------------- T2.6b: Jacobian spot columns at e^24, e^32, e^44 (production float vs hp Decimal), plus old-code comparison
prep = B.prepare(cl_seed, P[1:], high); strain = B.center_data(cl_seed)[0]
cand = read(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json'); old_prep = prepare_candidate(cand, 'center_chart')
cols = {'cl': 0}; 
for tr in [(0, 1, 0), (1, 1, 3), (2, 2, 0), (4, 4, 2)]: cols['low_%d_%d_%d' % tr] = B.LOW_INDEX[tr]
for tr in [(0, 0, 0), (5, 17, 1), (4, 12, 2), (9, 16, 3), (0, 20, 0), (3, 0, 0)]: cols['high_%d_%d_%d' % tr] = 60+B.HIGH_INDEX[tr]   # one low and one high per j, plus extras
spot_rows = []
for s_ in (24., 32., 44.):
    for th in (0., .3, math.pi/2):
        x = math.exp(s_)*math.cos(th); y = math.exp(s_)*math.sin(th)
        if th == math.pi/2: x = 0.
        if th == 0.: y = 0.
        rf, dr = new_residual(prep, [x], [y], True); rf_old = float(old_residual(old_prep, [x], [y])[0])
        ref = H.point_reference(prep, x, y, 50, True)      # SPEC v9: Decimal background fields and Decimal center factor (no binary64 intermediates)
        row = {'log_r': s_, 'theta': th, 'Rf_production': float(rf[0]), 'Rf_old_production': rf_old, 'Rf_hp50': ref['Rf'], 'columns': {}}
        for name, idx in cols.items(): row['columns'][name] = {'production': float(dr[0, idx]), 'hp50': float(ref['columns'][idx])}
        spot_rows.append(row)
out['T2.6b_spots'] = spot_rows
worst_cols = {}; worst_Rf = {}
for s_ in (24., 32., 44.):
    rows = [r_ for r_ in spot_rows if r_['log_r'] == s_]
    worst_Rf['e%d' % int(s_)] = {'production_vs_hp_band_ratio': max(abs(r_['Rf_production']-r_['Rf_hp50']) for r_ in rows)/max(max(abs(r_['Rf_hp50']) for r_ in rows), 1e-30),
                                 'old_production_vs_hp_band_ratio': max(abs(r_['Rf_old_production']-r_['Rf_hp50']) for r_ in rows)/max(max(abs(r_['Rf_hp50']) for r_ in rows), 1e-30)}
    for name in cols:
        scale = max(max(abs(r_['columns'][name]['hp50']) for r_ in rows), 1e-30); worst_cols['e%d_%s' % (int(s_), name)] = max(abs(r_['columns'][name]['production']-r_['columns'][name]['hp50']) for r_ in rows)/scale
out['T2.6b_column_band_ratios'] = worst_cols; out['T2.6b_Rf_band_ratios_new_and_old'] = worst_Rf
check('T2.6b_jacobian_spot_columns_e24_band_scaled', max(v for k, v in worst_cols.items() if k.startswith('e24')), 1e-11)
out['T2.6b_note'] = 'v2: the e^24 column gate stands; e^32 and e^44 are gated for the new production R_f (v9 longdouble path, 1e-11 band_max, as in t26 T2.6b); the old 181D binary64 route loses digits there (reported in T2.6b_old_route_far_cancellation_diagnostic), the repaired 860 route does not'
check('T2.6b_new_production_Rf_e32_e44_band_scaled', max(worst_Rf['e32']['production_vs_hp_band_ratio'], worst_Rf['e44']['production_vs_hp_band_ratio']), 1e-11, ratios={k: v['production_vs_hp_band_ratio'] for k, v in worst_Rf.items()}, note='v2: the new production R_f (v9 longdouble path) against hp50 at e^32 and e^44 is GATED at 1e-11 band_max (t26 T2.6b gates the same points)')
out['T2.6b_old_route_far_cancellation_diagnostic'] = {'old_production_vs_hp_band_ratio': {k: v['old_production_vs_hp_band_ratio'] for k, v in worst_Rf.items()}, 'new_production_vs_hp_band_ratio': {k: v['production_vs_hp_band_ratio'] for k, v in worst_Rf.items()}, 'old_over_new': {k: (v['old_production_vs_hp_band_ratio']/v['production_vs_hp_band_ratio'] if v['production_vs_hp_band_ratio'] else None) for k, v in worst_Rf.items()}, 'pass_fail': None, 'note': 'diagnostic only (v2): the 181D binary64 route keeps its far cancellation; the repaired 860 route no longer shares it (lead ruling), so the old v1 premise "old and new share the far cancellation" is withdrawn'}
# ---------------- T3.4b: two fresh processes, threads 1/4/8, bitwise vs seed residual
state = rt.read(ROOT/'campaign/global181_v3/state.json'); epoch = rt.read(state['epoch_path']); mesh_path = epoch['meshes']['training']['path']
code = """
import sys, json, hashlib; sys.path.insert(0, '%s'); import numpy as np
import basis860 as B; from model860 import Model860; from absolute_common import A_REF; from absolute_model import FrozenLogMesh
from threadpoolctl import threadpool_limits, threadpool_info
mesh = FrozenLogMesh.load('%s'); d = np.load('%s'); w = int(sys.argv[1]); th = int(sys.argv[2]); m = Model860(mesh, A_REF, block_size=4096, mode_block=64, workers=w, threads=th); r = m.fun(d['P'], d['high'])
with threadpool_limits(limits=w, user_api='blas'): inside = [(t['internal_api'], t['num_threads']) for t in threadpool_info()]
outside = [(t['internal_api'], t['num_threads']) for t in threadpool_info()]
print(json.dumps({'sha256': hashlib.sha256(np.ascontiguousarray(r).tobytes()).hexdigest(), 'bitwise_vs_seed': bool(np.array_equal(r, d['residual'])), 'diff_norm': float(np.linalg.norm(r-d['residual'])), 'threadpools_inside_model_context': inside, 'threadpools_outside': outside, 'pid': __import__('os').getpid()}))
""" % (str(Path(__file__).resolve().parents[1]), mesh_path, B.REPLAY_REFERENCE_FILE)       # replay reference of the repaired evaluator (written by t3)
runs = []
CONFIGS = [(1, 1), (4, 4), (8, 4), (8, 8), (8, 4)]      # (BLAS workers, cache-build threads): every configuration the campaign, the benchmarks and the gates use (SPEC v9.3 clause (d))
for (w, th) in CONFIGS:
    t0 = time.perf_counter(); res = subprocess.run([sys.executable, '-B', '-c', code, str(w), str(th)], capture_output=True, text=True, env=dict(os.environ))
    try: rep = json.loads(res.stdout.strip().splitlines()[-1])
    except Exception: rep = {'error': res.stderr[-1500:]}
    rep.update(workers=w, cache_threads=th, returncode=res.returncode, seconds=time.perf_counter()-t0); runs.append(rep); print('T3.4b run', rep, flush=True)
out['T3.4b_runs'] = runs
check('T3.4b_fresh_processes_and_threads_bitwise', all(r.get('returncode') == 0 and r.get('bitwise_vs_seed') for r in runs) and len({r.get('sha256') for r in runs}) == 1, replay_reference=B.REPLAY_REFERENCE_FILE, configurations=CONFIGS, note='bitwise agreement of every (workers, cache threads) configuration with the replay reference on the training mesh (SPEC v9.3 clause (d) agreement gate; 64 eps would suffice)')
# ---------------- T3.7b: exact dilations. The continuous J_abs is exactly dilation invariant; one tight independent integral at L = 1 is the
# reference for every L, and the frozen-rule quadrature error at dilation L is J_mesh(L) - J_indep(1) within the integrator's error estimate.
t0 = time.perf_counter(); ii1 = independent_integral(P, high, workers=workers, target_abs=1e-18, dilation=1., initial_upper_log_radius=44.)
dil = {'1.0': {'J_abs': ii1['J_abs'], 'error_abs': ii1['error_abs'], 'accuracy_passed': ii1['accuracy_passed'], 'seconds': time.perf_counter()-t0, 'origin_err': ii1['origin_tail_error_abs'], 'infinity_env': ii1['infinity_tail_error_abs'], 'radial_err': ii1['radial_quadrature_error_abs'], 'angular_err': ii1['angular_quadrature_error_abs']}}
J1 = dil['1.0']['J_abs']; e1 = dil['1.0']['error_abs']
out['T3.7b_independent_dilation'] = dil
check('T3.7b_independent_integral_L1_accuracy', ii1['accuracy_passed'])
from integrate860 import _panel
s_max = ii1['interval_expansions'][-1]['s_max']; far = _panel(prep, 24., s_max, 128, 96, 'gauss', workers)
out['T3.7b_log_r_gt_24_contribution'] = {'s_max_of_integrator': s_max, 'J_contribution_log_r_24_to_smax': far['J'], 'relative_to_J_abs': far['J']/J1, 'envelope_beyond_smax': ii1['infinity_tail_error_abs'], 'integration_error_abs': e1,
                                        'note': 'v2: the new production R_f is gated at e^32 and e^44 (T2.6b, 1e-11 band_max); the log r > 24 contribution is reported for the far-field record, and the integration error bounds its uncertainty'}
# frozen-mesh J at the dilations; quadrature error of the frozen rule at L = J_mesh(L) - J_indep(1) (exact invariance of the continuous J)
mesh = FrozenLogMesh.load(mesh_path); x, y = mesh.coordinates(); root = np.sqrt(2*mesh.weights/(np.pi*A_REF**2))
from fields860 import exact_dilation_fields
from threadpoolctl import threadpool_limits
fm = {}
with threadpool_limits(limits=workers, user_api='blas'):
    for Lf in (1., 1-1e-3, 1+1e-3, 2.):
        ff = exact_dilation_fields(prep, x, y, Lf); rfd = (cl_seed*x-ff['psiy'])*ff['fx']+(cl_seed*y+ff['psix'])*ff['fy']+ff['q']*ff['f']; Jm = float((root*rfd)@(root*rfd)/2)
        fm[str(Lf)] = {'J_mesh': Jm, 'frozen_rule_quadrature_error_vs_independent_L1': Jm-J1, 'relative': (Jm-J1)/J1, 'independent_error_abs': e1}
out['T3.7b_frozen_mesh_dilation'] = fm
check('T3.7b_frozen_rule_dilation_errors_small', max(abs(v['relative']) for v in fm.values()), 1e-9, **{k: v['relative'] for k, v in fm.items()})
# ---------------- T3.8 widths baseline from t0t1.json
t0t1 = json.loads(Path(out_path.parent.parent/'g2_v1'/'t0t1.json').read_text()) if (out_path.parent.parent/'g2_v1'/'t0t1.json').exists() else None
t0t1_path = out_path.parent.parent/'g2_v1'/'t0t1.json'
out['T3.8_widths_baseline'] = {'widths_l_eta': (t0t1 or {}).get('widths'), 'source': str(t0t1_path), 'source_sha256': digest(t0t1_path) if t0t1_path.exists() else None}; check('T3.8_widths_baseline_recorded_and_bound', out['T3.8_widths_baseline']['widths_l_eta'] is not None and out['T3.8_widths_baseline']['source_sha256'] is not None, **out['T3.8_widths_baseline'])
# ---------------- T5: seed immutability (chmod 0444) and hashes; child return code recorded above
replay_file = Path(B.REPLAY_REFERENCE_FILE); files = [seed_dir/'seed_860.json', seed_dir/'seed_860.npz', replay_file]
for f_ in files: os.chmod(f_, 0o444)
out['T5_seed_files'] = {f_.name: {'sha256': digest(f_), 'mode': oct(os.stat(f_).st_mode & 0o777), 'bytes': os.stat(f_).st_size} for f_ in files}
check('T5_seed_files_read_only_0444', all(v['mode'] == '0o444' for v in out['T5_seed_files'].values()), **out['T5_seed_files'])
with np.load(replay_file, allow_pickle=False) as rp: check('T5_replay_reference_coefficients_bitwise_equal_sealed_seed', bool(np.array_equal(rp['P'], P) and np.array_equal(rp['high'], high)), replay_residual_sha256=array_hash(rp['residual']))
from closure860 import loaded_closure; out['import_closure'] = loaded_closure()
out['passed'] = all(c['passed'] for c in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
