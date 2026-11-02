"""Check prefix synchronization, legal substitution and fresh continuation."""
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
from bot_research.bots.counters.delayed_policy_switch import DelayedPolicySwitch, economy17, PREFIX_PARAMETERS
from bot_research.bots.counters.catalogue_continuation import economy20, CONTINUATION_PARAMETERS
from bot_research.bots.counters.adaptive_continuation import AdaptiveContinuation
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.counters.identifying_counter import purchase_signature
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    sources = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.check_delayed_policy_switch'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for switch, tier in ((3, 'tier1'), (5, 'tier3'), (8, 'tier5'), (None, 'tier5')):
        for side in (0, 1):
            policy = DelayedPolicySwitch(switch_round=switch, tier=tier)
            observer = AdaptiveContinuation()
            reference = economy17(**PREFIX_PARAMETERS)
            continuation = None
            engine = Engine(balanced_config(), ('a', 'b'))
            mismatched = False
            for rnd in range(1, (switch or 7)+2):
                if engine.result is not None:
                    break
                obs = engine.observation(side)
                saved = deepcopy(obs)
                actual = policy.decide(obs)
                assert obs == saved, 'Input mutated.'
                qactions = observer.decide(engine.observation(1-side))
                qtrace = observer.trace[-1]
                if switch is None or rnd <= switch:
                    proposed = reference(deepcopy(obs))
                    assert policy.trace[-1]['prefix_proposal'] == proposed
                    assert 'economy17' in observer.active
                    assert qtrace['predictions']['economy17']['actions'] == proposed
                    if rnd != switch:
                        assert actual == proposed
                    else:
                        keep = [a for a in proposed if a['op'] not in ('buy_factory', 'buy_minion')]
                        projected = player_from_snapshot(obs['players'][side])
                        proposed_state = deepcopy(projected)
                        for a in proposed:
                            assert apply_action(proposed_state, a, rnd, engine.config)['accepted']
                        for a in keep:
                            assert apply_action(projected, a, rnd, engine.config)['accepted']
                        count = min(1000, projected.gold // obs['rules']['minions'][tier]['cost'])
                        assert actual == keep + [dict(op='buy_minion', type=tier)]*count
                        for a in actual[len(keep):]:
                            assert apply_action(projected, a, rnd, engine.config)['accepted']
                        mismatched = purchase_signature(projected, rnd) != purchase_signature(proposed_state, rnd)
                else:
                    if continuation is None:
                        continuation = economy20(**CONTINUATION_PARAMETERS)
                    assert actual == continuation(deepcopy(obs))
                    if mismatched:
                        assert 'economy17' not in observer.active
                pair = [None, None]
                pair[side], pair[1-side] = actual, qactions
                records = engine.play_round(pair)
                assert all(e['accepted'] for rec in records for e in rec['event'] if e['kind'] == 'action')
            cases.append(dict(switch_round=switch, tier=tier, side=side, rounds=engine.round,
                reached_switch=switch is not None and engine.round >= switch, signature_changed=mismatched,
                prefix_calls=policy.prefix_calls, continuation_calls=policy.continuation_calls,
                wave_count=next((t['wave_count'] for t in policy.trace if t['branch'] == 'switch'), None)))
            print(json.dumps(cases[-1]), flush=True)
    assert all(digest(p) == h for p, h in sources.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
                  all_passed=True, source_sha256=sources, cases=cases,
                  scope='Eight short actual-engine prefixes. Same-input prefix clone, substituted construction/budget, input immutability and fresh continuation checked; strength requires full games.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps(dict(all_passed=True, runtime_seconds=result['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
