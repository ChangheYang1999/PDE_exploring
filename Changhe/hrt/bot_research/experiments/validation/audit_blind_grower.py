"""Check that a forecast-disabled grower returns the blind policy's actions.

Observations come from the unchanged engine as it replays the archived game.
The archived forecast policy is source-attested separately; it is not rerun.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
from urllib.parse import parse_qsl
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.feature_bluff import FeatureBluff
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    strict = json.loads(Path(args.strict_audit).read_text())
    if strict['valid_conditions'] != strict['expected_conditions'] or strict['unresolved']:
        raise ValueError('Finish every declared condition before this equivalence audit.')
    inputs = {args.strict_audit: digest(args.strict_audit)}
    sources = {str(p): digest(p) for p in static_closure(
        {'bot_research.experiments.validation.audit_blind_grower'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    started = time.perf_counter()
    cases = []
    for case in strict['cases']:
        path = case['result_path']
        if digest(path) != strict['input_sha256'][path]:
            raise ValueError('Result bytes changed since the strict audit.')
        verified = checked_row(path, inputs)
        row = json.loads(Path(path).read_text())
        condition = row['condition']
        entry, _, query = condition['candidate_spec'].partition('?')
        if entry != 'bot_research.bots.counters.forecast_grower:@make':
            raise ValueError('Expected the declared forecast-grower entry point.')
        params = {k: json.loads(v) for k, v in parse_qsl(query, keep_blank_values=True)}
        if params.get('defend_from', 6) <= 50:
            raise ValueError('The no-defense theorem does not apply to this first defense round.')
        blind_params = {k: params[k] for k in ('turret_round', 'growth_rounds', 'tier',
            'factory_cap', 'purchase_cap') if k in params}
        # ForecastGrower defaults to round2; FeatureBluff defaults to round1.
        blind_params.setdefault('turret_round', 2)
        blind = FeatureBluff(**blind_params)
        side = condition['candidate_side']
        replay = Path(row['replay_path'])
        inputs[str(replay)] = digest(replay)
        if inputs[str(replay)] != row['trajectory_sha256']:
            raise ValueError('Replay bytes changed since the recorded result.')
        records = [json.loads(line) for line in replay.read_text().splitlines()]
        if len(records) != 2 * (row['rounds'] + 1):
            raise ValueError('Incomplete replay.')
        engine = Engine(balanced_config(), tuple(row['bot_specs']))
        if records[:2] != normalized(engine.initial_records(tuple(row['bot_specs']))):
            raise ValueError('Nonstandard initial records.')
        for rnd in range(1, row['rounds'] + 1):
            pair = records[2 * rnd:2 * rnd + 2]
            actual = [[e['action'] for e in record['event'] if e['kind'] == 'action']
                      for record in pair]
            proposed = blind.decide(engine.observation(side))
            if proposed != actual[side]:
                raise ValueError(f'Blind action mismatch in round {rnd}.')
            if pair != normalized(engine.play_round(actual)):
                raise ValueError(f'Original-engine replay mismatch in round {rnd}.')
        if engine.result != row['result'] or [p.hp for p in engine.players] != row['hp']:
            raise ValueError('Final state mismatch.')
        cases.append({**verified, 'checked_rounds': row['rounds'],
                      'blind_parameters': blind_params, 'all_actions_equal': True})
    changed = [p for p, h in sources.items() if digest(p) != h]
    output = {'time_utc': now(), 'runtime_seconds': time.perf_counter() - started,
        'input_sha256': inputs, 'source_sha256': sources,
        'source_changed_during_run': changed, 'cases': cases,
        'checked_games': len(cases), 'checked_rounds': sum(c['checked_rounds'] for c in cases),
        'all_passed': not changed and all(c['all_actions_equal'] for c in cases),
        'scope': 'Recorded no-defense controls only. Per-round policy recomputation for the blind policy and original-engine replay. This is not a new opponent match or an independent strength sample.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('checked_games', 'checked_rounds', 'all_passed')}))
    if not output['all_passed']:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
