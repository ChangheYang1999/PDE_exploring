"""Check legal prefixes and the public signal before wall-signal full games."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.wall_signal_timing import WallSignalTiming
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');A=E/'analysis/wall_signal_response'

def main():
 d=json.loads((E/'wall-signal-campaigns-001.json').read_text());inputs=d['input_sha256']
 assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in inputs.items())
 cases=[]
 for count in (19,20):
  for target in ('J','H','I'):
   for side in (0,1):
    cfg=balanced_config();engine=Engine(cfg,('a','b'));attacker=WallSignalTiming(count);opponent=resolve(d['policies'][target]);rounds=[]
    for rnd in range(1,9):
     obs=engine.observation(side);other=engine.observation(1-side);saved=deepcopy((obs,other))
     actions=attacker.decide(obs);answer=opponent.decide(other);assert (obs,other)==saved
     for ob,acts in ((obs,actions),(other,answer)):
      state=player_from_snapshot(ob['players'][ob['player']]);assert all(apply_action(state,a,rnd,cfg)['accepted'] for a in acts)
     exact=attacker.trace[-1]['predicted_actions']==answer
     if target=='H' or (target=='J' and count==20):assert exact
     if rnd==2:
      assert obs['players'][side]['n_walls']==count
     pair=[None,None];pair[side]=actions;pair[1-side]=answer;engine.play_round(pair)
     rounds.append(dict(round=rnd,model_matches=exact,attacker_actions=actions))
     if engine.result is not None:break
    cases.append(dict(wall_count=count,target=target,side=side,rounds=rounds))
 assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in inputs.items())
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,cases=cases,input_sha256=inputs)
 atomic_json(A/'verification/components.json',result,exclusive=True)
 print(json.dumps(dict(all_passed=True,cases=len(cases),checked_rounds=sum(len(c['rounds']) for c in cases))))
if __name__=='__main__':main()
