"""SPEC v9.7 rounding-calibration supplement, version d (new file; version c is frozen in g2_v9 and failed on a missing A_REF import): imports fixed and the
module-level names scanned (outputs/dev_v9/undefined_scan.py). Version c text: SPEC v9.7 rounding-calibration supplement, version c (new file; version b is frozen in g2_v8 and failed at import on an untranslated source-host epoch path, lead S1):
the handoff records are read through Runtime (translated paths). Version b text: SPEC v9.7 rounding-calibration supplement, version b (new file; lead checklist A5 / verifier preflight 08:37:56Z repairs): strict T3.6 parser (region['points'] is a dict
keyed by role with xy coordinates; unexpected schemas are rejected; the t3.json sha256 and point counts are recorded), an existing kappa file is refused (never silently kept),
a failed run publishes no usable kappa file (a .FAILED sidecar instead), the four near-y-axis training nodes of SPEC v9.13 (one per decade in [10, 1e5)) are evaluated in the actual
training-sized production batch configuration (Model860 on the training mesh with its condition sums) and in the three point shapes, and the T2.6d embedded configuration of the
T2.6c points is listed as uncovered with its reason. Version a text: For the seed coefficients at the seed c_l and at the
T2.6x parameter values (2, 3, 2(1+2^-20), 3(1-2^-20)), at the T2.6c points (FINITE_V92 and the far points e24/e32/e44) and, when outputs/g2/g2_v4/t3.json
exists, at its T3.6 diagnosed points: production R_f in the one-point, batch and stateless shapes; the production condition sums S_R of the SAME path
(Model860.condition_sums for the one-point and batch shapes, fields860.condition_sums for the stateless shape; origin disk: the Decimal residual polynomial
with absolute coefficients, as in production); the unrounded 85-digit Decimal reference (hp860.point_reference Rf_decimal); and
    rho_path = max(0, |R_f(path) - R_f(Decimal)| - 2^-53 |R_f(Decimal)|) / (u S_R(path)),   u = 2^-64,
the final binary64 rounding being charged to the 2^-53 |R_f| term. kappa = max(2^11, 4 rho_max) over every point, parameter value and path.
Writes the step JSON and outputs/campaign860/kappa_calibration.json (refused if it exists). Coverage of the T2.6d points: T2.6d uses the same T2.6c points
(embedded in the training-sized call), so they are covered by the T2.6c set. Usage: g2_kappa_v97d.py <out.json> <manifest> [workers]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, sys, time
from decimal import Decimal, localcontext
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import basis860 as B, hp860 as H
from fields860 import residual as stateless_residual, condition_sums as stateless_condition_sums
from shapes860 import point_model, share_prepared
from points860 import FINITE_V92, FAR
from model860 import Model860
from absolute_model import FrozenLogMesh
from absolute_common import ROOT
from absolute_common import digest, A_REF
from closure860 import loaded_closure
out_path = Path(sys.argv[1]); manifest_path = Path(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 3 else 4
out = {'schema': 'g2_kappa_v97d_v1', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
       'definition': 'SPEC v9.7: rho = max(0, |R_f(path) - R_f(Decimal 85)| - 2^-53 |R_f(Decimal)|) / (u S_R(path)), u = 2^-64, S_R from the production path itself (Model860.condition_sums / fields860.condition_sums); kappa = max(2^11, 4 rho_max)'}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
U = 2.**-64; D = Decimal
seed = json.loads(Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.json')).read_text())
P0 = np.array([float.fromhex(h) for h in seed['P_raw_chart_hex']]); high = np.array([float.fromhex(h) for h in seed['high_hex']])
CL = [('seed', float(P0[0])), ('cl2', 2.0), ('cl3', 3.0), ('cl2plus2m20', 2*(1+2**-20)), ('cl3minus2m20', 3*(1-2**-20))]
coverage_cl = {'T2.6x_parameter_values': [c for _, c in CL], 'note': 'the T2.6x parameter values (seed c_l, 2, 3, 2(1+2^-20), 3(1-2^-20)) are covered at every point set below'}
pts = [(name, x, y) for name, x, y in FINITE_V92+FAR]; coverage = {'T2.6c_finite_v92': len(FINITE_V92), 'T2.6b_far': len(FAR), 'T2.6d': 'same T2.6c points embedded in the training-sized call (covered)', 'T3.6_diagnosed_points': 0, **coverage_cl}
kfile = Path(((_artifact_root + "/outputs") + '/campaign860/kappa_calibration.json'))
if kfile.exists(): raise SystemExit('kappa_calibration.json already exists (sha256 %s); this run refuses to overwrite or silently keep it: move it aside with a recorded reason first' % digest(kfile))
t3 = Path(((_artifact_root + "/outputs") + '/g2/g2_v4/t3.json'))
if t3.exists():
    d3 = json.loads(t3.read_text()); n0 = len(pts); diag = d3.get('T3.6_region_diagnosis')
    if not isinstance(diag, dict): raise SystemExit('t3.json: T3.6_region_diagnosis is not a dict (unexpected schema)')
    for region, rec in diag.items():
        if not isinstance(rec, dict) or not isinstance(rec.get('points'), dict): raise SystemExit('t3.json: region %r: points is not a dict keyed by role (unexpected schema)' % region)
        for role, pt in rec['points'].items():
            xy = pt.get('xy') if isinstance(pt, dict) else None
            if not (isinstance(xy, list) and len(xy) == 2 and all(isinstance(v, (int, float)) and math.isfinite(v) for v in xy)): raise SystemExit('t3.json: region %r role %r: xy is not two finite numbers (unexpected schema)' % (region, role))
            pts.append(('T3.6_%s_%s' % (region, role), float(xy[0]), float(xy[1])))
    coverage['T3.6_diagnosed_points'] = len(pts)-n0; coverage['T3.6_source'] = {'path': str(t3), 'sha256': digest(t3), 'regions': len(diag), 'points_per_region': {k: len(v['points']) for k, v in diag.items()}}
else: coverage['T3.6_diagnosed_points_note'] = 't3.json absent at run time: T3.6 points not covered (uncovered set, reason: t3 had not produced its record)'
# SPEC v9.13: the four training nodes closest in angle to the y axis in the decades [10,1e2), [1e2,1e3), [1e3,1e4), [1e4,1e5), evaluated in the training-sized production batch configuration
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'tools')); from runtime import Runtime
RT = Runtime(str(Path(__file__).resolve().parents[2])); state181 = RT.read(ROOT/'campaign/global181_v3/state.json'); epoch = RT.read(state181['epoch_path']); mesh_tr = FrozenLogMesh.load(epoch['meshes']['training']['path'])   # S1: translated handoff paths
mx, my = mesh_tr.coordinates(); mr = np.hypot(mx, my); mth = np.arctan2(my, mx); yaxis_idx = []
for lo, hi in ((10., 1e2), (1e2, 1e3), (1e3, 1e4), (1e4, 1e5)):
    sel = np.flatnonzero((mr >= lo) & (mr < hi)); yaxis_idx.append(int(sel[np.argmin(abs(mth[sel]-np.pi/2))]))
for i in yaxis_idx: pts.append(('near_y_axis_node_%d' % i, float(mx[i]), float(my[i])))
coverage['near_y_axis_training_nodes_v913'] = {'indices': yaxis_idx, 'configurations': ['training_batch (Model860 on the training mesh, production call)', 'single', 'batch', 'stateless']}
coverage['T2.6d_embedded_configuration_of_T2.6c_points'] = 'uncovered by direct evaluation here; reason: g2_v4 t26 T2.6d gated the embedded start/middle/end copies of the T2.6c points in a training-sized call against the one-point and batch shapes with configuration difference 0.0 (bitwise), so the batch-shape rho at those points is the training-sized value; the four near-y-axis training nodes are evaluated in the actual training-sized production call'
root_tr = np.sqrt(2*mesh_tr.weights/(np.pi*A_REF**2))
xs = np.array([p[1] for p in pts]); ys = np.array([p[2] for p in pts]); rows = []; rho_max = 0.; rho_arg = None
for label, cl in CL:
    P = P0.copy(); P[0] = cl; t0 = time.time()
    prepared = B.prepare(cl, P[1:], high); share_prepared(prepared, P, high)
    mb, root_b = point_model(xs, ys, workers=workers); rf_b = mb.fun(P, high)/root_b; S_b = mb.condition_sums(P, high)
    mtr = Model860(mesh_tr, A_REF, block_size=4096, mode_block=64, workers=workers, threads=min(workers, 4)); r_tr = mtr.fun(P, high); S_tr_all = mtr.condition_sums(P, high); mtr.clear_cache()
    rf_tr = {i: float(r_tr[i]/root_tr[i]) for i in yaxis_idx}; S_tr = {i: float(S_tr_all[i]) for i in yaxis_idx}
    rf_st = stateless_residual(prepared, xs, ys); S_st = stateless_condition_sums(prepared, xs, ys)
    for i, (name, x, y) in enumerate(pts):
        ms, root_s = point_model([x], [y], workers=1); rf_s = float((ms.fun(P, high)/root_s)[0]); S_s = float(ms.condition_sums(P, high)[0]); ms.clear_cache()
        ref = H.point_reference(prepared, float(x), float(y), 85, columns=False)['Rf_decimal']
        rec = {'cl_label': label, 'cl': cl, 'point': name, 'x': float(x), 'y': float(y), 'r': float(math.hypot(x, y)), 'Rf_decimal_85': format(ref, '.40e')}
        with localcontext() as cx:
            cx.prec = 60; charge = D(2)**-53*abs(ref)
            paths = [('single', rf_s, S_s), ('batch', float(rf_b[i]), float(S_b[i])), ('stateless', float(rf_st[i]), float(S_st[i]))]
            if name.startswith('near_y_axis_node_'): ni = int(name.rsplit('_', 1)[1]); paths.append(('training_batch', rf_tr[ni], S_tr[ni]))
            for path, val, S in paths:
                err = abs(D.from_float(val)-ref); excess = err-charge
                rho = float(excess/(D(U)*D.from_float(S))) if (excess > 0 and S > 0) else (0. if excess <= 0 else float('inf'))
                rec['Rf_'+path] = val; rec['S_R_'+path] = S; rec['abs_error_'+path] = float(err); rec['rho_'+path] = rho
                if rho > rho_max: rho_max = rho; rho_arg = {'cl_label': label, 'point': name, 'path': path, 'rho': rho, 'S_R': S, 'abs_error': float(err)}
        rows.append(rec)
    out.setdefault('seconds_per_cl', {})[label] = time.time()-t0; mb.clear_cache(); print(label, 'done', round(time.time()-t0), 's', flush=True)
kappa = max(2.**11, 4*rho_max) if math.isfinite(rho_max) else float('inf')
out['rows'] = rows; out['rho_max'] = rho_max; out['rho_argmax'] = rho_arg; out['kappa'] = kappa; out['coverage'] = coverage
check('kappa_v97_finite', bool(math.isfinite(kappa)) and math.isfinite(rho_max)); check('kappa_v97_all_condition_sums_positive', all(r['S_R_'+p] > 0 for r in rows for p in ('single', 'batch', 'stateless')))
check('kappa_v97_rho_max', rho_max, 1e6, note='no pass/fail threshold is set by SPEC v9.7 for rho itself; the record value defines kappa; the 1e6 cap flags a defect', kappa=kappa, argmax=rho_arg)
out['import_closure'] = loaded_closure(); out['passed'] = all(c['passed'] for c in out['checks'])
record = {'schema': 'kappa_calibration_v97b', 'kappa': kappa, 'rho_max': rho_max, 'rho_argmax': rho_arg, 'definition': out['definition'], 'u': U, 'coverage': coverage, 'source_step_json': str(out_path), 'code_manifest_sha256': out['code_manifest_sha256'], 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'passed': out['passed']}
if out['passed'] and not kfile.exists():
    kfile.write_text(json.dumps(record, indent=1)+'\n'); out['kappa_file'] = {'path': str(kfile), 'sha256': digest(kfile)}
else:
    failed = kfile.with_name('kappa_calibration.FAILED_%d.json' % time.time_ns()); failed.write_text(json.dumps(record, indent=1)+'\n'); out['kappa_file'] = {'path': None, 'failed_record': str(failed), 'note': 'a failed run publishes no usable kappa file'}
out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', 'kappa', kappa, 'rho_max', rho_max, flush=True)
