"""Audit forecast traces in an already source-checked retry-aware campaign."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    strict = json.loads(Path(args.strict_audit).read_text())
    primary = {(c['directory'], c['job']) for c in strict['cases']}
    checked = []
    inputs = {args.strict_audit: digest(args.strict_audit)}
    for case in strict['attempts']:
        if case['status'] != 'valid':
            continue
        path = case['result_path']
        inputs[path] = digest(path)
        # The strict audit's source attestation applies to exactly these bytes.
        assert strict['input_sha256'][path] == inputs[path]
        row = json.loads(Path(path).read_text())
        side = row['condition']['candidate_side']
        trace = row['forecast_trace']
        assert sorted(t['round'] for t in trace) == list(range(1, row['rounds']+1))
        replay_path = row['replay_path']
        inputs[replay_path] = digest(replay_path)
        assert inputs[replay_path] == row['trajectory_sha256']
        records = [json.loads(line) for line in Path(replay_path).read_text().splitlines()]
        actual = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
                  for r in records if r['round'] > 0 and r['player'] == 1-side}
        mismatches = [t['round'] for t in trace if t['predicted_actions'] != actual[t['round']]]
        assert mismatches == row['forecast_mismatch_rounds']
        assert not row['forecast_trace_missing_rounds']
        checked.append({'directory': case['directory'], 'job': case['job'],
                        'condition': row['condition'], 'primary': (case['directory'],case['job']) in primary,
                        'forecast_mismatch_rounds': mismatches,
                        'trace_rounds': len(trace), 'hp_candidate_first': case['hp_candidate_first'],
                        'outcome': case['outcome'], 'rounds': case['rounds'],
                        'attack_trace': [t for t in trace if t.get('search') is not None or t.get('attack_count',0)]})
    assert sum(c['primary'] for c in checked) == strict['valid_conditions']
    output = {'time_utc': now(), 'checker_sha256': digest(__file__), 'input_sha256': inputs,
              'valid_conditions': strict['valid_conditions'], 'expected_conditions': strict['expected_conditions'],
              'unresolved': strict['unresolved'], 'attempt_counts': strict['attempt_counts'],
              'checked_valid_attempts': len(checked), 'attempts': checked,
              'games_with_forecast_mismatch': sum(bool(c['forecast_mismatch_rounds']) for c in checked),
              'scope': 'Forecast correctness is separate from source/outcome validity. All completed retries are checked and do not add independent conditions.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k:output[k] for k in ('valid_conditions','expected_conditions','attempt_counts','checked_valid_attempts','games_with_forecast_mismatch','unresolved')}))
    assert not output['games_with_forecast_mismatch']


if __name__ == '__main__':
    main()
