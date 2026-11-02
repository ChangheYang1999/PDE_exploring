"""Publish fixed-counter transfer for the prospectively declared af2g policy."""
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.publish_extended_counter_game import norm
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/af2g_fixed_counters';NAME='af2g-fixed-counters-001'

def main():
 inputs={};digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 def read(p):inputs[str(p)]=digest(p);return json.loads(Path(p).read_text())
 def verify(mapping):
  for p,h in mapping.items():assert digest(p)==h,p;inputs[p]=h
 m=read(E/(NAME+'.json'));verify(m['input_sha256'])
 audits={k:read(R/(NAME+'-'+k+'.json')) for k in ('strict','replay','summary','data','fresh','old-replay')}
 s=audits['strict'];assert s['valid_conditions']==s['expected_conditions']==10 and s['attempt_counts']=={'valid':10} and not s['unresolved'] and not s['repeat_disagreements']
 for k in ('replay','old-replay'):assert audits[k]['all_passed'] and audits[k]['count']==10;verify(audits[k]['input_sha256']);verify(audits[k]['source_sha256'])
 assert audits['data']['all_passed'] and audits['summary']['identical_assignment_pairs']==5
 f=audits['fresh'];assert f['games']==10 and all(f[k] for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'));verify(f['input_sha256'])
 old={};counter_specs={o['id']:o['spec'] for o in m['opponents']};score={'W':1,'D':0,'L':-1}
 for item in m['reused_controls']:
  p=Path(item['result']);r=checked_row(str(p),inputs);freeze=read(p.parent.parent/'freeze.json');verify({str(p.parent.parent/'sources'/q):h for q,h in freeze['source_sha256'].items()})
  cond=r['condition'];is_candidate=item['target_role']=='candidate';side=cond['candidate_side'] if is_candidate else 1-cond['candidate_side']
  oldspec=cond['candidate_spec' if is_candidate else 'opponent_spec'];module=oldspec.partition(':')[0].replace('.','/')+'.py'
  assert freeze['source_sha256'][module]==m['control_sha256']
  oppspec=cond['opponent_spec' if is_candidate else 'candidate_spec'];assert norm(oppspec)==norm(counter_specs[item['opponent']])
  result=r['outcome'] if is_candidate else {'W':'L','D':'D','L':'W'}[r['outcome']]
  old[(item['opponent'],side)]=dict(result_path=str(p),outcome=result,hp=r['hp_candidate_first'][::1 if is_candidate else -1],rounds=r['rounds'])
 assert len(old)==10
 root=R/NAME;freeze=read(root/'freeze.json');verify({str(root/'sources'/q):h for q,h in freeze['source_sha256'].items()})
 cases=[];groups=defaultdict(list);counts=Counter();transitions=Counter()
 for job in read(root/'jobs.json'):
  r=checked_row(str(root/'results'/(job['id']+'.json')),inputs);c=r['condition'];key=(c['opponent_id'],c['candidate_side']);previous=old[key]
  assert norm(c['candidate_spec'])==norm(m['candidates'][0]['spec']) and norm(c['opponent_spec'])==norm(counter_specs[c['opponent_id']])
  item=dict(opponent=c['opponent_id'],candidate_side=c['candidate_side'],old=previous,new=r,outcome_gap=score[r['outcome']]-score[previous['outcome']]);cases.append(item);groups[c['opponent_id']].append(item)
  counts[r['outcome']]+=1;transitions[previous['outcome']+'->'+r['outcome']]+=1
 for pair in groups.values():
  assert len(pair)==2 and {x['candidate_side'] for x in pair}=={0,1}
  assert all(pair[0]['new'][k]==pair[1]['new'][k] for k in ('outcome','hp_candidate_first','rounds','canonical_replay_sha256'))
 assert f['checked_calls']==2*sum(x['new']['rounds'] for x in cases)
 h1=all(x['outcome_gap']>=0 for x in cases);h2=any(x['old']['outcome']=='L' and x['new']['outcome']!='L' for x in cases)
 now=datetime.now(timezone.utc).isoformat();times=[x['new']['decision_seconds_candidate_first'][0] for x in cases]
 metrics=dict(calls=sum(x['calls'] for x in times),total_seconds=sum(x['total'] for x in times),max_seconds=max(x['max'] for x in times))
 text=['# Fixed development counters against af2g','',f'Checked {now}.','',f'H1, no outcome regression from best_v9e: {"CONFIRMED" if h1 else "REFUTED"}. H2, at least one earlier loss becomes a draw or win: {"CONFIRMED" if h2 else "REFUTED"}. Ten new candidate outcomes: {dict(counts)}. Transitions from the ten old controls: {dict(transitions)}.','',
 'af2g is frozen best_v9f with passive_until=null. No other parameter was changed. These five counter specifications were fixed before the af2g games. Four were selected because they beat best_v9e, and the fifth, I, was a negative control that best_v9e beats. This targeted development screen is not a held-out test and does not evaluate the lead\'s wider R13 acceptance rule.','',
 '| Counter | Old best_v9e | Old HP | New af2g | New HP | End round |','|---|---|---|---|---|---:|']
 for name in ('D','G','H','I','guarded_R4_half'):
  row=groups[name][0];o=row['old'];n=row['new'];text.append(f'| {name} | {o["outcome"]} | {o["hp"][0]}:{o["hp"][1]} | {n["outcome"]} | {n["hp_candidate_first"][0]}:{n["hp_candidate_first"][1]} | {n["rounds"]} |')
 text += ['',f'Each row represents both physical assignments; the five new pairs have identical complete normalized histories. All ten new games pass strict condition accounting, original-engine replay, source/data archives, observation immutability, sequential action legality, and {f["checked_calls"]} freshly regenerated external decisions. All ten old records are separately replayed on the original engine and their frozen archives and original hashes are checked. Old games are reused, not counted again as new evidence. Zero submitted rejections, bot errors or source drift occurred in the new games.','',
 f'New candidate decision timing: {metrics["calls"]} actual calls, {metrics["total_seconds"]:.6f} seconds total, largest {metrics["max_seconds"]:.6f} seconds. These are observed timings on a shared machine, not worst-case bounds.','',
 'Reproduce using af2g-fixed-counters-001.json and the exact bounded commands recorded in runs/validation/af2g-fixed-counters-001-pipeline.log. Restored old replays retain their original hashes. Pool D and the installed entry point are not read by these policy executions. No result here establishes global optimality or robustness to arbitrary future opponents.','']
 output=A/'RESULTS.md'
 with output.open('x') as stream:stream.write('\n'.join(text))
 for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
 result=dict(time_utc=now,all_passed=True,h1_no_regression=h1,h2_repairs_old_loss=h2,new_games=10,reused_games=10,outcomes=dict(counts),transitions=dict(transitions),fresh_calls=f['checked_calls'],timing=metrics,cases=cases,input_sha256=inputs)
 atomic_json(A/'verification/full_games.json',result,exclusive=True)
 with Path('bot_research/notes/validation.md').open('a') as stream:stream.write(f'\n## {now}: af2g fixed-counter development check complete\n\nH1 no regression: {"CONFIRMED" if h1 else "REFUTED"}; H2 repair at least one old loss: {"CONFIRMED" if h2 else "REFUTED"}. Ten new outcomes {dict(counts)}, old-to-new transitions {dict(transitions)}. All ten old controls are replayed, and all {f["checked_calls"]} new external decisions regenerate exactly. Five identical assignment pairs, no errors or submitted rejections. Details: experiments/validation/analysis/af2g_fixed_counters/RESULTS.md. This is a selected development screen, not pool D or the complete R13 gate; no job reads installed best.py.\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('cases','input_sha256')}))
if __name__=='__main__':main()
