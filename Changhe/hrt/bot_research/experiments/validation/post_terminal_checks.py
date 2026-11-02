"""Run bounded post-D integrity checks and retain their exact identities."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess

R = Path('bot_research/runs/validation')
V = Path('bot_research/experiments/validation/analysis/terminal_reserved_validation/verification')
FINAL = V / 'final_candidate.json'
PIPELINE = R / 'reserved-D-final-001-pipeline.log'
POST = V / 'dependency_supplement_post_d_001.json'
INTEGRITY = R / 'integrity-post-d-001.json'
ARTIFACTS = R / 'artifacts-post-d-001.json'
OUTPUT = R / 'post-d-checks-001.json'
BASELINE = R / 'integrity-start.json'
GUARD = Path('bot_research/experiments/validation/analysis/artifact_path_audit/verification/redaction.json')


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    assert not OUTPUT.exists(), 'Postcheck output already exists.'
    for path in (POST, INTEGRITY, ARTIFACTS):
        assert not path.exists(), 'Required output already exists: ' + str(path)
    assert json.loads(FINAL.read_text())['all_passed']
    events = [json.loads(line) for line in PIPELINE.read_text().splitlines() if line.startswith('{')]
    assert any(event.get('all_completed') is True for event in events)
    started = now()
    rows = []

    def run(name, args):
        command = ['.venv/bin/python', '-B', *args]
        log = R / ('post-d-' + name + '-001.log')
        assert not log.exists()
        begin = now()
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 timeout=120, check=False)
        with log.open('xb') as stream:
            stream.write(process.stdout)
        row = dict(name=name, command=command, started_utc=begin, completed_utc=now(),
                   returncode=process.returncode, log=str(log), log_sha256=sha(log))
        rows.append(row)
        assert process.returncode == 0, 'Postcheck failed: ' + name
        return process.stdout.decode()

    run('pins', ['-m', 'bot_research.experiments.validation.terminal_dependency_supplement',
                 'verify', '--phase', 'post-d', '--output', str(POST)])
    tests = run('unittest', ['-m', 'unittest', 'discover', '-s', 'tests', '-v'])
    assert re.search(r'Ran 59 tests in [0-9.]+s', tests)
    assert 'OK (skipped=9)' in tests
    run('integrity', ['-m', 'bot_research.experiments.validation.integrity',
                      '--output', str(INTEGRITY), '--baseline', str(BASELINE)])
    integrity = json.loads(INTEGRITY.read_text())
    assert all(not value for value in integrity['baseline_comparison'].values())
    assert len(integrity['inventory']) == 903
    assert len(integrity['manifest_missing']) == 1002
    assert set(integrity['manifest_changed']) == {'td_game/combat.py', 'tests/test_engine.py', 'tests/test_rules.py'}
    run('artifacts', ['-m', 'bot_research.experiments.validation.check_owned_artifacts_v2',
                      '--output', str(ARTIFACTS), '--guard-receipt', str(GUARD)])
    files = [Path(__file__).relative_to(Path.cwd()), FINAL, PIPELINE, POST, INTEGRITY,
             ARTIFACTS, BASELINE, GUARD, *(Path(row['log']) for row in rows)]
    result = dict(started_utc=started, completed_utc=now(), all_passed=True,
                  scope='Post-D source pins, original tests, protected-tree baseline equality and owned artifact paths/resources. These checks do not add strength trials.',
                  cpu_affinity=sorted(os.sched_getaffinity(0)), nice=os.getpriority(os.PRIO_PROCESS, 0),
                  steps=rows, original_tests=dict(run=59, skipped=9, failed=0),
                  unchanged_protected_entries=903, preexisting_missing_manifest_entries=1002,
                  preexisting_changed_manifest_files=sorted(integrity['manifest_changed']),
                  input_sha256={str(path): sha(path) for path in files})
    with OUTPUT.open('x') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({key: result[key] for key in ('started_utc', 'completed_utc', 'all_passed', 'original_tests', 'unchanged_protected_entries')}))


if __name__ == '__main__':
    main()
