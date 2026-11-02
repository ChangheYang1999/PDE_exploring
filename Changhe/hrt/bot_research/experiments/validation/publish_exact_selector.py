"""Publish exact-count repair and adversarial opening comparisons."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter,defaultdict
import argparse,hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--kind',choices=('exact','spoof'),required=True);args=p.parse_args()
 exact=args.kind=='exact';stem='exact-selector' if exact else 'roster-spoof';A=E/'analysis'/('exact_roster_selector' if exact else 'roster_feature_spoof')
 names=[f'{stem}-{tag}001' for tag in 'abc'] if exact else ['roster-spoof-001']
 inputs=[];rows=[];cells={};totals=defaultdict(Counter);games=calls=filtered=pairs=0
 for name in names:
  m=E/(name+'.json');inputs.append(m);expected=json.loads(m.read_text())['expected_conditions'];ds={}
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
   values={(x['outcome'],tuple(x['hp']),x['rounds']) for x in row['results']};assert len(row['results'])==2 and len(values)==1
   outcome,hp,rnd=next(iter(values));cs=[c for c in h['cases'] if c['condition']['candidate_id']==row['candidate'] and c['condition']['opponent_id']==row['opponent']];assert len(cs)==2
   selections={c['selected'] for c in cs};assert len(selections)==1;selected=next(iter(selections))
   counts={next((r['first_round_tier1_count'] for r in c['rounds'] if r['round']==2),None) for c in cs};assert len(counts)==1;count=next(iter(counts))
   rows.append(f'| {row["candidate"]} | {row["opponent"]} | {count} | {selected} | {outcome} | {hp[0]}:{hp[1]} | {rnd} |')
   totals[row['opponent']][{'W':'L','L':'W','D':'D'}[outcome]]+=2
   cells[row['candidate'],row['opponent']]=dict(outcome=outcome,hp=hp,rounds=rnd,selected=selected,count=count)
  games+=expected;pairs+=expected//2;calls+=sum(len(c['rounds']) for c in h['cases']);filtered+=sum(len(c['early_filtered_proposals'])+len(c['growth_filtered_proposals']) for c in h['cases'])
 q=R/f'{stem}-controls-001.json';cmp=json.loads(q.read_text());inputs.extend((q,E/f'{stem}-control-pairs-001.json'));controls=40 if exact else 22
 assert cmp['all_passed'] and len(cmp['pairs'])==controls and all(c['same_complete_trajectory'] for c in cmp['pairs'])
 assert all(digest(path)==sha for path,sha in cmp['input_sha256'].items())
 scores='; '.join(f'{mode} {v["W"]}W/{v["D"]}D/{v["L"]}L' for mode,v in totals.items())
 if exact:
  assert dict(totals['select_exact'])==dict(W=32,D=8)
  verdict='CONFIRMED: the exact-count predicate repairs the rush_t1 loss and preserves the selected branch histories on the other nineteen development targets.'
  detail='The forty new games score32W/8D/0L. The old threshold selector scored30W/8D/2L across the same twenty targets. Fixed early play scored24W/0D/16L and fixed growth30W/8D/2L. Every new history matches its predeclared old forced-branch control exactly. Those controls are reused evidence, not forty further independent samples. The repair was chosen after observing the old rush_t1 failure.'
 else:
  witnesses=[]
  for target in sorted({a for a,b in cells}):
   for mode in ('select_adaptive','select_exact'):
    c=cells[target,mode];alternative='select_growth' if c['selected']=='early' else 'select_early';other=cells[target,alternative]
    if c['outcome']=='W' and other['outcome']=='L':witnesses.append(dict(target=target,selector=mode,selected=c['selected'],hp_target_first=c['hp'],alternative=alternative,alternative_hp_target_first=other['hp']))
  verdict=('CONFIRMED' if witnesses else 'REFUTED')+': a declared change of opening count makes a selector lose while its alternative fixed branch wins.'
  detail='Qualifying controlled counterexamples: '+json.dumps(witnesses,sort_keys=True)+'. Each adaptive history matches its selected forced branch, and all six count3 default-control histories reproduce the earlier nominee experiment. The opening changes also change income and damage; the claim is the measured complete-policy comparison, not a pure isolated effect of the displayed count.'
 now=datetime.now(timezone.utc).isoformat()
 text=f'''# {'Exact-count selector repair' if exact else 'Adversarial first-round roster changes'}

Checked {now}.

{verdict}

Counter outcomes: {scores}.

Every row represents both physical assignments. The table gives target outcomes and target-first HP.

| Target | Counter | First-round tier1 | Selected branch | Target outcome | HP target:counter | Final round |
|---|---|---:|---|---|---|---:|
'''+ '\n'.join(rows)+f'''

{detail}

All{games} declared games pass strict accounting, original-engine replay, pinned source/data checks and fresh selector regeneration. All{calls} decisions reproduce exactly; the wrappers locally filter{filtered} proposals, and no invalid action or bot error is submitted. All{pairs} normalized seat pairs and{controls} complete-history controls match. These are development conditions. The growth planner retains a wall-clock cutoff, so exact repeatability is measured here rather than assumed for arbitrary machine load. Pool C remains unused.

Reproduction uses the declared manifests with run_data_development, the standard strict/replay/source/data audits, check_roster_selector_opening, check_roster_selector_histories and compare_recorded_controls. Run from the project root with the supplied Python environment, bytecode disabled, bot_research/tmp, one thread, assigned affinity and low priority.

Audit inputs:

'''+ '\n'.join(f'- `{q}`.' for q in inputs)+'\n'
 q=A/'RESULTS.md'
 with q.open('x') as f:f.write(text)
 inputs.extend((q,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())))
 if exact:
  for name in ('public_roster_selector','public_selector_baselines'):inputs.append(E/'analysis'/name/'verification/full_games.json')
 atomic_json(A/'verification/full_games.json',dict(time_utc=now,all_passed=True,input_sha256={str(q):digest(q) for q in inputs},games=games,fresh_decisions=calls,local_filtered_proposals=filtered,identical_assignment_pairs=pairs,exact_control_pairs=controls,counter_outcomes_by_mode=dict(totals),scope=verdict),exclusive=True)
 with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: {args.kind} roster-selection experiment complete\n\nClaim and verdict: {verdict}\n\nMethod and result: {games} new standard games, all audits pass, {calls} fresh decisions,{pairs} matching assignment pairs and{controls} exact history controls. {detail} Full table: experiments/validation/analysis/{A.name}/RESULTS.md. Pool C remains unused.\n')
 print(json.dumps(dict(time_utc=now,games=games,calls=calls,totals=dict(totals),verdict=verdict)))
if __name__=='__main__':main()
