"""Publish complete matched defensive-planner interventions."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter,defaultdict
import argparse,hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('--kind',choices=('wall','template'),required=True);args=p.parse_args();kind=args.kind
    A=E/'analysis'/('handoff_wall_intervention' if kind=='wall' else 'template_handoff_defense')
    inputs=[];rows=[];calls=filtered=games=pairs=0;outcomes=Counter();by_mode=defaultdict(Counter)
    for tag in 'abc':
        name=f'{kind}-handoff-{tag}001';ds={};m=E/(name+'.json');inputs.append(m);expected=json.loads(m.read_text())['expected_conditions']
        for key in ('strict','replay','summary','data','histories','opening'):
            q=R/f'{name}-{key}.json';inputs.append(q);ds[key]=json.loads(q.read_text())
        s,h=ds['summary'],ds['histories']
        assert ds['strict']['valid_conditions']==ds['strict']['expected_conditions']==expected
        assert s['valid_conditions']==s['expected_conditions']==expected and s['unresolved_conditions']==0
        assert s['identical_assignment_pairs']==s['complete_assignment_pairs']==expected//2 and not s['repeat_disagreements']
        assert ds['replay']['all_passed'] and ds['replay']['count']==expected and ds['data']['all_passed'] and ds['opening']['all_passed']
        assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_public_triggers_verified','all_replayed','exact_counter_policy_reproduction','no_post_handoff_minions'))
        for q,sha in h['input_sha256'].items():assert digest(q)==sha,q
        for row in s['rows']:
            values={(x['outcome'],tuple(x['hp']),x['rounds']) for x in row['results']};assert len(row['results'])==2 and len(values)==1
            outcome,hp,rnd=next(iter(values));cs=[c for c in h['cases'] if c['condition']['candidate_id']==row['candidate'] and c['condition']['opponent_id']==row['opponent']]
            switches={c['first_switch'] for c in cs};assert len(cs)==2 and len(switches)==1
            switch=next(iter(switches));switch='none' if switch is None else str(switch)
            rows.append(f'| {row["candidate"]} | {row["opponent"]} | {outcome} | {hp[0]}:{hp[1]} | {rnd} | {switch} |')
            by_mode[row['opponent']][outcome]+=2
        calls+=sum(len(c['rounds']) for c in h['cases']);filtered+=sum(len(c['filtered_proposals']) for c in h['cases']);games+=expected;pairs+=expected//2;outcomes.update(s['outcomes'])
    q=R/f'{kind}-handoff-controls-001.json';cmp=json.loads(q.read_text());assert cmp['all_passed'] and len(cmp['pairs'])==16
    assert all(digest(path)==sha for path,sha in cmp['input_sha256'].items());inputs.extend((q,E/f'{kind}-handoff-control-pairs-001.json'))
    now=datetime.now(timezone.utc).isoformat()
    if kind=='wall':
        verdict='CONFIRMED: both fixed-wall interventions preserve the three nominee/best_v9e wins. REFUTED: either intervention repairs any of the five other transfer targets.'
        detail='Both wall settings lose to F36/F37 in round16, compared with round15 without walls. They reduce lead8\'s final HP from500 to380 but still lose380:240. The economy targets prevent the trigger entirely, so all three modes have the same outcome320:-9 at round14. The completed tables do not support a strength improvement from fixed walls.'
        assert by_mode=={'walls_none':{'L':6,'W':10},'walls_stage_a':{'L':6,'W':10},'walls_full':{'L':6,'W':10}}
    else:
        verdict='CONFIRMED: the joint wall/turret planner repairs the F36/F37 transfer losses while preserving the three nominee/best_v9e wins. REFUTED: this intervention beats all eight targets.'
        detail='F36/F37 now lose740:765 at round50. The same targets beat the free planner740:-75 at round15. The joint planner still loses500:380 to lead8 at round50, while the free planner loses500:240. E25RM/E30 again prevent the trigger, so a post-trigger intervention cannot alter their320:-9 round14 wins. These matched complete-policy interventions establish the measured differences; they do not attribute them to one particular wall or turret.'
        assert by_mode=={'planner_free':{'L':6,'W':10},'planner_template':{'L':10,'W':6}}
    text=f'''# {"Fixed walls do not repair transfer" if kind=="wall" else "Joint construction repairs the two fortress losses"}

Checked {now}.

{verdict}

Every row represents both physical assignments. Outcome and HP are from the target perspective.

| Target | Counter mode | Outcome | HP target:counter | Final round | Handoff |
|---|---|---|---|---:|---:|
'''+ '\n'.join(rows)+f'''

{detail}

All{games} declared games pass strict accounting, original-engine replay, immutable source/data checks and fresh counter regeneration. All{pairs} assignment pairs have identical normalized histories. Fresh instances reproduce {calls} decisions and record {filtered} locally filtered proposals; no invalid action is submitted and no bot error occurs. All16 control histories exactly match their earlier half-budget guarded-strike counterparts. Repetition verifies reproducibility and is not an independent sample.

The intervention leaves the opening and public HP trigger unchanged. The forecast still covers a finite set of pure-tier purchases and gives no general mixed-roster guarantee. Targets and the inherited growth policies with wall-clock search retain that limitation. These are development conditions on the standard empty start. Pool C is unused.

Reproduce the three {kind}-handoff manifests with run_data_development, then the strict, replay, data and fresh-history checks named by the recorded pipeline. Run from the project root using the supplied Python environment, bytecode disabled, bot_research/tmp, one thread, assigned affinity and low priority. The control comparison is compare_recorded_controls with the declared16 pairs.

Audit inputs:

'''+ '\n'.join(f'- `{q}`.' for q in inputs)+'\n'
    q=A/'RESULTS.md'
    with q.open('x') as f:f.write(text)
    inputs += [q,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())]
    atomic_json(A/'verification/full_games.json',dict(time_utc=now,all_passed=True,input_sha256={str(q):digest(q) for q in inputs},games=games,fresh_decisions=calls,local_filtered_proposals=filtered,identical_assignment_pairs=pairs,target_outcomes=dict(outcomes),target_outcomes_by_mode=dict(by_mode),scope=verdict),exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: {kind} defensive handoff intervention complete\n\nClaim and verdict: {verdict}\n\nMethod and result: all{games} predeclared standard games, all strict/replay/source/data checks, {calls} fresh decisions and{pairs} identical seat pairs. {detail} All16 old control histories match exactly. Details experiments/validation/analysis/{A.name}/RESULTS.md. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now,games=games,calls=calls,filtered=filtered,published=str(q))))
if __name__=='__main__':main()
