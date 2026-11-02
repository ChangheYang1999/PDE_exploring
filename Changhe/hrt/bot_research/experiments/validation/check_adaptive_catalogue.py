"""Original-engine component checks for adaptive catalogue attacks."""
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
from bot_research.bots.counters.adaptive_catalogue import AdaptiveCatalogue
from bot_research.bots.counters.stateful_catalogue import StatefulCatalogue, CATALOGUE
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_adaptive_attacks import audit_attack
from bot_research.experiments.validation.audit_stateful_catalogue import audit_trace, EXPECTED
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    sources = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.check_adaptive_catalogue'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases, controls = [], []
    mutations = 0
    for name in [*CATALOGUE, 'idle']:
        for side in (0, 1):
            bot = AdaptiveCatalogue(attack_weight=4)
            enemy = (lambda obs: []) if name == 'idle' else CATALOGUE[name][0](**CATALOGUE[name][1])
            engine = Engine(balanced_config(), ('component0', 'component1'))
            records = json.loads(json.dumps(engine.initial_records(('component0', 'component1'))))
            checks = []
            for rnd in range(1, 9):
                if engine.result is not None:
                    break
                obs = engine.observation(side)
                saved = deepcopy(obs)
                actions = bot.decide(obs)
                assert obs == saved, 'The policy mutated its public observation.'
                other = enemy(engine.observation(1-side))
                trace = bot.trace[-1]
                if name in CATALOGUE:
                    assert name in trace['active']
                    assert trace['predictions'][name]['actions'] == other
                checks.append(audit_attack(obs, actions, trace))
                if rnd == 1:
                    for defect in ('damage', 'pool'):
                        broken = deepcopy(trace)
                        if defect == 'damage':
                            member = next(iter(broken['adaptive_attack']['selected']['damage']))
                            broken['adaptive_attack']['selected']['damage'][member] += 1
                        else:
                            broken['adaptive_attack']['pool_sha256'] = '0'*64
                        try:
                            audit_attack(obs, actions, broken)
                        except ValueError:
                            mutations += 1
                        else:
                            raise AssertionError('Corrupted attack evidence escaped the audit.')
                pair = [None, None]
                pair[side], pair[1-side] = actions, other
                new = engine.play_round(pair)
                assert all(e['accepted'] for r in new for e in r['event'] if e['kind'] == 'action')
                records.extend(json.loads(json.dumps(new)))
            if name == 'idle':
                spec = 'td_bots.protocol:idle'
            else:
                module, params = EXPECTED[name]
                spec = module+':@make?'+urlencode({k: json.dumps(v) for k, v in params.items()})
            row = json.loads(json.dumps(dict(condition=dict(candidate_side=side, opponent_spec=spec),
                catalogue_ids=bot.ids, catalogue_trace=bot.trace, rounds=engine.round, rules=engine.config.to_dict())))
            catalogue = audit_trace(row, records)
            cases.append(dict(target=name, side=side, rounds=engine.round, attacks=checks, catalogue=catalogue))
            print(json.dumps(dict(target=name, side=side, rounds=engine.round, purchased=sum(c.get('purchased', 0) for c in checks))), flush=True)
    for side in (0, 1):
        bot, control = AdaptiveCatalogue(search_enabled=False), StatefulCatalogue(attack_share=0)
        enemy = CATALOGUE['best_v9b'][0]()
        engine = Engine(balanced_config(), ('control0', 'control1'))
        for rnd in range(1, 9):
            if engine.result is not None:
                break
            obs = engine.observation(side)
            actions = bot.decide(deepcopy(obs))
            assert actions == control.decide(deepcopy(obs))
            pair = [None, None]
            pair[side], pair[1-side] = actions, enemy(engine.observation(1-side))
            new = engine.play_round(pair)
            assert all(e['accepted'] for r in new for e in r['event'] if e['kind'] == 'action')
        controls.append(dict(side=side, rounds=engine.round, identical_actions=True))
    assert all(digest(p) == h for p, h in sources.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
        source_sha256=sources, all_passed=True, cases=cases, disabled_controls=controls, mutation_rejections=mutations,
        scope='Eight prefixes against three true catalogue members and idle, with original combat checks of selected attacks. Two disabled-search controls test exact parent action equivalence. Full-game performance is separate.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(all_passed=True, runtime_seconds=output['runtime_seconds'], mutation_rejections=mutations)), flush=True)


if __name__ == '__main__':
    main()
