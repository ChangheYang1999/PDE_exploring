"""Record the complete no-defense ablation and declare descriptive comparisons."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    root = Path('bot_research/runs/validation')
    names = ['forecast-grower-strict-001', 'forecast-grower-nodefense-strict-001',
             'forecast-grower-nodefense-forecast-audit-001',
             'forecast-grower-nodefense-blind-audit-001',
             'forecast-grower-nodefense-replay-audit-001']
    paths = [root / (name + '.json') for name in names]
    full, control, forecasts, blind, replay = [json.loads(p.read_text()) for p in paths]
    assert full['valid_conditions'] == 16 and not full['unresolved']
    assert control['valid_conditions'] == 4 and not control['unresolved']
    assert control['attempt_counts'] == {'valid': 4}
    assert not forecasts['games_with_forecast_mismatch']
    assert blind['all_passed'] and blind['checked_rounds'] == 42
    assert replay['all_passed'] and replay['count'] == 4
    assert all(p['same_complete_trajectory'] for p in control['pairs'])
    baseline = {(c['condition']['candidate_id'], c['condition']['candidate_side']): c
                for c in control['cases']}
    pairs = []
    for c in full['cases']:
        ident = c['condition']['candidate_id']
        key = (ident.split('_defend')[0] + '_defend51', c['condition']['candidate_side'])
        b = baseline[key]
        pairs.append({'label': ident + '_side' + str(key[1]),
                      'a': b['result_path'], 'b': c['result_path']})
    now = datetime.now(timezone.utc).isoformat()
    pair_path = Path('bot_research/experiments/validation/grower-defense-comparisons-001.json')
    atomic_json(pair_path, pairs, exclusive=True)
    out = {'time_utc': now, 'input_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'cases': control['cases'], 'pairs': control['pairs'],
           'all_replays_passed': replay['all_passed'],
           'all_blind_actions_equal': blind['all_passed'],
           'blind_checked_rounds': blind['checked_rounds'],
           'forecast_games_with_mismatch': forecasts['games_with_forecast_mismatch'],
           'match_runtime_sum_seconds': sum(c['runtime_seconds'] for c in control['cases']),
           'candidate_decision_sum_seconds': sum(c['decision_seconds_candidate_first'][0]['total'] for c in control['cases']),
           'candidate_decision_max_seconds': max(c['decision_seconds_candidate_first'][0]['max'] for c in control['cases']),
           'comparison_pairs_path': str(pair_path),
           'conclusion': 'With no early gun, adding any tested defensive start reverses L to W. With a round-2 gun the blind baseline already wins. Accurate prediction necessity is not isolated by this intervention.',
           'scope': 'Post-result deterministic development ablation against fixed Lead10 C2 adaptive, standard start. Four baseline games are reused in sixteen descriptive comparisons; these are not sixteen independent baseline samples.'}
    atomic_json(root / 'forecast-grower-nodefense-summary-001.json', out, exclusive=True)
    lines = ['# No-defense grower controls', '', 'Recorded: ' + now, '',
             'Opponent: fixed Lead10 C2 adaptive. Standard start, both player assignments. '
             'Growth lasts through round 6, then the counter spends on tier5; first defensive round is 51, beyond the game horizon.', '',
             '| Early gun | Result in each seat | Counter HP | Opponent HP | End round |',
             '|---|---|---:|---:|---:|']
    for c in control['cases']:
        if c['condition']['candidate_side'] == 0:
            lines.append('| ' + c['condition']['candidate_id'] + ' | ' + c['outcome'] + ' | ' + str(c['hp_candidate_first'][0]) + ' | ' + str(c['hp_candidate_first'][1]) + ' | ' + str(c['rounds']) + ' |')
    lines += ['', 'All four games pass source and legality checks and unchanged-engine replay. Both normalized seat pairs have identical complete trajectories. A fresh blind FeatureBluff recomputation matches every action over all 42 recorded rounds. All model forecasts also match, although they do not affect the disabled defensive branch.', '',
              'The original sixteen defensive games all win. Adding defense therefore reverses the no-gun result, while the round-2-gun baseline already wins. This comparison does not establish that exact forecasting is necessary: the intervention enables the entire defensive policy. The separate visible-roster ablation addresses that question.', '',
              'These controls were declared after the original results. They are development evidence, not a reserved-pool score. Sixteen descriptive comparison pairs reuse four controls; the pairs are not independent samples.', '',
              'Evidence: forecast-grower-nodefense-{strict,forecast-audit,blind-audit,replay-audit,summary}-001.json; forecast-grower-strict-001.json.']
    (root / 'forecast-grower-nodefense-summary-001.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'time_utc': now, 'pairs': len(pairs), 'outcomes': control['outcomes']}))


if __name__ == '__main__':
    main()
