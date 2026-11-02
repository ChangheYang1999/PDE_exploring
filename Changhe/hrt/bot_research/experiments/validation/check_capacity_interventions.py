"""Validate recorded histories and test explicit one-round capacity interventions."""
from __future__ import annotations
import argparse
from copy import deepcopy
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.fixed_capacity import describe, lower_bound
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.source_closure import static_closure


def normalized(value):
    return json.loads(json.dumps(value))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text())
    probe_path = Path(manifest['source_probe'])
    probe = json.loads(probe_path.read_text())
    cfg = balanced_config()
    tier = manifest['tier']
    unit = cfg.minions[tier]
    assert tier == 'tier5' and unit.hp == 1500
    inputs = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (manifest_path, probe_path)}
    started = time.perf_counter()
    matches = []
    for match in probe['matches']:
        path = Path(match['log'])
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == probe['input_sha256'][str(path)]
        inputs[str(path)] = digest
        records = [json.loads(line) for line in raw.splitlines()]
        sides = [s for s in (0, 1) if manifest['candidate_needle'] in match['spec_a' if s == 0 else 'spec_b']]
        assert len(sides) == 1
        side = sides[0]
        eligible = []
        for offset in range(0, len(records)-2, 2):
            own, other = records[offset+side]['snapshot'], records[offset+1-side]['snapshot']
            acts = [e['action'] for e in records[offset+2+side]['event'] if e['kind'] == 'action']
            construction = [a for a in acts if a['op'] in ('build_wall', 'build_turret')]
            cost = sum(cfg.wall_cost if a['op'] == 'build_wall' else cfg.turrets[a['type']].cost for a in construction)
            budget = own['gold'] - cost
            buildings = own['buildings'] + [{'x': a['x'], 'y': a['y'],
                'type': 'wall' if a['op'] == 'build_wall' else a['type']} for a in construction]
            ours, theirs = describe(buildings, cfg.to_dict()), describe(other['buildings'], cfg.to_dict())
            if ours.splash >= unit.hp and theirs.splash < unit.hp and budget >= 61*unit.cost:
                eligible.append(offset//2 + 1)
        selected = sorted({eligible[0], eligible[-1]}) if eligible else []
        names = tuple(r['snapshot']['name'] for r in records[:2])
        engine = Engine(cfg, names)
        assert [r['snapshot'] for r in normalized(engine.initial_records(names))] == [r['snapshot'] for r in records[:2]]
        assert all(r['match']['rules'] == normalized(cfg.to_dict()) for r in records[:2])
        cases = []
        for rnd in range(1, len(records)//2):
            pair = records[2*rnd:2*rnd+2]
            assert all(not any(e['kind'] == 'bot_error' or e['kind'] == 'action' and not e['accepted'] for e in r['event']) for r in pair)
            submissions = [[e['action'] for e in r['event'] if e['kind'] == 'action'] for r in pair]
            if rnd in selected:
                construction = [a for a in submissions[side] if a['op'] in ('build_wall', 'build_turret')]
                spend = sum(cfg.wall_cost if a['op'] == 'build_wall' else cfg.turrets[a['type']].cost for a in construction)
                budget = engine.players[side].gold - spend
                mapping = describe([asdict(b) for b in engine.players[1-side].buildings], cfg.to_dict())
                existing = sum(e.active(rnd) for e in engine.players[side].roster)
                variants = {'cap60': 60, 'half_remaining_gold': budget//(2*unit.cost),
                            'all_remaining_gold': budget//unit.cost}
                tested = []
                for label, count in variants.items():
                    branch = deepcopy(engine)
                    actions = construction + [{'op': 'buy_minion', 'type': tier} for _ in range(count)]
                    attacker = deepcopy(engine.players[side])
                    for action in actions:
                        assert apply_action(attacker, action, rnd, cfg)['accepted']
                    fixed = simulate_map(attacker, deepcopy(engine.players[1-side]), engine.path(1-side), rnd, cfg)
                    alternative = deepcopy(submissions)
                    alternative[side] = actions
                    generated = branch.play_round(alternative)
                    assert all(e['accepted'] for r in generated for e in r['event'] if e['kind'] == 'action')
                    combat = next(e for e in generated[side]['event'] if e['kind'] == 'combat')
                    after = describe([asdict(b) for b in branch.players[1-side].buildings], cfg.to_dict())
                    tested.append({'label': label, 'count': count, 'cost': count*unit.cost,
                        'fixed_map_damage': fixed.damage, 'actual_damage': combat['damage_dealt'],
                        'hp_candidate_first': [branch.players[side].hp, branch.players[1-side].hp],
                        'result': branch.result, 'certificate': lower_bound(mapping, existing, count, unit.hp, unit.damage),
                        'defender_splash_after': after.splash, 'records': normalized(generated)})
                cases.append({'round': rnd, 'side': side, 'budget_after_construction': budget,
                              'defender_before': {'splash': mapping.splash, 'full': mapping.full, 'length': mapping.length},
                              'original_combat': next(e for e in pair[side]['event'] if e['kind'] == 'combat'),
                              'original_hp_candidate_first': [pair[side]['snapshot']['hp'], pair[1-side]['snapshot']['hp']],
                              'variants': tested})
            generated = normalized(engine.play_round(submissions))
            assert generated == pair, f'Original engine replay mismatch in {path.name}, round {rnd}.'
        matches.append({'log': str(path), 'side': side, 'eligible_rounds': eligible, 'selected_rounds': selected,
                        'source_rounds_replayed': engine.round, 'cases': cases})
        print(json.dumps({'log': str(path), 'eligible_rounds': eligible, 'selected_rounds': selected,
                          'cases': [{k: c[k] for k in ('round', 'budget_after_construction', 'defender_before')} for c in cases]}), flush=True)
    sources = set(static_closure({'bot_research.experiments.validation.check_capacity_interventions'}))
    sources.add(Path('td_game/balanced.json'))
    output = {'time_utc': now(), 'runtime_seconds': time.perf_counter()-started,
              'input_sha256': inputs, 'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
              'all_passed': True, 'matches': matches, 'scope': manifest['scope']}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('time_utc', 'runtime_seconds', 'all_passed')}))


if __name__ == '__main__':
    main()
