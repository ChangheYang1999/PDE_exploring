"""Publish the audited six-target public-HP-triggered budget matrix."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/triggered_budget_handoff'

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    now=datetime.now(timezone.utc).isoformat();inputs=[];rows=[];calls=filtered=count=pairs=0;outcomes=Counter();by_target={}
    for tag in 'abc':
        prefix=R/f'triggered-budget-{tag}001';ds={}
        for kind in ('strict','replay','summary','data','histories'):
            path=Path(f'{prefix}-{kind}.json');ds[kind]=json.loads(path.read_text());inputs.append(path)
        s,h=ds['summary'],ds['histories']
        assert ds['strict']['valid_conditions']==ds['strict']['expected_conditions']==16
        assert s['valid_conditions']==s['expected_conditions']==16 and s['unresolved_conditions']==0
        assert not s['repeat_disagreements']
        assert s['identical_assignment_pairs']==s['complete_assignment_pairs']==8
        assert ds['replay']['all_passed'] and ds['replay']['count']==16 and ds['data']['all_passed']
        assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_replayed',
            'exact_counter_policy_reproduction','no_post_handoff_minions','all_public_triggers_verified'))
        for path,sha in h['input_sha256'].items():assert digest(path)==sha,path
        for row in s['rows']:
            values={(x['outcome'],tuple(x['hp']),x['rounds']) for x in row['results']}
            assert len(row['results'])==2 and len(values)==1
            outcome,hp,rnd=next(iter(values))
            cs=[c for c in h['cases'] if c['condition']['candidate_id']==row['candidate'] and c['condition']['opponent_id']==row['opponent']]
            switches={c['first_switch'] for c in cs};assert len(cs)==2 and len(switches)==1
            switch=next(iter(switches));switch='none' if switch is None else str(switch)
            rows.append(f'| {row["candidate"]} | {row["opponent"]} | {outcome} | {hp[0]}:{hp[1]} | {rnd} | {switch} |')
            by_target.setdefault(row['candidate'],Counter()).update({outcome:2})
        calls+=sum(len(c['rounds']) for c in h['cases']);filtered+=sum(len(c['filtered_proposals']) for c in h['cases'])
        count+=16;pairs+=8;outcomes.update(s['outcomes']);inputs.append(E/f'triggered-budget-{tag}001.json')
    opening=R/'triggered-budget-opening-001.json';assert json.loads(opening.read_text())['all_passed'];inputs.append(opening)
    assert (count,calls,filtered,pairs)==(48,1426,312,24)
    assert outcomes=={'W':32,'L':12,'D':4}
    verdict=('CONFIRMED: the no-strike HP-triggered budget defender beats P4TNUB and best_v9e, '
        'while its one-tier4 variant beats P5TNUBM. REFUTED: one of these four fixed counter '
        'settings beats all six targets, or adding the HP trigger repairs transfer of the '
        'previous one-strike fixed-handoff counter to any of the five transfer targets.')
    text=f'''# Public HP switching produces complementary counters

Checked {now}.

{verdict}

Each row represents both physical assignments. Outcome and HP are from the target's perspective. The handoff column gives the first observed switch to pure defense, or none if the trigger never fires.

| Target | Counter | Target outcome | HP target:counter | Final round | Handoff |
|---|---|---|---|---:|---:|
'''+ '\n'.join(rows)+'''

All counters use the same screened opening and the same finite public-budget defense after switching. The eligibility round is 6, the HP margin is zero, and the forecast uses half or all public opponent gold. The strike flag changes only whether one tier4 is attempted in round 5. No counter receives a target identity or creates an opponent policy clone.

Without that extra strike, the counter reaches a 755:660 lead against P4TNUB and best_v9e and switches at round 8. Both budget fractions preserve that lead to round 50. Against P5TNUBM the same no-strike opening never leads and dies in round 13. Adding the tier4 reverses this comparison: P5TNUBM loses 740:755 after the counter switches in round 6, while P4TNUB and best_v9e win. These are complementary complete policies, not an identified universal adaptation rule.

Both fortress targets defeat every setting. In the no-strike games a lead exists at the switch, but the budget defender later leaks and loses. This is a concrete failure of treating an observed HP lead as a guarantee of future safety. Against lead8, both no-strike settings draw by simultaneous destruction in round 8; both HP totals are -40. The engine's declared result, not HP sign, determines the draw. The one-strike settings lose to lead8 despite switching while ahead in round 6.

Comparing only the one-strike variants to the previously published fixed-handoff transfer matrix, the HP trigger repairs no transfer loss. The new wins against P4TNUB and best_v9e also remove the round-five strike, so they do not isolate the effect of changing the handoff rule. A matched no-strike fixed-deadline control is needed for that causal comparison. The half- and full-budget settings agree in outcome throughout this matrix but sometimes differ greatly in final HP and survival time.

All 48 games pass strict accounting, complete original-engine replay and source/data archive checks. All 24 assignment pairs have identical normalized histories. Fresh instances reproduce all 1,426 counter decisions, with unchanged observations, legal submitted actions and independently verified first-switch rounds. There are 312 locally filtered parent factory proposals and no rejected submitted actions or bot errors. No minion is bought after an actual handoff. Prefix checks cover all 48 settings before the full-game runs. The original fortress planners retain their wall-clock limits; observed agreement is not a proof of load independence.

These are disclosed development conditions. Player swaps are controls, not independent samples. Pool C remains unused. Reproduce each triggered-budget manifest with `run_data_development` into a fresh directory, then run the strict, replay, data and `check_triggered_budget_histories` audits. Use the project root, `.venv/bin/python -B`, bytecode disabled, temporary files under `bot_research/tmp`, one thread, low priority and assigned CPU affinity.

Audit inputs:

'''+ '\n'.join(f'- `{p}`.' for p in inputs)+'\n'
    (A/'verification').mkdir(parents=True,exist_ok=True);result=A/'RESULTS.md'
    with result.open('x') as f:f.write(text)
    inputs += [A/'PROOF.md',result,Path(__file__).relative_to(Path.cwd()),E/'analysis/budget_handoff_transfer/verification/full_games.json']
    atomic_json(A/'verification/full_games.json',dict(time_utc=now,all_passed=True,input_sha256={str(p):digest(p) for p in inputs},games=count,
        identical_assignment_pairs=pairs,fresh_decisions=calls,local_filtered_proposals=filtered,target_outcomes=dict(outcomes),
        by_target={k:dict(v) for k,v in by_target.items()},scope=verdict),exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Public-budget counters have complementary wins\n\nClaim and verdict: {verdict}\n\nMethod and result: 48 declared standard games, both seats, all strict/replay/source/data checks passed, 1,426 exact fresh counter decisions and 24 identical assignment pairs. Target total 32W/4D/12L. No-strike wins 755:660 against P4TNUB and best_v9e; one tier4 in round 5 wins 755:740 against P5TNUBM. Both fortress targets win all eight settings. lead8 draws the no-strike counter by simultaneous destruction and beats the one-strike counter. Full table and scope: experiments/validation/analysis/triggered_budget_handoff/RESULTS.md. This does not isolate the trigger effect because removing the strike is another intervention. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now,published=str(result),games=count,fresh_decisions=calls)))
if __name__=='__main__':main()
