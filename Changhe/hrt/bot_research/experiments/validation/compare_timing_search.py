"""Compare one-round package objectives with complete matched game outcomes."""
from __future__ import annotations
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions


def canonical(observation):
    side = observation['player']
    return {'round': observation['round'], 'rules': observation['rules'],
            'players': [{k: v for k, v in observation['players'][p].items() if k != 'name'}
                        for p in (side, 1 - side)]}


def read_inputs(names, hashes):
    rows = []
    for name in names:
        path = Path(name)
        hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        for line in path.read_text().splitlines():
            row = json.loads(line)
            if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
                raise ValueError('Invalid match in timing comparison.')
            if row['forecast_mismatch_rounds'] or row['forecast_trace_missing_rounds']:
                raise ValueError('This comparison requires exact recorded target predictions.')
            rows.append(row)
    return rows


def detail(row):
    c = row['condition']
    side, rnd = c['counter_side'], c['parameters']['attack_round']
    own, opponent = row['hp'][side], row['hp'][1 - side]
    trace = {t['round']: t for t in row['forecast_trace']}
    history = {t['round']: t for t in row['history']}
    t = trace.get(rnd)
    attack = t.get('search') if t else None
    gain = attack['predicted_gain'] if attack else (t.get('forecast_attack_gain', 0) if t else None)
    actual = history[rnd]['players'][side]['combat']['damage_dealt'] if rnd in history else None
    return {'parameters': c['parameters'], 'outcome': row['counter_outcome'],
            'hp_candidate_first': [own, opponent], 'final_hp_margin': own - opponent,
            'rounds': row['rounds'], 'predicted_immediate_gain': gain,
            'actual_attack_round_damage': actual, 'replay_path': row['replay_path']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pure', nargs='+', required=True)
    parser.add_argument('--mixed', nargs='+', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    hashes = {}
    pure, mixed = read_inputs(args.pure, hashes), read_inputs(args.mixed, hashes)
    groups = defaultdict(list)
    for row in pure:
        c = row['condition']
        groups[(c['parameters']['attack_round'], c['counter_side'])].append(row)
    cases = []
    for row in mixed:
        c = row['condition']
        rnd, side = c['parameters']['attack_round'], c['counter_side']
        controls = groups.get((rnd, side), [])
        if not controls:
            continue
        if sorted(r['condition']['parameters']['tier'] for r in controls) != ['tier1', 'tier2', 'tier3', 'tier4', 'tier5']:
            raise ValueError('Incomplete or repeated pure-tier controls.')
        observations, actions = observations_and_actions(row, side)
        prefix_matches, prediction_matches = [], []
        predicted = {t['round']: t['predicted_actions'] for t in row['forecast_trace']}
        for control in controls:
            obs2, actions2 = observations_and_actions(control, side)
            if rnd not in observations or rnd not in obs2:
                raise ValueError('An attack round was not reached.')
            prefix_matches.append(all(canonical(observations[k]) == canonical(obs2[k]) for k in range(1, rnd + 1))
                                  and all(actions[k] == actions2[k] for k in range(1, rnd)))
            predicted2 = {t['round']: t['predicted_actions'] for t in control['forecast_trace']}
            prediction_matches.append(predicted[rnd] == predicted2[rnd])
        d, ds = detail(row), [detail(r) for r in controls]
        best_gain = max(x['predicted_immediate_gain'] for x in ds)
        best_margin = max(x['final_hp_margin'] for x in ds)
        cases.append({'attack_round': rnd, 'side': side,
                      'all_pre_attack_states_and_own_actions_equal': all(prefix_matches),
                      'all_attack_round_target_predictions_equal': all(prediction_matches),
                      'mixed_immediate_gain_at_least_all_pure_controls': d['predicted_immediate_gain'] >= best_gain,
                      'mixed_final_margin_minus_best_pure': d['final_hp_margin'] - best_margin,
                      'mixed': d, 'pure': ds})
    output = {'time_utc': now(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256': hashes, 'comparisons': cases,
              'scope': 'Matched development games. Immediate gain and full-game HP margin are different objectives; no population win-rate claim.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'comparisons': len(cases), 'all_prefixes_equal': all(x['all_pre_attack_states_and_own_actions_equal'] for x in cases),
                      'immediate_gain_dominance': all(x['mixed_immediate_gain_at_least_all_pure_controls'] for x in cases),
                      'full_game_margin_differences': [x['mixed_final_margin_minus_best_pure'] for x in cases]}))


if __name__ == '__main__':
    main()
