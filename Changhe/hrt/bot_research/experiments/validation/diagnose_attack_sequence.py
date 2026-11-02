"""Shadow an exact v24 policy and inspect its own attack-selection state."""
from copy import deepcopy
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.lead.v24 import Insurer,_cost_of,_with_buildings,_immune,P,TIER_ORDER
from bot_research.harness import gamekit as gk
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
 parser=argparse.ArgumentParser();parser.add_argument('--campaign',required=True);parser.add_argument('--candidate-id',required=True);parser.add_argument('--opponent-ids',nargs='*');parser.add_argument('--output',required=True);args=parser.parse_args();start=time.perf_counter()
 digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();root=Path(args.campaign)
 sources=set(static_closure({'bot_research.experiments.validation.diagnose_attack_sequence'}))|{Path('td_game/balanced.json'),Path('configs/balanced.json')}
 hashes={str(p):digest(p) for p in sources};jobs=root/'jobs.json';hashes[str(jobs)]=digest(jobs);cases=[]
 for job in json.loads(jobs.read_text()):
  c=job['condition']
  if c['candidate_id']!=args.candidate_id or (args.opponent_ids and c['opponent_id'] not in args.opponent_ids):continue
  result=root/'results'/(job['id']+'.json');checked_row(str(result),hashes);row=json.loads(result.read_text());records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
  spec=c['candidate_spec'];assert spec.split(':')[0]=='bot_research.experiments.lead.v24';params={k:json.loads(v[0]) for k,v in parse_qs(spec.partition('?')[2]).items()}
  policy=Insurer(**params);side=c['candidate_side'];engine=Engine(balanced_config(),tuple(row['bot_specs']));assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2];timeline=[]
  for rnd in range(1,row['rounds']+1):
   obs=engine.observation(side);copy=deepcopy(obs);before_failed=policy.failed;pending_before=deepcopy(policy.pending);proposed=policy(copy)
   pair=records[2*rnd:2*rnd+2];actions=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
   assert copy==obs and proposed==actions[side] and policy.alt is None
   rules=gk.Rules.from_observation(obs);defense=[a for a in proposed if a['op'] in ('build_wall','build_turret')];left=obs['players'][side]['gold']-_cost_of(defense,rules);constructed=_with_buildings(obs,defense,left)
   buildings=constructed['players'][side]['buildings'];path=gk.route_cached(gk.cells_of(buildings));score=gk.splash_total(path,buildings,rules);budget=int(left*policy.p['attack_share']);item=dict(round=rnd,failed_before=before_failed,failed_after=policy.failed,pending_before=pending_before,pending_after=deepcopy(policy.pending),post_construction_splash=score,immune=_immune(constructed,rules),attack_budget=budget,actual_purchases=dict(Counter(a['type'] for a in proposed if a['op']=='buy_minion')))
   if rnd in (6,7,9,10,11,20,21,30,50) and budget>0:
    state=deepcopy(policy.__dict__);base=P.opponent_leak(obs,[])[1];ranking=[]
    for tier in TIER_ORDER:
     n=min(policy.p['max_minions'],budget//rules.minions[tier]['cost'])
     if n<=0:continue
     gain=P.opponent_leak(obs,[tier]*n)[1]-base;ratio=gain/(n*rules.minions[tier]['cost'])
     if ratio<policy.p['min_leak_per_gold']:continue
     ranking.append(dict(tier=tier,count=n,current_damage_increment=gain,current_ratio=ratio))
    ranking.sort(key=lambda r:(r['current_ratio'],r['tier'],r['count'],r['current_damage_increment']),reverse=True)
    if policy.failed>=policy.p['fail_limit']:
     for rank,r in enumerate(ranking):
      damage=policy._leak_after_response(obs,rules,[r['tier']]*r['count']);r['response_total_damage']=damage;r['response_ratio']=damage/(r['count']*rules.minions[r['tier']]['cost']);r['considered_in_robust_mode']=rank<2
    assert state==policy.__dict__;item['current_ranking']=ranking
   timeline.append(item);assert normalized(engine.play_round(actions))==pair
  assert engine.result==row['result'];cases.append(dict(condition=c,result=str(result),outcome=row['candidate_outcome'],rounds=row['rounds'],timeline=timeline));print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=job['id'])),flush=True)
 assert cases and all(digest(p)==h for p,h in hashes.items())
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,cases=cases,scope='Fresh exact-policy shadows on existing complete histories. Extra pure attack/response queries are diagnostics, not actual actions or independent strength samples.')
 atomic_json(args.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
