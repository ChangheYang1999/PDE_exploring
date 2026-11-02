"""Publish matched no-strike controls after all declared checks pass."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/no_strike_handoff_controls'
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    inputs=[];ds={}
    for kind in ('strict','replay','summary','data','histories'):
        p=R/f'no-strike-controls-001-{kind}.json';inputs.append(p);ds[kind]=json.loads(p.read_text())
    s,h=ds['summary'],ds['histories']
    assert ds['strict']['valid_conditions']==ds['strict']['expected_conditions']==12
    assert s['valid_conditions']==s['expected_conditions']==12 and s['unresolved_conditions']==0
    assert s['identical_assignment_pairs']==s['complete_assignment_pairs']==6 and not s['repeat_disagreements']
    assert ds['replay']['all_passed'] and ds['replay']['count']==12 and ds['data']['all_passed']
    assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_replayed','exact_counter_policy_reproduction','no_post_handoff_minions'))
    for p,sha in h['input_sha256'].items():assert digest(p)==sha,p
    calls=sum(len(c['rounds']) for c in h['cases']);filtered=sum(len(c['filtered_proposals']) for c in h['cases']);assert calls==600 and filtered==0
    cmp=R/'no-strike-controls-comparison-001.json';comparison=json.loads(cmp.read_text());assert comparison['all_passed'] and len(comparison['pairs'])==6
    assert sum(p['same_complete_trajectory'] for p in comparison['pairs'])==4
    for p,sha in comparison['input_sha256'].items():assert digest(p)==sha,p
    rows=[]
    for row in s['rows']:
        values={(x['outcome'],tuple(x['hp']),x['rounds']) for x in row['results']};assert len(row['results'])==2 and len(values)==1
        outcome,hp,rnd=next(iter(values));rows.append(f'| {row["candidate"]} | {row["opponent"]} | {outcome} | {hp[0]}:{hp[1]} | {rnd} |')
    assert s['outcomes']=={'W':8,'L':4}
    now=datetime.now(timezone.utc).isoformat();verdict='CONFIRMED: delaying the fixed no-strike handoff from round 6 to round 8 converts losses into wins against P4TNUB and best_v9e. The H8 controls reproduce their HP-triggered reference histories exactly.'
    inputs += [cmp,E/'no-strike-controls-pairs-001.json',E/'no-strike-controls-001.json',E/'analysis/triggered_budget_handoff/verification/full_games.json']
    text=f'''# Matched no-strike handoff controls

Checked {now}.

{verdict}

Each row represents both physical assignments. Outcomes and HP are from the target perspective. The budget fraction is one-half in every row, and no extra tier4 is bought.

| Target | Counter | Target outcome | HP target:counter | Final round |
|---|---|---|---|---:|
'''+ '\n'.join(rows)+'''

The round-6 and round-8 controls differ only in their handoff deadline. Both lose against P5TNUBM. Against P4TNUB and best_v9e, the earlier defensive policy keeps both players alive but leaves the counter behind 755:800. Continuing its opening until round 8 lets it gain a 755:660 lead that the later defensive policy preserves. This is evidence for the complete deadline intervention under these fixed opponents, not a claim that every two-round delay is beneficial.

The previously audited trigger policy first switches at round 8 against P4TNUB and best_v9e. Its complete normalized trajectory equals the matching fixed-H8 control in all four target-assignment comparisons. Against P5TNUBM the trigger never fires and loses by round 13; its two histories differ from the H8 controls, which lose by the HP comparison at round 50. Thus the trigger does not strictly improve every target's survival or outcome. It is also not needed to obtain the two wins when H8 is known in advance.

All twelve new games pass strict accounting, original-engine replay and source/data checks. Six assignment pairs match exactly, and 600 fresh controller calls reproduce every action without observation mutation, invalid actions or locally filtered proposals. Six earlier trigger games are reused only for the reference comparison; they are not counted as new games. The comparison checks complete actions and states after player/name normalization. No reserved conditions are used.

Reproduce the no-strike-controls manifest through run_data_development and its strict, replay, data and check_budget_handoff_histories checks, then compare_recorded_controls with no-strike-controls-pairs-001.json. Use the project root, .venv/bin/python -B, bytecode disabled, bot_research/tmp, one thread, low priority and assigned affinity.

Audit inputs:

'''+ '\n'.join(f'- `{p}`.' for p in inputs)+'\n'
    (A/'verification').mkdir(exist_ok=True);result=A/'RESULTS.md'
    with result.open('x') as f:f.write(text)
    inputs += [result,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())]
    atomic_json(A/'verification/full_games.json',dict(time_utc=now,all_passed=True,input_sha256={str(p):digest(p) for p in inputs},new_games=12,reused_games=6,fresh_decisions=600,identical_assignment_pairs=6,equal_reference_histories=4,target_outcomes=s['outcomes'],scope=verdict),exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Matched deadline controls isolate the no-strike improvement\n\nClaim and verdict: {verdict}\n\nMethod and result: twelve new games, both seats, all strict/replay/source/data checks pass, 600 exact fresh decisions. H6 loses755:800 against all three targets. H8 wins755:660 against P4TNUB and best_v9e and still loses755:800 against P5TNUBM. All four expected H8-trigger full-history equalities pass; the P5TNUBM trigger never switches and instead dies by round13. Six trigger references are reused, not new samples. Full table: experiments/validation/analysis/no_strike_handoff_controls/RESULTS.md. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now,published=str(result))))
if __name__=='__main__':main()
