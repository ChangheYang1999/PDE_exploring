"""Recompute delayed-switch opponent decisions and inspect rejection timing."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from urllib.parse import parse_qsl
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.delayed_policy_switch import DelayedPolicySwitch
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.counters.identifying_counter import purchase_signature
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    strict = json.loads(Path(args.strict_audit).read_text())
    inputs = {args.strict_audit: digest(args.strict_audit)}
    sources = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.audit_delayed_policy_switch'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for case in strict['cases']:
        result_path = case['result_path']
        inputs[result_path] = digest(result_path)
        assert inputs[result_path] == strict['input_sha256'][result_path]
        row = json.loads(Path(result_path).read_text())
        replay = row['replay_path']
        inputs[replay] = digest(replay)
        assert inputs[replay] == row['trajectory_sha256']
        records = [json.loads(s) for s in Path(replay).read_text().splitlines()]
        side = 1-row['condition']['candidate_side']
        spec = row['condition']['opponent_spec']
        module, _, entry = spec.partition(':')
        assert module == 'bot_research.bots.counters.delayed_policy_switch'
        name, _, query = entry.partition('?')
        assert name == '@make'
        policy = DelayedPolicySwitch(**{k: json.loads(v) for k, v in parse_qsl(query)})
        config = config_from_dict(row['rules'])
        mismatch = None
        wave_count = None
        survived_switch = False
        for rnd, observer_trace in enumerate(row['catalogue_trace'], 1):
            assert rnd == observer_trace['round']
            obs = dict(round=rnd, player=side, rules=row['rules'],
                       players=[records[2*(rnd-1)+i]['snapshot'] for i in (0, 1)])
            actual = [e['action'] for e in records[2*rnd+side]['event'] if e['kind'] == 'action']
            expected = policy.decide(deepcopy(obs))
            assert actual == expected, 'Recomputed switching policy differs.'
            trace = policy.trace[-1]
            if trace['prefix_proposal'] is not None:
                assert 'economy17' in observer_trace['active'], 'True prefix eliminated too soon.'
                assert observer_trace['predictions']['economy17']['actions'] == trace['prefix_proposal']
            if trace['branch'] == 'switch':
                a, b = (player_from_snapshot(obs['players'][side]) for _ in (0, 1))
                for state, actions in ((a, actual), (b, trace['prefix_proposal'])):
                    for action in actions:
                        assert apply_action(state, action, rnd, config)['accepted']
                mismatch = purchase_signature(a, rnd) != purchase_signature(b, rnd)
                wave_count = trace['wave_count']
            if policy.switch_round is not None and rnd == policy.switch_round+1:
                survived_switch = True
                if mismatch:
                    assert 'economy17' in observer_trace['eliminated'], 'Changed prefix was not eliminated at first opportunity.'
        detail = dict(condition=row['condition'], candidate_outcome=row['candidate_outcome'], hp=row['hp'],
                      rounds=row['rounds'], recomputed_decisions=len(policy.trace), switch_round=policy.switch_round,
                      switch_reached=wave_count is not None, wave_count=wave_count, signature_changed=mismatch,
                      reached_next_round=survived_switch,
                      first_fallback_round=next((t['round'] for t in row['catalogue_trace'] if t['fallback']), None))
        cases.append(detail)
        print(json.dumps({k: detail[k] for k in ('switch_round', 'candidate_outcome', 'rounds', 'wave_count', 'signature_changed', 'first_fallback_round')}), flush=True)
    assert all(digest(p) == h for p, h in {**inputs, **sources}.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
                  all_passed=True, input_sha256=inputs, source_sha256=sources, cases=cases,
                  scope='Recomputed opponent actions on actual public observations, exact retained prefix proposals and observed rejection timing. These are targeted development games; original-engine replay is checked separately.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps(dict(all_passed=True, cases=len(cases), runtime_seconds=result['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
