"""SPEC section 16 benchmarks on the seed (G3 step bench), version 3 (lead pre-audit 10:07Z F9-F18; E1/E2):
each (workers, cache_threads) configuration runs in a FRESH CHILD PROCESS (one cache alive at a time, per-configuration peak RSS/PSS), with the model built at the
configured thread count (truthful key 'cache_threads'); timed rows carry wall, family CPU (psutil self+children user+system plus RUSAGE_CHILDREN), peak family PSS and
RSS sum from a background smaps_rollup sampler (timer stopped inside the sampler block; PSS read failures counted, a parent read failure fails the step); fun rows are
labelled by the observed change of model.cache_builds; the driver sequence is timed explicitly (trust step with its metadata, KKT, lift, condition_sums, validate with
coarse_r and prediction, Chart860, warm Jacobian, SVD, stationarity) and the per-trial estimates follow that sequence at the production pair; three full section 13
assessments (assess860 as the cadence invokes it) and three R_f spot checks (assess860 --spot-only) are timed at the production configuration; medians and ranges of
wall, cpu_s and peak PSS are reported; the step emits strict-verdict checks.
Version 3b (lead 10:50Z/10:58Z/11:01Z items A(c), E2, E3, E5, E9, E11, E12, N10, N12): terminal records need completeness.failed exactly False in BOTH modes;
the sampler thread takes its first sample before the timer starts (the caller waits for it, 5 s timeout) and counts loop samples separately from the exit read; every timed row and every terminal record must satisfy row_sampled_ok (SPEC v9.20) (family-wide child read failures are
recorded, not gated); integral rows record target_error_abs and training_J_abs beside the acceptance tolerance; configuration children capture a stderr tail and
every json.loads of a child or assessment output is guarded and every child record is validated against its full schema before it counts (E5 (a)); the configuration loop and the gate computation run inside one guarded block, so a malformed or structurally wrong record or an exception is a failed record or a failed check and the step JSON is still written with passed False (E5 (b)); every operation kind records
timed calls of total calls; nonfinite or negative times fail; the step JSON has no bare NaN/Infinity (sanitized, allow_nan=False) and is fsynced.
Usage: bench860.py <out.json> <manifest.json> <workers...> [--threads T] [--assessments N] [--dry-run]
       (internal) bench860.py --child <workers> <threads> <partial.json> <manifest.json>"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, resource, sys, time, gc, os, threading, subprocess, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np, psutil
import basis860 as B, chart860 as C
from model860 import Model860, feasible_matrix
from integrate860 import Integrator860
from stage13_solver import DenseTrustModel
from absolute_common import ROOT, A_REF, read, digest
from absolute_model import FrozenLogMesh
from closure860 import loaded_closure
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools')); from runtime import Runtime
HERE = Path(__file__).resolve().parent; LANE = Path((_artifact_root))     # fixed lane root (defect 15: resolves in the pending and the frozen layout)
SEED_JSON = LANE/'outputs/campaign860/seed/seed_860.json'

def family_pss_mib():
    """(pss_mib, rss_sum_mib, failures, parent_failed) from /proc/<pid>/smaps_rollup over this process and live children."""
    total = 0.; rss_sum = 0.; failures = 0; parent_failed = False; me = psutil.Process()
    for proc in [me]+me.children(recursive=True):
        try:
            with open('/proc/%d/smaps_rollup' % proc.pid) as fh:
                for line in fh:
                    if line.startswith('Pss:'): total += float(line.split()[1])/1024.
                    elif line.startswith('Rss:'): rss_sum += float(line.split()[1])/1024.
        except Exception:
            failures += 1
            if proc.pid == me.pid: parent_failed = True
    return total, rss_sum, failures, parent_failed

class PssSampler:
    def __init__(self): self.peak_pss = 0.; self.peak_rss = 0.; self.samples = 0; self.loop_samples = 0; self.exit_samples = 0; self.failures = 0; self.parent_failed = False; self.first_sample_before_timer = False; self._stop = threading.Event(); self._first = threading.Event(); self._t = threading.Thread(target=self._run, daemon=True)
    def _sample(self, loop):
        pss, rs, fails, pf = family_pss_mib(); self.peak_pss = max(self.peak_pss, pss); self.peak_rss = max(self.peak_rss, rs); self.samples += 1; self.failures += fails; self.parent_failed = self.parent_failed or pf
        if loop: self.loop_samples += 1          # E2: periodic-loop samples counted separately from the exit read
        else: self.exit_samples += 1
    def _run(self):
        self._sample(True); self._first.set()                                   # the thread's own first sample; __enter__ waits for it (SPEC v9.20)
        while not self._stop.wait(.5): self._sample(True)
    def __enter__(self): self._t.start(); self.first_sample_before_timer = bool(self._first.wait(5.)); return self      # the timer of the caller starts only after this returns
    def __exit__(self, *a): self._stop.set(); self._t.join(timeout=5); self._sample(False)
    def record(self): return {'peak_family_pss_mib': self.peak_pss, 'peak_family_rss_sum_mib': self.peak_rss, 'pss_samples': self.samples, 'pss_loop_samples': self.loop_samples, 'pss_exit_samples': self.exit_samples, 'pss_thread_first_sample_before_timer': self.first_sample_before_timer, 'pss_read_failures': self.failures, 'pss_parent_read_failed': self.parent_failed}

def cpu():
    total = 0.; me = psutil.Process()
    for proc in [me]+me.children(recursive=True):
        try: ct = proc.cpu_times(); total += ct.user+ct.system
        except Exception: pass
    rc = resource.getrusage(resource.RUSAGE_CHILDREN); return total+rc.ru_utime+rc.ru_stime

def timed(fn, **labels):
    with PssSampler() as ps:
        t0 = time.perf_counter(); c0 = cpu(); v = fn(); wall = time.perf_counter()-t0; cpu_s = cpu()-c0          # F16: the timer stops inside the sampler block
    return v, {'wall_s': wall, 'cpu_s': cpu_s, 'cpu_s_definition': 'process family: psutil user+system of self and live children plus RUSAGE_CHILDREN of reaped children', **ps.record(), **labels}

def row_sampled_ok(x):
    """SPEC v9.20 section 16 (lead 11:27Z): a timed row counts only if its sampling thread took a typed int pss_loop_samples >= 1, its first sample came before the timer
    started (pss_thread_first_sample_before_timer True), exactly one exit read was taken, the parent read never failed, and, when wall_s >= 1.0, at least two loop
    samples exist (the thread stayed active during a long operation; SPEC v9.22: sample counts do not show that a sample fell inside the operation)."""
    if not isinstance(x, dict): return False
    n = x.get('pss_loop_samples'); w = x.get('wall_s')
    return bool(type(n) is int and n >= 1 and x.get('pss_thread_first_sample_before_timer') is True and type(x.get('pss_exit_samples')) is int and x['pss_exit_samples'] == 1 and x.get('pss_parent_read_failed') is False
                and (n >= 2 or not (time_ok(w) and float(w) >= 1.0)))

SAMPLING_STATEMENT = 'memory is sampled by a thread every 0.5 s during each timed operation, with the thread first sample before the timer starts and one exit read after it; thread-sample counts show the sampler was active, not that a sample fell inside the timed operation; a sampled maximum is an observed peak, not an upper bound; for an operation shorter than the sampling interval its memory may not have been observed; the reported peak is the maximum of the samples taken by the row thread and the configuration-level sampler (SPEC v9.22 section 16)'

def time_ok(x):
    """E11: an operation time counts only if it is a finite, nonnegative real number (bool excluded)."""
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(float(x)) and float(x) >= 0.

def terminal_ok(a, mode):
    """ruling 2 / A(c) / E2 / E11: a terminal record (full assessment or spot check) counts only if: returncode is the int 0 (not a bool); the output file exists and its
    sha256 equals both the recorded and the read-back digests; wall and CPU times are finite and nonnegative; at least one periodic-loop sampler sample was taken and the
    parent self-read never failed (family-wide child read failures are recorded, not gated); mode equals the expected mode with is_full_assessment consistent; and
    completeness.failed is exactly the boolean False in BOTH modes (a spot record's failed refers to the spot-only required set)."""
    if not isinstance(a, dict): return False
    rcode = a.get('returncode')
    try: sha_file = digest(a['output']) if isinstance(a.get('output'), str) and Path(a['output']).exists() else None
    except Exception: sha_file = None
    return bool(type(rcode) is int and rcode == 0 and isinstance(a.get('output_sha256'), str) and a.get('output_sha256_read_back') == a['output_sha256'] and sha_file == a['output_sha256']
                and time_ok(a.get('wall_s')) and time_ok(a.get('cpu_s')) and row_sampled_ok(a)
                and a.get('mode') == mode and a.get('is_full_assessment') is (mode == 'full') and a.get('failed') is False)

def sanitize(value, key=None):
    """E9: no bare NaN/Infinity in the step JSON: nonfinite floats become null with a sibling '<key>_nonfinite' classification (dicts) or {'nonfinite': kind} (lists)."""
    if isinstance(value, np.floating): value = float(value)
    if isinstance(value, np.integer): return int(value)
    if isinstance(value, np.bool_): return bool(value)
    if isinstance(value, np.ndarray): value = value.tolist()
    if isinstance(value, float): return value if math.isfinite(value) else None
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            if isinstance(v, (float, np.floating)) and not math.isfinite(float(v)): out[k] = None; out[str(k)+'_nonfinite'] = 'nan' if math.isnan(float(v)) else ('+inf' if v > 0 else '-inf')
            else: out[k] = sanitize(v, k)
        return out
    if isinstance(value, (list, tuple)): return [({'nonfinite': 'nan' if math.isnan(float(v)) else ('+inf' if v > 0 else '-inf')} if isinstance(v, (float, np.floating)) and not math.isfinite(float(v)) else sanitize(v)) for v in value]
    return value

def fsync_write_json(path, obj):
    """N10 / E9: the step JSON is sanitized, dumped with allow_nan=False, written to a temporary name, fsynced and renamed."""
    tmp = Path(path).with_name(Path(path).name+'.partial'); text = json.dumps(sanitize(obj), indent=1, default=str, allow_nan=False)+'\n'
    with tmp.open('w') as f: f.write(text); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)

