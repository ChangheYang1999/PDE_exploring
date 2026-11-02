"""Publish the fully audited, predeclared triggered-timing experiment."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation'); R=Path('bot_research/runs/validation'); A=E/'analysis/triggered_budget_timing'
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    inputs=[]; rows=[]; calls=filtered=0; outcomes=Counter()
    for tag in 'ab':
        name=f'triggered-timing-{tag}001'; ds={}
        for kind in ('strict','replay','summary','data','histories','opening'):
            p=R/f'{name}-{kind}.json'; inputs.append(p); ds[kind]=json.loads(p.read_text())
        s,h=ds['summary'],ds['histories']
        assert ds['strict']['valid_conditions']==ds['strict']['expected_conditions']==16
        assert s['valid_conditions']==s['expected_conditions']==16 and s['unresolved_conditions']==0
        assert not s['repeat_disagreements'] and s['identical_assignment_pairs']==s['complete_assignment_pairs']==8
        assert ds['replay']['all_passed'] and ds['replay']['count']==16 and ds['data']['all_passed'] and ds['opening']['all_passed']
        assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_public_triggers_verified','all_replayed','exact_counter_policy_reproduction','no_post_handoff_minions'))
        for p,sha in h['input_sha256'].items(): assert digest(p)==sha,p
        for row in s['rows']:
            values={(x['outcome'],tuple(x['hp']),x['rounds']) for x in row['results']}; assert len(row['results'])==2 and len(values)==1
            outcome,hp,rnd=next(iter(values))
            cs=[c for c in h['cases'] if c['condition']['candidate_id']==row['candidate'] and c['condition']['opponent_id']==row['opponent']]
            switches={c['first_switch'] for c in cs}; assert len(cs)==2 and len(switches)==1
            switch=next(iter(switches)); switch='none' if switch is None else str(switch)
            rows.append(f'| {row["candidate"]} | {row["opponent"]} | {outcome} | {hp[0]}:{hp[1]} | {rnd} | {switch} |')
        calls+=sum(len(c['rounds']) for c in h['cases']); filtered+=sum(len(c['filtered_proposals']) for c in h['cases']); outcomes.update(s['outcomes']); inputs.append(E/f'{name}.json')
    assert (calls,filtered)==(692,288) and outcomes=={'W':24,'L':8}
    now=datetime.now(timezone.utc).isoformat()
    verdict='REFUTED: one of these eight fixed timing and budget settings beats both nominees. CONFIRMED: the round-six and round-seven variants beat P4TNUB, but neither beats P5TNUBM.'
    text=f'''# Earlier and later triggered strikes

Checked {now}.

{verdict}

Each row represents two matching physical assignments. Outcomes and HP are from the target perspective. The handoff is the first actual HP-triggered switch, which can be later than its eligibility round.

| Target | Counter | Target outcome | HP target:counter | Final round | Handoff |
|---|---|---|---|---:|---:|
'''+ '\n'.join(rows)+f'''

Both nominees beat the unguarded round-four strike. It lands for 60 damage, but the counter fails to preserve its own HP lead and never switches to its defensive policy. At the reached 291-gold decision, a tier4 costs 260 and the intended splash guard costs 60, so both cannot be purchased. This is a specific cash constraint, not a proof that every round-four strike must fail.

The round-six strike against P4TNUB does not trigger handoff at its earliest eligible round 7; the lead appears at round 9. The round-seven strike triggers at round 8. Both preserve a win to round 50. Neither later strike wins against P5TNUBM. The half- and full-budget versions agree on each listed outcome and final HP, but are retained as separate declared policies.

All 32 games pass strict accounting, full original-engine replay and source/data archive checks. All 16 assignment pairs have identical normalized histories. Fresh controllers reproduce all {calls} decisions with unchanged observations, independently verified public triggers and legal actions. There are {filtered} locally filtered parent proposals, no submitted invalid actions and no bot errors. The prefix checks were completed before each full campaign. These are development results, not independent samples from a policy population. No pool C condition was used.

Reproduction uses the two triggered-timing manifests with run_data_development, followed by audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives and check_triggered_budget_histories. Run from the project root with .venv/bin/python -B, bytecode disabled, temporary files under bot_research/tmp, low priority, one thread and assigned affinity.

Audit inputs:

'''+ '\n'.join(f'- `{p}`.' for p in inputs)+'\n'
    (A/'verification').mkdir(exist_ok=True); result=A/'RESULTS.md'
    with result.open('x') as f:f.write(text)
    inputs += [result,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())]
    atomic_json(A/'verification/full_games.json',dict(time_utc=now,all_passed=True,input_sha256={str(p):digest(p) for p in inputs},games=32,fresh_decisions=calls,local_filtered_proposals=filtered,identical_assignment_pairs=16,target_outcomes=dict(outcomes),scope=verdict),exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Unguarded timing alone does not beat both nominees\n\nClaim and verdict: {verdict}\n\nMethod and result: 32 predeclared standard games, all strict/replay/source/data checks passed, 692 freshly regenerated decisions and 16 matching assignment pairs. P4TNUB 8W/8L, P5TNUBM 16W. The round-four strike lands but loses its own lead; later P4 wins are counter HP755 against target520 or660. Full table: experiments/validation/analysis/triggered_budget_timing/RESULTS.md. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now,games=32,published=str(result))))
if __name__=='__main__': main()
