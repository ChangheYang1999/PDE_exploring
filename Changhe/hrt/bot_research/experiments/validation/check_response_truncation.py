"""Verify the truncated-response counterexample on original replay states."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from bot_research.harness import gamekit as gk
from bot_research.experiments.lead.v24 import Insurer,_cost_of,P
from bot_research.bots.counters.untruncated_response import UntruncatedInsurer
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args();start=time.perf_counter()
 digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 sources=set(static_closure({'bot_research.experiments.validation.check_response_truncation'}))|{Path('td_game/balanced.json'),Path('configs/balanced.json')}
 hashes={str(p):digest(p) for p in sources};D=Path('bot_research/runs/validation/screened-guard-001');diag=Path('bot_research/runs/validation/screened-guard-diagnostic-001.json');hashes[str(diag)]=digest(diag);diagnostic=json.loads(diag.read_text());assert diagnostic['all_passed'];cases=[]
 for jobid in ('case0000','case0001'):
  file=D/'results'/(jobid+'.json');checked_row(str(file),hashes);row=json.loads(file.read_text());side=row['condition']['candidate_side'];params={k:json.loads(v[0]) for k,v in parse_qs(row['condition']['candidate_spec'].partition('?')[2]).items()};policy=Insurer(**params);untruncated=UntruncatedInsurer(**params);cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']));records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()];assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
  for rnd in range(1,21):
   obs=engine.observation(side);copied=deepcopy(obs);actual=policy(copied);assert obs==copied and policy.alt is None;pair=records[2*rnd:2*rnd+2];actions=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair];assert actual==actions[side]
   if rnd==20:
    rules=gk.Rules.from_observation(obs);defense=[a for a in actual if a['op'] in ('build_wall','build_turret')];left=obs['players'][side]['gold']-_cost_of(defense,rules);budget=int(left*policy.p['attack_share']);assert policy.failed==2
    before=deepcopy(policy.__dict__);old=policy._attack(obs,rules,budget,'robust');new=untruncated._attack(obs,rules,budget,'robust');assert before==policy.__dict__ and old==([],0);assert new[0] and len(new[0])==22 and all(a==dict(op='buy_minion',type='tier5') for a in new[0]) and new[1]==3080
    attacker=player_from_snapshot(obs['players'][side]);defender=player_from_snapshot(obs['players'][1-side])
    for a in new[0]:assert apply_action(attacker,a,rnd,cfg)['accepted']
    types=[r.type for r in attacker.roster if r.active(rnd)];response_obs=deepcopy(obs);response_obs['player']=1-side;response=policy._plan(response_obs,defender.gold,threat_types=[types],partial='best')
    for a in response:assert apply_action(defender,a,rnd,cfg)['accepted']
    path=shortest_path(cfg.globals.width,cfg.globals.height,[(b.x,b.y) for b in defender.buildings],cfg.globals.spawn,cfg.globals.base);result=simulate_map(attacker,defender,path,rnd,cfg);assert result.damage==new[1]
    t=next(x for c in diagnostic['cases'] if c['condition']['candidate_side']==side for x in c['timeline'] if x['round']==rnd);ranking=t['current_ranking'];assert [r['tier'] for r in ranking]==['tier3','tier4','tier5'];assert all(r['response_ratio']<policy.p['min_leak_per_gold'] for r in ranking[:2]);assert ranking[2]['response_ratio']>=policy.p['min_leak_per_gold'];assert ranking[2]['response_total_damage']==result.damage
    cases.append(dict(side=side,round=rnd,budget=budget,current_ranking=ranking,truncated=old,untruncated=new,response_actions=response,original_combat=asdict(result)))
   assert normalized(engine.play_round(actions))==pair
 assert len(cases)==2 and all(digest(p)==h for p,h in hashes.items())
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,cases=cases,scope='Two original replay prefixes and exact hypothetical-response combats. The response is one policy plan, not every legal defense; full-game effects are separate.')
 atomic_json(args.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
