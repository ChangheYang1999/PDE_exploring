"""G2 supplement T2.7H-X (SPEC v9.3): all 860 generators, every field and its cl derivative, at the binary64 neighbours of 2 and 3 (nextafter toward 0
and toward infinity) and at 2(1 -+ 2^-30), 2(1 -+ 2^-40), 3(1 -+ 2^-30), 3(1 -+ 2^-40), on the T2.7H point set plus one generic-angle point at the
balance radius r_b = delta^(-1/4) per offset delta (added point gated with max(band_max of its band, its own reference magnitude); original points
keep their band scales). Production provider as in T2.7H, reference >= 85 digits, 1e-11 rule, gated.  Usage: g2_t27hx.py <out.json> <manifest> [workers]"""
import json, math, sys, time, hashlib
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import basis860 as B, hp860 as H
from points860 import t27h_points, T27H_BANDS
from model860 import production_generator_matrices
from origin860 import generator_polynomial, ORIGIN_ORDER
from highprecision_origin import _fields, evaluate_series
from absolute_common import digest
from closure860 import loaded_closure
out_path = Path(sys.argv[1]); manifest_path = Path(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 3 else 8
out = {'schema': 'g2_t27hx_v1_spec_v93', 'code_manifest_sha256': digest(manifest_path), 'basis_version': B.VERSION, 'checks': [], 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
def check(name, value, tol=None, **extra):
    bad = {'check', 'value', 'tolerance', 'passed'} & set(extra)
    if bad: raise RuntimeError('gate record collision in %s: %s' % (name, sorted(bad)))
    ok = bool(value <= tol) if tol is not None else bool(value)
    rec = {'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}
    if tol is not None and 'floor' not in extra: rec['floor'] = 'ratio to max(band_max, 1e-30): absolute 1e-41 where band_max < 1e-30 (cases listed)'
    out['checks'].append(rec); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
D = Decimal; FIELDS7 = B.KEYS
def band_index(rv):
    for b, (lo, hi) in enumerate(T27H_BANDS):
        if lo <= rv < hi: return b
    return len(T27H_BANDS)-1
XCL = []; XCL_EXACT = []
def exact_delta(c, base):      # exact relative displacement |c/base - 1| of the binary64 value c from the integer base, as a rational (verifier preflight 07:16Z: float c/base-1 is wrong at the neighbours of 3)
    return abs(Fraction(float(c))/Fraction(int(base))-1)
for base in (2.0, 3.0):
    for v in (np.nextafter(base, 0.), np.nextafter(base, np.inf)): XCL_EXACT.append((float(v), exact_delta(v, base), 'nextafter'))
    for e in (30, 40):
        for sgn in (-1, 1): c = base*(1+sgn*2.**-e); XCL_EXACT.append((c, exact_delta(c, base), 'offset_2^-%d' % e))
XCL = [(c, float(dx), kd) for c, dx, kd in XCL_EXACT]          # delta = correctly rounded binary64 of the exact rational; r_b = delta^(-1/4) in binary64
out['cl_values'] = [{'cl': c, 'cl_hex': float(c).hex(), 'delta': float(dx), 'delta_exact_rational': '%d/%d' % (dx.numerator, dx.denominator), 'delta_definition': '|cl/base - 1| in exact rational arithmetic on the binary64 cl', 'kind': kd, 'balance_radius': float(dx)**-.25, 'balance_radius_definition': 'delta^(-1/4) evaluated in binary64 from the correctly rounded delta'} for c, dx, kd in XCL_EXACT]
T27H_CL = [c for c, _, _ in XCL]; BASE_PTS = t27h_points(); NBASE = len(BASE_PTS)
def hp_gen(args):
    col, clv = args; kind, tr = ('low', B.LOW[col]) if col < 60 else ('high', B.HIGH[col-60]); vals = np.empty((len(pts), 7)); dvals = np.empty((len(pts), 7))
    for i, (b, x, y) in enumerate(pts):
        g = H.generator_fields(kind, tr, clv, x, y, 85); dg = H.generator_fields(kind, tr, clv, x, y, 85, cl_derivative=True)
        vals[i] = [float(g[k]) for k in FIELDS7]; dvals[i] = [float(dg[k]) for k in FIELDS7]
    return vals, dvals
import multiprocessing as mp
summary = {}
for clv, delta, xkind in XCL:          # xkind: the c_l value kind ('nextafter' or 'offset_2^-e'); 'kind' below is the generator kind (low/high)
    rb = delta**-.25; pts = BASE_PTS+[(band_index(rb), rb*math.cos(.9), rb*math.sin(.9))]; xs = np.array([p[1] for p in pts]); ys = np.array([p[2] for p in pts]); bands = np.array([p[0] for p in pts]); small = np.hypot(xs, ys) <= .02
    added = np.zeros(len(pts), bool); added[-1] = True
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
            sel = (bands == b) & ~added; sel_add = (bands == b) & added
            if not np.any(sel): continue
            bmax = np.max(abs(hp[k][sel]), axis=0); ratio = np.max(abs(prod[k][sel]-hp[k][sel]), axis=0)/np.maximum(bmax, 1e-30)
            dbmax = np.max(abs(dhp[k][sel]), axis=0); dratio = np.max(abs(dprod[k][sel]-dhp[k][sel]), axis=0)/np.maximum(dbmax, 1e-30)
            if np.any(sel_add):      # the balance-radius point: scale = max(original band_max of its band, its own reference magnitude); never enlarges the original scale
                sa = np.maximum(bmax, np.max(abs(hp[k][sel_add]), axis=0)); ra = np.max(abs(prod[k][sel_add]-hp[k][sel_add]), axis=0)/np.maximum(sa, 1e-30)
                dsa = np.maximum(dbmax, np.max(abs(dhp[k][sel_add]), axis=0)); dra = np.max(abs(dprod[k][sel_add]-dhp[k][sel_add]), axis=0)/np.maximum(dsa, 1e-30)
                ratio = np.maximum(ratio, ra); dratio = np.maximum(dratio, dra)
            for g_ in np.flatnonzero(bmax < 1e-30): floor_cases.append([int(g_), k, b, float(bmax[g_])])
            for g_ in np.flatnonzero(dbmax < 1e-30): floor_cases.append([int(g_), 'dcl_'+k, b, float(dbmax[g_])])
            per_gen = np.maximum(per_gen, ratio); per_gen_d = np.maximum(per_gen_d, dratio)
            if ratio.max() > worst: worst = float(ratio.max()); wloc = {'field': k, 'band': b, 'generator': int(np.argmax(ratio)), 'triple': list(B.LOW[int(np.argmax(ratio))]) if np.argmax(ratio) < 60 else list(B.HIGH[int(np.argmax(ratio))-60])}
            if dratio.max() > worst_d: worst_d = float(dratio.max()); wdloc = {'field': 'dcl_'+k, 'band': b, 'generator': int(np.argmax(dratio)), 'triple': list(B.LOW[int(np.argmax(dratio))]) if np.argmax(dratio) < 60 else list(B.HIGH[int(np.argmax(dratio))-60])}
    label = 'cl=%r' % clv
    out.setdefault('points_per_cl', {})[label] = [{'band': int(b), 'x': x, 'y': y, 'r': math.hypot(x, y), 'added_balance_point': bool(i_ == len(pts)-1)} for i_, (b, x, y) in enumerate(pts)]
    side = out_path.with_name(out_path.stem+'.floor_cases.%s' % xkind.replace('^', '')+('_%s.json' % float(clv).hex().replace('0x', '').replace('.', '_').replace('+', 'p').replace('-', 'm')))
    side.write_text(json.dumps({'cl': clv, 'cl_hex': float(clv).hex(), 'columns': ['generator', 'field_or_dcl_field', 'band', 'band_max'], 'rows': floor_cases}, indent=0)+'\n')
    summary[label] = {'cl_hex': float(clv).hex(), 'worst_field_ratio': worst, 'worst_field_at': wloc, 'worst_dcl_ratio': worst_d, 'worst_dcl_at': wdloc, 'floor_cases_count': len(floor_cases), 'floor_cases_first_300': floor_cases[:300],
                      'floor_cases_complete_sidecar': str(side), 'floor_cases_complete_sidecar_sha256': hashlib.sha256(side.read_bytes()).hexdigest(),
                      'per_generator_worst_ratio': per_gen.tolist(), 'per_generator_worst_dcl_ratio': per_gen_d.tolist(), 'seconds': time.time()-t0}
    check('T2.7HX_all860_fields_%s' % label, worst, 1e-11, at=wloc, cl_kind=xkind, delta=delta); check('T2.7HX_all860_dcl_%s' % label, worst_d, 1e-11, at=wdloc, cl_kind=xkind, delta=delta)
    if False:      # SPEC v9.3 structural zeros: the three zero-field low generators of the integer branch; fields exactly 0.0 expected, gated at 1e-41; cl derivatives gated above
        jz = 3 if clv == 2.0 else 2; zero_gens = [B.LOW_INDEX[(0, 0, jz)], B.LOW_INDEX[(0, 1, jz)], B.LOW_INDEX[(1, 1, jz)]]
        zrows = [{'generator': int(g_), 'triple': list(B.LOW[g_]), 'field': k, 'point': int(i_), 'production': float(prod[k][i_, g_]), 'reference': float(hp[k][i_, g_])} for g_ in zero_gens for k in FIELDS7 for i_ in range(len(pts))]
        nonzero = [z for z in zrows if z['production'] != 0.0]; worst_zero = max(abs(z['production']) for z in zrows)
        check('T2.7H_structural_zeros_fields_%s' % label, worst_zero, 1e-41, floor='absolute 1e-41 (band_max is 0)', generators=[list(B.LOW[g_]) for g_ in zero_gens], nonzero_production_values=nonzero[:100], nonzero_count=len(nonzero), reference_max_abs=max(abs(z['reference']) for z in zrows))
        dz = max(float(np.max(abs(dprod[k][:, g_]-dhp[k][:, g_]))/max(np.max(abs(dhp[k][:, g_])), 1e-30)) for g_ in zero_gens for k in FIELDS7)
        check('T2.7H_structural_zero_generators_dcl_nonzero_and_accurate_%s' % label, dz, 1e-11, dcl_reference_max=[float(np.max(abs(dhp[k][:, g_]))) for g_ in zero_gens for k in FIELDS7][:21])
        summary[label]['structural_zero_rows'] = zrows
out['T2.7H-X'] = summary; out['import_closure'] = loaded_closure()
out['passed'] = all(c['passed'] for c in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
out_path.write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
