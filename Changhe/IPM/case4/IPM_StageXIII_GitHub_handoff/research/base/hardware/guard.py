#!/usr/bin/env python3
"""Portable, exclusive, bounded single-worker supervisor; no numerical imports."""
import argparse
from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
from pathlib import Path
import platform
import signal
import subprocess
import sys
import time
import uuid

from policy import Policy, evaluate
from telemetry import family_metrics, snapshot

HERE = Path(__file__).resolve().parent
DEFAULT_LOCK = HERE / 'runtime' / 'worker.lock'
THREAD_VARIABLES = ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                    'VECLIB_MAXIMUM_THREADS', 'BLIS_NUM_THREADS', 'NUMEXPR_NUM_THREADS',
                    'GOTO_NUM_THREADS')


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.partial.' + str(os.getpid()))
    with temporary.open('w') as stream:
        json.dump(value, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def append_json(path, value):
    with Path(path).open('a') as stream:
        stream.write(json.dumps(value, sort_keys=True, allow_nan=False) + '\n')
        stream.flush()
        os.fsync(stream.fileno())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_session(directory):
    directory = Path(directory).resolve()
    session = json.loads((directory / 'session.json').read_text())
    if session.get('schema') != 1:
        raise ValueError('unsupported session schema')
    if digest(directory / 'policy.json') != session['policy_sha256']:
        raise ValueError('session policy changed; initialize a new resource session')
    if digest(directory / 'session_baseline.json') != session['baseline_sha256']:
        raise ValueError('session baseline changed; initialize a new resource session')
    return directory, session, Policy.from_dict(json.loads((directory / 'policy.json').read_text())), json.loads((directory / 'session_baseline.json').read_text())


@contextmanager
def exclusive_lock(path):
    path = Path(path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+') as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError('exclusive worker lock held; no worker started: ' + str(path))
        stream.seek(0)
        stream.truncate()
        stream.write(json.dumps({'supervisor_pid': os.getpid(), 'time': time.time()}) + '\n')
        stream.flush()
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def active_hold(directory):
    active = directory / 'ACTIVE_HOLD.json'
    if not active.exists():
        return None
    hold_hash = digest(active)
    acknowledgments = directory / 'hold_acknowledgments.jsonl'
    if acknowledgments.exists():
        for row in acknowledgments.read_text().splitlines():
            if json.loads(row).get('hold_sha256') == hold_hash:
                return None
    return hold_hash


def hold(directory, run_id, reasons, state):
    record = {'run_id': run_id, 'time': time.time(), 'reasons': reasons, 'snapshot': state}
    path = directory / 'holds' / (run_id + '.json')
    path.parent.mkdir(exist_ok=True)
    write_json(path, record)
    write_json(directory / 'ACTIVE_HOLD.json', record)


def collect(directory, cwd, child_pid=None):
    state = snapshot(cwd, child_pid, child_pid)
    import psutil
    session_free = psutil.disk_usage(str(directory)).free / 2 ** 30
    state['session_disk_free_gib'] = session_free
    state['disk_free_gib'] = min(state['disk_free_gib'], session_free)
    return state


def initialize(args):
    directory = Path(args.session_dir).resolve()
    if directory.exists() and any(directory.iterdir()):
        raise ValueError('session directory must be new or empty; prior baselines are immutable')
    policy = Policy.from_dict(json.loads(Path(args.policy).read_text())) if args.policy else Policy()
    directory.mkdir(parents=True, exist_ok=True)
    disk_path = Path(args.disk_path or directory).resolve()
    baseline = collect(directory, disk_path)
    write_json(directory / 'policy.json', policy.to_dict())
    write_json(directory / 'session_baseline.json', baseline)
    session = {'schema': 1, 'session_id': str(uuid.uuid4()), 'initialized_time': time.time(),
               'platform': platform.platform(), 'python': sys.version, 'python_executable': sys.executable,
               'hostname': platform.node(), 'disk_path': str(disk_path),
               'policy_sha256': digest(directory / 'policy.json'),
               'baseline_sha256': digest(directory / 'session_baseline.json'),
               'historical_hold_policy': 'Historical holds are audit records only; never read or applied.'}
    write_json(directory / 'session.json', session)
    decision = evaluate(baseline, baseline, None, policy)
    write_json(directory / 'initial_assessment.json', decision)
    print(json.dumps({'session_dir': str(directory), 'session_id': session['session_id'], 'initial_assessment': decision}))
    return 0


def acknowledge(args):
    with exclusive_lock(args.lock_file):
        directory, session, policy, baseline = load_session(args.session_dir)
        hold_hash = active_hold(directory)
        if hold_hash is None:
            raise ValueError('no unacknowledged current-session hold')
        state = collect(directory, Path(session['disk_path']))
        decision = evaluate(state, baseline, None, policy)
        if decision['stop']:
            raise RuntimeError('current resource conditions still fail policy: ' + '; '.join(decision['reasons']))
        append_json(directory / 'hold_acknowledgments.jsonl', {'time': time.time(), 'hold_sha256': hold_hash,
                    'reason': args.reason, 'snapshot': state, 'decision': decision})
        print(json.dumps({'acknowledged_hold_sha256': hold_hash, 'session_dir': str(directory)}))
    return 0


def send_group(pid, sig):
    try:
        os.killpg(pid, sig)
    except ProcessLookupError:
        pass


def stop_group(child, grace):
    """Signal entire group, allow checkpoint grace, then kill surviving members.

    Check the group even if its leader exits first; otherwise grandchildren can
    survive a superficially successful child.wait().
    """
    send_group(child.pid, signal.SIGTERM)
    deadline = time.monotonic() + grace
    while time.monotonic() < deadline:
        child.poll()
        if not family_metrics(process_group=child.pid)['worker_pids']:
            break
        time.sleep(min(0.1, max(0, deadline - time.monotonic())))
    remaining = family_metrics(process_group=child.pid)['worker_pids']
    if remaining:
        send_group(child.pid, signal.SIGKILL)
    child.wait(timeout=5)
    return {'sigterm_sent': True, 'sigkill_sent': bool(remaining), 'survivors_before_sigkill': remaining}


def run_locked(args):
    directory, session, policy, baseline = load_session(args.session_dir)
    cwd = Path(args.cwd or session['disk_path']).resolve()
    if not cwd.is_dir():
        raise ValueError('worker cwd does not exist: ' + str(cwd))
    command = args.command
    if command[:1] == ['--']:
        command = command[1:]
    if not command:
        raise ValueError('worker command required after --')
    if active_hold(directory):
        raise RuntimeError('current-session resource hold requires explicit acknowledge --reason; no worker started')
    ledger = directory / 'session_ledger.jsonl'
    accumulated = sum(json.loads(row).get('wall_seconds', 0) for row in ledger.read_text().splitlines()) if ledger.exists() else 0.0
    run_id = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime()) + '_' + str(time.time_ns()) + '_' + args.label
    run_dir = directory / 'runs' / run_id
    run_dir.mkdir(parents=True)
    state = collect(directory, cwd)
    decision = evaluate(state, baseline, None, policy, session_seconds=accumulated)
    append_json(run_dir / 'resources.jsonl', {'phase': 'preflight', 'snapshot': state, 'decision': decision})
    if decision['stop']:
        hold(directory, run_id, decision['reasons'], state)
        write_json(run_dir / 'result.json', {'worker_started': False, 'decision': decision, 'command': command})
        print('Preflight refused: ' + '; '.join(decision['reasons']), file=sys.stderr)
        return 2
    env = dict(os.environ)
    env.update({name: '1' for name in THREAD_VARIABLES})
    env.update({'OMP_DYNAMIC': 'FALSE', 'MKL_DYNAMIC': 'FALSE',
                'IPM_RESOURCE_SESSION': str(directory), 'IPM_RESOURCE_RUN': str(run_dir),
                'IPM_GUARD_TERMINATE_GRACE_SECONDS': str(policy.terminate_grace_seconds)})
    controlled_env = {key: env[key] for key in (*THREAD_VARIABLES, 'OMP_DYNAMIC', 'MKL_DYNAMIC', 'IPM_RESOURCE_SESSION', 'IPM_RESOURCE_RUN', 'IPM_GUARD_TERMINATE_GRACE_SECONDS')}
    result = {'run_id': run_id, 'session_id': session['session_id'], 'command': command, 'cwd': str(cwd),
              'worker_started': False, 'controlled_environment': controlled_env, 'policy': policy.to_dict(),
              'started_time': time.time(), 'stop_reasons': [], 'wall_seconds': 0.0,
              'peak_family_rss_mib': state['family_rss_mib'], 'session_seconds_before': accumulated}
    interrupted = []
    def interrupted_handler(signum, frame):
        interrupted.append(signum)
    old_handlers = {sig: signal.signal(sig, interrupted_handler) for sig in (signal.SIGINT, signal.SIGTERM)}
    began = time.monotonic()
    child = None
    previous = state
    failure = None
    try:
        with (run_dir / 'worker.log').open('w') as log:
            child = subprocess.Popen([sys.executable, str(HERE / 'worker_bootstrap.py'), str(policy.nice_increment),
                                      str(run_dir / 'worker_priority.json'), *command],
                                     cwd=str(cwd), env=env, stdout=log, stderr=subprocess.STDOUT,
                                     start_new_session=True)
            result.update(worker_started=True, worker_pid=child.pid, supervisor_pid=os.getpid())
            write_json(run_dir / 'running.json', result)
            # An immediate sample closes the preflight-to-launch gap. Sampling is
            # observational, not a kernel-enforced hard RSS limit.
            while True:
                elapsed = time.monotonic() - began
                child.poll()
                state = collect(directory, cwd, child.pid)
                result['peak_family_rss_mib'] = max(result['peak_family_rss_mib'], state['family_rss_mib'])
                decision = evaluate(state, baseline, previous, policy, elapsed, accumulated)
                if interrupted:
                    decision['stop'] = True
                    decision['reasons'].append('supervisor received signal ' + str(interrupted[0]))
                append_json(run_dir / 'resources.jsonl', {'phase': 'running', 'elapsed_seconds': elapsed, 'snapshot': state, 'decision': decision})
                previous = state
                if decision['stop']:
                    result['stop_reasons'] = decision['reasons']
                    hold(directory, run_id, decision['reasons'], state)
                    result['termination'] = stop_group(child, policy.terminate_grace_seconds)
                    break
                if child.returncode is not None:
                    if state['worker_pids']:
                        result['stop_reasons'] = ['worker leader exited with surviving process-group members']
                        hold(directory, run_id, result['stop_reasons'], state)
                        result['termination'] = stop_group(child, policy.terminate_grace_seconds)
                    break
                time.sleep(min(policy.sample_seconds, max(0.01, policy.max_seconds - elapsed),
                               max(0.01, policy.max_session_seconds - accumulated - elapsed)))
            result['returncode'] = child.wait(timeout=5)
    except BaseException as exc:
        failure = exc
        result['supervisor_error'] = type(exc).__name__ + ': ' + str(exc)
        result['stop_reasons'].append('supervisor exception; worker terminated')
        if child:
            result['termination'] = stop_group(child, policy.terminate_grace_seconds)
            result['returncode'] = child.returncode
        hold(directory, run_id, result['stop_reasons'], previous)
    finally:
        for sig, handler in old_handlers.items():
            signal.signal(sig, handler)
        result['finished_time'] = time.time()
        result['wall_seconds'] = time.monotonic() - began
        result['success'] = not result['stop_reasons'] and result.get('returncode') == 0
        write_json(run_dir / 'result.json', result)
        append_json(ledger, {'run_id': run_id, 'wall_seconds': result['wall_seconds'],
                    'worker_started': result['worker_started'], 'returncode': result.get('returncode'),
                    'stop_reasons': result['stop_reasons'], 'peak_family_rss_mib': result['peak_family_rss_mib']})
    print(json.dumps({'run_dir': str(run_dir), 'success': result['success'], 'wall_seconds': result['wall_seconds'],
                      'returncode': result.get('returncode'), 'stop_reasons': result['stop_reasons'],
                      'peak_family_rss_mib': result['peak_family_rss_mib']}))
    if failure:
        print(result['supervisor_error'], file=sys.stderr)
    return 0 if result['success'] else 2


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    sub = cli.add_subparsers(dest='action', required=True)
    snap = sub.add_parser('snapshot', help='read-only current telemetry; launches no worker')
    snap.add_argument('--disk-path', default='.')
    init = sub.add_parser('init', help='capture an explicit new-machine resource session and immutable baseline')
    init.add_argument('--session-dir', required=True)
    init.add_argument('--disk-path')
    init.add_argument('--policy', help='JSON with overrides to Policy defaults')
    run = sub.add_parser('run', help='run exactly one bounded low-priority process group')
    run.add_argument('--session-dir', required=True)
    run.add_argument('--cwd')
    run.add_argument('--label', default='worker')
    run.add_argument('--lock-file', default=str(DEFAULT_LOCK))
    run.add_argument('command', nargs=argparse.REMAINDER)
    ack = sub.add_parser('acknowledge', help='review current-session hold without deleting evidence or resetting budgets')
    ack.add_argument('--session-dir', required=True)
    ack.add_argument('--reason', required=True)
    ack.add_argument('--lock-file', default=str(DEFAULT_LOCK))
    sub.add_parser('default-policy', help='print the conservative default policy as JSON')
    return cli


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.action == 'snapshot':
            print(json.dumps(snapshot(Path(args.disk_path).resolve()), indent=2, sort_keys=True))
            return 0
        if args.action == 'default-policy':
            print(json.dumps(Policy().to_dict(), indent=2, sort_keys=True))
            return 0
        if args.action == 'init':
            return initialize(args)
        if args.action == 'acknowledge':
            return acknowledge(args)
        if args.action == 'run':
            if '/' in args.label or '\\' in args.label or args.label in ('.', '..'):
                raise ValueError('label must be a simple filename component')
            with exclusive_lock(args.lock_file):
                return run_locked(args)
    except (OSError, ValueError, RuntimeError, KeyError) as exc:
        print(type(exc).__name__ + ': ' + str(exc), file=sys.stderr)
        return 2
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
