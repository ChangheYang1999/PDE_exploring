#!/usr/bin/env python3
"""Fresh single-CPU reproduction of the retained R5 rejection; installs nothing."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, importlib.metadata, json, math, os, signal, subprocess, sys, time
from artifact_tool import verify
ROOT = Path(__file__).resolve().parent
BASE = ROOT / 'axisymmetric_euler_24h'
EXPECTED_COEFFICIENT = '12dfdcbfd44247669d19a0c0ab7e81bfa22ec0dcb6abd052e0633aa682d9830b'
EXPECTED_RHO = 1.793889555852889
EXPECTED_M = 8.565619692094037

def run_bounded(command, log, env, timeout):
    child = subprocess.Popen(command, cwd=ROOT, env=env, stdout=log,
                             stderr=subprocess.STDOUT, start_new_session=True)
    previous = {}
    def interrupted(signum, frame):
        raise InterruptedError('Reproduction received signal ' + str(signum))
    for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP]:
        previous[sig] = signal.signal(sig, interrupted)
    try:
        return child.wait(timeout=timeout)
    finally:
        if child.poll() is None:
            os.killpg(child.pid, signal.SIGTERM)
            try:
                child.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid, signal.SIGKILL)
                child.wait()
        for sig, handler in previous.items():
            signal.signal(sig, handler)


def main():
    start = time.perf_counter()
    if len(sys.argv) != 1:
        raise ValueError('No arguments: every invocation creates a new output directory.')
    if hasattr(os, 'sched_getaffinity'):
        core = min(os.sched_getaffinity(0))
        os.sched_setaffinity(0, {core})
    else:
        core = None
    if hasattr(os, 'nice'):
        current = os.nice(0)
        if current < 19:
            os.nice(19 - current)
    integrity = verify()
    versions = {name: importlib.metadata.version(name) for name in ['numpy', 'scipy']}
    env = os.environ.copy()
    env.update(CUDA_VISIBLE_DEVICES='', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
               MKL_NUM_THREADS='1', NUMEXPR_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1',
               PYTHONDONTWRITEBYTECODE='1', MPLBACKEND='Agg')
    cache = BASE / 'environment' / 'reproduction_cache'
    cache.mkdir(parents=True, exist_ok=True)
    env.update(TMPDIR=str(cache), MPLCONFIGDIR=str(cache / 'matplotlib'),
               XDG_CACHE_HOME=str(cache),
               PYTHONPATH=os.pathsep.join([str(BASE), str(BASE / 'src')]))
    export = BASE / 'external_exports' / 'T1_ladder_L4rm5_20261029T024821.564842Z'
    coefficient = export / 'coeffs.npz'
    if hashlib.sha256(coefficient.read_bytes()).hexdigest() != EXPECTED_COEFFICIENT:
        raise ValueError('R5 coefficient identity mismatch')
    now = datetime.now(timezone.utc)
    parent = BASE / 'results' / 'reproductions' / ('r5_' + now.strftime('%Y%m%dT%H%M%S.%fZ'))
    parent.mkdir(parents=True, exist_ok=False)
    driver = parent / 'driver'
    record = dict(started_utc=now.isoformat(), status='RUNNING', cpu_core=core,
                  python=sys.version, packages=versions, integrity=integrity,
                  expected_coefficient_sha256=EXPECTED_COEFFICIENT)
    output = parent / 'reproduction.json'
    output.write_text(json.dumps(record, indent=2) + '\n')
    try:
        command = [sys.executable, str(BASE / 'validate_export_native.py'), str(export),
                   '--output', str(driver)]
        with (parent / 'validation.log').open('xb') as log:
            code = run_bounded(command, log, env, 1800)
        if code != 2:
            raise RuntimeError('Expected completed rejection (driver exit 2), got ' + str(code))
        with (parent / 'collection.log').open('xb') as log:
            collection_code = run_bounded([sys.executable, str(BASE / 'collect_registered_arrays.py'), str(driver)], log, env, 300)
            if collection_code != 0:
                raise RuntimeError('Collector failed: ' + str(collection_code))
        summary = json.loads((driver / 'summary.json').read_text())
        collected = json.loads((driver / 'array_collection.json').read_text())
        if summary['status'] != 'REJECTED_BY_REQUIRED_CHECKS' or not collected['all_passed']:
            raise RuntimeError('Unexpected validation or collection status')
        if collected['candidate_sha256'] != EXPECTED_COEFFICIENT:
            raise RuntimeError('Collector coefficient identity mismatch')
        for key, target in [('rho_max', EXPECTED_RHO), ('m_max', EXPECTED_M)]:
            if not math.isclose(summary['aggregate'][key], target, rel_tol=2e-10, abs_tol=2e-12):
                raise RuntimeError('Retained metric changed: ' + key)
        record.update(status='PASS: R5 rejection reproduced', driver_exit_code=code,
                      collected_checks=collected['check_count'], aggregate=summary['aggregate'],
                      output=str(parent.relative_to(ROOT)),
                      scope='Fresh 57-row registered check and 684-array collection. A reproduced rejection is not an accepted Euler profile or a uniform residual certificate.')
    except BaseException as exc:
        record.update(status='FAILED', error=repr(exc))
        raise
    finally:
        record.update(completed_utc=datetime.now(timezone.utc).isoformat(),
                      wall_seconds=time.perf_counter() - start)
        output.write_text(json.dumps(record, indent=2) + '\n')
        print(json.dumps(record, indent=2), flush=True)

if __name__ == '__main__':
    main()
