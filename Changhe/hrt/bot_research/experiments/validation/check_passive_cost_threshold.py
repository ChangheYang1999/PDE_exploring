"""Evaluate the actual passive predicate on legal original-engine prefixes."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.gamekit import Rules
from bot_research.experiments.lead.v24 import Insurer
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure

BAITS=[['tier2'],['tier1']*3,['tier1','tier2'],['tier1']*4,['tier2']*2,['tier1']*6]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args();start=time.perf_counter()
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    paths=set(static_closure({'bot_research.experiments.validation.check_passive_cost_threshold'}))|{Path('configs/balanced.json'),Path('td_game/balanced.json')}
    hashes={str(p):digest(p) for p in paths};cases=[];cfg=balanced_config();assert cfg.minions['tier1'].cost==15 and cfg.minions['tier2'].cost==40
    enumerated=sorted({15*n1+40*n2 for n1 in range(8) for n2 in range(4) if 15*n1+40*n2>40});assert enumerated[0]==45
    for side in (0,1):
        for bait in BAITS:
            for turret in (False,True):
                engine=Engine(cfg,('observer','grower'));policy=Insurer(passive_until=5);rounds=[];cost=sum(cfg.minions[t].cost for t in bait)
                for rnd in range(1,8):
                    assert engine.result is None
                    obs=engine.observation(side);before=deepcopy(obs);rules=Rules.from_observation(obs)
                    actual=policy._passive(obs,rules);expected=rnd<=5 and (rnd<3 or cost<=40) and (not turret or rnd<4)
                    assert actual==expected and obs==before,(side,bait,turret,rnd,actual,expected)
                    assert not Insurer()._passive(obs,rules)
                    opposing=[dict(op='buy_factory')]*5 if rnd==1 else ([dict(op='buy_minion',type=t) for t in bait] if rnd==2 else ([dict(op='build_turret',type='gun1',x=10,y=1)] if rnd==3 and turret else []))
                    actions=[[],[]];actions[1-side]=opposing;events=engine.play_round(actions)
                    assert all(e['accepted'] for row in events for e in row['event'] if e['kind']=='action')
                    rounds.append(dict(round=rnd,predicate=actual))
                cases.append(dict(side=side,bait=bait,cost=cost,turret_round3=turret,rounds=rounds))
    assert all(digest(p)==h for p,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,cases=cases,scope='24 legal seven-round original-engine prefixes evaluating the exact current predicate; no full-game strength claim.')
    atomic_json(args.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))
if __name__=='__main__':main()
