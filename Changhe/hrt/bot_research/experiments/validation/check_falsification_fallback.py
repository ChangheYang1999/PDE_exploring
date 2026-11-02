"""Controller checks without a long game or an expensive real fallback call."""
from copy import deepcopy
import argparse
import hashlib
import json
from pathlib import Path
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.falsification_fallback import FalsificationFallback
from bot_research.bots.counters.identifying_opening import OpeningIdentifier
from bot_research.bots.counters.identifying_counter import purchase_signature
from bot_research.bots.counters.snapshots.lead_four_001 import make as opponent
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    paths = set(static_closure({'bot_research.experiments.validation.check_falsification_fallback'}))
    hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    wrapped = FalsificationFallback(saturate_round=12)
    baseline = OpeningIdentifier(saturate_round=12)
    target = opponent()
    game = Engine(balanced_config(), ('wrapper', 'known'))
    checks = {}
    for rnd in range(1, 4):
        obs = game.observation(0)
        actual, expected = wrapped.decide(deepcopy(obs)), baseline.decide(deepcopy(obs))
        checks[f'known_round_{rnd}_same_actions'] = actual == expected and not wrapped.switched
        game.play_round([actual, target(game.observation(1))])
    obs = game.observation(0)
    # A deliberately impossible saved signature forces the switching branch.
    wrapped.inner.inner.pending = {'fixture': ('contradicted signature',)}
    calls = []
    def fallback(observation):
        calls.append(observation['round'])
        return [{'op': 'buy_factory'}]
    wrapped.fallback = fallback
    checks['switches_once'] = wrapped.decide(deepcopy(obs)) == [{'op': 'buy_factory'}] and wrapped.switched
    switched = wrapped.switch_round
    # Even an exactly matching old signature must not re-enter the catalogue.
    wrapped.inner.inner.pending = {'fixture': purchase_signature(obs['players'][1], obs['round'] - 1)}
    wrapped.decide(deepcopy(obs))
    checks['stays_in_fallback'] = calls == [obs['round'], obs['round']] and wrapped.switch_round == switched
    checks['no_catalogue_calls_after_switch'] = all(t['catalogue_policy_calls'] == 0 for t in wrapped.trace[-2:])
    checks['one_fallback_call_per_decision'] = all(t['fallback_policy_calls'] == 1 for t in wrapped.trace[-2:])
    changed = [p for p, h in hashes.items() if hashlib.sha256(Path(p).read_bytes()).hexdigest() != h]
    result = {'time_utc': now(), 'checks': checks, 'all_passed': all(checks.values()) and not changed,
              'source_sha256': hashes, 'source_changed_during_run': changed,
              'scope': 'Controller regression and injected contradiction. Does not measure fallback strength.'}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({'checks': checks, 'all_passed': result['all_passed']}))
    assert result['all_passed']


if __name__ == '__main__':
    main()
