"""Check first handoff decisions on eight recorded public histories."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
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
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args();start=time.perf_counter();digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 sources=set(static_closure({'bot_research.experiments.validation.check_guard_handoff'}))|set(Path('bot_research/bots/counters/data').glob('*guard*.json'))|{Path('bot_research/bots/counters/data/maze_layouts_001.json'),Path('td_game/balanced.json'),Path('configs/balanced.json')};hashes={str(p):digest(p) for p in sources};outcomes=[]
 for handoff in (12,16,19,22):
  for index in (0,1):
   file=Path('bot_research/runs/validation/screened-guard-001/results')/f'case{index:04d}.json';checked_row(str(file),hashes);row=json.loads(file.read_text());side=1-row['condition']['candidate_side'];records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()];cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']));assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2];policy=GuardHandoff(handoff_round=handoff,layout='empty',growth_rounds=6,bait=[],bait_round=2,tier='tier5',factory_cap=2000,purchase_cap=1000)
   for rnd in range(1,handoff+1):
    obs=engine.observation(side);saved=deepcopy(obs);actions=policy.decide(obs);assert saved==obs
    if rnd<handoff:
     pair=records[2*rnd:2*rnd+2];actual=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair];assert actions==actual[side];assert normalized(engine.play_round(actual))==pair
    else:
     state=player_from_snapshot(obs['players'][side]);events=[apply_action(state,a,rnd,cfg) for a in actions];assert all(e['accepted'] for e in events);assert not policy.rejected_proposals
     outcomes.append(dict(handoff_round=handoff,side=side,actions=actions,internal_rejected_proposals=policy.rejected_proposals))
 assert all(digest(p)==h for p,h in hashes.items());out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,cases=outcomes,scope='Eight first-handoff component calls after exact original replay prefixes. Full-game outcomes are separate.')
 atomic_json(args.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
