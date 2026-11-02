"""Publish the declared projected-lead selector experiment after all audits."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import hashlib, json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation'); R=Path('bot_research/runs/validation')
A=E/'analysis/round4_public_projection'
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    inputs=[]; totals=defaultdict(Counter); cells={}; table=[]; calls=filtered=0
    for tag in 'abc':
        name=f'projection-selector-{tag}001'; m=E/(name+'.json'); inputs.append(m)
        declaration=json.loads(m.read_text()); assert declaration['expected_conditions']==48
        ds={}
        for kind in ('strict','replay','summary','data','histories'):
            p=R/f'{name}-{kind}.json'; inputs.append(p); ds[kind]=json.loads(p.read_text())
        assert ds['strict']['valid_conditions']==ds['strict']['expected_conditions']==48
        s,h=ds['summary'],ds['histories']
        assert s['valid_conditions']==s['expected_conditions']==48 and s['unresolved_conditions']==0
        assert s['complete_assignment_pairs']==s['identical_assignment_pairs']==24
        assert not s['repeat_disagreements']
        assert ds['replay']['all_passed'] and ds['replay']['count']==48 and ds['data']['all_passed']
        assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_public_selections_verified','all_replayed','exact_counter_policy_reproduction'))
        assert all(digest(p)==sha for p,sha in h['input_sha256'].items())
        for row in s['rows']:
            values={(x['outcome'],tuple(x['hp']),x['rounds']) for x in row['results']}
            assert len(row['results'])==2 and len(values)==1
            outcome,hp,rnd=next(iter(values))
            cs=[c for c in h['cases'] if c['condition']['candidate_id']==row['candidate'] and c['condition']['opponent_id']==row['opponent']]
            assert len(cs)==2
            selected={c['selected'] for c in cs}; assert len(selected)==1; selected=next(iter(selected))
            projections=[next(r['projection'] for r in c['rounds'] if r['round']==4) for c in cs]
            assert projections[0]==projections[1]
            q=projections[0]
            totals[row['opponent']][{'W':'L','L':'W','D':'D'}[outcome]]+=2
            cells[row['candidate'],row['opponent']]=dict(target_outcome=outcome,hp_target_first=hp,rounds=rnd,selected=selected,projection=q)
            table.append(f'| {row["candidate"]} | {row["opponent"]} | {selected} | {q["projected_lead"]} | {outcome} | {hp[0]}:{hp[1]} | {rnd} |')
        calls+=sum(len(c['rounds']) for c in h['cases'])
        filtered+=sum(len(c['early_filtered_proposals'])+len(c['growth_filtered_proposals']) for c in h['cases'])
    p=R/'projection-selector-controls-001.json'; inputs.extend((p,E/'projection-selector-control-pairs-001.json'))
    cmp=json.loads(p.read_text()); assert cmp['all_passed'] and len(cmp['pairs'])==96
    assert all(c['same_complete_trajectory'] for c in cmp['pairs'])
    assert all(digest(p)==sha for p,sha in cmp['input_sha256'].items())
    repaired=[t for t in ('P5M_poke0','P5M_poke2','P5M_poke3','P5M_poke4') if cells[t,'project_adaptive']['target_outcome']=='L']
    mistakes=[]
    for target in sorted({t for t,m in cells}):
        c=cells[target,'project_adaptive']; other='project_growth' if c['selected']=='early' else 'project_early'
        if c['target_outcome']=='W' and cells[target,other]['target_outcome']=='L':
            mistakes.append(dict(target=target,selected=c['selected'],hp_target_first=c['hp_target_first'],alternative=other,alternative_hp_target_first=cells[target,other]['hp_target_first']))
    verdict=('CONFIRMED' if len(repaired)==4 else 'REFUTED')+': the selector beats all four declared nominee opening-count variants.'
    robustness=('REFUTED' if mistakes else 'OPEN')+': a positive one-round projected lead suffices to select a winning complete policy.'
    scores='; '.join(f'{m}: {v["W"]}W/{v["D"]}D/{v["L"]}L' for m,v in totals.items())
    now=datetime.now(timezone.utc).isoformat()
    text=f'''# Round-four selection from a public HP projection

Checked {now}.

{verdict} {robustness}

Counter outcomes over forty-eight games per mode: {scores}.

The selector delays commitment to round four. It evaluates the proposed corner gun and tier4 against the visible enemy roster and map, assuming no new enemy actions that round. It chooses this early strike only when that calculation gives a positive surviving HP lead, and otherwise continues growth through round six and hands defense to the frozen fortress in round ten. The early branch uses joint wall/turret planning after taking a lead. Both branches have the same first three rounds.

The four changed-opening targets beaten by the adaptive mode are {', '.join(repaired) or 'none'}. Counterexamples where the selected policy loses but its alternative wins are recorded below. Changing the branch planner as well as the selection time means this is not a one-factor comparison with the previous exact-count selector.

'''+''.join(f'- `{m["target"]}`: selected {m["selected"]}, target-first HP {m["hp_target_first"]}; alternative {m["alternative"]}, target-first HP {m["alternative_hp_target_first"]}.\n' for m in mistakes)+'''
Every row below represents both physical assignments, with identical normalized histories. HP and outcomes are from the target's perspective, while projected lead is from the counter's perspective.

| Target | Counter | Selected branch | Projected lead | Target outcome | HP target:counter | Final round |
|---|---|---|---:|---|---|---:|
'''+ '\n'.join(table)+f'''

All144 full games pass strict accounting, original-engine action replay, source/data pinning and fresh policy regeneration. All{calls} freshly generated counter decisions reproduce; local wrappers filter{filtered} proposals before submission. There are no submitted illegal actions or bot errors. All72 assignment pairs and96 declared complete-history controls agree exactly. The controls comprise48 selected-branch comparisons and48 old growth-branch comparisons; they add no independent strength samples.

The separate48-prefix component check validates the local projection against an actual original-engine round with no new enemy action. That conditional result does not predict the opponent's hidden current purchase or later adaptation. The first component implementation double-subtracted mutable HP; it was corrected and rechecked before any of these full games, as documented in COMPONENT_CORRECTION.md.

All targets and opening variants were disclosed development conditions. The fixed branch and feature choices were informed by earlier failures. The growth delegate retains a three-second planner cutoff, so the observed exact reproducibility is not an unconditional load-independence claim. These development conditions were declared before the separate pool C validation began.

Reproduction: use the three declared manifests with run_data_development, followed by audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_projection_histories and compare_recorded_controls. Use the supplied Python environment from the project root, disabled bytecode, bot_research/tmp, assigned affinity, one thread and low priority. The campaign pipeline logs contain the exact commands.
'''
    q=A/'RESULTS.md'
    with q.open('x') as f: f.write(text)
    inputs.extend((q,A/'PROOF.md',A/'COMPONENT_CORRECTION.md',A/'verification/prefixes_corrected.json',Path(__file__).relative_to(Path.cwd())))
    atomic_json(A/'verification/full_games.json',dict(time_utc=now,all_passed=True,games=144,fresh_decisions=calls,local_filtered_proposals=filtered,identical_assignment_pairs=72,exact_control_pairs=96,counter_outcomes_by_mode=dict(totals),opening_variants_beaten=repaired,branch_selection_counterexamples=mistakes,input_sha256={str(p):digest(p) for p in inputs}),exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {now}: Projected-lead selector full experiment complete\n\nClaim and verdict: {verdict} {robustness}\n\nMethod and result:144 new development games,24 targets,three modes,both seats. Counter scores: {scores}. All{calls} fresh counter decisions reproduce, all72 seat pairs and96 predeclared control histories agree. All original-engine, source, data and legality audits pass. Wrong-branch witnesses: '+json.dumps(mistakes)+'. Full table experiments/validation/analysis/round4_public_projection/RESULTS.md. These are disclosed development conditions; the separately declared pool C validation is running.\n')
    print(json.dumps(dict(time_utc=now,games=144,calls=calls,scores=dict(totals),verdict=verdict,robustness=robustness)))
if __name__=='__main__': main()
