"""Independently check library filtering against recorded public observations."""
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    directory = Path(args.input)
    hashes, cache = {}, {}
    def load(name):
        name = str(name)
        if name not in cache:
            raw = Path(name).read_bytes()
            hashes[name] = hashlib.sha256(raw).hexdigest()
            cache[name] = [json.loads(s) for s in raw.splitlines()] if name.endswith('.jsonl') else json.loads(raw)
        return cache[name]
    metadata, jobs = load(directory / 'freeze.json'), load(directory / 'jobs.json')
    cases, unresolved, counts = [], [], Counter()
    for job in jobs:
        path = directory / 'results' / (job['id'] + '.json')
        failed = path.with_suffix('.failure.json')
        if failed.exists() or not path.exists():
            unresolved.append({'condition': job['condition'], 'failure': load(failed) if failed.exists() else None})
            continue
        load(path)
        row = read_result(path, job, metadata['source_sha256'])
        if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
            raise ValueError('Invalid completed game.')
        condition, side = job['condition'], job['condition']['candidate_side']
        params = dict(parse_qsl(condition['candidate_spec'].partition('?')[2]))
        data = load(params['data_file'])
        if hashes[params['data_file']] != params['data_sha256'] or metadata['source_sha256'].get(params['data_file']) != params['data_sha256']:
            raise ValueError('Library data differ from the declared and frozen input.')
        plans = {p['id']: {t['round']: t for t in p['rounds']} for p in data['plans']}
        active = list(plans)
        observations, actions = observations_and_actions(row, side)
        trace = row['compiled_trace']
        if not isinstance(trace, list) or [t['round'] for t in trace] != list(range(1, row['rounds'] + 1)):
            raise ValueError('Missing, duplicate or reordered library trace.')
        switched, first_departure = False, None
        for entry in trace:
            rnd = entry['round']
            if not switched:
                active = [key for key in active if rnd in plans[key]
                          and plans[key][rnd]['observation'] == canonical_observation(observations[rnd])]
                if not active:
                    switched, first_departure = True, rnd
            if entry['active'] != active or entry['fallback'] != (params.get('fallback', 'fortress15') if switched else None):
                raise ValueError('Library trace differs from complete public-history filtering.')
            if not switched:
                if any(plans[key][rnd]['actions'] != actions[rnd] for key in active):
                    raise ValueError('Recorded action differs from the common library action.')
        canonical = canonical_replay(row['replay_path'], side)
        matching = []
        for plan in data['plans']:
            source = load(plan['source_file'])
            if hashes[plan['source_file']] != plan['source_file_sha256']:
                raise ValueError('Original source evidence changed.')
            original = source[plan['source_row']] if isinstance(source, list) else source
            original_side = original['condition'].get('candidate_side', original['condition'].get('counter_side'))
            if canonical == canonical_replay(original['replay_path'], original_side):
                matching.append({'plan': plan['id'], 'source_condition': original['condition'],
                                 'source_decision_seconds': original['decision_seconds'][original_side]})
        cases.append({'condition': condition, 'outcome': row['candidate_outcome'],
                      'hp_candidate_first': row['hp'][::1 if side == 0 else -1],
                      'rounds': row['rounds'], 'runtime_seconds': row['runtime_seconds'],
                      'candidate_decision_seconds': row['decision_seconds'][side],
                      'first_departure_round': first_departure,
                      'rounds_using_library': row['rounds'] if first_departure is None else first_departure - 1,
                      'final_active_plans': active, 'same_source_trajectories': matching,
                      'canonical_replay_sha256': canonical, 'result_path': str(path),
                      'replay_path': row['replay_path'], 'guard_audit_passed': True})
        counts[row['candidate_outcome']] += 1
    groups = defaultdict(list)
    for case in cases:
        groups[case['condition']['opponent_id']].append(case)
    pairs = []
    for opponent, group in sorted(groups.items()):
        sides = sorted(c['condition']['candidate_side'] for c in group)
        if len(sides) != len(set(sides)):
            raise ValueError('Duplicate condition.')
        pairs.append({'opponent': opponent, 'sides': sides, 'same_complete_trajectory':
                      sides == [0, 1] and len({c['canonical_replay_sha256'] for c in group}) == 1})
    output = {'time_utc': now(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256': hashes, 'planned': len(jobs), 'valid_completed': len(cases),
              'unresolved': unresolved, 'outcomes': dict(counts), 'cases': cases, 'pairs': pairs,
              'scope': 'Source-attested development games and complete public-history checks. Timings exclude policy construction and are not calibrated speed benchmarks.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({key: output[key] for key in ('planned', 'valid_completed', 'outcomes', 'unresolved')}))


if __name__ == '__main__':
    main()
