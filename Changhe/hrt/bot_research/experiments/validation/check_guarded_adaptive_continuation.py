"""Check opening replacement against an independent parent on actual inputs."""
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
from bot_research.bots.counters.stateful_catalogue import CATALOGUE
from bot_research.bots.counters.adaptive_continuation import AdaptiveContinuation
from bot_research.bots.counters.guarded_adaptive_continuation import GuardedAdaptiveContinuation
from bot_research.bots.counters.guard_geometry import GuardGeometry, make as guard
from bot_research.experiments.validation.audit_adaptive_attacks import audit_attack
from bot_research.experiments.validation.audit_stateful_catalogue import audit_trace, EXPECTED
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    sources = {str(p): digest(p) for p in static_closure({
        'bot_research.experiments.validation.check_guarded_adaptive_continuation'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for roster in (['tier1'], ['tier1', 'tier1']):
        for name in [*CATALOGUE, 'idle', 'guard']:
            for side in (0, 1):
                bot = GuardedAdaptiveContinuation(roster=roster)
                parent, opening = AdaptiveContinuation(), GuardGeometry(roster=roster)
                if name in CATALOGUE:
                    enemy = CATALOGUE[name][0](**CATALOGUE[name][1])
                    module, parameters = EXPECTED[name]
                    spec = module+':@make?'+urlencode({k:json.dumps(v) for k,v in parameters.items()})
                elif name == 'idle':
                    enemy, spec = (lambda obs: []), 'td_bots.protocol:idle'
                else:
                    parameters = dict(roster=['tier1'], x=9, y=1,
                                      parameters={'foreign_attack_from':None})
                    enemy = guard(**parameters)
                    spec = 'bot_research.bots.counters.guard_geometry:@make?'+urlencode({
                        k:json.dumps(v) for k,v in parameters.items()})
                engine = Engine(balanced_config(), ('component0', 'component1'))
                records = json.loads(json.dumps(engine.initial_records(('component0', 'component1'))))
                equal_rounds = fallback_rounds = 0
                for rnd in range(1, 9):
                    if engine.result is not None:
                        break
                    obs = engine.observation(side)
                    saved = deepcopy(obs)
                    actions = bot.decide(obs)
                    expected = parent.decide(deepcopy(obs))
                    assert obs == saved, 'Input was mutated.'
                    trace = bot.trace[-1]
                    if rnd == 1:
                        assert actions == opening.decide(deepcopy(obs))
                        assert not trace['adaptive_attack']['enabled']
                        assert trace['attack_count'] == len(roster)
                    else:
                        assert actions == expected, 'Later action differs from same-input parent.'
                        equal_rounds += 1
                    assert bot.pending == parent.pending and bot.active == parent.active
                    assert bot.calls == parent.calls and bot.last_round == parent.last_round
                    if trace['fallback']:
                        fallback_rounds += 1
                    check = audit_attack(obs, actions, trace)
                    assert check['enabled'] == (rnd != 1 and not trace['fallback'])
                    other = enemy(engine.observation(1-side))
                    if name in CATALOGUE:
                        assert not trace['fallback'] and trace['predictions'][name]['actions'] == other
                    pair = [None, None]
                    pair[side], pair[1-side] = actions, other
                    new = engine.play_round(pair)
                    assert all(e['accepted'] for r in new for e in r['event'] if e['kind'] == 'action')
                    records.extend(json.loads(json.dumps(new)))
                if name not in CATALOGUE:
                    assert fallback_rounds > 0
                row = json.loads(json.dumps(dict(condition=dict(candidate_side=side, opponent_spec=spec),
                    catalogue_ids=bot.ids, catalogue_trace=bot.trace, rounds=engine.round,
                    rules=engine.config.to_dict())))
                detail = audit_trace(row, records)
                cases.append(dict(roster=roster, opponent=name, side=side, rounds=engine.round,
                    equal_parent_rounds=equal_rounds, fallback_rounds=fallback_rounds, catalogue=detail))
                print(json.dumps({k:v for k,v in cases[-1].items() if k != 'catalogue'}), flush=True)
    assert all(digest(p) == h for p,h in sources.items()), 'Source changed during check.'
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
                  source_sha256=sources, cases=cases, all_passed=True,
                  scope='Twenty eight-round prefixes, two guard rosters, five opponents and both seats. Parent uses the actual modified-game inputs. Full-game strength is separate.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(all_passed=True, runtime_seconds=output['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
