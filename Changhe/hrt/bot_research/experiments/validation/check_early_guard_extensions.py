"""Check the complete JSON components and live round6 insertion independently."""
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
from bot_research.bots.counters.early_guard_handoff import DATA, DATA_SHA256, EarlyGuardHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    assert digest(DATA) == DATA_SHA256
    data = json.loads(DATA.read_text())
    hashes = dict(data['input_sha256'])
    hashes[str(DATA.relative_to(Path.cwd()))] = DATA_SHA256
    for path in static_closure({'bot_research.experiments.validation.check_early_guard_extensions'}):
        if str(path) in hashes:
            assert hashes[str(path)] == digest(path)
        hashes[str(path)] = digest(path)
    cfg = balanced_config()
    fixtures, histories = [], []
    for plan in data['plans']:
        state = PlayerState('funded guard fixture', 800, data['funded_initial_gold'])
        assert all(apply_action(state, a, 6, cfg)['accepted'] for a in data['original_constructions'])
        gold = state.gold
        assert all(apply_action(state, a, 6, cfg)['accepted'] for a in plan['actions'])
        assert gold-state.gold == plan['extra_cost']
        path = shortest_path(12, 12, ((b.x, b.y) for b in state.buildings), (0, 0), (11, 11))
        assert path and [list(c) for c in path] == plan['path']
        exposure = 10*sum(b.type == 'splash' and max(abs(x-b.x), abs(y-b.y)) == 1
                          for x, y in path[:-1] for b in state.buildings)
        assert exposure == plan['splash_exposure']
        for name, types in data['threats'].items():
            attacker = PlayerState('component attacker', 800, 0)
            attacker.roster = [RosterEntry(i, t, 6, 17) for i, t in enumerate(types)]
            actual = asdict(simulate_map(attacker, deepcopy(state), path, 6, cfg))
            assert actual == plan['outcomes'][name]
            fixtures.append(dict(plan=plan['id'], roster=name, **actual))
        for side in (0, 1):
            bot = EarlyGuardHandoff(extension=plan['id'], layout='empty', growth_rounds=6,
                                   bait=[], tier='tier5', factory_cap=2000, purchase_cap=1000)
            engine = Engine(cfg, ('component', 'idle'))
            for rnd in range(1, 7):
                obs = engine.observation(side)
                saved = deepcopy(obs)
                actions = bot.decide(obs)
                assert saved == obs
                private = player_from_snapshot(obs['players'][side])
                assert all(apply_action(private, a, rnd, cfg)['accepted'] for a in actions)
                submitted = [[], []]
                submitted[side] = actions
                engine.play_round(submitted)
            assert bot.trace[-1]['extension_complete']
            assert not any(r['stage'] == 'extension' for r in bot.filtered_proposals)
            histories.append(dict(extension=plan['id'], side=side, rounds=6,
                extension_complete=True, filtered_economic_proposals=len(bot.filtered_proposals)))
    assert len(fixtures) == 24 and len(histories) == 12
    assert all(digest(p) == h for p, h in hashes.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
        all_passed=True, input_sha256=hashes, components=fixtures, opening_histories=histories,
        generator_note='Generator completed and atomically published its JSON before a final display-only '
                       'KeyError (base_damage instead of damage). Its unchanged source hash is retained; '
                       'this independent checker verifies every published component and cost.',
        scope='Funded component equality and six-round legal opening insertions against idle. '
              'No full-game result or general affordability guarantee.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc', 'runtime_seconds', 'all_passed')}))


if __name__ == '__main__':
    main()
