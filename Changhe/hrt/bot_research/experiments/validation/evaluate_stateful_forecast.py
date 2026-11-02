"""Original-engine timing attacks against an independently cloned adapting bot."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.stateful_forecast import StatefulTiming,policy_factory
from bot_research.experiments.validation.search_timing_equivalence import run_case


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--rounds',nargs='+',type=int,default=[1,6,8,10])
    p.add_argument('--tiers',nargs='+',default=['tier3','tier4','tier5'])
    p.add_argument('--caps',nargs='+',type=int,default=[200])
    p.add_argument('--shares',nargs='+',type=float,default=[1.0])
    p.add_argument('--sides',nargs='+',type=int,choices=(0,1),default=[0,1])
    p.add_argument('--start',type=int,default=0)
    p.add_argument('--shard',type=int,default=0)
    p.add_argument('--shards',type=int,default=1)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    root=Path(a.output).with_suffix('')
    root.mkdir(exist_ok=False)
    started=time.perf_counter()
    with Path(a.output).open('x') as output:
        for index,(rnd,tier,cap,share,side) in enumerate(itertools.product(
                a.rounds,a.tiers,a.caps,a.shares,a.sides)):
            if index<a.start or index%a.shards!=a.shard:
                continue
            if time.perf_counter()-started>480:
                print(json.dumps({'stopped_before_index':index,'reason':'480 second budget'}),flush=True)
                return
            row=run_case('identifying_counter',{},
                {'attack_round':rnd,'tier':tier,'count_cap':cap,'attack_share':share},
                side,root/f'case{index:04d}.jsonl','stateful public-policy counter; development',
                counter_type=StatefulTiming,target_factory=policy_factory)
            row['condition']['index']=index
            output.write(json.dumps(row,sort_keys=True)+'\n')
            output.flush()
            print(json.dumps({key:row[key] for key in ('condition','counter_outcome','hp','rounds',
                'runtime_seconds','forecast_mismatch_rounds','bot_errors','rejected_actions',
                'source_changed_during_match')}),flush=True)


if __name__=='__main__':
    main()
