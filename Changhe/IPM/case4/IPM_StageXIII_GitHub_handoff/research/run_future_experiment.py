#!/usr/bin/env python3
"""Explicit future run, gated by this machine's successful saved-candidate check.

This script is delivered for later use. Migration preparation never invokes it.
It does not choose an experiment, change solver settings, or discard counters.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--verification', type=Path, required=True)
    p.add_argument('--session-dir', type=Path, required=True)
    p.add_argument('--work-dir', type=Path, required=True)
    p.add_argument('--label', default='future_experiment')
    p.add_argument('command', nargs=argparse.REMAINDER)
    a = p.parse_args()
    report = json.loads(a.verification.read_text())
    if report.get('mode') != 'candidates' or not report.get('passed') or set(report.get('cases', {})) != {'original', 'final', 'five'}:
        p.error('a passed full final/five/Stage IX candidate verification is required')
    if report.get('hostname') != platform.node():
        p.error('verification must have been produced on this host; rerun reproduce.sh here')
    import numpy
    import scipy
    import scipy.linalg  # Load the SciPy BLAS runtime, as the verifier does.
    from threadpoolctl import threadpool_info, threadpool_limits
    if (report['python'], report['numpy'], report['scipy'], report['platform']) != (
            platform.python_version(), numpy.__version__, scipy.__version__, platform.platform()):
        p.error('current numerical environment differs from verification')
    with threadpool_limits(limits=1):
        current_pools = threadpool_info()
    pool_identity = lambda rows: sorted((r.get('internal_api', ''), r.get('version', ''), r.get('architecture', '')) for r in rows)
    if pool_identity(current_pools) != pool_identity(report['threadpools']):
        p.error('BLAS runtime differs from verification')
    verifier = HERE / 'base/reproduction/verify_candidates.py'
    if hashlib.sha256(verifier.read_bytes()).hexdigest() != report.get('verifier_sha256'):
        p.error('verification code changed; rerun the benchmark')
    source_dir = HERE / 'base/engine'
    sources = {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in source_dir.glob('*.py')}
    if sources != report.get('portable_source_sha256'):
        p.error('portable numerical code changed; rerun the benchmark')
    for label in ('final', 'five', 'original'):
        source = source_dir / ('inputs/start_original.json' if label == 'original' else 'reference_results/' + label + '.json')
        if hashlib.sha256(source.read_bytes()).hexdigest() != report['cases'][label]['input_sha256']:
            p.error('reference candidate changed since verification')
    work = a.work_dir.expanduser().resolve()
    forbidden = [HERE / 'engine'] + list(HERE.parent.glob('pilot_y_branch*'))
    if any(work == f.resolve() or f.resolve() in work.parents for f in forbidden):
        p.error('work directory must be separate from preserved research and references')
    if not (work / 'workspace.json').exists():
        p.error('initialize an isolated numerical workspace with prepare_workspace.py first')
    command = a.command[1:] if a.command[:1] == ['--'] else a.command
    if not command:
        p.error('explicit future worker command is required after --')
    env = dict(os.environ, IPM_WORK_DIR=str(work), PYTHONDONTWRITEBYTECODE='1')
    work.joinpath('future_run_gate_' + str(time.time_ns()) + '.json').write_text(json.dumps({
        'verification_sha256': hashlib.sha256(a.verification.read_bytes()).hexdigest(),
        'hostname': platform.node(), 'command': command, 'timestamp': time.time()}, indent=2) + '\n')
    raise SystemExit(subprocess.call([sys.executable, '-B', str(HERE / 'hardware/guard.py'), 'run',
        '--session-dir', str(a.session_dir.resolve()), '--cwd', str(work), '--label', a.label, '--'] + command,
        env=env))


if __name__ == '__main__':
    main()
