"""G2 test T3 (+T5), SPEC v9: embedded seed on the production meshes; residual vs fresh 181D V3 production with the v9 excusal procedure
(failing nodes listed; excused only where the >= 85-digit evaluator shows the 860 value closer to the exact value and within 1e-12 a_ref;
T3.1 recomputed with the high-precision values substituted); Jacobian chain rule; independent J_abs with tightened targets; refined sampled
maxima on the frozen 32 regions with the v9 excusal (condition (ii) at 1e-11 in every band, band_max from the t26 record); exact dilation;
the repaired evaluator's replay reference file and the fresh-process strict replay.  Usage: g2_t3.py <out.json> <manifest.json> [workers]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, sys, time, gc, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import basis860 as B, hp860 as H
from model860 import Model860
from closure860 import loaded_closure
from fields860 import residual as new_residual, fields as new_fields, exact_dilation_fields
from integrate860 import independent_integral, Integrator860
from absolute_common import read, ROOT, BASE, A_REF, digest, array_hash
from absolute_fields import prepare_candidate
from absolute_fields_v2 import residual as old_residual, fields as old_fields
from absolute_model import FrozenLogMesh
from stage13_model_v3 import CachedAbsoluteProblem as V3
from stage13_integration_v2 import independent_integral as old_independent_integral
from threadpoolctl import threadpool_limits
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'tools'))
from runtime import Runtime
rt = Runtime(str(Path(__file__).resolve().parents[2]))      # path translation only (no audit hook install here)
out_path = Path(sys.argv[1]); manifest_path = Path(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 3 else 8
out = {'schema': 'g2_t3_v2_spec_v9', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'timings': {}, 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))     # SPEC v8 item 3
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
state = rt.read(ROOT/'campaign/global181_v3/state.json'); epoch = rt.read(state['epoch_path']); cand = read(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json')
mesh = FrozenLogMesh.load(epoch['meshes']['training']['path']); refined = FrozenLogMesh.load(epoch['meshes']['refined']['path'])
with np.load(epoch['meshes']['training']['path'], allow_pickle=False) as a: tblocks = a['block_ids'].copy()
prep = prepare_candidate(cand, 'center_chart'); pold = prep['p']; eold = prep['extra']; cl = float(pold[0])
low, high = B.embed_old(prep['coefficients'], eold, prep['modes']); P = np.r_[cl, low[1:]]
seed_json = json.loads(Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.json')).read_text())
check('T3.0_seed_json_matches_embedding', seed_json['P_raw_chart_hex'] == [float(v).hex() for v in P] and seed_json['high_hex'] == [float(v).hex() for v in high])
# ---- old V3 production residual and Jacobian (fresh, this host)
t0 = time.perf_counter(); old = V3(cand, mesh, A_REF, workers=4, block_size=1024); r_old = old.fun(pold, eold); out['timings']['old_v3_fun_cold_s'] = time.perf_counter()-t0
t0 = time.perf_counter(); J_old = old.jacobian(pold, eold); out['timings']['old_v3_jacobian_s'] = time.perf_counter()-t0
old.clear_cache(); del old; gc.collect()
# ---- new production provider
model = Model860(mesh, A_REF, block_size=4096, mode_block=64, workers=workers, threads=min(workers, 4))
t0 = time.perf_counter(); r_new = model.fun(P, high); out['timings']['new_fun_cold_s'] = time.perf_counter()-t0
out['timings']['new_cache_build_s'] = model.cache_build_seconds; out['timings']['new_origin_series_value_s'] = model.origin_series_seconds
t0 = time.perf_counter(); J_new = model.jacobian(P, high); out['timings']['new_jacobian_s'] = time.perf_counter()-t0
out['timings']['new_origin_series_total_s'] = model.origin_series_seconds; out['cache_record'] = model.cache_record()
r2 = model.fun(P, high); check('T3.4_repeat_same_process_bitwise', np.array_equal(r_new, r2))
root = model.root; n_old = np.linalg.norm(r_old)
prep860 = B.prepare(cl, low[1:], high); x_tr, y_tr = mesh.coordinates()
def excusal(name, rn, ro, rootv, xv, yv, cap_nodes=400):
    """SPEC v9 T3.1/T3.2 rule: list the failing nodes (pointwise |dR_f|/a_ref > 1e-12, or the largest differences if the norm test fails diffusely);
    at each, the 85-digit R_f; excused where the 860 value is closer to it than the 181D value and within 1e-12 a_ref; recompute the norm with the
    high-precision values substituted on the 181D side at the excused nodes."""
    d = abs(rn-ro)/rootv/A_REF; rel = float(np.linalg.norm(rn-ro)/np.linalg.norm(ro)); pmax = float(d.max())
    rec = {'rel_norm': rel, 'max_dRf_over_aref': pmax, 'n_differ': int(np.count_nonzero(rn-ro)), 'excusal_applied': False}
    if rel <= 1e-9 and pmax <= 1e-12: return rel, pmax, rec
    idx = np.flatnonzero(d > 1e-12)
    if len(idx) == 0: idx = np.argsort(-d)[:cap_nodes]
    rec['failing_nodes_count'] = int(len(idx)); rec['failing_nodes_capped'] = bool(len(idx) > cap_nodes); idx = idx[np.argsort(-d[idx])][:cap_nodes]
    nodes = []; ro_sub = ro.copy(); excused_all = len(idx) <= cap_nodes
    for i in idx:
        ref = H.point_reference(prep860, float(xv[i]), float(yv[i]), 85, columns=False)['Rf']; e860 = abs(float(rn[i])/rootv[i]-ref); e181 = abs(float(ro[i])/rootv[i]-ref)
        ok = bool(e860 < e181 and e860 <= 1e-12*A_REF); excused_all = excused_all and ok
        if ok: ro_sub[i] = rootv[i]*ref
        nodes.append({'node': int(i), 'xy': [float(xv[i]), float(yv[i])], 'r': float(math.hypot(xv[i], yv[i])), 'Rf_860': float(rn[i]/rootv[i]), 'Rf_181D': float(ro[i]/rootv[i]), 'Rf_hp85': ref, 'err_860_over_aref': e860/A_REF, 'err_181D_over_aref': e181/A_REF, 'excused': ok})
    rec.update(excusal_applied=True, nodes=nodes, all_listed_nodes_excused=excused_all, rel_norm_after_substitution=float(np.linalg.norm(rn-ro_sub)/np.linalg.norm(ro_sub)), max_dRf_over_aref_after_substitution=float(np.max(abs(rn-ro_sub)/rootv)/A_REF))
    if excused_all: rel, pmax = rec['rel_norm_after_substitution'], rec['max_dRf_over_aref_after_substitution']
    out[name+'_excusal'] = rec; return rel, pmax, rec
rel31, pmax31, rec31 = excusal('T3.1', r_new, r_old, root, x_tr, y_tr)
check('T3.1_training_residual_rel_norm', rel31, 1e-9, diff_norm=float(np.linalg.norm(r_new-r_old)), old_norm=float(n_old), n_differ=int(np.count_nonzero(r_new-r_old)), raw_rel_norm=rec31['rel_norm'], excusal_applied=rec31['excusal_applied'], stated_deviation=bool(rec31['excusal_applied']))
check('T3.1_training_max_dRf_over_aref', pmax31, 1e-12, raw_value=rec31['max_dRf_over_aref'], excusal_applied=rec31['excusal_applied'])
for b, name in enumerate(('origin', 'middle', 'infinity')):
    sel = tblocks == b; out.setdefault('block_residual', {})[name] = {'rel_norm': float(np.linalg.norm(r_new[sel]-r_old[sel])/max(np.linalg.norm(r_old[sel]), 1e-300)), 'max_dRf_over_aref': float(np.max(abs(r_new[sel]-r_old[sel])/root[sel])/A_REF), 'J_block_new': float(r_new[sel]@r_new[sel]/2), 'J_block_old': float(r_old[sel]@r_old[sel]/2)}
check('T2.5_infinity_block_residual_rel_norm', out['block_residual']['infinity']['rel_norm'], 1e-9)
Jm_new = float(r_new@r_new/2); Jm_old = float(r_old@r_old/2); out['J_mesh'] = {'new': Jm_new, 'old_fresh': Jm_old, 'old_saved_state': state['objective']}
# ---- Jacobian chain rule (T4.1): J_old = J_new @ E
E = np.zeros((860, 186)); E[0, 0] = 1.
for jold, (m, s) in enumerate(B.OLD_CORE_ORDER):
    if jold == 0: continue
    for kind, idx, f in B.old_core_to_internal(m, s):
        if kind == 'low' and idx == 0: continue        # a_000 is eliminated on both sides; its chain is implicit (identical center condition)
        E[idx if kind == 'low' else 60+idx, jold] += f
for k, mode in enumerate(prep['modes']): E[60+B.old_mode_to_internal(mode), 24+k] = 1.
JE = J_new@E; colnorm = np.linalg.norm(J_old, axis=0); floor = 1e-13*colnorm.max(); err = np.linalg.norm(JE-J_old, axis=0)
rel = err/colnorm; passes_rel = rel <= 1e-9; passes_floor = err <= 1e-9*colnorm+floor
check('T4.1_jacobian_chain_rule_all_columns', bool(np.all(passes_floor)), worst_rel=float(rel.max()), worst_col=int(np.argmax(rel)), median_rel=float(np.median(rel)), cl_col_rel=float(rel[0]), floor_only_columns=[int(i) for i in np.flatnonzero(passes_floor & ~passes_rel)])
sel = tblocks == 2; err_inf = np.linalg.norm(JE[sel]-J_old[sel], axis=0); cn_inf = np.linalg.norm(J_old[sel], axis=0)
check('T2.5_infinity_block_jacobian_columns', bool(np.all(err_inf <= 1e-9*cn_inf+1e-13*cn_inf.max())), worst_rel=float(np.max(err_inf/np.maximum(cn_inf, 1e-300))))
np.savez_compressed(out_path.with_name('g2_t3_arrays.npz'), r_new=r_new, r_old=r_old, P=P, high=high)
del J_old, JE; gc.collect()
# ---- training-mesh cross-configuration agreement (SPEC v9.3 clause (d)): stateless/integrator entrypoint vs the production provider, 64 eps
integ = Integrator860(epoch, workers=workers)
t0 = time.perf_counter(); r_state = integ.stateless(P, high, mesh); out['timings']['stateless_training_s'] = time.perf_counter()-t0
tol64 = 64*np.finfo(float).eps*max(np.linalg.norm(r_new), np.linalg.norm(r_state), 1e-300)
check('T3.9_training_residual_stateless_vs_production_64eps', float(np.linalg.norm(r_new-r_state)), float(tol64), bitwise=bool(np.array_equal(r_new, r_state)), n_differ=int(np.count_nonzero(r_new-r_state)), max_abs=float(np.max(abs(r_new-r_state))))
# ---- refined mesh residual (stateless both sides) 
t0 = time.perf_counter(); rf_new = integ.stateless(P, high, refined); out['timings']['new_stateless_refined_s'] = time.perf_counter()-t0
xr, yr = refined.coordinates(); rootr = np.sqrt(2*refined.weights/(np.pi*A_REF**2))
with threadpool_limits(limits=workers, user_api='blas'): rf_old = rootr*old_residual(prep, xr, yr)
rel32, pmax32, rec32 = excusal('T3.2', rf_new, rf_old, rootr, xr, yr)
check('T3.2_refined_residual_rel_norm', rel32, 1e-9, raw_rel_norm=rec32['rel_norm'], excusal_applied=rec32['excusal_applied'], stated_deviation=bool(rec32['excusal_applied']))
check('T3.2_refined_max_dRf_over_aref', pmax32, 1e-12, raw_value=rec32['max_dRf_over_aref'], excusal_applied=rec32['excusal_applied'])
# ---- independent whole-axis J_abs, tightened targets (T3.5)
t0 = time.perf_counter(); ii_new = independent_integral(P, high, workers=workers, target_abs=1e-18, initial_upper_log_radius=44.); out['timings']['independent_integral_new_s'] = time.perf_counter()-t0
t0 = time.perf_counter(); ii_old = old_independent_integral(cand, pold, eold, workers=workers, target_abs=1e-18, initial_upper_log_radius=44.); out['timings']['independent_integral_old_s'] = time.perf_counter()-t0
cap = 1e-9*ii_old['J_abs']; esum = ii_new['error_abs']+ii_old['error_abs']
check('T3.5_J_abs_difference', abs(ii_new['J_abs']-ii_old['J_abs']), cap+esum, J_new=ii_new['J_abs'], J_old=ii_old['J_abs'], e_new=ii_new['error_abs'], e_old=ii_old['error_abs'], conclusive=bool(esum <= cap), reference_handoff=4.2683726070948805e-09)
check('T3.5_errors_conclusive', esum, cap); check('T3.5_new_accuracy_passed', ii_new['accuracy_passed']); check('T3.5_new_overlap_passed', ii_new['origin_independent_overlap']['passed'], **{k: ii_new['origin_independent_overlap'][k] for k in ('order48_error_abs', 'order56_error_abs', 'tolerance_abs')})
out['integrator_largest_log_radius_seed_integral'] = {'s_max': ii_new['interval_expansions'][-1]['s_max'], 'r_max': math.exp(ii_new['interval_expansions'][-1]['s_max']), 'exceeds_e44': bool(ii_new['interval_expansions'][-1]['s_max'] > 44.)}
out['independent_integral_new'] = {k: ii_new[k] for k in ('J_abs', 'error_abs', 'origin_tail_error_abs', 'infinity_tail_error_abs', 'radial_quadrature_error_abs', 'angular_quadrature_error_abs', 'accuracy_passed', 'seconds')}
out['independent_integral_old'] = {k: ii_old[k] for k in ('J_abs', 'error_abs', 'origin_tail_error_abs', 'infinity_tail_error_abs', 'radial_quadrature_error_abs', 'angular_quadrature_error_abs', 'accuracy_passed', 'seconds')}
# ---- T3.6 refined sampled maxima on the frozen 32 regions and the two dense grids (same points both sides)
design = read(ROOT/'inputs/absolute_assessment_design.json'); grids = read(BASE/'inputs/assessment_grids_stage12.json')
with np.load(ROOT/'inputs/absolute_assessment_coordinates.npz', allow_pickle=False) as arrays:
    for name in design['regions']: grids[name] = {'x': arrays[name+'_x'].tolist(), 'y': arrays[name+'_y'].tolist()}
maxima = {}; worst_rel = 0.; region_diag = {}
t26_path = out_path.with_name('t26.json'); bandmax26 = {}
if t26_path.exists():
    for row in json.loads(t26_path.read_text())['finite_points']: bandmax26[row['band']] = max(bandmax26.get(row['band'], 0.), abs(row['Rf_hp85']))
out['T3.6_t26_band_maxima_used'] = {'path': str(t26_path), 'present': t26_path.exists(), 'band_max': bandmax26}
def band_of(rv): return 'origin' if rv < .02 else 'b1' if rv < .1 else 'b2' if rv < 1 else 'b3' if rv < 10 else 'b4' if rv < 1e3 else 'b5'
with threadpool_limits(limits=workers, user_api='blas'):
    for name, row in grids.items():
        x = np.asarray(row['x'], float); y = np.asarray(row['y'], float); r = np.hypot(x, y)
        ro = old_residual(prep, x, y); rn = new_residual(B.prepare(cl, low[1:], high), x, y)
        Ef_o = np.max(abs(ro))/A_REF; Ef_n = np.max(abs(rn))/A_REF
        yr_ = np.divide(y, r, out=np.zeros_like(y), where=r > 0); Er_o = np.max(abs(yr_*ro))/A_REF; Er_n = np.max(abs(yr_*rn))/A_REF
        rel = max(abs(Ef_o-Ef_n)/Ef_o if Ef_o else 0., abs(Er_o-Er_n)/Er_o if Er_o else 0.)
        maxima[name] = {'E_f_old': float(Ef_o), 'E_f_new': float(Ef_n), 'E_rho_old': float(Er_o), 'E_rho_new': float(Er_n), 'points': int(len(x)), 'rel_max_difference': float(rel), 'r_min': float(r.min()), 'r_max': float(r.max()),
                        'max_abs_dRf_over_aref': float(np.max(abs(ro-rn))/A_REF)}
        worst_rel = max(worst_rel, rel)
        if rel > 1e-10:   # SPEC v8 item 2: per-region diagnosis with the excusal rule
            pts = {'argmax_Ef_181D': int(np.argmax(abs(ro))), 'argmax_Ef_860': int(np.argmax(abs(rn))), 'argmax_Erho_181D': int(np.argmax(abs(yr_*ro))), 'argmax_Erho_860': int(np.argmax(abs(yr_*rn))), 'worst_dRf': int(np.argmax(abs(ro-rn)))}; detail = {}
            for lab, i in pts.items():
                ref = H.point_reference(prep860, float(x[i]), float(y[i]), 85, columns=False)['Rf']
                detail[lab] = {'xy': [float(x[i]), float(y[i])], 'r': float(r[i]), 'band': band_of(float(r[i])), 'Rf_181D': float(ro[i]), 'Rf_860': float(rn[i]), 'Rf_hp85': ref, 'err_860': abs(float(rn[i])-ref), 'err_181D': abs(float(ro[i])-ref)}
            for d_ in detail.values():      # SPEC v9 condition (ii): 1e-11 band_max, band_max = max(T2.6c reference band max, largest reference |R_f| among the diagnosed points of that band)
                bm = max(bandmax26.get(d_['band'], 0.), max(abs(e['Rf_hp85']) for e in detail.values() if e['band'] == d_['band']), 1e-30); d_['band_max_used'] = bm; d_['ratio_1e-11_rule'] = d_['err_860']/bm; d_['meets_rule'] = bool(d_['err_860'] <= 1e-11*bm)
            excused = bool(maxima[name]['max_abs_dRf_over_aref'] <= 1e-12 and all(d_['meets_rule'] for d_ in detail.values()))
            region_diag[name] = {'r_range': [float(r.min()), float(r.max())], 'points': detail, 'max_abs_dRf_over_aref': maxima[name]['max_abs_dRf_over_aref'], 'excused_by_SPEC_v9_rule': excused,
                                 'reported_860_error_le_181D_error_at_all_points': bool(all(d_['err_860'] <= d_['err_181D'] for d_ in detail.values()))}
out['sampled_maxima'] = maxima; out['T3.6_region_diagnosis'] = region_diag; EfO = max(v['E_f_old'] for k, v in maxima.items() if k != 'dense_769x199'); EfN = max(v['E_f_new'] for k, v in maxima.items() if k != 'dense_769x199')
check('T3.6_frozen32_E_f_max_rel', abs(EfO-EfN)/EfO, 1e-10, E_f_old=EfO, E_f_new=EfN, handoff=1.23849639744e-4)
ErO = max(v['E_rho_old'] for k, v in maxima.items() if k != 'dense_769x199'); ErN = max(v['E_rho_new'] for k, v in maxima.items() if k != 'dense_769x199')
check('T3.6_frozen32_E_rho_max_rel', abs(ErO-ErN)/ErO, 1e-10, E_rho_old=ErO, E_rho_new=ErN, handoff=7.16582921424e-5)
check('T3.6_all_regions_worst_rel_diagnostic_with_excusal', bool(all(v['excused_by_SPEC_v9_rule'] for v in region_diag.values())), worst_rel=worst_rel, diagnosed_regions=sorted(region_diag), excused_regions=sorted(k for k, v in region_diag.items() if v['excused_by_SPEC_v9_rule']), note='SPEC criterion = overall frozen-32 maxima (T3.6_frozen32_*); per-region differences above 1e-10 are diagnosed and excused only by the SPEC v9 rule ((i) pointwise 1e-12 a_ref, (ii) 1e-11 band_max at every diagnosed point); excused regions are stated deviations')
# ---- T3.7 exact dilation on the frozen mesh (new evaluator): J(L) vs J(1)
seedp = B.prepare(cl, low[1:], high); x, y = mesh.coordinates(); dil = {}
with threadpool_limits(limits=workers, user_api='blas'):
    for L in (1-1e-3, 1+1e-3, 2.):
        ff = exact_dilation_fields(seedp, x, y, L); wx = cl*x-ff['psiy']; wy = cl*y+ff['psix']; rfd = wx*ff['fx']+wy*ff['fy']+ff['q']*ff['f']
        rd = root*rfd; dil[str(L)] = {'J_mesh_dilated': float(rd@rd/2), 'relative_change_vs_L1': float((rd@rd/2-Jm_new)/Jm_new)}
out['exact_dilation_frozen_mesh'] = dil
# ---- T5: the repaired evaluator's replay reference file (SPEC v9, named in the manifest); P/high/low bitwise equal to the sealed coefficient file seed_860.npz (g2_v1 record; gated); residual difference reported overall and per block
seed_npz = Path(B.REPLAY_REFERENCE_FILE); sealed_npz = Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.npz'))
if seed_npz.exists(): raise SystemExit('replay reference exists; refusing to overwrite')
np.savez(seed_npz, P=P, high=high, low=low, residual=r_new)
out['replay_reference_file'] = str(seed_npz); out['replay_reference_sha256'] = digest(seed_npz); out['seed_residual_sha256'] = array_hash(r_new)
with np.load(sealed_npz, allow_pickle=False) as s0:
    same = {k: bool(np.array_equal(s0[k], v)) for k, v in (('P', P), ('high', high), ('low', low))}; r_v1 = s0['residual'].copy()
check('T5.0_replay_file_coefficient_arrays_bitwise_equal_sealed_g2_v1', all(same.values()), **same, sealed_sha256=digest(sealed_npz))
blocks_diff = {}
for b, name in enumerate(('origin', 'middle', 'infinity')):
    sel = tblocks == b; blocks_diff[name] = {'difference_norm': float(np.linalg.norm(r_new[sel]-r_v1[sel])), 'relative': float(np.linalg.norm(r_new[sel]-r_v1[sel])/max(np.linalg.norm(r_v1[sel]), 1e-300)), 'max_dRf_over_aref': float(np.max(abs(r_new[sel]-r_v1[sel])/root[sel])/A_REF)}
out['T5.0_residual_difference_vs_g2_v1'] = {'overall': {'difference_norm': float(np.linalg.norm(r_new-r_v1)), 'relative': float(np.linalg.norm(r_new-r_v1)/np.linalg.norm(r_v1)), 'max_dRf_over_aref': float(np.max(abs(r_new-r_v1)/root)/A_REF)}, 'per_block': blocks_diff,
                                            'note': 'SPEC v9: the production residual is regenerated under the repaired evaluator (longdouble assembly, centered q below r_s = 1, stable linear transport above, exact exponent differences); reported, not gated'}
replay_target = seed_npz
code = """
import sys, json; sys.path.insert(0, '%s'); import numpy as np
import basis860 as B; from model860 import Model860; from absolute_common import A_REF; from absolute_model import FrozenLogMesh
mesh = FrozenLogMesh.load('%s'); d = np.load('%s'); m = Model860(mesh, A_REF, block_size=4096, mode_block=64, workers=%d, threads=4); r = m.fun(d['P'], d['high'])
diff = float(np.linalg.norm(r-d['residual'])); tol = float(64*np.finfo(float).eps*max(np.linalg.norm(r), np.linalg.norm(d['residual']), 1e-300))
print(json.dumps({'diff': diff, 'tol': tol, 'bitwise': bool(np.array_equal(r, d['residual'])), 'passed': diff <= tol}))
""" % (str(Path(__file__).resolve().parents[1]), epoch['meshes']['training']['path'], str(replay_target), workers)
import subprocess; t0 = time.perf_counter(); res = subprocess.run([sys.executable, '-B', '-c', code], capture_output=True, text=True, env=dict(os.environ)); out['timings']['replay_fresh_process_s'] = time.perf_counter()-t0
try: rep = json.loads(res.stdout.strip().splitlines()[-1])
except Exception: rep = {'passed': False, 'stdout': res.stdout[-2000:], 'stderr': res.stderr[-2000:]}
rep['child_returncode'] = res.returncode
check('T5.2_fresh_process_strict_replay_64eps', bool(rep.get('passed', False)) and res.returncode == 0, replay=rep)
out['import_closure'] = loaded_closure()
out['passed'] = all(r['passed'] for r in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
