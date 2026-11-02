"""Regenerate both fixed policies on each recorded public history.

A private opponent model is allowed to be wrong. This checker compares the
actual action-generating policies, not their predicted opponent identities.
"""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import time
from bot_research.bots.counters.early_wall_followup import EarlyWallFollowup
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--expected', type=int, required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    root = Path(args.campaign)
    digest = lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    inputs = {str(p):digest(p) for p in static_closure({
        'bot_research.experiments.validation.check_early_wall_followup_histories'})}
    freeze_path = root/'freeze.json'
    freeze = json.loads(freeze_path.read_text())
    inputs[str(freeze_path)] = digest(freeze_path)
    for p, sha in freeze['source_sha256'].items():
        assert digest(p) == sha, p
        inputs[p] = sha
    jobs_path = root/'jobs.json'
    jobs = json.loads(jobs_path.read_text())
    inputs[str(jobs_path)] = digest(jobs_path)
    cases = []
    for job in jobs:
        assert 'prefixes' not in job, 'This checker is for standard starts.'
        result_path = root/'results'/(job['id']+'.json')
        checked_row(str(result_path), inputs)
        row = json.loads(result_path.read_text())
        records = [json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
        cfg = balanced_config()
        engine = Engine(cfg, tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
        policies = [resolve(description) for description in job['bots']]
        owners = [getattr(p.decide, '__self__', None) for p in policies]
        guards = [o for o in owners if isinstance(o, EarlyWallFollowup)]
        assert len(guards)==1
        guard=guards[0]
        rounds = []
        for rnd in range(1,row['rounds']+1):
            pair = records[2*rnd:2*rnd+2]
            actions = [[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
            calls = []
            for side, policy in enumerate(policies):
                obs = engine.observation(side)
                saved = deepcopy(obs)
                begin = time.perf_counter()
                proposed = policy.decide(obs)
                seconds = time.perf_counter()-begin
                assert obs == saved, (job['id'],rnd,side,'mutated observation')
                own = player_from_snapshot(obs['players'][side])
                assert all(apply_action(own,a,rnd,cfg)['accepted'] for a in proposed)
                calls.append(dict(side=side,seconds=seconds,exact=proposed==actions[side]))
            assert normalized(engine.play_round(actions)) == pair
            rounds.append(dict(round=rnd,calls=calls))
        assert engine.result == row['result']
        exact = all(c['exact'] for r in rounds for c in r['calls'])
        cases.append(dict(result=str(result_path),condition=job['condition'],rounds=rounds,exact=exact,witness=guard.witness['id'],filtered_proposals=guard.filtered_proposals,guard_trace=guard.trace,followup_trace=guard.followup_trace))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),
            finished=job['id'],exact=exact,checked_calls=2*len(rounds))),flush=True)
    assert len(cases) == args.expected
    assert all(digest(p)==sha for p,sha in inputs.items())
    exact = all(c['exact'] for c in cases)
    out = dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_passed=exact,all_replayed=True,all_actions_legal=True,all_observations_unchanged=True,
        games=len(cases),filtered_proposals=sum(len(c['filtered_proposals']) for c in cases),checked_calls=sum(2*len(c['rounds']) for c in cases),
        cases=cases,input_sha256=inputs,
        scope='Fresh standard-start policies on each public history, including the extra-purchase predicate, package trace and any filtered proposals.')
    atomic_json(args.output,out,exclusive=True)
    print(json.dumps({k:v for k,v in out.items() if k not in ('cases','input_sha256')}))
    if not exact:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
