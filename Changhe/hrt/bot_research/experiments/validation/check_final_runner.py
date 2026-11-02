"""Fault-injection checks of final scoring and artifacts; no held-out matches."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation import archive_sources, digest, now, summarize


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    directory = Path(args.output_dir)
    directory.mkdir(exist_ok=False)
    (directory / 'results').mkdir()
    checks = {}
    path = directory / 'atomic.json'
    atomic_json(path, {'first': 1}, exclusive=True)
    try:
        atomic_json(path, {'second': 2}, exclusive=True)
    except FileExistsError:
        checks['exclusive_preserves_old_evidence'] = json.loads(path.read_text()) == {'first': 1}
    else:
        checks['exclusive_preserves_old_evidence'] = False
    checks['no_temporary_artifacts_after_write'] = not list(directory.glob('.partial-*'))
    source = 'bot_research/experiments/validation/artifact_io.py'
    archive_sources({source: digest(source)}, directory)
    checks['archive_identical'] = digest(directory / 'sources' / source) == digest(source)
    # Each error state must be counted exactly once and excluded from W/D/L.
    jobs = []
    for name in ('clean', 'conflict', 'truncated', 'rejected', 'pending', 'stress'):
        condition = {'candidate_side': 0, 'strength_score_eligible': name != 'stress'}
        job = {'id': name, 'condition': condition}
        jobs.append(job)
        if name == 'pending':
            continue
        if name == 'truncated':
            (directory / 'results' / f'{name}.json').write_text('{')
            continue
        row = {'condition': condition, 'candidate_outcome': 'W', 'result': {'winner': 0},
               'bot_errors': [[], []], 'rejected_actions': [1 if name == 'rejected' else 0, 0],
               'source_changed_during_match': {}}
        atomic_json(directory / 'results' / f'{name}.json', row, exclusive=True)
        if name == 'conflict':
            atomic_json(directory / 'results' / f'{name}.failure.json', {'job': name, 'test_failure': True}, exclusive=True)
    metadata = {'candidate': 'fixture', 'pool': 'fixture', 'interpretation': 'Synthetic scoring faults, not game evidence.'}
    summary = summarize(directory, jobs, metadata)
    checks['pending_keeps_incomplete'] = summary['complete'] is False
    checks['one_status_per_condition'] = summary['resolved_conditions'] == 5
    checks['two_failure_conditions'] = len(summary['failed_conditions']) == 2
    checks['standard_excludes_failures_and_rejections'] = summary['standard_initial_state'] == {'W': 1}
    checks['stress_separate'] = summary['continuation_stress'] == {'W': 1}
    checks['rejection_flagged'] = summary['conditions_with_errors_or_rejections_or_drift'] == ['rejected']
    checks['all_successful_false'] = summary['all_completed_successfully'] is False
    absolute = '/' + 'home/example/file.py'
    checks['diagnostic_redacts_local_paths'] = absolute not in public_diagnostic(f'File "{absolute}", line 3')
    output = {'completed_utc': now(), 'checks': checks, 'all_passed': all(checks.values()),
              'source_sha256': {p: digest(p) for p in (source,
                  'bot_research/experiments/validation/final_validation.py',
                  'bot_research/experiments/validation/check_final_runner.py')},
              'interpretation': 'Fault-injection tests only. No reserved holdout was used.'}
    atomic_json(directory / 'checks.json', output, exclusive=True)
    print(json.dumps(output, sort_keys=True))
    if not output['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