def validate_child_record(rec):
    """E5 (a): full schema of a configuration child record before it enters ok_runs; returns None or the first failing field. configuration: dict; rows: dict with exactly
    the planned kinds, each a list of dicts; counts: dict of ints over the planned kinds; stats: dict with every planned kind as a dict carrying wall_s.median; calls_total
    and calls_timed_of_total present; pss_parent_read_failed a bool."""
    if not isinstance(rec, dict): return 'record is not an object'
    if not isinstance(rec.get('configuration'), dict): return 'configuration'
    rows = rec.get('rows')
    if not isinstance(rows, dict) or set(rows) != set(PLANNED): return 'rows'
    for k, v in rows.items():
        if not isinstance(v, list) or not all(isinstance(x, dict) for x in v): return 'rows.%s' % k
    counts = rec.get('counts')
    if not isinstance(counts, dict) or set(counts) != set(PLANNED) or not all(type(v) is int for v in counts.values()): return 'counts'
    st = rec.get('stats')
    if not isinstance(st, dict) or not set(PLANNED) <= set(st): return 'stats'
    for k in PLANNED:
        if not (isinstance(st[k], dict) and isinstance(st[k].get('wall_s'), dict) and 'median' in st[k]['wall_s']): return 'stats.%s' % k
    for k in ('calls_total', 'calls_timed_of_total'):
        if k not in rec: return k
    if not isinstance(rec.get('pss_parent_read_failed'), bool): return 'pss_parent_read_failed'
    return None

