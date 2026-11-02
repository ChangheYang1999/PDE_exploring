"""Generate a small fixed construction library, verifying original combat fixtures."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import time

from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.bots.economy.frozen.v17.freeplan import free_plan
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    root = Path('bot_research/bots/counters/data')
    ladder_path = root / 'guard_ladder_001.json'
    screen_path = root / 'screened_guard_001.json'
    files = set(static_closure({'bot_research.experiments.validation.design_early_guard_extension'}))
    files.update([ladder_path, screen_path, Path('td_game/balanced.json'), Path('configs/balanced.json')])
    hashes = {str(p): digest(p) for p in files}
    ladder = json.loads(ladder_path.read_text())
    screen = json.loads(screen_path.read_text())
    cfg = balanced_config()
    base = PlayerState('funded guard fixture', 800, 10000)
    original = [dict(op='build_turret', type='splash', x=x, y=y)
                for x, y in ladder['guards'][:2]]
    assert all(apply_action(base, a, 6, cfg)['accepted'] for a in original)
    obs = Engine(cfg, ('fixture', 'fixture')).observation(0)
    obs['round'] = 6
    obs['players'][0]['buildings'] = [asdict(b) for b in base.buildings]
    obs['players'][0]['gold'] = 10000
    threats = {'t3x3': ['tier1']*3+['tier3']*3,
               't3x6': ['tier1']*3+['tier3']*6,
               't4x1': ['tier1']*3+['tier4'],
               't3swarm': ['tier3']*100}
    choices = [('none', []), ('screened', screen['witnesses'][0]['extra_actions'])]
    for name in ('t3x3', 't3x6', 't4x1'):
        saved = deepcopy(obs)
        extension = free_plan(deepcopy(obs), 600, [threats[name]], partial='none', max_steps=15)
        assert obs == saved
        choices.append(('free_' + name, extension))
    choices.append(('splash200', [dict(op='build_turret', type='splash', x=x, y=y)
                                  for x, y in ladder['guards'][2:]]))
    rows = []
    for name, extension in choices:
        state = deepcopy(base)
        assert all(apply_action(state, a, 6, cfg)['accepted'] for a in extension)
        path = shortest_path(12, 12, ((b.x, b.y) for b in state.buildings), (0, 0), (11, 11))
        assert path
        splash = cfg.turrets['splash'].damage * sum(
            b.type == 'splash' and max(abs(x-b.x), abs(y-b.y)) == 1
            for x, y in path[:-1] for b in state.buildings)
        outcomes = {}
        for target, types in threats.items():
            attacker = PlayerState('component attacker', 800, 0)
            attacker.roster = [RosterEntry(i, t, 6, 17) for i, t in enumerate(types)]
            outcomes[target] = asdict(simulate_map(attacker, deepcopy(state), path, 6, cfg))
        rows.append(dict(id=name, actions=extension, extra_cost=base.gold-state.gold,
                         path=path, splash_exposure=splash, outcomes=outcomes))
    assert all(digest(p) == h for p, h in hashes.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(),
        runtime_seconds=time.perf_counter()-start, input_sha256=hashes,
        original_constructions=original, funded_initial_gold=10000, fixture_round=6,
        threats=threats, plans=rows,
        scope='Fixed-map funded components; original legality and combat checked. '
              'Free-plan outputs are heuristic choices under a 600-gold budget, not cost minima. '
              'Full-game affordability and strength are separate tests.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps([dict(id=r['id'], cost=r['extra_cost'], splash=r['splash_exposure'],
                         damage={k:v['base_damage'] for k,v in r['outcomes'].items()})
                      for r in rows]))


if __name__ == '__main__':
    main()
