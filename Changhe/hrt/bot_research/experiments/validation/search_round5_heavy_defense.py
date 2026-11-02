"""Enumerate one-building responses on a recorded original-engine fixture."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
import argparse, hashlib, json, time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    args = p.parse_args()
    started = time.perf_counter()
    source = Path('bot_research/runs/validation/early-heavy-opening-001.json')
    proof = Path('bot_research/experiments/validation/analysis/round5_heavy_defense/PROOF.md')
    paths = set(static_closure({'bot_research.experiments.validation.search_round5_heavy_defense'})) | {source, proof, Path('configs/balanced.json'), Path('td_game/balanced.json')}
    digest = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
    hashes = {str(path): digest(path) for path in sorted(paths)}
    original = json.loads(source.read_text())
    case = next(c for c in original['cases'] if c['strike_count'] == 1 and c['target_side'] == 0)
    snapshot = case['records'][-1][0]['snapshot']
    cfg = balanced_config()
    base = player_from_snapshot(snapshot)
    base.gold = 10000
    base.hp = 800
    attacker = PlayerState('single tier4', 800, 0)
    attacker.roster = [RosterEntry(0, 'tier4', 5, 16)]
    actions = [None]
    for kind in ('wall', *cfg.turrets.keys()):
        for x in range(cfg.globals.width):
            for y in range(cfg.globals.height):
                action = dict(op='build_wall' if kind == 'wall' else 'build_turret', x=x, y=y)
                if kind != 'wall':
                    action['type'] = kind
                actions.append(action)
    rows = []
    for action in actions:
        state = deepcopy(base)
        event = None if action is None else apply_action(state, action, 5, cfg)
        if event is not None and not event['accepted']:
            rows.append(dict(action=action, legal=False, reason=event['reason']))
            continue
        path = shortest_path(cfg.globals.width, cfg.globals.height,
            [(b.x, b.y) for b in state.buildings], cfg.globals.spawn, cfg.globals.base)
        assert path
        splash = sum(cfg.turrets[b.type].damage for b in state.buildings if b.type == 'splash'
            for x, y in path[:-1] if max(abs(x-b.x), abs(y-b.y)) == 1)
        totals = asdict(simulate_map(attacker, state, path, 5, cfg))
        rows.append(dict(action=action, legal=True, cost=base.gold-state.gold,
                         splash_exposure=splash, path_length=len(path)-1,
                         totals=totals, qualifies=totals['damage'] == 0 and splash >= cfg.minions['tier3'].hp))
    valid = [r for r in rows if r.get('qualifies')]
    winner = min(valid, key=lambda r: (r['cost'], json.dumps(r['action'], sort_keys=True))) if valid else None
    assert all(digest(path) == sha for path, sha in hashes.items())
    out = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        input_sha256=hashes, source_case=dict(strike_count=1, target_side=0),
        fixture_snapshot=snapshot, fixture_funding=10000, round=5,
        threat=['tier4'], proposals=rows, winner=winner,
        scope='Funded single-building geometric minimum with retained tier3 splash immunity; no mixed-roster or full-game claim.')
    atomic_json(args.output, out, exclusive=True)
    print(json.dumps(dict(time_utc=out['time_utc'], runtime_seconds=out['runtime_seconds'], proposed=len(rows), legal=sum(r['legal'] for r in rows), winner=winner)))

if __name__ == '__main__':
    main()