def stats(rows, key):
    vals = [r[key] for r in rows if isinstance(r.get(key), (int, float))]
    return {'median': float(np.median(vals)) if vals else None, 'min': float(min(vals)) if vals else None, 'max': float(max(vals)) if vals else None, 'n': len(vals)}

PLANNED = {'fun': 5, 'jacobian_warm': 3, 'jacobian_rebuild': 2, 'svd': 3, 'trust': 3, 'kkt': 3, 'lift': 3, 'condition_sums': 3, 'chart': 1, 'stationarity': 3, 'integral': 3, 'io': 3}   # ruling 1: defined once, used by the loops and the gate
SPEC16_MINIMA = {'fun': 5, 'jacobian': 3, 'svd': 3, 'trust': 3, 'integral': 3}
N_ASSESS = 3

def child(w, th, partial, manifest):
    rt = Runtime(str(HERE.parent)); state = rt.read(ROOT/'campaign/global181_v3/state.json'); epoch = rt.read(state['epoch_path'])
    mesh = FrozenLogMesh.load(epoch['meshes']['training']['path']); sd = np.load(B.REPLAY_REFERENCE_FILE); P = sd['P'].copy(); high = sd['high'].copy(); rng = np.random.default_rng(16)
    rows = {k: [] for k in ('fun', 'jacobian_warm', 'jacobian_rebuild', 'svd', 'trust', 'kkt', 'lift', 'condition_sums', 'chart', 'stationarity', 'integral', 'io')}
    CALLS = {k: 0 for k in rows}                                                                             # E12: total calls per kind (timed and untimed), beside the timed count len(rows[k])
    def count(kind, fn):
        CALLS[kind] += 1; return fn()
    model = Model860(mesh, A_REF, block_size=4096, mode_block=64, workers=w, threads=th)                     # F15: the model built at the configured thread count
    def builds(): return model.cache_record().get('cache_builds', 0)
    b0 = builds(); r, t = timed(lambda: count('fun', lambda: model.fun(P, high))); t.update(cache_builds_delta=builds()-b0, label='observed: cold cache build at %d threads' % th if builds()-b0 else 'observed: cached basis'); rows['fun'].append(t)
    chart, t = timed(lambda: count('chart', lambda: C.Chart860(P))); rows['chart'].append(t)
    # ruling 4: three WARM Jacobians, each right after a fun at the same key (the driver's acceptance path), plus the two rebuild Jacobians labelled separately
    def jac_row(t, b0, context):                                                                            # fix check 3 minor: row kind, CALLS key and label all derive from the observed cache_builds change
        kind = 'jacobian_warm' if builds() == b0 else 'jacobian_rebuild'; CALLS[kind] += 1
        t.update(cache_builds_delta=builds()-b0, label=('warm Jacobian at the key just evaluated by fun (%s)' if kind == 'jacobian_warm' else 'Jacobian with a cache rebuild (%s)') % context); rows[kind].append(t)
    b0 = builds(); J, t = timed(lambda: model.jacobian(P, high)); jac_row(t, b0, 'seed')
    for k in (1, 2):
        Pk = P.copy(); Pk[0] *= 1+1e-9*k; b0 = builds(); Jk, t = timed(lambda: model.jacobian(Pk, high)); jac_row(t, b0, 'c_l perturbed %d, first call' % k); del Jk
        b0 = builds(); _ = count('fun', lambda: model.fun(Pk, high)); Jw, t = timed(lambda: model.jacobian(Pk, high)); jac_row(t, b0, 'c_l perturbed %d, after fun' % k); del Jw
    b0 = builds(); r_again, t = timed(lambda: count('fun', lambda: model.fun(P, high))); t.update(cache_builds_delta=builds()-b0, label='observed: cold cache build (c_l changed back)' if builds() > b0 else 'observed: cached basis'); rows['fun'].append(t)
    A, scales = feasible_matrix(J, chart); A_shape = list(A.shape); del J
    for k in range(3):
        f, t = timed(lambda: count('svd', lambda: DenseTrustModel(A, r))); t.update(factor_seconds=getattr(f, 'factor_seconds', None), A_shape=A_shape); rows['svd'].append(t)
        step_sub, t2 = timed(lambda: count('trust', lambda: f.step(.5*np.linalg.norm(r)*10**(-k)))); step, sub = step_sub; t2.update(radius=.5*np.linalg.norm(r)*10**(-k), metadata={kk: vv for kk, vv in sub.items() if not kk.startswith('svd_coordinate') and isinstance(vv, (int, float, bool, str))}); rows['trust'].append(t2)
        st, t3 = timed(lambda: count('stationarity', lambda: f.stationarity())); t3.update(indicator=st.get('full_range_projected_residual_relative')); rows['stationarity'].append(t3)
        def kkt():
            mu = sub.get('lagrange_multiplier'); response = A@step; gradient = A.T@r; rg = A.T@response; return float(np.linalg.norm(gradient+rg+(mu or 0.)*step)/max(np.linalg.norm(gradient), 1e-300))
        _, t4 = timed(lambda: count('kkt', kkt)); rows['kkt'].append(t4)
    integ = Integrator860(epoch, workers=w)
    for k in range(3):                                                                                           # F13 / defect 3: the driver sequence for a real trust-step trial with the GN prediction
        fk = count('svd', lambda: DenseTrustModel(A, r)); radius = .5*np.linalg.norm(r)*10**(-k); step, sub_ = count('trust', lambda: fk.step(radius)); pred = float(sub_['actual_matrix_predicted_decrease']); phys = step*scales
        Pp, t = timed(lambda: count('lift', lambda: chart.lift_delta(phys[:55]))); t.update(iterations=len(chart.last_diagnostics['iterations']), radius=radius); rows['lift'].append(t)
        hh = high+phys[55:]
        b0 = builds(); rr, t = timed(lambda: count('fun', lambda: model.fun(Pp, hh))); t.update(cache_builds_delta=builds()-b0, label='trial fun after a lift (c_l changes: cache rebuild)' if builds() > b0 else 'trial fun at the cached c_l'); rows['fun'].append(t)
        _, t = timed(lambda: count('condition_sums', lambda: model.condition_sums(Pp, hh))); rows['condition_sums'].append(t)
        v, t = timed(lambda: count('integral', lambda: integ.validate(Pp, hh, coarse_r=rr, predicted_reduction=pred, reference=None))); t.update(J_abs=v['J_abs'], error_abs=v['error_abs'], accuracy_passed=v['accuracy_passed'], requires_refinement=v.get('requires_refinement'), predicted_decrease_used=pred, acceptance_tolerance=v.get('accuracy_tolerance'), acceptance_tolerance_note='accuracy_tolerance of validate: the ACCEPTANCE tolerance on |J_training - J_independent|, not the integration target', target_error_abs=(v.get('independent_integral') or {}).get('target_error_abs'), training_J_abs=v.get('training_J_abs'), actual_mesh_decrease=float(r@r/2-rr@rr/2)); rows['integral'].append(t)   # E3
        del fk
    # ruling 5: commit I/O: three writes of a production-sized snapshot (P, high, residual, S_R, e; compressed npz) plus one event JSON, each fsynced, in a lane tmp dir
    import tempfile, hashlib as _hl
    from absolute_common import npz as _npz
    S_R_tmp = count('condition_sums', lambda: model.condition_sums(P, high)); e_tmp = model.root*S_R_tmp+2.**-53*abs(r)
    with tempfile.TemporaryDirectory(dir=str(LANE/'outputs/dev_v9')) as td:
        for k in range(3):
            def io_write():
                _npz(Path(td)/('snap_%d.npz' % k), P=P, high=high, residual=r, S_R=S_R_tmp, e=e_tmp)
                evp = Path(td)/('event_%d.json' % k); fd = os.open(str(evp), os.O_WRONLY|os.O_CREAT, 0o644); os.write(fd, json.dumps({'trial': k, 'post_state': {'P': P.tolist(), 'high': high.tolist(), 'objective': float(r@r/2)}, 'row': {'k': k}}).encode()); os.fsync(fd); os.close(fd)
                return str(evp)
            _, t = timed(lambda: count('io', io_write)); t.update(label='snapshot npz (5 arrays) + event JSON with fsync, lane tmp dir'); rows['io'].append(t)
    pss_now = family_pss_mib()
    rec = {'configuration': {'workers': w, 'cache_threads': th, 'block_size': 4096, 'mode_block': 64}, 'sampling_statement': SAMPLING_STATEMENT, 'rows': rows, 'cache_record': model.cache_record(), 'A_shape': A_shape,
           'peak_rss_mib_this_process': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 'peak_family_pss_mib': max(x['peak_family_pss_mib'] for v in rows.values() for x in v), 'peak_family_rss_sum_mib': max(x['peak_family_rss_sum_mib'] for v in rows.values() for x in v),
           'pss_read_failures': sum(x['pss_read_failures'] for v in rows.values() for x in v), 'pss_parent_read_failed': any(x['pss_parent_read_failed'] for v in rows.values() for x in v),
           'stats': {k: {'wall_s': stats(v, 'wall_s'), 'cpu_s': stats(v, 'cpu_s'), 'peak_family_pss_mib': stats(v, 'peak_family_pss_mib')} for k, v in rows.items()}, 'counts': {k: len(v) for k, v in rows.items()}, 'calls_total': dict(CALLS), 'calls_timed_of_total': {k: '%d timed of %d' % (len(rows[k]), CALLS[k]) for k in rows}, 'planned_counts': PLANNED,   # E12
           'child_import_closure': loaded_closure(), 'child_cpu_total_s_rusage_self_plus_children': (lambda ru, rc: ru.ru_utime+ru.ru_stime+rc.ru_utime+rc.ru_stime)(resource.getrusage(resource.RUSAGE_SELF), resource.getrusage(resource.RUSAGE_CHILDREN))}
    fsync_write_json(partial, rec); print(json.dumps({'child': w, 'threads': th, 'medians_wall_s': {k: rec['stats'][k]['wall_s']['median'] for k in rows}, 'peak_family_pss_mib': rec['peak_family_pss_mib']}), flush=True)

