"""Compare declared growth/poke openings while preserving online identification."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.identifying_counter import CATALOGUE
from bot_research.bots.counters.identifying_opening import OpeningIdentifier
from bot_research.bots.counters.known_policy import policy_factory as legacy_factory
from bot_research.bots.counters.known_frontier import policy_factory as frontier_factory
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--targets',nargs='+',default=[x[0] for x in CATALOGUE])
    p.add_argument('--openings',nargs='+',default=['factories'])
    p.add_argument('--attack-from',type=int,default=6)
    p.add_argument('--sides',nargs='+',type=int,choices=(0,1),default=[0,1])
    p.add_argument('--shard',type=int,default=0)
    p.add_argument('--shards',type=int,default=1)
    p.add_argument('--start',type=int,default=0)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    catalogue={name:(family,model,params) for name,family,model,params in CATALOGUE}
    root=Path(a.output).with_suffix('')
    root.mkdir(exist_ok=False)
    started=time.perf_counter()
    with Path(a.output).open('x') as output:
        for index,(name,opening,side) in enumerate(itertools.product(a.targets,a.openings,a.sides)):
            if index<a.start or index%a.shards!=a.shard:
                continue
            if time.perf_counter()-started>480:
                print(json.dumps({'stopped_before_index':index,'reason':'480 second budget'}),flush=True)
                return
            parameters={'opening':opening,'attack_from':a.attack_from}
            counter=OpeningIdentifier(**parameters)
            family,model,model_parameters=catalogue[name]
            target=CallableBot((legacy_factory if family=='known' else frontier_factory)(model,model_parameters))
            bots,names=[counter,target],('opening_identifier',name)
            if side:
                bots.reverse()
                names=tuple(reversed(names))
            replay=root/f'case{index:04d}.jsonl'
            row=evaluate(names,bots=bots,replay_path=str(replay),condition={
                'index':index,'counter_side':side,'target_id':name,'mode':'opening_'+opening,
                'parameters':parameters,'initial_state':'standard','engine_seed':None,
                'purpose':'declared first-round opening ablation; development'})
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
            output.write(json.dumps(row,sort_keys=True)+'\n')
            output.flush()
            print(json.dumps({k:row[k] for k in ('condition','counter_outcome','hp','rounds','runtime_seconds',
                'true_model_missing_rounds','true_forecast_mismatch_rounds','catalogue_reset_rounds',
                'first_singleton_round','trace_missing_rounds','forecast_model_errors','bot_errors',
                'rejected_actions','source_changed_during_match')}),flush=True)


if __name__=='__main__':
    main()
