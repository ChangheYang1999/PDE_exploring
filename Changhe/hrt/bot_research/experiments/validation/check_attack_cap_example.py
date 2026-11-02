"""Reproduce the economy lane's sub-immunity fortress example on original combat."""
from collections import Counter
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import time

from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.state import PlayerState, RosterEntry
from bot_research.bots.counters.fixed_capacity import describe, lower_bound, minimum_count
from bot_research.bots.economy.frozen.v24 import fastsim, offense
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def normalized(value):
    return json.loads(json.dumps(value, allow_nan=False))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    table = Path('bot_research/runs/economy/w1v29c/results.jsonl')
    rows = [json.loads(line) for line in table.read_text().splitlines()]
    matches = [row for row in rows if row['scenario'] == 'asym:24:3'
               and row['candidate_side'] == 0
               and row['spec_b'] == 'bot_research.bots.defense.frozen.v28.fortress:@make']
    assert len(matches) == 1
    row = matches[0]
    replay = Path(row['log'])
    inputs = set(static_closure({'bot_research.experiments.validation.check_attack_cap_example'}))
    inputs |= {table, replay, Path('td_game/balanced.json'), Path('configs/balanced.json'),
               Path('bot_research/experiments/validation/analysis/fixed_gun_support/PROOF.md')}
    digest = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
    hashes = {str(path): digest(path) for path in inputs}
    records = [json.loads(line) for line in replay.read_text().splitlines()]
    config = balanced_config()
    rules = config.to_dict()
    specs = (row['spec_a'], row['spec_b'])
    engine = Engine(config, specs)
    initial = normalized(engine.initial_records(specs))
    for record in initial:
        record['match'].update(research_scenario=row['scenario'],
                               research_specs=list(specs), research_metadata=row['metadata'])
    assert initial == records[:2]
    assert len(records) == 2 * (row['rounds'] + 1)
    snapshots = {}
    for rnd in range(1, row['rounds'] + 1):
        pair = records[2*rnd:2*rnd+2]
        assert not any(event['kind'] == 'bot_error' for record in pair for event in record['event'])
        actions = [[event['action'] for event in record['event'] if event['kind'] == 'action']
                   for record in pair]
        generated = normalized(engine.play_round(actions))
        assert generated == pair, f'Replay differs in round {rnd}'
        assert all(event['accepted'] for record in pair for event in record['event']
                   if event['kind'] == 'action')
        if rnd in (20, 24, 35):
            snapshots[rnd] = (deepcopy(engine.players), engine.path(1), engine.snapshot(1))
    assert engine.result == dict(winner=row['winner'], reason=row['reason'])
    assert [p.hp for p in engine.players] == [row['hp_a'], row['hp_b']]
    assert not row['source_changed'] and not row['error']
    checks = []
    for rnd in (20, 24):
        players, path, snapshot = snapshots[rnd]
        buildings = snapshot['buildings']
        mapping = describe(buildings, rules)
        gun_damage = sum(config.turrets[b.type].damage for b in players[1].buildings
                         if b.type != 'wall' and config.turrets[b.type].aoe != 8)
        counts = Counter(b.type for b in players[1].buildings)
        if rnd == 20:
            assert mapping.length == 42 and mapping.splash == 960 and gun_damage == 1482
            assert counts['splash'] == 27 and counts['gun3'] == 26 and counts['gun2'] == 2 and counts['gun1'] == 1
        unit = config.minions['tier5']
        assert unit.hp > mapping.splash
        model = fastsim.MapModel([(b['x'], b['y'], b['type']) for b in buildings], rules)
        combats = []
        for count in (500, 750, 1000, 3000):
            attacker = PlayerState('component attacker', 800, 0,
                roster=[RosterEntry(k, 'tier5', 1, None) for k in range(count)])
            target = deepcopy(players[1])
            result = simulate_map(attacker, target, path, rnd + 1, config)
            fast = fastsim.simulate(model, ['tier5'] * count, rules)
            assert tuple(fast[:2]) == (result.hits, result.damage)
            eligible = sum(k % config.globals.ticks_per_round + mapping.length < config.globals.ticks_per_round
                           for k in range(count))
            coarse = max(0, eligible - config.globals.ticks_per_round * gun_damage // (unit.hp - mapping.splash))
            support = lower_bound(mapping, 0, count, unit.hp, unit.damage)
            assert result.hits >= support['arrival_lower_bound'] >= coarse
            if rnd == 20:
                assert result.hits == {500: 0, 750: 201, 1000: 409, 3000: 2074}[count]
            combats.append(dict(count=count, original=asdict(result), coarse_arrival_lower_bound=coarse,
                                exact_support_certificate=support, price=count * unit.cost,
                                affordable_from_recorded_end_round_gold=count * unit.cost <= players[0].gold))
        checks.append(dict(recorded_end_round=rnd, map=snapshot, path=path,
                           per_tick_gun_damage=gun_damage, splash_exposure=mapping.splash,
                           full_map=mapping.full, attacker_gold=players[0].gold,
                           minimum_supported_lethal=minimum_count(mapping, 0, unit.hp, unit.damage, players[1].hp),
                           combats=combats))
    # This is a deliberately supplied 500,000 budget, not a claim about round 24 cash.
    players, path, snapshot = snapshots[24]
    search_started = time.perf_counter()
    result = offense.search([(b['x'], b['y'], b['type']) for b in snapshot['buildings']], [], 500000,
                            rules, cap=3000, active_cap=4000)
    search_seconds = time.perf_counter() - search_started
    assert all(digest(path) == value for path, value in hashes.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(),
                  runtime_seconds=time.perf_counter()-started, all_passed=True,
                  input_sha256=hashes, replay_rounds=row['rounds'], original_result=engine.result,
                  checks=checks, search_with_supplied_budget=dict(packages=[dict(types=dict(Counter(p)), cost=c, marginal_damage=md, response_damage=rd) for p,c,md,rd in result[0]], base_damage=result[1], runtime_seconds=search_seconds),
                  attacker_end_round_35_gold=snapshots[35][0][0].gold,
                  scope='Replay of one recorded game and synthetic homogeneous attacks on its fixed end-round maps. This independently checks combat and the gun-capacity bound, not a fresh bot match, affordability of every synthetic roster, or immunity to a changed defender map.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(time_utc=output['time_utc'], runtime_seconds=output['runtime_seconds'],
                          all_passed=True, rounds=row['rounds'],
                          hits=[[c['original']['hits'] for c in r['combats']] for r in checks],
                          search_seconds=search_seconds)))


if __name__ == '__main__':
    main()
