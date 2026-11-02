"""Audit actual forecast-guided games, allowing explicit forecast errors.

A prediction mismatch does not invalidate an original-engine game outcome.
It does invalidate any claim that the predictor reproduced the target exactly.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', nargs='+', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--expected', type=int)
    args = parser.parse_args()
    cases, invalid, input_hashes = [], [], {}
    for filename in args.inputs:
        path = Path(filename)
        input_hashes[filename] = hashlib.sha256(path.read_bytes()).hexdigest()
        for line in path.read_text().splitlines():
            row = json.loads(line)
            issues = [name for name in ('bot_errors', 'rejected_actions') if any(row[name])]
            if row['source_changed_during_match']:
                issues.append('source_changed_during_match')
            for field in ('source_sha256', 'source_sha256_at_end'):
                if not row.get(field):
                    issues.append('missing_' + field)
            if issues:
                invalid.append({'input': filename, 'condition': row['condition'], 'issues': issues})
                continue
            condition = row['condition']
            side = condition['counter_side']
            expected = 'D' if row['result']['winner'] is None else (
                'W' if row['result']['winner'] == side else 'L')
            if row['counter_outcome'] != expected:
                raise ValueError('Recorded outcome differs from the authoritative winner.')
            trace = row['forecast_trace']
            rounds = sorted(t['round'] for t in trace)
            if rounds != list(range(1, row['rounds'] + 1)):
                raise ValueError('Incomplete or duplicate forecast trace.')
            cases.append({'input': filename, 'condition': condition, 'outcome': expected,
                          'hp_counter_first': row['hp'][::1 if side == 0 else -1],
                          'rounds': row['rounds'], 'runtime_seconds': row['runtime_seconds'],
                          'decision_seconds_counter_first': row['decision_seconds'][::1 if side == 0 else -1],
                          'forecast_mismatch_rounds': row['forecast_mismatch_rounds'],
                          'canonical_replay_sha256': canonical_replay(row['replay_path'], side),
                          'replay_path': row['replay_path'],
                          'attack_trace': [t for t in trace if t['round'] == condition['parameters']['attack_round']]})
    groups = defaultdict(list)
    for case in cases:
        identity = {k: v for k, v in case['condition'].items() if k not in ('index', 'counter_side')}
        groups[json.dumps(identity, sort_keys=True)].append(case)
    pairs = []
    for identity, group in sorted(groups.items()):
        sides = sorted(case['condition']['counter_side'] for case in group)
        if len(set(sides)) != len(sides):
            raise ValueError('Duplicate condition and player assignment; do not pool repetitions silently.')
        pairs.append({'condition': json.loads(identity), 'sides': sides,
                      'exactly_two_assignments': sides == [0, 1],
                      'same_complete_trajectory': len(group) == 2 and len({c['canonical_replay_sha256'] for c in group}) == 1,
                      'outcomes': [c['outcome'] for c in group]})
    output = {'time_utc': now(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256': input_hashes, 'valid_cases': len(cases), 'invalid': invalid,
              'expected_cases': args.expected, 'outcomes': dict(Counter(c['outcome'] for c in cases)),
              'games_with_forecast_mismatch': sum(bool(c['forecast_mismatch_rounds']) for c in cases),
              'distinct_canonical_trajectories': len({c['canonical_replay_sha256'] for c in cases}),
              'pairs': pairs, 'cases': cases,
              'scope': 'All included games were played on the original engine. Explicit development conditions, not independent samples or held-out strength estimates.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('valid_cases', 'invalid', 'outcomes', 'games_with_forecast_mismatch', 'distinct_canonical_trajectories')}))
    assert not invalid
    if args.expected is not None:
        assert len(cases) == args.expected
        assert all(p['exactly_two_assignments'] for p in pairs)


if __name__ == '__main__':
    main()
