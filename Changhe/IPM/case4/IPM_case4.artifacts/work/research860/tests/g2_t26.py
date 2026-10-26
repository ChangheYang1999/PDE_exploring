"""G2 tests T2.6b and T2.6c (SPEC v9 / v9.2): every raw Jacobian column (cl, 59 low, 800 high) and R_f of the seed for the three provider
shapes (one-point Model860, batch Model860 with all points in one call, stateless provider) against the lane's Decimal reference
(hp860.point_reference, >= 85 digits, no binary64 intermediates), |difference| <= 1e-11 max(band_max, 1e-30) in every band:
T2.6b at r = e^24, e^32, e^44 and at the largest training and refined mesh radii, three angles each (all gated, v9.3), T2.6c one point triple per finite band plus two origin-disk points and
the r = 0.999 / 1.001 straddle of the R_f switch; T2.6d: the production chunking with its remainder chunk (points embedded at the start, the middle and
the remainder chunk of a training-mesh-sized Model860 call) and the integrator validation entrypoint (refined-mesh-sized call through Integrator860.stateless);
T2.6x: one-point shape for the seed coefficients at c_l = 2, 3, 2(1+2^-20), 3(1-2^-20). Floors: 1e-41 where band_max < 1e-30 (listed).
The largest difference between configurations and rho = |diff| / (u S_R), u = 2^-64, are reported.
Usage: g2_t26.py <out.json> <manifest> [workers]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, sys, time
from decimal import Decimal
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import basis860 as B, hp860 as H
from points860 import FAR, FINITE_V92, GATED_FAR
from shapes860 import production_single, production_batch, stateless, point_model, share_prepared, SHARED_SERIES
from model860 import Model860
from integrate860 import Integrator860
from absolute_common import digest, ROOT, A_REF
from absolute_model import FrozenLogMesh
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'tools')); from runtime import Runtime
from closure860 import loaded_closure
out_path = Path(sys.argv[1]); manifest_path = Path(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 3 else 8
out = {'schema': 'g2_t26_v3_spec_v93', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
       'switch_radius_residual_and_columns': B.R_SWITCH, 'unit_roundoff_u': 2.**-64, 'extended_arithmetic': B.extended_arithmetic_statement()}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))     # SPEC v8 item 3
    ok = bool(value <= tol) if tol is not None else bool(value)
    rec = {'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}
    if tol is not None and 'floor' not in extra: rec['floor'] = 'ratio to max(band_max, 1e-30): absolute 1e-41 where band_max < 1e-30'
    out['checks'].append(rec); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
D = Decimal; LD = B.LD; U = 2.**-64; SHAPES = ('single', 'batch', 'stateless')
seed = json.loads(Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.json')).read_text())
P = np.array([float.fromhex(h) for h in seed['P_raw_chart_hex']]); high = np.array([float.fromhex(h) for h in seed['high_hex']]); cl = float(P[0])
prep = share_prepared(B.prepare(cl, P[1:], high), P, high)      # one origin series (order 48) for every shape of the seed

def condition_sum(x, y):
    """S_R: R_f assembled with every field replaced by its absolute condition sum over the generators (same split as the provider)."""
    blk = B.generator_block(cl, [x], [y], False, True); ac = abs(prep['coeff_ld'])
    S = {k: float(abs(blk[k][0])@ac) for k in ('f', 'fx', 'fy', 'psix', 'psiy', 'ratio')}
    Sq = float(abs(blk['qcore'][0])@abs(prep['c_ld'])+abs(blk['ratio'][0, 60:])@abs(np.asarray(high, LD)))
    if math.hypot(x, y) >= B.R_SWITCH:
        return float((abs(cl-1)*B.JCOL_LD*abs(blk['f'][0])+2*cl*abs(blk['frem'][0]))@ac)+S['psiy']*S['fx']+S['psix']*S['fy']+S['ratio']*S['f']
    return (abs(cl*x)+S['psiy'])*S['fx']+(abs(cl*y)+S['psix'])*S['fy']+Sq*S['f']

def hp_ref(args):
    band, x, y = args; ref = H.point_reference(prep, x, y, 85, True)
    return {'band': band, 'x': x, 'y': y, 'Rf': ref['Rf'], 'Rf_decimal': str(ref['Rf_decimal']), 'columns': ref['columns']}

def run_points(points, label):
    import multiprocessing as mp
    t0 = time.time(); xs = np.array([p[1] for p in points]); ys = np.array([p[2] for p in points])
    with mp.get_context('fork').Pool(min(workers, len(points))) as pool: refs = pool.map(hp_ref, points)
    t_ref = time.time()-t0; t0 = time.time()
    rf_b, dr_b = production_batch(P, high, xs, ys, True); rf_s, dr_s = stateless(prep, xs, ys, True); rows = []
    for i, (b, x, y) in enumerate(points):
        rf1, dr1 = production_single(P, high, x, y, True)
        rows.append({'band': b, 'x': x, 'y': y, 'r': math.hypot(x, y), 'Rf_hp85': refs[i]['Rf'], 'Rf_hp85_decimal': refs[i]['Rf_decimal'], 'Rf_single': rf1, 'Rf_batch': float(rf_b[i]), 'Rf_stateless': float(rf_s[i]),
                     'S_R': condition_sum(x, y), 'cols_hp85': refs[i]['columns'], 'cols_single': dr1, 'cols_batch': dr_b[i], 'cols_stateless': dr_s[i]})
        print(label, b, 'r=%.3g' % rows[-1]['r'], 'Rf err single %.2e batch %.2e stateless %.2e' % tuple(abs(rows[-1]['Rf_'+s]-rows[-1]['Rf_hp85']) for s in SHAPES), flush=True)
    out[label+'_seconds'] = {'reference': t_ref, 'providers': time.time()-t0}
    return rows

def band_eval(rows, name):
    res = {}
    for band in sorted({r_['band'] for r_ in rows}):
        sub = [r_ for r_ in rows if r_['band'] == band]; rfmax = max(max(abs(r_['Rf_hp85']) for r_ in sub), 1e-30)
        cref = np.array([r_['cols_hp85'] for r_ in sub]); cmax = np.maximum(np.max(abs(cref), axis=0), 1e-30)
        entry = {'points': len(sub), 'Rf_band_max': rfmax, 'columns_floor_cases': [int(i) for i in np.flatnonzero(cmax <= 1e-30)]}
        for s in SHAPES:
            errs = [abs(r_['Rf_'+s]-r_['Rf_hp85']) for r_ in sub]; i = int(np.argmax(errs))
            entry['Rf_'+s] = {'ratio': errs[i]/rfmax, 'abs': errs[i], 'at_r': sub[i]['r'], 'rho': errs[i]/(U*sub[i]['S_R'])}
            cerr = np.max(abs(np.array([r_['cols_'+s] for r_ in sub])-cref), axis=0); ratio = cerr/cmax
            entry['columns_'+s] = {'worst_ratio': float(ratio.max()), 'worst_index': int(np.argmax(ratio)), 'failing_count': int(np.count_nonzero(ratio > 1e-11))}
        entry['Rf_largest_shape_difference'] = max(abs(r_['Rf_'+a]-r_['Rf_'+b]) for r_ in sub for a in SHAPES for b in SHAPES)
        entry['columns_largest_shape_difference'] = max(float(np.max(abs(r_['cols_'+a]-r_['cols_'+b]))) for r_ in sub for a in SHAPES for b in SHAPES)
        entry['columns_largest_shape_difference_relative_to_band_max'] = max(float(np.max(abs(r_['cols_'+a]-r_['cols_'+b])/cmax)) for r_ in sub for a in SHAPES for b in SHAPES)
        entry['Rf_shapes_bitwise_equal'] = bool(entry['Rf_largest_shape_difference'] == 0)
        res[band] = entry
    out[name] = res; return res

rt = Runtime(str(Path(__file__).resolve().parents[2])); state = rt.read(ROOT/'campaign/global181_v3/state.json'); epoch = rt.read(state['epoch_path'])
mesh_tr = FrozenLogMesh.load(epoch['meshes']['training']['path']); mesh_rf = FrozenLogMesh.load(epoch['meshes']['refined']['path'])
def mesh_rmax(mesh_):
    xm, ym = mesh_.coordinates(); return float(np.max(np.hypot(xm, ym)))
RMAX = {'rmax_training': mesh_rmax(mesh_tr), 'rmax_refined': mesh_rmax(mesh_rf)}; out['largest_mesh_radii'] = RMAX
def _xy(r, th):
    x = r*math.cos(th); y = r*math.sin(th)
    if th == math.pi/2: x = 0.
    if th == 0.: y = 0.
    return x, y
FAR_ALL = FAR+[(name, *_xy(rv, th)) for name, rv in RMAX.items() for th in (0., .3, math.pi/2)]
t_far = run_points(FAR_ALL, 'T2.6b'); res_far = band_eval(t_far, 'T2.6b_bands')
for band in ('e24', 'e32', 'e44', 'rmax_training', 'rmax_refined'):
    for s in SHAPES:
        check('T2.6b_%s_all_raw_columns_%s' % (band, s), res_far[band]['columns_'+s]['worst_ratio'], 1e-11, **{k: v for k, v in res_far[band]['columns_'+s].items() if k != 'worst_ratio'})
        check('T2.6b_%s_Rf_%s' % (band, s), res_far[band]['Rf_'+s]['ratio'], 1e-11, rho=res_far[band]['Rf_'+s]['rho'], abs_error=res_far[band]['Rf_'+s]['abs'])
t_fin = run_points(FINITE_V92, 'T2.6c'); res_fin = band_eval(t_fin, 'T2.6c_bands')
for band, v in res_fin.items():
    for s in SHAPES:
        check('T2.6c_%s_all_raw_columns_%s' % (band, s), v['columns_'+s]['worst_ratio'], 1e-11, failing=v['columns_'+s]['failing_count'], worst_index=v['columns_'+s]['worst_index'])
        check('T2.6c_%s_Rf_%s' % (band, s), v['Rf_'+s]['ratio'], 1e-11, rule='SPEC v9: 1e-11 band_max in every band and every shape', rho=v['Rf_'+s]['rho'], abs_error=v['Rf_'+s]['abs'])
out['largest_shape_differences'] = {'Rf': max(v['Rf_largest_shape_difference'] for v in list(res_fin.values())+list(res_far.values())), 'columns_absolute': max(v['columns_largest_shape_difference'] for v in list(res_fin.values())+list(res_far.values())), 'columns_relative_to_band_max': max(v['columns_largest_shape_difference_relative_to_band_max'] for v in list(res_fin.values())+list(res_far.values()))}
out['rho_rows'] = [{'band': r_['band'], 'r': r_['r'], 'Rf_hp85': r_['Rf_hp85'], 'S_R': r_['S_R'], **{'rho_'+s: abs(r_['Rf_'+s]-r_['Rf_hp85'])/(U*r_['S_R']) for s in SHAPES}} for r_ in t_fin+t_far]
out['rho_definition'] = 'rho = |Rf_provider - Rf_hp85| / (u S_R), u = 2^-64 (longdouble unit roundoff actually used); S_R = R_f assembled with every field replaced by sum_i |c_i phi_i| (centered q terms inside r_s, stable L_i terms outside), all products in absolute value'
out['points_on_both_sides_of_r_s'] = {'r_s': B.R_SWITCH, 'below': sorted(r_['r'] for r_ in t_fin if r_['r'] < B.R_SWITCH), 'above': sorted(r_['r'] for r_ in t_fin if r_['r'] >= B.R_SWITCH)}
out['points_on_both_sides_of_origin_radius'] = {'below_0.02': sorted(r_['r'] for r_ in t_fin if r_['r'] <= .02), 'above': sorted(r_['r'] for r_ in t_fin if r_['r'] > .02)}
# ---------------- T2.6d (SPEC v9.3 clause (d)): production chunking with its remainder chunk, and the integrator validation entrypoint
def embedded_call(mesh_, pts_rows, label):
    """A call of mesh_ size with the T2.6c points inserted at the start, in the middle and as the remainder chunk; returns R_f at the embedded points (three copies) and the restored-order residual on the mesh nodes."""
    xm, ym = mesh_.coordinates(); n = len(xm); k = len(pts_rows); px = np.array([r_['x'] for r_ in pts_rows]); py = np.array([r_['y'] for r_ in pts_rows])
    nb = 4096; n_direct_pad = ((n+2*k)//nb)*nb; tail = n_direct_pad+ (nb - ((n+2*k) % nb)) if (n+2*k) % nb else n+2*k   # position so that the last copy falls in a remainder chunk
    xs = np.concatenate([px, xm[:n//2], px, xm[n//2:], px]); ys = np.concatenate([py, ym[:n//2], py, ym[n//2:], py])
    return xs, ys, k, n
pts_rows = t_fin
xs_e, ys_e, k_e, n_e = embedded_call(mesh_tr, pts_rows, 'training')
t0 = time.time(); m_e, root_e = point_model(xs_e, ys_e, workers=workers); m_e.threads = 4; rf_e = m_e.fun(P, high)/root_e; out['T2.6d_training_sized_call_seconds'] = time.time()-t0
cache_e = m_e.cache_record(); n_dir = int(cache_e['direct_nodes']); out['T2.6d_training_sized_call'] = {'points_total': int(len(xs_e)), 'direct_nodes': n_dir, 'block_size': 4096, 'full_blocks': n_dir//4096, 'remainder_block_nodes': n_dir % 4096, 'embedded_copies': ['start', 'middle', 'end (remainder chunk)']}
copies = {'start': rf_e[:k_e], 'middle': rf_e[k_e+n_e//2:2*k_e+n_e//2], 'end': rf_e[-k_e:]}
restored = np.concatenate([rf_e[k_e:k_e+n_e//2], rf_e[2*k_e+n_e//2:2*k_e+n_e]])
ref_tr = Model860(mesh_tr, A_REF, block_size=4096, mode_block=64, workers=workers, threads=4, shared_series_cache=SHARED_SERIES); r_tr = ref_tr.fun(P, high)/ref_tr.root; ref_tr.clear_cache(); del ref_tr
tol64 = 64*np.finfo(float).eps*max(np.linalg.norm(r_tr), np.linalg.norm(restored), 1e-300)
check('T2.6d_training_mesh_residual_agrees_after_restoring_order_64eps', float(np.linalg.norm(r_tr-restored)), float(tol64), bitwise=bool(np.array_equal(r_tr, restored)), note='standard training-mesh call vs the embedded call with shifted chunk boundaries, R_f on the mesh nodes')
m_e.clear_cache(); del m_e
for cname, vals in copies.items():
    rows_c = [dict(r_, Rf_cfg=float(vals[i])) for i, r_ in enumerate(pts_rows)]
    for band in sorted({r_['band'] for r_ in rows_c}):
        sub = [r_ for r_ in rows_c if r_['band'] == band]; rfmax = max(max(abs(r_['Rf_hp85']) for r_ in sub), 1e-30); err = max(abs(r_['Rf_cfg']-r_['Rf_hp85']) for r_ in sub)
        check('T2.6d_chunking_%s_%s_Rf' % (cname, band), err/rfmax, 1e-11, bitwise_vs_single=bool(all(r_['Rf_cfg'] == r_['Rf_single'] for r_ in sub)))
# integrator validation entrypoint: refined-mesh-sized call through Integrator860.stateless (fork pool, block 4096)
class _MeshLike:
    def __init__(self, xs, ys): self._x = xs; self._y = ys; self.weights = np.ones(len(xs)); self.size = len(xs); self.fingerprint = 'embedded'
    def coordinates(self): return self._x, self._y
xs_r, ys_r, k_r, n_r = embedded_call(mesh_rf, pts_rows, 'refined')
integ = Integrator860(epoch, workers=workers); t0 = time.time(); rr_i = integ.stateless(P, high, _MeshLike(xs_r, ys_r))/np.sqrt(2/(np.pi*A_REF**2)); out['T2.6d_integrator_refined_sized_call_seconds'] = time.time()-t0
copies_i = {'start': rr_i[:k_r], 'middle': rr_i[k_r+n_r//2:2*k_r+n_r//2], 'end': rr_i[-k_r:]}
for cname, vals in copies_i.items():
    rows_c = [dict(r_, Rf_cfg=float(vals[i])) for i, r_ in enumerate(pts_rows)]
    for band in sorted({r_['band'] for r_ in rows_c}):
        sub = [r_ for r_ in rows_c if r_['band'] == band]; rfmax = max(max(abs(r_['Rf_hp85']) for r_ in sub), 1e-30); err = max(abs(r_['Rf_cfg']-r_['Rf_hp85']) for r_ in sub)
        check('T2.6d_integrator_entrypoint_%s_%s_Rf' % (cname, band), err/rfmax, 1e-11, bitwise_vs_single=bool(all(r_['Rf_cfg'] == r_['Rf_single'] for r_ in sub)))
restored_i = np.concatenate([rr_i[k_r:k_r+n_r//2], rr_i[2*k_r+n_r//2:2*k_r+n_r]]); rr_std = integ.stateless(P, high, mesh_rf)/np.sqrt(2*mesh_rf.weights/(np.pi*A_REF**2))
tol64r = 64*np.finfo(float).eps*max(np.linalg.norm(rr_std), np.linalg.norm(restored_i), 1e-300)
check('T2.6d_refined_mesh_integrator_residual_agrees_after_restoring_order_64eps', float(np.linalg.norm(rr_std-restored_i)), float(tol64r), bitwise=bool(np.array_equal(rr_std, restored_i)))
out['T2.6d_largest_configuration_difference_Rf'] = max(float(np.max(abs(v-np.array([r_['Rf_single'] for r_ in pts_rows])))) for v in list(copies.values())+list(copies_i.values()))
# ---------------- T2.6x (SPEC v9.3): exceptional parameters, one-point shape, seed coefficients with c_l replaced
X_CL = [2.0, 3.0, 2*(1+2**-20), 3*(1-2**-20)]; out['T2.6x'] = {}
for clx in X_CL:
    Px = P.copy(); Px[0] = clx; prepx = share_prepared(B.prepare(clx, Px[1:], high), Px, high)
    def hp_ref_x(args):
        band, x, y = args; ref = H.point_reference(prepx, x, y, 85, True); return {'band': band, 'Rf': ref['Rf'], 'columns': ref['columns']}
    import multiprocessing as mp
    t0 = time.time()
    with mp.get_context('fork').Pool(min(workers, len(FINITE_V92))) as pool: refs = pool.map(hp_ref_x, FINITE_V92)
    rows_x = []
    for i, (b, x, y) in enumerate(FINITE_V92):
        mx, rootx = point_model([x], [y]); rf1 = float((mx.fun(Px, high)/rootx)[0]); dr1 = (mx.jacobian(Px, high)/rootx[:, None])[0]
        rows_x.append({'band': b, 'x': x, 'y': y, 'r': math.hypot(x, y), 'Rf_hp85': refs[i]['Rf'], 'Rf_single': rf1, 'cols_hp85': refs[i]['columns'], 'cols_single': dr1})
    resx = {}
    for band in sorted({r_['band'] for r_ in rows_x}):
        sub = [r_ for r_ in rows_x if r_['band'] == band]; rfmax = max(max(abs(r_['Rf_hp85']) for r_ in sub), 1e-30); cref = np.array([r_['cols_hp85'] for r_ in sub]); cmax = np.maximum(np.max(abs(cref), axis=0), 1e-30)
        ratio = np.max(abs(np.array([r_['cols_single'] for r_ in sub])-cref), axis=0)/cmax; err = max(abs(r_['Rf_single']-r_['Rf_hp85']) for r_ in sub)
        resx[band] = {'Rf_ratio': err/rfmax, 'Rf_band_max': rfmax, 'columns_worst_ratio': float(ratio.max()), 'columns_worst_index': int(np.argmax(ratio)), 'columns_failing': int(np.count_nonzero(ratio > 1e-11)), 'columns_floor_cases': [int(i_) for i_ in np.flatnonzero(cmax <= 1e-30)]}
        check('T2.6x_cl%r_%s_Rf' % (clx, band), resx[band]['Rf_ratio'], 1e-11); check('T2.6x_cl%r_%s_all_columns' % (clx, band), resx[band]['columns_worst_ratio'], 1e-11, failing=resx[band]['columns_failing'], floor_cases=len(resx[band]['columns_floor_cases']))
    out['T2.6x']['cl=%r' % clx] = {'cl_hex': float(clx).hex(), 'bands': resx, 'seconds': time.time()-t0, 'points': [{k: v for k, v in r_.items() if not k.startswith('cols_')} for r_ in rows_x]}
np.savez_compressed(out_path.with_name('g2_t26_arrays.npz'), **{'%s_%d_%s' % (lab, i, s): r_['cols_'+s] for lab, rows in (('far', t_far), ('fin', t_fin)) for i, r_ in enumerate(rows) for s in SHAPES+('hp85',)})
for rows in (t_far, t_fin):
    for r_ in rows:
        for s in SHAPES+('hp85',): r_.pop('cols_'+s)
out['far_points'] = t_far; out['finite_points'] = t_fin; out['import_closure'] = loaded_closure()
out['passed'] = all(c['passed'] for c in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
