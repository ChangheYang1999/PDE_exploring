"""Original-engine checks of guarded opening alternatives; the third tier1 leaks."""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.guard_roster import GuardRoster
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure

ROSTERS = ((), ('tier1',), ('tier1', 'tier1'), ('tier2',), ('tier1', 'tier1', 'tier2'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    config = balanced_config()
    enemy_rosters = []

    def visit(roster, gold):
        enemy_rosters.append(roster)
        for tier, spec in config.minions.items():
            if spec.cost <= gold:
                visit(roster + [tier], gold - spec.cost)

    visit([], 100)
    assert len(enemy_rosters) == 27
    cases = []
    for roster in ROSTERS:
        for side in (0, 1):
            outcomes = []
            for enemy in enemy_rosters:
                engine = Engine(config, ('check0', 'check1'))
                observation = engine.observation(side)
                before = deepcopy(observation)
                opening = GuardRoster(roster).decide(observation)
                assert observation == before
                pair = [None, None]
                pair[side] = opening
                pair[1-side] = [{'op': 'buy_minion', 'type': tier} for tier in enemy]
                records = engine.play_round(pair)
                assert all(e['accepted'] for r in records for e in r['event'] if e['kind'] == 'action')
                own = engine.players[side]
                opposing = engine.players[1-side]
                outcomes.append(dict(enemy_roster=enemy, own_damage=800-own.hp,
                    enemy_damage=800-opposing.hp, factories=own.n_factories,
                    own_gold=own.gold, own_actions=opening))
                if enemy == ['tier1'] * 3:
                    assert own.hp == 795
            cases.append(dict(roster=roster, side=side, outcomes=outcomes))
    for i in range(0, len(cases), 2):
        assert cases[i]['outcomes'] == cases[i+1]['outcomes']
    paths = set(static_closure({'bot_research.experiments.validation.check_guard_roster_v2'}))
    paths.add(Path('td_game/balanced.json'))
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        all_passed=True, original_engine_rounds=len(cases)*len(enemy_rosters), cases=cases,
        scope='Opening legality, immutability and first-round combat only. No full-game strength claim.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('time_utc', 'runtime_seconds', 'all_passed', 'original_engine_rounds')}))


if __name__ == '__main__':
    main()
