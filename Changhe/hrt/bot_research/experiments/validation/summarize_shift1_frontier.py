"""Freeze a descriptive checkpoint of incomplete development campaigns."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    root = Path('bot_research/runs/validation')
    inputs = {}
    def read(name):
        path = root / (name + '.json')
        inputs[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        return json.loads(path.read_text())
    names = [('visible-grower', 'visible-grower'),
             ('lead-thirteen-fortress4', 'lead-thirteen-fortress4'),
             ('lead-thirteen-splash', 'lead-thirteen-splash'),
             ('lead-thirteen-fortress2', 'lead-thirteen-fortress2')]
    campaigns = {}
    for label, base in names:
        strict = read(base + '-partial-strict-001')
        forecasts = read(base + '-partial-forecasts-001')
        assert forecasts['valid_conditions'] == strict['valid_conditions']
        errors = Counter()
        for c in forecasts['cases']:
            if c['primary']:
                errors.update(c['projection_error_rounds'])
        campaigns[label] = {'expected': strict['expected_conditions'],
            'valid': strict['valid_conditions'], 'unresolved': len(strict['unresolved']),
            'attempt_counts': strict['attempt_counts'], 'outcomes': strict['outcomes'],
            'forecast_rounds': sum(c['forecast_rounds'] for c in forecasts['cases'] if c['primary']),
            'projection_error_rounds': dict(errors),
            'cases': [{k: c[k] for k in ('condition', 'outcome', 'hp_candidate_first', 'rounds', 'result_path')}
                      for c in strict['cases']]}
    replay = read('lead-thirteen-partial-replays-001')
    visible_replay = read('visible-grower-partial-replays-001')
    assert replay['all_passed'] and replay['count'] == 16
    assert visible_replay['all_passed'] and visible_replay['count'] == 5
    exact = read('forecast-grower-strict-001')
    lookup = {(c['condition']['candidate_id'], c['condition']['candidate_side']): c
              for c in exact['cases']}
    pairs = []
    for c in campaigns['visible-grower']['cases']:
        cond = c['condition']
        ident = cond['candidate_id'].removeprefix('visible_')
        original = lookup[(ident, cond['candidate_side'])]
        pairs.append({'label': cond['candidate_id'] + '_side' + str(cond['candidate_side']),
                      'a': original['result_path'], 'b': c['result_path']})
    pair_path = Path('bot_research/experiments/validation/visible-grower-partial-comparisons-001.json')
    atomic_json(pair_path, pairs, exclusive=True)
    out = {'time_utc': datetime.now(timezone.utc).isoformat(), 'input_sha256': inputs,
           'campaigns': campaigns, 'all_21_completed_engine_replays_passed': True,
           'comparison_pairs': str(pair_path),
           'scope': 'Incomplete declared development matrices. All successful games are retained, including draws. Timeouts and unstarted conditions remain unresolved and are not losses. No complete-campaign ranking is inferred.'}
    atomic_json(root / 'shift1-frontier-checkpoint-001.json', out, exclusive=True)
    print(json.dumps({name: {k: v[k] for k in ('expected', 'valid', 'unresolved', 'attempt_counts', 'forecast_rounds', 'projection_error_rounds')} for name, v in campaigns.items()}))


if __name__ == '__main__':
    main()
