"""Check contingent-plan trace guards and the fresh game trajectories."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qsl
from bot_research.bots.counters.compiled_plan import canonical_observation
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now, read_result
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    directory = Path(args.input)
    hashes = {}
    def load(path):
        hashes[str(path)] = sha(path)
        return json.loads(Path(path).read_text())
    metadata = load(directory / 'freeze.json')
    jobs = load(directory / 'jobs.json')
    cases, unresolved = [], []
    counts = defaultdict(Counter)
    for job in jobs:
        path = directory / 'results' / (job['id'] + '.json')
        failure = path.with_suffix('.failure.json')
        if failure.exists() or not path.exists():
            unresolved.append({'condition': job['condition'], 'failure': load(failure) if failure.exists() else None})
            continue
        hashes[str(path)] = sha(path)
        row = read_result(path, job, metadata['source_sha256'])
        if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
            raise ValueError('Invalid completed game.')
        c = job['condition']
        side = c['candidate_side']
        spec = c['candidate_spec']
        item = {'condition': c, 'outcome': row['candidate_outcome'],
                'hp_candidate_first': row['hp'][::1 if side == 0 else -1],
                'rounds': row['rounds'], 'runtime_seconds': row['runtime_seconds'],
                'candidate_decision_seconds': row['decision_seconds'][side],
                'result_path': str(path), 'replay_path': row['replay_path'],
                'canonical_replay_sha256': canonical_replay(row['replay_path'], side)}
        if spec.startswith('bot_research.bots.counters.compiled_plan:'):
            params = dict(parse_qsl(spec.partition('?')[2]))
            plan_name = params['plan_file']
            data = load(plan_name)
            if hashes[plan_name] != params['plan_sha256'] or metadata['source_sha256'].get(plan_name) != params['plan_sha256']:
                raise ValueError('Policy data differ from the declaration or frozen inputs.')
            source = load(data['source_result'])
            if hashes[data['source_result']] != data['source_result_sha256']:
                raise ValueError('Original source match changed.')
            table = {t['round']: t for t in data['rounds']}
            observations, actions = observations_and_actions(row, side)
            trace = row['compiled_trace']
            if not isinstance(trace, list) or [t['round'] for t in trace] != list(range(1, row['rounds'] + 1)):
                raise ValueError('Missing, extra, or reordered plan trace.')
            switched = False
            first_divergence = None
            for entry in trace:
                rnd = entry['round']
                expected = not switched and rnd in table and canonical_observation(observations[rnd]) == table[rnd]['observation']
                if not expected and not switched:
                    first_divergence = rnd
                switched = switched or not expected
                if type(entry['plan_matched']) is not bool or entry['plan_matched'] != expected:
                    raise ValueError('Plan guard trace differs from complete observation comparison.')
                if entry['fallback'] != (params.get('fallback', 'fortress15') if switched else None):
                    raise ValueError('Incorrect permanent fallback trace.')
                if expected and actions[rnd] != table[rnd]['actions']:
                    raise ValueError('On-plan submission differs from the exact action list.')
            original_side = source['condition']['candidate_side']
            original_hash = canonical_replay(source['replay_path'], original_side)
            item.update(plan_guard_audit_passed=True, first_departure_round=first_divergence,
                        plan_rounds=sum(t['plan_matched'] for t in trace),
                        same_complete_trajectory_as_source=item['canonical_replay_sha256'] == original_hash)
        counts[c['candidate_id']][row['candidate_outcome']] += 1
        cases.append(item)
    groups = defaultdict(list)
    for item in cases:
        c = item['condition']
        groups[(c['candidate_id'], c['opponent_id'])].append(item)
    pairs = []
    for (candidate, opponent), group in sorted(groups.items()):
        sides = sorted(c['condition']['candidate_side'] for c in group)
        if len(set(sides)) != len(sides):
            raise ValueError('Duplicate candidate, opponent, and assignment.')
        pairs.append({'candidate': candidate, 'opponent': opponent, 'sides': sides,
                      'same_complete_trajectory': sides == [0, 1] and len({c['canonical_replay_sha256'] for c in group}) == 1})
    output = {'time_utc': now(), 'checker_sha256': sha(__file__), 'input_sha256': hashes,
              'planned': len(jobs), 'valid_completed': len(cases), 'unresolved': unresolved,
              'outcomes': {key: dict(value) for key, value in counts.items()},
              'cases': cases, 'pairs': pairs,
              'scope': 'Fresh development games with complete plan guards checked against original-engine observations. Runtime observations are not calibrated speed benchmarks.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({key: output[key] for key in ('valid_completed', 'planned', 'outcomes')}))


if __name__ == '__main__':
    main()
