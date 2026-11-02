"""Stream terminal validation output through the existing path redactor.

This wrapper changes only diagnostics. The fixed pipeline retains responsibility
for declaration hashes, the start-time gate, bounded children and final checks.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import traceback

from bot_research.experiments.validation.artifact_io import public_diagnostic


def emit(text):
    sys.stdout.write(public_diagnostic(text))
    sys.stdout.flush()


def main():
    declaration = Path('bot_research/experiments/validation/terminal-candidate-declaration-001.json')
    if not declaration.is_file():
        raise RuntimeError('The final candidate declaration is required before launch.')
    wrapper = Path('bot_research/experiments/validation/terminal_logged.py')
    command = ['.venv/bin/python', '-B', '-m',
               'bot_research.experiments.validation.run_terminal_pipeline']
    emit(json.dumps(dict(
        time_utc=datetime.now(timezone.utc).isoformat(),
        log_wrapper=str(wrapper),
        wrapper_sha256=hashlib.sha256(wrapper.read_bytes()).hexdigest(),
        declaration_sha256=hashlib.sha256(declaration.read_bytes()).hexdigest(),
        command=command,
    )) + '\n')
    child = subprocess.Popen(command, stdin=subprocess.DEVNULL,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert child.stdout is not None
    for line in iter(child.stdout.readline, b''):
        emit(line.decode('utf-8', errors='replace'))
    code = child.wait()
    emit(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),
                         pipeline_returncode=code)) + '\n')
    return code if code >= 0 else 128 - code


if __name__ == '__main__':
    try:
        status = main()
    except Exception:
        emit(traceback.format_exc())
        status = 1
    raise SystemExit(status)
