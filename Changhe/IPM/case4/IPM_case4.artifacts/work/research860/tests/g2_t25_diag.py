"""Non-blocking diagnostic (lead 09:11Z item 2; G3 records gate the infinity-block Jacobian like T4.1 with the floor-only columns listed). On the training infinity-block
nodes only: for every old (186) column, err = ||(J_new E - J_old)[inf]||, with both column norms ||(J_new E)[inf]|| and ||J_old[inf]||; list every column with err > 1e-9 ||J_old[inf]||
and, for the three worst, compare the 860 (J_new E) and 181D (J_old) values at the worst node with the 85-digit point_reference column (reference old column = reference raw
columns @ E[:, j]). Also the T4.1-style gate on the infinity block with the floor-only columns listed. Usage: g2_t25_diag.py <out.json> <manifest> [workers]"""
import json, math, sys, time, gc
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import basis860 as B, hp860 as H
from model860 import Model860
from absolute_common import read, ROOT, A_REF, digest, array_hash
from absolute_fields import prepare_candidate
from absolute_model import FrozenLogMesh
from stage13_model_v3 import CachedAbsoluteProblem as V3
from closure860 import loaded_closure
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'tools')); from runtime import Runtime
rt = Runtime(str(Path(__file__).resolve().parents[2]))
out_path = Path(sys.argv[1]); manifest_path = Path(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 3 else 4
out = {'schema': 'g2_t25_diag_v1', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
state = rt.read(ROOT/'campaign/global181_v3/state.json'); epoch = rt.read(state['epoch_path']); cand = read(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json')
mesh = FrozenLogMesh.load(epoch['meshes']['training']['path'])
with np.load(epoch['meshes']['training']['path'], allow_pickle=False) as a: tblocks = a['block_ids'].copy()
prep = prepare_candidate(cand, 'center_chart'); pold = prep['p']; eold = prep['extra']; cl = float(pold[0])
low, high = B.embed_old(prep['coefficients'], eold, prep['modes']); P = np.r_[cl, low[1:]]
t0 = time.perf_counter(); old = V3(cand, mesh, A_REF, workers=4, block_size=1024); r_old = old.fun(pold, eold); J_old = old.jacobian(pold, eold); out['old_seconds'] = time.perf_counter()-t0; old.clear_cache(); del old; gc.collect()
model = Model860(mesh, A_REF, block_size=4096, mode_block=64, workers=workers, threads=min(workers, 4))
t0 = time.perf_counter(); r_new = model.fun(P, high); J_new = model.jacobian(P, high); out['new_seconds'] = time.perf_counter()-t0
E = np.zeros((860, 186)); E[0, 0] = 1.
for jold, (m, s) in enumerate(B.OLD_CORE_ORDER):
    if jold == 0: continue
    for kind, idx, f in B.old_core_to_internal(m, s):
        if kind == 'low' and idx == 0: continue
        E[idx if kind == 'low' else 60+idx, jold] += f
for k, mode in enumerate(prep['modes']): E[60+B.old_mode_to_internal(mode), 24+k] = 1.
sel = np.flatnonzero(tblocks == 2); JE = J_new[sel]@E; JO = J_old[sel]; root = model.root[sel]; x, y = mesh.coordinates(); xs = x[sel]; ys = y[sel]
err = np.linalg.norm(JE-JO, axis=0); cn_new = np.linalg.norm(JE, axis=0); cn_old = np.linalg.norm(JO, axis=0); floor = 1e-13*cn_old.max()
passes_rel = err <= 1e-9*cn_old; passes_floor = err <= 1e-9*cn_old+floor
rows = [{'old_column': int(j), 'err': float(err[j]), 'norm_860_JE_inf': float(cn_new[j]), 'norm_181D_inf': float(cn_old[j]), 'err_over_norm_181D': float(err[j]/max(cn_old[j], 1e-300)), 'err_over_floor': float(err[j]/floor), 'passes_floor_rule': bool(passes_floor[j])} for j in np.flatnonzero(~passes_rel)]
rows.sort(key=lambda r_: -r_['err_over_norm_181D'])
out['infinity_block'] = {'nodes': int(len(sel)), 'floor_abs': float(floor), 'columns_with_err_above_1e-9_norm': rows, 'count': len(rows), 'floor_only_columns': [int(j) for j in np.flatnonzero(passes_floor & ~passes_rel)], 'worst_rel': float(np.max(err/np.maximum(cn_old, 1e-300)))}
check('T2.5_infinity_block_jacobian_columns_T41_rule', bool(np.all(passes_floor)), floor_only_columns=[int(j) for j in np.flatnonzero(passes_floor & ~passes_rel)], worst_rel=out['infinity_block']['worst_rel'], failing_columns=[int(j) for j in np.flatnonzero(~passes_floor)])
# three worst columns: compare at the worst node with the 85-digit reference (center-eliminated raw columns @ E)
prep860 = B.prepare(cl, low[1:], high); detail = []
for r_ in rows[:3]:
    j = r_['old_column']; d = abs(JE[:, j]-JO[:, j]); i = int(np.argmax(d)); ref = H.point_reference(prep860, float(xs[i]), float(ys[i]), 85, columns=True)
    ref_old_col = float(ref['columns']@E[:, j]); ref_cl = float(ref['columns'][0]) if j == 0 else None
    detail.append({'old_column': j, 'worst_node_index_in_block': i, 'xy': [float(xs[i]), float(ys[i])], 'r': float(math.hypot(xs[i], ys[i])), 'value_860_JE': float(JE[i, j]/root[i]), 'value_181D': float(JO[i, j]/root[i]), 'reference_85': ref_old_col,
                   'err_860': abs(float(JE[i, j]/root[i])-ref_old_col), 'err_181D': abs(float(JO[i, j]/root[i])-ref_old_col), 'note': 'values divided by the root weight (unweighted Jacobian entries); reference = 85-digit center-eliminated raw columns combined through E'})
out['three_worst_columns_reference_comparison'] = detail
out['import_closure'] = loaded_closure(); out['passed'] = all(c['passed'] for c in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
