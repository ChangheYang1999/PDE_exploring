"""Cross-check the proved isolated-copy threshold on legally constructed maps."""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry
from bot_research.bots.counters.exposure_guard import ExposureGuard, single_copy_exposure
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    fixtures = [('empty', [])]
    for kind in ('gun1', 'gun2', 'gun3', 'splash'):
        for label, x, y in (('near', 3, 1), ('far', 0, 11)):
            fixtures.append((kind + '_' + label,
                [{'op': 'build_turret', 'type': kind, 'x': x, 'y': y}]))
    fixtures.append(('mixed', [
        {'op': 'build_turret', 'type': kind, 'x': x, 'y': y}
        for kind, x, y in [('gun1', 3, 1), ('gun2', 5, 1), ('gun3', 7, 1), ('splash', 9, 1)]]))
    fixtures.append(('bend', [
        {'op': 'build_wall', 'x': x, 'y': 0} for x in range(2, 10)] + [
        {'op': 'build_turret', 'type': 'gun2', 'x': 5, 'y': 2},
        {'op': 'build_turret', 'type': 'splash', 'x': 8, 'y': 2}]))
    cfg = balanced_config()
    checks, cases = {}, []
    for label, actions in fixtures:
        engine = Engine(cfg, ('exposure_fixture', 'idle'))
        for _ in range(5):
            obs = engine.observation(0)
            gold = obs['players'][0]['gold']
            records = engine.play_round([[{'op': 'buy_factory'}] * (gold // cfg.globals.factory_cost), []])
            assert all(e['accepted'] for r in records for e in r['event'] if e['kind'] == 'action')
        records = engine.play_round([actions, []])
        checks[label + '_legal'] = all(e['accepted'] for r in records for e in r['event'] if e['kind'] == 'action')
        obs = engine.observation(0)
        buildings = obs['players'][0]['buildings']
        route = shortest_path(cfg.globals.width, cfg.globals.height,
            {(b['x'], b['y']) for b in buildings}, cfg.globals.spawn, cfg.globals.base)
        assert route is not None
        exposure = single_copy_exposure(buildings, obs['rules'])
        for kind, minion in cfg.minions.items():
            attacker = PlayerState('A', 800, 0, roster=[RosterEntry(0, kind, 1, None)])
            defender = PlayerState('D', 1000000, 0,
                buildings=[Building(b['x'], b['y'], b['type']) for b in buildings])
            totals = simulate_map(attacker, defender, route, 1, cfg)
            expected = int(minion.hp > exposure)
            passed = (totals.hits == expected and totals.damage == expected * minion.damage
                      and totals.killed == 1 - expected and totals.spawned == 1 and totals.cleared == 0)
            checks[label + '_' + kind] = passed
            cases.append({'map': label, 'buildings': buildings, 'route_steps': len(route) - 1,
                'minion': kind, 'hp': minion.hp, 'exposure': exposure,
                'expected_hits': expected, 'actual_hits': totals.hits, 'passed': passed})
    engine = Engine(cfg, ('guard', 'idle'))
    obs = engine.observation(0)
    before = deepcopy(obs)
    actions = ExposureGuard().decide(obs)
    checks['policy_preserves_observation'] = obs == before
    records = engine.play_round([actions, []])
    checks['policy_opening_legal'] = all(e['accepted'] for r in records for e in r['event'] if e['kind'] == 'action')
    paths = set(static_closure({'bot_research.experiments.validation.check_single_copy_exposure'}))
    paths.add(Path('td_game/balanced.json'))
    output = {'time_utc': now(), 'checks': checks, 'all_passed': all(checks.values()), 'cases': cases,
        'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        'proof': 'bot_research/experiments/validation/analysis/single_copy_exposure/PROOF.md',
        'scope': 'Component checks on fixed legal maps with one active entry. No multi-copy defense or policy-strength guarantee.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'all_passed': output['all_passed'], 'checks': len(checks), 'single_copy_cases': len(cases)}))
    if not output['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
