"""860-generator absolute-loss campaign (T1 coordinates): durable, restartable, guarded slices. SPEC sections 11, 13, 14, 15, 16 (v9.3 to v9.8);
lead pre-audit c4-lead/reviews/lead_campaign860_preaudit.md findings F1 to F22, SPEC v9.11 (bound logging, boundary states) and SPEC v9.12 (a) to (l)
(fsum objective, root-weight check h, acceptance d(1-2^-51) > (T_ref+T_trial)(1+2^-40) with T = B + 2^-51 J, underflow stop, mandatory validated kappa file bound
in the manifest, thread/worker lock, rejection prefixes, NaN-safe KKT, stationarity recomputed at the accepted state, lift diagnostics, committed stops at
initialization, assessment gate) implemented (version 3 of this driver).

Unchanged semantics from stage13_campaign_v3 (column scales fixed per epoch, full thin SVD trust step, KKT and precision-floor stops,
feasible_trial reasons lift/C5/bound/a0/nonfinite with radius x0.25, acceptance rules, radius rules, 12-rejection and stationarity stops).
Added by SPEC v9.3 section 11: the exceptional-parameter stop (|c_l/2 - 1| < 2^-30 or |c_l/3 - 1| < 2^-30 after an acceptance or before an
epoch start; a zero or nonfinite column norm at an epoch start), the epoch-start record (column norms over seed norms, three smallest scaled
singular values) and the rounding bound in acceptance (S_R condition sums from the production path, e_i = root_i kappa u S_R + 2^-53 |r_i|,
E = ||e||, B = sqrt(2J) E + E^2/2; acceptance needs decrease > B_ref + B_trial; 2 B_ref > 5% of the prediction stops the run).

Durable records (commits/ is the only authority; state.json is a cache of the last commit's post_state):
  slice_start, trial, scientific_stop, scientific_stop_override, slice_end and slice_interrupted events with the full post_state (F4, F18);
  proposals before validation with incumbent binding and radius_before (F1); immutable outcomes with decision_only: true (F19);
  reconciliation: every proposal visited, commitment decided from commit-bound sha256 only, orphans get interrupted outcomes, outcomes written
  but not committed get a separate reconciliation record (F1, F19); trajectory.jsonl rebuilt atomically from commits/ (F9, F20);
  per-slice binding verification of manifest files, frozen closure, loaded import closure and protected source (F2); epoch and mesh binding
  on recovery (F13); column-scale hash binding (F6); STOPPED_FOR_DIAGNOSIS refusal and recorded override (F5, F10); single heartbeat writer
  thread fed from a locked snapshot, unique temporary names, heartbeat failures never end the run (F7, F21); one sanitizer for every durable
  write: a nonfinite float becomes null with a sibling classification (F16, F22); slice-completion record bound to the guard run id (F12).
Nonfinite handling (F16/F22, stated): Jacobian or step entries that are not finite are process faults (logged with the phase, slice ends
abnormally, exit 3); a nonfinite predicted decrease is the committed precision-floor stop with its classification (SPEC 11); a nonfinite trial
residual or trial objective is detected explicitly before any comparison and is the documented 'nonfinite' rejection of SPEC 11 (radius x0.25),
not a process fault (lead ruling 07:5xZ: SPEC 11 wins over the F16 wording; nonfinite Jacobian or step entries at the incumbent stay process faults, and the fault record names the phase and the first nonfinite location).
Usage: campaign860.py --root <dir> --seed-json <seed> --seed-npz <replay npz> --manifest <code_manifest.json> --kappa-file F --seconds S --workers W
       [--resume] [--initial-radius R] [--max-trials N] [--reserve-seconds R] [--threads T] [--config-change-reason TXT] [--skip-assessment-gate]
       [--override-stop --override-reason TXT --release-ref PATH:SHA]
Exit codes (S7): 0 slice ended with a committed slice_end (any status, scientific stops included); 3 process fault (slice ended abnormally); 4 refusal before any
slice work (scientific stop state without release, STOPPED_FOR_DIAGNOSIS present, assessment due, release reference mismatch, kappa/binding refusal). Paired supervisor:
bin/supervise860_v3.sh (reads slice_completion/slice_<n>_<run_id>.json; passes its own sha256 in SUPERVISOR_SHA256, recorded in slice_start).
"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import argparse, hashlib, json, math, os, resource, signal, sys, tempfile, threading, time, traceback
from pathlib import Path
import numpy as np
import psutil
HERE = Path(__file__).resolve().parent; LANE = HERE.parents[1]
import basis860 as B, chart860 as C
from model860 import Model860, feasible_matrix
from integrate860 import Integrator860
from closure860 import loaded_closure
from widths860 import widths
from kappa860 import load_kappa as load_kappa_file
from absolute_common import ROOT, A_REF, read, npz, digest, array_hash, provenance
from absolute_model import FrozenLogMesh
from stage13_solver import DenseTrustModel
sys.path.insert(0, str(HERE.parent/'tools')); from runtime import Runtime
IMPORT_CLOSURE = loaded_closure()          # SPEC v9.13 (f): sha256 of every loaded module, read immediately after import; recomputed at slice end
RT = Runtime(str(HERE.parent))             # S1: every handoff-derived record (state.json, epoch.json) is read through Runtime, which translates the source-host paths
EXIT_REFUSAL = 4

VERSION = 'campaign860_v3_F1_F22_spec_v916'
STOP = False
PHASE = {'phase': 'startup', 'trial': None}
U_RF = 2.**-64                 # unit roundoff of the extended R_f path (SPEC v9 clause (a))
EXCEPTIONAL_WINDOW = 2.**-30   # SPEC v9.3 section 11
SCIENTIFIC_STOPS = ('full_matrix_trust_subproblem_inaccuracy_requires_diagnosis', 'model_reduction_at_precision_floor', 'needs_mesh_refinement',
                    'trust_obstruction_requires_diagnosis', 'needs_independent_stationarity_verification', 'exceptional_parameter_requires_rank_treatment', 'assessment_scientific_stop', 'frozen_code_changed_requires_diagnosis')
REJECTION_PREFIXES = ('lift:', 'C5:', 'bound:', 'a0:', 'nonfinite:')     # SPEC v9.12 (f): the only trial rejections; anything else is a process fault
V64 = 2.**-53                                                                # binary64 unit roundoff
PI50 = '3.14159265358979323846264338327950288419716939937510'

def objective(r):
    """SPEC v9.12 (a): J = 0.5 fsum(r_i^2), exactly rounded sum."""
    return 0.5*math.fsum(np.multiply(np.asarray(r, float), np.asarray(r, float)).tolist())


class PrecisionFloorStop(Exception):
    """C18 / v9.15 (4): the trial objective is exactly zero or below 1e-250 (or the incumbent objective is): the model_reduction_at_precision_floor stop is committed BEFORE
    validation and acceptance; the incumbent candidate, objective and accepted count stay unchanged and no accepted_* snapshot is written."""
    def __init__(self, trial_objective): super().__init__('precision floor'); self.trial_objective = trial_objective

class ProcessFault(RuntimeError):
    """F16: a nonfinite Jacobian/step/objective or any other implementation fault; ends the slice abnormally (never a trial rejection)."""

def request_stop(signum, frame):
    global STOP; STOP = True

def guard_run_id():
    run = os.environ.get('IPM_RESOURCE_RUN'); return os.path.basename(run) if run else None

# ---------------- F16/F22: one sanitizer for every durable write ----------------
def _classify(v): return 'nan' if math.isnan(v) else ('+inf' if v > 0 else '-inf')

def durable(value):
    """Recursively map nonfinite floats to null with a sibling classification (dicts) or a {'nonfinite': kind} element (lists)."""
    if isinstance(value, (np.floating,)): value = float(value)
    if isinstance(value, (np.integer,)): return int(value)
    if isinstance(value, np.bool_): return bool(value)
    if isinstance(value, np.ndarray): value = value.tolist()
    if isinstance(value, float): return value if math.isfinite(value) else None
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            if isinstance(v, (float, np.floating)) and not math.isfinite(float(v)): out[str(k)] = None; out[str(k)+'_nonfinite'] = _classify(float(v))
            else: out[str(k)] = durable(v)
        return out
    if isinstance(value, (list, tuple)):
        return [({'nonfinite': _classify(float(v))} if isinstance(v, (float, np.floating)) and not math.isfinite(float(v)) else durable(v)) for v in value]
    return value

def atomic_write(path, value):
    """F21: unique temporary name in the target directory, fsync, atomic replace; value sanitized (F22)."""
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name+'.', suffix='.partial', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump(durable(value), stream, indent=2, allow_nan=False, default=str); stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
        os.replace(tmp, path)
    except BaseException:
        try: os.unlink(tmp)
        except OSError: pass
        raise

def append(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a') as stream: stream.write(json.dumps(durable(value), allow_nan=False, default=str)+'\n'); stream.flush(); os.fsync(stream.fileno())

def sha_file(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

# ---------------- F2: binding verification ----------------
def verify_binding(manifest_path, directory, slice_number, check_source=True):
    m = json.loads(Path(manifest_path).read_text()); bad = []
    for row in m['files']+m.get('frozen_181_closure', []):
        p = LANE/row['path']; h = sha_file(p) if p.exists() else None
        if h != row['sha256']: bad.append(row['path'])
    manifest_paths = {row['path'] for row in m['files']}|{row['path'] for row in m.get('frozen_181_closure', [])}
    closure = loaded_closure(); not_in_manifest = [rel for rel in closure['files'] if ('work/'+rel) not in manifest_paths and rel not in manifest_paths]
    source_ok = None; source_mismatch = []
    if check_source:
        src_root = Path((__import__("os").environ["IPM_SOURCE_REALPATH"]))
        for line in (LANE/'outputs/integrity/source_before.sha256').read_text().splitlines():
            h, rel = line.split(None, 1); rel = rel.strip(); p = src_root/rel[2:] if rel.startswith('./') else src_root/rel
            if not p.exists() or sha_file(p) != h: source_mismatch.append(rel)
        source_ok = not source_mismatch
    record = {'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'slice': slice_number, 'manifest': str(manifest_path), 'manifest_sha256': sha_file(manifest_path),
              'manifest_files_verified': not bad, 'mismatched': bad, 'loaded_closure_count': closure['count'], 'loaded_not_in_manifest': not_in_manifest,
              'protected_source_verified': source_ok, 'protected_source_mismatch': source_mismatch, 'guard_run_id': guard_run_id(), 'driver_version': VERSION}
    vdir = directory/'verifications'; vdir.mkdir(parents=True, exist_ok=True); path = vdir/('slice_%04d_%d.json' % (slice_number, time.time_ns()))
    atomic_write(path, record); record['record_path'] = str(path); record['record_sha256'] = digest(path)
    if bad or not_in_manifest or (check_source and not source_ok):
        raise RuntimeError('binding verification failed: mismatched=%s loaded_not_in_manifest=%s source_ok=%s (record %s)' % (bad, not_in_manifest, source_ok, path))
    return record

def epoch_record():
    state = RT.read(ROOT/'campaign/global181_v3/state.json'); return RT.read(state['epoch_path']), state

def resources():
    pr = psutil.Process(); ru = resource.getrusage(resource.RUSAGE_SELF); rc = resource.getrusage(resource.RUSAGE_CHILDREN)
    return {'rss_mib': pr.memory_info().rss/2**20, 'peak_rss_mib': ru.ru_maxrss/1024, 'peak_rss_children_mib': rc.ru_maxrss/1024, 'cpu_seconds': ru.ru_utime+ru.ru_stime+rc.ru_utime+rc.ru_stime, 'cpu_seconds_self': ru.ru_utime+ru.ru_stime, 'cpu_seconds_children_terminated': rc.ru_utime+rc.ru_stime, 'epoch': time.time()}   # S8/N13: children included (terminated children only; live pool workers are reported by the guard)

MODEL_NONFINITE = 'Nonfinite residual/Jacobian'      # the exact message model860.Model860 raises inside fun/jacobian (frozen module)

def locate_nonfinite(P, high, mesh, derivatives):
    """S2: a non-raising stateless evaluation to name the first nonfinite entry after Model860 raised; block by block, stops at the first hit."""
    from fields860 import residual as stateless_residual
    x, y = mesh.coordinates(); prepared = B.prepare(float(P[0]), np.asarray(P[1:], float), np.asarray(high, float)); bs = 4096
    for lo in range(0, len(x), bs):
        hi = min(len(x), lo+bs)
        try:
            if derivatives:
                rf, dr = stateless_residual(prepared, x[lo:hi], y[lo:hi], derivatives=True)
                badc = np.argwhere(~np.isfinite(dr))
                if len(badc): i, j = badc[0]; return {'kind': 'jacobian', 'node': int(lo+i), 'column': int(j), 'x': float(x[lo+i]), 'y': float(y[lo+i]), 'value': _classify(float(dr[i, j]))}
            else: rf = stateless_residual(prepared, x[lo:hi], y[lo:hi])
            bad = np.flatnonzero(~np.isfinite(rf))
            if len(bad): i = int(bad[0]); return {'kind': 'residual', 'node': int(lo+i), 'x': float(x[lo+i]), 'y': float(y[lo+i]), 'value': _classify(float(rf[i]))}
        except Exception as exc: return {'kind': 'locator_failed', 'block_start': lo, 'error': type(exc).__name__+': '+str(exc)}
    return {'kind': 'not_found_by_stateless_evaluation', 'note': 'the stateless provider returned finite values on every node; the fault came from the cached Model860 path'}

def model_call(fn, P, high, mesh, phase, derivatives):
    """S2: call model.fun/model.jacobian; Model860's ValueError('Nonfinite residual/Jacobian') becomes a ProcessFault naming the first nonfinite location."""
    try: return fn(P, high)
    except ValueError as exc:
        if str(exc).startswith(MODEL_NONFINITE):
            loc = locate_nonfinite(P, high, mesh, derivatives); raise ProcessFault('phase %s: %s: first nonfinite entry %s' % (phase, str(exc), json.dumps(durable(loc)))) from exc
        raise

