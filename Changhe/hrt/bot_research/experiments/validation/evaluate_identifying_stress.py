"""Challenge the catalogue counter with unknown and changing public policies."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.identifying_counter import IdentifyingCounter
from bot_research.bots.counters.catalogue_switch import CatalogueSwitch
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import resolve

CASES={
    'rush_t1':{'spec':'bot_research.bots.counters.archetypes:rush_t1'},
    'rush_t2':{'spec':'bot_research.bots.counters.archetypes:rush_t2'},
    'eco5_t1':{'spec':'bot_research.bots.counters.archetypes:eco5_t1'},
    'mixed5':{'spec':'bot_research.bots.counters.archetypes:mixed5'},
    'economy_to_flood7':{'switch':{'prefix':'economy','after':'archetype:eco6_t5','switch_round':7}},
    'fortress_to_flood7':{'switch':{'prefix':'fortress','after':'archetype:eco6_t5','switch_round':7}},
    'lead_to_economy6':{'switch':{'prefix':'lead_four','after':'economy','switch_round':6}},
    'alternate3':{'switch':{'prefix':'economy','after':'archetype:eco6_t5','switch_round':7,'period':3}},
}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--cases',nargs='+',default=list(CASES))
    parser.add_argument('--attack-from',type=int,default=6)
    parser.add_argument('--sides',nargs='+',type=int,choices=(0,1),default=[0,1])
    parser.add_argument('--shard',type=int,default=0)
    parser.add_argument('--shards',type=int,default=1)
    parser.add_argument('--start',type=int,default=0)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    root=Path(args.output).with_suffix('')
    root.mkdir(exist_ok=False)
    started=time.perf_counter()
    with Path(args.output).open('x') as output:
        for index,(name,side) in enumerate(itertools.product(args.cases,args.sides)):
            if index<args.start or index%args.shards!=args.shard:
                continue
            if time.perf_counter()-started>480:
                print(json.dumps({'stopped_before_index':index,'reason':'480 second budget'}),flush=True)
                return
            description=CASES[name]
            target=CatalogueSwitch(**description['switch']) if 'switch' in description else resolve(description)
            counter=IdentifyingCounter(attack_from=args.attack_from)
            bots,names=[counter,target],('identifying_counter',name)
            if side:
                bots.reverse()
                names=tuple(reversed(names))
            replay=root/f'case{index:04d}.jsonl'
            row=evaluate(names,bots=bots,replay_path=str(replay),condition={
                'index':index,'counter_side':side,'target_id':name,'target_description':description,
                'parameters':{'attack_from':args.attack_from},'initial_state':'standard','engine_seed':None,
                'purpose':'out-of-catalogue development stress; no reserved opponents'})
            row['counter_outcome']='D' if row['result']['winner'] is None else (
                'W' if row['result']['winner']==side else 'L')
            row['identification_trace']=counter.trace
            row['catalogue_reset_rounds']=[t['round'] for t in counter.trace if t['catalogue_reset']]
            row['forecast_model_errors']=[{'round':t['round'],**error}
                                          for t in counter.trace for error in t['forecast_errors']]
            rounds={t['round'] for t in counter.trace}
            row['trace_missing_rounds']=sorted(set(range(1,row['rounds']+1))-rounds)
            if hasattr(target,'trace'):
                row['opponent_phase_trace']=target.trace
            records=[json.loads(line) for line in replay.read_text().splitlines()]
            enemy_actions={r['round']:[e['action'] for e in r['event'] if e['kind']=='action']
                           for r in records if r['round']>0 and r['player']==1-side}
            row['no_matching_forecast_rounds']=[t['round'] for t in counter.trace
                if not any(actions==enemy_actions[t['round']] for actions in t['predicted_actions'].values())]
            output.write(json.dumps(row,sort_keys=True)+'\n')
            output.flush()
            print(json.dumps({key:row[key] for key in ('condition','counter_outcome','hp','rounds',
                'runtime_seconds','catalogue_reset_rounds','no_matching_forecast_rounds',
                'trace_missing_rounds','forecast_model_errors','bot_errors','rejected_actions',
                'source_changed_during_match')}),flush=True)


if __name__=='__main__':
    main()