def main():
    argv = sys.argv[1:]
    if argv and argv[0] == '--child': child(int(argv[1]), int(argv[2]), argv[3], argv[4]); return
    DRY = '--dry-run' in argv; argv = [a for a in argv if a != '--dry-run']
    th_opt = int(argv[argv.index('--threads')+1]) if '--threads' in argv else None
    n_assess = int(argv[argv.index('--assessments')+1]) if '--assessments' in argv else N_ASSESS
    plain = [a for i, a in enumerate(argv) if not (a in ('--threads', '--assessments') or (i > 0 and argv[i-1] in ('--threads', '--assessments')))]
    out_path = Path(plain[0]); manifest = Path(plain[1]); worker_list = [int(v) for v in plain[2:]] or [8]
    out = {'schema': 'bench860_v3', 'code_manifest_sha256': digest(manifest), 'basis_version': B.VERSION, 'began_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'runs': {}, 'checks': [], 'sampling_statement': SAMPLING_STATEMENT}
    def check(name, value, tol=None, **extra):
        if any(c['check'] == name for c in out['checks']): raise RuntimeError('duplicate check name %s' % name)
        ok = bool(value <= tol) if tol is not None else bool(value)
        out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
    rt = Runtime(str(HERE.parent)); state = rt.read(ROOT/'campaign/global181_v3/state.json'); epoch = rt.read(state['epoch_path']); FrozenLogMesh.load(epoch['meshes']['training']['path']); np.load(B.REPLAY_REFERENCE_FILE)
    if DRY: print('DRY RUN OK: imports, epoch, mesh and replay reference resolve', flush=True); raise SystemExit(0)
    def _configurations_and_gates():                                                                             # E5 (b): any exception here becomes a failed check; the step JSON is still written
        pairs = [(w, th_opt if th_opt else min(w, 4)) for w in worker_list]
        if (8, 4) not in pairs and 8 in worker_list: pairs.append((8, 4))
        for w, th in pairs:                                                                                            # F11: one configuration per fresh child process
            partial = out_path.with_name(out_path.stem+'.child_w%d_t%d.json' % (w, th)); t0 = time.time(); rc0 = resource.getrusage(resource.RUSAGE_CHILDREN)
            with PssSampler() as ps: rc = subprocess.run([sys.executable, '-B', str(Path(__file__).resolve()), '--child', str(w), str(th), str(partial), str(manifest)], env=dict(os.environ), capture_output=True, text=True)   # E5: stderr captured
            sys.stdout.write(rc.stdout[-4000:]); sys.stdout.flush()
            rc1 = resource.getrusage(resource.RUSAGE_CHILDREN); child_cpu = (rc1.ru_utime+rc1.ru_stime)-(rc0.ru_utime+rc0.ru_stime)
            key = 'w%d_t%d' % (w, th)
            if rc.returncode != 0 or not partial.exists(): out['runs'][key] = {'failed': True, 'returncode': rc.returncode, 'partial_exists': partial.exists(), 'stderr_tail': rc.stderr[-2000:], 'reason': 'child exited %d' % rc.returncode if rc.returncode != 0 else 'child wrote no record'}; continue
            try: rec = json.loads(partial.read_text()); assert isinstance(rec, dict) and 'rows' in rec and 'counts' in rec and 'configuration' in rec
            except Exception as exc: out['runs'][key] = {'failed': True, 'returncode': rc.returncode, 'stderr_tail': rc.stderr[-2000:], 'reason': 'child record unreadable or incomplete: %s: %s' % (type(exc).__name__, exc)}; continue   # E5
            bad = validate_child_record(rec)
            if bad: out['runs'][key] = {'failed': True, 'returncode': rc.returncode, 'stderr_tail': rc.stderr[-2000:], 'reason': 'child record failed schema validation at field %s' % bad}; continue    # E5 (a)
            try:
              rec.update(stderr_tail=rc.stderr[-2000:] if rc.stderr else None); rec.update(child_wall_s=time.time()-t0, child_cpu_total_s_from_parent_rusage_children=child_cpu, child_peak_family_pss_mib_from_parent=ps.peak_pss, child_peak_family_rss_sum_mib_from_parent=ps.peak_rss, parent_sampler_failures=ps.failures, parent_sampler_loop_samples=ps.loop_samples, parent_sampler_parent_read_failed=ps.parent_failed, partial_json=str(partial), partial_sha256=digest(partial))
              out['runs'][key] = rec
            except Exception as exc: out['runs'][key] = {'failed': True, 'returncode': rc.returncode, 'reason': 'child record postprocessing failed: %s: %s' % (type(exc).__name__, exc)}    # E5 (b)
        # section 13 assessments and R_f spot checks at the production configuration (F12)
        prod = [k for k in out['runs'] if k.startswith('w8_t4') and not out['runs'][k].get('failed')]; pw = 8                     # defect 9: assessments at the production worker count regardless
        out['assessments'] = []; out['spot_checks'] = []
        def timed_subprocess(cmd, output):
            with PssSampler() as ps:
                t0 = time.perf_counter(); c0 = cpu(); rc = subprocess.run(cmd, env=dict(os.environ), capture_output=True, text=True); wall = time.perf_counter()-t0; cpu_s = cpu()-c0      # ruling 6: timer inside the sampler block
            rec = {'wall_s': wall, 'cpu_s': cpu_s, 'returncode': rc.returncode, 'output': str(output), 'output_sha256': digest(output) if output.exists() else None, **ps.record(), 'workers': pw, 'stderr_tail': rc.stderr[-2000:] if (rc.returncode or rc.stderr) else None}
            if output.exists():
                try:
                    d_ = json.loads(output.read_text()); comp = d_.get('completeness_v913') if isinstance(d_, dict) else None; comp = comp if isinstance(comp, dict) else {}
                    rec.update(mode=comp.get('mode'), is_full_assessment=comp.get('is_full_assessment'), failed=comp.get('failed', 'missing'), output_sha256_read_back=digest(output))   # raw typed values (A(c): failed must be exactly False)
                except Exception as exc: rec.update(mode=None, is_full_assessment=None, failed='unreadable: %s: %s' % (type(exc).__name__, exc), output_sha256_read_back=None)   # E5: guarded
            else: rec.update(mode=None, is_full_assessment=None, failed='no output file')
            return rec
        for i in range(n_assess):
            o = out_path.with_name(out_path.stem+'.assess_%d.json' % i); out['assessments'].append(timed_subprocess([sys.executable, '-B', str(HERE/'assess860.py'), str(o), str(manifest), str(SEED_JSON), str(pw)], o))
            o2 = out_path.with_name(out_path.stem+'.spot_%d.json' % i); out['spot_checks'].append(timed_subprocess([sys.executable, '-B', str(HERE/'assess860.py'), str(o2), str(manifest), str(SEED_JSON), str(pw), '--spot-only'], o2))
        out['assessment_stats'] = {'full_assessment_wall_s': stats(out['assessments'], 'wall_s'), 'full_assessment_cpu_s': stats(out['assessments'], 'cpu_s'), 'spot_check_wall_s': stats(out['spot_checks'], 'wall_s'), 'spot_check_cpu_s': stats(out['spot_checks'], 'cpu_s'), 'spot_check_scope': 'section 13 R_f spot check only (--spot-only: no integral, no exact far field, no large-r check)', 'spot_check_input': 'seed, no saved arrays: each spot run builds a training-mesh Model860 for the production batch arrays (N12); a campaign snapshot with saved arrays skips that build'}
        # per-trial estimate at the production pair (F13): driver sequence
        if not prod: out['per_trial_estimate_s'] = {'unavailable': 'the production configuration (8, 4) did not complete; no estimate'}
        if prod:
            m = {k: out['runs'][prod[0]]['stats'][k]['wall_s']['median'] for k in out['runs'][prod[0]]['stats']}
            rebuild_fun = [x['wall_s'] for x in out['runs'][prod[0]]['rows']['fun'][1:] if x.get('cache_builds_delta')]            # defect 5: the cold first build excluded
            io_med = m.get('io') or 0.
            rejected = (m['trust'] or 0)+(m['kkt'] or 0)+(m['lift'] or 0)+(float(np.median(rebuild_fun)) if rebuild_fun else (m['fun'] or 0))+(m['condition_sums'] or 0)+(m['integral'] or 0)+io_med
            accepted = rejected+(m['chart'] or 0)+(m['jacobian_warm'] or 0)+(m['svd'] or 0)+(m['stationarity'] or 0)+io_med
            out['per_trial_estimate_s'] = {'production_pair': out['runs'][prod[0]]['configuration'], 'rejected_lift_feasible_trial': rejected, 'accepted_trial': accepted, 'io_measured_median_s': io_med,
                                           'sequence': 'rejected: trust step + KKT + lift + trial fun (cache rebuild at the configured threads) + condition_sums + validate(coarse_r, prediction) + measured commit I/O; accepted adds Chart860 + WARM Jacobian (median of the warm rows) + SVD + stationarity + snapshot I/O (F13, rulings 4 and 5)', 'medians_used_s': m, 'rebuild_fun_median_s': float(np.median(rebuild_fun)) if rebuild_fun else None,
                                           'counts_multiplied': {'rejected': {'trust': 1, 'kkt': 1, 'lift': 1, 'fun_rebuild': 1, 'condition_sums': 1, 'integral': 1, 'io': 1}, 'accepted_adds': {'chart': 1, 'jacobian_warm': 1, 'svd': 1, 'stationarity': 1, 'io': 1}}, 'medians_are_of_timed_calls': out['runs'][prod[0]].get('calls_timed_of_total'), 'note': 'E12: each median is over the timed calls of its kind (timed of total shown); the estimate multiplies each median by the per-trial count of the driver sequence'}
        out['memory_basis_for_G4_limit'] = {'rule': 'lead checklist E1: the G4 family RSS limit rests on the measured peak family PSS (smaps_rollup) at the production worker count; the RSS sum (copy-on-write pages counted per child) is shown for comparison',
                                            'per_configuration': {k: {'peak_family_pss_mib': v.get('peak_family_pss_mib'), 'peak_family_rss_sum_mib': v.get('peak_family_rss_sum_mib'), 'peak_rss_mib_this_process': v.get('peak_rss_mib_this_process')} for k, v in out['runs'].items() if not v.get('failed')}}
        # checks (F9)
        ok_runs = {k: v for k, v in out['runs'].items() if not v.get('failed')}
        check('bench_all_configurations_completed', len(ok_runs) == len(pairs) and len(ok_runs) > 0, configurations=[v['configuration'] for v in ok_runs.values()])
        def jac_count(v): return v['counts']['jacobian_warm']+v['counts']['jacobian_rebuild']
        check('bench_spec16_minimum_counts', all(v['counts']['fun'] >= SPEC16_MINIMA['fun'] and jac_count(v) >= SPEC16_MINIMA['jacobian'] and v['counts']['svd'] >= SPEC16_MINIMA['svd'] and v['counts']['trust'] >= SPEC16_MINIMA['trust'] and v['counts']['integral'] >= SPEC16_MINIMA['integral'] for v in ok_runs.values()), minima=SPEC16_MINIMA)
        check('bench_observed_counts_equal_planned', all(v['counts'] == PLANNED for v in ok_runs.values()), planned=PLANNED, observed={k: v['counts'] for k, v in ok_runs.items()})
        check('bench_every_timed_row_sampled_ok', all(row_sampled_ok(x) for v in ok_runs.values() for rows in v['rows'].values() for x in rows) and all(row_sampled_ok(a) for a in out['assessments']+out['spot_checks']) and any(rows for v in ok_runs.values() for rows in v['rows'].values()), note='SPEC v9.20 section 16: every timed row of every configuration and every timed assessment subprocess row (verifier 11:21Z/11:25Z)')
        check('bench_timings_finite_and_nonnegative', all(time_ok(x.get('wall_s')) and time_ok(x.get('cpu_s')) for v in ok_runs.values() for rows in v['rows'].values() for x in rows), note='E11: a negative or nonfinite wall or CPU time fails')
        check('bench_integrals_accuracy_passed', all(x['accuracy_passed'] is True for v in ok_runs.values() for x in v['rows']['integral']))
        check('bench_pss_no_parent_read_failure', all(v['pss_parent_read_failed'] is False for v in ok_runs.values()) and all(a.get('parent_sampler_parent_read_failed') is False and (a.get('parent_sampler_loop_samples') or 0) >= 1 for a in ok_runs.values()), child_read_failures_reported={k: v['pss_read_failures'] for k, v in ok_runs.items()}, note='E2: gated on the parent self-read and at least one periodic-loop sample per configuration child; family-wide child read failures are reported, not gated (a pool worker can exit between children() and open(), defect 10)')
        check('bench_production_pair_present', any(v['configuration']['workers'] == 8 and v['configuration']['cache_threads'] == 4 for v in ok_runs.values()))
        check('bench_assessments_exactly_%d_complete_and_typed' % N_ASSESS, len(out['assessments']) == N_ASSESS and all(terminal_ok(a, 'full') for a in out['assessments']), n=len(out['assessments']))
        check('bench_spot_checks_exactly_%d_complete_and_typed' % N_ASSESS, len(out['spot_checks']) == N_ASSESS and all(terminal_ok(a, 'spot_only') for a in out['spot_checks']), n=len(out['spot_checks']))
        check('bench_processing_completed_without_exception', True)
    try: _configurations_and_gates()
    except Exception as exc: out['checks'].append({'check': 'bench_processing_completed_without_exception', 'value': False, 'tolerance': None, 'passed': False, 'exception': type(exc).__name__+': '+str(exc)}); print('bench processing failed:', type(exc).__name__, exc, flush=True)
    out['import_closure'] = loaded_closure(); out['passed'] = all(c['passed'] for c in out['checks']); out['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    fsync_write_json(out_path, out); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)      # E9 / N10

if __name__ == '__main__': main()