def exceptional_parameter(cl):
    """SPEC v9.3 section 11: within relative 2^-30 of 2 or 3."""
    return bool(abs(cl/2.-1.) < EXCEPTIONAL_WINDOW or abs(cl/3.-1.) < EXCEPTIONAL_WINDOW)

# ---------------- F15: exact canonical export ----------------
def canonical_exact(P, high, hp, digits=50):
    """Canonical a from the exact rational checkpoint (exactcheckpoint860: Fraction c_l, Fraction P/high, a_000 by the rational center relation, exact N_n and Legendre
    integers); returned as Decimals rounded to `digits` significant digits at the end, with the exact record (D3 (f))."""
    from decimal import Decimal, localcontext
    from exactcheckpoint860 import exact_canonical
    a, rec = exact_canonical(P, high)
    with localcontext() as ctx:
        ctx.prec = digits; return [+(Decimal(x.numerator)/Decimal(x.denominator)) for x in a], rec

def export_candidate(P, high, state, tag, hp):
    a, xrec = canonical_exact(P, high, hp, 50); w = widths(hp)
    return {'schema': 'candidate_860_T1_v3', 'label': tag, 'cl': float(P[0]), 'P_raw_chart': P.tolist(), 'P_hex': [float(v).hex() for v in P],
            'high_internal': high.tolist(), 'high_hex': [float(v).hex() for v in high], 'a000_analytic_decimal': hp['coefficients_decimal'][0],
            'center_convention': 'analytic center elimination: a_000 = (1 - c_l - sum_{i>=1} s_i a_i)/s_0; the P/high state with this relation is the authoritative state; a_canonical_decimal50 is the exact rational checkpoint rounded to 50 digits at the end (F15, D3 (f))', 'input_exact_for_checkpoint': xrec,
            'a_canonical_decimal50_rounded': [format(v, '.49e') if v else '0' for v in a], 'a_canonical_decimal50_rounded_note': 'the exact rational checkpoint (input_exact_for_checkpoint) rounded to 50 significant digits; the P/high state is authoritative', 'a_canonical_float_display_only': [float(v) for v in a],
            'a_canonical_float_note': 'binary64 display values of the Decimal canonical coefficients; rounding a_000 to binary64 leaves a center defect of order 1e-16 (verifier F15), so these are not the authoritative state',
            'canonical_order': 'I(j,m,k)=215j+26m-m(m-1)/2+(k-m)', 'basis_version': B.VERSION, 'T_version': '860-T1', 'frozen_Nn_hex': [float(v).hex() for v in B.NN],
            'a0': hp['a0'], 'five_Taylor': hp['constraints'], 'five_Taylor_max': hp['max_abs'], 'widths': w,
            'objectives': {'J_abs_mesh': state['objective'], 'J_abs_independent': state['validation']['J_abs'], 'integration_error_diagnostic': state['validation']['error_abs']},
            'rounding_bound': state.get('rounding_bound'), 'feasible_variables': 855, 'generators': 860, 'accepted_trials': state['accepted'], 'total_trials': state['trials'],
            'seed_sha256': state['seed_sha256'], 'code_manifest_sha256': state['code_manifest_sha256'], 'driver_version': VERSION, 'no_weak_directions_removed': True, 'not_an_exact_PDE_solution': True}

def snapshot(directory, state, P, high, r, tag, hp, **extra_arrays):
    folder = directory/'snapshots'; folder.mkdir(parents=True, exist_ok=True); cpath = folder/(tag+'.json'); apath = folder/(tag+'.npz')
    if cpath.exists() or apath.exists():
        tag = tag+'_uncommitted_retry_'+str(time.time_ns()); cpath = folder/(tag+'.json'); apath = folder/(tag+'.npz')
    npz(apath, P=P, high=high, residual=r, mesh_fingerprint=np.array(str(state.get('mesh_sha256'))), configuration_json=np.array(json.dumps({'workers': int(state['workers']), 'cache_threads': int(state.get('cache_threads') or 1), 'block_size': BLOCK_SIZE, 'mode_block': MODE_BLOCK}, sort_keys=True)), **extra_arrays)   # D6: the artifact carries its own state, mesh and configuration
    case = export_candidate(P, high, state, tag, hp); case['snapshot_arrays_path'] = str(apath); case['snapshot_arrays_sha256'] = digest(apath); atomic_write(cpath, case)
    return str(cpath), str(apath)

def proposal_snapshot(directory, state, P, high, r, step, scales, hp):
    folder = directory/'trial_proposals'; folder.mkdir(parents=True, exist_ok=True)
    tag = 'trial_'+str(state['trials']).zfill(8)+'_'+str(time.time_ns()); arrays = folder/(tag+'.npz'); rec = folder/(tag+'.json')
    npz(arrays, P=P, high=high, residual=r, scaled_coordinate_step=step, column_scales=scales)
    record = {'schema': 'trial_proposal_860_v3', 'trial': state['trials'], 'status': 'unvalidated', 'accepted_incumbent': False, 'arrays_path': str(arrays), 'arrays_sha256': digest(arrays),
              'P_sha256': array_hash(P), 'high_sha256': array_hash(high), 'residual_sha256': array_hash(r), 'mesh_J_abs': objective(r), 'five_Taylor_max': hp['max_abs'], 'cl': float(P[0]), 'a0': hp['a0'],
              'base_candidate_sha256': state['candidate_sha256'], 'base_arrays_sha256': state['arrays_sha256'], 'radius_before': state['radius'], 'slice': state['slices'], 'guard_run_id': guard_run_id(), 'created_epoch': time.time(),
              'commitment': 'defined only by a commit row that binds this record_sha256 (complete_trial_proposal); file existence decides nothing (F19)'}
    atomic_write(rec, record); return {'record_path': str(rec), 'record_sha256': digest(rec), 'arrays_path': str(arrays), 'arrays_sha256': digest(arrays)}

def commit(directory, state, row):
    """Event commit: the commit file is the authority; state.json is rewritten as a cache; trajectory.jsonl is a derived log (F9/F20)."""
    state['events'] = state.get('events', 0)+1; row['event_sequence'] = state['events']; row.setdefault('guard_run_id', guard_run_id()); row.setdefault('driver_version', VERSION); row.setdefault('code_manifest_sha256', state.get('code_manifest_sha256'))   # v9.13 (e)
    path = directory/'commits'/('event_'+str(state['events']).zfill(8)+'.json')
    if path.exists(): raise ValueError('Immutable trial commit collision')
    atomic_write(path, {'trial': row, 'post_state': state}); atomic_write(directory/'state.json', state); append(directory/'trajectory.jsonl', row)

def actual_matrix_kkt(A, r, step, sub):
    mu = sub.get('lagrange_multiplier')
    if mu is None or not np.isfinite(float(mu)): sub['kkt_value_classification'] = 'nonfinite multiplier (%r)' % (mu,); return float('nan')     # S4: v9.12 (g) stop, not a fault
    response = A@step; gradient = A.T@r; rg = A.T@response
    scale = max(np.linalg.norm(gradient), np.linalg.norm(rg), mu*np.linalg.norm(step), 1e-300)
    return float(np.linalg.norm(gradient+rg+mu*step)/scale)

LOW_BOX = 100.
def feasible_trial(chart, P, high, step, scales):
    phys = step*scales
    seed_pt = np.asarray(chart.base, float)+np.asarray(chart.free, float)@phys[:55]                                                      # S3: the uncorrected trial point, before the chart's own bound check
    if not np.all(np.isfinite(seed_pt)): raise ValueError('nonfinite: uncorrected trial point')
    if seed_pt[0] < 1.02: raise ValueError('bound: lower c_l (%.17g < 1.02, uncorrected trial point)' % seed_pt[0])
    if seed_pt[0] > 10.: raise ValueError('bound: upper c_l (%.17g > 10, uncorrected trial point)' % seed_pt[0])
    if np.any(abs(seed_pt[1:]) > LOW_BOX): raise ValueError('bound: low coefficient (|a_i| > %g at the uncorrected trial point)' % LOW_BOX)
    try: Pp = chart.lift_delta(phys[:55])
    except (ValueError, np.linalg.LinAlgError) as exc: raise ValueError('lift: '+type(exc).__name__+': '+str(exc))
    hh = high+phys[55:]
    if not np.all(np.isfinite(hh)) or not np.all(np.isfinite(Pp)): raise ValueError('nonfinite: trial coordinates')
    hp = C.hp_report(Pp)
    if hp['max_abs'] >= 1e-10: raise ValueError('C5: max defect %.3e' % hp['max_abs'])
    a000 = float(hp['coefficients_decimal'][0])
    if not math.isfinite(a000): raise ValueError('nonfinite: eliminated a_000')
    if Pp[0] < 1.02: raise ValueError('bound: lower c_l (%.17g < 1.02)' % Pp[0])                                   # SPEC v9.11 (1): which bound
    if Pp[0] > 10.: raise ValueError('bound: upper c_l (%.17g > 10)' % Pp[0])
    if not hp['physical_bounds'] or np.any(abs(Pp[1:]) > LOW_BOX): raise ValueError('bound: low coefficient (chart box or |a_i| <= %g on the 59 free low coefficients, SPEC v6 section 7)' % LOW_BOX)
    if abs(hp['a0']) <= 1e-12: raise ValueError('a0: |a0| <= 1e-12')
    hp['a000_float'] = a000; return Pp, hh, hp

def predicted_responses(chart, P, step, scales):
    """F8: chart-predicted physical responses of the linearized map applied to the saved step."""
    dP = chart.base_tangent@(step*scales)[:55]; Plin = P+dP
    try: hp = C.hp_report(Plin); w = widths(hp); return {'cl': float(Plin[0]), 'a0': hp['a0'], 'W_x': w['W_x'], 'W_y': w['W_y'], 'linearized_point_C5_max': hp['max_abs']}
    except Exception as exc: return {'error': str(exc)}

BLOCK_SIZE = 4096; MODE_BLOCK = 64      # production Model860 configuration constants (recorded in every snapshot artifact, D6)
def make_model(mesh, workers, threads=1): return Model860(mesh, A_REF, block_size=BLOCK_SIZE, mode_block=MODE_BLOCK, workers=workers, threads=threads)

# ---------------- SPEC v9.3 section 11: rounding bound ----------------
def load_kappa(args):
    """SPEC v9.12 (d) / v9.15 (4): validated kappa file (kappa860.load_kappa); the development fallback is removed."""
    return load_kappa_file(args.kappa_file, args.manifest)

