"""Publish all threshold-signal outcomes and the standalone branch controls."""
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/wall_signal_response'

def main():
 inputs={};digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 def read(p):inputs[str(p)]=digest(p);return json.loads(Path(p).read_text())
 def verify(mapping):
  for p,h in mapping.items():assert digest(p)==h,p;inputs[p]=h
 d=read(E/'wall-signal-campaigns-001.json');verify(d['input_sha256']);c=read(A/'verification/components.json');assert c['all_passed'] and len(c['cases'])==12;verify(c['input_sha256'])
 rows=[];groups=defaultdict(list);fresh=extra=0
 for item in d['campaigns']:
  name=item['name'];count=item['wall_count'];root=R/name
  audits={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','summary','data','fresh','forecasts')}
  s=audits['strict'];assert s['valid_conditions']==s['expected_conditions']==6 and s['attempt_counts']=={'valid':6} and not s['unresolved'] and not s['repeat_disagreements']
  assert audits['summary']['identical_assignment_pairs']==3 and audits['replay']['all_passed'] and audits['replay']['count']==6 and audits['data']['all_passed']
  for k in ('fresh','forecasts'):
   a=audits[k];assert all(a[x] for x in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'));verify(a['input_sha256'])
  fresh+=audits['fresh']['checked_calls'];extra+=audits['forecasts']['checked_calls'];fc={x['result_path']:x for x in audits['forecasts']['cases']}
  freeze=read(root/'freeze.json');verify({str(root/'sources'/p):h for p,h in freeze['source_sha256'].items()})
  for job in read(root/'jobs.json'):
   path=str(root/'results'/(job['id']+'.json'));r=checked_row(path,inputs);target=r['condition']['opponent_id'];trace=fc[path]['rounds'];attacks=[x for x in trace if x['attack_count']]
   row=dict(wall_count=count,target=target,record=r,attack_count=attacks[0]['attack_count'] if attacks else 0,model_mismatch_rounds=[x['round'] for x in trace if not x['model_matches']]);rows.append(row);groups[(count,target)].append(row)
 assert len(rows)==12 and fresh==2*extra
 for pair in groups.values():
  assert len(pair)==2 and {x['record']['condition']['candidate_side'] for x in pair}=={0,1}
  assert all(pair[0]['record'][k]==pair[1]['record'][k] for k in ('outcome','hp_candidate_first','rounds','canonical_replay_sha256'))
 score={'W':1,'D':0,'L':-1};one=lambda count,target:groups[(count,target)][0]
 same20=one(20,'J')['record']['canonical_replay_sha256']==one(20,'H')['record']['canonical_replay_sha256']
 same19=one(19,'J')['record']['canonical_replay_sha256']==one(19,'I')['record']['canonical_replay_sha256']
 h1=one(20,'J')['record']['outcome']=='W' and same20
 h2=score[one(20,'J')['record']['outcome']]>score[one(19,'J')['record']['outcome']] and score[one(20,'J')['record']['outcome']]>score[one(20,'I')['record']['outcome']]
 now=datetime.now(timezone.utc).isoformat()
 text=['# Manipulating the public response signal','',f'Checked {now}.','',f'H1, twenty-wall attacker wins against J with exactly the H response history: {"CONFIRMED" if h1 else "REFUTED"}. H2, that win exceeds both the nineteen-wall J result and the same twenty-wall attacker against I: {"CONFIRMED" if h2 else "REFUTED"}.','',
 'Each attacker advances its private H model from round one, replaces only its first factory action list with a prefix of the existing guard00 wall witness and affordable factories, then uses the fixed round-three tier2 timing policy. K19 and K20 differ by one wall. J selects H for K20 and I for K19. This criterion was deliberately targeted after inspecting J, so all games are development evidence.','',
 '| Walls | Opponent | Attacker outcome | HP attacker:opponent | End round | Tier2 purchases | Forecast mismatch rounds |','|---:|---|---|---|---:|---:|---|']
 for count in (19,20):
  for target in ('J','H','I'):
   x=one(count,target);r=x['record'];text.append(f'| {count} | {target} | {r["outcome"]} | {r["hp_candidate_first"][0]}:{r["hp_candidate_first"][1]} | {r["rounds"]} | {x["attack_count"]} | {len(x["model_mismatch_rounds"])} |')
 text += ['',f'All twelve full games pass source/data archives, strict condition accounting, original-engine replay, legality and observation checks, {fresh} fresh external decisions and {extra} additional attacker/forecast checks. Twelve prefix cases were checked first. Each displayed row represents two physical assignments with identical complete canonical histories. No rejected submissions, bot errors or source drift occurred.','',f'The complete K20-J history equals K20-H: {same20}. The complete K19-J history equals K19-I: {same19}. These matched fixed-response controls separate the chosen response from a comparison that changes wall geometry alone. A nineteen-versus-twenty-wall outcome difference by itself would not identify response selection as the cause, because walls also change cost and path.','',
 'A successful attack would show only that this public threshold can be induced to choose an exploitable branch. It would not show that public-history adaptation is generally harmful or that either fixed response is globally superior. J already loses to B in the earlier finite table. This is a specific failure mechanism, not its first counterexample.','',
 'Full conditions, timings, traces and hashes are in verification/full_games.json and the two wall-signal manifests. Reproduce with the bounded commands in runs/validation/wall-signal-001-pipeline.log. Pool D and the installed final entry point are not used.','']
 output=A/'RESULTS.md'
 with output.open('x') as stream:stream.write('\n'.join(text))
 for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
 result=dict(time_utc=now,all_passed=True,new_games=12,h1=h1,h2=h2,same_K20_J_H=same20,same_K19_J_I=same19,fresh_calls=fresh,forecast_checks=extra,rows=rows,input_sha256=inputs)
 atomic_json(A/'verification/full_games.json',result,exclusive=True)
 with Path('bot_research/notes/validation.md').open('a') as stream:stream.write(f'\n## {now}: Public wall-signal attack complete\n\nH1, K20 wins against J on the exact H-response history: {"CONFIRMED" if h1 else "REFUTED"}. H2, it exceeds K19-J and K20-I: {"CONFIRMED" if h2 else "REFUTED"}. Twelve new games, six identical assignment pairs, {fresh} fresh external decisions and {extra} forecast checks pass. K20-J equals K20-H: {same20}; K19-J equals K19-I: {same19}. Complete outcomes and limitations: experiments/validation/analysis/wall_signal_response/RESULTS.md. This deliberately selected signal attack uses no pool D data.\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('rows','input_sha256')}))
if __name__=='__main__':main()
