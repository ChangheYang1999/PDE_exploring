"""Explicit timing screens of timed policies; no trajectory deductions."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.timed_frontier import policy_factory
from bot_research.bots.counters.mixed_timing import MixedTiming
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--model',default='fortress12')
    parser.add_argument('--model-parameters',type=json.loads,default={})
    parser.add_argument('--rounds',nargs='+',type=int,default=[4,6,8,10])
    parser.add_argument('--seeds',nargs='+',type=int,default=[0])
    parser.add_argument('--evaluations',type=int,default=192)
    parser.add_argument('--shares',nargs='+',type=float,default=[1.0])
    parser.add_argument('--caps',nargs='+',type=int,default=[200])
    parser.add_argument('--sides',nargs='+',type=int,choices=(0,1),default=[0,1])
    parser.add_argument('--shard',type=int,default=0)
    parser.add_argument('--shards',type=int,default=1)
    parser.add_argument('--start',type=int,default=0)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    directory=Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    started=time.perf_counter()
    with Path(args.output).open('x') as stream:
        for index,(rnd,seed,share,cap,side) in enumerate(itertools.product(
            args.rounds,args.seeds,args.shares,args.caps,args.sides)):
            if index<args.start or index%args.shards!=args.shard:
                continue
            if time.perf_counter()-started>480:
                print(json.dumps({'stopped_before_index':index,'reason':'480 second bound'}),flush=True)
                break
            params={'attack_round':rnd,'evaluations':args.evaluations,'seed':seed,'attack_share':share,'count_cap':cap}
            counter=MixedTiming(model=args.model,model_parameters=args.model_parameters,**params)
            target=CallableBot(policy_factory(args.model,args.model_parameters))
            bots,names=[counter,target],('mixed_forecast_counter',args.model)
            if side:
                bots.reverse()
                names=tuple(reversed(names))
            row=evaluate(names,bots=bots,replay_path=str(directory/f'case{index:04d}.jsonl'),
                condition={'counter_side':side,'index':index,'model':args.model,
                    'model_parameters':args.model_parameters,'parameters':params,
                    'initial_state':'standard','engine_seed':None,
                    'purpose':'mixed-order timed-policy development screen; no deterministic equivalence assumption'})
            row['counter_outcome']='D' if row['result']['winner'] is None else (
                'W' if row['result']['winner']==side else 'L')
            row['forecast_trace']=counter.trace
            _,actual=observations_and_actions(row,1-side)
            row['forecast_mismatch_rounds']=[t['round'] for t in counter.trace if t['predicted_actions']!=actual[t['round']]]
            row['forecast_trace_missing_rounds']=sorted(set(range(1,row['rounds']+1))-{t['round'] for t in counter.trace})
            stream.write(json.dumps(row,sort_keys=True)+'\n')
            stream.flush()
            print(json.dumps({k:row[k] for k in ('condition','counter_outcome','hp','rounds','runtime_seconds',
                'forecast_mismatch_rounds','forecast_trace_missing_rounds','bot_errors',
                'rejected_actions','source_changed_during_match')}),flush=True)


if __name__=='__main__':
    main()