def root_weight_check(model):
    """SPEC v9.12 (b): compare alpha_i = sqrt(2 w_i / (pi a_ref^2)) (model.root) with a 40-digit Decimal evaluation; h = max relative difference, must be <= 8 v."""
    from decimal import Decimal, localcontext
    w = np.asarray(model.mesh.weights, float); root = np.asarray(model.root, float); h = 0.
    with localcontext() as cx:
        cx.prec = 40; pi = Decimal(PI50); a2 = Decimal(A_REF)*Decimal(A_REF)
        for i in range(len(w)):
            alpha = (2*Decimal(float(w[i]))/(pi*a2)).sqrt(); rel = abs(Decimal(float(root[i]))-alpha)/alpha
            if rel > h: h = float(rel)
    rec = {'h': h, 'bound_8v': 8*V64, 'nodes': int(len(w)), 'digits': 40, 'passed': bool(h <= 8*V64)}
    if not rec['passed']: raise ProcessFault('phase initialize: root weights differ from the 40-digit evaluation by %.3e > 8v' % h)
    return rec

def rounding_bound(model, P, g, r, kappa, h):
    """SPEC v9.3/v9.12: e_i = root_i kappa u S_R(X_i) + (2^-53 + h + 2 v)|r_i|; E = sqrt(fsum(e^2)); J = objective(r); B = sqrt(2J) E + E^2/2; C = 2^-51 J; T = B + C.
    Returns (record, S_R, e). Nonfinite -> ValueError('nonfinite: rounding bound')."""
    S = np.asarray(model.condition_sums(P, g), float); r = np.asarray(r, float); e = np.asarray(model.root, float)*(kappa*U_RF*S)+(V64+h+2*V64)*abs(r)
    E = math.sqrt(math.fsum(np.multiply(e, e).tolist())); J = objective(r); Bv = math.sqrt(2*J)*E+E*E/2; Cv = 2.**-51*J
    if not (np.all(np.isfinite(S)) and math.isfinite(E) and math.isfinite(Bv) and math.isfinite(Cv)): raise ValueError('nonfinite: rounding bound')
    return {'E': E, 'B': Bv, 'C': Cv, 'T': Bv+Cv, 'J': J, 'kappa': kappa, 'u': U_RF, 'h': h, 'S_R_max': float(np.max(S)), 'S_R_norm': float(np.linalg.norm(np.asarray(model.root, float)*S)), 'definition': 'SPEC v9.3 section 11 indicator with the v9.12 arithmetic (fsum, root-weight term h, C = 2^-51 J); not a rigorous bound'}, S, e

# ---------------- F7/F21: single heartbeat writer ----------------
HB_LOCK = threading.Lock(); HB_SNAP = {}; HB_STOP = threading.Event(); HB_INTERVAL = 60.     # seconds between heartbeat writes (F7: <= 60 s); tests may shorten it
def hb_update(**fields):
    with HB_LOCK: HB_SNAP.update(fields)

def write_heartbeat(directory, note=None):
    with HB_LOCK: snap = dict(HB_SNAP)
    try: atomic_write(directory/'HEARTBEAT.json', {**snap, 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'epoch': time.time(), 'pid': os.getpid(), 'phase': PHASE['phase'], 'phase_trial': PHASE['trial'], 'note': note if note is not None else snap.get('note'), 'guard_run_id': guard_run_id()})
    except Exception: pass                                                   # F21: a heartbeat failure never ends the run

def heartbeat_thread(directory):
    def loop():
        while not HB_STOP.is_set():
            write_heartbeat(directory); HB_STOP.wait(HB_INTERVAL)
    t = threading.Thread(target=loop, daemon=True, name='heartbeat'); t.start(); return t

def hb_state(state):
    hb_update(trials=state.get('trials'), accepted=state.get('accepted'), objective=state.get('objective'), J_abs_independent=(state.get('validation') or {}).get('J_abs'), radius=state.get('radius'), status=state.get('status'), slice=state.get('slices'))

def epoch_start_record(A, scales, factors, seed_norms):
    """SPEC v9.3 section 11: column norms over their seed-epoch norms and the three smallest scaled singular values at every epoch start."""
    norms = np.linalg.norm(A, axis=0)/scales          # A carries the scales; unscaled norms = ||A_j|| / scale_j
    ratio = norms/seed_norms; s = np.sort(np.asarray(factors.s, float))
    return {'column_norm_over_seed_norm_min': float(np.min(ratio)), 'column_norm_over_seed_norm_max': float(np.max(ratio)), 'column_norm_over_seed_norm_argmin': int(np.argmin(ratio)), 'column_norm_over_seed_norm_argmax': int(np.argmax(ratio)),
            'three_smallest_scaled_singular_values': s[:3].tolist(), 'largest_scaled_singular_value': float(s[-1]), 'all_norms_finite_positive': bool(np.all(np.isfinite(norms)) and np.all(norms > 0))}

def initialize(args, directory, verification, kappa):
    PHASE['phase'] = 'initialize'
    seed = json.loads(Path(args.seed_json).read_text()); sd = np.load(args.seed_npz)
    P = sd['P'].copy(); high = sd['high'].copy(); r_seed = sd['residual'].copy()
    if seed['P_raw_chart_hex'] != [float(v).hex() for v in P] or seed['high_hex'] != [float(v).hex() for v in high]: raise ValueError('seed json/replay npz disagree')
    epoch, old_state = epoch_record(); mesh = FrozenLogMesh.load(epoch['meshes']['training']['path'])
    model = make_model(mesh, args.workers, args.threads); r = model_call(model.fun, P, high, mesh, 'initialize', False)
    if not np.all(np.isfinite(r)): bad = int(np.flatnonzero(~np.isfinite(r))[0]); raise ProcessFault('phase initialize: nonfinite seed residual: first at node %d, value %s' % (bad, _classify(float(r[bad]))))
    diff = np.linalg.norm(r-r_seed); tol = 64*np.finfo(float).eps*max(np.linalg.norm(r), np.linalg.norm(r_seed), 1e-300)
    if not (math.isfinite(diff) and math.isfinite(tol) and diff <= tol): raise ValueError('Seed residual did not replay under 64 eps on this host (or nonfinite): %r > %r' % (diff, tol))   # S8
    rootcheck = root_weight_check(model)                                                                                          # v9.12 (b)
    pending_stop = None
    if exceptional_parameter(P[0]): pending_stop = ('exceptional_parameter_requires_rank_treatment', 'exceptional', {'cl': float(P[0]), 'reason': 'seed c_l within relative 2^-30 of 2 or 3 (SPEC v9.3 section 11; committed stop per v9.12 (k))'})
    PHASE['phase'] = 'jacobian'; chart = C.Chart860(P); J = model_call(model.jacobian, P, high, mesh, 'jacobian', True)
    if not np.all(np.isfinite(J)): bad = np.argwhere(~np.isfinite(J))[0]; raise ProcessFault('phase jacobian: nonfinite seed Jacobian: first at row %d column %d, value %s' % (bad[0], bad[1], _classify(float(J[tuple(bad)]))))
    try: A, scales = feasible_matrix(J, chart)
    except ValueError as exc:
        A = None; scales = np.ones(B.NFEASIBLE_CLAIMED)
        if pending_stop is None: pending_stop = ('exceptional_parameter_requires_rank_treatment', 'column', {'cl': float(P[0]), 'reason': str(exc)+' (committed stop per v9.12 (k))'})
    del J
    bound, S_seed, e_seed = rounding_bound(model, P, high, r, kappa['kappa'], rootcheck['h'])
    PHASE['phase'] = 'validation'; integ = Integrator860(epoch, workers=args.workers); validation = integ.validate(P, high, coarse_r=r, predicted_reduction=None, reference=None)
    if not validation['accuracy_passed']: raise ValueError('Initial whole-axis validation failed')
    hp = C.hp_report(P)
    state = {'schema': 'campaign_860_T1_v3', 'driver_version': VERSION, 'label': args.label, 'root': str(directory), 'P': P.tolist(), 'high': high.tolist(),
             'seed_json': str(Path(args.seed_json).resolve()), 'seed_sha256': digest(args.seed_json), 'seed_npz': str(Path(args.seed_npz).resolve()), 'seed_npz_sha256': digest(args.seed_npz),
             'code_manifest': str(Path(args.manifest).resolve()), 'code_manifest_sha256': digest(args.manifest), 'verification': verification,
             'epoch_path': RT.translate(str(old_state['epoch_path'])), 'epoch_path_as_recorded_in_handoff': str(old_state['epoch_path']), 'epoch_sha256': old_state['epoch_sha256'], 'mesh_sha256': mesh.fingerprint, 'refined_mesh_sha256': epoch['meshes']['refined']['fingerprint'],
             'column_scales_sha256': array_hash(scales), 'seed_column_norms_sha256': array_hash(1/scales), 'feasible_variables': 855, 'workers': args.workers, 'cache_threads': args.threads,
             'objective': objective(r), 'initial_objective': objective(r), 'validation': validation, 'rounding_bound': bound, 'kappa': kappa, 'root_weight_check': rootcheck,
             'seed_replay': {'difference_norm': float(diff), 'tolerance': float(tol), 'bitwise': bool(diff == 0)},
             'radius': float(args.initial_radius or .5*np.linalg.norm(r)), 'radius_reason': 'explicit --initial-radius' if args.initial_radius else 'baseline default 0.5*||r||',
             'accepted': 0, 'rejected': 0, 'trials': 0, 'events': 0, 'consecutive_rejections': 0, 'cl_bound_rejections_total': 0, 'cl_bound_rejections_consecutive': 0, 'recent_trial_kinds': [], 'slices': 0, 'elapsed_worker_seconds': 0., 'solver_cpu_seconds': 0., 'interrupted_seconds': 0., 'iteration_wall_max_seconds': 0.,
             'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'started_epoch': time.time(), 'last_epoch': time.time(), 'status': 'running', 'a_ref': A_REF,
             'widths_history': [widths(hp)], 'reference_epoch': 'Linux host reference (SPEC v7 section 5a / v9 / v9.3): %s' % Path(args.seed_npz).name, 'stationarity_independently_verified': False, 'last_assessed_J_abs': None}
    state['replay_reference_file'] = B.REPLAY_REFERENCE_FILE; state['seed_npz_is_replay_reference'] = bool(Path(B.REPLAY_REFERENCE_FILE).exists() and digest(args.seed_npz) == digest(B.REPLAY_REFERENCE_FILE))
    cpath, apath = snapshot(directory, state, P, high, r, 'initial', hp, S_R=S_seed, e=e_seed)
    state.update(candidate_path=cpath, arrays_path=apath, candidate_sha256=digest(cpath), arrays_sha256=digest(apath))
    npz(directory/'coordinate_map.npz', column_scales=scales, initial_core_tangent=chart.base_tangent)         # F6: the map is durable before the initial commit
    state['coordinate_map_sha256'] = digest(directory/'coordinate_map.npz')
    commit(directory, state, {'kind': 'initialization_from_seed', 'accepted': False, 'seed_replay': state['seed_replay'], 'epoch': time.time(), 'environment': provenance(),
                              'code_manifest_sha256': state['code_manifest_sha256'], 'verification_sha256': verification['record_sha256'], 'slice': 0, 'rounding_bound': bound, 'kappa': kappa, 'root_weight_check': rootcheck})
    if pending_stop is not None:
        scientific_stop(directory, state, pending_stop[0], pending_stop[1], pending_stop[2], {'code_manifest_sha256': state['code_manifest_sha256'], 'verification_sha256': verification['record_sha256'], 'slice': 0, 'epoch': time.time()})
        return state, model, integ, r, scales, None
    return state, model, integ, r, scales, (chart, A)

def rebuild_trajectory(directory, commits):
    """F20: the complete trajectory from commits/ in event order, written to a unique temporary file, fsynced and replaced atomically."""
    traj = directory/'trajectory.jsonl'; rows = [json.loads(c.read_text())['trial'] for c in commits]
    new_bytes = ''.join(json.dumps(durable(row), allow_nan=False, default=str)+'\n' for row in rows).encode()
    result = {'rows': len(rows), 'replaced': False, 'damaged_copy': None, 'damaged_sha256': None, 'previous_state': 'absent'}
    if traj.exists():
        old = traj.read_bytes()
        if old == new_bytes: result['previous_state'] = 'identical'; return result
        parsed = []; ok = True
        for line in old.decode(errors='replace').splitlines():
            try: parsed.append(json.loads(line).get('event_sequence'))
            except Exception: ok = False; break
        if ok and parsed == [row.get('event_sequence') for row in rows][:len(parsed)]: result['previous_state'] = 'behind_by_%d_rows' % (len(rows)-len(parsed))
        else:
            dmg = directory/('trajectory.jsonl.damaged_%d' % time.time_ns()); dmg.write_bytes(old); result.update(previous_state='damaged', damaged_copy=str(dmg), damaged_sha256=hashlib.sha256(old).hexdigest())
    fd, tmp = tempfile.mkstemp(prefix='trajectory.jsonl.', suffix='.rebuild', dir=str(directory))
    with os.fdopen(fd, 'wb') as stream: stream.write(new_bytes); stream.flush(); os.fsync(stream.fileno())
    os.replace(tmp, traj); result['replaced'] = True; return result

