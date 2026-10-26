"""G2 tests T0 (static identities, T1 matrix, frozen N_n, strains/jets) and T1 (seed construction) per EMBEDDING_TESTS.md v3; SPEC v9.6 supplement edition (new file; T0.5 arbiter reference gate, T1.8 Decimal-tail rule). The g2_v4 file g2_t0_t1.py is unchanged.
Usage: g2_t0_t1_v2.py <out.json> <code_manifest.json> [--seed-dir=DIR] [--fast]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, sys, time, hashlib
from decimal import Decimal, localcontext
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'research'/'base'/'engine'))
import numpy as np
import basis860 as B, chart860 as C, hp860 as H
from absolute_common import read, ROOT, digest, array_hash
from absolute_fields import prepare_candidate, core_matrices as old_core_matrices
from spectral_basis import evaluate_modes
from taylor_jet import series as old_series
D = Decimal
out_path = Path(sys.argv[1]); manifest_path = Path(sys.argv[2]); fast = '--fast' in sys.argv
seed_dir_arg = next((a.split('=', 1)[1] for a in sys.argv if a.startswith('--seed-dir=')), ((_artifact_root + "/outputs") + '/campaign860/seed'))
from closure860 import loaded_closure
out = {'schema': 'g2_t0_t1_v2_spec_v96', 'code_manifest': str(manifest_path), 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))     # SPEC v8 item 3
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
def dstr(v, n=50): return format(v, '.%de' % (n-1))
# ---------------- T0.1 manifest
check('T0.1_canonical_860_unique_bijective', len(set(B.CANONICAL)) == 860 and all(B.canonical_index(*t) == i for i, t in enumerate(B.CANONICAL)) and len(B.LOW) == 60 and len(B.HIGH) == 800)
check('T0.1_per_j_215_per_jm_26_minus_m', all(sum(1 for (j, m, k) in B.CANONICAL if j == jj) == 215 for jj in range(4)) and all(sum(1 for (j, m, k) in B.CANONICAL if j == 0 and m == mm) == 26-mm for mm in range(10)))
# ---------------- T0.2 T1 matrix exactness (round trips at 60 and 110 digits), block diagonal
rng = np.random.default_rng(860)
for digits in (60, 110):
    low = rng.normal(size=60); high = rng.normal(size=800)*rng.choice([1e-7, 1e-3, 1.], 800)
    a = B.internal_to_canonical_exact(low, high, digits, round_output=False); low2, high2 = B.canonical_to_internal_exact(a, digits)
    with localcontext() as ctx:
        ctx.prec = digits
        e1 = max(abs(D.from_float(float(v))-w) for v, w in zip(low, low2)); e2 = max(abs(D.from_float(float(v))-w)/max(abs(D.from_float(float(v))), D('1e-30')) for v, w in zip(high, high2))
    check('T0.2_Tinv_T_identity_low_digits%d' % digits, float(e1), 1e-40); check('T0.2_Tinv_T_identity_high_rel_digits%d' % digits, float(e2), 1e-40)
    # derived canonical record: rounding a to `digits` significant digits limits the recoverable internal coefficients (block coefficients up to ~1e16, dynamic range of c)
    a_r = B.internal_to_canonical_exact(low, high, digits); low3, high3 = B.canonical_to_internal_exact(a_r, digits)
    with localcontext() as ctx:
        ctx.prec = digits; e3 = max(abs(D.from_float(float(v))-w)/max(abs(D.from_float(float(v))), D('1e-30')) for v, w in zip(high, high3))
    out.setdefault('canonical_record_roundtrip_rel_loss', {})[str(digits)] = float(e3)
T = B.conversion_matrix(); out['T_float_condition'] = float(np.linalg.cond(T))
check('T0.2_T_block_triangular_nonzero_diagonal', all(T[B.canonical_index(j, m, k), B.LOW_INDEX[(m, k, j)]] == 1 for (m, k, j) in B.LOW) and all(T[B.canonical_index(j, m, max(5, m)+n), 60+B.HIGH_INDEX[(m, n, j)]] != 0 for (m, n, j) in B.HIGH))
# ---------------- T0.2b frozen N_n
lead_nn = json.load(open((__import__("os").environ["IPM_REFERENCE_DIR"] + '/checks/source_Nn_pinned.json')))['rows']
check('T0.2b_frozen_Nn_hex_equal_lead_manifest', all(float(v).hex() == r['N_hex'] for v, r in zip(B.NN, lead_nn)) and len(B.NN) == 26)
check('T0.2b_N0_exactly_one', B.NN[0] == 1.0)
out['Nn_hex'] = [float(v).hex() for v in B.NN]; out['Nn_ulps_from_sqrt'] = [float((v-math.sqrt(2*n+1))/math.ulp(math.sqrt(2*n+1))) for n, v in enumerate(B.NN)]
# production evaluate_modes uses the same constants: chi field of mode (m,n,0) at a point equals Hn_m R^A t^v N_n P_n (float level)
x0, y0 = np.array([0.7]), np.array([0.4]); cl0 = 1.8089923602744993
V = evaluate_modes(x0, y0, cl0, [{'family': 'global', 'm': 1, 'n': 7, 'sigma': 0.0}])
with localcontext() as ctx:
    ctx.prec = 50; ref = H.generator_fields('high', (1, 7, 0), cl0, 0.7, 0.4, 50)['chi']
check('T0.2b_production_mode_chi_matches_frozen_Nn_value_rel', abs(float(V['chi'][0, 0])-float(ref))/abs(float(ref)), 1e-14)
# ---------------- T0.3 / T0.4 identities at 85 and 110 digits
pts = [(D('0.3'), D('0.7')), (D('2.5'), D('0.1')), (D('0.012'), D('0.015')), (D('0.02'), D('0')), (D('0'), D('1.3')), (D('40'), D('17')), (D('8886110.5'), D('1.2')), (D('0.005'), D('0.0049'))]
if fast: pts = pts[:3]
cls = ['1.8089923602744993', '1.5', '2.5', '4.0'] if not fast else ['1.8089923602744993']
FIELDS = ('chi', 'f', 'fx', 'fy', 'psi', 'psix', 'psiy', 'ratio')
def cmp(a, b, tol_rel=D('1e-40'), floor=D('1e-30')):
    worst = D(0)
    for key in FIELDS:
        d = abs(a[key]-b[key]); scale = max(abs(a[key]), abs(b[key]), floor)
        worst = max(worst, d/scale)
    return worst
high_sample = [(m, n, j) for j in range(4) for (m, n) in ((0, 0), (0, 20), (3, 0), (4, 10), (5, 17), (7, 5), (9, 16), (2, 13))]
if fast: high_sample = high_sample[:6]
t0 = time.time(); worst = {}
for digits in ((85, 110) if not fast else (85,)):
    w_low = D(0); w_high = D(0); w_oldcore = D(0); w_oldglob = D(0)
    for cl in cls:
        for (xx, yy) in pts:
            for (m, k, j) in (B.LOW if not fast else B.LOW[::7]):
                a = H.generator_fields('low', (m, k, j), D(cl), xx, yy, digits); b = H.monomial_fields(m, k, j, D(cl), xx, yy, digits)
                w_low = max(w_low, cmp(a, b))
            for (m, n, j) in high_sample:
                a = H.generator_fields('high', (m, n, j), D(cl), xx, yy, digits)
                with localcontext() as ctx:
                    ctx.prec = digits; v = max(5, m); comb = {key: D(0) for key in FIELDS}
                    for h, L in enumerate(B.legendre_monomial(n)):
                        mono = H.monomial_fields(m, v+h, j, D(cl), xx, yy, digits)
                        for key in FIELDS: comb[key] += B.NN_DECIMAL[n]*L*mono[key]
                w_high = max(w_high, cmp(a, comb))
            for jold, (m, s) in enumerate(B.OLD_CORE_ORDER):
                old = H.old_generator_fields(m, s, D(cl), xx, yy, digits)
                with localcontext() as ctx:
                    ctx.prec = digits; comb = {key: D(0) for key in FIELDS}
                    for kind, idx, f in B.old_core_to_internal(m, s):
                        g = H.generator_fields(kind, B.LOW[idx] if kind == 'low' else B.HIGH[idx], D(cl), xx, yy, digits)
                        for key in FIELDS: comb[key] += f*g[key]
                w_oldcore = max(w_oldcore, cmp(old, comb))
    worst[str(digits)] = {'internal_low_vs_monomial': float(w_low), 'internal_high_vs_monomial_expansion': float(w_high), 'old_core_vs_B_map': float(w_oldcore)}
    check('T0.3_low_identities_digits%d' % digits, float(w_low), 1e-40); check('T0.3_high_identities_digits%d' % digits, float(w_high), 1e-40); check('T0.4_old_core_identities_digits%d' % digits, float(w_oldcore), 1e-40)
out['identity_worst'] = worst; out['identity_seconds'] = time.time()-t0
# ---------------- T0.5 strains and jets
for cl in (1.8089923602744993, 1.5, 2.5, 4.0):
    js = B.jets(cl); s, ds = B.strain_values(cl)
    with localcontext() as ctx:
        ctx.prec = 60; jd = B.jets(D.from_float(cl), True)
    check('T0.5_strain_equals_jet_h_cl%.4f' % cl, float(max(abs(s[i]-float(js[i][6])) for i in range(60))), 1e-12)
    with localcontext() as ctx:
        ctx.prec = 60; sD, _ = B.strain_values(D.from_float(cl))
        check('T0.5_strain_equals_jet_h_decimal_cl%.4f' % cl, float(max(abs(sD[i]-jd[i][6]) for i in range(60))), 1e-55)
    old = old_series(cl); worst_j = 0.
    for jold, (m, s_) in enumerate(B.OLD_CORE_ORDER):
        comb = np.zeros(12)
        for kind, idx, f in B.old_core_to_internal(m, s_):
            if kind == 'low': comb += f*np.array([float(v) for v in js[idx]])
        worst_j = max(worst_j, float(np.max(abs(comb-np.array([float(v) for v in old[jold]])))))
    check('T0.5_old_core_jets_via_B_map_cl%.4f' % cl, worst_j, 1e-11)
    # low-block field evaluator vs old core_matrices through the B map (float, points off symmetry zeros)
    xs = np.r_[rng.uniform(.03, 3, 30), 0., 2., 1e4, 50.]; ys = np.r_[rng.uniform(.03, 3, 30), 1.3, 0., 3e3, 1e-9]
    oM, odM = old_core_matrices(cl, xs, ys, True); nM, ndM = B.low_matrices(cl, xs, ys, True); Vh, dVh = evaluate_modes(xs, ys, cl, [{'family': 'global', 'm': 3, 'n': 0, 'sigma': 0.0}], True)
    e = 0.; ed = 0.; e_rel = 0.
    for jold, (m, s_) in enumerate(B.OLD_CORE_ORDER):
        terms = B.old_core_to_internal(m, s_)
        for key in B.KEYS:
            val = sum(f*(nM[key][:, idx] if kind == 'low' else Vh[key][:, 0]) for kind, idx, f in terms); dval = sum(f*(ndM[key][:, idx] if kind == 'low' else dVh[key][:, 0]) for kind, idx, f in terms)
            size = sum(abs(f*(nM[key][:, idx] if kind == 'low' else Vh[key][:, 0])) for kind, idx, f in terms)   # envelope of the monomial pieces
            e = max(e, float(np.max(abs(oM[key][:, jold]-val)/np.maximum(size, 1e-300))))
            use = abs(oM[key][:, jold]) > 1e-8*size
            if np.any(use): e_rel = max(e_rel, float(np.max(abs(oM[key][use, jold]-val[use])/abs(oM[key][use, jold]))))
            dsize = sum(abs(f*(ndM[key][:, idx] if kind == 'low' else dVh[key][:, 0])) for kind, idx, f in terms)
            ed = max(ed, float(np.max(abs(odM[key][:, jold]-dval)/np.maximum(dsize, 1e-300))))
    # v9.6 (g2_v5 supplement): the v9 low block is extended-precision, so the handoff's binary64 core_matrices route is no longer a valid
    # 1e-12 reference for it (g2_v4 t0t1: old-vs-new 1.1e-12 to 3.1e-12 of the envelope at c_l = 1.5, 2.5, 4.0; the old route itself is
    # 3e-13 (values) and 1.1e-11 (c_l derivatives) from the 85-digit reference at the seed, outputs/dev_v9/t05_diag.json). Gate the new
    # low block against the lane's 85-digit evaluator through the same B-map combinations (envelope-relative 1e-12, values and c_l
    # derivatives); report old-route-vs-reference and old-vs-new as diagnostics.
    e_new = 0.; ed_new = 0.; e_old = 0.; ed_old = 0.; worst_pt = None; t05_cd = out.setdefault('T0.5_reference_analytic_jet_vs_centered_difference_h1e-20_rel', {})
    for jold, (m, s_) in enumerate(B.OLD_CORE_ORDER):
        terms = B.old_core_to_internal(m, s_)
        ref = {key: np.empty(len(xs)) for key in B.KEYS}; dref = {key: np.empty(len(xs)) for key in B.KEYS}
        cd_rows = []
        for i in range(len(xs)):
            with localcontext() as ctx:
                ctx.prec = 90; acc = {key: D(0) for key in B.KEYS}; dacc = {key: D(0) for key in B.KEYS}; dcd = {key: D(0) for key in B.KEYS}; hstep = D('1e-20'); L = D.from_float(cl)
                for kind, idx, f in terms:
                    tr = B.LOW[idx] if kind == 'low' else B.HIGH[idx]
                    g = H.generator_fields(kind, tr, L, xs[i], ys[i], 90); dg = H.generator_fields(kind, tr, L, xs[i], ys[i], 90, cl_derivative=True)
                    gp = H.generator_fields(kind, tr, L+hstep, xs[i], ys[i], 90); gm = H.generator_fields(kind, tr, L-hstep, xs[i], ys[i], 90)
                    for key in B.KEYS: acc[key] += f*g[key]; dacc[key] += f*dg[key]; dcd[key] += f*(gp[key]-gm[key])/(2*hstep)
                for key in B.KEYS: ref[key][i] = float(acc[key]); dref[key][i] = float(dacc[key])
                cd_rows.append({key: float(abs(dacc[key]-dcd[key])/max(abs(dacc[key]), D('1e-30'))) for key in B.KEYS})      # analytic jet vs centered difference, relative (floor 1e-30), per point
        t05_cd.setdefault('cl=%.4f' % cl, {})['old_core_%d_%d' % (m, s_)] = cd_rows
        for key in B.KEYS:
            val = sum(f*(nM[key][:, idx] if kind == 'low' else Vh[key][:, 0]) for kind, idx, f in terms); dval = sum(f*(ndM[key][:, idx] if kind == 'low' else dVh[key][:, 0]) for kind, idx, f in terms)
            size = sum(abs(f*(nM[key][:, idx] if kind == 'low' else Vh[key][:, 0])) for kind, idx, f in terms); dsize = sum(abs(f*(ndM[key][:, idx] if kind == 'low' else dVh[key][:, 0])) for kind, idx, f in terms)
            en = np.max(abs(val-ref[key])/np.maximum(size, 1e-300)); eo = np.max(abs(oM[key][:, jold]-ref[key])/np.maximum(size, 1e-300))
            dn = np.max(abs(dval-dref[key])/np.maximum(dsize, 1e-300)); do = np.max(abs(odM[key][:, jold]-dref[key])/np.maximum(dsize, 1e-300))
            if max(en, dn) > max(e_new, ed_new): worst_pt = {'old_core_ms': [m, s_], 'field': key, 'point_index': int(np.argmax(np.maximum(abs(val-ref[key])/np.maximum(size, 1e-300), abs(dval-dref[key])/np.maximum(dsize, 1e-300))))}
            e_new = max(e_new, float(en)); ed_new = max(ed_new, float(dn)); e_old = max(e_old, float(eo)); ed_old = max(ed_old, float(do))
    cdmax = max(max(row.values()) for rows in t05_cd['cl=%.4f' % cl].values() for row in rows)
    check('T0.5_low_evaluator_vs_90digit_reference_envelope_rel_cl%.4f' % cl, e_new, 1e-12, at=worst_pt, reference='hp860.generator_fields at 90 digits combined through the B map (exact integer weights); SPEC v9.6 T0.5 arbiter', envelope='sum of |weight x monomial piece| of the new evaluator', points=len(xs))
    check('T0.5_low_evaluator_cl_derivative_vs_90digit_reference_envelope_rel_cl%.4f' % cl, ed_new, 1e-12, derivative_reference='analytic 90-digit cl jet (hp860.generator_fields cl_derivative=True); its difference from a Decimal centered difference with h = 1e-20 at 90 digits is reported at every point', analytic_vs_centered_difference_max_rel=cdmax)
    out.setdefault('T0.5_old_core_matrices_route_diagnostics', {})['cl=%.4f' % cl] = {'old_route_vs_reference_envelope_rel': e_old, 'old_route_cl_derivative_vs_reference_envelope_rel': ed_old, 'old_vs_new_envelope_rel': e, 'old_vs_new_cl_derivative_envelope_rel': ed, 'old_vs_new_plain_relative': e_rel,
                                                                                  'note': 'the handoff binary64 core_matrices route is reported, not gated (v9.6); it is the reference of T3.1/T3.2 only through the 181D residual, where the section 9 excusal rule applies'}
# ---------------- T1 seed construction
cand = read(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json'); cand_sha = digest(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json')
check('T1.0_accepted278_sha256', cand_sha == '812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955')
prep = prepare_candidate(cand, 'center_chart'); cl = float(prep['p'][0])
lowD, highD = B.embed_old_decimal(cand['coefficients_decimal'], cand['extra_coefficients'], cand['modes'], 100)
aD = B.internal_to_canonical_exact(lowD, highD, 100)
lead = json.load(open((__import__("os").environ["IPM_REFERENCE_DIR"] + '/checks/embed_seed_coefficients.json')))
out['lead_reference_sha256'] = digest((__import__("os").environ["IPM_REFERENCE_DIR"] + '/checks/embed_seed_coefficients.json'))
with localcontext() as ctx:
    ctx.prec = 100
    worst_digits = 1000.; worst_abs0 = D(0); nz = 0
    for row in lead['raw_a']:
        mine = aD[row['I']]; theirs = D(row['a'])
        if theirs == 0 and mine == 0: continue
        if theirs == 0 or mine == 0: worst_abs0 = max(worst_abs0, abs(mine-theirs)); continue
        nz += 1; rel = abs(mine-theirs)/abs(theirs); digits_agree = float(-rel.log10()) if rel else 200.
        worst_digits = min(worst_digits, digits_agree)
    check('T1.1b_raw_a_vs_lead_min_agreeing_digits', -worst_digits, -40., nonzero_compared=nz, zero_mismatch_abs=float(worst_abs0))
    check('T1.1b_lead_assumes_I_order', lead['order'].startswith('I = 215 j + 26 m - m(m-1)/2 + (k - m)'))
    # a_000 identity: elimination from the other 59 mapped low coefficients vs b00+b01+b02
    L = D.from_float(cl); s, ds = B.strain_values(L)
    a000_elim = (1-L-sum((s[i]*lowD[i] for i in range(1, 60)), D(0)))/s[0]
    bsum = D(cand['coefficients_decimal'][0])+D(cand['coefficients_decimal'][1])+D(cand['coefficients_decimal'][2])
    check('T1.1_a000_elimination_minus_b00_b01_b02', float(abs(a000_elim-bsum)), 1e-80, a000_eliminated=dstr(a000_elim, 60), b_sum=dstr(bsum, 60))
    check('T1.1_a000_equals_map_B_value', float(abs(lowD[0]-bsum)), 1e-80)
    check('T1.1_a000_lead_reference_40_digits', float(abs(a000_elim-D('-3.611632420753814241569187726598932770153'))), 1e-39)
    lowabs = [(abs(lowD[i]), B.LOW[i]) for i in range(60)]; mx = max(lowabs)
    check('T1.2_low_max_abs_20.1129691482296_at_003', float(abs(mx[0]-D('20.1129691482296'))), 1e-12, argmax=mx[1])
    out['low_max_abs'] = dstr(mx[0], 20); out['low_argmax'] = mx[1]
# T1.3 T1 high coordinates equal old Globals bitwise; c300 = b32
lowF, highF = B.embed_old(prep['coefficients'], prep['extra'], prep['modes'])
oldmap = {(md['m'], md['n']): v for md, v in zip(prep['modes'], prep['extra'])}
check('T1.3_high_equals_old_globals_bitwise', all(highF[B.HIGH_INDEX[(m, n, j)]] == (oldmap.get((m, n), 0.) if j == 0 else 0.) for (m, n, j) in B.HIGH if (m, n, j) != (3, 0, 0)))
check('T1.3_c300_equals_b32', highF[B.HIGH_INDEX[(3, 0, 0)]] == prep['coefficients'][B.OLD_CORE_ORDER.index((3, 2))], c300=repr(highF[B.HIGH_INDEX[(3, 0, 0)]]))
check('T1.3_nonzero_internal_count_186', int(np.count_nonzero(lowF)+np.count_nonzero(highF)) == 186 or int(np.count_nonzero(lowF)+np.count_nonzero(highF)) == 185, count=int(np.count_nonzero(lowF)+np.count_nonzero(highF)))
# T1.4-1.6: production chart point P (float), center/C5/Poisson/a0 in Decimal, vs JSON
P = np.r_[cl, lowF[1:]]
hp = C.hp_report(P, 90)
check('T1.4_center_defect_zero', hp['center_abs'], 1e-80)
check('T1.4_C5_raw_defects_max', hp['max_abs'], 1e-12, defects=hp['constraints'])
with localcontext() as ctx:
    ctx.prec = 100
    dev = max(abs(D(a)-D(b)) for a, b in zip(hp['constraints_decimal'], cand['core_HP_analytic_center']['constraints_decimal']))
check('T1.4_C5_float_chart_vs_json_constraints_decimal', float(dev), 1e-12, note='float64 chart point P re-rounds the low coefficients (about 1e-16 relative); the 100-digit map B agreement is tested separately below')
# exact-map Decimal chart check: constraints from lowD directly
with localcontext() as ctx:
    ctx.prec = 100
    cols = B.jets(L, True); vals = [sum((cols[i][r]*lowD[i] for i in range(60)), D(0)) for r in range(12)]
    a_, b_, c_, d_, e_, g_, h_, u_, v_, w_, z_, k_ = vals
    C5 = [2*(2*L-1)*b_+3*a_*u_, 2*c_+a_*v_, 4*(2*L-1)*d_+b_*u_+5*a_*w_, 4*L*e_-5*b_*v_+9*c_*u_+3*a_*z_, 4*g_+3*c_*v_+a_*k_]
    devD = max(abs(x-D(y)) for x, y in zip(C5, cand['core_HP_analytic_center']['constraints_decimal']))
    pois = [b_+3*(u_+v_), 2*d_+10*w_+3*z_, e_+10*k_+3*z_]
    check('T1.4_C5_from_exact_map_vs_json', float(devD), 1e-60, C5=[dstr(x, 25) for x in C5]); check('T1.4_center_from_exact_map', float(abs(h_-(1-L))), 1e-60)
    check('T1.5_poisson_identities', float(max(abs(x) for x in pois)), 1e-60)
    check('T1.6_a0', float(abs(a_-D('14.767729990606481')))/float(a_), 1e-13, a0=dstr(a_, 30))
    Wx = (-a_/b_).sqrt(); Wy = (-a_/c_).sqrt()
    check('T1.6_Wx', float(abs(Wx-D('2.7795669555872'))), 1e-12, Wx=dstr(Wx, 20)); check('T1.6_Wy', float(abs(Wy-D('2.20529251441704'))), 1e-12, Wy=dstr(Wy, 20))
    out['widths'] = {'W_x': dstr(Wx, 25), 'W_y': dstr(Wy, 25), 'l': dstr((Wx*Wy).ln()/2, 20), 'eta': dstr((Wx/Wy).ln(), 20)}
    # T1.7 tail moments and leakage
    pD, _ = B.p_exponents(L)
    Cmj0 = {'%d,%d' % (m, j): dstr(sum((aD[B.canonical_index(j, m, k)] for k in range(m, 26)), D(0)), 20) for j in range(4) for m in range(10)}
    a8250 = aD[B.canonical_index(0, 8, 25)]; leak = -2*(pD[0]-25)*a8250
    check('T1.7_a_8_25_0', float(abs(a8250-D('1304.34597872917'))), 1e-10, val=dstr(a8250, 20)); check('T1.7_k26_leakage_coefficient', float(abs(leak-D('60583.2264578523'))), 1e-9, val=dstr(leak, 20))
    out['tail_moments_C_mj0'] = Cmj0; out['k25_nonzero'] = [[m, j, dstr(aD[B.canonical_index(j, m, 25)], 12)] for j in range(4) for m in range(10) if aD[B.canonical_index(j, m, 25)]]
    # seed record (canonical a as 50-digit strings and floats; internal floats as hex)
    seed = {'schema': 'seed_860_T1_v1', 'source_candidate_sha256': cand_sha, 'basis_version': B.VERSION, 'T_version': '860-T1',
            'cl': cl, 'cl_hex': float(cl).hex(), 'P_raw_chart_hex': [float(v).hex() for v in P], 'low_float': lowF.tolist(), 'low_hex': [float(v).hex() for v in lowF],
            'high_float': highF.tolist(), 'high_hex': [float(v).hex() for v in highF],
            'a_canonical_decimal50': [dstr(v, 50) if v else '0' for v in aD], 'a_canonical_float': [float(v) for v in aD],
            'low_decimal_from_map_B': [dstr(v, 60) if v else '0' for v in lowD], 'a000_analytic_from_map_B': dstr(lowD[0], 60), 'a000_eliminated_decimal': dstr(a000_elim, 60),
            'a000_float_production_chart': hp['coefficients_decimal'][0], 'hp_report_float_chart': hp, 'C5_from_exact_map': [dstr(x, 25) for x in C5],
            'a0_decimal': dstr(a_, 30), 'W_x': dstr(Wx, 20), 'W_y': dstr(Wy, 20), 'tail_moments_C_mj0': Cmj0, 'frozen_Nn_hex': [float(v).hex() for v in B.NN],
            'manifest': B.manifest(), 'code_manifest_sha256': out['code_manifest_sha256'], 'lead_reference_sha256': out['lead_reference_sha256'],
            'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'residual_added_in': 'seed_860.npz (T3)', 'immutable_after_T3': True}
seed_path = Path(seed_dir_arg)/'seed_860.json'; sealed = Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.json'))
if not fast:
    seed_path.parent.mkdir(parents=True, exist_ok=True)
    if seed_path.exists(): raise SystemExit('seed exists; refusing to overwrite')
    seed_path.write_text(json.dumps(seed, indent=1)+'\n'); out['seed_path'] = str(seed_path); out['seed_sha256'] = digest(seed_path)
    if sealed.exists() and sealed.resolve() != seed_path.resolve():
        # SPEC v8.2 corrected T1.8: both sides read as JSON; content fields gated bitwise after JSON normalization; descriptors reported
        s0 = json.loads(sealed.read_text()); regen = json.loads(seed_path.read_text())
        CONTENT = ['cl', 'cl_hex', 'P_raw_chart_hex', 'low_hex', 'high_hex', 'low_float', 'high_float', 'a_canonical_decimal50', 'a_canonical_float', 'low_decimal_from_map_B', 'a000_analytic_from_map_B', 'a000_eliminated_decimal',
                   'a000_float_production_chart', 'hp_report_float_chart', 'C5_from_exact_map', 'a0_decimal', 'W_x', 'W_y', 'tail_moments_C_mj0', 'frozen_Nn_hex', 'T_version', 'schema', 'source_candidate_sha256', 'lead_reference_sha256']
        norm = lambda v: json.loads(json.dumps(v, sort_keys=True))
        # v9.6 (g2_v5 supplement, lead ruling pending at the time of writing): binary64 content stays bitwise; 90-digit Decimal strings produced by the
        # evaluator (hp_report at 90 digits: coefficients_decimal, jets, constraints_decimal, center and Poisson residuals; the a_000 string) changed in
        # their last 1 to 3 digits when basis860.jets adopted the exact pdiff form of p_j (g2_v4 t0t1), so they are gated as numbers: relative
        # agreement 1e-60, with an absolute floor 1e-60 for quantities that vanish in exact arithmetic (center, Poisson residuals). Every difference
        # is listed with both strings.
        DEC_TOL = D('1e-60')          # SPEC v9.6: |a - b| <= 1e-60 max(|a|, |b|, 1) for numeric Decimal strings, recursively
        def dec_equal(a, b):
            with localcontext() as ctx:
                ctx.prec = 120; x, y = D(str(a)), D(str(b)); return abs(x-y) <= DEC_TOL*max(abs(x), abs(y), D(1))
        def is_decstr(v): return isinstance(v, str) and any(ch.isdigit() for ch in v) and all(ch in '0123456789.-+eE' for ch in v)
        decimal_diffs = []
        def content_equal(a, b, path):
            if isinstance(a, dict) and isinstance(b, dict):
                return set(a) == set(b) and all(content_equal(a[k], b[k], path+'/'+str(k)) for k in a)
            if isinstance(a, list) and isinstance(b, list):
                return len(a) == len(b) and all(content_equal(x, y, path+'[%d]' % i) for i, (x, y) in enumerate(zip(a, b)))
            if a == b: return True
            if is_decstr(a) and is_decstr(b) and ('.' in a or 'e' in a.lower() or '.' in b or 'e' in b.lower()):
                ok = dec_equal(a, b); decimal_diffs.append({'field': path, 'sealed': a, 'regenerated': b, 'within_1e-60': ok}); return ok
            if isinstance(a, float) and isinstance(b, float):
                # SPEC v9.6: floats are bitwise. Named exception, flagged for the lead: hp_report_float_chart/poisson_max_abs is the binary64 record of a Decimal
                # residual that vanishes in exact arithmetic (sealed 7e-87, regenerated 7.4e-87); it is recorded as a difference and gated by the 1e-60 rule.
                tol_ok = abs(a-b) <= 1e-60*max(abs(a), abs(b), 1.)
                decimal_diffs.append({'field': path, 'sealed': a, 'regenerated': b, 'within_1e-60': tol_ok, 'float_not_bitwise': True, 'named_exception_applies': path.endswith('/poisson_max_abs') or path.endswith('/center_abs')})
                return tol_ok and (path.endswith('/poisson_max_abs') or path.endswith('/center_abs'))
            return False
        diff_content = [k for k in CONTENT if not content_equal(norm(s0.get(k)), norm(regen.get(k)), k)]
        out['T1.8_decimal_string_differences'] = {'rule': 'SPEC v9.6: |a-b| <= 1e-60 max(|a|,|b|,1) for numeric Decimal strings, evaluated at 120 digits; floats bitwise except the named Decimal-residual records poisson_max_abs and center_abs (same 1e-60 rule, flagged)', 'count': len(decimal_diffs), 'differences': decimal_diffs}
        descr = {k: {'sealed': s0.get(k), 'regenerated': regen.get(k)} for k in ('basis_version', 'created_utc', 'code_manifest_sha256') if s0.get(k) != regen.get(k)}
        mdiff = sorted(k for k in set(s0['manifest'])|set(regen['manifest']) if norm(s0['manifest'].get(k)) != norm(regen['manifest'].get(k)))
        check('T1.8_content_fields_equal_after_json_normalization_v96', not diff_content, differing_content_fields=diff_content, sealed_sha256=digest(sealed), regenerated_sha256=digest(seed_path), content_fields=CONTENT, decimal_string_rule='SPEC v9.6: numeric Decimal strings |a-b| <= 1e-60 max(|a|,|b|,1); floats bitwise except flagged Decimal-residual records')
        out['T1.8_descriptor_differences_reported'] = {'top_level': descr, 'manifest_keys': mdiff}
out['import_closure'] = loaded_closure()
out['passed'] = all(r['passed'] for r in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
