"""Independent assessment of an 860 T1 state (SPEC v5 sections 12, 13): frozen 32 regions, dense grid, local refinements, exact axes,
near-origin bands, C5 in high precision, widths, far-field E_1/E_2/E_3 with represented/unresolved harmonics, tight whole-axis integral,
direct large-r check of R_rho against the leading E_1 term. Stateless evaluator (independent of the production cache).
Usage: assess860.py <out.json> <manifest.json> <candidate.json or seed_860.json> [workers] [--spot-only [--no-integral]]
--no-integral is accepted only together with --spot-only (E7); a full assessment always carries tight_independent_integral and its accuracy flag must be a boolean.
All imports are at the top (lead item F, 10:50Z): a missing module fails in the first second. Layout: the frozen work/research860 (tests/ beside this file,
tools/ beside research860); a development copy elsewhere resolves both against the frozen layout through absolute_common.ROOT."""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, sys, time
if '--no-integral' in sys.argv and '--spot-only' not in sys.argv:                 # E7 (a): a full assessment always runs the tight independent integral (SPEC 13 (a)); refused before any import or evaluation
    sys.stderr.write('REFUSAL: --no-integral is allowed only together with --spot-only; a full assessment always runs the tight independent integral (SPEC 13 (a), lead E7)\n'); sys.exit(2)
from decimal import Decimal, localcontext
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
if not (Path(__file__).resolve().parent/'basis860.py').exists():                                   # development copy outside the frozen layout (outputs/dev_v9/pending): the frozen library is <lane>/work/research860
    for _up in Path(__file__).resolve().parents:
        if (_up/'work'/'research860'/'basis860.py').exists(): sys.path.insert(1, str(_up/'work'/'research860')); break