def reconcile(directory, state):
    """F1 + F19 + F20: commitment decided from commit-bound sha256 only; every proposal visited; orphans and uncommitted outcomes recorded; trajectory rebuilt."""
    commits = sorted((directory/'commits').glob('event_*.json')); found = []
    committed_proposals = set(); committed_outcomes = set()
    for c in commits:
        row = json.loads(c.read_text())['trial']
        if row.get('complete_trial_proposal') and row.get('complete_trial_outcome'):                                                  # v9.13 (e): both hashes in the same commit
            committed_proposals.add(row['complete_trial_proposal'].get('record_sha256')); committed_outcomes.add(row['complete_trial_outcome'].get('sha256'))
    for rec in sorted((directory/'trial_proposals').glob('trial_*.json')):
        if rec.name.endswith(('.outcome.json', '.candidate.json', '.reconciliation.json')): continue
        if digest(rec) in committed_proposals: continue
        row = json.loads(rec.read_text()); outcome = rec.with_suffix('.outcome.json'); base = {'trial': row['trial'], 'record': str(rec), 'record_sha256': digest(rec), 'P_sha256': row['P_sha256'], 'high_sha256': row['high_sha256'], 'residual_sha256': row['residual_sha256'], 'radius_before': row.get('radius_before'), 'base_candidate_sha256': row.get('base_candidate_sha256')}
        if not outcome.exists():
            atomic_write(outcome, {'schema': 'trial_outcome_860_v3', 'decision_only': True, 'adoption': 'adoption is defined by the bound commit event', 'trial': row['trial'], 'proposal': {'record_path': str(rec), 'record_sha256': digest(rec), 'arrays_path': row['arrays_path'], 'arrays_sha256': row['arrays_sha256']},
                                   'accepted': False, 'status': 'interrupted_by_process_fault', 'base_candidate_sha256': row.get('base_candidate_sha256'), 'radius_before': row.get('radius_before'), 'created_epoch': time.time(), 'written_by': 'reconcile',
                                   'note': 'proposal written before validation; the process ended before its event was committed; the trial number is reused by the next proposal and compared (completed_identically)'})
            found.append({'kind': 'orphan_proposal', 'outcome': str(outcome), **base})
        else:
            recon = rec.with_suffix('.reconciliation.json')
            if not recon.exists():
                o = json.loads(outcome.read_text())
                atomic_write(recon, {'schema': 'trial_reconciliation_860_v3', 'status': 'outcome_written_but_not_committed', 'trial': row['trial'], 'proposal_record_sha256': digest(rec), 'outcome_path': str(outcome), 'outcome_sha256': digest(outcome),
                                     'outcome_recorded_accepted': o.get('accepted'), 'outcome_bound_by_a_commit': digest(outcome) in committed_outcomes, 'created_epoch': time.time(),
                                     'statement': 'not adopted; the incumbent is the last committed state'})
            found.append({'kind': 'outcome_written_but_not_committed', 'outcome': str(outcome), 'outcome_sha256': digest(outcome), 'reconciliation': str(recon), **base})
    referenced = {str(Path(json.loads(c.read_text())['post_state'].get('candidate_path') or '').resolve()) for c in commits}
    for snap in sorted((directory/'snapshots').glob('accepted_*.json')):
        if str(snap.resolve()) not in referenced and not snap.name.endswith('.orphan.json'):
            marker = snap.with_suffix('.orphan.json')
            if not marker.exists(): atomic_write(marker, {'status': 'uncommitted_snapshot_interrupted_by_process_fault', 'snapshot': str(snap), 'sha256': digest(snap), 'created_epoch': time.time()})
            found.append({'kind': 'orphan_snapshot', 'snapshot': str(snap)})
    traj = rebuild_trajectory(directory, commits)
    return {'orphans': found, 'trajectory': traj, 'committed_proposals': len(committed_proposals)}

def verify_epoch_binding(state):
    """F13: the recorded epoch file and the fingerprints of the meshes it names must match the campaign binding."""
    epoch_path = Path(RT.translate(str(state['epoch_path'])))                                                                    # S1: translated path
    if not epoch_path.exists(): raise ValueError('recorded epoch file missing: %s' % epoch_path)
    if digest(epoch_path) != state['epoch_sha256']: raise ValueError('recorded epoch file changed (F13 binding)')
    epoch = RT.read(epoch_path)                                                                                                     # S1: mesh paths translated
    for name, key in (('training', 'mesh_sha256'), ('refined', 'refined_mesh_sha256')):
        row = epoch['meshes'][name]
        if row['fingerprint'] != state[key]: raise ValueError('epoch names a different %s mesh fingerprint (F13 binding)' % name)
        mesh = FrozenLogMesh.load(row['path'])
        if mesh.fingerprint != row['fingerprint']: raise ValueError('%s mesh file does not match its recorded fingerprint (F13 binding)' % name)
    return epoch

def recover(args, directory, verification):
    PHASE['phase'] = 'recover'
    cache = read(directory/'state.json'); commits = sorted((directory/'commits').glob('event_*.json'))
    if not commits: raise ValueError('no commits: the campaign was never initialized durably')
    last = read(commits[-1]); committed = last['post_state']; last_kind = last['trial'].get('kind', 'trial')
    if committed['events'] > cache['events']: state = committed                                   # cache behind the authority (crash between commit and cache)
    elif committed['events'] < cache['events']: raise ValueError('State cache claims an uncommitted later event')
    else:
        differing = [k for k in set(cache)|set(committed) if json.dumps(cache.get(k), sort_keys=True, default=str) != json.dumps(committed.get(k), sort_keys=True, default=str)]
        if differing: raise ValueError('State cache differs from the authoritative commit: %s' % sorted(differing))
        state = committed
    atomic_write(directory/'state.json', state)
    if state['code_manifest_sha256'] != digest(args.manifest): raise ValueError('code manifest differs from the campaign binding')
    if state['candidate_sha256'] != digest(state['candidate_path']) or state['arrays_sha256'] != digest(state['arrays_path']): raise ValueError('Immutable accepted snapshot changed')
    if (args.workers != state['workers'] or args.threads != state.get('cache_threads')) and not args.config_change_reason: raise ValueError('configuration changed (workers %r -> %r, threads %r -> %r); allowed only to a G3-qualified configuration with --config-change-reason, recorded as an event (SPEC v9.12 (e))' % (state['workers'], args.workers, state.get('cache_threads'), args.threads))
    recon = reconcile(directory, state)
    interrupted = None
    if state['status'] == 'running' and last_kind != 'slice_end':                                 # F18 (3): the previous slice ended abnormally
        hb = None
        try: hb = read(directory/'HEARTBEAT.json')
        except Exception: pass
        last_epoch = last['trial'].get('epoch') or state.get('last_epoch'); hb_epoch = (hb or {}).get('epoch')
        uncounted = max(0., hb_epoch-last_epoch) if (hb_epoch and last_epoch) else None
        interrupted = {'kind': 'slice_interrupted', 'previous_last_event_kind': last_kind, 'previous_slice': state.get('slices'), 'last_heartbeat': hb, 'uncounted_interval_seconds': uncounted,
                       'reconciliation': recon, 'epoch': time.time(), 'accepted': False, 'verification_sha256': verification['record_sha256'], 'slice': state.get('slices'),
                       'note': 'interval from the last commit to the last heartbeat is reported as interrupted time (PROMPT section 4); never added to active solver time'}
        state['interrupted_seconds'] = state.get('interrupted_seconds', 0.)+(uncounted or 0.); state['status'] = 'interrupted'
        commit(directory, state, interrupted)
    epoch = verify_epoch_binding(state)                                                             # F13
    mesh = FrozenLogMesh.load(epoch['meshes']['training']['path'])
    if mesh.fingerprint != state['mesh_sha256']: raise ValueError('mesh changed')
    model = make_model(mesh, args.workers, args.threads); P = np.asarray(state['P']); high = np.asarray(state['high']); r = model_call(model.fun, P, high, mesh, 'recover', False)
    state['root_weight_check'] = root_weight_check(model)                                                                             # v9.12 (b), once per slice
    with np.load(state['arrays_path'], allow_pickle=False) as data:
        if array_hash(data['P']) != array_hash(P) or array_hash(data['high']) != array_hash(high): raise ValueError('checkpoint arrays changed (bitwise)')   # S8: bit pattern, not np.array_equal
        diff = np.linalg.norm(r-data['residual']); tol = 64*np.finfo(float).eps*max(np.linalg.norm(r), np.linalg.norm(data['residual']), 1e-300)
        if not (math.isfinite(diff) and math.isfinite(tol)) or diff > tol: raise ValueError('Exact endpoint residual did not reproduce within 64 eps (or nonfinite): %r > %r' % (diff, tol))   # v9.13 (e)
    if state.get('coordinate_map_sha256') and digest(directory/'coordinate_map.npz') != state['coordinate_map_sha256']: raise ValueError('coordinate map file changed (F6 binding)')
    with np.load(directory/'coordinate_map.npz', allow_pickle=False) as data: scales = data['column_scales'].copy()
    if array_hash(scales) != state['column_scales_sha256']: raise ValueError('column scales changed (F6 binding)')
    append(directory/'continuations.jsonl', {'epoch': time.time(), 'trials': state['trials'], 'residual_difference_norm': float(diff), 'tolerance': float(tol), 'bitwise': bool(diff == 0), 'reconciliation': recon,
                                             'slice_interrupted_committed': interrupted is not None, 'verification_sha256': verification['record_sha256'], 'environment': provenance(), 'guard_run_id': guard_run_id()})
    state['last_reconciliation'] = recon
    return state, model, Integrator860(epoch, workers=args.workers), r, scales, None

def boundary_metrics(A, r, t):
    """SPEC v9.16 (verifier topic 42): with t the scaled feasible-coordinate image of the chart direction that increases c_l by one unit
    (t = [base_tangent[0,:] * scales[:55], 800 zeros]; chart coordinate 0 is NOT c_l: Chart860.free is an SVD nullspace basis with normal[0] = 0),
    g = A^T r, d = t/(t.t): the c_l derivative of J_mesh is g.d; Qg = g - t (g.t)/(t.t) is the gradient projected onto ker(t^T) (directions with c_l fixed);
    the tangential indicator is ||Qg|| / (||AQ||_F ||r||) with ||AQ||_F^2 = ||A||_F^2 - ||A t||^2/(t.t) clamped at 0 (||AQ||_F = 0 or r = 0 give null with
    the convention recorded); the all-directions indicator by the same formula is ||g|| / (||A||_F ||r||)."""
    A = np.asarray(A, float); r = np.asarray(r, float); t = np.asarray(t, float); tt = float(t@t); g = A.T@r; rn = float(np.linalg.norm(r)); AF = float(np.linalg.norm(A))
    out = {'t_norm': math.sqrt(tt), 'g_norm': float(np.linalg.norm(g)), 'A_frobenius': AF, 'r_norm': rn, 'convention': 'indicators are null when the denominator is 0'}
    if tt <= 0: out.update(dJ_mesh_d_cl=None, Qg_norm=None, tangential_indicator=None, AQ_frobenius=None, AQ_frobenius_clamped=None, all_directions_indicator=(float(np.linalg.norm(g))/(AF*rn) if AF > 0 and rn > 0 else None), note='t = 0: the chart direction increasing c_l is degenerate'); return out
    gt = float(g@t); dJ = gt/tt; Qg = g-t*(gt/tt); At = A@t; AQ2 = max(AF*AF-float(At@At)/tt, 0.); AQ = math.sqrt(AQ2)
    out.update(dJ_mesh_d_cl=dJ, Qg_norm=float(np.linalg.norm(Qg)), AQ_frobenius=AQ, AQ_frobenius_clamped=bool(AF*AF-float(At@At)/tt < 0),
               tangential_indicator=(float(np.linalg.norm(Qg))/(AQ*rn) if AQ > 0 and rn > 0 else None), all_directions_indicator=(float(np.linalg.norm(g))/(AF*rn) if AF > 0 and rn > 0 else None))
    return out

