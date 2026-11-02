"""Verify the output-only ablation on actual public game prefixes."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.delayed_switch_ablation import DelayedSwitchAblation
from bot_research.bots.counters.delayed_policy_switch import DelayedPolicySwitch
from bot_research.bots.counters.adaptive_continuation import AdaptiveContinuation
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    sources = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.check_delayed_switch_ablation'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for switch in (5, 9):
        for mode in ('wave', 'save', 'prefix'):
            for side in (0, 1):
                policy = DelayedSwitchAblation(switch_round=switch, tier='tier3', mode=mode)
                parent = DelayedPolicySwitch(switch_round=switch, tier='tier3')
                observer = AdaptiveContinuation()
                engine = Engine(balanced_config(), ('a', 'b'))
                for rnd in range(1, switch+2):
                    if engine.result is not None:
                        break
                    obs = engine.observation(side)
                    saved = deepcopy(obs)
                    actual = policy.decide(obs)
                    expected = parent.decide(deepcopy(obs))
                    assert obs == saved
                    if rnd == switch:
                        if mode == 'save':
                            expected = [a for a in expected if a['op'] != 'buy_minion']
                        elif mode == 'prefix':
                            expected = parent.trace[-1]['prefix_proposal']
                    assert actual == expected, 'Ablation differs from its stated output transformation.'
                    assert policy.prefix_calls == parent.prefix_calls and policy.continuation_calls == parent.continuation_calls
                    pair = [None, None]
                    pair[side], pair[1-side] = actual, observer.decide(engine.observation(1-side))
                    rec = engine.play_round(pair)
                    assert all(e['accepted'] for r in rec for e in r['event'] if e['kind'] == 'action')
                cases.append(dict(switch_round=switch, mode=mode, side=side, rounds=engine.round))
                print(json.dumps(cases[-1]), flush=True)
    assert all(digest(p) == h for p, h in sources.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
                  all_passed=True, source_sha256=sources, cases=cases,
                  scope='Twelve actual-engine prefixes. Same-input parent comparison and declared output transformation, input immutability and action legality. Full-game results are separate.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps(dict(all_passed=True, runtime_seconds=result['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
