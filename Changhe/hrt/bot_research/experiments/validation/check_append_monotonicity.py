"""Check fixed-map append dominance using only original combat operations."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time

from td_game.actions import apply_action
from td_game.combat import combat_tick, simulate_map, spawn_schedule
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.bots.counters.lethal_threshold import minimum_lethal_count
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def player(types, inactive=0):
    roster = [RosterEntry(i, 'tier2', 1, 6) for i in range(inactive)]
    roster.extend(RosterEntry(i+inactive, kind, 1, None) for i, kind in enumerate(types))
    return PlayerState('attacker', 800, 0, roster=roster)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    declaration = json.loads(Path(args.manifest).read_text())
    inputs = {args.manifest: digest(args.manifest), **declaration['input_sha256']}
    assert all(digest(p) == h for p, h in inputs.items()), 'Declared input changed.'
    sources = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.check_append_monotonicity'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cfg = balanced_config()
    ticks, rnd = cfg.globals.ticks_per_round, declaration['round_number']
    maps = {}
    for fixture in declaration['maps']:
        state = PlayerState('defender', 800, 10**9)
        if 'source' in fixture:
            src = fixture['source']
            row = json.loads(Path(src['result_path']).read_text())
            assert digest(row['replay_path']) == row['trajectory_sha256']
            records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
            assert records[2*src['round']+src['side']]['snapshot']['buildings'] == fixture['buildings']
        for b in fixture['buildings']:
            action = dict(op='build_wall' if b['type'] == 'wall' else 'build_turret', x=b['x'], y=b['y'])
            if b['type'] != 'wall':
                action['type'] = b['type']
            assert apply_action(state, action, rnd, cfg)['accepted'], 'Illegal fixture construction.'
        path = shortest_path(cfg.globals.width, cfg.globals.height,
                             {(b.x,b.y) for b in state.buildings}, cfg.globals.spawn, cfg.globals.base)
        assert path is not None
        maps[fixture['id']] = state, path
    cases = []
    for fixture in declaration['cases']:
        defender, path = maps[fixture['map_id']]
        a = player(fixture['base_types'], inactive=fixture['inactive_count'])
        b = player(fixture['base_types']+fixture['appended_types'], inactive=fixture['inactive_count'])
        schedule_a, schedule_b = (spawn_schedule(p.roster, rnd, ticks) for p in (a,b))
        born_a = {e.id:t for t, entries in enumerate(schedule_a) for e in entries}
        born_b = {e.id:t for t, entries in enumerate(schedule_b) for e in entries}
        assert all(born_b[i] == t for i,t in born_a.items()), 'Old spawn index changed.'
        da, db = deepcopy(defender), deepcopy(defender)
        ea, eb = [], []
        total_a = total_b = 0
        strict_hp_ticks = 0
        strict_damage_ticks = 0
        for tick in range(ticks):
            ea, ta = combat_tick(tick, ea, schedule_a[tick], path, da, cfg)
            eb, tb = combat_tick(tick, eb, schedule_b[tick], path, db, cfg)
            by_id = {e.roster_id:e for e in eb}
            assert all(e.roster_id in by_id for e in ea), 'Old live identity missing.'
            assert all(by_id[e.roster_id].path_index == e.path_index for e in ea), 'Old position changed.'
            assert all(by_id[e.roster_id].hp >= e.hp for e in ea), 'Old HP decreased under extension.'
            old_ids = {e.roster_id for e in ea}
            assert [e.roster_id for e in eb if e.roster_id in old_ids] == [e.roster_id for e in ea]
            total_a += ta.damage
            total_b += tb.damage
            assert tb.damage >= ta.damage, 'Same-tick base damage decreased.'
            strict_hp_ticks += any(by_id[e.roster_id].hp > e.hp for e in ea)
            strict_damage_ticks += tb.damage > ta.damage
        direct_a = simulate_map(deepcopy(a), deepcopy(defender), path, rnd, cfg).damage
        direct_b = simulate_map(deepcopy(b), deepcopy(defender), path, rnd, cfg).damage
        assert direct_a == total_a == defender.hp-da.hp
        assert direct_b == total_b == defender.hp-db.hp
        cases.append(dict(id=fixture['id'], map_id=fixture['map_id'], base_count=len(fixture['base_types']),
            appended_count=len(fixture['appended_types']), inactive_count=fixture['inactive_count'],
            old_birth_ticks_preserved=True, checked_ticks=ticks, all_tick_invariants_pass=True,
            old_damage=total_a, extended_damage=total_b, strict_hp_ticks=strict_hp_ticks,
            strict_damage_ticks=strict_damage_ticks))
        print(json.dumps(cases[-1]), flush=True)
    thresholds = []
    for map_id in declaration['threshold_maps']:
        defender,path = maps[map_id]
        values = {n: simulate_map(player(['tier5']*n), deepcopy(defender), path, rnd, cfg).damage
                  for n in range(1, declaration['threshold_max_count']+1)}
        assert all(values[n] <= values[n+1] for n in range(1, len(values)))
        for hp in declaration['threshold_hp']:
            for limit in declaration['threshold_bounds']:
                seen = []
                def damage(n):
                    assert 1 <= n <= limit
                    seen.append(n)
                    return values[n]
                actual = minimum_lethal_count(damage, hp, limit)
                expected = next((n for n in range(1,limit+1) if values[n] >= hp), None)
                assert actual == expected, 'Threshold differs from exhaustive original combat.'
                thresholds.append(dict(map_id=map_id, hp=hp, n_max=limit, returned=actual,
                    exact_minimum=expected, tested_counts=seen))
    assert all(digest(p) == h for p,h in {**inputs,**sources}.items()), 'Input or source changed during check.'
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        all_passed=True, input_sha256=inputs, source_sha256=sources, cases=cases,
        threshold_cases=thresholds, total_tick_checks=sum(c['checked_ticks'] for c in cases),
        scope='Fixed maps and declared appended rosters only. Original combat_tick checks the live-identity/HP invariant at every tick, and original simulate_map confirms total damage. Finite tests supplement the separate informal proof. The threshold helper agrees with exhaustive original combat on its declared finite domains. No full-game strength or construction monotonicity is claimed.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(all_passed=True,cases=len(cases),threshold_cases=len(thresholds),runtime_seconds=output['runtime_seconds'])),flush=True)


if __name__ == '__main__':
    main()
