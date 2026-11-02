"""Summarize the completed exact-versus-visible information ablation."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    root = Path('bot_research/runs/validation')
    names = ['forecast-grower-strict-001', 'visible-grower-strict-final-001',
             'visible-grower-forecasts-final-001', 'visible-grower-replay-final-001']
    paths = [root/(name+'.json') for name in names]
    exact, visible, forecasts, replay = [json.loads(p.read_text()) for p in paths]
    assert exact['valid_conditions'] == visible['valid_conditions'] == 16
    assert not exact['unresolved'] and not visible['unresolved']
    assert not visible['repeat_disagreements']
    assert replay['all_passed'] and replay['count'] == 17
    assert all(p['same_complete_trajectory'] for p in visible['pairs'])
    lookup = {(c['condition']['candidate_id'], c['condition']['candidate_side']): c for c in exact['cases']}
    comparisons, pairs = [], []
    for v in visible['cases']:
        identifier = v['condition']['candidate_id'].removeprefix('visible_')
        side = v['condition']['candidate_side']
        e = lookup[identifier, side]
        pairs.append({'label': identifier+'_side'+str(side), 'a': e['result_path'], 'b': v['result_path']})
        comparisons.append({'condition': identifier, 'side': side,
            'exact_hp': e['hp_candidate_first'], 'visible_hp': v['hp_candidate_first'],
            'exact_rounds': e['rounds'], 'visible_rounds': v['rounds'],
            'exact_outcome': e['outcome'], 'visible_outcome': v['outcome'],
            'same_trajectory': e['canonical_replay_sha256'] == v['canonical_replay_sha256']})
    groups = forecasts['primary_groups']
    metrics = ('forecast_rounds', 'full_actions_error_rounds', 'construction_error_rounds',
               'minion_purchases_error_rounds', 'factory_purchases_error_rounds')
    counts = {m: sum(g[m] for g in groups.values()) for m in metrics}
    pair_path = Path('bot_research/experiments/validation/visible-grower-final-comparisons-001.json')
    atomic_json(pair_path, pairs, exclusive=True)
    now = datetime.now(timezone.utc).isoformat()
    result = {'time_utc': now, 'input_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        'comparisons': comparisons, 'counts': counts, 'attempt_counts': visible['attempt_counts'],
        'all_replays_passed': replay['all_passed'], 'normalized_seat_pairs_equal': len(visible['pairs']),
        'candidate_decision_sum_seconds': sum(c['decision_seconds_candidate_first'][0]['total'] for c in visible['cases']),
        'candidate_decision_max_seconds': max(c['decision_seconds_candidate_first'][0]['max'] for c in visible['cases']),
        'selected_match_runtime_seconds': sum(c['runtime_seconds'] for c in visible['cases']),
        'comparison_pairs_path': str(pair_path),
        'conclusion': 'Exact public-action forecasting is not necessary to win any of these sixteen conditions: the otherwise identical visible-roster controller also wins all sixteen. This does not establish which other defensive controller is sufficient against other targets.',
        'scope': 'Post-result deterministic development ablation against fixed Lead10 C2 adaptive. Eight distinct conditions with paired player assignments; repeats are not independent evidence.'}
    atomic_json(root/'visible-grower-summary-final-001.json', result, exclusive=True)
    lines = ['# Exact model versus visible-roster grower defense', '', 'Recorded: '+now, '',
        'Both controllers win all 16 declared games against the fixed Lead10 C2 adaptive policy. '
        'The visible-roster controller assumes no new opponent purchases when choosing defense; '
        'growth, flood timing, optional early gun and defensive start rules are unchanged.', '',
        '| Gun round; first defense round | Exact-model HP | Visible-roster HP | Exact / visible end round |',
        '|---|---|---|---|']
    for c in comparisons:
        if c['side'] == 0:
            lines.append('| '+c['condition']+' | '+':'.join(map(str,c['exact_hp']))+' | '+':'.join(map(str,c['visible_hp']))+' | '+str(c['exact_rounds'])+' / '+str(c['visible_rounds'])+' |')
    lines += ['', 'All 16 visible-roster conditions pass strict source and legality checks. '
        'All eight reversed-seat pairs have identical normalized complete histories. '
        'All 17 completed attempts pass unchanged-engine replay. One original 180-second timeout '
        'is retained; a separately declared 300-second retry resolved it and repeated the other seat as a control.', '',
        f"The empty-action prediction is deliberately wrong in {counts['full_actions_error_rounds']} of {counts['forecast_rounds']} selected-game rounds: "
        f"{counts['construction_error_rounds']} construction mismatches, {counts['minion_purchases_error_rounds']} minion-purchase mismatches and {counts['factory_purchases_error_rounds']} factory-purchase mismatches. "
        'These categories overlap. Wrong predictions are an intentional intervention, not invalid game outcomes.', '',
        result['conclusion'], '',
        'The earlier no-defense ablation loses without an early gun and wins with the round-2 gun. '
        'Taken together, the experiments support a role for defense in the no-gun conditions, while '
        'refuting the necessity of exact forecasting for these wins. They do not identify an optimal defense policy.', '',
        'Evidence: visible-grower-{strict,forecasts,replay,summary}-final-001.json and forecast-grower-strict-001.json. '
        'The comparison declaration is in experiments/validation/visible-grower-final-comparisons-001.json.']
    with (root/'visible-grower-summary-final-001.md').open('x') as stream:
        stream.write('\n'.join(lines)+'\n')
    print(json.dumps({'time_utc': now, 'counts': counts, 'comparisons': len(comparisons),
                      'identical_exact_visible': sum(c['same_trajectory'] for c in comparisons)}))


if __name__ == '__main__':
    main()
