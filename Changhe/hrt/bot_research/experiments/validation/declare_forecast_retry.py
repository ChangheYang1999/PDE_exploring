"""Preserve completed-attempt accounting while declaring a longer retry matrix.

The underlying runner forms a Cartesian matrix. Selecting a failed candidate
therefore also repeats its successful opponent/seat combinations as controls.
Those controls are labeled here and must not increase the condition count.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', required=True)
    parser.add_argument('--source-manifest', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--timeout', type=int, default=300)
    args = parser.parse_args()
    directory = Path(args.input_dir)
    freeze = json.loads((directory / 'freeze.json').read_text())
    if digest(args.source_manifest) != freeze['manifest_sha256']:
        raise ValueError('Original declaration differs from the frozen manifest.')
    changed = [name for name, expected in freeze['source_sha256'].items()
               if not Path(name).is_file() or digest(name) != expected]
    if changed:
        raise ValueError('Original source changed: ' + repr(changed))
    jobs = json.loads((directory / 'jobs.json').read_text())
    failures, successful = [], []
    evidence = {str(directory / 'freeze.json'): digest(directory / 'freeze.json'),
                str(directory / 'jobs.json'): digest(directory / 'jobs.json'),
                args.source_manifest: digest(args.source_manifest)}
    for job in jobs:
        result = directory / 'results' / (job['id'] + '.json')
        failure = result.with_suffix('.failure.json')
        if failure.exists():
            row = json.loads(failure.read_text())
            if 'timeout_seconds' not in row:
                raise ValueError('Fix and review non-timeout failures separately.')
            evidence[str(failure)] = digest(failure)
            failures.append(job['condition'])
        elif result.exists():
            successful.append(job['condition'])
        else:
            raise ValueError('Finish all original declared attempts before declaring retries.')
    if not failures:
        raise ValueError('No timeout condition requires retry.')
    failed_candidates = {c['candidate_id'] for c in failures}
    source = json.loads(Path(args.source_manifest).read_text())
    selected = [c for c in source['candidates'] if c['id'] in failed_candidates]
    if {c['id'] for c in selected} != failed_candidates:
        raise ValueError('Failed candidate identity is missing from the original manifest.')
    controls = [c for c in successful if c['candidate_id'] in failed_candidates]
    output = {'declared_utc': now(),
              'purpose': f'Explicit retry of recorded timeouts, permitting {args.timeout} seconds per match. Original failures remain in accounting; completed combinations repeated by the Cartesian runner are controls.',
              'candidates': selected, 'opponents': source['opponents'],
              'retry_of_directory': args.input_dir, 'requested_timeout_seconds': args.timeout,
              'prior_failed_conditions': failures, 'repeat_control_conditions': controls,
              'original_evidence_sha256': evidence,
              'original_source_sha256': freeze['source_sha256'],
              'scope': 'No new statistical condition. Combine using retry-aware strict accounting and retain all attempts.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'declared_utc': output['declared_utc'], 'retry_candidates': len(selected),
                      'prior_timeouts': len(failures), 'repeat_controls': len(controls)}))


if __name__ == '__main__':
    main()
