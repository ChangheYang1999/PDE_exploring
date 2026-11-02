"""Check uncertain-roster timing policies on original-engine prefixes."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
from pathlib import Path
import json
import time
from td_game.engine import Engine
from td_game.config import balanced_config
from bot_research.bots.counters.budget_timing import BudgetTiming
from bot_research.bots.counters.snapshots.lead_fifteen_001 import make as lead15
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    started=time.perf_counter()
    cases=[]
    for fraction in (0.25,0.5,1.0):
        for side in (0,1):
            e=Engine(balanced_config(),('check0','check1'))
            candidate=BudgetTiming(budget_fraction=fraction)
            opponent=lead15(big_threat=100,gun_cap=120,poke_until=3,poke_reactive='turret',
                big_partial=True,r1_poke=3,attack_mode='adaptive',fortress_n=4,immune_attack=True)
            for _ in range(12):
                if e.result is not None:
                    break
                obs=e.observation(side)
                before=deepcopy(obs)
                chosen=candidate.decide(obs)
                assert obs==before
                pair=[None,None]
                pair[side]=chosen
                pair[1-side]=opponent(e.observation(1-side))
                records=e.play_round(pair)
                assert all(ev['accepted'] for rec in records for ev in rec['event'] if ev['kind']=='action')
                trace=candidate.trace[-1]
                assert trace['threat_gold']==(0 if obs['round']==1 else int(obs['players'][1-side]['gold']*fraction))
            cases.append(dict(fraction=fraction,side=side,rounds=e.round,
                              hp=[e.players[side].hp,e.players[1-side].hp],trace=candidate.trace))
    paths=set(static_closure({'bot_research.experiments.validation.check_budget_timing'}))|{Path('td_game/balanced.json')}
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-started,
             all_passed=True,original_engine_rounds=sum(c['rounds'] for c in cases),cases=cases,
             source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
             scope='Legality and observation immutability on six prefixes, not a strength result or universal defense certificate.')
    atomic_json(args.output,out,exclusive=True)
    print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed','original_engine_rounds')}))


if __name__=='__main__':
    main()
