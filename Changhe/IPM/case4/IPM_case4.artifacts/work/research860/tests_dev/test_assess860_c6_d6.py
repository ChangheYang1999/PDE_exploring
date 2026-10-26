"""Fixtures for assess860.py functions extracted by AST from the (pending or frozen) source and executed with their own globals (no production assessment runs):
bind_snapshot (D6 provenance: P/high read from the artifact and compared bitwise, exact (N,) shapes, finite residual, mesh fingerprint and typed configuration from the
artifact, supplied-missing vs not-supplied) and bound_ratio (C6 ruling: zero bound with zero error gives ratio 0; zero bound with nonzero error is invalid, ratio inf;
nonfinite inputs invalid). Records the sha256 of the source and of this script (E10). Usage: test_assess860_c6_d6.py <assess860.py path> <out.json>"""
import ast, json, sys, math, hashlib, tempfile
from decimal import Decimal, localcontext
from pathlib import Path
import numpy as np
src_path = Path(sys.argv[1]).resolve(); src = src_path.read_text(); tree = ast.parse(src); out_json = Path(sys.argv[2]).resolve()
def pick(name):
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == name: return n
    raise KeyError(name)
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
INVALID = []; EXACT = []
ns = {'np': np, 'json': json, 'math': math, 'Path': Path, 'digest': digest, 'Decimal': Decimal, 'localcontext': localcontext, 'INVALID_BOUND_INPUTS': INVALID, 'EXACT_ZERO_BOUNDS': EXACT, 'kappa': 2048., 'U_RF': 2.**-64}
for fn in ('bind_snapshot', 'bound_ratio'): exec(compile(ast.Module(body=[pick(fn)], type_ignores=[]), str(src_path), 'exec'), ns)
bind_snapshot = ns['bind_snapshot']; bound_ratio = ns['bound_ratio']
res = {'source': str(src_path), 'source_sha256': digest(src_path), 'script_sha256': digest(__file__), 'cases': {}}
def record(name, ok, **info): res['cases'][name] = {'passed': bool(ok), **info}; print(name, 'PASS' if ok else 'FAIL', json.dumps(info, default=str)[:260], flush=True)
N = 7; rng = np.random.default_rng(5); P = rng.normal(size=60); high = rng.normal(size=800); r = rng.normal(size=N)*1e-6; S = np.abs(rng.normal(size=N)); e = np.abs(rng.normal(size=N))*1e-20
conf = json.dumps({'workers': 8, 'cache_threads': 4, 'block_size': 4096, 'mode_block': 64}, sort_keys=True)
with tempfile.TemporaryDirectory(dir=str(out_json.parent)) as td:
    td = Path(td); cand_path = td/'cand.json'; cand_path.write_text('{}')
    def make(name, **over):
        arrays = dict(P=P, high=high, residual=r, S_R=S, e=e, mesh_fingerprint=np.array('fp-train'), configuration_json=np.array(conf)); arrays.update({k: v for k, v in over.items() if v is not None})
        for k, v in over.items():
            if v is None: arrays.pop(k)
        p = td/(name+'.npz'); np.savez_compressed(p, **arrays); return p
    def cand(p): return {'snapshot_arrays_path': str(p), 'snapshot_arrays_sha256': digest(p)}
    good = make('good'); arrays, fail, srcrec, supplied = bind_snapshot(cand(good), cand_path, N, 'fp-train', P, high)
    record('good_snapshot_bound_and_provenance_from_artifact', arrays is not None and fail is None and supplied is True and srcrec['mesh_fingerprint'] == 'fp-train' and srcrec['configuration'] == json.loads(conf) and np.array_equal(arrays[0], r) and 'D6' in srcrec['provenance'], reason=fail)
    arrays, fail, srcrec, supplied = bind_snapshot({}, cand_path, N, 'fp-train', P, high)
    record('no_snapshot_supplied_is_not_a_failure', arrays is None and fail is None and supplied is False)
    arrays, fail, srcrec, supplied = bind_snapshot({'snapshot_arrays_path': str(td/'missing.npz'), 'snapshot_arrays_sha256': 'x'}, cand_path, N, 'fp-train', P, high)
    record('supplied_missing_snapshot_is_a_failure', arrays is None and fail is not None and 'missing' in fail and supplied is True, reason=fail)
    arrays, fail, _, _ = bind_snapshot(dict(cand(good), snapshot_arrays_sha256='0'*64), cand_path, N, 'fp-train', P, high)
    record('sha_mismatch_refused', arrays is None and fail is not None and 'mismatch' in fail, reason=fail)
    p2 = make('n1', residual=r.reshape(N, 1)); arrays, fail, _, _ = bind_snapshot(cand(p2), cand_path, N, 'fp-train', P, high)
    record('shape_N_1_refused', arrays is None and fail is not None and 'not (%d,)' % N in fail, reason=fail)
    r_bad = r.copy(); r_bad[2] = float('nan'); p3 = make('nan', residual=r_bad); arrays, fail, _, _ = bind_snapshot(cand(p3), cand_path, N, 'fp-train', P, high)
    record('nonfinite_residual_refused', arrays is None and fail is not None and 'not finite' in fail, reason=fail)
    P2 = P.copy(); P2[3] = np.nextafter(P2[3], 1.); p4 = make('pdiff', P=P2); arrays, fail, _, _ = bind_snapshot(cand(p4), cand_path, N, 'fp-train', P, high)
    record('one_ulp_P_difference_refused_bitwise', arrays is None and fail is not None and 'differ from the candidate' in fail, reason=fail)
    p5 = make('nometa', mesh_fingerprint=None, configuration_json=None); arrays, fail, _, _ = bind_snapshot(cand(p5), cand_path, N, 'fp-train', P, high)
    record('missing_provenance_metadata_refused', arrays is None and fail is not None and 'lacks' in fail, reason=fail)
    arrays, fail, _, _ = bind_snapshot(cand(good), cand_path, N, 'fp-other', P, high)
    record('mesh_fingerprint_mismatch_refused', arrays is None and fail is not None and 'fingerprint' in fail, reason=fail)
    p6 = make('conf', configuration_json=np.array(json.dumps({'workers': '8'}))); arrays, fail, _, _ = bind_snapshot(cand(p6), cand_path, N, 'fp-train', P, high)
    record('untyped_configuration_refused', arrays is None and fail is not None and 'configuration' in fail, reason=fail)
    arrays, fail, _, _ = bind_snapshot(cand(good), cand_path, N+1, 'fp-train', P, high)
    record('wrong_mesh_size_refused', arrays is None and fail is not None and 'shape' in fail, reason=fail)
