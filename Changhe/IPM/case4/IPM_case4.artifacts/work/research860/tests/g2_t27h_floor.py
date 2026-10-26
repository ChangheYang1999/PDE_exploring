"""G2 supplement T2.7H floor sidecars (lead 08:30Z, new file): the same evaluation and gates as g2_t27h.py at exactly c_l = 2.0, 3.0 and 10.0 (the values whose
floor_cases_count exceeded 300 in g2_v4 t27h: 416, 562, 1323), with COMPLETE floor-case sidecars (sha256 and row count recorded in the step JSON, as in g2_t27hx2).
Original description: G2 test T2.7H (SPEC v9.1 / v9.2): all 860 generators, every field (f, f_x, f_y, psi, psi_x, psi_y, psi_x/y) and its cl derivative at fixed
raw coefficients, at c_l = 1.02, 2, 3, 10 and 2(1 -+ 2^-20), 3(1 -+ 2^-20), at one generic-angle point per band (seven bands) plus
r = 0.0199 and 0.0201 on both sides of the origin-series radius, production provider (basis860.generator_block rounded once for r > 0.02;
the order-48 Decimal series route for r <= 0.02) against the lane's >= 85-digit evaluator, |difference| <= 1e-11 max(band_max, 1e-30), gated.
Usage: g2_t27h_floor.py <out.json> <manifest> [workers]"""
import json, math, sys, time, hashlib
from decimal import Decimal, localcontext
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import basis860 as B, hp860 as H
from points860 import t27h_points, T27H_BANDS, T27H_CL
from model860 import production_generator_matrices
from origin860 import generator_polynomial, ORIGIN_ORDER
from highprecision_origin import _fields, evaluate_series
from absolute_common import digest
from closure860 import loaded_closure
out_path = Path(sys.argv[1]); manifest_path = Path(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 3 else 8
out = {'schema': 'g2_t27h_floor_v2_spec_v93', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))
    ok = bool(value <= tol) if tol is not None else bool(value)
    rec = {'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}
    if tol is not None and 'floor' not in extra: rec['floor'] = 'ratio to max(band_max, 1e-30): absolute 1e-41 where band_max < 1e-30 (cases listed)'
    out['checks'].append(rec); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
D = Decimal; FIELDS7 = B.KEYS; pts = t27h_points(); xs = np.array([p[1] for p in pts]); ys = np.array([p[2] for p in pts]); bands = np.array([p[0] for p in pts]); small = np.hypot(xs, ys) <= .02
T27H_CL = [2.0, 3.0, 10.0]          # the three g2_v4 t27h values with more than 300 floor cases
out['points'] = [{'band': b, 'x': x, 'y': y, 'r': math.hypot(x, y)} for b, x, y in pts]; out['cl_values'] = [{'cl': c, 'cl_hex': float(c).hex()} for c in T27H_CL]
def hp_gen(args):
    col, clv = args; kind, tr = ('low', B.LOW[col]) if col < 60 else ('high', B.HIGH[col-60]); vals = np.empty((len(pts), 7)); dvals = np.empty((len(pts), 7))
    for i, (b, x, y) in enumerate(pts):
        g = H.generator_fields(kind, tr, clv, x, y, 85); dg = H.generator_fields(kind, tr, clv, x, y, 85, cl_derivative=True)
        vals[i] = [float(g[k]) for k in FIELDS7]; dvals[i] = [float(dg[k]) for k in FIELDS7]
    return vals, dvals
import multiprocessing as mp
summary = {}
for clv in T27H_CL:
    t0 = time.time(); pm = production_generator_matrices(clv, xs[~small], ys[~small], True, False)
    prod = {k: np.empty((len(pts), 860)) for k in FIELDS7}; dprod = {k: np.empty((len(pts), 860)) for k in FIELDS7}
    for k in FIELDS7: prod[k][~small] = pm[k]; dprod[k][~small] = pm['d_'+k]
    with localcontext() as cx:
        cx.prec = 90; L = D.from_float(clv)
        for col in range(860):
            kind, tr = ('low', B.LOW[col]) if col < 60 else ('high', B.HIGH[col-60]); chi, dchi = generator_polynomial(kind, tr, L, ORIGIN_ORDER+4); ff = _fields(chi, ORIGIN_ORDER); dff = _fields(dchi, ORIGIN_ORDER)
            for k in FIELDS7: prod[k][small, col] = evaluate_series(ff[k], xs[small], ys[small]); dprod[k][small, col] = evaluate_series(dff[k], xs[small], ys[small])
    with mp.get_context('fork').Pool(workers) as pool: res = pool.map(hp_gen, [(col, clv) for col in range(860)])
    hp = {k: np.empty((len(pts), 860)) for k in FIELDS7}; dhp = {k: np.empty((len(pts), 860)) for k in FIELDS7}
    for col, (v, dv) in enumerate(res):
        for ik, k in enumerate(FIELDS7): hp[k][:, col] = v[:, ik]; dhp[k][:, col] = dv[:, ik]
    worst = 0.; worst_d = 0.; wloc = None; wdloc = None; floor_cases = []; per_gen = np.zeros(860); per_gen_d = np.zeros(860)
    for k in FIELDS7:
        for b in range(len(T27H_BANDS)):
            sel = bands == b
            bmax = np.max(abs(hp[k][sel]), axis=0); ratio = np.max(abs(prod[k][sel]-hp[k][sel]), axis=0)/np.maximum(bmax, 1e-30)
            dbmax = np.max(abs(dhp[k][sel]), axis=0); dratio = np.max(abs(dprod[k][sel]-dhp[k][sel]), axis=0)/np.maximum(dbmax, 1e-30)
            for g_ in np.flatnonzero(bmax < 1e-30): floor_cases.append([int(g_), k, b, float(bmax[g_])])
            for g_ in np.flatnonzero(dbmax < 1e-30): floor_cases.append([int(g_), 'dcl_'+k, b, float(dbmax[g_])])
            per_gen = np.maximum(per_gen, ratio); per_gen_d = np.maximum(per_gen_d, dratio)
            if ratio.max() > worst: worst = float(ratio.max()); wloc = {'field': k, 'band': b, 'generator': int(np.argmax(ratio)), 'triple': list(B.LOW[int(np.argmax(ratio))]) if np.argmax(ratio) < 60 else list(B.HIGH[int(np.argmax(ratio))-60])}
            if dratio.max() > worst_d: worst_d = float(dratio.max()); wdloc = {'field': 'dcl_'+k, 'band': b, 'generator': int(np.argmax(dratio)), 'triple': list(B.LOW[int(np.argmax(dratio))]) if np.argmax(dratio) < 60 else list(B.HIGH[int(np.argmax(dratio))-60])}
    label = 'cl=%r' % clv
    side = out_path.with_name(out_path.stem+'.floor_cases_cl_%s.json' % float(clv).hex().replace('0x', '').replace('.', '_').replace('+', 'p').replace('-', 'm'))
    side.write_text(json.dumps({'cl': clv, 'cl_hex': float(clv).hex(), 'columns': ['generator', 'field_or_dcl_field', 'band', 'band_max'], 'rows': floor_cases}, indent=0)+'\n')
    summary[label] = {'cl_hex': float(clv).hex(), 'worst_field_ratio': worst, 'worst_field_at': wloc, 'worst_dcl_ratio': worst_d, 'worst_dcl_at': wdloc, 'floor_cases_count': len(floor_cases), 'floor_cases_first_300': floor_cases[:300],
                      'floor_cases_complete_sidecar': str(side), 'floor_cases_complete_sidecar_sha256': hashlib.sha256(side.read_bytes()).hexdigest(), 'floor_cases_complete_sidecar_rows': len(floor_cases),
                      'per_generator_worst_ratio': per_gen.tolist(), 'per_generator_worst_dcl_ratio': per_gen_d.tolist(), 'seconds': time.time()-t0}
    check('T2.7Hfloor_all860_fields_%s' % label, worst, 1e-11, at=wloc, floor_sidecar=str(side), floor_sidecar_rows=len(floor_cases)); check('T2.7Hfloor_all860_dcl_%s' % label, worst_d, 1e-11, at=wdloc)
    if clv in (2.0, 3.0):      # SPEC v9.3 structural zeros: the three zero-field low generators of the integer branch; fields exactly 0.0 expected, gated at 1e-41; cl derivatives gated above
        jz = 3 if clv == 2.0 else 2; zero_gens = [B.LOW_INDEX[(0, 0, jz)], B.LOW_INDEX[(0, 1, jz)], B.LOW_INDEX[(1, 1, jz)]]
        zrows = [{'generator': int(g_), 'triple': list(B.LOW[g_]), 'field': k, 'point': int(i_), 'production': float(prod[k][i_, g_]), 'reference': float(hp[k][i_, g_])} for g_ in zero_gens for k in FIELDS7 for i_ in range(len(pts))]
        nonzero = [z for z in zrows if z['production'] != 0.0]; worst_zero = max(abs(z['production']) for z in zrows)
        check('T2.7Hfloor_structural_zeros_fields_%s' % label, worst_zero, 1e-41, floor='absolute 1e-41 (band_max is 0)', generators=[list(B.LOW[g_]) for g_ in zero_gens], nonzero_production_values=nonzero[:100], nonzero_count=len(nonzero), reference_max_abs=max(abs(z['reference']) for z in zrows))
        dz = max(float(np.max(abs(dprod[k][:, g_]-dhp[k][:, g_]))/max(np.max(abs(dhp[k][:, g_])), 1e-30)) for g_ in zero_gens for k in FIELDS7)
        check('T2.7Hfloor_structural_zero_generators_dcl_nonzero_and_accurate_%s' % label, dz, 1e-11, dcl_reference_max=[float(np.max(abs(dhp[k][:, g_]))) for g_ in zero_gens for k in FIELDS7][:21])
        summary[label]['structural_zero_rows'] = zrows
out['T2.7H_floor'] = summary; out['import_closure'] = loaded_closure()
out['passed'] = all(c['passed'] for c in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