def boundary_state(state, P, high, r, pending, model, scales):
    """SPEC v9.11 (2) as corrected by v9.13 and v9.16: a slice end (any status) is a boundary state if c_l - 1.02 < 1e-3 or at least two of the last 12 trials
    were c_l-bound rejections. For a boundary state the record gives, as SEPARATE quantities, (i) the derivative of J_mesh along the named direction that
    increases c_l by one unit on the C5 manifold (t = base_tangent[0,:] * scales[:55] in the scaled feasible coordinates, high block zero) and (ii) the
    tangential stationarity indicator over the chart directions with c_l fixed (boundary_metrics), plus the active low-coefficient box bounds. First-order
    stationarity at the lower bound in a regular chart (c_l, z) with the other inequalities strict holds exactly when the tangential derivative vanishes and
    the inward c_l derivative is nonnegative, and only at the bound itself; a positive margin does not make the bound active; until tangential stationarity
    holds, different increasing-c_l directions can give different signs. The sign of the c_l derivative alone is not a KKT test. All labels are monitoring
    heuristics, not active-set certificates; a boundary state is never an interior critical point; the section 11 indicator is not a KKT test at the bound."""
    recent = state.get('recent_trial_kinds', []); n_cl = sum(1 for k in recent if k == 'cl_bound'); margin = float(P[0])-1.02; is_boundary = bool(margin < 1e-3 or n_cl >= 2)
    active_low = [int(i) for i in np.flatnonzero(abs(np.asarray(P[1:], float)) >= LOW_BOX*(1-1e-12))]
    out = {'is_boundary_state': is_boundary, 'cl_minus_1.02': margin, 'at_lower_bound_exactly': bool(float(P[0]) <= 1.02), 'cl_bound_rejections_in_last_12': n_cl, 'rule': 'c_l - 1.02 < 1e-3 or >= 2 c_l-bound rejections among the last 12 trials (monitoring heuristic, SPEC v9.11 (2) / v9.13 / v9.16)',
           'active_low_coefficient_box_bounds': {'indices_1_based_free_low': [i+1 for i in active_low], 'box': LOW_BOX}, 'J_mesh_minus_J_abs_independent': (state['objective']-state['validation']['J_abs']) if state.get('validation') else None,
           'J_mesh_minus_J_abs_required_when': 'c_l < 4/3 (SPEC v9.11 (3)); reported always',
           'first_order_condition_statement': 'in a regular chart (c_l, z) of the C5 manifold with the other inequalities strict, first-order stationarity at the lower bound holds exactly when the tangential derivative vanishes and the inward c_l derivative is nonnegative, and only at the bound itself (necessary for a local minimum, not sufficient); a positive margin does not make the bound active; the sign of one c_l derivative is not a KKT test',
           'labels_are': 'monitoring heuristics, not active-set certificates; never an interior critical point'}
    if not is_boundary: return out
    try:
        if pending is not None: chart, A = pending[0], pending[1]
        else: chart = C.Chart860(P); J = model_call(model.jacobian, P, high, model.mesh, 'jacobian', True); A, _ = feasible_matrix(J, chart, column_scales=scales); del J
        t = np.r_[np.asarray(chart.base_tangent, float)[0, :]*np.asarray(scales, float)[:55], np.zeros(A.shape[1]-55)]
        m = boundary_metrics(A, r, t)
        out.update(direction_used='d = t/(t . t) with t = [chart.base_tangent[0,:] * scales[:55], 800 zeros] (the c_l row of the scaled tangent): d is the direction in the scaled feasible coordinates that increases c_l by exactly one unit; the reported derivative is g . d = g . t/(t . t) (chart coordinate 0 is not c_l; SPEC v9.16)',
                   dJ_mesh_d_cl_along_named_direction=m['dJ_mesh_d_cl'], inward_derivative_nonnegative=(None if m['dJ_mesh_d_cl'] is None else bool(m['dJ_mesh_d_cl'] >= 0)),
                   tangential_stationarity_cl_fixed=m['tangential_indicator'], tangential_gradient_norm=m['Qg_norm'], t_norm=m['t_norm'], AQ_frobenius=m['AQ_frobenius'], AQ_frobenius_clamped=m.get('AQ_frobenius_clamped'),
                   stationarity_all_directions_same_formula=m['all_directions_indicator'], denominator_convention=m['convention'],
                   note='reported separately; neither quantity alone is a KKT test; first-order stationarity at the bound needs tangential derivative zero and inward c_l derivative >= 0, evaluated at the bound itself')
    except Exception as exc: out['error'] = type(exc).__name__+': '+str(exc)
    return out

def _reject_nonfinite_token(token): raise ValueError('nonfinite JSON token %s in the assessment output' % token)
def _finite_float(s):
    v = float(s)
    if not math.isfinite(v): raise ValueError('nonfinite JSON number %s in the assessment output' % s)                                          # R5 item 4: 1e999 parses to inf without parse_constant
    return v

def read_assessment_output(path, P_sha, H_sha):
    """C6 / A(d): strict read of one section 13 assessment output for the gate. The FIRST test after the parse is the mode: a record that is not a full assessment
    (completeness_v913.mode != 'full' or is_full_assessment is not True) is refused with the driver's own reason before any other field is read (ruling 3; a spot_only
    record gets 'spot_only_record_not_a_full_assessment'); next, a full record without tight_independent_integral or whose accuracy_passed is not exactly True is refused (E7). Then the output's own P/high digests must bind to the current candidate (foreign outputs never count),
    completeness.failed and the scientific-stop flags must be booleans (anything else is untyped and invalid), failed must be False to count, and the stop is read
    from the output. J_abs comes from the output's tight integral when it is a finite number."""
    rec = {'readable': False, 'full': False, 'bound': False, 'typed': False, 'failed': True, 'stop': True, 'sources': [], 'reason': None, 'J_abs': None, 'mode': None}
    try:
        a = json.loads(Path(str(path)).read_text(), parse_constant=_reject_nonfinite_token, parse_float=_finite_float)               # E9 (b) / R5: a bare NaN/Infinity token or an overflowing number is unreadable (stop)
        if not isinstance(a, dict): raise ValueError('output is not a JSON object')
    except Exception as exc: rec['reason'] = 'unreadable output: %s: %s' % (type(exc).__name__, exc); rec['sources'] = ['unreadable_assessment_output']; return rec
    rec['readable'] = True; comp = a.get('completeness_v913'); comp = comp if isinstance(comp, dict) else {}; rec['mode'] = comp.get('mode')
    if comp.get('mode') != 'full' or comp.get('is_full_assessment') is not True:
        tag = 'spot_only_record_not_a_full_assessment' if comp.get('mode') == 'spot_only' else 'not_a_full_assessment'
        rec['reason'] = '%s (mode %r, is_full_assessment %r): refused before any other field was read (ruling 3)' % (tag, comp.get('mode'), comp.get('is_full_assessment')); rec['sources'] = [tag]; return rec
    ti = a.get('tight_independent_integral')
    if not isinstance(ti, dict) or ti.get('accuracy_passed') is not True:                                                              # E7 (c): refused right after the mode test, before any other field
        rec['reason'] = 'full_record_without_passed_tight_integral (tight_independent_integral %s, accuracy_passed %r): refused before any other field was read (E7)' % ('missing' if not isinstance(ti, dict) else 'present', ti.get('accuracy_passed') if isinstance(ti, dict) else None); rec['sources'] = ['full_record_without_passed_tight_integral']; return rec
    rec['full'] = True; rec['bound'] = bool(a.get('P_sha256') == P_sha and a.get('high_sha256') == H_sha)
    if not rec['bound']: rec['reason'] = 'foreign output: its P/high digests do not bind to the current candidate'; rec['sources'] = ['foreign_assessment_output']; return rec
    flags = {k: (a[k].get('scientific_stop') if isinstance(a.get(k), dict) else None) for k in ('origin_truncation_monitor', 'rf_reference_spot_check')}
    rec['typed'] = isinstance(comp.get('failed'), bool) and all(isinstance(v, bool) for v in flags.values())
    if not rec['typed']: rec['reason'] = 'untyped fields: completeness.failed %r, scientific_stop flags %r' % (comp.get('failed'), flags); rec['sources'] = ['untyped_assessment_output']; return rec
    rec['failed'] = comp.get('failed') is not False
    rec['sources'] = [k for k, v in flags.items() if v is True]+(['failed_assessment_v913a'] if rec['failed'] else [])
    rec['stop'] = bool(rec['failed'] or any(v is True for v in flags.values()))
    J = a['tight_independent_integral'].get('J_abs') if isinstance(a.get('tight_independent_integral'), dict) else None
    rec['J_abs'] = float(J) if isinstance(J, (int, float)) and not isinstance(J, bool) and math.isfinite(float(J)) else None
    rec['reason'] = ('scientific stop from %s' % rec['sources']) if rec['stop'] else None
    return rec

def assessment_gate(args, directory, state, verification, slice_number):
    """SPEC v9.12 (l), section 13, checklist C6 (fail closed). Every ledger row is read strictly. A row COUNTS for the current candidate only if: its output key is a
    nonempty string naming an existing file whose sha256 equals the row's output_sha256; its returncode is the int 0 (a bool is refused); and the output itself is a
    full assessment bound to the current candidate by its own P/high digests, with completeness.failed the boolean False, boolean stop flags and no scientific stop
    (read_assessment_output). Rows without an output key and foreign outputs (bound to another state) never satisfy nor suppress the gate and never stop the campaign.
    Unreadable, non-full (spot_only), untyped, failed or stopped records commit the stop (status assessment_scientific_stop). 'due' uses only the driver's own committed
    reference state['assessment_reference'] (set when a counting row was committed), never an unvalidated rows[-1]. Due and unsatisfied refuses the slice (exit 4)
    unless --skip-assessment-gate (fixtures only; recorded in slice_start)."""
    ledger = directory/'assessments'/'ledger.jsonl'; rows = []
    if ledger.exists():
        for n, line in enumerate(ledger.read_text().splitlines()):
            if not line.strip(): continue
            try: rows.append(json.loads(line))
            except Exception as exc: raise ValueError('assessment ledger line %d is unparsable (%s): refusing to continue (S6)' % (n+1, exc))
    done = state.setdefault('assessments_committed', [])
    P_sha = array_hash(np.asarray(state['P'], float)); H_sha = array_hash(np.asarray(state['high'], float))
    satisfying = []; reports = []
    for n, row in enumerate(rows):
        if not isinstance(row, dict): raise ValueError('assessment ledger row %d is not an object (S6)' % (n+1))
        out = row.get('output'); rep = {'row': n+1, 'output': out if isinstance(out, str) else None, 'counts': False, 'reason': None, 'foreign': False}
        if not isinstance(out, str) or not out: rep['reason'] = 'row has no output key: never counts, never suppresses'; reports.append(rep); continue
        if not Path(out).exists(): rep['reason'] = 'output file missing'
        elif not (type(row.get('returncode')) is int and row.get('returncode') == 0): rep['reason'] = 'returncode %r is not the int 0' % (row.get('returncode'),)
        elif row.get('output_sha256') != digest(out): rep['reason'] = 'output_sha256 does not match the file'
        read = read_assessment_output(out, P_sha, H_sha) if rep['reason'] is None else None
        if read is not None: rep.update(mode=read['mode'], bound=read['bound'], failed=read['failed'], stop=read['stop'], sources=read['sources'], J_abs=read['J_abs'], reason=read['reason']); rep['foreign'] = bool(read['full'] and not read['bound'])
        record_ok = bool(read is not None and read['readable'] and read['full'] and read['bound'] and read['typed'])
        rep['counts'] = bool(record_ok and not read['failed'] and not read['stop']); reports.append(rep)
        if out not in done:                                                                                                        # every new row is committed once, as a record or as a refusal
            stop = bool(not rep['foreign'] and (not record_ok or read['stop']))                                                  # fail closed; foreign outputs never stop, count or suppress
            if stop and state['status'] not in SCIENTIFIC_STOPS: state['status'] = 'assessment_scientific_stop'
            done.append(out)
            if rep['counts']:
                rowJ = row.get('J_abs'); rowJ = float(rowJ) if isinstance(rowJ, (int, float)) and not isinstance(rowJ, bool) and math.isfinite(float(rowJ)) else None
                state['assessment_reference'] = {'output': out, 'output_sha256': row.get('output_sha256'), 'J_abs': read['J_abs'] if read['J_abs'] is not None else rowJ, 'J_abs_source': 'output tight_independent_integral' if read['J_abs'] is not None else ('ledger row' if rowJ is not None else None), 'accepted': int(state.get('accepted', 0)), 'slice': slice_number}
                state['last_assessed_J_abs'] = state['assessment_reference']['J_abs']
            commit(directory, state, {'kind': 'assessment', 'reason': row.get('reason'), 'output': out, 'output_sha256': row.get('output_sha256'), 'record_valid': record_ok, 'counts_for_gate': rep['counts'], 'foreign': rep['foreign'], 'scientific_stop': stop,
                                      'failed': (read['failed'] if record_ok else True), 'sources': (read['sources'] if read is not None else ['invalid_ledger_row']), 'refusal_reason': rep['reason'], 'mode': rep.get('mode'), 'candidate_sha256': row.get('candidate_sha256'), 'epoch': time.time(), 'accepted': False, 'verification_sha256': verification['record_sha256'], 'slice': slice_number})
        if rep['counts']: satisfying.append(rep)
    ref = state.get('assessment_reference'); J_now = (state.get('validation') or {}).get('J_abs')
    due = bool(ref is None or (ref.get('J_abs') is not None and isinstance(J_now, (int, float)) and J_now <= .5*ref['J_abs']) or (int(state.get('accepted', 0))-int(ref.get('accepted') or 0) >= 100))
    state['assessment_gate'] = {'due': due, 'assessed_for_candidate': bool(satisfying), 'ledger_rows': len(rows), 'rows_counting': len(satisfying), 'row_reports': reports[-20:], 'reference': ref, 'skipped': bool(args.skip_assessment_gate), 'rule': 'C6: counting rows only; foreign rows and rows without output never satisfy nor suppress; due from the committed reference, never rows[-1]'}
    if due and not satisfying and not args.skip_assessment_gate:
        commit(directory, state, {'kind': 'assessment_gate_refusal', 'gate': state['assessment_gate'], 'candidate_sha256': state.get('candidate_sha256'), 'epoch': time.time(), 'accepted': False, 'verification_sha256': verification['record_sha256'], 'slice': slice_number})   # durable record of the refusal (state.json cache rewritten with the gate report)
        print('REFUSAL: section 13 assessment due for candidate %s (ledger %s, %d rows, none counting); run assess_cadence860 before this slice (SPEC v9.12 (l), C6)' % (state.get('candidate_sha256'), ledger, len(rows)), flush=True); raise SystemExit(EXIT_REFUSAL)