import numpy as np
from threadpoolctl import threadpool_limits
import basis860 as B, chart860 as C, hp860 as H, farfield860 as FF
from widths860 import widths                       # F14: never raises; None with reasons
from fields860 import residual as new_residual, fields as new_fields
from integrate860 import independent_integral
from absolute_common import ROOT, BASE, A_REF, read, digest, array_hash
from closure860 import loaded_closure
HERE = Path(__file__).resolve().parent
_TESTS = HERE/'tests' if (HERE/'tests'/'points860.py').exists() else ROOT.parent/'research860'/'tests'
_WORK = HERE.parent if (HERE.parent/'tools'/'runtime.py').exists() else ROOT.parent
sys.path.insert(0, str(_TESTS)); sys.path.insert(0, str(_WORK/'tools'))
import os, hashlib as _hl
from fractions import Fraction
from points860 import FINITE_V92, FAR, T27H_BANDS
from fields860 import condition_sums as stateless_condition_sums
from kappa860 import load_kappa as _load_kappa
from shapes860 import point_model
from model860 import Model860
from absolute_model import FrozenLogMesh
from runtime import Runtime
from exactcheckpoint860 import exact_canonical
from absolute_common import array_hash as _ah
from origin860 import generator_polynomial
from highprecision_origin import _fields, evaluate_series
from decimal import localcontext as _lc
U_RF = 2.**-64
EXACT_ZERO_BOUNDS = []        # C6 ruling: a zero bound with zero error is ratio 0 (recorded here), a zero bound with nonzero error is invalid (ratio inf)
out_path = Path(sys.argv[1]); manifest = Path(sys.argv[2]); cand_path = Path(sys.argv[3]); workers = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4].isdigit() else 8; do_integral = '--no-integral' not in sys.argv
SPOT_ONLY = '--spot-only' in sys.argv      # bench860 F12 / lead ruling 3: time the section 13 R_f spot check alone: no integral, no exact far field, no large-r check; mode 'spot_only'; consumers refuse it as a full assessment
if SPOT_ONLY: do_integral = False
cand = json.loads(cand_path.read_text())
P = np.array([float.fromhex(h) for h in (cand.get('P_raw_chart_hex') or cand['P_hex'])]); high = np.array([float.fromhex(h) for h in cand['high_hex']]); cl = float(P[0])
prep = B.prepare(cl, P[1:], high); hp = C.hp_report(P, 90)
out = {'schema': 'assess860_v2_spec_v915', 'P_sha256': _ah(P), 'high_sha256': _ah(high), 'code_manifest_sha256': digest(manifest), 'candidate_path': str(cand_path), 'candidate_sha256': digest(cand_path), 'basis_version': B.VERSION, 'cl': cl, 'a0': hp['a0'],
       'five_Taylor': hp['constraints'], 'five_Taylor_max': hp['max_abs'], 'center_abs': hp['center_abs'], 'poisson_max_abs': hp['poisson_max_abs'], 'a000_analytic': hp['coefficients_decimal'][0],
       'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'sampled_only': True, 'continuous_supremum_certificate': False}
out['widths'] = widths(hp)                                                                     # F14 (lead review of topics 31/33): undefined widths are null with a reason
UNDEFINED_QUOTIENTS = {'count': 0, 'where': []}
NONFINITE_MONITOR = []        # E9: every nonfinite input met before a monitor reduction (near_origin, direct_large_r, origin truncation monitor), with where/generator/key
def finite_max(values, label):
    """E9 (lead fix check 3): count the nonfinite entries (NONFINITE_SAMPLES, which enters completeness.failed, and NONFINITE_MONITOR with the label) BEFORE the reduction;
    return the maximum over the finite entries, or None when none is finite (the caller records the reason)."""
    v = np.asarray(values, float).ravel(); bad = int(np.count_nonzero(~np.isfinite(v)))
    if bad: NONFINITE_SAMPLES['count'] += bad; NONFINITE_MONITOR.append({'where': label, 'nonfinite_count': bad, 'total': int(v.size)})
    fin = v[np.isfinite(v)]
    return float(np.max(fin)) if len(fin) else None
def origin_compare(v40, v48, w40, w48, generator, key):
    """E9 addendum (lead 11:56Z): relative differences of the order-48 vs order-56 series values and c_l derivatives at the monitor points. A nonfinite input or ratio is
    counted (NONFINITE_SAMPLES and NONFINITE_MONITOR with generator and key) and returned as None, so the caller's worst stays finite and the monitor stops on it."""
    def rel(p48, p56):
        p48 = np.asarray(p48, float); p56 = np.asarray(p56, float)
        if not (np.all(np.isfinite(p48)) and np.all(np.isfinite(p56))): return None
        scale = max(float(np.max(abs(p56))), 1e-30); r_ = float(np.max(abs(p48-p56))/scale)
        return r_ if math.isfinite(r_) else None
    rat = rel(v40, v48); drat = rel(w40, w48); bad = [n for n, r_ in (('value', rat), ('cl_derivative', drat)) if r_ is None]
    if bad: NONFINITE_SAMPLES['count'] += len(bad); NONFINITE_MONITOR.append({'where': 'origin_truncation_monitor', 'generator': generator, 'key': key, 'nonfinite': bad})
    return rat, drat
def values(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float); r = np.hypot(x, y); ff = new_fields(prep, x, y, threads=workers); rf = new_residual(prep, x, y, procs=workers)      # parallel stateless provider (the serial call needed about an hour for the dense grids)
    wx = cl*x-ff['psiy']; wy = cl*y+ff['psix']; nf = abs(wx*ff['fx'])+abs(wy*ff['fy'])+abs(ff['q']*ff['f']); nrf = abs(wx*ff['fx'])+abs((ff['q']+1)*(ff['f']+y*ff['fy']))+abs(ff['f'])
    yr = np.divide(y, r, out=np.zeros_like(y), where=r > 0)
    rel_f = np.divide(abs(rf), nf, out=np.full_like(rf, np.nan), where=nf > 0); rel_rho = np.divide(abs(rf), nrf, out=np.full_like(rf, np.nan), where=nrf > 0)
    # SPEC 13 (g) / v9.15 (2): at exactly (0,0) with R_f == 0.0 and N_f == 0.0 exactly and finite f, rho, R_rho, N_rho the quotient is undefined 0/0 (null with reason), counted under
    # undefined_quotients and excluded from the nonfinite count; any other NaN/Inf (including R_f != 0 at the origin) remains a failing nonfinite sample
    undefined = (r == 0.) & (rf == 0.) & (nf == 0.) & np.isfinite(ff['f']) & np.isfinite(y*ff['f']) & np.isfinite(y*rf) & np.isfinite(nrf)
    if np.any(undefined): UNDEFINED_QUOTIENTS['count'] += int(np.count_nonzero(undefined)); UNDEFINED_QUOTIENTS['where'].append({'reason': 'undefined 0/0 at the exact origin', 'count': int(np.count_nonzero(undefined))}); rel_f = rel_f.copy(); rel_rho = rel_rho.copy(); rel_f[undefined] = np.nan; rel_rho[undefined & (nrf == 0.)] = np.nan
    return {'E_f': abs(rf)/A_REF, 'E_rho': abs(yr*rf)/A_REF, 'relative_Rf_exact': rel_f, 'relative_Rrho_factored': rel_rho, 'abs_Rrho': abs(y*rf), '_undefined': undefined}
NONFINITE_SAMPLES = {'count': 0}
def maxrec(v, x, y, region, undefined=None):
    ok = np.isfinite(v); und = np.zeros(len(v), bool) if undefined is None else np.asarray(undefined, bool); nbad = int(np.count_nonzero(~ok & ~und)); NONFINITE_SAMPLES['count'] += nbad   # v9.13 (a): nonfinite samples counted, never dropped; exact-origin 0/0 excluded (v9.15 (2))
    rec = {'region': region, 'points': int(len(x)), 'nonfinite_samples': nbad, 'undefined_quotients': int(np.count_nonzero(und)), 'undefined_reason': ('undefined 0/0 at the exact origin' if np.any(und) else None)}
    if not np.any(ok): rec['value'] = None; return rec
    i = int(np.flatnonzero(ok)[np.argmax(abs(v[ok]))]); rec.update(value=float(abs(v[i])), xy=[float(x[i]), float(y[i])], radius=float(math.hypot(x[i], y[i])), theta=float(math.atan2(y[i], x[i]))); return rec
TARGETS = ('E_f', 'E_rho', 'relative_Rf_exact', 'relative_Rrho_factored')
design = read(ROOT/'inputs/absolute_assessment_design.json'); grids = read(BASE/'inputs/assessment_grids_stage12.json')
with np.load(ROOT/'inputs/absolute_assessment_coordinates.npz', allow_pickle=False) as arrays:
    for name in design['regions']: grids[name] = {'x': arrays[name+'_x'].tolist(), 'y': arrays[name+'_y'].tolist()}
regions = {}; allx = []; ally = []
if not SPOT_ONLY:    # bench860 --spot-only skips the 32 regions, dense grids, refinements, near-origin bands and 85-digit peak checks
    with threadpool_limits(limits=workers, user_api='blas'):
        for name, row in grids.items():
            x = np.asarray(row['x'], float); y = np.asarray(row['y'], float); vv = values(x, y); regions[name] = {k: maxrec(v, x, y, name, vv['_undefined'] if k.startswith('relative_') else None) for k, v in vv.items() if k != '_undefined'}; allx.append(x); ally.append(y)
        out['frozen32_regions'] = regions; out['frozen32_maxima'] = {t: max((r_[t] for r_ in regions.values()), key=lambda z: -1 if z['value'] is None else z['value']) for t in TARGETS+('abs_Rrho',)}
        X = np.concatenate(allx); Y = np.concatenate(ally); R = np.hypot(X, Y); vv = values(X, Y)
        out['frozen32_radial_bands'] = [{'lo': lo, 'hi': hi, 'points': int(np.count_nonzero((R >= lo) & (R < hi))), 'E_f_max': float(np.nanmax(vv['E_f'][(R >= lo) & (R < hi)])) if np.any((R >= lo) & (R < hi)) else None, 'E_rho_max': float(np.nanmax(vv['E_rho'][(R >= lo) & (R < hi)])) if np.any((R >= lo) & (R < hi)) else None}
                                         for lo, hi in zip([0., 1e-7, 1e-5, 1e-3, .02, .1, 1., 10., 100., 1e3, 1e4, 1e6, 1e8, 1e12, 1e16, 1e20], [1e-7, 1e-5, 1e-3, .02, .1, 1., 10., 100., 1e3, 1e4, 1e6, 1e8, 1e12, 1e16, 1e20, float('inf')])]
        radii = np.geomspace(1e-12, 1e20, 129); xx = np.r_[radii, np.zeros_like(radii), 0.]; yy = np.r_[np.zeros_like(radii), radii, 0.]; va = values(xx, yy); out['exact_axes_origin'] = {k: maxrec(v, xx, yy, 'exact_axes', va['_undefined'] if k.startswith('relative_') else None) for k, v in va.items() if k != '_undefined'}
        out['dense_grids'] = {}
        for level, (nr, nt) in enumerate(((769, 199), (1537, 397))):
            rr = np.geomspace(.02, 1e12, nr)[:, None]; ang = np.linspace(0, np.pi/2, nt); x = (rr*np.cos(ang)).ravel(); y = (rr*np.sin(ang)).ravel(); x[np.tile(ang == np.pi/2, nr)] = 0.; y[np.tile(ang == 0, nr)] = 0.
            vd = values(x, y); out['dense_grids']['level%d_%dx%d' % (level, nr, nt)] = {k: maxrec(v, x, y, 'dense%d' % level, vd['_undefined'] if k.startswith('relative_') else None) for k, v in vd.items() if k != '_undefined'}
        # local refinements (4 levels) around the top seeds for E_f and E_rho
        out['refinements'] = {}
        for target in ('E_f', 'E_rho'):
            seeds = sorted([r_[target] for r_ in list(regions.values())+list(out['dense_grids'].values()) if r_[target]['value'] is not None and r_[target].get('radius', 0) > 0], key=lambda z: -z['value'])
            chosen = []; seen = set()
            for sd in seeds:
                key = (round(math.log(sd['radius']), 1), round(sd['theta'], 1))
                if key not in seen: seen.add(key); chosen.append(sd)
                if len(chosen) == 3: break
            refs = []
            for sd in chosen:
                s = math.log(sd['radius']); th = sd['theta']; levels = []
                for sw, tw, cnt in ((.12, .04, 25), (.03, .01, 33), (.0075, .0025, 49), (.001875, .000625, 65)):
                    ss = np.linspace(s-sw, s+sw, cnt); tt = np.unique(np.clip(np.linspace(th-tw, th+tw, cnt), 0, np.pi/2)); rr = np.exp(ss)[:, None]
                    x = (rr*np.cos(tt[None, :])).ravel(); y = (rr*np.sin(tt[None, :])).ravel(); x[np.tile(tt == np.pi/2, len(ss))] = 0.; y[np.tile(tt == 0, len(ss))] = 0.
                    pk = maxrec(values(x, y)[target], x, y, 'refine'); levels.append(pk); s = math.log(pk['radius']) if pk['radius'] > 0 else s; th = pk['theta']
                refs.append({'seed': sd, 'levels': levels})
            out['refinements'][target] = refs
        out['refined_maxima'] = {t: max((z['levels'][-1] for z in out['refinements'][t]), key=lambda z: z['value']) for t in ('E_f', 'E_rho')}
        # near-origin bands and the origin series region
        rr = np.geomspace(1e-6, .1, 400)[:, None]; ang = np.linspace(0, np.pi/2, 65); x = (rr*np.cos(ang)).ravel(); y = (rr*np.sin(ang)).ravel(); x[np.tile(ang == np.pi/2, 400)] = 0.; y[np.tile(ang == 0, 400)] = 0.; r = np.hypot(x, y); vo = values(x, y)
        out['near_origin'] = {'E_f_max_r_lt_0p02': finite_max(vo['E_f'][r < .02], 'near_origin.E_f_max_r_lt_0p02'), 'E_f_max_0p02_le_r_lt_0p1': finite_max(vo['E_f'][(r >= .02) & (r < .1)], 'near_origin.E_f_max_0p02_le_r_lt_0p1'), 'E_rho_max_r_lt_0p02': finite_max(vo['E_rho'][r < .02], 'near_origin.E_rho_max_r_lt_0p02'), 'E_rho_max_0p02_le_r_lt_0p1': finite_max(vo['E_rho'][(r >= .02) & (r < .1)], 'near_origin.E_rho_max_0p02_le_r_lt_0p1')}   # E9: nonfinite samples counted before the reduction
        out['near_origin']['nonfinite_samples'] = [m for m in NONFINITE_MONITOR if m['where'].startswith('near_origin')]; out['near_origin']['reasons'] = {k: 'no finite sample in this band' for k, v in out['near_origin'].items() if v is None}
        # 85-digit check at the refined peaks
        checks = []
        for t in ('E_f', 'E_rho'):
            pk = out['refined_maxima'][t]; x0, y0 = pk['xy']; ref = H.independent_fields(prep, x0, y0, 85)['Rf']; got = float(new_residual(prep, [x0], [y0])[0])
            checks.append({'target': t, 'xy': [x0, y0], 'stateless_Rf': got, 'independent85_Rf': ref, 'difference_abs': abs(got-ref), 'tolerance_abs': 1e-12+1e-7*abs(ref), 'passed': abs(got-ref) <= 1e-12+1e-7*abs(ref)})
        out['peak_independent85_checks'] = checks
if not SPOT_ONLY:    # bench860 --spot-only skips the origin truncation monitor
    # origin truncation monitor (SPEC v9.3 section 13): production order-48 generator fields and cl derivatives at the training nodes with r = 0.02 vs order 56
    with _lc() as ctx:
        ctx.prec = 90; L = Decimal.from_float(cl); worst = 0.; worst_gen = None; th = np.linspace(0, np.pi/2, 9); xo = .02*np.cos(th); yo = .02*np.sin(th); xo[-1] = 0.; yo[0] = 0.
        for col in range(860):
            kind, tr = ('low', B.LOW[col]) if col < 60 else ('high', B.HIGH[col-60])
            c40, d40 = generator_polynomial(kind, tr, L, 52); c48, d48 = generator_polynomial(kind, tr, L, 60)
            f40 = _fields(c40, 48); f48 = _fields(c48, 56); g40 = _fields(d40, 48); g48 = _fields(d48, 56)
            for key in ('f', 'fx', 'fy', 'psi', 'psix', 'psiy', 'ratio'):
                v40 = evaluate_series(f40[key], xo, yo); v48 = evaluate_series(f48[key], xo, yo); w40 = evaluate_series(g40[key], xo, yo); w48 = evaluate_series(g48[key], xo, yo)
                rat, drat = origin_compare(v40, v48, w40, w48, [kind, list(tr)], key)                                         # E9 addendum: a nonfinite comparison is counted and stops; worst stays finite
                for r_ in (rat, drat):
                    if r_ is not None and r_ > worst: worst = r_; worst_gen = [kind, list(tr), key]
    nonfinite_origin = [m for m in NONFINITE_MONITOR if m['where'] == 'origin_truncation_monitor']
    out['origin_truncation_monitor'] = {'order_production': 48, 'order_check': 56, 'radius': .02, 'angles': 9, 'worst_band_relative': worst, 'worst_generator': worst_gen, 'stop_threshold': 1e-12, 'nonfinite_comparisons': nonfinite_origin, 'scientific_stop': bool(worst > 1e-12 or nonfinite_origin)}
if not SPOT_ONLY:    # ruling 3: --spot-only has no exact far field and no large-r check
    # far field from the canonical a (Decimal)
    aX, xrec = exact_canonical(P, high); out['farfield_input_exact_for_checkpoint'] = xrec            # D3 (f): exact rationals of the checkpoint, not a rounded array
    ff = FF.analyze(aX, cl, qmax=3); out['farfield'] = ff                      # v3: exact rational engine (topic 43); growth fields null unless determined
    # direct large-r check (F17 (d), SPEC 12 v9.3/v9.4): R_rho(r, theta) / r^alpha against the ACTUAL leading sector's angular profile (sine coefficients)
    # at r in [1e3, 1e7]; when the leading power is undetermined, the unnormalized values are reported and no ratio is formed.
    def leading_profile(ff, theta):
        """D3-c / ruling 10: the leading-sector angular profile sum_k c_k sin(k theta) from the exact engine's binary64 coefficients, formed from the coefficients divided by
        their maximum absolute value (common scale, so its norm is O(1)); returns (profile or None, scale or None, note). If any leading coefficient is unrepresentable
        (None), no profile is formed and the note names the harmonics and their reasons; also None when the leading power is not determined."""
        coeffs = ff.get('leading_sector_sine_coefficients_odd'); unrep = ff.get('leading_sector_sine_coefficients_unrepresentable') or {}
        if not ff['actual_leading_density_power'].get('determined'): return None, None, 'no determined leading sector (status: %s)' % ff['actual_leading_density_power'].get('status')
        if not coeffs: return None, None, 'determined leading sector without representable coefficients'
        bad = {k: v for k, v in coeffs.items() if v is None}
        if bad or unrep: return None, None, 'leading coefficients unrepresentable in binary64: %s' % json.dumps({k: unrep.get(k, {'reason': 'null'}) for k in sorted(set(bad)|set(unrep), key=int)})
        scale = max(abs(v) for v in coeffs.values())
        if not (scale > 0 and math.isfinite(scale)): return None, None, 'leading coefficients have no finite positive scale'
        prof = sum((v/scale)*np.sin(int(k)*theta) for k, v in coeffs.items())
        return prof, scale, None
    gamma = 1/cl; theta = np.linspace(0, np.pi/2, 513); lead = ff['actual_leading_density_power']; rows = []
    prof, prof_scale, prof_note = leading_profile(ff, theta); pnorm = float(np.linalg.norm(prof)) if prof is not None else 0.
    with threadpool_limits(limits=workers, user_api='blas'):
        for rad in (1e3, 1e4, 1e5, 1e6, 1e7):
            x = rad*np.cos(theta); y = rad*np.sin(theta); x[-1] = 0.; y[0] = 0.; rf = new_residual(prep, x, y); rrho = y*rf
            row = {'radius': rad, 'max_abs_Rrho': finite_max(abs(rrho), 'direct_large_r.max_abs_Rrho.r=%g' % rad), 'leading_power_status': lead['status']}      # E9: nonfinite production values counted before the reduction
            if row['max_abs_Rrho'] is None: row['max_abs_Rrho_reason'] = 'no finite production value at this radius'
            if lead['exponent'] is not None and prof is not None and pnorm > 0 and math.isfinite(pnorm):
                scaled = (rrho/rad**lead['exponent'])/prof_scale; rel = float(np.linalg.norm(scaled-prof)/pnorm)                       # ruling 10: common scale (max |coef|)
                if math.isfinite(rel): row.update(leading_exponent=lead['exponent'], relative_difference_from_leading_sector_profile=rel, profile_scale=prof_scale)
                else: row.update(leading_exponent=lead['exponent'], relative_difference_from_leading_sector_profile=None, note='ratio not finite after common scaling (overflow/underflow of the production values at this radius); unnormalized max_abs_Rrho kept')
            else: row.update(leading_exponent=lead['exponent'], relative_difference_from_leading_sector_profile=None, note=(prof_note or 'no determined leading sector')+'; unnormalized max_abs_Rrho kept')
            rows.append(row)
    out['direct_large_r_vs_leading_sector'] = rows
# ---- SPEC v9.9 (b), section 13 from the G4 pilot on: R_f reference spot check at the T2.6c points against the unrounded Decimal reference with the complete
# rounding-bound ratio per point; a ratio above 1 is a scientific stop; r_d and r_z (SPEC v9.9 (a)) are added within relative 2^-20 of 2 or 3.
kfile = Path(os.environ.get('IPM_KAPPA_FILE', ((_artifact_root + "/outputs") + '/campaign860/kappa_calibration_typed.json')))
KAPPA_FAILURE = None
try: kap = _load_kappa(str(kfile), str(manifest)); kappa = kap['kappa']; kappa_source = kap
except Exception as exc: KAPPA_FAILURE = 'kappa: %s: %s' % (type(exc).__name__, exc); kappa = float('nan'); kappa_source = {'error': KAPPA_FAILURE, 'rule': 'v9.15 (3): kappa may come only from the validated calibration file; this assessment is marked failed'}
INVALID_BOUND_INPUTS = []
spot_pts = [(name, x, y) for name, x, y in FINITE_V92+FAR]
def near_integer_radii(cl):
    """SPEC v9.9 (a) / v9.13 (b): within relative 2^-20 of 2 or 3, beta = (1 - j + (1 + j)/c_l)/2 exactly (j = 3 near 2, j = 2 near 3); r_d = |beta|^(-1/2), r_z = (2/|beta|)^(1/2)
    at 60 digits rounded once; at exactly c_l = 2 or 3 beta = 0 is recorded and the infinite radii are omitted (never raises). Returns None away from 2 and 3."""
    for base, jj in ((2., 3), (3., 2)):
        if abs(cl/base-1.) < 2.**-20:
            beta = (Fraction(1-jj)+Fraction(1+jj)/Fraction(float(cl)))/2
            if beta == 0: return {'base': base, 'j': jj, 'beta_exact_rational': '0', 'r_d': None, 'r_z': None, 'note': 'beta = 0 exactly at c_l = %g: the transition radii are infinite and omitted (SPEC v9.13 (b)); the exceptional-parameter rule of section 11 applies' % base}
            with localcontext() as cx:
                cx.prec = 60; bb = abs(Decimal(beta.numerator)/Decimal(beta.denominator)); rd = float((1/bb).sqrt()); rz = float((2/bb).sqrt())
            return {'base': base, 'j': jj, 'beta_exact_rational': '%d/%d' % (beta.numerator, beta.denominator), 'r_d': rd, 'r_z': rz}
    return None
near = near_integer_radii(cl)
if near and near['r_d'] is not None: spot_pts += [('r_d', near['r_d']*math.cos(.9), near['r_d']*math.sin(.9)), ('r_z', near['r_z']*math.cos(.9), near['r_z']*math.sin(.9))]
sx = np.array([q[1] for q in spot_pts]); sy = np.array([q[2] for q in spot_pts])
with threadpool_limits(limits=1, user_api='blas'):
    rf_st = new_residual(prep, sx, sy); SR_st = stateless_condition_sums(prep, sx, sy)
    mb, root_b = point_model(sx, sy, workers=workers); rf_b = mb.fun(P, high)/root_b; SR_b = mb.condition_sums(P, high); mb.clear_cache()
    rf_s = np.empty(len(sx)); SR_s = np.empty(len(sx))
    for i in range(len(sx)):
        ms, root_s = point_model([sx[i]], [sy[i]], workers=1); rf_s[i] = float((ms.fun(P, high)/root_s)[0]); SR_s[i] = float(ms.condition_sums(P, high)[0]); ms.clear_cache()
def bound_ratio(val, S, ref):
    """v9.13 (d): |R_f,prod - R_f,dec| / (kappa u S_R + 2^-53 |R_f,prod|), the production value in the denominator. v9.15 (3): invalid inputs (nonfinite or negative S_R,
    nonfinite kappa, nonfinite production value) are recorded as failures and return ratio inf, never 0."""
    if not (math.isfinite(float(S)) and float(S) >= 0 and math.isfinite(float(kappa)) and math.isfinite(float(val))):
        INVALID_BOUND_INPUTS.append({'S_R': float(S), 'kappa': float(kappa), 'value': float(val)}); return float('inf'), float('inf'), float('inf')
    with localcontext() as cx:
        cx.prec = 60; err = abs(Decimal.from_float(float(val))-ref); den = Decimal(kappa)*Decimal(U_RF)*Decimal.from_float(float(S))+Decimal(2)**-53*abs(Decimal.from_float(float(val)))
        if den <= 0:
            if err == 0: EXACT_ZERO_BOUNDS.append({'S_R': float(S), 'value': float(val), 'reference': format(ref, '.6e')}); return 0., 0., 0.      # C6 ruling: zero bound with zero error is ratio 0 (an exact zero of the evaluation)
            INVALID_BOUND_INPUTS.append({'S_R': float(S), 'kappa': float(kappa), 'value': float(val), 'note': 'zero bound with nonzero error %s' % format(err, '.6e')}); return float(err), 0., float('inf')
        return float(err), float(den), float(err/den)
spot_rows = []; worst_ratio = 0.
for i, (name, x, y) in enumerate(spot_pts):
    ref = H.point_reference(prep, float(x), float(y), 85, columns=False)['Rf_decimal']
    rec = {'point': name, 'x': float(x), 'y': float(y), 'r': float(math.hypot(x, y)), 'Rf_decimal_85': format(ref, '.40e')}
    for path, val, S in (('stateless', rf_st[i], SR_st[i]), ('batch', rf_b[i], SR_b[i]), ('single', rf_s[i], SR_s[i])):
        err, den, ratio = bound_ratio(val, S, ref); rec['Rf_'+path] = float(val); rec['S_R_'+path] = float(S); rec['abs_error_'+path] = err; rec['bound_'+path] = den; rec['ratio_'+path] = ratio; worst_ratio = max(worst_ratio, ratio)
    spot_rows.append(rec)
out['rf_reference_spot_check'] = {'rule': 'SPEC v9.9 (b) / v9.13 (d): |R_f(prod) - R_f(Decimal 85, unrounded)| <= kappa u S_R(prod path) + 2^-53 |R_f(prod)| per point and per production configuration (stateless, batch Model860, one-point Model860); a ratio above 1 is a scientific stop',
                                  'kappa': kappa, 'kappa_source': kappa_source, 'u': U_RF, 'points': spot_rows, 'worst_ratio': worst_ratio, 'added_near_integer_points': near, 'configurations': ['stateless', 'batch', 'single'],
                                  'scientific_stop': bool(not math.isfinite(worst_ratio) or worst_ratio > 1.)}
# ---- SPEC v9.12 (4) / v9.13 / v9.14: stratified random and targeted training nodes against the production batch arrays of the state
RT = Runtime(str(_WORK)); rt_state2 = RT.read(ROOT/'campaign/global181_v3/state.json'); epoch_rec = RT.read(rt_state2['epoch_path']); mesh_tr = FrozenLogMesh.load(epoch_rec['meshes']['training']['path'])   # S1: translated handoff paths
mx, my = mesh_tr.coordinates(); mr = np.hypot(mx, my); root_tr = np.sqrt(2*mesh_tr.weights/(np.pi*A_REF**2)); N = len(mx)
def bind_snapshot(cand, cand_path, N, mesh_fingerprint, P, high):
    """D6 (checklist): the production batch arrays of a campaign snapshot are used only when the snapshot artifact itself carries the state and matches it: its own P
    and high arrays equal the candidate's bitwise, its mesh fingerprint equals the training mesh in use, its configuration metadata is present and typed, every
    array has the exact shape (N,) ((N, 1) is refused), the residual is finite, S_R and e are finite and nonnegative, and the file hash equals the hash recorded in
    the candidate. Nothing is copied from the candidate into the record. Returns (arrays or None, failure reason or None, source record or None, supplied flag):
    a supplied but missing or invalid snapshot is a failure (supplied True); no snapshot supplied (the seed) is not (supplied False)."""
    arrays_path = cand.get('snapshot_arrays_path')
    if not arrays_path: return None, None, None, False
    p = Path(str(arrays_path))
    if not p.exists(): return None, 'supplied snapshot missing: %s' % arrays_path, None, True
    sha_now = digest(p)
    if cand.get('snapshot_arrays_sha256') != sha_now: return None, 'snapshot_arrays_sha256 mismatch: candidate %s vs file %s' % (cand.get('snapshot_arrays_sha256'), sha_now), None, True
    try:
        with np.load(p, allow_pickle=False) as zz:
            miss = [k for k in ('P', 'high', 'residual', 'S_R', 'e', 'mesh_fingerprint', 'configuration_json') if k not in zz]
            if miss: return None, 'snapshot lacks arrays/metadata %s' % miss, None, True
            Ps = np.asarray(zz['P']); Hs = np.asarray(zz['high']); r_ = np.asarray(zz['residual']); S_ = np.asarray(zz['S_R']); e_ = np.asarray(zz['e']); fp = str(zz['mesh_fingerprint']); conf_raw = str(zz['configuration_json'])
    except Exception as exc: return None, 'snapshot unreadable: %s: %s' % (type(exc).__name__, exc), None, True
    P = np.asarray(P, float); high = np.asarray(high, float)
    if not (Ps.dtype == np.float64 and Hs.dtype == np.float64 and Ps.shape == P.shape and Hs.shape == high.shape and Ps.tobytes() == P.tobytes() and Hs.tobytes() == high.tobytes()): return None, 'snapshot P/high differ from the candidate (bitwise comparison of the saved arrays)', None, True
    for name, arr in (('residual', r_), ('S_R', S_), ('e', e_)):
        if arr.shape != (N,): return None, '%s shape %s is not (%d,)' % (name, arr.shape, N), None, True
        if arr.dtype != np.float64: return None, '%s dtype %s is not float64' % (name, arr.dtype), None, True
    if not np.all(np.isfinite(r_)): return None, 'residual not finite (%d entries)' % int(np.count_nonzero(~np.isfinite(r_))), None, True
    if not (np.all(np.isfinite(S_)) and np.all(S_ >= 0) and np.all(np.isfinite(e_)) and np.all(e_ >= 0)): return None, 'S_R or e not finite and nonnegative', None, True
    if fp != str(mesh_fingerprint): return None, 'snapshot mesh fingerprint %s differs from the training mesh %s' % (fp, mesh_fingerprint), None, True
    try: conf = json.loads(conf_raw)
    except Exception as exc: return None, 'snapshot configuration metadata unparsable: %s' % exc, None, True
    if not (isinstance(conf, dict) and all(type(conf.get(k)) is int for k in ('workers', 'cache_threads', 'block_size', 'mode_block'))): return None, 'snapshot configuration metadata incomplete or untyped: %r' % (conf,), None, True
    src = {'kind': 'campaign snapshot (production batch evaluation of the state)', 'path': str(p), 'sha256': sha_now, 'candidate_sha256': digest(cand_path), 'mesh_fingerprint': fp, 'configuration': conf,
           'provenance': 'P, high, mesh fingerprint and configuration read from the snapshot artifact itself and compared with the candidate and the training mesh (D6)'}
    return (r_.copy(), S_.copy(), e_.copy()), None, src, True
arrays_path = cand.get('snapshot_arrays_path'); r_arr = S_arr = e_arr = None
bound_arrays, ARRAY_BINDING_FAILURE, arrays_source, SNAPSHOT_SUPPLIED = bind_snapshot(cand, cand_path, N, mesh_tr.fingerprint, P, high)      # v9.15 (3) / D6
if bound_arrays is not None: r_arr, S_arr, e_arr = bound_arrays
if r_arr is None:
    t0 = time.time(); mtr = Model860(mesh_tr, A_REF, block_size=4096, mode_block=64, workers=workers, threads=min(workers, 4)); r_arr = mtr.fun(P, high); S_arr = mtr.condition_sums(P, high)
    e_arr = root_tr*(kappa*U_RF*S_arr)+2.**-53*abs(r_arr); mtr.clear_cache(); side = out_path.with_name(out_path.stem+'.production_batch_arrays.npz'); np.savez_compressed(side, residual=r_arr, S_R=S_arr, e=e_arr)
    arrays_source = {'kind': 'production batch evaluation (Model860, training mesh) computed by this assessment', 'path': str(side), 'sha256': digest(side), 'seconds': time.time()-t0, 'e_definition': 'root (kappa u S_R) + 2^-53 |r| (no root-weight term h: campaign states carry their own e)', 'candidate_sha256': digest(cand_path), 'mesh_fingerprint': mesh_tr.fingerprint, 'configuration': {'workers': workers, 'threads': min(workers, 4), 'block_size': 4096}, 'snapshot_supplied': SNAPSHOT_SUPPLIED, 'snapshot_arrays_binding_failure': ARRAY_BINDING_FAILURE}
band_edges = [b[0] for b in T27H_BANDS]+[float('inf')]
band_id = np.digitize(mr, band_edges[1:-1]); Nb = [int(np.count_nonzero(band_id == b)) for b in range(len(T27H_BANDS))]
seed_int = int(_hl.sha256(digest(cand_path).encode()).hexdigest()[:16], 16); rng = np.random.default_rng(seed_int)
RANDOM_TOTAL = 32; nb = [min(Nb[b], max(2, math.ceil(RANDOM_TOTAL*Nb[b]/N))) if Nb[b] > 0 else 0 for b in range(len(T27H_BANDS))]
random_idx = []
for b in range(len(T27H_BANDS)):
    members = np.flatnonzero(band_id == b)
    if nb[b] > 0: random_idx += [int(i) for i in rng.choice(members, size=nb[b], replace=False)]
rf_prod_tr = np.divide(r_arr, root_tr, out=np.zeros_like(r_arr), where=root_tr > 0)
nz = np.flatnonzero(r_arr != 0); ratio_er = np.full(N, np.inf); ratio_er[nz] = e_arr[nz]/abs(r_arr[nz])
targeted = {'smallest_e_over_r': [int(i) for i in np.argsort(ratio_er)[:4]], 'smallest_nonzero_S_R_among_nonzero_residuals': [int(i) for i in nz[np.argsort(S_arr[nz])[:2]]] if len(nz) else [],
            'nearest_r_1': [int(np.argmin(abs(mr-1.)))], 'nearest_r_0.02': [int(np.argmin(abs(mr-.02)))], 'near_y_axis_per_decade': []}
th = np.arctan2(my, mx)
for lo, hi in ((10., 1e2), (1e2, 1e3), (1e3, 1e4), (1e4, 1e5)):
    sel = np.flatnonzero((mr >= lo) & (mr < hi))
    if len(sel): targeted['near_y_axis_per_decade'].append(int(sel[np.argmin(abs(th[sel]-np.pi/2))]))
targeted_idx = sorted({i for v in targeted.values() for i in v})
spot_nodes = []; worst_random = 0.; worst_targeted = 0.; fails_random = 0; sel_idx = sorted(set(random_idx)|set(targeted_idx))
nx = mx[sel_idx]; ny = my[sel_idx]
with threadpool_limits(limits=1, user_api='blas'):                                                                               # S6: every production configuration at the selected nodes
    rf_st_n = new_residual(prep, nx, ny); SR_st_n = stateless_condition_sums(prep, nx, ny); rf_s_n = np.empty(len(sel_idx)); SR_s_n = np.empty(len(sel_idx))
    for j, i in enumerate(sel_idx):
        ms, root_s = point_model([mx[i]], [my[i]], workers=1); rf_s_n[j] = float((ms.fun(P, high)/root_s)[0]); SR_s_n[j] = float(ms.condition_sums(P, high)[0]); ms.clear_cache()
for j, i in enumerate(sel_idx):
    ref = H.point_reference(prep, float(mx[i]), float(my[i]), 85, columns=False)['Rf_decimal']
    rec = {'index': i, 'x': float(mx[i]), 'y': float(my[i]), 'r': float(mr[i]), 'band': int(band_id[i]), 'kinds': (['random'] if i in random_idx else [])+[k for k, v in targeted.items() if i in v], 'Rf_decimal_85': format(ref, '.40e')}
    worst_here = 0.
    for path, val, S in (('production_batch', rf_prod_tr[i], S_arr[i]), ('stateless', rf_st_n[j], SR_st_n[j]), ('single', rf_s_n[j], SR_s_n[j])):
        err, den, ratio = bound_ratio(val, S, ref); rec['Rf_'+path] = float(val); rec['S_R_'+path] = float(S); rec['abs_error_'+path] = err; rec['bound_'+path] = den; rec['ratio_'+path] = ratio; worst_here = max(worst_here, ratio)
    rec['ratio_worst'] = worst_here; spot_nodes.append(rec)
    if i in random_idx: worst_random = max(worst_random, worst_here); fails_random += int(not (worst_here <= 1.))
    if i in targeted_idx: worst_targeted = max(worst_targeted, worst_here)
m_eff = N*min(nb[b]/Nb[b] for b in range(len(T27H_BANDS)) if Nb[b] > 0)
out['rf_spot_nodes_v912_v914'] = {'arrays_source': arrays_source, 'training_nodes': N, 'bands': [list(b) for b in T27H_BANDS], 'N_b': Nb, 'n_b': nb, 'allocation': 'n_b = min(N_b, max(2, ceil(32 N_b / N))) (v9.14 ceiling allocation)', 'random_total_requested': RANDOM_TOTAL, 'random_drawn': len(random_idx),
                                   'seed': {'derivation': 'int(sha256(candidate_sha256 string)[:16], 16)', 'candidate_sha256': digest(cand_path), 'value': seed_int}, 'random_indices': sorted(random_idx), 'targeted': targeted, 'nodes': spot_nodes,
                                   'worst_ratio_random': worst_random, 'worst_ratio_targeted': worst_targeted, 'random_failures': fails_random, 'm_eff': m_eff,
                                   'limit_on_failing_fraction_95pct': (1-0.05**(1/m_eff)) if fails_random == 0 else None,
                                   'assumption': 'the 95% statement holds only if the hash-seeded draw behaves as independent uniform sampling without replacement within each band; targeted and fixed nodes are not counted; no bound is claimed at unassessed nodes or states (SPEC v9.14)',
                                   'scientific_stop': bool(not math.isfinite(max(worst_random, worst_targeted)) or max(worst_random, worst_targeted) > 1.), 'configurations': ['production_batch (campaign snapshot arrays when present, else a Model860 training-mesh call)', 'stateless', 'single']}
out['rf_reference_spot_check']['scientific_stop'] = bool(out['rf_reference_spot_check']['scientific_stop'] or out['rf_spot_nodes_v912_v914']['scientific_stop'])
# ---- SPEC v9.11 (3): for c_l < 1.1 report the leading far-field power, the estimated fraction of J beyond the current upper log radius and the log radius needed
# for the 2.5e-15 absolute target. Model: at large r, R_f = R_rho / y ~ r^(alpha - 1) E(theta)/sin(theta) with alpha the actual leading density power, so
# int R_f^2 dtheta ~ r^(2 alpha - 2) Q with Q = ||E/sin||^2 (leading sector quotient norm), and J_tail(R) = Q R^(2 alpha - 2) / ((2 - 2 alpha) pi a_ref^2) when alpha < 1.
ff = out.get('farfield'); lead = ff['actual_leading_density_power'] if ff else {'status': 'not computed (spot_only)', 'exponent': None, 'determined': False}; tail_report = {'applies': bool(cl < 1.1), 'cl': cl, 'leading_power_status': lead['status'], 'leading_density_power': lead['exponent']}
if ff and lead['exponent'] is not None and ff.get('leading_sector_quotient_L2') is not None and lead['exponent'] < 1.:
    alpha = lead['exponent']; Q = ff['leading_sector_quotient_L2']**2; decay = 2.-2.*alpha; S0 = None   # S0 = the upper log radius actually used by the independent integrator (set after the tight integral; v9.13 (c))
    def J_tail(S): return Q*math.exp(-decay*S)/(decay*math.pi*A_REF**2)
    tail_report.update({'Rf_squared_decay_power': -decay, 'log_radius_for_2.5e-15_abs': (math.log(Q/(decay*math.pi*A_REF**2*2.5e-15))/decay if Q > 0 else None), 'leading_power_determined': lead.get('determined'),
                        'note': 'leading-term estimate from the far-field sector sum, not an enclosure; when the leading power is only a candidate this estimate inherits that uncertainty; the integrator envelope (infinity_tail_error_abs of the tight integral) is the production arbiter'})
else: tail_report['note'] = 'no determined decaying leading sector; tail fraction not estimated'
out['tail_report_v911'] = tail_report
if do_integral:
    t0 = time.time(); ii = independent_integral(P, high, workers=workers, target_abs=1e-18, initial_upper_log_radius=44.)
    out['tight_independent_integral'] = {k: ii[k] for k in ('J_abs', 'error_abs', 'origin_tail_error_abs', 'infinity_tail_error_abs', 'radial_quadrature_error_abs', 'angular_quadrature_error_abs', 'accuracy_passed')}; out['tight_independent_integral']['seconds'] = time.time()-t0
    if 'Rf_squared_decay_power' in tail_report:
        S0 = float(ii['interval_expansions'][-1]['s_max']) if ii.get('interval_expansions') else 44.; tail_report['upper_log_radius_used_by_integrator'] = S0; tail_report['J_tail_beyond_integrator_upper_radius'] = J_tail(S0)
        if ii['J_abs']: tail_report['J_tail_fraction_beyond_integrator_upper_radius'] = tail_report['J_tail_beyond_integrator_upper_radius']/ii['J_abs']
    out['J_mesh_minus_J_abs_note'] = 'J_mesh is the campaign state objective (state.json); J_mesh - J_abs is reported by the campaign rows and the cadence ledger at every state with c_l < 4/3 (SPEC v9.11 (3)); here J_abs (tight) = %r' % ii['J_abs']
required = (['rf_reference_spot_check', 'rf_spot_nodes_v912_v914', 'five_Taylor', 'widths'] if SPOT_ONLY else ['origin_truncation_monitor', 'rf_reference_spot_check', 'rf_spot_nodes_v912_v914', 'frozen32_regions', 'frozen32_maxima', 'refined_maxima', 'farfield', 'five_Taylor', 'widths', 'near_origin', 'peak_independent85_checks', 'tight_independent_integral'])      # E7 (b): always required in full mode
missing = [k for k in required if k not in out]
booleans = {'poisson_sector_identity_exact': (out['farfield'].get('poisson_sector_identity_exact') if not SPOT_ONLY else None), 'farfield_strict_json_safe': ((lambda: (json.dumps(out['farfield'], allow_nan=False) is not None))() if not SPOT_ONLY else None), 'peak_independent85_checks_passed': (all(c['passed'] for c in out['peak_independent85_checks']) if not SPOT_ONLY else None),
            'tight_integral_accuracy_passed': ((out.get('tight_independent_integral') or {}).get('accuracy_passed') if not SPOT_ONLY else None), 'widths_finite_or_null_with_reason': all((v is None and k in out['widths']['reasons']) or (isinstance(v, float) and math.isfinite(v)) for k, v in out['widths'].items() if k in ('W_x', 'W_y', 'l', 'eta')),
            'origin_monitor_below_threshold': (not out['origin_truncation_monitor']['scientific_stop']) if not SPOT_ONLY else None, 'rf_spot_check_ratios_le_1': not out['rf_reference_spot_check']['scientific_stop']}
skip_none = set()        # E7 (b): in full mode every check, including tight_integral_accuracy_passed, must be a boolean
if SPOT_ONLY: skip_none |= {'tight_integral_accuracy_passed', 'peak_independent85_checks_passed', 'origin_monitor_below_threshold', 'poisson_sector_identity_exact', 'farfield_strict_json_safe'}
non_boolean = [k for k, v in booleans.items() if not isinstance(v, bool) and not (k in skip_none and v is None)]
false_checks = [k for k, v in booleans.items() if v is False]
out['completeness_v913'] = {'mode': ('spot_only' if SPOT_ONLY else 'full'), 'partial_record_spot_only': SPOT_ONLY, 'is_full_assessment': not SPOT_ONLY, 'required_records': required, 'missing_records': missing, 'checks': booleans, 'non_boolean_checks': non_boolean, 'false_checks': false_checks, 'nonfinite_samples_total': NONFINITE_SAMPLES['count'], 'nonfinite_monitor_inputs': NONFINITE_MONITOR, 'undefined_quotients': UNDEFINED_QUOTIENTS, 'kappa_failure': KAPPA_FAILURE, 'invalid_bound_inputs': INVALID_BOUND_INPUTS, 'exact_zero_bounds': EXACT_ZERO_BOUNDS, 'snapshot_supplied': SNAPSHOT_SUPPLIED, 'snapshot_arrays_binding_failure': ARRAY_BINDING_FAILURE if SNAPSHOT_SUPPLIED else None,
                            'failed_refers_to': ('the spot-only required set %s; this record is NOT a full assessment (mode spot_only, is_full_assessment false) and every consumer refuses it as one' % required) if SPOT_ONLY else 'the full required set',
                            'failed': bool(missing or non_boolean or false_checks or NONFINITE_SAMPLES['count'] > 0 or KAPPA_FAILURE or INVALID_BOUND_INPUTS or (SNAPSHOT_SUPPLIED and ARRAY_BINDING_FAILURE)), 'rule': 'SPEC v9.13 (a): complete only if every required record is present, every check returns a boolean and none is False, and no sample is nonfinite; otherwise failed (STOPPED_FOR_DIAGNOSIS by the cadence)'}
def sanitize(value):
    """E9: no bare NaN/Infinity in the assessment JSON: nonfinite floats become null with a sibling '<key>_nonfinite' classification (dicts) or {'nonfinite': kind}
    (lists); every nonfinite value has already set completeness.failed or a scientific_stop flag above, so the checks still fail on it."""
    if isinstance(value, np.floating): value = float(value)
    if isinstance(value, np.integer): return int(value)
    if isinstance(value, np.bool_): return bool(value)
    if isinstance(value, np.ndarray): value = value.tolist()
    if isinstance(value, float): return value if math.isfinite(value) else None
    if isinstance(value, dict):
        res = {}
        for k, v in value.items():
            if isinstance(v, (float, np.floating)) and not math.isfinite(float(v)): res[k] = None; res[str(k)+'_nonfinite'] = 'nan' if math.isnan(float(v)) else ('+inf' if v > 0 else '-inf')
            else: res[k] = sanitize(v)
        return res
    if isinstance(value, (list, tuple)): return [({'nonfinite': 'nan' if math.isnan(float(v)) else ('+inf' if v > 0 else '-inf')} if isinstance(v, (float, np.floating)) and not math.isfinite(float(v)) else sanitize(v)) for v in value]
    return value
out['import_closure'] = loaded_closure(); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
_tmp = out_path.with_name(out_path.name+'.partial'); _text = json.dumps(sanitize(out), indent=1, default=str, allow_nan=False)+'\n'          # E9 / N10: sanitized, allow_nan=False, fsync, rename
with _tmp.open('w') as _f: _f.write(_text); _f.flush(); os.fsync(_f.fileno())
os.replace(_tmp, out_path)
fm = out.get('frozen32_maxima') or {}; rm = out.get('refined_maxima') or {}; ffE1 = ((ff or {}).get('E') or {}).get('1') or {}; ffL = (ff or {}).get('actual_leading_density_power') or lead    # spot_only: ff is None (lead A(a): exit 0)
print(json.dumps({'spot_only': SPOT_ONLY, 'E_f_frozen': (fm.get('E_f') or {}).get('value'), 'E_rho_frozen': (fm.get('E_rho') or {}).get('value'), 'E_f_refined': (rm.get('E_f') or {}).get('value'), 'E_rho_refined': (rm.get('E_rho') or {}).get('value'), 'E1_L2': ffE1.get('L2'), 'E1_unresolved_fraction': ffE1.get('unresolved_fraction'), 'leading_power': ffL.get('exponent'), 'leading_status': ffL.get('status'), 'mode': out['completeness_v913']['mode'], 'spot_worst_ratio': out['rf_reference_spot_check']['worst_ratio'], 'nodes_worst_ratio': max(out['rf_spot_nodes_v912_v914']['worst_ratio_random'], out['rf_spot_nodes_v912_v914']['worst_ratio_targeted']), 'm_eff': out['rf_spot_nodes_v912_v914']['m_eff'], 'failed': out['completeness_v913']['failed'], 'J_abs': out.get('tight_independent_integral', {}).get('J_abs')}), flush=True)
