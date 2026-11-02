"""Check adaptive parent actions and fresh continuation against independent policies."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from urllib.parse import urlencode

from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.catalogue_continuation import (
    CONTINUATION_PARAMETERS, economy20,
)
from bot_research.bots.counters.stateful_catalogue import CATALOGUE
from bot_research.bots.counters.adaptive_catalogue import AdaptiveCatalogue
from bot_research.bots.counters.adaptive_continuation import AdaptiveContinuation
from bot_research.experiments.validation.audit_adaptive_attacks import audit_attack
from bot_research.bots.counters.guard_geometry import make as guard
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_stateful_catalogue import audit_trace, EXPECTED
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    sources = {str(p): digest(p) for p in static_closure({
        'bot_research.experiments.validation.check_adaptive_continuation_v2'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for parameters, name in [(p, n) for p in (dict(search_enabled=False), dict(search_enabled=True, attack_weight=4)) for n in [*CATALOGUE, 'idle', 'guard']]:
        for side in (0, 1):
            bot, parent, independent = AdaptiveContinuation(**parameters), AdaptiveCatalogue(**parameters), None
            if name in CATALOGUE:
                enemy = CATALOGUE[name][0](**CATALOGUE[name][1])
                module, opponent_parameters = EXPECTED[name]
                spec = module+':@make?'+urlencode({k: json.dumps(v) for k, v in opponent_parameters.items()})
            elif name == 'idle':
                enemy, spec = (lambda obs: []), 'td_bots.protocol:idle'
            else:
                enemy = guard(roster=['tier1'], x=9, y=1, parameters={'foreign_attack_from': None})
                spec = 'bot_research.bots.counters.guard_geometry:@make?'+urlencode({
                    'roster': json.dumps(['tier1']), 'x': 9, 'y': 1,
                    'parameters': json.dumps({'foreign_attack_from': None})})
            engine = Engine(balanced_config(), ('component0', 'component1'))
            records = json.loads(json.dumps(engine.initial_records(('component0', 'component1'))))
            parent_rounds = continuation_rounds = 0
            for rnd in range(1, 9):
                if engine.result is not None:
                    break
                obs = engine.observation(side)
                saved = deepcopy(obs)
                actions = bot.decide(obs)
                assert obs == saved, 'Input observation was mutated.'
                t = bot.trace[-1]
                if not t['fallback']:
                    assert actions == parent.decide(deepcopy(obs)), 'Nonempty branch differs from parent.'
                    parent_rounds += 1
                else:
                    if independent is None:
                        independent = economy20(**CONTINUATION_PARAMETERS)
                    assert actions == independent(deepcopy(obs)), 'Continuation differs from independent fresh state.'
                    continuation_rounds += 1
                    assert t['continuation']['calls'] == continuation_rounds
                    assert t['continuation']['started_round'] == rnd-continuation_rounds+1
                attack_check = audit_attack(obs, actions, t)
                assert attack_check['enabled'] == (parameters['search_enabled'] and not t['fallback'])
                other = enemy(engine.observation(1-side))
                if name in CATALOGUE:
                    assert not t['fallback'] and t['predictions'][name]['actions'] == other
                pair = [None, None]
                pair[side], pair[1-side] = actions, other
                new = engine.play_round(pair)
                assert all(e['accepted'] for r in new for e in r['event'] if e['kind'] == 'action')
                records.extend(json.loads(json.dumps(new)))
            if name not in CATALOGUE:
                assert continuation_rounds > 0
            row = json.loads(json.dumps(dict(condition=dict(candidate_side=side, opponent_spec=spec),
                catalogue_ids=bot.ids, catalogue_trace=bot.trace, rounds=engine.round, rules=engine.config.to_dict())))
            details = audit_trace(row, records)
            cases.append(dict(parameters=parameters, target=name, side=side, rounds=engine.round,
                parent_equal_rounds=parent_rounds, continuation_equal_rounds=continuation_rounds,
                catalogue=details))
            print(json.dumps({k: cases[-1][k] for k in ('target', 'side', 'rounds', 'parent_equal_rounds', 'continuation_equal_rounds')}), flush=True)
    assert all(digest(p) == value for p, value in sources.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
        source_sha256=sources, all_passed=True, cases=cases,
        scope='Twenty eight-round prefixes with adaptive search enabled and disabled. Exact parent actions before rejection and an independent fresh economy20 after rejection. Full-game strength is separate.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(all_passed=True, runtime_seconds=output['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