def scientific_stop(directory, state, status, name, payload, common):
    state['status'] = status
    dpath = directory/'diagnosis'/('%s_%08d_%d.json' % (name, state['trials'], time.time_ns())); atomic_write(dpath, {'trial': state['trials'], 'status': status, 'incumbent_preserved': True, **payload})
    commit(directory, state, {'kind': 'scientific_stop', 'status': status, 'diagnosis_path': str(dpath), 'diagnosis_sha256': digest(dpath), 'accepted': False, **common})

def run(args):
    began = time.monotonic(); run_start_epoch = time.time(); deadline = began+args.seconds; directory = Path(args.root).resolve(); directory.mkdir(parents=True, exist_ok=True)   # v9.15 (1): optimizer time = [run_start_epoch, slice_end epoch]
    commits0 = sorted((directory/'commits').glob('event_*.json')) if (directory/'commits').exists() else []
    existing = bool(commits0)                                                                                                         # v9.13 (e): the commits are the authority; a missing cache is rebuilt
    if existing and not (directory/'state.json').exists(): atomic_write(directory/'state.json', read(commits0[-1])['post_state'])
    slice_number = (read(commits0[-1])['post_state']['slices']+1) if existing else 1
    verification = verify_binding(args.manifest, directory, slice_number, check_source=True)                    # F2
    if (directory/'STOPPED_FOR_DIAGNOSIS').exists() and not args.override_stop: print('REFUSAL: STOPPED_FOR_DIAGNOSIS present; a written diagnosis and lead release (--override-stop --override-reason --release-ref) are required', flush=True); raise SystemExit(EXIT_REFUSAL)   # F10, S7
    hb_update(phase='startup', slice=slice_number); hb = heartbeat_thread(directory)                                                    # v9.13 (f): heartbeat before initialization or recovery
    kappa = load_kappa(args)
    if existing:
        if not args.resume: raise ValueError('Existing campaign requires --resume')
        state, model, integ, r, scales, prepared = recover(args, directory, verification)
        if state.get('kappa', {}).get('source_sha256') != kappa['source_sha256']: raise ValueError('kappa file changed (sha %r vs %r); a new kappa needs a new campaign root or a lead release (SPEC v9.12 (d))' % ((state.get('kappa') or {}).get('source_sha256'), kappa['source_sha256']))
        if args.workers != state['workers'] or args.threads != state.get('cache_threads'):
            if not args.benchmark_record: raise ValueError('configuration change needs --benchmark-record (the G3 benchmark listing the qualified (workers, threads) pairs)')
            bench = json.loads(Path(args.benchmark_record).read_text()); bsha = digest(args.benchmark_record); m = json.loads(Path(args.manifest).read_text())
            try: brel = str(Path(args.benchmark_record).resolve().relative_to(LANE))
            except ValueError: brel = str(Path(args.benchmark_record).resolve())
            brows = [r_ for r_ in m.get('files', []) if r_.get('path') in (brel, str(Path(args.benchmark_record).resolve()))]
            if not brows or any(r_.get('sha256') != bsha for r_ in brows): raise ValueError('benchmark record sha256 %s is not bound in the release manifest (SPEC v9.15 (e))' % bsha[:16])   # defect 2 (a)
            if bench.get('passed') is not True: raise ValueError('benchmark record did not pass; no configuration is qualified by it')                                                           # defect 2 (b)
            pairs = {(int(v['configuration']['workers']), int(v['configuration']['cache_threads'])) for v in bench.get('runs', {}).values() if not v.get('failed')}
            if (args.workers, args.threads) not in pairs: raise ValueError('configuration (%d, %d) is not a G3-qualified pair %s' % (args.workers, args.threads, sorted(pairs)))
            commit(directory, state, {'kind': 'configuration_change', 'benchmark_record': str(Path(args.benchmark_record).resolve()), 'benchmark_record_sha256': digest(args.benchmark_record), 'reason': args.config_change_reason, 'workers': [state['workers'], args.workers], 'cache_threads': [state.get('cache_threads'), args.threads], 'epoch': time.time(), 'accepted': False, 'verification_sha256': verification['record_sha256'], 'slice': slice_number})
            state['workers'] = args.workers; state['cache_threads'] = args.threads
    else:
        if args.resume: raise ValueError('Cannot resume a nonexistent campaign')
        state, model, integ, r, scales, prepared = initialize(args, directory, verification, kappa)
    seed_norms = 1/scales
    if state['consecutive_rejections'] >= 12 and state['status'] in ('running', 'interrupted'): state['status'] = 'trust_obstruction_requires_diagnosis'   # F4 recheck
    assessment_gate(args, directory, state, verification, slice_number)                                                                 # v9.12 (l)
    if not existing and state['status'] in SCIENTIFIC_STOPS:                                                                              # v9.12 (k): initialization stop already committed
        print(json.dumps({'campaign': str(directory), 'status': state['status'], 'note': 'committed scientific stop at initialization'}), flush=True); return state['status']
    if state['status'] in SCIENTIFIC_STOPS or (directory/'STOPPED_FOR_DIAGNOSIS').exists():
        if not args.override_stop: print('REFUSAL: campaign is in a scientific stop state (%s); a written diagnosis and lead release are required' % state['status'], flush=True); raise SystemExit(EXIT_REFUSAL)
        ref_path, ref_sha = args.release_ref.split(':', 1)
        if digest(ref_path) != ref_sha: print('REFUSAL: release reference hash mismatch', flush=True); raise SystemExit(EXIT_REFUSAL)
        prior = state['status']; state['status'] = 'running'
        commit(directory, state, {'kind': 'scientific_stop_override', 'prior_status': prior, 'reason': args.override_reason, 'release_ref': {'path': ref_path, 'sha256': ref_sha}, 'epoch': time.time(), 'accepted': False, 'verification_sha256': verification['record_sha256'], 'slice': slice_number})   # F5
        if (directory/'STOPPED_FOR_DIAGNOSIS').exists(): (directory/'STOPPED_FOR_DIAGNOSIS').rename(directory/('STOPPED_FOR_DIAGNOSIS.released_'+str(time.time_ns())))
    P, high = np.asarray(state['P']), np.asarray(state['high'])
    state['status'] = 'running'; state['slices'] = slice_number; state['verification'] = verification
    common0 = {'code_manifest_sha256': state['code_manifest_sha256'], 'verification_sha256': verification['record_sha256'], 'slice': slice_number}
    commit(directory, state, {'kind': 'slice_start', 'epoch': time.time(), 'run_start_epoch': run_start_epoch, 'accepted': False, 'paired_supervisor_sha256': os.environ.get('SUPERVISOR_SHA256'), 'exit_contract': '0 committed slice_end; 3 process fault; 4 refusal', 'workers': args.workers, 'cache_threads': args.threads, 'seconds_budget': args.seconds, 'reserve_seconds_floor': args.reserve_seconds, 'kappa': kappa, 'assessment_gate': state.get('assessment_gate'), 'root_weight_check': state.get('root_weight_check'), 'loaded_modules_sha256_at_import': IMPORT_CLOSURE['files'], 'budget_renewal_reason': args.budget_renewal_reason, 'environment': provenance(), **common0})   # F18, v9.13 (f)
    hb_state(state)
    pending = None; trials_this_slice = 0; cpu0 = resources()['cpu_seconds']; end_reason = None
    reserve = max(args.reserve_seconds, 1.5*state.get('iteration_wall_max_seconds', 0.))                                            # F3(a)
    orphans = {o['trial']: o for o in (state.get('last_reconciliation') or {}).get('orphans', []) if o['kind'] in ('orphan_proposal', 'outcome_written_but_not_committed')}
    while not STOP and not (directory/'STOP').exists() and trials_this_slice < args.max_trials:
        if time.monotonic()+reserve > deadline: end_reason = 'time reserve %.0f s reached' % reserve; break
        t_iter = time.perf_counter()
        common = {**common0, 'epoch': time.time()}
        if pending is None:                                                                                                          # epoch start
            if exceptional_parameter(P[0]):                                                                                          # SPEC v9.3 section 11
                scientific_stop(directory, state, 'exceptional_parameter_requires_rank_treatment', 'exceptional', {'cl': float(P[0]), 'reason': 'incumbent c_l within relative 2^-30 of 2 or 3 at an epoch start'}, common); break
            PHASE['phase'] = 'jacobian'; hb_update(phase='jacobian'); t0 = time.perf_counter()
            if prepared is None:
                chart = C.Chart860(P); J = model_call(model.jacobian, P, high, model.mesh, 'jacobian', True)
                if not np.all(np.isfinite(J)): bad = np.argwhere(~np.isfinite(J))[0]; raise ProcessFault('phase jacobian: nonfinite Jacobian entry at epoch start (trial %d): first at row %d column %d, value %s' % (state['trials']+1, bad[0], bad[1], _classify(float(J[tuple(bad)]))))
                try: A, _ = feasible_matrix(J, chart, column_scales=scales)
                except ValueError as exc:
                    del J; scientific_stop(directory, state, 'exceptional_parameter_requires_rank_treatment', 'column', {'cl': float(P[0]), 'reason': str(exc)}, common); break
                del J
            else: chart, A = prepared; prepared = None
            PHASE['phase'] = 'factorization'; hb_update(phase='factorization'); factors = DenseTrustModel(A, r); stationarity = factors.stationarity()
            if not state.get('rounding_bound'): state['rounding_bound'] = rounding_bound(model, P, high, r, kappa['kappa'], state['root_weight_check']['h'])[0]
            bound_ref = state['rounding_bound']
            erec = epoch_start_record(A, scales, factors, seed_norms)
            atomic_write(directory/'latest_model.json', {'accepted': state['accepted'], 'trials': state['trials'], 'objective': state['objective'], 'stationarity': {k: v for k, v in stationarity.items() if k != 'singular_values'},
                                                          'singular_values_min_max': [float(min(factors.s)), float(max(factors.s))], 'diagnostic_rank': factors.diagnostic_rank, 'rank_floor': float(factors.rank_floor), 'epoch_start_record': erec, 'rounding_bound_ref': bound_ref,
                                                          'chart': {k: v for k, v in chart.geometry_diagnostics.items() if k != 'base_HP'}, 'model_seconds': time.perf_counter()-t0})
            pending = (chart, A, factors, stationarity, time.perf_counter()-t0, erec)
        chart, A, factors, stationarity, model_seconds, erec = pending; bound_ref = state['rounding_bound']
        PHASE['phase'] = 'trust_step'; PHASE['trial'] = state['trials']+1; hb_update(phase='trust_step', phase_trial=state['trials']+1); t_trial = time.perf_counter(); res0 = resources()
        step, sub = factors.step(state['radius'])
        if not np.all(np.isfinite(step)): bad = int(np.flatnonzero(~np.isfinite(step))[0]); raise ProcessFault('phase trust_step: nonfinite trust step (trial %d): first at coordinate %d, value %s' % (state['trials']+1, bad, _classify(float(step[bad]))))
        sub['actual_matrix_KKT_relative'] = actual_matrix_kkt(A, r, step, sub)
        if not (sub['actual_matrix_KKT_relative'] <= 1e-8):                                                                          # F4 + v9.12 (g): NaN stops
            kv = sub['actual_matrix_KKT_relative']; scientific_stop(directory, state, 'full_matrix_trust_subproblem_inaccuracy_requires_diagnosis', 'kkt', {'kkt_relative': kv, 'kkt_classification': ('finite above 1e-8' if math.isfinite(kv) else _classify(float(kv))), 'subproblem': {k: v for k, v in sub.items() if not k.startswith('svd_coordinate')}}, common); break
        prediction = sub['actual_matrix_predicted_decrease']
        if not np.isfinite(prediction) or prediction <= 128*np.finfo(float).eps*max(state['objective'], 1e-300):                   # SPEC 11 + F22
            scientific_stop(directory, state, 'model_reduction_at_precision_floor', 'floor', {'predicted_decrease': prediction, 'predicted_decrease_classification': ('finite' if np.isfinite(prediction) else _classify(float(prediction))), 'objective': state['objective'], 'reason': 'prediction'}, common); break
        if state['objective'] < 1e-250:                                                                                               # v9.12 (c) underflow
            scientific_stop(directory, state, 'model_reduction_at_precision_floor', 'floor', {'objective': state['objective'], 'reason': 'underflow'}, common); break
        if 2*bound_ref['T']*(1+2.**-40) > .05*prediction:                                                                             # SPEC v9.3 section 11 rounding bound, v9.12 (c) arithmetic
            scientific_stop(directory, state, 'model_reduction_at_precision_floor', 'floor', {'predicted_decrease': prediction, 'T_ref': bound_ref['T'], 'B_ref': bound_ref['B'], 'C_ref': bound_ref['C'], 'E_ref': bound_ref['E'], 'objective': state['objective'], 'reason': 'rounding_bound'}, common); break
        state['trials'] += 1; trials_this_slice += 1
        row = {'trial': state['trials'], 'accepted_before': state['accepted'], 'objective_before': state['objective'], 'radius_before': state['radius'], 'predicted_decrease': prediction,
               'subproblem': {k: v for k, v in sub.items() if not k.startswith('svd_coordinate')}, 'stationarity': {k: v for k, v in stationarity.items() if k != 'singular_values'}, 'epoch_start_record': erec,
               'model_seconds': model_seconds, 'accepted': False, 'step_norm': float(np.linalg.norm(step)), 'incumbent_candidate_sha256': state['candidate_sha256'], 'B_ref': bound_ref['B'], 'C_ref': bound_ref['C'], 'T_ref': bound_ref['T'], 'E_ref': bound_ref['E'], 'stationarity_incumbent_candidate_sha256': state['candidate_sha256'], **common}
        row['cl_bounds_incumbent'] = {'cl_minus_1.02': float(P[0])-1.02, '10_minus_cl': 10.-float(P[0])}                                  # SPEC v9.11 (1)
        intent = directory/'trial_intents'/('trial_%08d_%d.json' % (state['trials'], time.time_ns())); atomic_write(intent, {'trial': state['trials'], 'radius': state['radius'], 'step_sha256': array_hash(step), 'scales_sha256': array_hash(scales), 'incumbent_candidate_sha256': state['candidate_sha256'], 'predicted_decrease': prediction, 'epoch': time.time()}); row['trial_intent'] = {'path': str(intent), 'sha256': digest(intent)}   # S8: durable record before the lift
        try:
            PHASE['phase'] = 'lift'; hb_update(phase='lift'); Pp, hh, hp = feasible_trial(chart, P, high, step, scales)
            ld = getattr(chart, 'last_diagnostics', None) or {}; row['lift'] = {'iterations': len(ld.get('iterations', [])), 'final': ld.get('final'), 'last_iteration': (ld.get('iterations') or [None])[-1]}   # v9.12 (i)
            PHASE['phase'] = 'trial_fun'; hb_update(phase='trial_fun'); t1 = time.perf_counter(); rr = model.fun(Pp, hh); row['trial_fun_seconds'] = time.perf_counter()-t1
            PHASE['phase'] = 'trial_checks'
            if not np.all(np.isfinite(rr)): raise ValueError('nonfinite: trial residual (%d entries)' % int(np.count_nonzero(~np.isfinite(rr))))   # explicit, before any comparison
            trial_objective = objective(rr)
            if not math.isfinite(trial_objective): raise ValueError('nonfinite: trial objective')
            if trial_objective == 0. or trial_objective < 1e-250 or state['objective'] < 1e-250: raise PrecisionFloorStop(trial_objective)                       # C18: stop before validation and acceptance
            bound_trial, S_trial, e_trial = rounding_bound(model, Pp, hh, rr, kappa['kappa'], state['root_weight_check']['h']); row.update(B_trial=bound_trial['B'], C_trial=bound_trial['C'], T_trial=bound_trial['T'], E_trial=bound_trial['E'])
            row['complete_trial_proposal'] = proposal_snapshot(directory, state, Pp, hh, rr, step, scales, hp)
            if state['trials'] in orphans:                                                                                              # F1 completed_identically
                o = orphans[state['trials']]; row['orphan_comparison'] = {'orphan_kind': o['kind'], 'orphan_record': o['record'], 'completed_identically': bool(o['P_sha256'] == array_hash(Pp) and o['high_sha256'] == array_hash(hh) and o['residual_sha256'] == array_hash(rr) and o.get('radius_before') == state['radius'])}
            PHASE['phase'] = 'validation'; hb_update(phase='validation'); t1 = time.perf_counter(); validation = integ.validate(Pp, hh, coarse_r=rr, predicted_reduction=prediction, reference=state['validation']); row['validation_seconds'] = time.perf_counter()-t1
            decrease = state['objective']-trial_objective; ratio = decrease/prediction
            independent_decrease = state['validation']['J_abs']-validation['J_abs']; uncertainty = state['validation']['error_abs']+validation['error_abs']
            for name, v in (('decrease', decrease), ('ratio', ratio), ('independent_decrease', independent_decrease), ('uncertainty', uncertainty)):
                if not math.isfinite(v): raise ValueError('nonfinite: %s' % name)
            accuracy = bool(validation['accuracy_passed'] and not validation.get('requires_refinement', False) and uncertainty <= .05*prediction and independent_decrease > uncertainty)
            rounding_ok = bool(decrease*(1-2.**-51) > (bound_ref['T']+bound_trial['T'])*(1+2.**-40))                                   # SPEC v9.3 section 11, v9.12 (c)
            accepted = bool(decrease > 128*np.finfo(float).eps*max(state['objective'], 1e-300) and ratio > .1 and accuracy and rounding_ok)
            row.update(objective_trial=trial_objective, actual_mesh_decrease=decrease, gain_ratio=ratio, independent_decrease=independent_decrease, integration_uncertainty=uncertainty, rounding_bound_passed=rounding_ok,
                       trial_validation={k: v for k, v in validation.items() if k != 'independent_integral'}, trial_J_abs_independent=validation['J_abs'], trial_error_abs=validation['error_abs'],
                       five_Taylor_max=hp['max_abs'], trial_cl=float(Pp[0]), trial_a0=hp['a0'], trial_a000=hp.get('a000_float'), accepted=accepted, cl_bounds_trial={'cl_minus_1.02': float(Pp[0])-1.02, '10_minus_cl': 10.-float(Pp[0])})
            if not validation['accuracy_passed'] or validation.get('requires_refinement', False) or uncertainty > .05*prediction:
                row['stop_reason'] = 'integration_uncertainty_requires_new_mesh_epoch'; state['status'] = 'needs_mesh_refinement'
            if ratio < .25: state['radius'] *= .25
            elif ratio > .75 and np.linalg.norm(step) > .8*state['radius']: state['radius'] *= 2
            try:                                                                                                                       # F14: widths after the decision, cannot change it
                hp_inc = C.hp_report(P); w_inc = widths(hp_inc); w_tr = widths(hp)
                row.update(trial_widths=w_tr, physical_changes={k: {'incumbent': v0, 'trial': v1, 'absolute': (v1-v0) if (v0 is not None and v1 is not None) else None, 'relative': ((v1-v0)/v0 if (v0 is not None and v1 is not None and v0) else None)}
                                                                 for k, v0, v1 in (('cl', float(P[0]), float(Pp[0])), ('a0', hp_inc['a0'], hp['a0']), ('W_x', w_inc['W_x'], w_tr['W_x']), ('W_y', w_inc['W_y'], w_tr['W_y']))},
                           chart_predicted_responses=predicted_responses(chart, P, step, scales))                                      # F8
            except Exception as exc: row['widths_error'] = type(exc).__name__+': '+str(exc); w_tr = {'W_x': None, 'W_y': None, 'l': None, 'eta': None}
            if accepted:
                prospective = json.loads(json.dumps(state, default=str)); prospective.update(P=Pp.tolist(), high=hh.tolist(), objective=trial_objective, validation=validation, accepted=state['accepted']+1, consecutive_rejections=0, rounding_bound=bound_trial)
                tag = 'accepted_'+str(prospective['accepted']).zfill(8); cpath, apath = snapshot(directory, prospective, Pp, hh, rr, tag, hp, S_R=S_trial, e=e_trial)
                prospective.update(candidate_path=cpath, arrays_path=apath, candidate_sha256=digest(cpath), arrays_sha256=digest(apath))
                prospective['widths_history'] = (state.get('widths_history', [])+[dict(w_tr, trial=state['trials'], J=validation['J_abs'], e=validation['error_abs'], cl=float(Pp[0]))])[-11:]
                hist = [h for h in prospective['widths_history'] if h.get('l') is not None]                                           # F14: nulls skipped
                if len(hist) >= 2:
                    dl = hist[-1]['l']-hist[0]['l']; deta = hist[-1]['eta']-hist[0]['eta']; Jold = hist[0].get('J'); Jnew = hist[-1]['J']
                    if Jold is not None and abs(dl) > .01 and abs(deta) < .01 and (Jold-Jnew) <= max(1e-3*Jold, 10*(hist[0].get('e', 0)+hist[-1]['e'])):
                        row['width_drift_warning'] = {'delta_l': dl, 'delta_eta': deta, 'J_old': Jold, 'J_new': Jnew}; append(directory/'width_drift_warnings.jsonl', {'trial': state['trials'], **row['width_drift_warning']})
                P, high, r = Pp, hh, rr; state.update(prospective); pending = None
                if exceptional_parameter(float(Pp[0])) and state['status'] == 'running': state['status'] = 'exceptional_parameter_requires_rank_treatment'; row['stop_reason'] = 'accepted c_l within relative 2^-30 of 2 or 3 (SPEC v9.3 section 11)'
            else: state['rejected'] += 1; state['consecutive_rejections'] += 1
        except PrecisionFloorStop as exc:                                                                                              # C18 (verifier 09:25Z): nothing validated, nothing accepted
            row.update(accepted=False, objective_trial=exc.trial_objective, precision_floor_stop=True, stop_reason='trial objective %r is zero or below 1e-250 (C18, v9.15 (4)): precision-floor stop before validation and acceptance; incumbent candidate, objective and accepted count unchanged' % exc.trial_objective)
            scientific_stop(directory, state, 'model_reduction_at_precision_floor', 'floor', {'objective': state['objective'], 'trial_objective': exc.trial_objective, 'reason': 'trial_underflow', 'accepted': state['accepted'], 'candidate_sha256': state['candidate_sha256'], 'nothing_accepted': True}, common)
        except Exception as exc:
            reason = str(exc)
            if isinstance(exc, ValueError) and reason.startswith(MODEL_NONFINITE) and PHASE['phase'] == 'trial_fun': reason = 'nonfinite: trial residual (model860 raised: %s)' % reason   # S2
            rejection_phase = PHASE['phase'] in ('lift', 'trial_fun', 'trial_checks')                                                 # v9.15 (4): an exception inside the integral (phase validation) is never a rejection
            if not (rejection_phase and isinstance(exc, ValueError) and reason.startswith(REJECTION_PREFIXES)):                       # v9.12 (f): anything else is a process fault
                raise ProcessFault('phase %s: %s: %s' % (PHASE['phase'], type(exc).__name__, reason)) from exc
            row.update(failure=reason, failure_kind=reason.split(':')[0], failure_phase=PHASE['phase'], accepted=False)
            ld = getattr(chart, 'last_diagnostics', None)
            if PHASE['phase'] == 'lift' and ld: row['lift'] = {'iterations': len(ld.get('iterations', [])), 'final': ld.get('final'), 'last_iteration': (ld.get('iterations') or [None])[-1], 'note': 'diagnostics of the last successful lift of this chart object; the failed lift raised before setting them'}   # S8/v9.12 (i)
            state['radius'] *= .25; state['rejected'] += 1; state['consecutive_rejections'] += 1
            if reason.startswith('bound: lower c_l') or reason.startswith('bound: upper c_l'):                                            # SPEC v9.11 (1)
                state['cl_bound_rejections_total'] = state.get('cl_bound_rejections_total', 0)+1; state['cl_bound_rejections_consecutive'] = state.get('cl_bound_rejections_consecutive', 0)+1; row['bound_violated'] = reason.split('(')[0].strip()
            elif reason.startswith('bound:'): row['bound_violated'] = 'low coefficient'
        if not str(row.get('bound_violated', '')).endswith('c_l'): state['cl_bound_rejections_consecutive'] = 0                      # a trial that is not a c_l-bound rejection resets the consecutive count
        state['recent_trial_kinds'] = (state.get('recent_trial_kinds', [])+[('accepted' if row['accepted'] else ('cl_bound' if str(row.get('bound_violated', '')).endswith('c_l') else ('rejected:'+str(row.get('failure_kind', 'evaluation')) if row.get('failure') else 'rejected')))])[-12:]
        row['cl_bound_rejections'] = {'total': state.get('cl_bound_rejections_total', 0), 'consecutive': state.get('cl_bound_rejections_consecutive', 0)}
        if row.get('complete_trial_proposal'):
            outcome_path = Path(row['complete_trial_proposal']['record_path']).with_suffix('.outcome.json')
            atomic_write(outcome_path, {'schema': 'trial_outcome_860_v3', 'decision_only': True, 'adoption': 'adoption is defined by the bound commit event', 'trial': state['trials'], 'proposal': row['complete_trial_proposal'], 'accepted': row['accepted'],
                                        'status': 'accepted' if row['accepted'] else ('validation_failed' if row.get('failure') else 'rejected'), 'failure': row.get('failure'), 'stop_reason': row.get('stop_reason'),
                                        'incumbent_candidate_sha256': state['candidate_sha256'], 'completed_identically': (row.get('orphan_comparison') or {}).get('completed_identically'), 'created_epoch': time.time()})
            row['complete_trial_outcome'] = {'path': str(outcome_path), 'sha256': digest(outcome_path)}
        if state['status'] == 'running' and state['consecutive_rejections'] >= 12: state['status'] = 'trust_obstruction_requires_diagnosis'                     # F4
        if state['status'] == 'running' and stationarity['full_range_projected_residual_relative'] <= 1e-5 and row['accepted']:         # baseline timing (stage13_campaign_v3:542): indicator of the pre-step incumbent
            state['status'] = 'needs_independent_stationarity_verification'
            try:                                                                                                                       # v9.12 (h): also recomputed at the new accepted state
                PHASE['phase'] = 'stationarity_recompute'; J2 = model.jacobian(P, high); A2, _ = feasible_matrix(J2, C.Chart860(P), column_scales=scales); del J2
                row['stationarity_recomputed_at_accepted_state'] = {k: v for k, v in DenseTrustModel(A2, r).stationarity().items() if k != 'singular_values'}; del A2
            except Exception as exc: row['stationarity_recomputed_at_accepted_state'] = {'error': type(exc).__name__+': '+str(exc)}
        res1 = resources(); iteration_wall = time.perf_counter()-t_iter; state['iteration_wall_max_seconds'] = max(state.get('iteration_wall_max_seconds', 0.), iteration_wall)
        row.update(radius_after=state['radius'], accepted_after=state['accepted'], status_after=state['status'], trial_wall_seconds=time.perf_counter()-t_trial, iteration_wall_seconds=iteration_wall, trial_cpu_seconds=res1['cpu_seconds']-res0['cpu_seconds'], rss_mib=res1['rss_mib'], peak_rss_mib=res1['peak_rss_mib'],
                   cache_record={k: v for k, v in model.cache_record().items() if k in ('cache_builds', 'cache_build_seconds', 'jacobian_seconds', 'origin_series_seconds', 'evaluation_cache_hits')})
        state['last_epoch'] = time.time(); state['last_stationarity'] = {k: v for k, v in stationarity.items() if k != 'singular_values'}
        commit(directory, state, row); hb_state(state); hb_update(note='trial committed')
        print(json.dumps(durable({'trial': state['trials'], 'accepted': state['accepted'], 'J_mesh': state['objective'], 'J_abs_independent': state['validation']['J_abs'], 'radius': state['radius'], 'status': state['status'], 'wall_s': row['trial_wall_seconds'], 'failure': row.get('failure')})), flush=True)
        reserve = max(args.reserve_seconds, 1.5*state['iteration_wall_max_seconds'])
        if state['status'] != 'running': break
    if state['status'] == 'running': state['status'] = 'checkpointed_slice' if not (STOP or (directory/'STOP').exists()) else 'stopped_by_request'
    if end_reason is None: end_reason = 'operator STOP' if (STOP or (directory/'STOP').exists()) else ('max_trials reached' if trials_this_slice >= args.max_trials else ('status %s' % state['status']))
    boundary = boundary_state(state, P, high, r, pending, model, scales)                                                          # SPEC v9.11 (2) / v9.13
    end_closure = loaded_closure(); changed_modules = sorted(k for k in set(IMPORT_CLOSURE['files'])|set(end_closure['files']) if IMPORT_CLOSURE['files'].get(k) != end_closure['files'].get(k) and k in IMPORT_CLOSURE['files'])
    if changed_modules:                                                                                                                # v9.13 (f): frozen code changed during the slice
        state['status'] = 'frozen_code_changed_requires_diagnosis'; (directory/'STOPPED_FOR_DIAGNOSIS').write_text('frozen_code_changed %s %s\n' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), changed_modules)); end_reason = 'loaded module files changed during the slice: %s' % changed_modules
    HB_STOP.set()
    if hb is not None: hb.join(timeout=10)
    inc_wall = time.monotonic()-began; inc_cpu = resources()['cpu_seconds']-cpu0
    state['elapsed_worker_seconds'] += inc_wall; state['solver_cpu_seconds'] += inc_cpu; state['last_epoch'] = time.time()
    commit(directory, state, {'kind': 'slice_end', 'status': state['status'], 'slice_end_reason': end_reason, 'run_start_epoch': run_start_epoch, 'boundary_state': boundary, 'module_sha256_at_import_equal_at_end': not changed_modules, 'changed_modules': changed_modules, 'loaded_modules_at_import': IMPORT_CLOSURE['files'], 'elapsed_worker_seconds_increment': inc_wall, 'solver_cpu_seconds_increment': inc_cpu, 'trials_this_slice': trials_this_slice,
                              'accepted': False, 'epoch': time.time(), 'environment': provenance(), **common0})                      # F18
    completion = {'schema': 'slice_completion_860_v3', 'slice': slice_number, 'status': state['status'], 'guard_run_id': guard_run_id(), 'slice_end_event_sequence': state['events'], 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                  'trials_this_slice': trials_this_slice, 'accepted': state['accepted'], 'trials': state['trials'], 'objective': state['objective'], 'J_abs_independent': state['validation']['J_abs'], 'slice_end_reason': end_reason, 'pid': os.getpid()}
    atomic_write(directory/'slice_completion'/('slice_%04d_%s.json' % (slice_number, guard_run_id() or 'norun')), completion)      # F12
    hb_state(state); write_heartbeat(directory, 'slice end')                                                                        # single writer: thread has stopped
    append(directory/'slices.jsonl', {**completion, 'seconds': inc_wall, 'verification_sha256': verification['record_sha256'], 'environment': provenance()})
    print(json.dumps(durable({'campaign': str(directory), 'status': state['status'], 'accepted': state['accepted'], 'trials': state['trials'], 'J_abs': state['validation']['J_abs'], 'elapsed_worker_seconds': state['elapsed_worker_seconds']})), flush=True)
    return state['status']

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True); parser.add_argument('--seed-json', required=True); parser.add_argument('--seed-npz', required=True); parser.add_argument('--manifest', required=True)
    parser.add_argument('--label', default='campaign860'); parser.add_argument('--seconds', type=float, default=3300.); parser.add_argument('--workers', type=int, default=8); parser.add_argument('--threads', type=int, default=4)
    parser.add_argument('--resume', action='store_true'); parser.add_argument('--initial-radius', type=float); parser.add_argument('--max-trials', type=int, default=10**9)
    parser.add_argument('--reserve-seconds', type=float, default=900., help='F3(a): minimum remaining slice time to start a trial; raised to 1.5x the largest observed iteration')
    parser.add_argument('--kappa-file', required=True, help='SPEC v9.7 calibration record (kappa, rho_max, coverage); mandatory and validated (v9.12 (d)), sha256 bound in the manifest')
    parser.add_argument('--config-change-reason', help='v9.12 (e): allow a change of workers/threads to another G3-qualified configuration, recorded as an event')
    parser.add_argument('--skip-assessment-gate', action='store_true', help='fixtures only: do not refuse a slice while a section 13 assessment is due (recorded in slice_start)')
    parser.add_argument('--benchmark-record', help='v9.15 (4): the G3 benchmark JSON whose (workers, threads) configurations are the only allowed targets of --config-change-reason')
    parser.add_argument('--budget-renewal-reason', help='v9.13 (e): a fresh guard session with an explicit new cumulative budget after a planned budget exhaustion; recorded in the slice_start event')
    parser.add_argument('--override-stop', action='store_true'); parser.add_argument('--override-reason'); parser.add_argument('--release-ref', help='path:sha256 of the lead release note or diagnosis')
    args = parser.parse_args()
    if not (0 < args.seconds <= 9000) or args.workers < 1: parser.error('slice must be positive and fit the guard budget; workers >= 1')
    if args.override_stop and not (args.override_reason and args.release_ref and ':' in args.release_ref): parser.error('--override-stop requires --override-reason and --release-ref path:sha256')
    signal.signal(signal.SIGTERM, request_stop); signal.signal(signal.SIGINT, request_stop)
    os.register_at_fork(after_in_child=lambda: (signal.signal(signal.SIGTERM, signal.SIG_DFL), signal.signal(signal.SIGINT, signal.SIG_DFL)))   # 2026-10-25 hang fix: fork-pool workers must not inherit request_stop, or Pool.terminate's SIGTERM is swallowed and the parent's join hangs (outputs/diag/pilot_hang_20261025T0050Z.md)
    try:
        run(args); raise SystemExit(0)
    except SystemExit as exc:
        if exc.code not in (0, EXIT_REFUSAL):                                                                                          # S7: any other SystemExit is a fault with a record
            try: append(Path(args.root)/'faults.jsonl', {'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'phase': PHASE['phase'], 'trial': PHASE['trial'], 'kind': 'SystemExit', 'message': str(exc.code), 'guard_run_id': guard_run_id(), 'pid': os.getpid()})
            except Exception: pass
            raise SystemExit(3)
        raise
    except BaseException as exc:                                                                                                     # F16: process fault record
        try: append(Path(args.root)/'faults.jsonl', {'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'phase': PHASE['phase'], 'trial': PHASE['trial'], 'kind': type(exc).__name__, 'message': str(exc), 'traceback': traceback.format_exc()[-4000:], 'guard_run_id': guard_run_id(), 'pid': os.getpid()})
        except Exception: pass
        traceback.print_exc(); raise SystemExit(3)

if __name__ == '__main__': main()
