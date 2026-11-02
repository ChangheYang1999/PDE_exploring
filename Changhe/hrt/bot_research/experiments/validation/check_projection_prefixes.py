"""Check common branch prefixes and round-four projections on disclosed histories."""
from pathlib import Path
from datetime import datetime,timezone
from copy import deepcopy
import hashlib,json
from td_game.engine import Engine
from td_game.config import balanced_config
from bot_research.bots.counters.projected_lead_selector import ProjectedLeadSelector
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.artifact_io import atomic_json

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 inputs={str(p):sha(p) for p in static_closure({'bot_research.experiments.validation.check_projection_prefixes'})};cases=[]
 names=['public-selector-'+tag+'001' for tag in 'abc']+['selector-baselines-'+tag+'001' for tag in 'abc']+['roster-spoof-001']
 for name in names:
  root=Path('bot_research/runs/validation')/name
  for job in json.loads((root/'jobs.json').read_text()):
   c=job['condition']
   if c['opponent_id']!='select_growth':continue
   side=1-c['candidate_side'];p=root/'results'/(job['id']+'.json');checked_row(str(p),inputs);row=json.loads(p.read_text())
   records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()];game=Engine(balanced_config(),tuple(row['bot_specs']))
   assert normalized(game.initial_records(tuple(row['bot_specs'])))==records[:2]
   policy=ProjectedLeadSelector();traces=[];prefix_actions=[]
   for rnd in range(1,5):
    obs=game.observation(side);saved=deepcopy(obs);actions=policy.decide(obs);assert obs==saved
    traces.append(dict(policy.trace[-1],actions=actions))
    if rnd<4:
     pair=records[2*rnd:2*rnd+2];actual=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
     assert actions==actual[side];assert normalized(game.play_round(actual))==pair;prefix_actions.append(actual)
    else:
     verify=Engine(balanced_config(),tuple(row['bot_specs']))
     for pair in prefix_actions:verify.play_round(pair)
     # Use a separate forced-early policy to recover the hypothetical action list
     # even when the adaptive selector returned the growth branch.
     ep=ProjectedLeadSelector(mode='early');pg=Engine(balanced_config(),tuple(row['bot_specs']))
     for pair in prefix_actions:
      ep.decide(pg.observation(side));pg.play_round(pair)
     early=ep.decide(pg.observation(side));both=[[],[]];both[side]=early
     out=verify.play_round(both);v=policy.trace[-1]['projection']
     incoming=next(e['base_damage'] for e in out[side]['event'] if e['kind']=='combat')
     outgoing=next(e['base_damage'] for e in out[1-side]['event'] if e['kind']=='combat')
     assert v['incoming_damage']==incoming and v['outgoing_damage']==outgoing
     assert v['projected_own_hp']==verify.players[side].hp
     assert v['projected_lead']==verify.players[side].hp-verify.players[1-side].hp
   cases.append(dict(target=c['candidate_id'],side=c['candidate_side'],reference=str(p),selected=policy.selected,traces=traces))
 assert len(cases)==48
 output=dict(time_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,input_sha256=inputs,cases=cases,scope='Common rounds1-3 and exact counterfactual no-enemy-action round-four Engine checks, not full-game outcomes.')
 atomic_json('bot_research/experiments/validation/analysis/round4_public_projection/verification/prefixes_corrected.json',output,exclusive=True)
 for c in cases[::2]:print(json.dumps(dict(target=c['target'],selected=c['selected'],projection=c['traces'][-1]['projection'])))
if __name__=='__main__':main()
