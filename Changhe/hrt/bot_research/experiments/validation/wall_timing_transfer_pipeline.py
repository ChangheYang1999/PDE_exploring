"""Bounded scheduling of protocol160; never selects or changes a policy."""
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
from bot_research.experiments.validation.artifact_io import public_diagnostic

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
DEADLINE = datetime.fromisoformat('2026-10-31T22:50:00+00:00')


def emit(**values):
    print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(), **values)), flush=True)


def verify_active_inputs(declaration):
    for name, expected in declaration['input_sha256'].items():
        path = Path(name)
        if path.is_absolute() or '..' in path.parts:
            raise ValueError('Expected a relative declared input.')
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError('Changed declared source: ' + name)
    if shutil.disk_usage('.').free < 20_000_000_000:
        raise RuntimeError('Less than 20 GB free; no new child work.')


def run(declaration, module, *args):
    verify_active_inputs(declaration)
    if (DEADLINE - datetime.now(timezone.utc)).total_seconds() < 560:
        raise RuntimeError('Not enough time for a bounded child before 22:50 UTC.')
    command = ['.venv/bin/python', '-B', '-m',
               'bot_research.experiments.validation.' + module, *map(str, args)]
    emit(command=command)
    child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             text=True, start_new_session=True)
    timed_out = False
    cleanup_complete = True
    try:
        output, _ = child.communicate(timeout=530)
    except subprocess.TimeoutExpired:
        timed_out = True
        try:
            os.killpg(child.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            output, _ = child.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(child.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            try:
                output, _ = child.communicate(timeout=5)
            except subprocess.TimeoutExpired as final_timeout:
                cleanup_complete = False
                output = final_timeout.output or ''
                if isinstance(output, bytes):
                    output = output.decode('utf-8', errors='replace')
                child.stdout.close()
                child.poll()
    print(public_diagnostic(output or ''), end='', flush=True)
    emit(returncode=child.returncode, timed_out=timed_out, cleanup_complete=cleanup_complete)
    verify_active_inputs(declaration)
    if not cleanup_complete:
        raise RuntimeError('Process-group cleanup did not complete within its bound; partial output retained, stop this lane job.')
    if timed_out:
        raise RuntimeError('Bounded child timed out; its process group was terminated and output retained.')
    if child.returncode:
        raise RuntimeError('Child failed; preserve diagnostics and attempt artifacts.')


def main():
    index = int(sys.argv[1])
    declaration = json.loads((E / 'wall-timing-transfer-001.json').read_text())
    campaign = declaration['campaigns'][index]
    name, expected = campaign['name'], campaign['expected']
    root = R / name
    if hashlib.sha256(Path(campaign['manifest']).read_bytes()).hexdigest() != campaign['manifest_sha256']:
        raise RuntimeError('Campaign manifest changed.')
    for batch in range(12):
        args = ['--manifest', campaign['manifest'], '--output-dir', root,
                '--max-seconds', 500, '--match-timeout', 300]
        if root.exists():
            args.append('--resume')
        run(declaration, 'run_data_development', *args)
        summary = json.loads((root / 'summary.json').read_text())
        if summary['complete']:
            break
    else:
        raise RuntimeError('Incomplete bounded campaign; preserve all cases.')
    if summary['valid_completed'] != expected or summary['invalid'] or summary['failures']:
        raise RuntimeError('Campaign contains incomplete, invalid or failed attempts.')
    run(declaration, 'audit_development_strict', '--inputs', root, '--expected', expected,
        '--output', R / (name + '-strict.json'))
    run(declaration, 'replay_audit', '--inputs', root / 'matches.jsonl',
        '--output', R / (name + '-replay.json'))
    run(declaration, 'audit_data_archives', '--campaigns', root,
        '--output', R / (name + '-data.json'))
    run(declaration, 'check_fixed_game_histories', '--campaign', root, '--expected', expected,
        '--output', R / (name + '-fresh.json'))
    emit(campaign_complete=name)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(public_diagnostic(traceback.format_exc()), flush=True)
        raise SystemExit(1)
