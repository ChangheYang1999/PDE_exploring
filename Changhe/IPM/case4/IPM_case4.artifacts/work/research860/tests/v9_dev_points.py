"""SPEC v9/v9.1/v9.2 development check (unfrozen, not a gate record): R_f and all 860 columns of the seed at the 26 g2_v3 points and R_f at the
verifier's 23 diagnostic points for the three provider shapes against the Decimal reference (hp860.point_reference); rho = |diff|/(u S_R) with
u = 2^-64; T2.7H (all 860 generators, fields and cl derivatives) at c_l = 2 and 3.  Usage: v9_dev_points.py <out.json> [procs]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, sys, time, os
from decimal import Decimal, localcontext
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import basis860 as B, hp860 as H
from points860 import FAR, FINITE_V92, VERIFIER_23, GATED_FAR, t27h_points, T27H_BANDS, band_of
from shapes860 import production_single, production_batch, stateless, share_prepared
from model860 import production_generator_matrices
from origin860 import generator_polynomial, ORIGIN_ORDER
from highprecision_origin import _fields, evaluate_series
from closure860 import loaded_closure
out_path = Path(sys.argv[1]); procs = int(sys.argv[2]) if len(sys.argv) > 2 else 8
D = Decimal; LD = B.LD; U = 2.**-64
out = {'schema': 'v9_dev_points_v1', 'basis_version': B.VERSION, 'switch_radius': B.R_SWITCH, 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'unit_roundoff_for_rho': U}
seed = json.loads(Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.json')).read_text())
P = np.array([float.fromhex(h) for h in seed['P_raw_chart_hex']]); high = np.array([float.fromhex(h) for h in seed['high_hex']]); cl = float(P[0])
prep = share_prepared(B.prepare(cl, P[1:], high), P, high)

def condition_sum(x, y):
    """S_R: R_f assembled with every field replaced by its absolute condition sum over the generators (longdouble block, same split)."""
    blk = B.generator_block(cl, [x], [y], False, True); ac = abs(prep['coeff_ld']); r = math.hypot(x, y)
    S = {k: float(abs(blk[k][0])@ac) for k in ('f', 'fx', 'fy', 'psix', 'psiy', 'ratio')}
    Sq = float(abs(blk['qcore'][0])@abs(prep['c_ld'])+abs(blk['ratio'][0, 60:])@abs(np.asarray(high, LD)))
    if r >= B.R_SWITCH:
        SL = float((abs(cl-1)*B.JCOL_LD*abs(blk['f'][0])+2*cl*abs(blk['frem'][0]))@ac)
        return SL+S['psiy']*S['fx']+S['psix']*S['fy']+S['ratio']*S['f']
    return (abs(cl*x)+S['psiy'])*S['fx']+(abs(cl*y)+S['psix'])*S['fy']+Sq*S['f']

def hp_ref(args):
    band, x, y, columns = args; ref = H.point_reference(prep, x, y, 85, columns)
    return {'band': band, 'x': x, 'y': y, 'Rf': ref['Rf'], 'Rf_decimal': str(ref['Rf_decimal']), 'columns': ref['columns'].tolist() if columns else None}

import multiprocessing as mp
ctx = mp.get_context('fork')
def band_table(rows, label, columns=True):
    """rows: list of dicts with band, Rf_ref, Rf_<shape>, cols_ref, cols_<shape>."""
    res = {}
    for band in sorted({r_['band'] for r_ in rows}):
        sub = [r_ for r_ in rows if r_['band'] == band]; rfmax = max(max(abs(r_['Rf_ref']) for r_ in sub), 1e-30); entry = {'Rf_band_max': rfmax, 'points': len(sub), 'gated': band not in ('e32', 'e44')}
        for shape in ('single', 'batch', 'stateless'):
            errs = [abs(r_['Rf_'+shape]-r_['Rf_ref']) for r_ in sub]; i = int(np.argmax(errs))
            entry['Rf_'+shape] = {'ratio': errs[i]/rfmax, 'abs': errs[i], 'at': [sub[i]['x'], sub[i]['y']], 'rho': errs[i]/(U*sub[i]['S_R']) if sub[i].get('S_R') else None, 'passed_1e-11': bool(errs[i] <= 1e-11*rfmax)}
            if columns:
                cref = np.array([r_['cols_ref'] for r_ in sub]); cmax = np.maximum(np.max(abs(cref), axis=0), 1e-30)
                cerr = np.max(abs(np.array([r_['cols_'+shape] for r_ in sub])-cref), axis=0); ratio = cerr/cmax
                entry['columns_'+shape] = {'worst_ratio': float(ratio.max()), 'worst_index': int(np.argmax(ratio)), 'failing': int(np.count_nonzero(ratio > 1e-11)), 'floor_cases': int(np.count_nonzero(cmax <= 1e-30))}
        entry['Rf_largest_shape_difference'] = max(abs(r_['Rf_'+a]-r_['Rf_'+b]) for r_ in sub for a in ('single', 'batch', 'stateless') for b in ('single', 'batch', 'stateless'))
        if columns: entry['columns_largest_shape_difference'] = max(float(np.max(abs(np.array(r_['cols_'+a])-np.array(r_['cols_'+b])))) for r_ in sub for a in ('single', 'batch', 'stateless') for b in ('single', 'batch', 'stateless'))
        res[band] = entry
    out[label] = res
    worst = max(v['Rf_'+s]['ratio'] for v in res.values() if v['gated'] for s in ('single', 'batch', 'stateless'))
    print(label, 'worst gated R_f ratio', worst, flush=True)
    for band, v in res.items(): print('  ', band, 'Rf', {s: '%.3e' % v['Rf_'+s]['ratio'] for s in ('single', 'batch', 'stateless')}, 'cols', {s: '%.3e' % v['columns_'+s]['worst_ratio'] for s in ('single', 'batch', 'stateless')} if columns else '', 'shape diff %.2e' % v['Rf_largest_shape_difference'], flush=True)
    return res

def run_set(points, label, columns):
    t0 = time.time(); xs = np.array([p[1] for p in points]); ys = np.array([p[2] for p in points])
    with ctx.Pool(procs) as pool: refs = pool.map(hp_ref, [(b, x, y, columns) for (b, x, y) in points])
    t_ref = time.time()-t0; t0 = time.time()
    rf_b, dr_b = production_batch(P, high, xs, ys, columns); rf_s, dr_s = stateless(prep, xs, ys, columns)
    rows = []
    for i, (b, x, y) in enumerate(points):
        rf1, dr1 = production_single(P, high, x, y, columns)
        row = {'band': b, 'x': x, 'y': y, 'r': math.hypot(x, y), 'Rf_ref': refs[i]['Rf'], 'Rf_single': rf1, 'Rf_batch': float(rf_b[i]), 'Rf_stateless': float(rf_s[i]), 'S_R': condition_sum(x, y)}
        if columns: row.update(cols_ref=refs[i]['columns'], cols_single=dr1.tolist(), cols_batch=dr_b[i].tolist(), cols_stateless=dr_s[i].tolist())
        rows.append(row)
    out[label+'_seconds'] = {'reference': t_ref, 'providers': time.time()-t0}
    table = band_table(rows, label, columns)
    out[label+'_points'] = [{k: v for k, v in r_.items() if not k.startswith('cols_')} for r_ in rows]
    return rows, table

rows26, t26 = run_set(FAR+FINITE_V92, 'g2v3_points_plus_v92', True)
rows23, t23 = run_set(VERIFIER_23, 'verifier_23_points', False)
# ---------------- T2.7H at cl = 2, 3: all 860 generators, every field and cl derivative, T2.7 rule
FIELDS7 = B.KEYS; pts = t27h_points(); xs = np.array([p[1] for p in pts]); ys = np.array([p[2] for p in pts]); bands = np.array([p[0] for p in pts]); small = np.hypot(xs, ys) <= .02
def hp_gen(args):
    col, clv = args; kind, tr = ('low', B.LOW[col]) if col < 60 else ('high', B.HIGH[col-60]); vals = np.empty((len(pts), 7)); dvals = np.empty((len(pts), 7))
    for i, (b, x, y) in enumerate(pts):
        g = H.generator_fields(kind, tr, clv, x, y, 85); dg = H.generator_fields(kind, tr, clv, x, y, 85, cl_derivative=True)
        vals[i] = [float(g[k]) for k in FIELDS7]; dvals[i] = [float(dg[k]) for k in FIELDS7]
    return vals, dvals
summary = {}
for clv in (2.0, 3.0):
    t0 = time.time(); pm = production_generator_matrices(clv, xs[~small], ys[~small], True, False)
    prod = {k: np.empty((len(pts), 860)) for k in FIELDS7}; dprod = {k: np.empty((len(pts), 860)) for k in FIELDS7}
    for k in FIELDS7: prod[k][~small] = pm[k]; dprod[k][~small] = pm['d_'+k]
    with localcontext() as cx:
        cx.prec = 90; L = D.from_float(clv)
        for col in range(860):
            kind, tr = ('low', B.LOW[col]) if col < 60 else ('high', B.HIGH[col-60]); chi, dchi = generator_polynomial(kind, tr, L, ORIGIN_ORDER+4); ff = _fields(chi, ORIGIN_ORDER); dff = _fields(dchi, ORIGIN_ORDER)
            for k in FIELDS7: prod[k][small, col] = evaluate_series(ff[k], xs[small], ys[small]); dprod[k][small, col] = evaluate_series(dff[k], xs[small], ys[small])
    with ctx.Pool(procs) as pool: res = pool.map(hp_gen, [(col, clv) for col in range(860)])
    hp = {k: np.empty((len(pts), 860)) for k in FIELDS7}; dhp = {k: np.empty((len(pts), 860)) for k in FIELDS7}
    for col, (v, dv) in enumerate(res):
        for ik, k in enumerate(FIELDS7): hp[k][:, col] = v[:, ik]; dhp[k][:, col] = dv[:, ik]
    worst = 0.; worst_d = 0.; wloc = None; wdloc = None; floor_cases = 0
    for k in FIELDS7:
        for b in range(len(T27H_BANDS)):
            sel = bands == b
            bmax = np.max(abs(hp[k][sel]), axis=0); ratio = np.max(abs(prod[k][sel]-hp[k][sel]), axis=0)/np.maximum(bmax, 1e-30)
            dbmax = np.max(abs(dhp[k][sel]), axis=0); dratio = np.max(abs(dprod[k][sel]-dhp[k][sel]), axis=0)/np.maximum(dbmax, 1e-30)
            floor_cases += int(np.count_nonzero(bmax < 1e-30))+int(np.count_nonzero(dbmax < 1e-30))
            if ratio.max() > worst: worst = float(ratio.max()); wloc = [k, b, int(np.argmax(ratio))]
            if dratio.max() > worst_d: worst_d = float(dratio.max()); wdloc = ['dcl_'+k, b, int(np.argmax(dratio))]
    summary['cl=%g' % clv] = {'worst_field_ratio': worst, 'worst_field_at': wloc, 'worst_dcl_ratio': worst_d, 'worst_dcl_at': wdloc, 'floor_cases': floor_cases, 'seconds': time.time()-t0, 'passed_1e-11': bool(worst <= 1e-11 and worst_d <= 1e-11)}
    print('T2.7H cl=%g' % clv, summary['cl=%g' % clv], flush=True)
out['T2.7H_dev'] = summary; out['import_closure'] = loaded_closure(); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('DONE', flush=True)
