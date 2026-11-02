"""Audit finite-policy identification and compare with an informed counter."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.identifying_counter import CATALOGUE, IdentifyingCounter
from bot_research.bots.counters.known_policy import policy_factory as legacy_factory
from bot_research.bots.counters.known_frontier import policy_factory as frontier_factory
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--targets',nargs='+',default=[x[0] for x in CATALOGUE])
    p.add_argument('--modes',nargs='+',choices=('adaptive','informed'),default=['adaptive'])
    p.add_argument('--attack-from',nargs='+',type=int,default=[6])
    p.add_argument('--attack-share',type=float,default=1.0)
    p.add_argument('--cost-penalty',type=float,default=0.1)
    p.add_argument('--sides',nargs='+',type=int,choices=(0,1),default=[0,1])
    p.add_argument('--start',type=int,default=0)
    p.add_argument('--shard',type=int,default=0)
    p.add_argument('--shards',type=int,default=1)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    catalogue={name:(family,model,params) for name,family,model,params in CATALOGUE}
    if any(name not in catalogue for name in a.targets):
        p.error('Unknown target ID.')
    root=Path(a.output).with_suffix('')
    root.mkdir(exist_ok=False)
    start=time.perf_counter()
    with Path(a.output).open('x') as out:
        for index,(name,mode,attack_from,side) in enumerate(itertools.product(
                a.targets,a.modes,a.attack_from,a.sides)):
            if index<a.start or index%a.shards!=a.shard:
                continue
            if time.perf_counter()-start>480:
                print(json.dumps({'stopped_before_index':index,'reason':'480 second budget'}),flush=True)
                return
            parameters={'attack_from':attack_from,'attack_share':a.attack_share,
                        'cost_penalty':a.cost_penalty,'fixed_id':name if mode=='informed' else None}
            counter=IdentifyingCounter(**parameters)
            family,model,model_parameters=catalogue[name]
            target=CallableBot((legacy_factory if family=='known' else frontier_factory)(model,model_parameters))
            bots,names=[counter,target],('identifying_counter',name)
            if side:
                bots.reverse()
                names=tuple(reversed(names))
            replay=root/f'case{index:04d}.jsonl'
            row=evaluate(names,bots=bots,replay_path=str(replay),condition={
                'index':index,'counter_side':side,'target_id':name,'mode':mode,
                'parameters':parameters,'initial_state':'standard','engine_seed':None,
                'purpose':'development catalogue identification; no reserved opponents'})
            row['counter_outcome']='D' if row['result']['winner'] is None else (
                'W' if row['result']['winner']==side else 'L')
            records=[json.loads(s) for s in replay.read_text().splitlines()]
            enemy_actions={r['round']:[e['action'] for e in r['event'] if e['kind']=='action']
                           for r in records if r['player']==1-side and r['round']>0}
            row['identification_trace']=counter.trace
            recorded_rounds={t['round'] for t in counter.trace}
            row['trace_missing_rounds']=sorted(set(range(1,row['rounds']+1))-recorded_rounds)
            row['forecast_model_errors']=[{'round':t['round'],**e} for t in counter.trace for e in t['forecast_errors']]
            row['true_model_missing_rounds']=[t['round'] for t in counter.trace if name not in t['active']]
            row['true_forecast_mismatch_rounds']=[t['round'] for t in counter.trace
                if t['predicted_actions'].get(name)!=enemy_actions[t['round']]]
            row['catalogue_reset_rounds']=[t['round'] for t in counter.trace if t['catalogue_reset']]
            row['first_singleton_round']=next((t['round'] for t in counter.trace if t['active']==[name]),None)
            out.write(json.dumps(row,sort_keys=True)+'\n')
            out.flush()
            print(json.dumps({k:row[k] for k in ('condition','counter_outcome','hp','rounds',
                'runtime_seconds','true_model_missing_rounds','true_forecast_mismatch_rounds',
                'catalogue_reset_rounds','first_singleton_round','trace_missing_rounds','forecast_model_errors','bot_errors','rejected_actions',
                'source_changed_during_match')}),flush=True)


if __name__=='__main__':
    main()
