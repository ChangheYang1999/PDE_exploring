"""Check prescribed openings, public forecasts, and original incoming combat."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time

from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.guarded_forecast import GuardedForecast
from bot_research.bots.counters.guard_geometry import GuardGeometry
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.lead.frozen.best_v9b import make as target
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_adaptive_attacks import combat
from bot_research.experiments.validation.source_closure import static_closure

MODEL = 'bot_research.experiments.lead.frozen.best_v9b:@make'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    sources = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.check_guarded_forecast'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for roster in ((), ('tier1',), ('tier1', 'tier1'), ('tier2',)):
        for side in (0, 1):
            bot = GuardedForecast(roster=roster, model_spec=MODEL)
            opening, enemy = GuardGeometry(roster=roster), target()
            engine = Engine(balanced_config(), ('guarded0', 'guarded1'))
            rounds = []
            for rnd in range(1, 9):
                if engine.result is not None:
                    break
                obs = engine.observation(side)
                saved = deepcopy(obs)
                actions = bot.decide(obs)
                assert obs == saved, 'Input observation changed.'
                if rnd == 1:
                    assert actions == opening.decide(deepcopy(obs)), 'Prescribed opening changed.'
                other = enemy(engine.observation(1-side))
                trace = bot.trace[-1]
                assert trace['predicted_actions'] == other, 'Private prediction differs from actual opponent.'
                assert bot.model.last_round == rnd
                own_copy = player_from_snapshot(obs['players'][side])
                enemy_copy = player_from_snapshot(obs['players'][1-side])
                for state, chosen in ((own_copy, actions), (enemy_copy, other)):
                    for action in chosen:
                        assert apply_action(state, action, rnd, engine.config)['accepted']
                incoming = combat(enemy_copy, own_copy, rnd, engine.config)
                assert incoming == trace['forecast_residual_damage'], 'Original combat disagrees with residual.'
                pair = [None, None]
                pair[side], pair[1-side] = actions, other
                records = engine.play_round(pair)
                assert all(e['accepted'] for r in records for e in r['event'] if e['kind'] == 'action')
                hp_after = engine.observation(side)['players'][side]['hp']
                assert saved['players'][side]['hp'] - hp_after == incoming
                rounds.append(dict(round=rnd, incoming_damage=incoming, predicted_actions_equal=True))
            cases.append(dict(roster=list(roster), side=side, rounds=rounds))
            print(json.dumps(dict(roster=roster, side=side, rounds=len(rounds))), flush=True)
    assert all(digest(p) == value for p, value in sources.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        source_sha256=sources, all_passed=True, cases=cases,
        scope='Eight eight-round prefixes against frozen best_v9b, checking guard equality, independent opponent actions, input immutability, legality and original combat damage. No full-game strength claim.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(all_passed=True, runtime_seconds=output['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
