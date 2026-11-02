"""Replay source games and select an exact maximum compatible plan subset."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.bots.counters.compiled_plan import canonical_observation
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.replay_audit import audit_row
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions


def conflict_round(left, right):
    for a, b in zip(left['rounds'], right['rounds']):
        if a['round'] != b['round']:
            raise ValueError('Nonconsecutive plan indices.')
        if a['observation'] != b['observation']:
            return None
        if a['actions'] != b['actions']:
            return a['round']
    return None


def maximum_compatible(plans):
    n = len(plans)
    if not 0 < n <= 20:
        raise ValueError('This exact finite search supports one through twenty plans.')
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            rnd = conflict_round(plans[i], plans[j])
            if rnd is not None:
                edges.append({'left': i, 'right': j, 'round': rnd})
    masks = [(1 << edge['left']) | (1 << edge['right']) for edge in edges]
    best = 0
    for mask in range(1 << n):
        if mask.bit_count() <= best.bit_count():
            continue
        if not any(mask & edge == edge for edge in masks):
            best = mask
    return [i for i in range(n) if best & (1 << i)], edges


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--audit', required=True)
    args = parser.parse_args()
    manifest = json.loads(Path(args.manifest).read_text())
    plans, inputs, summaries = [], {}, []
    for source in manifest['sources']:
        path = Path(source['path'])
        if path.is_absolute() or '..' in path.parts:
            raise ValueError('Source paths must be project relative.')
        inputs[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        rows = [json.loads(line) for line in path.read_text().splitlines()] if path.suffix == '.jsonl' else [json.loads(path.read_text())]
        for index, row in enumerate(rows):
            condition = row['condition']
            side = condition.get('candidate_side', condition.get('counter_side'))
            if side != 0:
                continue
            if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
                raise ValueError('Invalid source game.')
            if row['result']['winner'] != side:
                raise ValueError('This declared library uses only counter wins.')
            checked = audit_row(row)
            observations, actions = observations_and_actions(row, side)
            key = f'p{len(plans):03d}'
            plan = {'id': key, 'source_file': str(path), 'source_row': index,
                    'source_file_sha256': inputs[str(path)], 'source_condition': condition,
                    'source_replay': row['replay_path'], 'source_replay_sha256': row['trajectory_sha256'],
                    'rounds': [{'round': rnd, 'observation': canonical_observation(observations[rnd]),
                                'actions': actions[rnd]} for rnd in sorted(actions)]}
            plans.append(plan)
            summaries.append({'id': key, 'source_file': str(path), 'source_row': index,
                              'source_condition': condition, 'replay_audit': checked})
    selected, edges = maximum_compatible(plans)
    data = {'schema_version': 2, 'time_utc': now(), 'plans': [plans[i] for i in selected],
            'selection': 'Maximum cardinality compatible subset; ties use the lowest ascending subset mask.',
            'scope': 'Fixed public policy data; exact history matching, no live hidden action access.'}
    atomic_json(args.output, data, exclusive=True)
    audit = {'time_utc': now(), 'compiler_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'manifest_sha256': hashlib.sha256(Path(args.manifest).read_bytes()).hexdigest(),
             'input_sha256': inputs, 'source_plans': summaries, 'conflicts': edges,
             'selected_indices': selected, 'plan_count': len(plans), 'selected_count': len(selected),
             'subsets_enumerated': 1 << len(plans), 'data_file': args.output,
             'data_sha256': hashlib.sha256(Path(args.output).read_bytes()).hexdigest(),
             'scope': 'Exact finite compatibility selection and unchanged-engine source replay, not fresh policy evaluation.'}
    atomic_json(args.audit, audit, exclusive=True)
    print(json.dumps({key: audit[key] for key in ('plan_count', 'selected_count', 'conflicts', 'selected_indices', 'data_sha256')}))


if __name__ == '__main__':
    main()
