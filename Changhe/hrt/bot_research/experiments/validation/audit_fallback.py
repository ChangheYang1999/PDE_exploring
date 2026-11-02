"""Audit one-way fallback traces and known-policy trajectory preservation."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--summary', required=True)
    parser.add_argument('--baseline-summary')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    source = Path(args.summary)
    summary = json.loads(source.read_text())
    hashes = {str(source): hashlib.sha256(source.read_bytes()).hexdigest()}
    baseline = []
    if args.baseline_summary:
        path = Path(args.baseline_summary)
        hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        baseline = json.loads(path.read_text())['cases']
    cases = []
    failures = []
    for case in summary['cases']:
        path = Path(case['result_path'])
        hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        row = json.loads(path.read_text())
        trace = row['identification_trace']
        issues = []
        if [t['round'] for t in trace] != list(range(1, row['rounds'] + 1)):
            issues.append('Incomplete or duplicate trace.')
        switches = [t['round'] for t in trace if t['fallback_switch_round'] is not None]
        first = min(switches, default=None)
        if first is not None:
            for t in trace:
                if t['round'] >= first:
                    if (t['fallback_switch_round'] != first or t['fallback_policy'] is None
                            or t['catalogue_policy_calls'] != 0 or t['fallback_policy_calls'] != 1
                            or t['predicted_actions']):
                        issues.append('Post-switch controller invariant violated.')
                elif t['fallback_policy_calls'] or t['fallback_switch_round'] is not None:
                    issues.append('Unexpected pre-switch fallback call.')
        if row['forecast_model_errors']:
            issues.append('Catalogue model evaluation errors.')
        c = case['condition']
        references = [b for b in baseline if b['condition']['opponent_id'] == c['opponent_id']
                      and b['condition']['candidate_side'] == c['candidate_side']
                      and b['condition']['candidate_id'] == 'factory_identifier_sat12']
        same = None
        if first is None and references:
            if len(references) != 1:
                issues.append('Nonunique baseline condition.')
            same = case['canonical_replay_sha256'] == references[0]['canonical_replay_sha256']
            if not same:
                issues.append('Unswitched trajectory differs from baseline.')
        item = {'condition': c, 'outcome': case['outcome'], 'hp_candidate_first': case['hp_candidate_first'],
                'rounds': case['rounds'], 'runtime_seconds': case['runtime_seconds'],
                'switch_round': first, 'catalogue_policy_calls': sum(t['catalogue_policy_calls'] for t in trace),
                'fallback_policy_calls': sum(t['fallback_policy_calls'] for t in trace),
                'decision_seconds_candidate_first': row['decision_seconds'][::1 if c['candidate_side'] == 0 else -1],
                'matches_original_without_switch': same, 'issues': issues}
        cases.append(item)
        if issues:
            failures.append(item)
    output = {'time_utc': now(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256': hashes, 'cases': cases, 'failures': failures,
              'scope': 'A switch bounds catalogue calls, not the running time or strength of the fallback.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'checked': len(cases), 'failures': len(failures),
                      'switch_rounds': [c['switch_round'] for c in cases]}))
    assert not failures


if __name__ == '__main__':
    main()
