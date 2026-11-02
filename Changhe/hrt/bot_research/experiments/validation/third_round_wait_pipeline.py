"""Sequential bounded protocol161 scheduler with durable child-attempt output."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import signal
import shutil
import subprocess
import sys
import traceback

from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
NAME = 'third-round-wait-00-001'
D = E / 'third-round-wait-001.json'
DEADLINE = datetime.fromisoformat('2026-10-31T22:50:00+00:00')


def now():
    return datetime.now(timezone.utc).isoformat()


def emit(**values):
    print(json.dumps(dict(time_utc=now(), **values)), flush=True)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify_inputs(declaration, declaration_sha):
    if sys.flags.optimize != 0 or os.environ.get("PYTHONOPTIMIZE", "") not in ("", "0"):
        raise RuntimeError("Pipeline requires interpreter assertions enabled, including inherited child environments.")
    affinity = os.sched_getaffinity(0)
    if len(affinity) != 1 or not affinity <= {28, 29, 30} or os.getpriority(os.PRIO_PROCESS, 0) < 19:
        raise RuntimeError("Pipeline requires one assigned local core and nice19.")
    for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        if os.environ.get(key) != "1":
            raise RuntimeError("Pipeline requires all declared numerical thread limits to equal one.")
    if os.environ.get("PYTHONDONTWRITEBYTECODE") != "1" or Path(os.environ.get("TMPDIR", ".")).resolve() != (Path.cwd()/"bot_research/tmp").resolve():
        raise RuntimeError("Pipeline requires bytecode disabled and the research temporary directory.")
    if digest(D) != declaration_sha:
        raise ValueError('Declaration bytes changed.')
    for field in ('input_sha256', 'retained_input_sha256'):
        for name, expected in declaration[field].items():
            path = Path(name)
            if path.is_absolute() or '..' in path.parts:
                raise ValueError('Expected a project-relative declared input.')
            if digest(path) != expected:
                raise ValueError('Changed declared input: ' + name)
    for campaign in declaration['campaigns']:
        if digest(campaign['manifest']) != campaign['manifest_sha256']:
            raise ValueError('Campaign manifest bytes changed.')
    if shutil.disk_usage('.').free < 20_000_000_000:
        raise RuntimeError('Less than 20 GB free; no new child work.')


def run(declaration, declaration_sha, output_dir, ordinal, module, *args):
    verify_inputs(declaration, declaration_sha)
    if (DEADLINE-datetime.now(timezone.utc)).total_seconds() < 560:
        raise RuntimeError('Not enough time for a bounded child before 22:50 UTC.')
    command = ['.venv/bin/python', '-B', '-m',
               'bot_research.experiments.validation.'+module, *map(str, args)]
    prefix = output_dir / f'child{ordinal:03d}'
    raw_path = Path("bot_research/tmp") / (NAME + "-child" + str(ordinal) + "-" + str(os.getpid()) + ".raw.log")
    started = dict(time_utc=now(), ordinal=ordinal, command=command, status='started',
                   declaration=str(D), declaration_sha256=declaration_sha, private_raw_spool=str(raw_path))
    atomic_json(prefix.with_suffix('.started.json'), started, exclusive=True)
    emit(child=ordinal, command=command)
    child = None
    output = ''
    timed_out = False
    cleanup_complete = True
    try:
        # Files, not a pipe buffer, retain child output even if this scheduler
        # is interrupted before communicate returns. The child has a new group.
        with raw_path.open('x') as log:
            child = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                                     text=True, start_new_session=True)
            atomic_json(prefix.with_suffix('.spawned.json'), dict(time_utc=now(), pid=child.pid,
                        process_group=child.pid, ordinal=ordinal), exclusive=True)
            try:
                child.wait(timeout=530)
            except subprocess.TimeoutExpired:
                timed_out = True
                try:
                    os.killpg(child.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                try:
                    child.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    try:
                        os.killpg(child.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    try:
                        child.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        cleanup_complete = False
                        child.poll()
            log.flush()
            os.fsync(log.fileno())
        # Child tools already redact diagnostics, but make the retained output
        # safe even if a Python exception escaped before their own handler.
        raw = raw_path.read_text(errors='replace')
        output = public_diagnostic(raw)
        with prefix.with_suffix('.output.log').open('x') as published:
            published.write(output)
        record = dict(time_utc=now(), ordinal=ordinal, command=command,
            returncode=child.returncode, timed_out=timed_out, cleanup_complete=cleanup_complete,
            output=str(prefix.with_suffix('.output.log')), output_sha256=digest(prefix.with_suffix('.output.log')))
        atomic_json(prefix.with_suffix('.finished.json'), record, exclusive=True)
        print(output, end='', flush=True)
        emit(child=ordinal, returncode=child.returncode, timed_out=timed_out, cleanup_complete=cleanup_complete)
        verify_inputs(declaration, declaration_sha)
        if not cleanup_complete:
            raise RuntimeError('Process-group cleanup incomplete after TERM/KILL bounds; stop with durable partial output.')
        if timed_out:
            raise RuntimeError('Child timed out; its group was terminated and partial output retained.')
        return record
    except Exception as error:
        if child is not None and child.poll() is None:
            try:
                os.killpg(child.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                child.wait(timeout=5)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(child.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                try:
                    child.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    cleanup_complete = False
                    child.poll()
        if raw_path.exists() and not prefix.with_suffix(".output.log").exists():
            with prefix.with_suffix(".output.log").open("x") as published:
                published.write(public_diagnostic(raw_path.read_text(errors="replace")))
        atomic_json(prefix.with_suffix('.scheduler-error.json'), dict(time_utc=now(), ordinal=ordinal,
            diagnostic=public_diagnostic(str(error)), timed_out=timed_out, cleanup_complete=cleanup_complete,
            returncode=child.returncode if child is not None else None), exclusive=True)
        raise


def main():
    declaration = json.loads(D.read_text())
    declaration_sha = digest(D)
    if declaration['protocol'] != 161 or len(declaration['campaigns']) != 1:
        raise ValueError('Expected the single four-game protocol161 campaign.')
    campaign = declaration['campaigns'][0]
    if campaign['name'] != NAME or campaign['expected'] != 4:
        raise ValueError('Wrong campaign or case count.')
    verify_inputs(declaration, declaration_sha)
    root = R / NAME
    output_dir = R / (NAME+'-pipeline')
    output_dir.mkdir(exist_ok=False)
    (E / 'analysis/third_round_wait/verification').mkdir(exist_ok=True)
    children = []
    try:
        for batch in range(8):
            args = ['--manifest', campaign['manifest'], '--output-dir', root,
                    '--max-seconds', 500, '--match-timeout', 300]
            if root.exists():
                args.append('--resume')
            receipt = run(declaration, declaration_sha, output_dir, len(children), 'run_data_development', *args)
            children.append(receipt)
            summary_path = root / 'summary.json'
            summary = json.loads(summary_path.read_text()) if summary_path.exists() else None
            if receipt['returncode'] or (summary and (summary['complete'] or summary['invalid'] or summary['failures'])):
                break
        else:
            emit(campaign_incomplete=True, reason='Eight bounded scheduling batches exhausted.')
        # A nonzero ordinary audit does not silently discard the other required
        # receipts. Timeouts, cleanup, integrity, disk and deadline failures stop
        # immediately. Failed game files are never retried by this pipeline.
        steps = [
            ('audit_development_strict', ['--inputs', root, '--expected', 4, '--output', R/(NAME+'-strict.json')]),
            ('replay_audit', ['--inputs', root/'matches.jsonl', '--output', R/(NAME+'-replay.json')]),
            ('audit_data_archives', ['--campaigns', root, '--output', R/(NAME+'-data.json')]),
            ('check_fixed_game_histories', ['--campaign', root, '--expected', 4, '--output', R/(NAME+'-fresh.json')]),
            ('third_round_wait_check', ['mechanism']),
            ('third_round_wait_check', ['check']),
        ]
        for module, args in steps:
            children.append(run(declaration, declaration_sha, output_dir, len(children), module, *args))
        verify_inputs(declaration, declaration_sha)
        result = dict(time_utc=now(), scheduling_completed=True,
            all_children_successful=all(c['returncode'] == 0 for c in children),
            children=children, declaration=str(D), declaration_sha256=declaration_sha,
            scope='Sequential one-core child execution; scientific hypothesis verdicts are in the final checker receipt.')
        atomic_json(output_dir/'complete.json', result, exclusive=True)
        emit(scheduling_completed=True, all_children_successful=result['all_children_successful'])
        return 0 if result['all_children_successful'] else 2
    except Exception as error:
        atomic_json(output_dir/'incomplete.json', dict(time_utc=now(), scheduling_completed=False,
            diagnostic=public_diagnostic(str(error)), children=children,
            declaration=str(D), declaration_sha256=declaration_sha), exclusive=True)
        raise


def termination_requested(signum, frame):
    # One graceful parent signal enters ordinary exception cleanup. Ignore
    # repeats during the bounded cleanup; SIGKILL remains unrecoverable.
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    raise RuntimeError("Scheduler termination requested by signal " + str(signum))


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, termination_requested)
    signal.signal(signal.SIGINT, termination_requested)
    try:
        raise SystemExit(main())
    except Exception:
        print(public_diagnostic(traceback.format_exc()), flush=True)
        raise SystemExit(1)
