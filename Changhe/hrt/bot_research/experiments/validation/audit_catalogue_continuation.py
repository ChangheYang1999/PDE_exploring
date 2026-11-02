"""Replay the fresh continuation on recorded public observations only."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time

from bot_research.bots.counters.catalogue_continuation import CONTINUATION_PARAMETERS, economy20
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.replay_audit import check
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    strict = json.loads(Path(args.strict_audit).read_text())
    inputs = {args.strict_audit: digest(args.strict_audit)}
    sources = {str(p): digest(p) for p in static_closure({
        'bot_research.experiments.validation.audit_catalogue_continuation'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for case in strict['cases']:
        path = case['result_path']
        check(digest(path) == strict['input_sha256'][path], 'Result bytes changed.')
        inputs[path] = digest(path)
        row = json.loads(Path(path).read_text())
        replay = row['replay_path']
        inputs[replay] = digest(replay)
        check(inputs[replay] == row['trajectory_sha256'], 'Replay bytes changed.')
        records = [json.loads(line) for line in Path(replay).read_text().splitlines()]
        side = row['condition']['candidate_side']
        model, first, calls = None, None, 0
        for trace in row['catalogue_trace']:
            rnd = trace['round']
            detail = trace['continuation']
            if not trace['fallback']:
                check(model is None, 'Catalogue branch resumed after rejection.')
                check(detail == dict(active=False, calls=0, started_round=None), 'Inactive continuation trace differs.')
                continue
            if model is None:
                model, first = economy20(**CONTINUATION_PARAMETERS), rnd
            calls += 1
            check(detail['active'] and detail['started_round'] == first, 'Continuation start differs.')
            check(detail['calls'] == calls == rnd-first+1, 'Continuation call cadence differs.')
            check(detail['policy'] == 'bot_research.bots.economy.frozen.v20.econ20:@make', 'Continuation identity differs.')
            check(detail['parameters'] == CONTINUATION_PARAMETERS, 'Continuation parameters differ.')
            obs = dict(round=rnd, player=side, rules=row['rules'],
                players=[records[2*(rnd-1)+i]['snapshot'] for i in (0, 1)])
            expected = model(deepcopy(obs))
            actual = [e['action'] for e in records[2*rnd+side]['event'] if e['kind'] == 'action']
            check(expected == actual, 'Fresh continuation actions differ from recorded actions.')
        cases.append(dict(result_path=path, condition=row['condition'], started_round=first,
                          exact_continuation_rounds=calls))
        print(json.dumps(dict(checked=case['job'], started_round=first, exact_continuation_rounds=calls)), flush=True)
    check(all(digest(p) == h for p, h in {**inputs, **sources}.items()), 'Audit inputs or sources changed.')
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        all_passed=True, input_sha256=inputs, source_sha256=sources, cases=cases,
        scope='Fresh economy20 is recomputed once on each recorded public observation after permanent rejection. Exact parent behavior and engine replay have separate checks.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(all_passed=True, runtime_seconds=output['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
