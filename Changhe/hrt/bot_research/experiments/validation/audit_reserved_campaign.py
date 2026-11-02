"""Independently account for every predeclared reserved validation condition.

This checks source archives, the prescribed jobs, result validity, exact replay
hashes and paired trajectories. Full original-engine replay is a separate step.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from datetime import datetime
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation_strict import make_jobs, now, read_result
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def account(directory, metadata, inputs):
    jobs_path = directory / 'jobs.json'
    inputs[str(jobs_path)] = digest(jobs_path)
    jobs = json.loads(jobs_path.read_text())
    attempts = []
    for job in jobs:
        single = directory / 'jobs' / (job['id'] + '.json')
        if json.loads(single.read_text()) != job:
            raise ValueError('Individual job differs from job list: ' + job['id'])
        inputs[str(single)] = digest(single)
        result = directory / 'results' / (job['id'] + '.json')
        failure = directory / 'results' / (job['id'] + '.failure.json')
        item = {'job': job['id'], 'directory': str(directory), 'condition': job['condition']}
        if failure.exists():
            inputs[str(failure)] = digest(failure)
            item.update(status='failed', failure=json.loads(failure.read_text()),
                        result_also_exists=result.exists())
        elif not result.exists():
            item['status'] = 'unstarted_or_incomplete'
        else:
            inputs[str(result)] = digest(result)
            try:
                row = read_result(result, job, metadata['source_sha256'])
                if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
                    raise ValueError('Bot errors, rejected actions or source drift in result.')
                replay = Path(row['replay_path'])
                if replay.is_absolute() or '..' in replay.parts or replay.parts[:3] != ('bot_research', 'runs', 'validation'):
                    raise ValueError('Replay path outside permitted evidence directory.')
                inputs[str(replay)] = digest(replay)
                if inputs[str(replay)] != row['trajectory_sha256']:
                    raise ValueError('Replay bytes differ from the reported digest.')
                side = job['condition']['candidate_side']
                times = row['decision_seconds'][::1 if side == 0 else -1]
                item.update(status='valid', result_path=str(result), replay_path=str(replay),
                            completed_utc=row['time_utc'], outcome=row['candidate_outcome'],
                            hp_candidate_first=row['hp'][::1 if side == 0 else -1],
                            rounds=row['rounds'], runtime_seconds=row['runtime_seconds'],
                            decision_seconds_candidate_first=times,
                            canonical_replay_sha256=canonical_replay(replay, side))
            except (ValueError, KeyError, TypeError, OSError) as error:
                item.update(status='invalid', diagnostic=public_diagnostic(str(error)))
        attempts.append(item)
    return jobs, attempts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', required=True)
    parser.add_argument('--candidate-sha256', required=True)
    parser.add_argument('--retries', nargs='*', default=[])
    parser.add_argument('--output', required=True)
    parser.add_argument('--allow-incomplete', action='store_true')
    args = parser.parse_args()
    directory = Path(args.directory)
    freeze_path = directory / 'freeze.json'
    metadata = json.loads(freeze_path.read_text())
    inputs = {str(freeze_path): digest(freeze_path)}
    candidate = metadata['candidate'].partition(':')[0].replace('.', '/') + '.py'
    if metadata['source_sha256'].get(candidate) != args.candidate_sha256:
        raise ValueError('Candidate digest differs from requested freeze.')
    archive_problems = []
    current_drift = []
    for name, expected in metadata['source_sha256'].items():
        archived = directory / 'sources' / name
        if not archived.is_file() or digest(archived) != expected:
            archive_problems.append(name)
        if not Path(name).is_file() or digest(name) != expected:
            current_drift.append(name)
    if archive_problems:
        raise ValueError('Frozen source archive is incomplete or changed: ' + repr(archive_problems))
    manifest_name = 'bot_research/experiments/validation/holdout_manifest.json'
    manifest_path = directory / 'sources' / manifest_name
    if digest(manifest_path) != metadata['manifest_sha256']:
        raise ValueError('Archived reserved manifest differs from freeze.')
    manifest = json.loads(manifest_path.read_text())
    jobs, attempts = account(directory, metadata, inputs)
    prescribed = make_jobs(metadata['candidate'], metadata['pool'], manifest, directory, metadata['stress'])
    if jobs != prescribed:
        raise ValueError('Recorded jobs differ from predeclared conditions.')
    declarations = {j['id']: j for j in jobs}
    for retry_name in args.retries:
        retry = Path(retry_name)
        retry_meta = json.loads((retry / 'freeze.json').read_text())
        inputs[str(retry / 'freeze.json')] = digest(retry / 'freeze.json')
        if retry_meta['source_sha256'] != metadata['source_sha256']:
            raise ValueError('Retry source freeze differs from original campaign.')
        retry_jobs, retry_attempts = account(retry, metadata, inputs)
        for job in retry_jobs:
            original = declarations.get(job['id'])
            if original is None or any(job[k] != original[k] for k in ('id', 'names', 'bots', 'condition')):
                raise ValueError('Retry introduced or changed a reserved condition.')
            if job.get('prefixes') != original.get('prefixes'):
                raise ValueError('Retry changed the prescribed legal opening.')
        attempts.extend(retry_attempts)
    grouped = defaultdict(list)
    for attempt in attempts:
        grouped[attempt['job']].append(attempt)
    cases, unresolved, repeat_disagreements = [], [], []
    for job in jobs:
        valid = sorted((a for a in grouped[job['id']] if a['status'] == 'valid'), key=lambda a: a['completed_utc'])
        if not valid:
            unresolved.append(job['id'])
            continue
        cases.append(valid[0])
        if len({a['canonical_replay_sha256'] for a in valid}) > 1:
            repeat_disagreements.append(job['id'])
    scores = defaultdict(Counter)
    pairs = defaultdict(list)
    for case in cases:
        condition = case['condition']
        scores[condition['scenario']][case['outcome']] += 1
        identity = (condition['scenario'], json.dumps(condition['opponent'], sort_keys=True))
        pairs[identity].append(case)
    pair_rows = []
    for (scenario, opponent), group in sorted(pairs.items()):
        group.sort(key=lambda c: c['condition']['candidate_side'])
        sides = [c['condition']['candidate_side'] for c in group]
        pair_rows.append({'scenario': scenario, 'opponent': json.loads(opponent), 'sides': sides,
                          'exactly_two_assignments': sides == [0, 1],
                          'same_complete_trajectory': len(group) == 2 and len({c['canonical_replay_sha256'] for c in group}) == 1,
                          'outcomes': [c['outcome'] for c in group],
                          'hp_candidate_first': [c['hp_candidate_first'] for c in group]})
    latest = max((c['completed_utc'] for c in cases), default=None)
    elapsed = None if latest is None else (datetime.fromisoformat(latest) - datetime.fromisoformat(metadata['started_utc'])).total_seconds()
    output = {'time_utc': now(), 'checker_sha256': digest(__file__), 'input_sha256': inputs,
              'candidate': metadata['candidate'], 'candidate_sha256': args.candidate_sha256,
              'pool': metadata['pool'], 'manifest_sha256': metadata['manifest_sha256'],
              'started_utc': metadata['started_utc'], 'latest_completed_utc': latest,
              'elapsed_to_latest_completion_seconds': elapsed,
              'source_archive_verified': True, 'current_source_drift': current_drift,
              'jobs_match_predeclared_manifest': True, 'expected_conditions': len(jobs),
              'valid_conditions': len(cases), 'attempt_counts': dict(Counter(a['status'] for a in attempts)),
              'unresolved': unresolved, 'repeat_disagreements': repeat_disagreements,
              'scores_by_scenario': {name: dict(counts) for name, counts in scores.items()},
              'runtime_seconds_sum_of_primary_matches': sum(c['runtime_seconds'] for c in cases),
              'pairs': pair_rows, 'cases': cases, 'attempts': attempts,
              'distinct_canonical_trajectories': len({c['canonical_replay_sha256'] for c in cases}),
              'primary_selection': 'Earliest valid completion per prescribed condition. Every failure and retry retained.',
              'scope': manifest['interpretation_limit'],
              'replay_note': 'Checks replay bytes and paired trajectories only. Complete original-engine replay is recorded separately.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({key: output[key] for key in ('valid_conditions', 'expected_conditions', 'attempt_counts', 'unresolved', 'scores_by_scenario', 'current_source_drift')}))
    if repeat_disagreements or (unresolved and not args.allow_incomplete):
        raise SystemExit(2)


if __name__ == '__main__':
    main()
