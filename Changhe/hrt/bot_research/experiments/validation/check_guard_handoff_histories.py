"""Replay public histories while checking fresh guard-handoff controller calls.

Clock-limited planner differences are reported, not silently equated with
record corruption. The original recorded actions drive each engine replay.
"""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.guard_handoff import GuardHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
 p=argparse.ArgumentParser();p.add_argument('--campaign',required=True);p.add_argument('--candidate-ids',nargs='+',required=True);p.add_argument('--opponent-ids',nargs='+',required=True);p.add_argument('--output',required=True);args=p.parse_args()
 start=time.perf_counter();root=Path(args.campaign);digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();sources=set(static_closure({'bot_research.experiments.validation.check_guard_handoff_histories'}))|{Path(p) for p in json.loads((root/'freeze.json').read_text())['source_sha256']};hashes={str(p):digest(p) for p in sources};cases=[];jobs=root/'jobs.json';hashes[str(jobs)]=digest(jobs)
 for job in json.loads(jobs.read_text()):
  c=job['condition']
  if c['candidate_id'] not in args.candidate_ids or c['opponent_id'] not in args.opponent_ids:continue
  file=root/'results'/(job['id']+'.json');checked_row(str(file),hashes);row=json.loads(file.read_text());records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()];side=1-c['candidate_side'];cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']));assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
  spec=c['opponent_spec'];assert spec.split(':')[0]=='bot_research.bots.counters.guard_handoff';params={k:json.loads(v[0]) for k,v in parse_qs(spec.partition('?')[2]).items()};policy=GuardHandoff(**params);differences=[];times=[];fresh_attack_rounds=[]
  for rnd in range(1,row['rounds']+1):
   obs=engine.observation(side);saved=deepcopy(obs);t=time.perf_counter();fresh=policy.decide(obs);times.append(time.perf_counter()-t);assert obs==saved
   state=player_from_snapshot(obs['players'][side]);assert all(apply_action(state,a,rnd,cfg)['accepted'] for a in fresh)
   if any(a['op']=='buy_minion' for a in fresh) and rnd>=params['handoff_round']:fresh_attack_rounds.append(rnd)
   pair=records[2*rnd:2*rnd+2];actual=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
   if fresh!=actual[side]:differences.append(dict(round=rnd,recorded_actions=actual[side],fresh_actions=fresh))
   assert normalized(engine.play_round(actual))==pair
  assert engine.result==row['result'];cases.append(dict(condition=c,result=str(file),rounds=row['rounds'],replayed=True,observations_unchanged=True,fresh_actions_legal=True,internal_rejected_proposals=policy.rejected_proposals,policy_action_differences=differences,fresh_post_handoff_attack_rounds=fresh_attack_rounds,decision_seconds=times));print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=job['id'],differences=len(differences),internal_rejected=len(policy.rejected_proposals))),flush=True)
 assert cases and all(digest(p)==h for p,h in hashes.items());out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_replayed=True,all_observations_unchanged=True,all_fresh_actions_legal=True,exact_policy_reproduction=all(not c['policy_action_differences'] for c in cases),no_internal_rejections=all(not c['internal_rejected_proposals'] for c in cases),input_sha256=hashes,cases=cases,scope='Fresh policies on existing recorded public histories; original actions drive replay. Clock-limited planner divergences are reported explicitly. No independent strength sample.')
 atomic_json(args.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','exact_policy_reproduction','no_internal_rejections')}))

if __name__=='__main__':main()
