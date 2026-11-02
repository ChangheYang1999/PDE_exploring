"""Compare each completed selector history with its chosen standalone policy."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse,hashlib,json,time
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
    parser=argparse.ArgumentParser();parser.add_argument('--campaign',required=True);parser.add_argument('--expected',type=int,required=True);parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.perf_counter();root=Path(args.campaign);E=Path('bot_research/experiments/validation')
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    inputs={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.check_shared_prefix_histories'})}
    declaration=E/'shared-prefix-campaigns-001.json';d=json.loads(declaration.read_text());inputs[str(declaration)]=digest(declaration)
    freeze=json.loads((root/'freeze.json').read_text())
    for p,h in freeze['source_sha256'].items():assert digest(p)==h;inputs[p]=h
    cases=[]
    for job in json.loads((root/'jobs.json').read_text()):
        path=root/'results'/(job['id']+'.json');summary=checked_row(str(path),inputs);row=json.loads(path.read_text())
        records=[json.loads(x) for x in Path(row['replay_path']).read_text().splitlines()]
        side=row['condition']['candidate_side'];assert row['rounds']>=2
        after_first=records[2+(1-side)]['snapshot']
        branch='H' if after_first['n_walls']>=20 and not after_first['roster'] else 'I'
        reference=resolve({'spec':d['policies'][branch]['spec']})
        engine=Engine(balanced_config(),tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
        rounds=[]
        for rnd in range(1,row['rounds']+1):
            obs=engine.observation(side);before=deepcopy(obs);actions=reference.decide(obs)
            assert obs==before
            state=player_from_snapshot(before['players'][side])
            assert all(apply_action(state,x,rnd,engine.config)['accepted'] for x in actions)
            pair=records[2*rnd:2*rnd+2]
            actual=[[e['action'] for e in rec['event'] if e['kind']=='action'] for rec in pair]
            assert actions==actual[side],(job['id'],rnd,branch)
            assert normalized(engine.play_round(actual))==pair
            rounds.append(dict(round=rnd,selected_reference_actions_agree=True))
        assert engine.result==row['result']
        cases.append(dict(result_path=str(path),opponent_id=row['condition']['opponent_id'],candidate_side=side,selected_branch=branch,round2_opponent_walls=after_first['n_walls'],round2_opponent_roster=len(after_first['roster']),rounds=rounds))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=job['id'],branch=branch,checked_calls=len(rounds))),flush=True)
    assert len(cases)==args.expected and all(digest(p)==h for p,h in inputs.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,all_reference_actions_agree=True,all_actions_legal=True,all_observations_unchanged=True,all_replayed=True,checked_calls=sum(len(x['rounds']) for x in cases),cases=cases,input_sha256=inputs)
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','input_sha256')}),flush=True)


if __name__=='__main__':main()
