"""Embedded accepted278 on the production training mesh: residual vs frozen V3 provider, J_mesh, raw Jacobian chain rule, timings."""
import json, sys, time, gc
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import basis860 as B, chart860 as C
from model860 import Model860, feasible_matrix
from absolute_common import read, ROOT, A_REF, array_hash
from absolute_fields import prepare_candidate
from absolute_model import FrozenLogMesh
from stage13_model_v3 import CachedAbsoluteProblem as V3
out = {'checks': [], 'timings': {}}
def check(name, value, tol=None, **extra):
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
state = read(ROOT/'campaign/global181_v3/state.json'); cand = read(state['parent_candidate_path'])
epoch = read(state['epoch_path']); mesh = FrozenLogMesh.load(epoch['meshes']['training']['path'])
prep = prepare_candidate(cand, 'center_chart'); pold = prep['p']; eold = prep['extra']
c, g = B.embed_old(prep['coefficients'], eold, prep['modes']); P = np.r_[pold[0], c[1:]]
workers = int(sys.argv[2]) if len(sys.argv) > 2 else 8
# old production provider, fresh on this host
t0 = time.perf_counter(); old = V3(cand, mesh, A_REF, workers=4, block_size=1024); r_old = old.fun(pold, eold); out['timings']['old_v3_fun_cold'] = time.perf_counter()-t0
t0 = time.perf_counter(); J_old = old.jacobian(pold, eold); out['timings']['old_v3_jacobian'] = time.perf_counter()-t0
with np.load(state['arrays_path'], allow_pickle=False) as a: r_saved = a['residual'].copy()
old.clear_cache(); del old; gc.collect()
# new provider
model = Model860(mesh, A_REF, block_size=4096, mode_block=64, workers=workers)
t0 = time.perf_counter(); r_new = model.fun(P, g); out['timings']['new_fun_cold'] = time.perf_counter()-t0
out['timings']['new_cache_build'] = model.cache_build_seconds; out['timings']['new_origin_series_value'] = model.origin_series_seconds
t0 = time.perf_counter(); J_new = model.jacobian(P, g); out['timings']['new_jacobian'] = time.perf_counter()-t0
out['timings']['new_origin_series_total'] = model.origin_series_seconds; out['cache_record'] = model.cache_record()
t0 = time.perf_counter(); r_again = model.fun(P, g); out['timings']['new_fun_cached_hit'] = time.perf_counter()-t0
check('new_fun_repeat_bitwise', np.array_equal(r_new, r_again))
d = r_new-r_old; n = np.linalg.norm(r_old)
check('residual_vs_old_v3_norm_rel', float(np.linalg.norm(d)/n), 1e-12, diff_norm=float(np.linalg.norm(d)), n_differ=int(np.count_nonzero(d)), max_abs=float(np.max(abs(d))), threshold_64eps=float(64*np.finfo(float).eps*n))
check('residual_vs_mac_saved_norm_rel', float(np.linalg.norm(r_new-r_saved)/n), 1e-9)
J_mesh_new = float(r_new@r_new/2); J_mesh_old = float(r_old@r_old/2)
check('J_mesh_rel_vs_old', abs(J_mesh_new-J_mesh_old)/J_mesh_old, 1e-12, J_mesh_new=J_mesh_new, J_mesh_old=J_mesh_old, state_objective=state['objective'])
# chain rule: J_old (N x 186) = J_new (N x 860) @ E (860 x 186)
E = np.zeros((860, 186)); E[0, 0] = 1.
for jold, (m, s) in enumerate(B.OLD_CORE_ORDER):
    if jold == 0: continue
    for kind, idx, f in B.old_core_to_internal(m, s): E[idx if kind == 'core' else 60+idx, jold] += f
for k, mode in enumerate(prep['modes']): E[60+B.old_mode_to_internal(mode), 24+k] = 1.
t0 = time.perf_counter(); JE = J_new@E; out['timings']['chain_product'] = time.perf_counter()-t0
colnorm = np.linalg.norm(J_old, axis=0); err = np.linalg.norm(JE-J_old, axis=0)/colnorm
check('jacobian_chain_rule_max_col_rel', float(np.max(err)), 1e-10, worst_col=int(np.argmax(err)), cl_col_rel=float(err[0]), median=float(np.median(err)))
# feasible matrix and its scales, singular spectrum, conditioning versus monomial coordinates (diagnostic)
chart = C.Chart860(P)
t0 = time.perf_counter(); A, scales = feasible_matrix(J_new, chart); out['timings']['feasible_matrix'] = time.perf_counter()-t0
check('feasible_columns_855', A.shape[1] == 855)
t0 = time.perf_counter(); s = np.linalg.svd(A, compute_uv=False); out['timings']['svd_values_only'] = time.perf_counter()-t0
out['feasible_singular_values'] = {'max': float(s[0]), 'min': float(s[-1]), 'count': len(s), 'log10_quantiles': np.log10(np.quantile(s, [0, .1, .5, .9, 1])).tolist()}
gradient = A.T@r_new; out['scaled_gradient_norm'] = float(np.linalg.norm(gradient)); out['projected_residual_fraction_estimate'] = None
# monomial-coordinate conditioning of the raw extra block (diagnostic only): J_a = J_internal T^{-1} restricted to extras
T = B.conversion_matrix(); Tinv = np.linalg.solve(T, np.eye(860))
Ja = J_new@Tinv; sa = np.linalg.svd(Ja[:, :], compute_uv=False); si = np.linalg.svd(J_new, compute_uv=False)
out['raw_jacobian_singular_values'] = {'internal': {'max': float(si[0]), 'min': float(si[-1]), 'cond': float(si[0]/si[-1])}, 'monomial_canonical': {'max': float(sa[0]), 'min': float(sa[-1]), 'cond': float(sa[0]/sa[-1])}}
out['embedded'] = {'P_sha256': array_hash(P), 'g_sha256': array_hash(g), 'c_sha256': array_hash(np.r_[c]), 'nonzero_extra': int(np.count_nonzero(g)), 'cl': float(P[0])}
np.savez_compressed(Path(sys.argv[1]).with_suffix('.npz'), r_new=r_new, r_old=r_old, P=P, g=g, scales=scales, singular_values=s)
out['passed'] = all(r['passed'] for r in out['checks'])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
