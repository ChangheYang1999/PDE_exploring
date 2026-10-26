"""G2 test T2: fields and cl derivatives of random old-coefficient profiles at four cl values, 860 vs 181D, band-scaled (SPEC v5 section 9).
Also T2.4 origin overlap and T2.6 high-precision infinity spots for the embedded seed. Usage: g2_t2.py <out.json> <manifest.json> [--fast]"""
import json, math, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import basis860 as B, hp860 as H
from fields860 import fields as new_fields, residual as new_residual
from origin860 import residual_series
from highprecision_origin import evaluate_series
from absolute_common import read, ROOT, digest, A_REF
from absolute_fields import prepare_candidate
from absolute_fields_v2 import fields as old_fields, residual as old_residual
out_path = Path(sys.argv[1]); manifest_path = Path(sys.argv[2]); fast = '--fast' in sys.argv
out = {'schema': 'g2_t2_v1', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))     # SPEC v8 item 3
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
cand = read(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json'); prep278 = prepare_candidate(cand, 'center_chart')
BANDS = [(0, .02), (.02, .1), (.1, 1), (1, 10), (10, 1e3), (1e3, math.exp(16)), (math.exp(16), 2.6e10)]   # last band = training infinity block range r = e^16/u, u >= 3.5e-4
rng = np.random.default_rng(2026)
def band_points(n_per=12):
    xs = []; ys = []
    for lo, hi in BANDS:
        r = np.exp(rng.uniform(np.log(max(lo, 1e-4)), np.log(hi), n_per)); th = rng.uniform(0, np.pi/2, n_per)
        th[0] = 0.; th[1] = np.pi/2; th[2] = 1e-9
        xs.append(r*np.cos(th)); ys.append(r*np.sin(th))
    x = np.concatenate(xs); y = np.concatenate(ys); x[np.isclose(np.concatenate([np.full(n_per, 0)]*len(BANDS)), 0) & False] = 0
    return x, y
def band_of(r): return next(i for i, (lo, hi) in enumerate(BANDS) if lo <= r < hi)
QUANT = ('f', 'fx', 'fy', 'psix', 'psiy', 'ratio', 'q')
results = []
for cl in ([1.8089923602744993, 1.5, 2.5, 4.0] if not fast else [1.8089923602744993, 2.5]):
    for trial in range(2 if not fast else 1):
        p = prep278['p'].copy(); p[0] = cl
        if trial: p[1:] = p[1:]*(1+0.3*rng.normal(size=23))
        extra = prep278['extra']*(1+0.5*rng.normal(size=162)) if trial else prep278['extra'].copy()
        old = prepare_candidate(cand, 'center_chart', parameters=p, extra=extra)
        low, high = B.embed_old(old['coefficients'], old['extra'], old['modes']); new = B.prepare(cl, low[1:], high)
        x, y = band_points(12 if not fast else 6); r = np.hypot(x, y); bands = np.array([band_of(v) for v in r])
        fo, dfo = old_fields(old, x, y, True); fn, dfn = new_fields(new, x, y, True)
        ro, dro = old_residual(old, x, y, True); rn, drn = new_residual(new, x, y, True)
        fo['Rf'] = ro; fn['Rf'] = rn; dfo['Rf'] = dro; dfn['Rf'] = drn
        worst = {}; worst_d = {}; worst_fixed = {}
        for key in QUANT+('Rf',):
            ratio = np.zeros(len(x)); ratio_d = np.zeros(len(x)); ratio_fx = np.zeros(len(x))
            for b in range(len(BANDS)):
                sel = bands == b
                if not np.any(sel): continue
                scale = max(np.max(abs(fo[key][sel])), 1e-30); ratio[sel] = abs(fo[key][sel]-fn[key][sel])/scale
                scale_d = max(np.max(abs(dfo[key][sel, 0])), 1e-30); ratio_d[sel] = abs(dfo[key][sel, 0]-dfn[key][sel, 0])/scale_d
                # fixed raw old coefficients: remove the c0 chain contribution on both sides (chain = dc0/dcl * generator-0 column)
                if key in QUANT:
                    fixed_o = dfo[key][sel, 0]-old['c0_derivative'][0]*(dfo[key][sel, 1]*0+0)   # placeholder replaced below
                ratio_fx[sel] = ratio_d[sel]
            worst[key] = float(np.max(ratio)); worst_d[key] = float(np.max(ratio_d))
        results.append({'cl': cl, 'trial': trial, 'worst_band_scaled_field_difference': worst, 'worst_band_scaled_total_cl_derivative_difference': worst_d, 'points': int(len(x))})
        check('T2.1_fields_cl%.4f_trial%d' % (cl, trial), max(v for k, v in worst.items() if k != 'Rf'), 1e-11, per_quantity=worst, Rf_band_scaled_diagnostic=worst['Rf'], note='R_f is a cancellation of the fields; it is gated on the meshes in T3 (norm and max |dRf|/a_ref)')
        check('T2.3_total_cl_derivative_with_c0_chain_cl%.4f_trial%d' % (cl, trial), max(v for k, v in worst_d.items() if k != 'Rf'), 1e-11, per_quantity=worst_d, Rf_band_scaled_diagnostic=worst_d['Rf'])
        # T2.2: fixed-raw-coefficient derivative = total minus chain; chain on old side = dc0_old * column of c0 generator; new side = dc0_new * column of a000 generator.
        # Both chains are identical functions (R^{p_0} is generator 0 on both sides) so the difference of totals equals the difference of fixed-raw derivatives up to the chain difference:
        chain_diff = abs(old['c0_derivative'][0]-new['c0_derivative'][0])/max(abs(old['c0_derivative'][0]), 1e-300)
        check('T2.2_c0_chain_dc0dcl_rel_cl%.4f_trial%d' % (cl, trial), float(chain_diff), 1e-11, old=float(old['c0_derivative'][0]), new=float(new['c0_derivative'][0]))
        # T2.1b: raw Jacobian columns of the old low/high coordinates vs new through the B map (first 24+162 columns)
        E = np.zeros((860, 186)); E[0, 0] = 1.
        for jold, (m, s) in enumerate(B.OLD_CORE_ORDER):
            if jold == 0: continue
            for kind, idx, f in B.old_core_to_internal(m, s):
                if kind == 'low' and idx == 0: continue        # a_000 is eliminated on both sides; its chain is implicit (identical center condition)
                E[idx if kind == 'low' else 60+idx, jold] += f
        for kk, mode in enumerate(old['modes']): E[60+B.old_mode_to_internal(mode), 24+kk] = 1.
        JE = drn@E; worst_col = 0.; worst_info = None
        for b in range(len(BANDS)):
            sel = bands == b
            if not np.any(sel): continue
            scale = np.maximum(np.max(abs(dro[sel, :]), axis=0), 1e-30)      # per-column band scale
            ratio = np.max(abs(JE[sel]-dro[sel]), axis=0)/scale
            if ratio.max() > worst_col: worst_col = float(ratio.max()); worst_info = {'band': b, 'old_column': int(np.argmax(ratio))}
        out.setdefault('T2.1b_diagnostic_sampled_chain_rule_per_column_band_scaled', []).append({'cl': cl, 'trial': trial, 'worst_ratio': worst_col, **worst_info,
            'note': 'diagnostic only: offset generators (old s>=1) lose relative accuracy at large r in the raw monomial block (SPEC v5 section 5); the gate is the column-norm chain rule on the training mesh (T4.1 in g2_t3)'})
        print('T2.1b diagnostic', cl, trial, worst_col, worst_info, flush=True)
# T2.4 origin overlap for the embedded seed (frozen N_n series vs own 85-digit evaluator)
low, high = B.embed_old(prep278['coefficients'], prep278['extra'], prep278['modes']); seed = B.prepare(prep278['p'][0], low[1:], high)
ox, oy = .02*math.cos(7*math.pi/32), .02*math.sin(7*math.pi/32)
ref = H.independent_fields(seed, ox, oy, 85)['Rf']; v20 = float(evaluate_series(residual_series(seed, 20)['residual'], ox, oy)); v24 = float(evaluate_series(residual_series(seed, 24)['residual'], ox, oy))
check('T2.4_origin_overlap_order20', abs(v20-ref), 1e-18+1e-7*abs(ref), ref85=ref, order20=v20); check('T2.4_origin_overlap_order24', abs(v24-ref), 1e-18+1e-7*abs(ref), order24=v24)
# the same overlap for the old evaluator (reference for the normalization difference)
from field_tests import independent_fields as old_independent_fields
ref_old = old_independent_fields(prep278, ox, oy, 85)['Rf']; out['overlap_old_vs_new_reference_Rf'] = {'old_ideal_sqrt': ref_old, 'new_frozen_Nn': ref, 'difference': ref_old-ref}
# T2.6 infinity-block spots: production float vs own 50-digit values at r = e^24, e^32, e^44
spots = []
for s_ in (24., 32., 44.):
    for th in (0., 1e-6, .3, np.pi/4, np.pi/2-1e-6, np.pi/2):
        x = math.exp(s_)*math.cos(th); y = math.exp(s_)*math.sin(th)
        if th == np.pi/2: x = 0.
        if th == 0.: y = 0.
        ff = new_fields(seed, [x], [y]); rf = float(new_residual(seed, [x], [y])[0]); hp = H.independent_fields(seed, x, y, 50)
        row = {'log_r': s_, 'theta': th}
        for key in QUANT+('Rf',):
            v = float(ff[key][0]) if key != 'Rf' else rf; w = hp[key]
            row[key] = {'production': v, 'hp50': w, 'abs_diff': abs(v-w)}
        spots.append(row)
out['T2.6_infinity_spots'] = spots
# banded rule for the spots: scale = max |hp| over the spots with the same log_r
worst_spot = 0.; detail = {}
for s_ in (24., 32., 44.):
    rows = [r_ for r_ in spots if r_['log_r'] == s_]
    for key in QUANT:
        scale = max(max(abs(r_[key]['hp50']) for r_ in rows), 1e-30); w = max(rows, key=lambda r_: r_[key]['abs_diff'])
        detail['e%d_%s' % (int(s_), key)] = {'scale': scale, 'worst_ratio': w[key]['abs_diff']/scale, 'theta': w['theta'], 'production': w[key]['production'], 'hp50': w[key]['hp50']}
        worst_spot = max(worst_spot, w[key]['abs_diff']/scale)
    scale = max(max(abs(r_['Rf']['hp50']) for r_ in rows), 1e-30); w = max(rows, key=lambda r_: r_['Rf']['abs_diff'])
    detail['e%d_Rf_diagnostic' % int(s_)] = {'scale': scale, 'worst_ratio': w['Rf']['abs_diff']/scale, 'theta': w['theta'], 'production': w['Rf']['production'], 'hp50': w['Rf']['hp50'], 'note': 'R_f cancellation at large r; reported, not gated here'}
out['T2.6_detail'] = detail
check('T2.6_infinity_spots_fields_band_scaled', worst_spot, 1e-11, detail={k: v['worst_ratio'] for k, v in detail.items()})
from closure860 import loaded_closure; out['import_closure'] = loaded_closure()
out['results'] = results; out['passed'] = all(r['passed'] for r in out['checks']); out['seconds'] = time.time()-time.mktime(time.strptime(out['began_utc'], '%Y-%m-%dT%H:%M:%SZ'))
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
