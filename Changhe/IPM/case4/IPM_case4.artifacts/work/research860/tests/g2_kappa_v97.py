"""SPEC v9.7 rounding-calibration supplement (postprocessing, before the G4 pilot manifest; new file). For the seed coefficients at the seed c_l and at the
T2.6x parameter values (2, 3, 2(1+2^-20), 3(1-2^-20)), at the T2.6c points (FINITE_V92 and the far points e24/e32/e44) and, when outputs/g2/g2_v4/t3.json
exists, at its T3.6 diagnosed points: production R_f in the one-point, batch and stateless shapes; the production condition sums S_R of the SAME path
(Model860.condition_sums for the one-point and batch shapes, fields860.condition_sums for the stateless shape; origin disk: the Decimal residual polynomial
with absolute coefficients, as in production); the unrounded 85-digit Decimal reference (hp860.point_reference Rf_decimal); and
    rho_path = max(0, |R_f(path) - R_f(Decimal)| - 2^-53 |R_f(Decimal)|) / (u S_R(path)),   u = 2^-64,
the final binary64 rounding being charged to the 2^-53 |R_f| term. kappa = max(2^11, 4 rho_max) over every point, parameter value and path.
Writes the step JSON and outputs/campaign860/kappa_calibration.json (refused if it exists). Coverage of the T2.6d points: T2.6d uses the same T2.6c points
(embedded in the training-sized call), so they are covered by the T2.6c set. Usage: g2_kappa_v97.py <out.json> <manifest> [workers]"""
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
from absolute_common import digest
from closure860 import loaded_closure
out_path = Path(sys.argv[1]); manifest_path = Path(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 3 else 4
out = {'schema': 'g2_kappa_v97_v1', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
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
pts = [(name, x, y) for name, x, y in FINITE_V92+FAR]; coverage = {'T2.6c_finite_v92': len(FINITE_V92), 'T2.6b_far': len(FAR), 'T2.6d': 'same T2.6c points embedded in the training-sized call (covered)', 'T3.6_diagnosed_points': 0}
t3 = Path(((_artifact_root + "/outputs") + '/g2/g2_v4/t3.json'))
if t3.exists():
    d3 = json.loads(t3.read_text()); n0 = len(pts)
    for region, diag in (d3.get('T3.6_region_diagnosis') or d3.get('T3.6_diagnosed_points') or {}).items():
        rows = diag if isinstance(diag, list) else diag.get('points', [])
        for row in rows:
            if isinstance(row, dict) and 'x' in row and 'y' in row: pts.append(('T3.6_'+str(region), float(row['x']), float(row['y'])))
    coverage['T3.6_diagnosed_points'] = len(pts)-n0
else: coverage['T3.6_diagnosed_points_note'] = 't3.json absent at run time: T3.6 points not covered (listed as uncovered)'
xs = np.array([p[1] for p in pts]); ys = np.array([p[2] for p in pts]); rows = []; rho_max = 0.; rho_arg = None
for label, cl in CL:
    P = P0.copy(); P[0] = cl; t0 = time.time()
    prepared = B.prepare(cl, P[1:], high); share_prepared(prepared, P, high)
    mb, root_b = point_model(xs, ys, workers=workers); rf_b = mb.fun(P, high)/root_b; S_b = mb.condition_sums(P, high)
    rf_st = stateless_residual(prepared, xs, ys); S_st = stateless_condition_sums(prepared, xs, ys)
    for i, (name, x, y) in enumerate(pts):
        ms, root_s = point_model([x], [y], workers=1); rf_s = float((ms.fun(P, high)/root_s)[0]); S_s = float(ms.condition_sums(P, high)[0]); ms.clear_cache()
        ref = H.point_reference(prepared, float(x), float(y), 85, columns=False)['Rf_decimal']
        rec = {'cl_label': label, 'cl': cl, 'point': name, 'x': float(x), 'y': float(y), 'r': float(math.hypot(x, y)), 'Rf_decimal_85': format(ref, '.40e')}
        with localcontext() as cx:
            cx.prec = 60; charge = D(2)**-53*abs(ref)
            for path, val, S in (('single', rf_s, S_s), ('batch', float(rf_b[i]), float(S_b[i])), ('stateless', float(rf_st[i]), float(S_st[i]))):
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
kfile = Path(((_artifact_root + "/outputs") + '/campaign860/kappa_calibration.json'))
if kfile.exists(): out['kappa_file'] = {'path': str(kfile), 'note': 'exists; not overwritten', 'sha256': digest(kfile)}
else:
    kfile.write_text(json.dumps({'schema': 'kappa_calibration_v97', 'kappa': kappa, 'rho_max': rho_max, 'rho_argmax': rho_arg, 'definition': out['definition'], 'u': U, 'coverage': coverage, 'source_step_json': str(out_path), 'code_manifest_sha256': out['code_manifest_sha256'], 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, indent=1)+'\n')
    out['kappa_file'] = {'path': str(kfile), 'sha256': digest(kfile)}
out['import_closure'] = loaded_closure(); out['passed'] = all(c['passed'] for c in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', 'kappa', kappa, 'rho_max', rho_max, flush=True)
