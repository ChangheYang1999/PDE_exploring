"""Publish finite public-selector comparisons after all independent audits."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import argparse, hashlib, json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation'); R=Path('bot_research/runs/validation')
def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser(); p.add_argument('--pool',choices=('targets','baselines'),required=True); args=p.parse_args()
 targets=args.pool=='targets'; stem='public-selector' if targets else 'selector-baselines'
 A=E/'analysis'/('public_roster_selector' if targets else 'public_selector_baselines')
 inputs=[];rows=[];totals=defaultdict(Counter);calls=filtered=games=pairs=0;selected_counts=Counter()
 for tag in 'abc':
  name=f'{stem}-{tag}001'; m=E/(name+'.json'); inputs.append(m); expected=json.loads(m.read_text())['expected_conditions'];ds={}
  for kind in ('strict','replay','summary','data','histories','opening'):
   q=R/f'{name}-{kind}.json';inputs.append(q);ds[kind]=json.loads(q.read_text())
  s,h=ds['summary'],ds['histories']
  assert ds['strict']['valid_conditions']==ds['strict']['expected_conditions']==expected
  assert s['valid_conditions']==s['expected_conditions']==expected and s['unresolved_conditions']==0
  assert s['complete_assignment_pairs']==s['identical_assignment_pairs']==expected//2 and not s['repeat_disagreements']
  assert ds['replay']['all_passed'] and ds['replay']['count']==expected and ds['data']['all_passed'] and ds['opening']['all_passed']
  assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_public_selections_verified','all_replayed','exact_counter_policy_reproduction'))
  assert all(digest(path)==sha for path,sha in h['input_sha256'].items())
  for row in s['rows']:
   values={(r['outcome'],tuple(r['hp']),r['rounds']) for r in row['results']};assert len(row['results'])==2 and len(values)==1
   outcome,hp,rnd=next(iter(values));cs=[c for c in h['cases'] if c['condition']['candidate_id']==row['candidate'] and c['condition']['opponent_id']==row['opponent']]
   selections={c['selected'] for c in cs};assert len(cs)==2 and len(selections)==1
   selected=next(iter(selections));counts={next((r['first_round_tier1_count'] for r in c['rounds'] if r['round']==2),None) for c in cs};assert len(counts)==1
   count=next(iter(counts));mode=row['opponent'].removeprefix('select_')
   rows.append(f'| {row["candidate"]} | {mode} | {selected} | {count} | {outcome} | {hp[0]}:{hp[1]} | {rnd} |')
   totals[mode][{'W':'L','L':'W','D':'D'}[outcome]]+=2
   if mode=='adaptive':selected_counts[selected]+=2
  calls+=sum(len(c['rounds']) for c in h['cases']);filtered+=sum(len(c['early_filtered_proposals'])+len(c['growth_filtered_proposals']) for c in h['cases']);games+=expected;pairs+=expected//2
 q=R/f'{stem}-controls-001.json';cmp=json.loads(q.read_text());inputs.extend((q,E/f'{stem}-control-pairs-001.json'))
 expected_controls=32 if targets else 24
 assert cmp['all_passed'] and len(cmp['pairs'])==expected_controls and all(c['same_complete_trajectory'] for c in cmp['pairs'])
 assert all(digest(path)==sha for path,sha in cmp['input_sha256'].items())
 def score(c):return 2*c['W']+c['D']
 better=all(score(totals['adaptive'])>score(totals[m]) for m in ('early','growth'))
 verdict=('CONFIRMED' if better else 'REFUTED')+': the adaptive selector scores strictly more wins plus half draws than either fixed branch on this finite set.'
 now=datetime.now(timezone.utc).isoformat();scores='; '.join(f'{m} {totals[m]["W"]}W/{totals[m]["D"]}D/{totals[m]["L"]}L' for m in ('adaptive','early','growth'))
 text=f'''# Public first-roster selection: {args.pool}

Checked {now}.

{verdict} Counter outcomes: {scores}. The selected branch is early in{selected_counts['early']} games and growth in{selected_counts['growth']} games.

Every table row represents both assignments. Outcome and HP below are from the target perspective, opposite to the counter totals above.

| Target | Mode | Selected branch | First-round tier1 count | Target outcome | HP target:counter | Final round |
|---|---|---|---:|---|---|---:|
'''+ '\n'.join(rows)+f'''

All{games} declared games pass strict accounting, unchanged-engine replay, immutable source/data verification, public-selection checks and fresh policy regeneration. There are{calls} exactly reproduced decisions and{filtered} locally filtered proposals. No invalid action or bot error is submitted. All{pairs} normalized assignment pairs match, and all{expected_controls} declared complete-history comparisons pass. The adaptive histories equal those of their selected forced branch. For the eight-target experiment the other16 comparisons reproduce the earlier guarded-strike policy exactly.

The feature and threshold were chosen from development histories, and all opponents here are known development policies. This is a finite matched comparison, not an estimate of a population win rate. Equality of repeated decisions was checked empirically because the growth branch and some targets retain wall-clock planner cutoffs. No improvement outside the stated set follows. The selector commits permanently after round1; it can be misled by an opponent that changes its later behavior. Pool C remains unused.

Reproduction: use each{stem} manifest with run_data_development; run the strict, replay, summary, data and check_public_selector_histories audits; then compare_recorded_controls with{stem}-control-pairs-001.json. Run from the project root with the supplied Python environment, bytecode disabled, bot_research/tmp, one thread, assigned affinity and low priority.

Audit inputs:

'''+ '\n'.join(f'- `{q}`.' for q in inputs)+'\n'
 q=A/'RESULTS.md'
 with q.open('x') as f:f.write(text)
 inputs.extend((q,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())))
 atomic_json(A/'verification/full_games.json',dict(time_utc=now,all_passed=True,input_sha256={str(q):digest(q) for q in inputs},games=games,fresh_decisions=calls,local_filtered_proposals=filtered,identical_assignment_pairs=pairs,exact_control_pairs=expected_controls,counter_outcomes_by_mode=dict(totals),scope=verdict),exclusive=True)
 with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Public selector {args.pool} complete\n\nClaim and verdict: {verdict}\n\nMethod and result: {games} declared standard games, all independent audits pass; {calls} fresh decisions,{pairs} identical seat pairs and{expected_controls} exact complete-history controls. Counter totals: {scores}. Details experiments/validation/analysis/{A.name}/RESULTS.md. This is a development comparison; pool C remains unused.\n')
 print(json.dumps(dict(time_utc=now,games=games,calls=calls,totals=dict(totals),verdict=verdict)))
if __name__=='__main__':main()
