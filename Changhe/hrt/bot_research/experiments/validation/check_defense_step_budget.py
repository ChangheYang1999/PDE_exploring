"""Check a larger construction budget on one recorded lethal position."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.free_forecast import FreeForecast
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.defense_plan import saturate
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_adaptive_attacks import combat
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    manifest = json.loads(Path(args.manifest).read_text())
    inputs = {args.manifest: digest(args.manifest), **manifest['input_sha256']}
    assert all(digest(p) == h for p, h in inputs.items())
    path = manifest['result_path']
    row = json.loads(Path(path).read_text())
    assert digest(row['replay_path']) == row['trajectory_sha256']
    records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
    rnd, side = row['rounds'], row['condition']['candidate_side']
    assert rnd == 41 and side == 0
    before = [records[2*(rnd-1)+i]['snapshot'] for i in (0, 1)]
    observation = dict(round=rnd, player=side, rules=row['rules'], players=deepcopy(before))
    saved = deepcopy(observation)
    chosen = [[e['action'] for e in records[2*rnd+i]['event'] if e['kind'] == 'action'] for i in (0, 1)]
    config = config_from_dict(row['rules'])
    enemy = player_from_snapshot(before[1-side])
    for action in chosen[1-side]:
        assert apply_action(enemy, action, rnd, config)['accepted']
    assert row['forecast_trace'][-1]['predicted_actions'] == chosen[1-side]
    threat = [e.type for e in enemy.roster if e.active(rnd)]
    me = before[side]
    assert me['hp'] == 790 and me['gold'] == 639450
    buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
    sources = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.check_defense_step_budget'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for steps in manifest['step_budgets']:
        begin = time.perf_counter()
        policy = FreeForecast(free_steps=steps)
        actions, built, gold, residual, detail = policy.defense(observation, buildings, me['gold'], threat)
        extra, built, gold, _ = saturate(built, gold, 1500, row['rules'])
        construction = actions+extra
        defender = player_from_snapshot(me)
        for action in construction:
            assert apply_action(defender, action, rnd, config)['accepted']
        damage = combat(enemy, defender, rnd, config)
        if steps == 15:
            recorded_construction = [a for a in chosen[side] if a['op'] not in ('buy_factory', 'buy_minion')]
            assert construction == recorded_construction, 'Default construction differs from actual game.'
            assert residual == 1120 and damage == 1120
        assert observation == saved, 'Proposal generation changed its input.'
        result = dict(steps=steps, actions=construction, construction_count=len(construction),
                      cost=me['gold']-defender.gold, remaining_gold=defender.gold,
                      original_combat_damage=damage, hp_after=me['hp']-damage,
                      survives=damage < me['hp'], planner_residual_before_saturation=residual,
                      alternatives=detail, runtime_seconds=time.perf_counter()-begin)
        cases.append(result)
        print(json.dumps({k:v for k,v in result.items() if k not in ('actions','alternatives')}), flush=True)
    assert all(digest(p) == h for p, h in {**inputs, **sources}.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
                  input_sha256=inputs, source_sha256=sources, all_checks_passed=True, cases=cases,
                  scope='One recorded round with fixed actual opponent actions. A surviving construction proves current-round feasibility only; full-game improvement remains untested.')
    atomic_json(args.output, output, exclusive=True)


if __name__ == '__main__':
    main()
