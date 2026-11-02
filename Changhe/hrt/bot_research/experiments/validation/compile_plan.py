"""Build policy data from an independently replayed development game."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.bots.counters.compiled_plan import canonical_observation
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.replay_audit import audit_row
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions
from bot_research.experiments.validation.final_validation import now


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--result', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    source = Path(args.result)
    output = Path(args.output)
    if source.is_absolute() or output.is_absolute() or '..' in source.parts + output.parts:
        parser.error('Use project-relative paths.')
    row = json.loads(source.read_text())
    if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
        raise ValueError('Cannot compile an invalid source game.')
    audit = audit_row(row)
    side = row['condition']['candidate_side']
    observations, actions = observations_and_actions(row, side)
    data = {'schema_version': 1, 'time_utc': now(), 'source_result': str(source),
            'source_result_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'source_replay': row['replay_path'], 'source_replay_sha256': row['trajectory_sha256'],
            'source_condition': row['condition'], 'source_audit': audit,
            'scope': 'Fixed own policy data compiled from one development game. Full observation equality is required before each recorded action list.',
            'rounds': [{'round': rnd, 'observation': canonical_observation(observations[rnd]),
                        'actions': actions[rnd]} for rnd in sorted(actions)]}
    atomic_json(output, data, exclusive=True)
    print(json.dumps({'file': str(output), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                      'rounds': len(data['rounds']), 'source_replay_checked': True}))


if __name__ == '__main__':
    main()
