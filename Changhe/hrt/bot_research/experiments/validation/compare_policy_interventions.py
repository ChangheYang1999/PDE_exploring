"""Trace explicitly declared full-policy comparisons with fresh source checks.

The input names two completed results per comparison. This reports the first
record and action differences without claiming a local mechanism unless the
intervention and the common history support that interpretation separately.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.analyze_partial_ablation import actions, summary
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.compare_feature_ablation import records
from bot_research.experiments.validation.final_validation_strict import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pairs', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--trace-through', type=int, default=12)
    args = parser.parse_args()
    pairs = json.loads(Path(args.pairs).read_text())
    inputs = {args.pairs: digest(args.pairs)}
    comparisons = []
    for pair in pairs:
        checked = {label: checked_row(pair[label], inputs) for label in ('a', 'b')}
        raw = {label: json.loads(Path(pair[label]).read_text()) for label in ('a', 'b')}
        traces = {label: {(r['round'], r['player']): r for r in records(raw[label])}
                  for label in ('a', 'b')}
        common = sorted(traces['a'].keys() & traces['b'].keys())
        changed = [key for key in common if traces['a'][key] != traces['b'][key]]
        changed_actions = [key for key in common
                           if actions(traces['a'][key]) != actions(traces['b'][key])]
        first = changed[0][0] if changed else None
        rounds = set(range(min(args.trace_through, raw['a']['rounds'], raw['b']['rounds']) + 1))
        if first is not None:
            rounds.update((max(0, first - 1), first))
        timelines = {label: [{'round': rnd,
                              'players': [summary(trace[(rnd, side)]) for side in (0, 1)]}
                             for rnd in sorted(rounds)
                             if all((rnd, side) in trace for side in (0, 1))]
                     for label, trace in traces.items()}
        comparisons.append({'label': pair['label'], **checked,
            'same_complete_trajectory': checked['a']['canonical_replay_sha256'] == checked['b']['canonical_replay_sha256'],
            'first_state_difference_round': first,
            'first_candidate_action_difference_round': next((k[0] for k in changed_actions if k[1] == 0), None),
            'first_opponent_action_difference_round': next((k[0] for k in changed_actions if k[1] == 1), None),
            'timelines': timelines})
    output = {'time_utc': now(), 'checker_sha256': digest(__file__), 'input_sha256': inputs,
              'comparisons': comparisons,
              'scope': 'Explicit policy comparisons on recorded standard-start games. Source checks are fresh; original-engine replay is audited separately. Timing differences are descriptive, not proof of an unspecified mechanism.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'pairs': len(comparisons), 'identical': sum(c['same_complete_trajectory'] for c in comparisons)}))


if __name__ == '__main__':
    main()
