"""Check the finite search by isolated-copy exposure, then replay a funded deviation."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter
import argparse, hashlib, json, time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    source = Path(args.input)
    data = json.loads(source.read_text())
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    hashes = dict(data['input_sha256'])
    assert all(digest(p) == h for p, h in hashes.items())
    for p in static_closure({'bot_research.experiments.validation.check_round5_heavy_defense'}):
        if str(p) in hashes:
            assert digest(p) == hashes[str(p)]
        hashes[str(p)] = digest(p)
    hashes[str(source)] = digest(source)
    cfg = balanced_config()
    candidates = {}
    for row in data['proposals']:
        key = json.dumps(row['action'], sort_keys=True)
        assert key not in candidates
        candidates[key] = row
    expected = [None]
    for y in range(cfg.globals.height-1, -1, -1):
        for x in range(cfg.globals.width-1, -1, -1):
            expected.append(dict(op='build_wall', x=x, y=y))
            for typ in reversed(tuple(cfg.turrets)):
                expected.append(dict(op='build_turret', type=typ, x=x, y=y))
    assert len(expected) == len(candidates)
    accepted = 0
    qualifying = []
    max_exposure = {}
    for action in expected:
        row = candidates[json.dumps(action, sort_keys=True)]
        state = player_from_snapshot(data['fixture_snapshot'])
        state.gold = data['fixture_funding']
        state.hp = 800
        event = None if action is None else apply_action(state, action, 5, cfg)
        legal = event is None or event['accepted']
        assert legal == row['legal']
        if not legal:
            assert event['reason'] == row['reason']
            continue
        accepted += 1
        route = shortest_path(cfg.globals.width, cfg.globals.height,
            [(b.x, b.y) for b in state.buildings], cfg.globals.spawn, cfg.globals.base)
        assert route and len(route)-1 < cfg.globals.ticks_per_round
        splash = total = 0
        for building in state.buildings:
            if building.type == 'wall':
                continue
            turret = cfg.turrets[building.type]
            for x, y in route[:-1]:
                dx, dy = x-building.x, y-building.y
                if turret.aoe == 8:
                    if max(abs(dx), abs(dy)) == 1:
                        splash += turret.damage
                        total += turret.damage
                elif dx*dx + dy*dy <= turret.range*turret.range:
                    total += turret.damage
        cost = data['fixture_funding']-state.gold
        damage = 0 if total >= cfg.minions['tier4'].hp else cfg.minions['tier4'].damage
        assert row['splash_exposure'] == splash and row['cost'] == cost
        assert row['path_length'] == len(route)-1 and row['totals']['damage'] == damage
        good = splash >= cfg.minions['tier3'].hp and damage == 0
        assert row['qualifies'] == good
        kind = 'none' if action is None else action.get('type', 'wall')
        if splash >= cfg.minions['tier3'].hp:
            max_exposure[kind] = max(total, max_exposure.get(kind, -1))
        if good:
            qualifying.append((cost, json.dumps(action, sort_keys=True), row))
    winning = min(qualifying)[2]
    assert winning == data['winner']
    component = json.loads(Path('bot_research/runs/validation/early-heavy-opening-001.json').read_text())
    case = next(c for c in component['cases'] if c['strike_count'] == 1 and c['target_side'] == 0)
    engine = Engine(cfg, ('P5TNUBM', 'early_heavy'))
    for pair in case['records'][:4]:
        acts = [[e['action'] for e in r['event'] if e['kind'] == 'action'] for r in pair]
        assert normalized(engine.play_round(acts)) == normalized(pair)
    acts = [[e['action'] for e in r['event'] if e['kind'] == 'action'] for r in case['records'][4]]
    omitted = 0
    required = winning['cost']
    changed = []
    for action in acts[0]:
        if action['op'] == 'buy_factory' and omitted*cfg.globals.factory_cost < required:
            omitted += 1
        else:
            changed.append(action)
    assert omitted*cfg.globals.factory_cost >= required
    changed.append(winning['action'])
    before = engine.observation(0)
    counterfactual = engine.play_round([changed, acts[1]])
    assert all(e['accepted'] for r in counterfactual for e in r['event'] if e['kind'] == 'action')
    assert engine.players[0].hp == 800 and engine.players[1].hp == 755
    assert all(digest(p) == h for p, h in hashes.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        input_sha256=hashes, all_passed=True, proposed=len(expected), legal=accepted,
        minimum_cost=winning['cost'], witness=winning['action'],
        maximum_single_copy_exposure_with_retained_splash=max_exposure,
        counterfactual=dict(omitted_factories=omitted, pre_round_observation=before,
                            target_actions=changed, records=counterfactual),
        scope='Independent isolated-copy arithmetic on every legal addition and original-engine replay of one affordable round-five deviation; no full-game or mixed-roster guarantee.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k:output[k] for k in ('time_utc','runtime_seconds','all_passed','proposed','legal','minimum_cost','witness','maximum_single_copy_exposure_with_retained_splash')}))

if __name__ == '__main__':
    main()
