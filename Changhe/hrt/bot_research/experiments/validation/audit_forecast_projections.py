"""Classify recorded forecast errors without re-executing either policy.

Exact action equality, ordered construction equality and ordered attack-purchase
 equality are distinct claims. This audit does not infer one from another.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.final_validation import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def projection(actions, operations):
    return [action for action in actions if action['op'] in operations]


def counts(actions):
    return dict(sorted(Counter(action['op'] + ':' + action.get('type', '')
                               for action in actions).items()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', nargs='+', required=True)
    parser.add_argument('--expected', type=int, required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    inputs, cases, groups = {}, [], defaultdict(Counter)
    for name in args.inputs:
        directory = Path(name)
        jobfile = directory / 'jobs.json'
        inputs[str(jobfile)] = digest(jobfile)
        jobs = json.loads(jobfile.read_text())
        for job in jobs:
            filename = directory / 'results' / (job['id'] + '.json')
            if filename.with_suffix('.failure.json').exists():
                raise ValueError('A declared game failed; account for it before this audit.')
            summary = checked_row(str(filename), inputs)
            row = json.loads(filename.read_text())
            side = row['condition']['candidate_side']
            actual = {}
            for line in Path(row['replay_path']).read_text().splitlines():
                record = json.loads(line)
                if record['round'] > 0 and record['player'] == 1 - side:
                    actual[record['round']] = [event['action'] for event in record['event']
                                               if event['kind'] == 'action']
            trace = row['forecast_trace']
            if sorted(item['round'] for item in trace) != list(range(1, row['rounds'] + 1)):
                raise ValueError('Missing, repeated or unexpected forecast round.')
            detail = []
            projection_errors = Counter()
            for item in trace:
                rnd, predicted = item['round'], item['predicted_actions']
                observed = actual[rnd]
                errors = {'full_actions': predicted != observed,
                          'construction': projection(predicted, {'build_wall', 'build_turret'}) !=
                                          projection(observed, {'build_wall', 'build_turret'}),
                          'minion_purchases': projection(predicted, {'buy_minion'}) !=
                                              projection(observed, {'buy_minion'}),
                          'factory_purchases': projection(predicted, {'buy_factory'}) !=
                                               projection(observed, {'buy_factory'})}
                projection_errors.update(key for key, error in errors.items() if error)
                if errors['full_actions']:
                    detail.append({'round': rnd, 'different': errors,
                                   'predicted_counts': counts(predicted),
                                   'actual_counts': counts(observed)})
            if [item['round'] for item in detail] != row['forecast_mismatch_rounds']:
                raise ValueError('Mismatch with saved forecast diagnostic.')
            candidate = row['condition']['candidate_id']
            group = groups[candidate]
            group['games'] += 1
            group['forecast_rounds'] += len(trace)
            group.update({key + '_error_rounds': value for key, value in projection_errors.items()})
            group['games_with_error'] += bool(detail)
            group[row['candidate_outcome']] += 1
            cases.append({**summary, 'forecast_rounds': len(trace),
                          'projection_error_rounds': dict(projection_errors),
                          'maximum_submitted_attack_count': max((t.get('attack_count', 0) for t in trace), default=0),
                          'mismatches': detail})
    if len(cases) != args.expected:
        raise ValueError('Unexpected number of cases.')
    output = {'time_utc': now(), 'checker_sha256': digest(__file__),
              'input_sha256': inputs, 'cases': cases, 'valid_completed': len(cases),
              'groups': {name: dict(value) for name, value in sorted(groups.items())},
              'scope': 'All declared games must be complete and source-attested. Ordered projections are compared within the same observed round. Original-engine replay is checked separately. Error frequency is descriptive, not an independent-sample estimate. A purchase-count bound does not establish equivalence to another cap because an unsubmitted hypothetical attack may differ.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'valid_completed': len(cases), 'groups': output['groups']}))


if __name__ == '__main__':
    main()
