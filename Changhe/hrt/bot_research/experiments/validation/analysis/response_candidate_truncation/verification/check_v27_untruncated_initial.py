"""Check the lead's robust_k=None implementation on twelve complete histories."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import argparse,ast,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.lead import v24,v27
from bot_research.bots.counters.untruncated_response import UntruncatedInsurer
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args();start=time.perf_counter();digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 sources=set(static_closure({'bot_research.experiments.validation.check_v27_untruncated'}))|{Path('configs/balanced.json'),Path('td_game/balanced.json'),Path('bot_research/experiments/validation/analysis/response_candidate_truncation/V27_EQUIVALENCE.md')};hashes={str(p):digest(p) for p in sources}
 assert all(v27.DEFAULTS[k]==value for k,value in v24.DEFAULTS.items())
 added=set(v27.DEFAULTS)-set(v24.DEFAULTS);assert added=={'robust_k','passive_ratio','passive_defend','passive_turret'}
 trees=[ast.parse(Path(m.__file__).read_text()) for m in (v24,v27)];classes=[next(n for n in t.body if isinstance(n,ast.ClassDef) and n.name=='Insurer') for t in trees];methods=[{n.name:ast.dump(n,include_attributes=False) for n in c.body if isinstance(n,ast.FunctionDef)} for c in classes];assert set(methods[0])==set(methods[1]);changed=[k for k in methods[0] if methods[0][k]!=methods[1][k]];assert set(changed)=={'__call__','_passive','_attack'}
 helpers=[{n.name:ast.dump(n,include_attributes=False) for n in t.body if isinstance(n,ast.FunctionDef)} for t in trees];assert helpers[0]==helpers[1]
 root=Path('bot_research/runs/validation/response-truncation-001');jobs=root/'jobs.json';hashes[str(jobs)]=digest(jobs);cases=[]
 for job in json.loads(jobs.read_text()):
  c=job['condition']
  if c['candidate_id']!='P5TFullResponse':continue
  file=root/'results'/(job['id']+'.json');checked=checked_row(str(file),hashes);row=json.loads(file.read_text());records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()];engine=Engine(balanced_config(),tuple(row['bot_specs']));assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2];policy=v27.Insurer(passive_until=5,poke_reactive='turret_only',fail_limit=2,robust_k=None);side=c['candidate_side']
  for rnd in range(1,row['rounds']+1):
   obs=engine.observation(side);argument=deepcopy(obs);proposed=policy(argument);pair=records[2*rnd:2*rnd+2];actions=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair];assert argument==obs and proposed==actions[side],(job['id'],rnd);assert normalized(engine.play_round(actions))==pair
  assert engine.result==row['result'];cases.append(dict(condition=c,result=str(file),rounds=row['rounds'],all_actions_identical=True,all_original_transitions_identical=True,inputs_unchanged=True));print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=job['id'])),flush=True)
 assert len(cases)==12 and all(digest(p)==h for p,h in hashes.items());out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,common_defaults_identical=True,changed_class_methods=changed,additional_options=sorted(added),input_sha256=hashes,cases=cases,scope='v27 robust_k=None shadows twelve complete untruncated-response histories; exact finite replay check, not new independent games.')
 atomic_json(args.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
