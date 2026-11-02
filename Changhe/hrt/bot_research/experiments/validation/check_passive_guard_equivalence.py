"""Shadow fresh parameter variants on validated guarded-heavy engine histories."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import argparse,ast,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.lead.v24 import Insurer
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.perf_counter();digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    paths=set(static_closure({'bot_research.experiments.validation.check_passive_guard_equivalence'}))|{Path('configs/balanced.json'),Path('td_game/balanced.json')}
    hashes={str(p):digest(p) for p in paths}
    source=Path('bot_research/experiments/lead/v24.py');tree=ast.parse(source.read_text());uses={key:[] for key in ('passive_bait','poke_reactive')}
    for node in ast.walk(tree):
        if not isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):continue
        for sub in ast.walk(node):
            if isinstance(sub,ast.Subscript) and isinstance(sub.slice,ast.Constant) and sub.slice.value in uses:uses[sub.slice.value].append(dict(function=node.name,line=sub.lineno))
    assert [u['function'] for u in uses['passive_bait']]==['_passive']
    assert [u['function'] for u in uses['poke_reactive']]==['_reactive']
    root=Path('bot_research/runs/validation/passive-guard-transfer-001');jobs=root/'jobs.json';hashes[str(jobs)]=digest(jobs);cases=[]
    variants=[dict(id='B0',passive_bait=0),dict(id='B60',passive_bait=60),dict(id='B1000000000',passive_bait=1000000000),dict(id='turret_only',poke_reactive='turret_only')]
    for job in json.loads(jobs.read_text()):
        c=job['condition']
        if c['opponent_id'] not in ('empty_g6_s4_6','fixed_heavy_drip'):continue
        result=root/'results'/(job['id']+'.json');checked=checked_row(str(result),hashes);row=json.loads(result.read_text());records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
        cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']));assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
        policies=[(v['id'],Insurer(passive_until=5,**{k:x for k,x in v.items() if k!='id'})) for v in variants];side=c['candidate_side'];calls=0
        for rnd in range(1,row['rounds']+1):
            obs=engine.observation(side);opp=obs['players'][1-side];new=[e for e in opp['roster'] if e['bought_round']>=2]
            if rnd<=5:assert not new
            assert all(cfg.minions[e['type']].hp>70 for e in new)
            pair=records[2*rnd:2*rnd+2];actions=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
            for name,policy in policies:
                argument=deepcopy(obs);candidate=policy(argument);assert argument==obs and candidate==actions[side],(job['id'],rnd,name);calls+=1
            assert normalized(engine.play_round(actions))==pair
        assert engine.result==row['result']
        cases.append(dict(result=str(result),condition=c,outcome=checked['outcome'],hp=checked['hp_candidate_first'],rounds=row['rounds'],shadow_policy_calls=calls,all_full_action_lists_identical=True,roster_hypotheses_verified=True))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=job['id'],calls=calls)),flush=True)
    assert len(cases)==4 and all(digest(p)==h for p,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,parameter_uses=uses,variants=variants,cases=cases,scope='Sixteen fresh private policy instances shadow four validated baseline histories. All decisions and original-engine transitions must match. These are exact trajectory checks, not sixteen new independent games.')
    atomic_json(a.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))
if __name__=='__main__':main()
