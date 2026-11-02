"""Retry-aware projection audit that permits deliberately inexact forecasts.

A wrong model prediction is reported separately from an invalid engine game.
All valid attempts are rechecked; primary selection comes from strict accounting.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_forecast_projections import projection, counts
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.final_validation import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    strict = json.loads(Path(args.strict_audit).read_text())
    inputs = {args.strict_audit: digest(args.strict_audit)}
    primary = {(c['directory'], c['job']) for c in strict['cases']}
    cases, groups = [], defaultdict(Counter)
    for case in strict['attempts']:
        if case['status'] != 'valid':
            continue
        path = case['result_path']
        if strict['input_sha256'][path] != digest(path):
            raise ValueError('Result differs from the strict-accounting input.')
        checked = checked_row(path, inputs)
        row = json.loads(Path(path).read_text())
        if row['condition'] != case['condition']:
            raise ValueError('Strict-accounting condition differs from the result.')
        side = row['condition']['candidate_side']
        replay = row['replay_path']
        inputs[replay] = digest(replay)
        if inputs[replay] != row['trajectory_sha256']:
            raise ValueError('Replay bytes differ from the result attestation.')
        actual = {}
        for line in Path(replay).read_text().splitlines():
            record = json.loads(line)
            if record['round'] > 0 and record['player'] == 1 - side:
                actual[record['round']] = [event['action'] for event in record['event']
                                           if event['kind'] == 'action']
        trace = row['forecast_trace']
        if sorted(item['round'] for item in trace) != list(range(1, row['rounds'] + 1)):
            raise ValueError('Incomplete or duplicate forecast rounds.')
        errors, details = Counter(), []
        for item in trace:
            rnd = item['round']
            predicted, observed = item['predicted_actions'], actual[rnd]
            different = {'full_actions': predicted != observed}
            for name, ops in (('construction', {'build_wall', 'build_turret'}),
                              ('minion_purchases', {'buy_minion'}),
                              ('factory_purchases', {'buy_factory'})):
                different[name] = projection(predicted, ops) != projection(observed, ops)
            errors.update(name for name, differs in different.items() if differs)
            if different['full_actions']:
                details.append({'round': rnd, 'different': different,
                                'predicted_counts': counts(predicted),
                                'actual_counts': counts(observed)})
        if [item['round'] for item in details] != row['forecast_mismatch_rounds']:
            raise ValueError('Saved mismatch diagnostic differs from replay.')
        if row['forecast_trace_missing_rounds']:
            raise ValueError('Saved trace diagnostic reports missing rounds.')
        selected = (case['directory'], case['job']) in primary
        cases.append({**checked, 'directory': case['directory'], 'job': case['job'],
                      'primary': selected, 'forecast_rounds': len(trace),
                      'projection_error_rounds': dict(errors), 'mismatches': details})
        if selected:
            group = groups[case['condition']['candidate_id']]
            group['games'] += 1
            group['forecast_rounds'] += len(trace)
            group['games_with_error'] += bool(details)
            group[case['outcome']] += 1
            group.update({name + '_error_rounds': value for name, value in errors.items()})
    if sum(c['primary'] for c in cases) != strict['valid_conditions']:
        raise ValueError('Primary valid-condition count differs from strict accounting.')
    output = {'time_utc': now(), 'checker_sha256': digest(__file__), 'input_sha256': inputs,
              'valid_conditions': strict['valid_conditions'],
              'expected_conditions': strict['expected_conditions'],
              'attempt_counts': strict['attempt_counts'], 'unresolved': strict['unresolved'],
              'checked_valid_attempts': len(cases), 'cases': cases,
              'primary_groups': {name: dict(value) for name, value in sorted(groups.items())},
              'scope': 'Deliberately inexact predictions are permitted and counted. All valid attempts are freshly source-checked. Primary groups do not double-count retries. Full original-engine replay is audited separately.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('valid_conditions', 'expected_conditions', 'checked_valid_attempts', 'primary_groups')}))
    if strict['unresolved']:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
