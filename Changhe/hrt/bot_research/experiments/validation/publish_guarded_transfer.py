"""Publish all declared guarded-strike transfer conditions."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/guarded_round4_transfer'
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    inputs=[];rows=[];calls=filtered=0;outcomes=Counter()
    for tag in 'abc':
        name=f'guarded-transfer-{tag}001';ds={}
        for kind in ('strict','replay','summary','data','histories','opening'):
            p=R/f'{name}-{kind}.json';inputs.append(p);ds[kind]=json.loads(p.read_text())
        s,h=ds['summary'],ds['histories']
        assert ds['strict']['valid_conditions']==ds['strict']['expected_conditions']==8
        assert s['valid_conditions']==s['expected_conditions']==8 and s['unresolved_conditions']==0
        assert s['identical_assignment_pairs']==s['complete_assignment_pairs']==4 and not s['repeat_disagreements']
        assert ds['replay']['all_passed'] and ds['replay']['count']==8 and ds['data']['all_passed'] and ds['opening']['all_passed']
        assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_public_triggers_verified','all_replayed','exact_counter_policy_reproduction','no_post_handoff_minions'))
        for p,sha in h['input_sha256'].items():assert digest(p)==sha,p
        for row in s['rows']:
            values={(x['outcome'],tuple(x['hp']),x['rounds']) for x in row['results']};assert len(row['results'])==2 and len(values)==1
            outcome,hp,rnd=next(iter(values));cs=[c for c in h['cases'] if c['condition']['candidate_id']==row['candidate'] and c['condition']['opponent_id']==row['opponent']]
            switches={c['first_switch'] for c in cs};assert len(cs)==2 and len(switches)==1
            switch=next(iter(switches));switch='none' if switch is None else str(switch)
            rows.append(f'| {row["candidate"]} | {row["opponent"]} | {outcome} | {hp[0]}:{hp[1]} | {rnd} | {switch} |')
        calls+=sum(len(c['rounds']) for c in h['cases']);filtered+=sum(len(c['filtered_proposals']) for c in h['cases']);outcomes.update(s['outcomes']);inputs.append(E/f'{name}.json')
    assert outcomes=={'W':20,'L':4}
    now=datetime.now(timezone.utc).isoformat();verdict='CONFIRMED: both guarded round-four settings beat best_v9e by 15 HP in both assignments. REFUTED: either fixed setting also beats the five other declared targets.'
    text=f'''# Guarded-strike transfer is limited

Checked {now}.

{verdict}

Each row represents both assignments, with outcome and HP from the target perspective.

| Target | Counter | Target outcome | HP target:counter | Final round | Handoff |
|---|---|---|---|---:|---:|
'''+ '\n'.join(rows)+f'''

The early strike preserves its 755:740 win against the installed best_v9e, whose exact source is pinned in the declaration. It also gains an early lead against F36 and F37, but their later attacks defeat the budget defender. The two fortress versions have the same complete recorded outcomes here. Both economy targets stop the early strike and later win320:-9 in round14; the public lead trigger never fires. Against lead8 it does fire, but the defense later leaks. Using the whole public budget is not uniformly better than using half: against lead8 it dies in round9, whereas the half-budget policy survives to round50 but still loses.

All24 games pass strict accounting, original-engine replay, source/data archive checks and fresh counter regeneration. All12 assignment pairs have identical normalized histories. The checker reproduces {calls} decisions, verifies all public triggers and records {filtered} locally filtered proposals. No invalid action is submitted and no bot error occurs. The fortress planners retain wall-clock limits; these agreements do not prove load independence.

These are the six named transfer targets, without retuning between them. The original two nominee wins remain valid but do not establish general dominance. Player swaps are reproducibility controls, not independent samples. Pool C remains unused.

Reproduce guarded-transfer-a001/b001/c001 with run_data_development and the strict, replay, data and check_guarded_round4_histories audits. Run from the project root with .venv/bin/python -B, bytecode disabled, bot_research/tmp, one thread, low priority and assigned affinity.

Audit inputs:

'''+ '\n'.join(f'- `{p}`.' for p in inputs)+'\n'
    result=A/'RESULTS.md'
    with result.open('x') as f:f.write(text)
    inputs += [result,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())]
    atomic_json(A/'verification/full_games.json',dict(time_utc=now,all_passed=True,input_sha256={str(p):digest(p) for p in inputs},games=24,fresh_decisions=calls,local_filtered_proposals=filtered,identical_assignment_pairs=12,target_outcomes=dict(outcomes),scope=verdict),exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Guarded strike also beats best_v9e, but five transfer targets win\n\nClaim and verdict: {verdict}\n\nMethod and result:24 predeclared standard games, all strict/replay/source/data checks pass, {calls} fresh decisions and12 identical assignment pairs. F36/F37 win740:-75 at round15 (half budget) or740:-67 at round25 (full). E25RM/E30 win320:-9 at round14. lead8 wins500:240 at round50 or500:-40 at round9. Best_v9e loses740:755 in both settings. Table: experiments/validation/analysis/guarded_round4_transfer/RESULTS.md. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now,fresh_decisions=calls,filtered=filtered,published=str(result))))
if __name__=='__main__':main()