# bound_ratio (C6 ruling)
err, den, ratio = bound_ratio(0., 0., Decimal(0)); record('zero_bound_zero_error_ratio_0', (err, den, ratio) == (0., 0., 0.) and len(EXACT) == 1 and not INVALID, ratio=ratio)
err, den, ratio = bound_ratio(0., 0., Decimal('1e-30')); record('zero_bound_nonzero_error_invalid_inf', den == 0. and ratio == float('inf') and len(INVALID) == 1 and 'nonzero error' in INVALID[0]['note'], ratio=ratio, note=INVALID[0].get('note') if INVALID else None)
err, den, ratio = bound_ratio(float('nan'), 1., Decimal(1)); record('nonfinite_value_invalid_inf', ratio == float('inf') and len(INVALID) == 2)
err, den, ratio = bound_ratio(1., -1., Decimal(1)); record('negative_S_R_invalid_inf', ratio == float('inf') and len(INVALID) == 3)
err, den, ratio = bound_ratio(1.0000000000000002, 1., Decimal(1)); record('ordinary_ratio_finite_positive', math.isfinite(ratio) and ratio > 0 and abs(den-(2048*2.**-64+2.**-53*1.0000000000000002)) < 1e-30, ratio=ratio)
res['passed'] = all(c['passed'] for c in res['cases'].values()); out_json.write_text(json.dumps(res, indent=1, default=str)+'\n'); print('ALL PASSED' if res['passed'] else 'SOME FAILED')
