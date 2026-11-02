"""Regenerate a public-clone timing adversary and compare its predicted target actions."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.stateful_public import StatefulPublicTiming
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p=argparse.ArgumentParser();p.add_argument('--campaign',required=True);p.add_argument('--expected',type=int,required=True);p.add_argument('--output',required=True);a=p.parse_args()
    start=time.perf_counter();digest=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest()
    inputs={str(q):digest(q) for q in static_closure({'bot_research.experiments.validation.check_timing_forecaster_histories'})}
    root=Path(a.campaign);freeze=json.loads((root/'freeze.json').read_text())
    for q,h in freeze['source_sha256'].items():assert digest(q)==h;inputs[q]=h
    cases=[]
    for job in json.loads((root/'jobs.json').read_text()):
        q=root/'results'/(job['id']+'.json');checked_row(str(q),inputs);row=json.loads(q.read_text())
        side=row['condition']['candidate_side'];spec=row['condition']['candidate_spec']
        assert spec.partition(':')[0]=='bot_research.bots.counters.stateful_public'
        params={k:json.loads(v[0]) for k,v in parse_qs(spec.partition('?')[2]).items()}
        counter=StatefulPublicTiming(**params)
        records=[json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
        engine=Engine(balanced_config(),tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
        rounds=[];differences=[];prediction_errors=[]
        saved_trace={v['round']:v for v in row['forecast_trace']}
        for rnd in range(1,row['rounds']+1):
            obs=engine.observation(side);saved=deepcopy(obs);fresh=counter.decide(obs)
            assert obs==saved
            state=player_from_snapshot(saved['players'][side])
            assert all(apply_action(state,x,rnd,engine.config)['accepted'] for x in fresh)
            pair=records[2*rnd:2*rnd+2]
            actions=[[e['action'] for e in rec['event'] if e['kind']=='action'] for rec in pair]
            trace=counter.trace[-1]
            if fresh!=actions[side]:differences.append(rnd)
            if trace['predicted_actions']!=actions[1-side]:prediction_errors.append(rnd)
            assert trace==saved_trace[rnd]
            assert counter.model.last_round==rnd and counter.model.player==1-side
            assert normalized(engine.play_round(actions))==pair
            incoming=next(e['base_damage'] for e in pair[side]['event'] if e['kind']=='combat')
            assert incoming==trace['forecast_residual_damage']
            rounds.append(dict(round=rnd,actions_agree=fresh==actions[side],prediction_exact=trace['predicted_actions']==actions[1-side],incoming_damage=incoming,attack_count=trace['attack_count']))
        assert engine.result==row['result']
        cases.append(dict(result=str(q),condition=row['condition'],rounds=rounds,differing_rounds=differences,prediction_mismatches=prediction_errors))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=job['id'],differences=differences,prediction_mismatches=prediction_errors)),flush=True)
    assert len(cases)==a.expected and all(digest(q)==h for q,h in inputs.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_fresh_actions_agree=all(not c['differing_rounds'] for c in cases),all_predictions_exact=all(not c['prediction_mismatches'] for c in cases),
        all_observations_unchanged=True,all_fresh_actions_legal=True,all_original_combat_agrees=True,
        checked_calls=sum(len(c['rounds']) for c in cases),cases=cases,input_sha256=inputs)
    atomic_json(a.output,out,exclusive=True)
    print(json.dumps({k:v for k,v in out.items() if k not in ('cases','input_sha256')}),flush=True)

if __name__=='__main__':main()
