"""Replay and retabulate the defense lane's fixed x158 comparison."""
from pathlib import Path
from collections import Counter,defaultdict
from datetime import datetime,timezone
import hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure,module_file
from bot_research.experiments.validation.artifact_io import atomic_json

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
 start=time.perf_counter();p=Path('bot_research/runs/defense/x158_vs_lead/results.jsonl')
 inputs={str(p):sha(p)};source={str(q):sha(q) for q in static_closure({'bot_research.experiments.validation.audit_team_fortress_table'})}
 source['td_game/balanced.json']=sha('td_game/balanced.json')
 rows=[json.loads(s) for s in p.read_text().splitlines()];assert len(rows)==60
 seen=set();counts=defaultdict(Counter);cases=[]
 for i,r in enumerate(rows):
  assert not r.get('error') and not r['source_changed'] and not any(r['scenario_errors'])
  assert all(not v['bot_errors'] and not v['rejected'] for v in r['players'])
  side=r['candidate_side'];specs=[r['spec_a'],r['spec_b']]
  for label in ('a','b'):assert r['sources'][str(module_file(r['spec_'+label].partition(':')[0]))]==r['hash_'+label]
  for name in ('engine','combat','actions','config','state','pathfinding'):
   key='td_game/'+name+'.py';assert r['sources'][key]==source[key]
  key=(specs[side],specs[1-side],r['scenario'],side);assert key not in seen;seen.add(key)
  path=Path(r['log']);assert not path.is_absolute() and '..' not in path.parts
  inputs[str(path)]=sha(path);records=[json.loads(s) for s in path.read_text().splitlines()]
  assert len(records)==2*(r['rounds']+1)
  engine=Engine(balanced_config(),tuple(specs));initial=normalized(engine.initial_records(tuple(specs)))
  extra={'research_specs':specs,'research_scenario':r['scenario']}
  if r.get('metadata'):extra['research_metadata']=r['metadata']
  for v in initial:v['match'].update(extra)
  assert initial==records[:2]
  dealt=[0,0]
  for rnd in range(1,r['rounds']+1):
   pair=records[2*rnd:2*rnd+2];actions=[[e['action'] for e in v['event'] if e['kind']=='action'] for v in pair]
   assert normalized(engine.play_round(actions))==pair
   for defender,v in enumerate(pair):dealt[1-defender]+=next(e['base_damage'] for e in v['event'] if e['kind']=='combat')
  assert engine.result=={'winner':r['winner'],'reason':r['reason']}
  assert [v.hp for v in engine.players]==[r['hp_a'],r['hp_b']]
  assert r['hp_diff_a']==r['hp_a']-r['hp_b']
  assert dealt==[v['damage_dealt'] for v in r['players']]
  outcome='D' if r['winner'] is None else 'W' if r['winner']==side else 'L'
  group='standard' if r['scenario'] is None else 'continuation';counts[group][outcome]+=1
  cases.append(dict(row=i,scenario=r['scenario'],fortress=specs[side],opponent=specs[1-side],side=side,outcome=outcome,hp_fortress_first=[r['hp_a'],r['hp_b']][::1 if side==0 else -1],damage_dealt_fortress_first=dealt[::1 if side==0 else -1],rounds=r['rounds'],replayed=True))
  print(json.dumps(dict(replayed=i+1,total=60)),flush=True)
 assert len({c['fortress'] for c in cases})==3 and len({c['opponent'] for c in cases})==2 and len({c['scenario'] for c in cases})==5
 assert dict(counts['standard'])==dict(D=6,L=6) and dict(counts['continuation'])==dict(W=24,L=24)
 assert all(sha(k)==v for k,v in source.items())
 output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,source_sha256=source,input_sha256=inputs,all_passed=True,cases=cases,fortress_outcomes=dict(counts),scope='Original-engine replay of sixty existing defense-lane games, not new strength samples.')
 atomic_json('bot_research/experiments/validation/analysis/team_fortress_report_audit/verification/x158.json',output,exclusive=True)
 print(json.dumps(dict(all_passed=True,counts=dict(counts))))
if __name__=='__main__':main()
