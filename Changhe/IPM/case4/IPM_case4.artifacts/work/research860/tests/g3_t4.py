"""G3 test T4 (G3 copy; lead pre-audit 10:07Z F1-F8 applied; --dry-run exits after loading the inputs): constraint Jacobian ranks, chart lifts, analytic vs finite-difference Jacobian at
three steps (c_l along the v9.16 direction, low tangent, high incl. small-n j = 1, 2, weakest singular vectors, projected dilation D), dilation tangency with row scales, zero-step
equality (bitwise or 64 eps, branch recorded; also a zero trial through campaign860.feasible_trial when importable), full spectrum (all 855 values stored, A.shape recorded).
Step convention (F6): a direction v is a unit vector in the scaled feasible coordinates (855); the physical raw step is h*v*scales ([c_l-chart part 55 -> lifted low coordinates, high 800]);
the feasible-coordinate step norm ||h v scales||, the actual raw displacement of the lifted point and its ratio to the norm of the affected raw coordinates (null with a reason when that norm is 0, e.g. high (0,0,1) at the seed) are recorded per step. Usage: g3_t4.py <out.json> <manifest.json> [workers] [--dry-run]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, sys, time, gc, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import basis860 as B, chart860 as C
from model860 import Model860, feasible_matrix
import campaign860 as CM                                   # defect 7: imported at the top; an ImportError fails the step (the frozen closure must contain the driver and its helpers)
from fields860 import residual as new_residual
from absolute_common import read, ROOT, A_REF, digest, array_hash
from absolute_model import FrozenLogMesh
from stage13_solver import DenseTrustModel
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'tools')); from runtime import Runtime
rt = Runtime(str(Path(__file__).resolve().parents[2]))
argv = [a for a in sys.argv[1:] if a != '--dry-run']; DRY = '--dry-run' in sys.argv
out_path = Path(argv[0]); manifest_path = Path(argv[1]); workers = int(argv[2]) if len(argv) > 2 else 8
out = {'schema': 'g3_t4_v1', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'timings': {}, 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))     # SPEC v8 item 3
    if any(c['check'] == name for c in out['checks']): raise RuntimeError('duplicate check name %s' % name)   # F7
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
seed = json.loads(Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.json')).read_text())
sd = np.load(B.REPLAY_REFERENCE_FILE)                                   # repaired-evaluator replay reference (SPEC v8 item 4)
P = sd['P'].copy(); high = sd['high'].copy(); r_seed = sd['residual'].copy()
with np.load(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.npz'), allow_pickle=False) as s1: scales_seed = s1['column_scales'].copy()   # g2_v1 preview copies, comparison only (not evidence)
if DRY: print('DRY RUN OK: imports, seed JSON, replay reference and g2_v1 preview copies resolve', flush=True); raise SystemExit(0)
check('T4.0_seed_json_P_high_equal_replay_arrays', seed['P_raw_chart_hex'] == [float(v).hex() for v in P] and seed['high_hex'] == [float(v).hex() for v in high])   # F8
state = rt.read(ROOT/'campaign/global181_v3/state.json'); epoch = rt.read(state['epoch_path']); mesh = FrozenLogMesh.load(epoch['meshes']['training']['path'])
cl = float(P[0])
# ---- T4.2 constraint Jacobian ranks and singular values
G = C.constraint_jacobian(P); sG = np.linalg.svd(G, compute_uv=False); sGc = np.linalg.svd(G[:, 1:], compute_uv=False)
strain = B.center_data(cl)[0]
G6 = C.unreduced_constraint_jacobian(P)      # 6 x 61 (center + C5) on (cl, a_000, a_1..a_59), a_000 independent; high rows are identically zero
sG6 = np.linalg.svd(G6, compute_uv=False); sG6c = np.linalg.svd(G6[1:, 2:], compute_uv=False)
check('T4.2_reduced_C5_rank_5_of_5x60', int(np.linalg.matrix_rank(G)) == 5, singular_values=sG.tolist()); check('T4.2_reduced_C5_coefficient_block_rank_5', int(np.linalg.matrix_rank(G[:, 1:])) == 5, singular_values=sGc.tolist())
check('T4.2_unreduced_center_plus_C5_rank_6_of_6x61', int(np.linalg.matrix_rank(G6)) == 6, singular_values=sG6.tolist(), gap_ratio=float(sG6[-1]/sG6[0]), center_row_cl_entry=float(G6[0, 0]), center_row_a000_entry=float(G6[0, 1]))
check('T4.2_unreduced_C5_block_a1_a59_rank_5', int(np.linalg.matrix_rank(G6[1:, 2:])) == 5, singular_values=sG6c.tolist())
out['constraint_rank_statement'] = 'center + five C5 on (cl, 860 raw a): the high block has identically zero rows, so the rank equals that of the 6 x 61 low system; feasible count 861 - 6 = 855 as a rank-based local count'
# ---- chart
t0 = time.perf_counter(); chart = C.Chart860(P); out['timings']['chart_s'] = time.perf_counter()-t0; gd = chart.geometry_diagnostics; out['chart_geometry'] = {k: v for k, v in gd.items() if k != 'base_HP'}
check('T4.3_tangent_rank_55', gd['tangent_rank'] == 55); check('T4.3_complete_rank_60', gd['complete_rank'] == 60); check('T4.3_G_T_small', gd['tangent_constraint_error'], 1e-8)
# old 19 tangent directions inside the new 55 (through the embedding derivative of the free coordinates)
from absolute_chart_v2 import AbsoluteC5ChartV2
from absolute_fields import prepare_candidate
cand = read(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json'); prep = prepare_candidate(cand, 'center_chart')
Eraw = np.zeros((60, 24)); Eraw[0, 0] = 1.; Efull = np.zeros((860, 24)); Efull[0, 0] = 1.
for jold, (m, s) in enumerate(B.OLD_CORE_ORDER):
    if jold == 0: continue
    for kind, idx, f in B.old_core_to_internal(m, s):
        if kind == 'low' and idx != 0: Eraw[idx, jold] += f; Efull[idx, jold] += f
        if kind == 'high': Efull[60+idx, jold] += f          # the (3,2) -> (3,0,0) high component
Tseed = AbsoluteC5ChartV2(prep['p']).base_tangent
Told = Eraw@Tseed; proj = chart.base_tangent@np.linalg.lstsq(chart.base_tangent, Told, rcond=None)[0]
check('T4.3_old_19_tangent_low_projection_inside_new_55', float(np.linalg.norm(proj-Told)/np.linalg.norm(Told)), 1e-9,
      label='low-projection test; valid as the full test because every high generator starts at potential degree 10 while the center and C5 use degrees <= 8, so the high block has zero constraint rows and the feasible tangent is T_low (55) + R^800')
Tfull = Efull@Tseed                                      # 860 x 19 in (cl, 59 low, 800 high)
basis_full = np.zeros((860, 855)); basis_full[:60, :55] = chart.base_tangent; basis_full[60:, 55:] = np.eye(800)
proj_full = basis_full@np.linalg.lstsq(basis_full, Tfull, rcond=None)[0]
check('T4.3_old_19_tangent_full_embedded_inside_855', float(np.linalg.norm(proj_full-Tfull)/np.linalg.norm(Tfull)), 1e-9, high_component_norm=float(np.linalg.norm(Tfull[60:])), low_component_norm=float(np.linalg.norm(Tfull[:60])))
# ---- T4.4 lifts
rng = np.random.default_rng(55)
for k in range(3):
    q = rng.normal(size=55); q *= 1e-3/np.linalg.norm(q); Pq = chart.lift_delta(q); rep = C.hp_report(Pq)
    check('T4.4_lift%d_C5_max' % k, rep['max_abs'], 1e-10, iterations=len(chart.last_diagnostics['iterations'])); check('T4.4_lift%d_cl_bits' % k, float(Pq[0]).hex() == float((P+chart.free@q)[0]).hex())
    h = 1e-5; u = q/np.linalg.norm(q); fd = (chart.lift_delta(h*u)-chart.lift_delta(-h*u))/(2*h); an = chart.base_tangent@u
    check('T4.4_lift%d_tangent_fd_rel' % k, float(np.linalg.norm(fd-an)/np.linalg.norm(an)), 1e-6)
# ---- model, Jacobian, feasible matrix, spectrum (T4.8)
model = Model860(mesh, A_REF, block_size=4096, mode_block=64, workers=workers)
t0 = time.perf_counter(); r0 = model.fun(P, high); out['timings']['fun_cold_s'] = time.perf_counter()-t0
def zero_step_check(name, rz, ref):
    """F3 / SPEC section 10: passes if bitwise equal (tobytes) or diff_norm <= 64 eps ||ref|| (section 15 replay rule); the branch is recorded."""
    bitwise = rz.tobytes() == ref.tobytes(); dn = float(np.linalg.norm(rz-ref)); tol = float(64*np.finfo(float).eps*np.linalg.norm(ref))
    check(name, bool(bitwise or dn <= tol), bitwise=bool(bitwise), diff_norm=dn, tol_64eps=tol, branch=('bitwise' if bitwise else ('64eps' if dn <= tol else 'fail')))
zero_step_check('T4.7_zero_step_vs_seed_residual_bitwise_or_64eps', r0, r_seed)
t0 = time.perf_counter(); J = model.jacobian(P, high); out['timings']['jacobian_s'] = time.perf_counter()-t0
A, scales = feasible_matrix(J, chart); out['scales_vs_g2_v1_preview_copies'] = {'max_rel_difference': float(np.max(abs(scales-scales_seed)/scales_seed)), 'note': 'g2_v1 preview scales are not evidence; difference reflects the repaired evaluator'}
t0 = time.perf_counter(); factors = DenseTrustModel(A, r0); out['timings']['svd_full_s'] = factors.factor_seconds; out['timings']['dense_trust_model_s'] = time.perf_counter()-t0
s = factors.s; out['spectrum'] = {'count': len(s), 'max': float(s[0]), 'min': float(s[-1]), 'cond': float(s[0]/s[-1]), 'diagnostic_rank': factors.diagnostic_rank, 'rank_floor': float(factors.rank_floor), 'log10_quantiles_0_10_50_90_100': np.log10(np.quantile(s, [0, .1, .5, .9, 1])).tolist(), 'stationarity': {k: v for k, v in factors.stationarity().items() if k != 'singular_values'}}
out['spectrum']['singular_values'] = s.tolist(); out['A_shape'] = list(A.shape)                                                      # F1
check('T4.8_all_855_singular_values_positive', bool(np.all(s > 0)), count=len(s)); check('T4.8_spectrum_count_855', len(s) == 855, A_shape=list(A.shape), expected_A_shape=[90624, 855]); check('T4.8_A_shape_90624_x_855', list(A.shape) == [90624, 855], A_shape=list(A.shape))
# lead request (04:23Z, 04:40Z): weighted residual-Jacobian column norms of the j=3 low generators and their quadrature-weighted field norms
Jn = np.linalg.norm(J, axis=0); weak_cols = {}
Mall = B.low_matrices(cl, model.x, model.y)   # direct formula for the single generators on every training node (no cancellation for a single monomial)
fnorm = np.linalg.norm(model.root[:, None]*Mall['f'], axis=0); qnorm = np.linalg.norm(model.root[:, None]*Mall['ratio'], axis=0)
med_f = float(np.median(fnorm[1:])); med_q = float(np.median(qnorm[1:]))
for tr in [(0, 0, 3), (0, 1, 3), (1, 1, 3), (0, 2, 3), (2, 2, 3)]:
    idx = B.LOW_INDEX[tr]
    weak_cols['low_%d_%d_%d' % tr] = {'raw_column_index': idx, 'weighted_residual_jacobian_column_norm': float(Jn[idx]), 'ratio_to_max_column_norm': float(Jn[idx]/Jn.max()),
        'quadrature_weighted_field_norm_f': float(fnorm[idx]), 'ratio_f_to_median_of_59_free_low': float(fnorm[idx]/med_f), 'quadrature_weighted_field_norm_psix_over_y': float(qnorm[idx]), 'ratio_ratio_to_median_of_59_free_low': float(qnorm[idx]/med_q),
        'note': 'raw column index = internal low index (only (0,0,0), index 0, is eliminated); the Jacobian column already contains the a_000 chain; field norms are sqrt(sum_i w_i*2/(pi a_ref^2) field_i^2) on the training mesh; p_3 - 1 = %.6f at the seed' % (B.p_exponents(cl)[0][3]-1)}
out['j3_low_columns'] = {'columns': weak_cols, 'smallest_scaled_singular_values': s[-5:].tolist(), 'largest_scaled_singular_value': float(s[0]), 'raw_column_norm_min': float(Jn[1:].min()), 'raw_column_norm_max': float(Jn.max()), 'raw_column_norm_argmin': int(np.argmin(Jn[1:])+1), 'median_field_norm_f_59_free_low': med_f, 'median_field_norm_ratio_59_free_low': med_q}
out['numerical_rank'] = {'diagnostic_rank': factors.diagnostic_rank, 'rank_floor': float(factors.rank_floor), 'columns': int(A.shape[1]), 'smallest_singular_value': float(s[-1]), 'note': 'positivity of binary64 singular values is not a rank certificate; no truncation is applied (SPEC section 11)'}
# ---- T4.5 analytic vs FD along directions (scaled feasible coordinates d in R^855; physical step = scales*d; lift the low part)
def trial_residual(d):
    phys = d*scales; Pp = chart.lift_delta(phys[:55]); hh = high+phys[55:]
    return model.fun(Pp, hh)
directions = {}
# c_l along the chart (SPEC v9.16): t = base_tangent[0,:] * scales[:55] is the c_l row of the scaled tangent; v = t/||t|| is the unit direction in scaled feasible coordinates that moves c_l
tcl = chart.base_tangent[0, :]*scales[:55]; v = np.zeros(855); v[:55] = tcl/np.linalg.norm(tcl); directions['cl_along_chart_v916'] = v
for i in rng.choice(55, 5, replace=False): v = np.zeros(855); v[i] = 1.; directions['low_tangent_%d' % i] = v
for (m, n, j) in [(0, 0, 0), (0, 20, 0), (3, 0, 0), (5, 17, 1), (9, 16, 2), (2, 5, 3), (7, 18, 3), (4, 12, 1), (6, 19, 0), (8, 17, 1), (1, 20, 2), (9, 16, 3), (0, 0, 1), (5, 2, 1), (0, 0, 2), (6, 3, 2)]:   # includes n = 25 - v_m for one m in each j; F5: small-n j = 1, 2
    v = np.zeros(855); v[55+B.HIGH_INDEX[(m, n, j)]] = 1.; directions['high_m%d_n%d_j%d' % (m, n, j)] = v
for k in range(3): directions['weakest_singular_%d' % k] = factors.vt[-(k+1)].copy()
# projected dilation D in internal coordinates: 4 chi - X.grad chi = (4-2k) chi_{mkj} - 2(p_j-k) chi_{m,k+1,j}; drop k=26 terms; convert to internal (low: direct; high: via T^-1); include cl? dilation leaves cl fixed.
low_now = np.r_[float(C.hp_report(P)['coefficients_decimal'][0]), P[1:]]                                                  # F8: a_000 from the chart report of the actual P
aD = B.internal_to_canonical_exact(low_now, high, 60, round_output=False)
from decimal import Decimal, localcontext
with localcontext() as ctx:
    ctx.prec = 60; pD, _ = B.p_exponents(Decimal.from_float(cl)); da = [Decimal(0)]*860; leak_coef = {}
    for (j, m, k) in B.CANONICAL:
        a = aD[B.canonical_index(j, m, k)]
        if a == 0: continue
        da[B.canonical_index(j, m, k)] += (4-2*k)*a
        if k+1 <= 25: da[B.canonical_index(j, m, k+1)] += -2*(pD[j]-k)*a
        else: leak_coef[(m, j)] = -2*(pD[j]-25)*a               # dropped k = 26 terms
    leak = {'%d,%d' % k_: float(v) for k_, v in leak_coef.items()}
    dlow, dhigh = B.canonical_to_internal_exact(da, 60); dlow = np.array([float(v) for v in dlow]); dhigh = np.array([float(v) for v in dhigh])
# a_000 semantics: the generator's own a_000 component is dlow[0]; in the chart a_000 follows the center condition, whose linearization gives -(s.dlow[1:])/s_0;
# the exact dilation preserves the center condition, so both agree up to the seed's center arithmetic.
raw60 = np.r_[0., dlow[1:]]                                 # cl component 0 (dilation keeps cl), a_000 implicit
qlow = np.linalg.lstsq(chart.base_tangent, raw60, rcond=None)[0]; resid_low = raw60-chart.base_tangent@qlow
Dfeas = np.r_[qlow, dhigh]/scales                           # scaled feasible coordinates with scales*Dfeas = physical step (per unit log L)
Draw860 = np.r_[0., dlow[1:], dhigh]                        # physical raw step per unit log L in [cl, 59 low, 800 high]
proj_col = J@Draw860                                        # residual-vector change of the projected dilation per unit log L (raw physical scale)
# leakage column: the dropped k=26 generators' residual columns (direct evaluation of chi_{m,26,j} on the training mesh), times their coefficients
def generator_residual_column(m, k, j):
    q = model.x**2+model.y**2; R = 1+q; u = 1/R; t_ = q*u; s_ = np.log1p(q); root = np.sqrt(R); xn = model.x/root; yn = model.y/root
    from absolute_fields import _harmonics, _assemble
    F_, _ = B.radial_jets(cl, j, m, u, B._power_jets(t_, k-m, 5)); vals = _assemble(*_harmonics(xn, yn, t_, m), xn, yn, t_, F_, 2*m)
    g = {key: np.exp(B.pdiff(cl, j, B.S_ORDERS[key])*s_)*vals[key] for key in B.KEYS}
    ff = model._fields; direct = model.direct
    col = np.zeros(mesh.size); wx = cl*model.x[direct]-ff['psiy']; wy = cl*model.y[direct]+ff['psix']
    col[direct] = wx*g['fx'][direct]+wy*g['fy'][direct]+ff['q']*g['f'][direct]-ff['fx']*g['psiy'][direct]+ff['fy']*g['psix'][direct]+ff['f']*g['ratio'][direct]
    return model.root*col                                   # origin nodes: potential degree 52, contribution below double precision; left at zero
leak_col = sum(c_*generator_residual_column(m_, 26, j_) for (m_, j_), c_ in ((tuple(int(v) for v in key.split(',')), val) for key, val in leak.items()))
out['dilation'] = {'k26_leakage_coefficients': leak, 'low_projection_residual_rel': float(np.linalg.norm(resid_low)/max(np.linalg.norm(raw60), 1e-300)), 'a000_component_of_generator': float(dlow[0]), 'a000_implied_by_center_linearization': float(-(strain[1:]@dlow[1:])/strain[0]),
                   'projected_column_norm_per_unit_logL': float(np.linalg.norm(proj_col)), 'k26_leakage_residual_column_norm_per_unit_logL': float(np.linalg.norm(leak_col)), 'residual_norm': float(np.linalg.norm(r0)),
                   'p_j_precision': '60-digit Decimal from the binary64 c_l', 'a000_semantics': 'generator applied to the full raw a including the analytic a_000; chart a_000 follows the center condition'}
directions['projected_dilation_D'] = Dfeas/np.linalg.norm(Dfeas)
out['dilation']['VT_D_weakest_3'] = [float(factors.vt[-(k+1)]@directions['projected_dilation_D']) for k in range(3)]                  # F8: V^T D for the weakest vectors
# tangency T4.6: G D_raw vs weights w = (-2Ex, -2Ey, -4D1, -4D2, -4D3); rowscale_i = norm of coefficient part of row i
hp = C.hp_report(P); Ex, Ey, D1, D2, D3 = hp['constraints']; w = np.array([-2*Ex, -2*Ey, -4*D1, -4*D2, -4*D3])
Draw = np.r_[0., dlow[1:]]; GD = G@Draw; rowscale = np.linalg.norm(G[:, 1:], axis=1)
check('T4.6_dilation_tangency_rows', float(np.max(abs(GD-w)/(rowscale*np.linalg.norm(Draw)))), 1e-10, GD=GD.tolist(), w=w.tolist(), rowscale=rowscale.tolist())
x, y = mesh.coordinates(); from fields860 import exact_dilation_fields
seedp = B.prepare(cl, P[1:], high)
def Jdil_fn(L):
    ff = exact_dilation_fields(seedp, x, y, L); wx = cl*x-ff['psiy']; wy = cl*y+ff['psix']; return model.root*(wx*ff['fx']+wy*ff['fy']+ff['q']*ff['f'])
cols_h = {}
for hL in (1e-3, 1e-4, 1e-5): cols_h[hL] = (Jdil_fn(1+hL)-Jdil_fn(1-hL))/(2*hL)      # finite-difference estimate of the exact dilation column d r/d log L
dil_col = cols_h[1e-4]
out['dilation']['exact_dilation_column_FD'] = {'method': 'centered finite difference of the exactly dilated fields on the frozen mesh (per unit log L); not analytic',
    'norms': {str(h_): float(np.linalg.norm(c_)) for h_, c_ in cols_h.items()}, 'refinement_differences': {'1e-3_vs_1e-4': float(np.linalg.norm(cols_h[1e-3]-cols_h[1e-4])), '1e-4_vs_1e-5': float(np.linalg.norm(cols_h[1e-4]-cols_h[1e-5]))}}
out['dilation']['exact_minus_projected_column_norm'] = float(np.linalg.norm(dil_col-proj_col)); out['dilation']['exact_minus_projected_minus_k26_norm'] = float(np.linalg.norm(dil_col-proj_col-leak_col))
out['dilation']['cosine_projected_vs_exact'] = float(proj_col@dil_col/(np.linalg.norm(proj_col)*np.linalg.norm(dil_col)))
out['dilation']['dJ_along_projected_D_per_unit_logL'] = float(r0@proj_col); out['dilation']['dJ_along_exact_FD_column'] = float(r0@dil_col); out['dilation']['dJ_along_k26_leak'] = float(r0@leak_col)
out['dilation']['verifier_topic17_reference'] = {'source': 'c4-ver/VERIFY_REPORT.md 04:14:36Z, research/basis860-dilation', 'dJ_D_exact': 0.0, 'dJ_D_proj': 19.33673805899552517024, 'dJ_leak': -19.33673805899552517024,
    'weighted_residual_derivative_squared_norm_projected': 5.479107913199974e14, 'weighted_residual_derivative_squared_norm_leak': 5.479107913200783e14, 'weighted_residual_derivative_squared_norm_exact': 1.199175682129626e-7, 'leaking_generator': '(j,m,k)=(0,8,26)', 'leak_coefficient': 60583.2264578523,
    'note': 'verifier values are an unscaled physical-direction comparison; my projected/leak/exact column norms squared per unit log L are the comparable quantities'}
out['dilation']['my_squared_norms'] = {'projected': float(np.linalg.norm(proj_col)**2), 'leak': float(np.linalg.norm(leak_col)**2), 'exact_FD': float(np.linalg.norm(dil_col)**2)}
AD = A@directions['projected_dilation_D']; out['dilation']['A_Ds_norm_over_Ds_norm_scaled_metric'] = float(np.linalg.norm(AD)); out['dilation']['smallest_singular'] = float(s[-1]); out['dilation']['median_singular'] = float(np.median(s))
# FD runs: central differences at relative steps 1e-4, 1e-5, 1e-6; baseline predicate = every completed step passes (raw 3e-5, feasible 1e-3) and every lifted FD point has C5 max < 1e-10
fd_rows = []
def lifted_c5(d):
    phys = d*scales; Pp = chart.lift_delta(phys[:55]); return C.hp_report(Pp)['max_abs']
for name, v in directions.items():
    v = v/np.linalg.norm(v); an = A@v; steps = []
    phys_unit = v*scales; raw_params = np.r_[P, high]
    for h in (1e-4, 1e-5, 1e-6):
        try:
            rp = trial_residual(h*v); rm = trial_residual(-h*v); fd = (rp-rm)/(2*h)
            feas_norm = float(np.linalg.norm(h*phys_unit))                                                                   # ruling 7: feasible-coordinate step norm ||h v scales||
            Pp_h = chart.lift_delta(h*phys_unit[:55]); raw_disp = np.r_[Pp_h-P, h*phys_unit[55:]]; aff_idx = np.r_[np.flatnonzero(Pp_h-P != 0), 60+np.flatnonzero(phys_unit[55:] != 0)]
            aff_norm = float(np.linalg.norm(raw_params[aff_idx])) if len(aff_idx) else 0.; raw_disp_norm = float(np.linalg.norm(raw_disp))
            steps.append({'step': h, 'completed': True, 'relative_error': float(np.linalg.norm(fd-an)/max(np.linalg.norm(an), 1e-300)), 'max_abs_error': float(np.max(abs(fd-an))), 'an_norm': float(np.linalg.norm(an)),
                          'feasible_coordinate_step_norm': feas_norm, 'raw_displacement_norm_of_lifted_point': raw_disp_norm, 'affected_raw_coordinate_norm': aff_norm,
                          'raw_displacement_ratio': (raw_disp_norm/aff_norm if aff_norm > 0 else None), 'raw_displacement_ratio_null_reason': (None if aff_norm > 0 else 'affected raw coordinates are 0 at the seed (ratio undefined)'),          # F6 / ruling 7
                          'lifted_C5_max_plus': lifted_c5(h*v), 'lifted_C5_max_minus': lifted_c5(-h*v)})
        except (ValueError, np.linalg.LinAlgError) as exc: steps.append({'step': h, 'completed': False, 'failure': type(exc).__name__+': '+str(exc)})           # F2: baseline predicate; anything else re-raises
    done = [st for st in steps if st.get('completed')]
    best = min((st['relative_error'] for st in done), default=float('inf'))
    kind = 'feasible' if (name.startswith('cl') or name.startswith('low') or name.startswith('weakest') or name.startswith('projected')) else 'raw'
    thr = 1e-3 if kind == 'feasible' else 3e-5
    ratios = [done[i]['relative_error']/done[i+1]['relative_error'] if done[i+1]['relative_error'] else None for i in range(len(done)-1)]
    c5vals = [st['lifted_C5_max_plus'] for st in done]+[st['lifted_C5_max_minus'] for st in done]; c5max = (max(c5vals) if c5vals and all(math.isfinite(v) for v in c5vals) else (float('nan') if c5vals else None))   # defect 15: a NaN is not hidden by max()
    all_steps_pass = len(done) == 3 and all(math.isfinite(st['relative_error']) and st['relative_error'] <= thr for st in done) and (c5max is not None and math.isfinite(c5max) and c5max < 1e-10)          # F2: all three steps complete and pass
    fd_rows.append({'direction': name, 'kind': kind, 'steps': steps, 'best_relative_error': best, 'threshold': thr, 'passed_best': best <= thr, 'passed_all_completed_steps_baseline': all_steps_pass, 'steps_completed': len(done),
                    'convergence_ratios_consecutive_steps': ratios, 'lifted_point_C5_max': c5max, 'target_1e-6_met': best <= 1e-6, 'failures': [st for st in steps if not st.get('completed')]})
    print('T4.5', name, kind, 'best', best, 'all-steps', all_steps_pass, 'ratios', ratios, flush=True)
out['T4.5'] = fd_rows
check('T4.5_all_directions_pass_baseline_thresholds_best_step', all(r['passed_best'] for r in fd_rows), n_meeting_1em6_target=sum(r['target_1e-6_met'] for r in fd_rows), n=len(fd_rows))
check('T4.5_all_directions_pass_baseline_all_completed_steps_and_lifted_C5', all(r['passed_all_completed_steps_baseline'] for r in fd_rows), failing=[r['direction'] for r in fd_rows if not r['passed_all_completed_steps_baseline']])
# zero step through the chart API: E6: this is a DETERMINISM check of the evaluator at the seed (the lifted zero step reproduces the seed key, so Model860 answers from its
# evaluation cache unless cleared); the campaign860.feasible_trial zero trial is then evaluated with the evaluation cache cleared first, and the record requires that the
# residual was recomputed (evaluation_cache_hits unchanged across the call, fun_calls advanced).
r_zero = trial_residual(np.zeros(855)); zero_step_check('T4.7_zero_step_through_chart_determinism_bitwise_or_64eps', r_zero, r0)
Pz, hz, hpz = CM.feasible_trial(chart, P, high, np.zeros(855), scales); model.clear_cache(); hits0 = int(model.evaluation_cache_hits); calls0 = int(model.fun_calls); builds0 = int(model.cache_builds)   # E6: attributes, not cache_record (which has no fun_calls key)
rz2 = model.fun(Pz, hz); hits1 = int(model.evaluation_cache_hits); calls1 = int(model.fun_calls)
reevaluated = bool(hits1 == hits0 and calls1 == calls0+1)
zero_step_check('T4.7_zero_trial_through_campaign860_feasible_trial_reevaluated', rz2, r0)
check('T4.7_zero_trial_residual_was_recomputed_not_a_cache_hit', reevaluated, evaluation_cache_hits_before=hits0, evaluation_cache_hits_after=hits1, fun_calls_before=calls0, fun_calls_after=calls1, cache_builds_delta=int(model.cache_builds)-builds0)   # E6 (lead 11:27Z): integer attribute counters
out['zero_trial_feasible_trial'] = {'cl_bits_equal': float(Pz[0]).hex() == float(P[0]).hex(), 'C5_max': hpz['max_abs'], 'cache_cleared_before_evaluation': True}   # F3 (no fallback: defect 7)
out['cache_record'] = model.cache_record(); from closure860 import loaded_closure; out['import_closure'] = loaded_closure()
out['passed'] = all(r['passed'] for r in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
tmp = out_path.with_name(out_path.name+'.partial'); text = json.dumps(CM.durable(out), indent=1, default=str, allow_nan=False)+'\n'          # E9 / N10: sanitized (nonfinite -> null + '<key>_nonfinite'), allow_nan=False, fsync
with tmp.open('w') as f: f.write(text); f.flush(); os.fsync(f.fileno())
os.replace(tmp, out_path)
print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
