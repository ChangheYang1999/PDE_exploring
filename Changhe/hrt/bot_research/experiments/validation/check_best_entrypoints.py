"""Regenerate direct and factory candidate decisions in one fresh interpreter."""
from copy import deepcopy
from pathlib import Path
import argparse,hashlib,importlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser();p.add_argument('--campaign',required=True);p.add_argument('--job',required=True)
    p.add_argument('--module',default='bot_research.bots.best');p.add_argument('--candidate-sha256',required=True);p.add_argument('--output',required=True)
    args=p.parse_args();start=time.perf_counter();root=Path(args.campaign)
    source_path=args.module.replace('.','/')+'.py'
    freeze=json.loads((root/'freeze.json').read_text())
    assert freeze['source_sha256'][source_path]==args.candidate_sha256==digest(source_path)
    source={str(q):digest(q) for q in static_closure({args.module,'bot_research.experiments.validation.check_best_entrypoints'})}
    for q,sha in freeze['source_sha256'].items():
        assert digest(q)==sha,q
        if q in source:assert source[q]==sha
        source[q]=sha
    inputs={};jobpath=root/'jobs'/(args.job+'.json');job=json.loads(jobpath.read_text());side=job['condition']['candidate_side']
    assert job['bots'][side]['spec'].partition(':')[0]==args.module
    recorded_spec=job['bots'][side]['spec'].partition(':')[2]
    assert recorded_spec in ('decide','@make'),recorded_spec
    resultpath=root/'results'/(args.job+'.json');checked_row(str(resultpath),inputs);row=json.loads(resultpath.read_text())
    records=[json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
    cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']))
    assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
    direct=resolve({'spec':args.module+':decide'}).decide
    factory=resolve({'spec':args.module+':@make'}).decide
    prefix=job.get('prefixes',[[],[]])[side]
    differences=[];rounds=[]
    for rnd in range(1,row['rounds']+1):
        pair=records[2*rnd:2*rnd+2]
        actual=[[event['action'] for event in r['event'] if event['kind']=='action'] for r in pair]
        obs=engine.observation(side);fresh=[];times=[]
        for function in (direct,factory):
            argument=deepcopy(obs);begin=time.perf_counter()
            actions=deepcopy(prefix[rnd-1]) if rnd<=len(prefix) else function(argument)
            times.append(time.perf_counter()-begin)
            assert argument==obs
            own=player_from_snapshot(obs['players'][side])
            assert all(apply_action(own,a,rnd,cfg)['accepted'] for a in actions)
            fresh.append(actions)
        flags=[fresh[0]==actual[side],fresh[1]==actual[side],fresh[0]==fresh[1]]
        if not all(flags):differences.append(dict(round=rnd,direct_matches_record=flags[0],factory_matches_record=flags[1],entrypoints_agree=flags[2],direct=fresh[0],factory=fresh[1],recorded=actual[side]))
        rounds.append(dict(round=rnd,policy_invoked=rnd>len(prefix),direct_seconds=times[0],factory_seconds=times[1],direct_matches_record=flags[0],factory_matches_record=flags[1],entrypoints_agree=flags[2]))
        assert normalized(engine.play_round(actual))==pair
    assert engine.result==row['result']
    changed=[q for q,sha in source.items() if digest(q)!=sha]
    assert not changed
    inputs[str(root/'jobs.json')]=digest(root/'jobs.json')
    case={k:row[k] for k in ('condition','hp','result','rounds','trajectory_sha256')}
    case.update(input=str(resultpath),row_index=0,passed=not differences,entrypoint_rounds=rounds,differences=differences,skipped_prefix_rounds=len(prefix),observations_unchanged=True,all_fresh_actions_legal=True)
    output=dict(time_utc=now(),runtime_seconds=time.perf_counter()-start,count=1,all_passed=not differences,candidate_module=args.module,candidate_sha256=args.candidate_sha256,input_sha256=inputs,source_sha256=source,source_changed_during_run=False,cases=[case],scope='Fresh-process direct/factory action equality on this recorded public history. Both policies skip prescribed opening calls. No new strength sample.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({k:output[k] for k in ('time_utc','runtime_seconds','all_passed','candidate_sha256')}))


if __name__=='__main__':main()
