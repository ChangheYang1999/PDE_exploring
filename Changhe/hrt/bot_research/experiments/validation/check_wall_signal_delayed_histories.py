"""Regenerate delayed twenty-wall actions and audit their private forecast."""
from copy import deepcopy
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.actions import apply_action
from bot_research.bots.counters.wall_signal_delayed import DelayedWallSignal
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.publish_extended_counter_game import norm
from bot_research.experiments.validation.replay_audit import normalized

def main():
 p=argparse.ArgumentParser();p.add_argument('--campaign',required=True);p.add_argument('--output',required=True);a=p.parse_args();root=Path(a.campaign)
 inputs={};digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 def read(p):inputs[str(p)]=digest(p);return json.loads(Path(p).read_text())
 freeze=read(root/'freeze.json')
 for path,h in freeze['source_sha256'].items():assert digest(path)==h,path;inputs[path]=h
 cases=[]
 for job in read(root/'jobs.json'):
  path=root/'results'/(job['id']+'.json');r=checked_row(str(path),inputs);row=read(path);c=r['condition'];side=c['candidate_side'];parameters=norm(c['candidate_spec'])[1];count=20;target=c['opponent_id']
  attacker=DelayedWallSignal(**parameters);cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']));records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
  assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2];rounds=[]
  for rnd in range(1,row['rounds']+1):
   pair=records[2*rnd:2*rnd+2];actions=[[e['action'] for e in z['event'] if e['kind']=='action'] for z in pair]
   obs=engine.observation(side);saved=deepcopy(obs);fresh=attacker.decide(obs);assert obs==saved and fresh==actions[side]
   state=player_from_snapshot(obs['players'][side]);assert all(apply_action(state,x,rnd,cfg)['accepted'] for x in fresh)
   trace=deepcopy(attacker.trace[-1]);trace['model_matches']=trace['predicted_actions']==actions[1-side]
   if target=='H' or (target=='J' and count==20):assert trace['model_matches']
   if rnd==2:assert obs['players'][side]['n_walls']==count and not obs['players'][side]['roster']
   assert normalized(engine.play_round(actions))==pair;rounds.append(trace)
  assert engine.result==row['result'];cases.append(dict(result_path=str(path),condition=c,rounds=rounds))
 assert len(cases)==6 and all(digest(path)==h for path,h in inputs.items())
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,all_replayed=True,all_actions_legal=True,all_observations_unchanged=True,cases=cases,checked_calls=sum(len(c['rounds']) for c in cases),input_sha256=inputs)
 atomic_json(a.output,result,exclusive=True);print(json.dumps(dict(all_passed=True,cases=len(cases),checked_calls=result['checked_calls'])))
if __name__=='__main__':main()
