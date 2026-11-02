"""Recheck source-attested forecast games and all recorded target submissions."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.final_validation_strict import read_result
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', nargs='+', required=True)
    parser.add_argument('--expected', type=int, required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    hashes, cases, failures, pending = {}, [], [], []
    for filename in args.inputs:
        directory = Path(filename)
        def load(name):
            path = directory / name
            hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
            return json.loads(path.read_text())
        metadata = load('freeze.json')
        for job in load('jobs.json'):
            path = directory / 'results' / (job['id'] + '.json')
            failure = path.with_suffix('.failure.json')
            if failure.exists():
                failures.append({'input': filename, 'job': job['id'], 'failure': load(str(failure.relative_to(directory)))})
                continue
            if not path.exists():
                pending.append({'input': filename, 'job': job['id']})
                continue
            hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
            row = read_result(path, job, metadata['source_sha256'])
            if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
                raise ValueError('An authoritative match is invalid.')
            side = job['condition']['candidate_side']
            trace = row['forecast_trace']
            if sorted(t['round'] for t in trace) != list(range(1, row['rounds'] + 1)):
                raise ValueError('Incomplete or duplicate prediction trace.')
            records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
            actual = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
                      for r in records if r['round'] > 0 and r['player'] == 1 - side}
            mismatches = sorted(t['round'] for t in trace if t['predicted_actions'] != actual[t['round']])
            if mismatches != row['forecast_mismatch_rounds'] or row['forecast_trace_missing_rounds']:
                raise ValueError('Prediction diagnostic differs from replay.')
            attacks = [t for t in trace if t.get('search') is not None or t.get('attack_count', 0)]
            cases.append({'condition': job['condition'], 'outcome': row['candidate_outcome'],
                          'hp_candidate_first': row['hp'][::1 if side == 0 else -1], 'rounds': row['rounds'],
                          'runtime_seconds': row['runtime_seconds'], 'forecast_mismatch_rounds': mismatches,
                          'attack_trace': attacks, 'result_path': str(path), 'replay_path': row['replay_path'],
                          'canonical_replay_sha256': canonical_replay(row['replay_path'], side)})
    pairs, groups, counts = [], defaultdict(list), defaultdict(Counter)
    for case in cases:
        c = case['condition']
        groups[(c['candidate_id'], c['opponent_id'])].append(case)
        counts[c['candidate_id']][case['outcome']] += 1
    for identity, group in sorted(groups.items()):
        sides = sorted(c['condition']['candidate_side'] for c in group)
        if len(set(sides)) != len(sides):
            raise ValueError('Duplicate condition and assignment.')
        pairs.append({'candidate': identity[0], 'opponent': identity[1], 'sides': sides,
                      'same_complete_trajectory': len(group) == 2 and len({c['canonical_replay_sha256'] for c in group}) == 1})
    output = {'time_utc': now(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256': hashes, 'cases': cases, 'failures': failures, 'pending': pending,
              'valid_completed': len(cases), 'expected': args.expected, 'pairs': pairs,
              'outcomes': {k: dict(v) for k, v in counts.items()},
              'games_with_forecast_mismatch': sum(bool(c['forecast_mismatch_rounds']) for c in cases),
              'scope': 'Each condition is an actual original-engine development game, not an independent random sample.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: v for k, v in output.items() if k not in ('input_sha256', 'cases', 'pairs')}))
    assert len(cases) == args.expected and not failures and not pending
    assert all(p['sides'] == [0, 1] for p in pairs)


if __name__ == '__main__':
    main()
