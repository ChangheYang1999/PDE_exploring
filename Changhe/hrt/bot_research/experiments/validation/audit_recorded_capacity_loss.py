"""Replay selected external records and apply the proved full-map capacity bound."""
from __future__ import annotations
import argparse
from copy import deepcopy
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def normal(value):
    return json.loads(json.dumps(value, allow_nan=False))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results', required=True)
    parser.add_argument('--candidate-substring', required=True)
    parser.add_argument('--opponent-substring', required=True)
    parser.add_argument('--round', type=int, required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    out = Path(args.output_dir)
    if out.is_absolute() or '..' in out.parts or out.parts[:3] != ('bot_research', 'runs', 'validation'):
        raise ValueError('Output must be a relative validation directory.')
    rows = [json.loads(s) for s in Path(args.results).read_text().splitlines()]
    selected = []
    for row in rows:
        side = row['candidate_side']
        specs = [row['spec_a'], row['spec_b']]
        if args.candidate_substring in specs[side] and args.opponent_substring in specs[1-side]:
            selected.append(row)
    if sorted(r['candidate_side'] for r in selected) != [0, 1]:
        raise ValueError('Select exactly one pair of exchanged assignments.')
    out.mkdir(parents=True, exist_ok=False)
    inputs = {args.results: digest(args.results)}
    atomic_json(out / 'selected_results.json', selected, exclusive=True)
    cfg = balanced_config()
    started = time.perf_counter()
    cases = []
    for row in selected:
        side = row['candidate_side']
        raw = Path(row['log']).read_bytes()
        inputs[row['log']] = hashlib.sha256(raw).hexdigest()
        archived = out / f'seat{side}.jsonl'
        archived.write_bytes(raw)
        records = [json.loads(s) for s in raw.splitlines()]
        assert len(records) == 2 * (row['rounds'] + 1)
        engine = Engine(cfg, (row['spec_a'], row['spec_b']))
        expected_initial = normal(engine.initial_records((row['spec_a'], row['spec_b'])))
        assert row['scenario'] is None
        for record in expected_initial:
            record['match'].update(research_scenario=row['scenario'],
                research_specs=[row['spec_a'], row['spec_b']], research_metadata=row['metadata'])
        assert records[:2] == expected_initial
        certificate = None
        for rnd in range(1, row['rounds'] + 1):
            pair = records[2*rnd:2*rnd+2]
            assert [r['player'] for r in pair] == [0, 1]
            assert all(r['round'] == rnd for r in pair)
            assert not any(e['kind'] == 'bot_error' for r in pair for e in r['event'])
            actions = [[e['action'] for e in r['event'] if e['kind'] == 'action'] for r in pair]
            if rnd == args.round:
                before = deepcopy(engine.players)
                players = deepcopy(before)
                for i in range(max(map(len, actions))):
                    for p in (0, 1):
                        if i < len(actions[p]):
                            assert apply_action(players[p], actions[p][i], rnd, cfg)['accepted']
                defender, attacker = players[side], players[1-side]
                g = cfg.globals
                blocked = {(b.x, b.y) for b in before[side].buildings}
                route = shortest_path(g.width, g.height, blocked, g.spawn, g.base)
                assert route is not None
                full = len(blocked) + len(route) == g.width * g.height
                same = defender.buildings == before[side].buildings
                splash, gun = 0, 0
                for b in defender.buildings:
                    if b.type == 'wall':
                        continue
                    turret = cfg.turrets[b.type]
                    if turret.aoe == 8:
                        splash += turret.damage * sum(max(abs(x-b.x), abs(y-b.y)) == 1 for x, y in route[:-1])
                    else:
                        gun += turret.damage
                active = [e for e in attacker.roster if e.active(rnd)]
                length = len(route)-1
                hp = cfg.minions['tier5'].hp
                eligible = [asdict(e) | {'active_index': k, 'spawn_tick': k % g.ticks_per_round}
                    for k, e in enumerate(active) if e.type == 'tier5' and k % g.ticks_per_round <= g.ticks_per_round-1-length]
                assert full and same and hp > splash
                killed_bound = g.ticks_per_round * gun // (hp-splash)
                arrivals = max(0, len(eligible)-killed_bound)
                certificate = {'round': rnd, 'full_map_at_start': full, 'buildings_unchanged_by_actions': same,
                    'route_steps': length, 'splash_exposure': splash, 'gun_damage_per_tick': gun,
                    'tier5_hp': hp, 'active_entries': len(active), 'eligible_tier5': len(eligible),
                    'selected_death_upper_bound': killed_bound, 'arrival_lower_bound': arrivals,
                    'base_damage_lower_bound': arrivals*cfg.minions['tier5'].damage,
                    'base_hp_before_round': before[side].hp,
                    'own_base_destruction_certified': arrivals*cfg.minions['tier5'].damage >= before[side].hp,
                    'defender_map': [asdict(b) for b in before[side].buildings],
                    'active_attacker_roster': [asdict(e) for e in active], 'route': route}
            generated = normal(engine.play_round(actions))
            assert pair == generated, f'Replay mismatch in round {rnd}'
            assert all(e['accepted'] for r in generated for e in r['event'] if e['kind'] == 'action')
            if rnd == args.round:
                combat = next(e for e in generated[side]['event'] if e['kind'] == 'combat')
                certificate['actual_base_damage'] = combat['base_damage']
                certificate['actual_incoming_hits'] = combat['incoming_hits']
                assert combat['base_damage'] >= certificate['base_damage_lower_bound']
                assert certificate['own_base_destruction_certified']
        assert certificate is not None
        assert engine.result == {'winner': row['winner'], 'reason': row['reason']}
        assert [p.hp for p in engine.players] == [row['hp_a'], row['hp_b']]
        cases.append({'candidate_side': side, 'replay': str(archived), 'replay_sha256': digest(archived),
            'replayed_rounds': row['rounds'], 'result': engine.result,
            'hp_candidate_first': [engine.players[side].hp, engine.players[1-side].hp],
            'certificate': certificate})
    paths = set(static_closure({'bot_research.experiments.validation.audit_recorded_capacity_loss'}))
    paths.update((Path('td_game/balanced.json'), Path('bot_research/experiments/validation/analysis/full_map_capacity/PROOF.md')))
    output = {'time_utc': now(), 'runtime_seconds': time.perf_counter()-started, 'all_passed': True,
        'input_sha256': inputs, 'source_sha256': {str(p): digest(p) for p in paths}, 'cases': cases,
        'scope': 'Exact action replay and full-map damage certificate for the selected recorded round. This does not independently re-execute bot decisions or rule out simultaneous opponent destruction under other legal attacks.'}
    atomic_json(out/'audit.json', output, exclusive=True)
    print(json.dumps({'all_passed': True, 'pairs': len(cases), 'runtime_seconds': output['runtime_seconds'],
        'certificates': [{k:v for k,v in c['certificate'].items() if k not in ('route', 'defender_map', 'active_attacker_roster')} for c in cases]}))


if __name__ == '__main__':
    main()
