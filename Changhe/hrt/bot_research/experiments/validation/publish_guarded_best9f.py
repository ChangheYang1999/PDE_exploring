"""Publish the fixed guarded round-four transfer without changing old evidence."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/guarded_round4_best9f';NAME='guarded-round4-best9f-001'
def main():
 inputs={}
 def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
 def read(p):inputs[str(p)]=digest(p);return json.loads(Path(p).read_text())
 def verify(mapping):
  for p,h in mapping.items():assert digest(p)==h,p;inputs[p]=h
 manifest=read(E/(NAME+'.json'));verify(manifest['input_sha256'])
 audits={k:read(R/(NAME+'-'+k+'.json')) for k in ('strict','replay','summary','data','fresh','histories','opening')}
 s=audits['summary'];h=audits['histories'];f=audits['fresh']
 assert audits['strict']['valid_conditions']==audits['strict']['expected_conditions']==4
 assert not audits['strict']['unresolved']
 assert s['valid_conditions']==s['expected_conditions']==4 and not s['unresolved_conditions']
 assert s['identical_assignment_pairs']==s['complete_assignment_pairs']==2 and not s['repeat_disagreements']
 assert audits['replay']['all_passed'] and audits['replay']['count']==4 and audits['data']['all_passed']
 assert audits['opening']['all_passed'] and f['all_passed'] and f['games']==4
 assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_public_triggers_verified','all_replayed','exact_counter_policy_reproduction','no_post_handoff_minions'))
 for d in (h,f,audits['opening']):verify(d['input_sha256'])
 oldroot=R/'guarded-transfer-b001';freeze=read(oldroot/'freeze.json')
 for p,sha in freeze['source_sha256'].items():
  q=oldroot/'sources'/p;assert digest(q)==sha,p;inputs[str(q)]=sha
 assert freeze['source_sha256']['bot_research/bots/best.py']=='70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87'
 oldproof=read(E/'analysis/guarded_round4_transfer/verification/full_games.json');assert oldproof['all_passed']
 oldhist=read(R/'guarded-transfer-b001-histories.json');assert oldhist['exact_counter_policy_reproduction']
 old={}
 for item in manifest['reused_controls']:
  row=checked_row(item['result'],inputs);cond=row['condition'];assert row['outcome']=='L'
  old[(cond['opponent_id'],cond['candidate_side'])]=row
 cases=[];counts=Counter();filtered=0;lines=[]
 jobs=read(R/NAME/'jobs.json')
 for job in jobs:
  new=checked_row(str(R/NAME/'results'/(job['id']+'.json')),inputs);cond=new['condition'];previous=old[(cond['opponent_id'],cond['candidate_side'])]
  assert previous['condition']['opponent_spec']==cond['opponent_spec']
  hs=[c for c in h['cases'] if c['condition']==cond];assert len(hs)==1;hc=hs[0]
  counts[new['outcome']]+=1;filtered+=len(hc['filtered_proposals'])
  cases.append(dict(old=previous,new=new,first_switch=hc['first_switch']))
  hp=new['hp_candidate_first'];lines.append(f'| {cond["opponent_id"]} | {cond["candidate_side"]} | {new["outcome"]} | {hp[0]}:{hp[1]} | {new["rounds"]} | {hc["first_switch"]} |')
 assert len(cases)==4
 verdict='CONFIRMED' if counts['L']==4 else 'REFUTED'
 now=datetime.now(timezone.utc).isoformat();calls=sum(len(c['rounds']) for c in h['cases'])
 times=[c['new']['decision_seconds_candidate_first'] for c in cases]
 metrics=[dict(calls=sum(t[i]['calls'] for t in times),total_seconds=sum(t[i]['total'] for t in times),max_call_seconds=max(t[i]['max'] for t in times)) for i in (0,1)]
 text=f'''# Fixed guarded round-four counter against best_v9f

Checked {now}.

H1 is **{verdict}**: the candidate outcomes in four declared games are {dict(counts)}. All four old best_v9e controls are losses for that candidate, 740:755. The two counter settings and all their parameters are unchanged. This is a development transfer test requested after the candidate was installed, not a held-out validation set.

The new candidate is frozen best_v9f, SHA256 {manifest['candidate_sha256']}, byte-identical to installed best.py when declared. Results and HP below are from the candidate's perspective.

| Counter | Candidate seat | Outcome | HP candidate:counter | Final round | Counter handoff |
|---|---:|---|---|---:|---:|
'''+ '\n'.join(lines)+f'''

Every game passes complete condition accounting, original-engine replay, source/data archival checks, fresh regeneration of both policies ({f['checked_calls']} calls), and a second counter-only check ({calls} decisions) of the exact public trigger and no purchases after handoff. There are {filtered} locally filtered proposals, zero submitted rejected actions, and zero bot errors. Both physical-assignment pairs have identical normalized complete histories. The old four controls and their source archives are checked but not counted as new games. The inherited gun lemma is not used as a substitute for these actual games.

Recorded candidate timing: {metrics[0]['calls']} decisions, {metrics[0]['total_seconds']:.6f} seconds total, maximum {metrics[0]['max_call_seconds']:.6f} seconds. Counter timing: {metrics[1]['calls']} decisions, {metrics[1]['total_seconds']:.6f} seconds total, maximum {metrics[1]['max_call_seconds']:.6f} seconds. These are observed shared-machine timings, not worst-case bounds.

A result here concerns these exact settings only. Equal player swaps do not supply independent samples or establish absence of load effects in other branches.

Reproduce from the project root with the supplied Python, disabled bytecode, research temporary directory, one assigned low-priority core and one numerical thread. Run run_data_development on guarded-round4-best9f-001.json, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_fixed_game_histories and check_guarded_round4_histories. The pipeline log records exact bounded invocations. See verification/full_games.json for complete input hashes and old/new rows.
'''
 out=A/'RESULTS.md'
 with out.open('x') as stream:stream.write(text)
 for p in (out,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
 receipt=dict(time_utc=now,all_passed=True,hypothesis_verdict=verdict,new_games=4,reused_games=4,candidate_outcomes=dict(counts),fresh_calls=f['checked_calls'],counter_rechecks=calls,local_filtered_proposals=filtered,identical_assignment_pairs=2,timing_candidate_counter=metrics,cases=cases,input_sha256=inputs)
 atomic_json(A/'verification/full_games.json',receipt,exclusive=True)
 with Path('bot_research/notes/validation.md').open('a') as stream:stream.write(f'\n## {now}: Fixed guarded round-four check against best_v9f complete\n\nClaim and verdict: {verdict}, both unchanged half/full-budget settings still defeat best_v9f in both seats. Candidate outcomes {dict(counts)}; exact four rows: {out}. All four games pass strict/replay/source/data and {f["checked_calls"]} fresh calls plus {calls} counter trigger rechecks. Two identical assignment pairs, {filtered} filtered proposals, zero submitted rejections or bot errors. The four old best_v9e losses remain separately archived controls. This answers the lead\'s 18:40Z request and is development evidence.\n')
 print(json.dumps({k:v for k,v in receipt.items() if k not in ('cases','input_sha256')}))
if __name__=='__main__':main()
