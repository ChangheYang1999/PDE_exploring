"""Recompute all control-opponent decisions from recorded public observations."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.bots.counters.delayed_switch_ablation import DelayedSwitchAblation


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
    roots = {'bot_research.experiments.validation.audit_delayed_switch_ablation',
             'bot_research.bots.economy.frozen.v20.econ20'}
    sources = {str(p): digest(p) for p in static_closure(roots)}
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
        opponent = resolve(dict(spec=row['condition']['opponent_spec']))
        owner = getattr(opponent.decide, '__self__', None)
        detail = dict(condition=row['condition'], outcome=row['candidate_outcome'], hp=row['hp'],
                      rounds=row['rounds'], switch_trace=None, first_prefix_mismatch=None)
        for rnd, observer in enumerate(row['catalogue_trace'], 1):
            obs = dict(round=rnd, player=side, rules=row['rules'],
                       players=[records[2*(rnd-1)+i]['snapshot'] for i in (0, 1)])
            actual = [e['action'] for e in records[2*rnd+side]['event'] if e['kind'] == 'action']
            assert opponent.decide(deepcopy(obs)) == actual, 'Recomputed control differs.'
            if isinstance(owner, DelayedSwitchAblation):
                trace = owner.trace[-1]
                if rnd < owner.switch_round or (rnd == owner.switch_round and owner.mode == 'prefix'):
                    assert 'economy17' in observer['active']
                    assert observer['predictions']['economy17']['actions'] == actual
                if rnd == owner.switch_round:
                    detail['switch_trace'] = {k: v for k, v in trace.items() if k != 'prefix_proposal'}
                if ('economy17' in observer['predictions'] and
                    observer['predictions']['economy17']['actions'] != actual and
                    detail['first_prefix_mismatch'] is None):
                    detail['first_prefix_mismatch'] = rnd
        detail['first_fallback_round'] = next((t['round'] for t in row['catalogue_trace'] if t['fallback']), None)
        cases.append(detail)
        print(json.dumps(dict(opponent=row['condition']['opponent_id'], side=side,
                             outcome=row['candidate_outcome'], rounds=row['rounds'])), flush=True)
    assert all(digest(p) == h for p, h in {**inputs, **sources}.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
                  all_passed=True, input_sha256=inputs, source_sha256=sources, cases=cases,
                  scope='All opponent actions recomputed from actual public inputs with fresh policy state. Prefix exactness checked before each declared output transformation. Full original-engine replay is separate.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps(dict(all_passed=True, cases=len(cases), runtime_seconds=result['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
