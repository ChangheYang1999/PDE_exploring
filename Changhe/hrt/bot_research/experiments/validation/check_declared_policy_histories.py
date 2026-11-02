"""Regenerate both fixed factory policies on every recorded public observation."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse, hashlib, json, time
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
    parser=argparse.ArgumentParser()
    parser.add_argument('--campaigns',nargs='+',required=True)
    parser.add_argument('--expected',type=int,required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args();start=time.perf_counter()
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    hashes={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.check_declared_policy_histories'})}
    cases=[]
    for directory in args.campaigns:
        root=Path(directory)
        for p,h in json.loads((root/'freeze.json').read_text())['source_sha256'].items():
            assert digest(p)==h
            if p in hashes:assert hashes[p]==h
            hashes[p]=h
        hashes[str(root/'jobs.json')]=digest(root/'jobs.json')
        for job in json.loads((root/'jobs.json').read_text()):
            assert 'prefixes' not in job
            assert all(bot['spec'].partition(':')[2].startswith('@') for bot in job['bots'])
            path=root/'results'/(job['id']+'.json');checked_row(str(path),hashes)
            row=json.loads(path.read_text())
            records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
            cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']))
            assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
            policies=[resolve(bot) for bot in job['bots']]
            differences=[[],[]];times=[[],[]]
            for rnd in range(1,row['rounds']+1):
                pair=records[2*rnd:2*rnd+2]
                actual=[[event['action'] for event in r['event'] if event['kind']=='action'] for r in pair]
                for side in (0,1):
                    observation=engine.observation(side);original=deepcopy(observation)
                    begin=time.perf_counter();fresh=policies[side].decide(observation)
                    times[side].append(time.perf_counter()-begin)
                    assert observation==original
                    own=player_from_snapshot(observation['players'][side])
                    assert all(apply_action(own,a,rnd,cfg)['accepted'] for a in fresh)
                    if fresh!=actual[side]:differences[side].append(rnd)
                assert normalized(engine.play_round(actual))==pair
            assert engine.result==row['result']
            cases.append(dict(condition=job['condition'],result=str(path),rounds=row['rounds'],
                differing_rounds= differences,decision_seconds=times,replayed=True,
                observations_unchanged=True,all_fresh_actions_legal=True))
            print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),campaign=directory,
                finished=job['id'],differences=list(map(len,differences)))),flush=True)
    assert len(cases)==args.expected
    assert all(digest(p)==h for p,h in hashes.items())
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        input_sha256=hashes,cases=cases,all_replayed=True,all_observations_unchanged=True,
        all_fresh_actions_legal=True,exact_policy_reproduction=all(not any(c['differing_rounds']) for c in cases),
        scope='Both fresh factory policies are advanced once on each recorded standard-start observation. Original actions drive replay. Differences, including possible timed-search differences, are reported without being discarded.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({k:output[k] for k in ('time_utc','runtime_seconds','exact_policy_reproduction')}))

if __name__=='__main__':main()
