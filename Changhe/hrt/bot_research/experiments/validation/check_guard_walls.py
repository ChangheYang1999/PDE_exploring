"""Compare the exact first-round consequences of small wall prefixes."""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
from pathlib import Path
import json
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.guard_walls import GuardWalls
from bot_research.bots.counters.opening_response import OpeningResponse
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    config = balanced_config()
    compositions = []
    def enumerate_compositions(prefix, gold):
        compositions.append(prefix)
        for kind, spec in config.minions.items():
            if spec.cost <= gold:
                enumerate_compositions(prefix + [kind], gold - spec.cost)
    enumerate_compositions([], 100)
    assert len(compositions) == 27
    rows = []
    for cap in (0, 9, 11, 13, 15):
        for side in (0, 1):
            game = Engine(config, ('a', 'b'))
            obs = game.observation(side)
            original = deepcopy(obs)
            actions = GuardWalls(wall_cap=cap).decide(obs)
            assert original == obs
            if cap == 0:
                assert actions == OpeningResponse(opening='guard_poke5').decide(obs)
            state = deepcopy(game.players[side])
            for action in actions:
                assert apply_action(state, action, 1, config)['accepted']
            damage = []
            for kinds in compositions:
                attacker = deepcopy(game.players[1-side])
                for kind in kinds:
                    assert apply_action(attacker, {'op': 'buy_minion', 'type': kind}, 1, config)['accepted']
                game.players[side] = deepcopy(state)
                outcome = simulate_map(attacker, deepcopy(state), game.path(side), 1, config)
                damage.append({'roster': kinds, 'damage': outcome.damage})
            game = Engine(config, ('a', 'b'))
            pair = [[], []]
            pair[side] = actions
            pair[1-side] = [{'op': 'buy_minion', 'type': 'tier1'}] * 2
            events = game.play_round(pair)
            assert not any(e['kind'] == 'action' and not e['accepted'] for r in events for e in r['event'])
            own = game.players[side]
            assert own.hp == 800
            rows.append({'wall_cap': cap, 'side': side, 'actions': actions,
                         'gold_after_purchases': state.gold, 'ending_gold': own.gold,
                         'route_length': len(game.path(side))-1,
                         'hp_candidate_first': [p.hp for p in game.players][::1 if side == 0 else -1],
                         'factory_count': own.n_factories, 'all_ordered_opening_rosters': damage})
    for cap in (0, 9, 11, 13, 15):
        pair = [r for r in rows if r['wall_cap'] == cap]
        assert [{k:v for k,v in r.items() if k != 'side'} for r in pair][0] == \
               [{k:v for k,v in r.items() if k != 'side'} for r in pair][1]
    paths = set(static_closure({'bot_research.experiments.validation.check_guard_walls'}))
    paths.add(Path('td_game/balanced.json'))
    output = {'time_utc': now(), 'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
              'all_passed': True, 'combat_checks': len(rows)*len(compositions), 'cases': rows,
              'scope': 'First-round components only; no full-game strength guarantee.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'all_passed': True, 'combat_checks': output['combat_checks'],
                      'rows': [{k:r[k] for k in ('wall_cap','side','ending_gold','route_length','factory_count')} for r in rows]}))


if __name__ == '__main__':
    main()
