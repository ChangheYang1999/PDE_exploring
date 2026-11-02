"""Validate projected traces and the complete private model behind each one."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    strict = json.loads(Path(args.strict).read_text())
    inputs = {args.strict:digest(args.strict)}
    cases = []
    total = Counter()
    for attempt in strict['attempts']:
        if attempt['status'] != 'valid':
            continue
        path = attempt['result_path']
        assert digest(path) == strict['input_sha256'][path]
        checked_row(path, inputs)
        result = json.loads(Path(path).read_text())
        side = result['condition']['candidate_side']
        replay = result['replay_path']
        inputs[replay] = digest(replay)
        assert inputs[replay] == result['trajectory_sha256']
        actual = {}
        for line in Path(replay).read_text().splitlines():
            row = json.loads(line)
            if row['round'] > 0 and row['player'] == 1-side:
                actual[row['round']] = [e['action'] for e in row['event'] if e['kind']=='action']
        traces = result['forecast_trace']
        assert [t['round'] for t in traces] == list(range(1,result['rounds']+1))
        counts = Counter()
        for trace in traces:
            projection = trace['projection']
            rnd = trace['round']
            if projection == 'opening':
                assert trace['full_predicted_actions'] is None
                expected = [{'op':'buy_minion','type':'tier1'} for _ in range(3)] if rnd==1 else []
            else:
                assert projection in ('minions','nonminions')
                assert trace['full_predicted_actions'] == actual[rnd]
                expected = [a for a in actual[rnd] if (a['op']=='buy_minion') == (projection=='minions')]
                counts['complete_model_rounds'] += 1
            assert trace['predicted_actions'] == expected
            counts['projection_rounds'] += 1
            counts['projection_differs_from_actual_rounds'] += expected != actual[rnd]
        cases.append(dict(result_path=path, projection=traces[0]['projection'], all_passed=True, counts=dict(counts)))
        total.update(counts)
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=digest(__file__),
                  input_sha256=inputs, cases=cases, all_passed=True, counts=dict(total),
                  valid_conditions=strict['valid_conditions'], expected_conditions=strict['expected_conditions'],
                  scope='All valid attempts, including retries. Exact complete-model forecasts are checked where a model exists; selected projections and fixed opening prior are checked in every round. Full engine replay is separate.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','valid_conditions','expected_conditions','counts','all_passed')}))


if __name__=='__main__':
    main()
