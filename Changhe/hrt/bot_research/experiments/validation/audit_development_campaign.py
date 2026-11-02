"""Combine frozen development shards with explicitly labeled timeout retries.

The earliest valid completion of each declared condition is the primary result.
Every attempted result remains visible; retries cannot silently add sample size.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation import now, read_result
from bot_research.experiments.validation.summarize_identifying import canonical_replay


KEY_FIELDS = ('candidate_id', 'candidate_spec', 'opponent_id', 'opponent_spec',
              'candidate_side', 'initial_state', 'engine_seed')


def key(condition):
    return json.dumps({name: condition[name] for name in KEY_FIELDS}, sort_keys=True)


def inspect(directory, hashes):
    directory = Path(directory)
    metadata = json.loads((directory / 'freeze.json').read_text())
    jobs = json.loads((directory / 'jobs.json').read_text())
    for name in ('freeze.json', 'jobs.json'):
        path = directory / name
        hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
    attempts = []
    for job in jobs:
        row = {'directory': str(directory), 'job': job['id'], 'condition': job['condition']}
        result = directory / 'results' / (job['id'] + '.json')
        failure = directory / 'results' / (job['id'] + '.failure.json')
        if failure.exists():
            hashes[str(failure)] = hashlib.sha256(failure.read_bytes()).hexdigest()
            row.update(status='failed', failure=json.loads(failure.read_text()),
                       result_also_exists=result.exists())
        elif not result.exists():
            row['status'] = 'unstarted_or_incomplete'
        else:
            hashes[str(result)] = hashlib.sha256(result.read_bytes()).hexdigest()
            try:
                data = read_result(result, job, metadata['source_sha256'])
                problems = [name for name in ('bot_errors', 'rejected_actions') if any(data[name])]
                if data['source_changed_during_match']:
                    problems.append('source_changed_during_match')
                if problems:
                    raise ValueError('Invalid match: ' + repr(problems))
                side = job['condition']['candidate_side']
                row.update(status='valid', outcome=data['candidate_outcome'],
                           hp_candidate_first=data['hp'][::1 if side == 0 else -1],
                           rounds=data['rounds'], runtime_seconds=data['runtime_seconds'],
                           decision_seconds_candidate_first=data['decision_seconds'][::1 if side == 0 else -1],
                           canonical_replay_sha256=canonical_replay(data['replay_path'], side),
                           completed_utc=data['time_utc'], replay_path=data['replay_path'],
                           result_path=str(result))
            except (KeyError, TypeError, ValueError, OSError) as error:
                row.update(status='invalid', error=public_diagnostic(str(error)))
        attempts.append(row)
    return attempts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', nargs='+', required=True)
    parser.add_argument('--retries', nargs='*', default=[])
    parser.add_argument('--output', required=True)
    parser.add_argument('--expected', type=int, required=True)
    args = parser.parse_args()
    hashes = {}
    attempts = []
    for source in args.inputs:
        attempts.extend(inspect(source, hashes))
    declared = {key(row['condition']): row['condition'] for row in attempts}
    if len(declared) != len(attempts) or len(declared) != args.expected:
        raise ValueError('Base shards must declare every condition exactly once.')
    for source in args.retries:
        extra = inspect(source, hashes)
        if any(key(row['condition']) not in declared for row in extra):
            raise ValueError('Retry contains a condition absent from the original declaration.')
        attempts.extend(extra)
    grouped = defaultdict(list)
    for row in attempts:
        grouped[key(row['condition'])].append(row)
    cases, unresolved, disagreements = [], [], []
    for identity, condition in declared.items():
        valid = sorted((r for r in grouped[identity] if r['status'] == 'valid'),
                       key=lambda r: r['completed_utc'])
        if not valid:
            unresolved.append(condition)
            continue
        cases.append(valid[0])
        if len({(r['outcome'], tuple(r['hp_candidate_first']), r['rounds']) for r in valid}) > 1:
            disagreements.append({'condition': condition, 'valid_attempts': valid})
    counts, pairs = defaultdict(Counter), defaultdict(list)
    for case in cases:
        condition = case['condition']
        counts[condition['candidate_id']][case['outcome']] += 1
        pairs[(condition['candidate_id'], condition['opponent_id'])].append(case)
    pair_rows = []
    for (candidate, opponent), group in sorted(pairs.items()):
        group.sort(key=lambda r: r['condition']['candidate_side'])
        sides = [r['condition']['candidate_side'] for r in group]
        pair_rows.append({'candidate': candidate, 'opponent': opponent, 'sides': sides,
            'exactly_two_assignments': sides == [0, 1],
            'same_complete_trajectory': len(group) == 2 and len({r['canonical_replay_sha256'] for r in group}) == 1,
            'outcomes': [r['outcome'] for r in group],
            'hp_candidate_first': [r['hp_candidate_first'] for r in group]})
    output = {'time_utc': now(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256': hashes, 'expected_conditions': args.expected,
              'valid_conditions': len(cases), 'attempt_counts': dict(Counter(r['status'] for r in attempts)),
              'unresolved': unresolved, 'repeat_disagreements': disagreements,
              'outcomes': {name: dict(count) for name, count in counts.items()},
              'pairs': pair_rows, 'cases': cases, 'attempts': attempts,
              'distinct_canonical_trajectories': len({r['canonical_replay_sha256'] for r in cases}),
              'primary_selection': 'Earliest valid completion per declared condition; all retries retained.',
              'scope': 'Development, not reserved validation. Timeouts are computational failures, not game losses. Paired deterministic assignments are not independent samples.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('valid_conditions', 'expected_conditions', 'attempt_counts', 'outcomes', 'unresolved')}))
    if unresolved:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
