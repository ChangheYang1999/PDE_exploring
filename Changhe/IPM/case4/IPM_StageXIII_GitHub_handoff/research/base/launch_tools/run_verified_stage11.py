#!/usr/bin/env python3
"""Launch an explicit future worker only after auditing the full Mac Pro suite."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

from summarize_deployment import summarize


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run-dir', type=Path, required=True)
    p.add_argument('--reference-dir', type=Path, required=True)
    p.add_argument('--session-dir', type=Path, required=True)
    p.add_argument('--work-dir', type=Path, required=True)
    p.add_argument('--label', default='reviewed_experiment')
    p.add_argument('command', nargs=argparse.REMAINDER)
    a = p.parse_args()
    command = a.command[1:] if a.command[:1] == ['--'] else a.command
    if not command:
        p.error('an explicitly selected future worker command is required after --')
    run, reference = a.run_dir.expanduser().resolve(), a.reference_dir.expanduser().resolve()
    python = run/'native_venv/bin/python'
    active = run/'migration_preparation'
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', LC_ALL='C', LANG='C')
    env.update({key: '1' for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
               'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS', 'GOTO_NUM_THREADS')})
    for mode in ('verify-package', 'verify-history'):
        subprocess.run([str(python), '-B', str(reference/'migration_preparation/integrity.py'), mode], env=env, check=True)
    report = summarize(argparse.Namespace(run_dir=run, reference_dir=reference))
    if not report['full_suite_gate_passed']:
        print(json.dumps(report['verification_failures'], indent=2), file=sys.stderr)
        p.error('the complete candidate and 22-direction Mac Pro suite must pass before a future worker can launch')
    work = a.work_dir.expanduser().resolve()
    session_dir = a.session_dir.expanduser().resolve()
    original = Path('/Users/caltech/Changhe/IPM/IPM_R2')
    forbidden = [reference, active, original/'migration_preparation'] + list(original.glob('pilot_y_branch*'))
    for path, label in ((work, 'work directory'), (session_dir, 'resource session')):
        if any(path == frozen.resolve() or frozen.resolve() in path.parents or path in frozen.resolve().parents
               for frozen in forbidden):
            p.error(label + ' must be separate from immutable reference, active source and historical research trees')
    verification_session = run/'resource_session'
    if session_dir == verification_session or verification_session in session_dir.parents:
        p.error('future work needs a separate resource session; retain verification logs unchanged')
    if not (work/'workspace.json').is_file():
        p.error('initialize an independent numerical workspace with prepare_workspace.py first')
    gate_path = work/'provenance'/('future_full_suite_gate_' + str(time.time_ns()) + '.json')
    gate_path.write_text(json.dumps({'passed': True, 'run_dir': str(run), 'reference_dir': str(reference),
        'gate_counts': report['counts'], 'stationarity': report['stationarity'], 'command': command,
        'generated_epoch': time.time()}, indent=2)+'\n')
    argv = [str(python), '-B', str(Path(__file__).resolve().parents[1]/'run_future_experiment.py'), '--verification',
            str(active/'reproduction/results/candidates_macpro.json'), '--session-dir', str(session_dir),
            '--work-dir', str(work), '--label', a.label, '--'] + command
    os.execve(str(python), argv, env)


if __name__ == '__main__':
    main()
