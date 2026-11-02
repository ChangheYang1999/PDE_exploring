"""Publish the matched round-four corner-gun intervention."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/guarded_round4_strike'
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    inputs=[];ds={}
    for kind in ('strict','replay','summary','data','histories','opening'):
        p=R/f'guarded-round4-001-{kind}.json';inputs.append(p);ds[kind]=json.loads(p.read_text())
    s,h=ds['summary'],ds['histories']
    assert ds['strict']['valid_conditions']==ds['strict']['expected_conditions']==16
    assert s['valid_conditions']==s['expected_conditions']==16 and s['unresolved_conditions']==0
    assert s['identical_assignment_pairs']==s['complete_assignment_pairs']==8 and not s['repeat_disagreements']
    assert ds['replay']['all_passed'] and ds['replay']['count']==16 and ds['data']['all_passed'] and ds['opening']['all_passed']
    assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_public_triggers_verified','all_replayed','exact_counter_policy_reproduction','no_post_handoff_minions'))
    for p,sha in h['input_sha256'].items():assert digest(p)==sha,p
    calls=sum(len(c['rounds']) for c in h['cases']);filtered=sum(len(c['filtered_proposals']) for c in h['cases']);assert (calls,filtered)==(496,184)
    cmp=R/'guarded-round4-controls-001.json';comparison=json.loads(cmp.read_text())
    assert comparison['all_passed'] and len(comparison['pairs'])==8 and all(p['same_complete_trajectory'] for p in comparison['pairs'])
    for p,sha in comparison['input_sha256'].items():assert digest(p)==sha,p
    rows=[]
    for row in s['rows']:
        values={(x['outcome'],tuple(x['hp']),x['rounds']) for x in row['results']};assert len(row['results'])==2 and len(values)==1
        outcome,hp,rnd=next(iter(values));cs=[c for c in h['cases'] if c['condition']['candidate_id']==row['candidate'] and c['condition']['opponent_id']==row['opponent']]
        switches={c['first_switch'] for c in cs};assert len(cs)==2 and len(switches)==1
        enabled='earlygun1' in row['opponent'];assert outcome==('L' if enabled else 'W') and next(iter(switches))==(5 if enabled else None)
        rows.append(f'| {row["candidate"]} | {row["opponent"]} | {outcome} | {hp[0]}:{hp[1]} | {rnd} |')
    now=datetime.now(timezone.utc).isoformat();verdict='CONFIRMED: the 30-gold round-four corner gun converts the fixed early-heavy policy from a loss into a 755:740 win against both P4TNUB and P5TNUBM, for both tested public-budget fractions and both assignments.'
    inputs += [cmp,E/'guarded-round4-control-pairs-001.json',E/'guarded-round4-001.json',E/'analysis/triggered_budget_timing/verification/full_games.json']
    text=f'''# One cheap gun makes the early strike win against both nominees

Checked {now}.

{verdict}

Each row represents both physical assignments. Outcome and HP are from the target perspective.

| Target | Counter | Target outcome | HP target:counter | Final round |
|---|---|---|---|---:|
'''+ '\n'.join(rows)+'''

The common opening reaches round 4 with 291 gold. The tier4 costs 260. A 60-gold splash cannot accompany it, but gun1 at (10,1) costs 30 and stops the three incoming tier1 copies on the unchanged empty route. The counter retains 755 HP while its tier4 reduces either nominee to 740. At round 5 the public-HP trigger sees that lead and switches to the budget defender. Both a half-budget and a full-budget forecast preserve the lead through round 50. No target policy clone or opponent-name lookup is used.

This is a complete-policy intervention. Prepending the gun also filters now-unaffordable later proposals and changes future income; the result is not attributed to a hypothetical gun with no opportunity cost. All eight disabled-gun controls match the earlier unguarded complete histories exactly, including their round-12 loss. Prefix and full-game checks use the original engine. The analytical gun claim is separately stated with its exact empty-route and three-tier1 hypotheses in PROOF.md.

The two nominees have identical gameplay through round 4 under equal labels. This counter therefore does not need to distinguish them before their policies diverge. The result illustrates why an identical-observation theorem alone cannot establish that one common strategy must lose against one of the targets.

All 16 games pass strict accounting, original-engine replay and source/data archive checks. All eight assignment pairs match exactly. Fresh instances reproduce all 496 decisions with unchanged observations and independently verified first-switch rounds. There are 184 locally rejected parent proposals, all omitted before submission; there are no invalid submitted actions or bot errors. These are disclosed development conditions, not independent statistical samples. Pool C remains unused.

The exact two winning specs and full source closure are in guarded-round4-001.json. Reproduce it with run_data_development, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives and check_guarded_round4_histories. The prefix and disabled-control checks are check_guarded_round4_opening and compare_recorded_controls. Use the project root, .venv/bin/python -B, bytecode disabled, bot_research/tmp, one thread, low priority and assigned affinity.

Audit inputs:

'''+ '\n'.join(f'- `{p}`.' for p in inputs)+'\n'
    (A/'verification').mkdir(exist_ok=True);result=A/'RESULTS.md'
    with result.open('x') as f:f.write(text)
    inputs += [result,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())]
    atomic_json(A/'verification/full_games.json',dict(time_utc=now,all_passed=True,input_sha256={str(p):digest(p) for p in inputs},games=16,fresh_decisions=calls,local_filtered_proposals=filtered,identical_assignment_pairs=8,equal_disabled_controls=8,target_outcomes=s['outcomes'],scope=verdict),exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: One fixed guarded strike beats both nominees\n\nClaim and verdict: {verdict}\n\nMethod and result: sixteen declared standard games, all strict/replay/source/data checks pass, 496 exact fresh decisions, eight identical assignment pairs and eight exact disabled-control histories. At round4, gun1(10,1)+tier4 costs290 of291 gold; the gun stops the three incoming tier1, preserving counter755 against target740. The public HP trigger hands off at round5 and holds the lead. Disabled gun loses in round12. Winning specs are earlygun1_budget1of2 and earlygun1_budget1of1 in experiments/validation/guarded-round4-001.json; source bots/counters/guarded_round4_trigger.py. Full table and receipt: experiments/validation/analysis/guarded_round4_strike/. No model or name lookup. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now,published=str(result))))
if __name__=='__main__':main()
