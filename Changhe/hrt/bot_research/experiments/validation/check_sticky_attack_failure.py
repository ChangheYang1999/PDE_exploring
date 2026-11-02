"""Diagnose legitimate private adaptation state without changing actual play."""
from copy import deepcopy
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.lead.v24 import Insurer,_cost_of,_with_buildings,_immune
from bot_research.harness import gamekit as gk
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.perf_counter();digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    paths=set(static_closure({'bot_research.experiments.validation.check_sticky_attack_failure'}))|{Path('configs/balanced.json'),Path('td_game/balanced.json')}
    hashes={str(p):digest(p) for p in paths};root=Path('bot_research/runs/validation/passive-guard-transfer-001');jobs=root/'jobs.json';hashes[str(jobs)]=digest(jobs);cases=[]
    for job in json.loads(jobs.read_text()):
        c=job['condition']
        if c['opponent_id']!='empty_g6_s4_6':continue
        result=root/'results'/(job['id']+'.json');checked_row(str(result),hashes);row=json.loads(result.read_text());records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
        engine=Engine(balanced_config(),tuple(row['bot_specs']));assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
        policy=Insurer(passive_until=5);side=c['candidate_side'];timeline=[]
        for rnd in range(1,row['rounds']+1):
            obs=engine.observation(side);rules=gk.Rules.from_observation(obs);pair=records[2*rnd:2*rnd+2];actions=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
            pending_before=deepcopy(policy.pending);failed_before=policy.failed;argument=deepcopy(obs);proposed=policy(argument)
            assert argument==obs and proposed==actions[side] and policy.alt is None
            defense=[a for a in proposed if a['op'] in ('build_wall','build_turret')];left=obs['players'][side]['gold']-_cost_of(defense,rules);constructed=_with_buildings(obs,defense,left)
            buildings=constructed['players'][side]['buildings'];path=gk.route_cached(gk.cells_of(buildings));score=gk.splash_total(path,buildings,rules)
            budget=int(left*policy.p['attack_share']);state_before=deepcopy(policy.__dict__)
            current,predicted=policy._attack(obs,rules,budget,'current') if rnd>=6 and budget>0 else ([],0)
            assert policy.__dict__==state_before
            item=dict(round=rnd,pending_before=pending_before,pending_after=policy.pending,failed_before=failed_before,failed_after=policy.failed,fortress=policy.fortress,post_construction_splash=score,post_construction_immune=_immune(constructed,rules),attack_budget=budget,current_query_purchases=dict(Counter(a['type'] for a in current)),current_query_predicted=predicted,actual_purchases=dict(Counter(a['type'] for a in proposed if a['op']=='buy_minion')),hp_before=[p['hp'] for p in obs['players']])
            timeline.append(item);assert normalized(engine.play_round(actions))==pair
        assert engine.result==row['result'] and row['rounds']==50
        sixth=timeline[5];seventh=timeline[6]
        assert sixth['actual_purchases']=={'tier2':2} and sixth['pending_after'][2]==24
        assert seventh['pending_before'][2]==24 and seventh['failed_before']==0 and seventh['failed_after']==1
        assert all(t['failed_after']==1 and not t['post_construction_immune'] and not t['actual_purchases'] for t in timeline[6:])
        assert any(t['current_query_purchases'] for t in timeline[6:])
        cases.append(dict(condition=c,result=str(result),timeline=timeline))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=job['id'])),flush=True)
    assert len(cases)==2 and all(digest(p)==h for p,h in hashes.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,cases=cases,scope='Two fresh policy shadows and original-engine replay checks; extra current-mode queries are offline diagnostics, not actual decisions or additional independent games.')
    atomic_json(args.output,result,exclusive=True);print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','all_passed')}))
if __name__=='__main__':main()
