"""Publish the fixed, complete defensive-delegate development matrix."""
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
AREA=E/'analysis/delegated_defense';NAME='delegated-defense-001'
INVERSE={'W':'L','D':'D','L':'W'}

def main():
    inputs={}
    def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    def read(path):inputs[str(path)]=digest(path);return json.loads(path.read_text())
    manifest=read(E/(NAME+'.json'));assert manifest['expected_conditions']==36
    for path,sha in manifest['input_sha256'].items():assert digest(path)==sha,path
    audits={kind:read(R/(NAME+'-'+kind+'.json')) for kind in ('strict','replay','summary','data','histories','delegation')}
    assert audits['strict']['valid_conditions']==36 and audits['replay']['count']==36
    assert audits['replay']['all_passed'] and audits['data']['all_passed']
    summary=audits['summary'];history=audits['histories']
    assert audits['delegation']['all_passed'] and audits['delegation']['games']==36
    assert summary['valid_conditions']==36 and summary['unresolved_conditions']==0
    assert summary['complete_assignment_pairs']==summary['identical_assignment_pairs']==18
    assert not summary['repeat_disagreements']
    assert all(history[k] for k in ('all_fresh_actions_legal','all_observations_unchanged',
        'all_public_selections_verified','all_replayed','exact_counter_policy_reproduction'))
    for path,sha in history['input_sha256'].items():assert digest(path)==sha,path
    component=read(AREA/'verification/component.json');assert component['all_passed'] and component['components']==18
    controls=read(R/'delegated-defense-controls-001.json');assert controls['all_passed'] and len(controls['pairs'])==12
    assert all(pair['same_complete_trajectory'] for pair in controls['pairs'])
    totals=defaultdict(Counter);times=defaultdict(list);table=[];cells=[];prefixes=defaultdict(list)
    for case in history['cases']:
        checked=checked_row(case['result'],inputs);raw=read(Path(case['result']))
        times[case['condition']['opponent_id']].append(checked['decision_seconds_candidate_first'][1])
        prefix=[json.loads(line) for line in Path(raw['replay_path']).read_text().splitlines()][:10]
        for rec in prefix:rec.pop('match',None)
        prefixes[case['condition']['candidate_id'],case['condition']['candidate_side']].append(prefix)
    assert len(prefixes)==12 and all(len(group)==3 and group[0]==group[1]==group[2] for group in prefixes.values())
    for row in summary['rows']:
        values={(r['outcome'],tuple(r['hp']),r['rounds']) for r in row['results']}
        assert len(values)==1 and len(row['results'])==2
        outcome,hp,end=next(iter(values));outcome=INVERSE[outcome]
        totals[row['opponent']][outcome]+=2
        cases=[case for case in history['cases'] if case['condition']['candidate_id']==row['candidate']
               and case['condition']['opponent_id']==row['opponent']]
        assert len(cases)==2 and cases[0]['delegate_started']==cases[1]['delegate_started']
        trigger=cases[0]['delegate_started']
        cells.append(dict(target=row['candidate'],counter=row['opponent'],outcome=outcome,
                          hp_counter_first=list(reversed(hp)),rounds=end,delegate_started=trigger))
        table.append(f'| {row["candidate"]} | {row["opponent"]} | {outcome} | {hp[1]}:{hp[0]} | {end} | {trigger} |')
    successes=[mode for mode,counts in totals.items() if mode!='delegated_template' and counts['W']==12]
    verdict=('CONFIRMED' if successes else 'REFUTED')+': at least one frozen delegate wins all six focused target settings.'
    scores='; '.join(f'{mode}: {counts["W"]}W/{counts["D"]}D/{counts["L"]}L' for mode,counts in totals.items())
    timing={mode:dict(calls=sum(v['calls'] for v in values),sum_seconds=sum(v['total'] for v in values),maximum_seconds=max((v['max'] for v in values),default=0)) for mode,values in times.items()}
    fresh=sum(len(case['rounds']) for case in history['cases'])
    assert audits['delegation']['checked_calls']==fresh==sum(t['calls'] for t in timing.values())
    now=datetime.now(timezone.utc).isoformat()
    output=AREA/'RESULTS.md'
    text=f'''# Frozen defensive continuation results

Checked {now}.

{verdict}

Counter outcomes: {scores}.

All 36 games were declared after the 18 reached-state component checks and before any of these full games. Targets are the common-prefix baseline and tier1 flood, the three long-route delayed tier5 growers, and best_v9e. This is a focused development comparison after failures were diagnosed. Each row covers both physical assignments, which agree on the complete normalized history.

| Target | Counter continuation | Outcome | HP counter:target | Final round | Delegate starts |
|---|---|---|---|---:|---|
'''+ '\n'.join(table)+f'''

All 36 games pass strict accounting, original-engine replay, source/data checks and {fresh} fresh counter decisions. Observations are unchanged, all submitted actions are legal, and no bot error is recorded. All twelve template controls reproduce their earlier complete trajectories. For each target and assignment, all three variants have exactly the same recorded states and actions through round four after removing only the run identifier. A separate checker reconstructed every handoff trace using public states and original combat without importing the controller. The component check independently verified legal round-five actions and combat against the recorded simultaneous target action.

These results apply to starting the frozen defenders on the reached maps, with fresh legitimate state at handoff. They do not compare their ordinary round-one openings. The teammate planners may contain time limits; exact observed pair/control agreement is not a guarantee under arbitrary machine load. The verification receipt records measured counter call totals and maxima by mode.

Reproduction: use run_anonymous_development with delegated-defense-001.json, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives and check_delegated_histories. Compare controls with delegated-defense-controls-001.json. The original component command is check_delegated_component. Use the fixed project Python environment, disabled bytecode, research temporary directory, assigned affinity, one thread and low priority. All evidence is pinned by verification/full_games.json. This development result does not alter best_v9e or its final pool-C evidence.
'''
    with output.open('x') as handle:handle.write(text)
    for path in (output,AREA/'PROOF.md',AREA/'FULL_GAME_PLAN.md',Path(__file__).relative_to(Path.cwd())):inputs[str(path)]=digest(path)
    receipt=dict(time_utc=now,all_audits_passed=True,verdict=verdict,games=36,fresh_counter_decisions=fresh,
        component_cases=18,exact_template_controls=12,common_prefix_groups=12,counter_outcomes=dict(totals),
        counter_timing=timing,cells=cells,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as handle:json.dump(receipt,handle,indent=2,sort_keys=True);handle.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as handle:handle.write(f'\n## {now}: Frozen defenders after the common counter opening\n\n'
        f'Claim and verdict: {verdict}\n\nMethod: 36 declared games, three continuations, six focused targets, both assignments. '
        f'Result: {scores}. All {fresh} fresh counter decisions, 36 replays, 12 template controls and 12 three-way common-prefix groups '
        f'agree; no illegal actions or errors. Development only. Evidence: {output}.\n')
    print(json.dumps({key:value for key,value in receipt.items() if key not in ('cells','input_sha256')}))

if __name__=='__main__':main()
