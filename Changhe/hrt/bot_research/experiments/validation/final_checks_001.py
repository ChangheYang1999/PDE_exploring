"""Final bounded integrity and artifact checks after the research audits.

The unchanged original source reuses the completed post-D test run. This tool
never constructs a bot, starts a game, runs a test, or starts a server.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import subprocess

R = Path('bot_research/runs/validation')
V = Path('bot_research/experiments/validation/analysis/terminal_reserved_validation/verification')
OUTPUT = R / 'final-checks-001.json'
POST = V / 'dependency_supplement_final_001.json'
INTEGRITY = R / 'integrity-final-001.json'
ARTIFACTS = R / 'artifacts-final-001.json'
BASELINE = R / 'integrity-start.json'
GUARD = Path('bot_research/experiments/validation/analysis/artifact_path_audit/verification/redaction.json')
PRIOR = R / 'post-d-checks-001.json'


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    for path in (OUTPUT, POST, INTEGRITY, ARTIFACTS):
        assert not path.exists(), 'Output already exists: ' + str(path)
    assert sha(PRIOR) == '14035e05f2daa67ca4ac520f6a2e5c21d8b6caceb0cf0c703c753edb2691e693'
    prior = json.loads(PRIOR.read_text())
    assert prior['all_passed'] and prior['original_tests'] == {'run': 59, 'skipped': 9, 'failed': 0}
    test = next(step for step in prior['steps'] if step['name'] == 'unittest')
    assert test['returncode'] == 0 and sha(test['log']) == test['log_sha256']
    result = dict(schema='final-integrity-checks-001', started_utc=now(),
                  all_passed=False, actual_model='GPT-6 Astra',
                  cpu_affinity=sorted(os.sched_getaffinity(0)), nice=os.getpriority(os.PRIO_PROCESS, 0),
                  steps=[], reused_original_tests=dict(prior_receipt=str(PRIOR),
                  prior_receipt_sha256=sha(PRIOR), test_step=test, counts=prior['original_tests']))

    def run(name, args):
        command = ['.venv/bin/python', '-B', *args]
        log = R / ('final-' + name + '-001.log')
        assert not log.exists(), 'Log already exists: ' + str(log)
        started = now()
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 timeout=180, check=False)
        with log.open('xb') as stream:
            stream.write(process.stdout)
        result['steps'].append(dict(name=name, command=command, started_utc=started,
                                   completed_utc=now(), returncode=process.returncode,
                                   log=str(log), log_sha256=sha(log)))
        assert process.returncode == 0, 'Final check failed: ' + name

    try:
        run('pins', ['-m', 'bot_research.experiments.validation.terminal_dependency_supplement',
                     'verify', '--phase', 'post-d', '--output', str(POST)])
        run('integrity', ['-m', 'bot_research.experiments.validation.integrity',
                         '--output', str(INTEGRITY), '--baseline', str(BASELINE)])
        integrity = json.loads(INTEGRITY.read_text())
        assert all(not value for value in integrity['baseline_comparison'].values())
        assert len(integrity['inventory']) == 903
        assert len(integrity['manifest_missing']) == 1002
        assert set(integrity['manifest_changed']) == {'td_game/combat.py', 'tests/test_engine.py', 'tests/test_rules.py'}
        run('artifacts', ['-m', 'bot_research.experiments.validation.check_owned_artifacts_v2',
                         '--output', str(ARTIFACTS), '--guard-receipt', str(GUARD)])
        artifacts = json.loads(ARTIFACTS.read_text())
        result.update(all_passed=True, unchanged_protected_entries=903,
                      preexisting_missing_manifest_entries=1002,
                      preexisting_changed_manifest_files=sorted(integrity['manifest_changed']),
                      owned_bytes_including_lane=artifacts['lane_bytes'] + sum(v['bytes'] for v in artifacts['owned_project_files'].values()),
                      filesystem_free_bytes=artifacts['filesystem_free_bytes'],
                      scanned_text_files=artifacts['scanned_text_files'],
                      concrete_absolute_path_matches=len(artifacts['absolute_path_matches']),
                      frozen_generic_path_guard_matches=len(artifacts['generic_prefix_guard_matches']))
    except Exception as error:
        result['failure'] = dict(type=type(error).__name__, message=str(error))
        raise
    finally:
        paths = [Path(__file__).relative_to(Path.cwd()), PRIOR, Path(test['log']), BASELINE, GUARD]
        paths += [p for p in (POST, INTEGRITY, ARTIFACTS) if p.exists()]
        paths += [Path(step['log']) for step in result['steps']]
        result.update(completed_utc=now(), input_sha256={str(path): sha(path) for path in paths},
                      scope='Final source-pin, protected-tree and owned-artifact checks. Original tests reused from the authenticated post-D run because protected code is unchanged. No new games, policy calls, tests or servers.')
        with OUTPUT.open('x') as stream:
            json.dump(result, stream, indent=2, sort_keys=True)
            stream.write('\n')
        print(json.dumps({key: result[key] for key in ('started_utc', 'completed_utc', 'all_passed')}, sort_keys=True))


if __name__ == '__main__':
    main()
