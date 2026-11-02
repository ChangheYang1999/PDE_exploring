"""Publish the complete final reserve, including all declared conditions."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

E=Path('bot_research/experiments/validation')
R=Path('bot_research/runs/validation')
A=E/'analysis/terminal_reserved_validation'


def timing_accounting(rows, entry_by_job):
    """Reconcile wrapper calls with independently audited policy/prefix turns."""
    actual_calls=prefix_calls=wrapper_calls=0
    total_seconds=maximum_seconds=0.0
    for row in rows:
        timed=row['decision_seconds_candidate_first'][0]
        checked=entry_by_job[row['job']]
        assert checked['condition']==row['condition']
        assert checked['rounds']==row['rounds']==timed['calls']
        assert checked['rounds']==checked['policy_rounds']+checked['prefix_rounds']
        assert checked['policy_rounds']>=0 and checked['prefix_rounds']>=0
        actual_calls+=checked['policy_rounds']
        prefix_calls+=checked['prefix_rounds']
        wrapper_calls+=timed['calls']
        total_seconds+=timed['total']
        maximum_seconds=max(maximum_seconds,timed['max'])
    assert wrapper_calls==actual_calls+prefix_calls
    return dict(timed_decision_wrapper_calls=wrapper_calls,
        actual_policy_calls=actual_calls,prescribed_prefix_turns=prefix_calls,
        total_timed_wrapper_seconds=total_seconds,
        maximum_timed_wrapper_call_seconds=maximum_seconds)


def main():
    inputs={}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)]=digest(p)
        return json.loads(Path(p).read_text())
    def verify(mapping):
        for p,h in mapping.items():
            assert digest(p)==h,p
            inputs[p]=h
    declaration=read(E/'terminal-candidate-declaration-001.json')
    verify(declaration['source_sha256'])
    manifest=read(declaration['manifest'])
    assert digest(declaration['manifest'])==declaration['manifest_sha256']
    assert declaration['candidate_and_opponent_calls']==0
    assert declaration['selection_excerpt'] in Path(declaration['selection_record']).read_text()
    name=declaration['campaign_name'];directory=R/name
    freeze=read(directory/'freeze.json')
    strict=read(R/(name+'-strict.json'))
    replay=read(R/(name+'-replay.json'))
    entry=read(R/(name+'-entrypoint-summary.json'))
    parameter=read(R/(name+'-parameter-separation.json'))
    scenario=read(R/(name+'-scenario-separation.json'))
    losses=read(R/(name+'-losses.json'))
    assert freeze['candidate']==strict['candidate']==replay['candidate']==declaration['candidate']
    assert freeze['candidate_sha256']==strict['candidate_sha256']==replay['candidate_sha256']==declaration['candidate_sha256']
    assert freeze['pool']=='D' and freeze['manifest_sha256']==declaration['manifest_sha256']
    start=datetime.fromisoformat(freeze['started_utc'])
    assert start>=datetime.fromisoformat(declaration['not_before_utc'])
    assert start>datetime.fromisoformat(declaration['time_utc'])>=datetime.fromisoformat(declaration['selection_time_utc'])
    assert strict['valid_conditions']==strict['expected_conditions']==manifest['planned_conditions']==96
    assert not strict['unresolved'] and not strict['repeat_disagreements'] and not strict['current_source_drift']
    assert strict['source_archive_verified'] and strict['jobs_match_predeclared_manifest']
    assert replay['all_primary_conditions_completed_and_replayed'] and replay['verified_primary_replays']==96
    assert replay['all_pairs_have_both_assignments']
    assert entry['all_passed'] and entry['count']==96
    assert entry['candidate_sha256']==declaration['candidate_sha256']
    assert scenario['candidate_or_opponent_calls']==0
    for p,h in freeze['source_sha256'].items():
        assert digest(p)==digest(directory/'sources'/p)==h,p
    for item in (strict,replay,entry,losses):verify(item['input_sha256'])
    verify(entry['source_sha256'])
    assert len(strict['pairs'])==48 and all(p['exactly_two_assignments'] for p in strict['pairs'])
    assert len(losses['losses'])==sum(c['outcome']=='L' for c in strict['cases'])
    group=defaultdict(list)
    for row in strict['cases']:group[row['condition']['scenario']].append(row)
    order=['standard']+sorted(k for k in group if k!='standard')
    assert len(order)==3
    entry_by_job={c['job']:c for c in entry['cases']}
    assert len(entry_by_job)==96
    assert set(entry_by_job)=={c['job'] for c in strict['cases']}
    metrics={};table=[]
    fmt=lambda c:'/'.join(str(c.get(k,0)) for k in ('W','D','L'))
    for start_name in order:
        rows=group[start_name]
        assert len(rows)==32
        counts=Counter(r['outcome'] for r in rows)
        seats=[Counter(r['outcome'] for r in rows if r['condition']['candidate_side']==s) for s in (0,1)]
        assert all(sum(x.values())==16 for x in seats)
        metrics[start_name]=dict(games=32,outcomes=counts,outcomes_by_seat=seats,
            worst_hp_difference=min(r['hp_candidate_first'][0]-r['hp_candidate_first'][1] for r in rows),
            ending_rounds=sorted({r['rounds'] for r in rows}),**timing_accounting(rows,entry_by_job))
        m=metrics[start_name]
        table.append(f'| {start_name} | {fmt(counts)} | {fmt(seats[0])} | {fmt(seats[1])} | {m["worst_hp_difference"]} | {m["ending_rounds"]} | {m["maximum_timed_wrapper_call_seconds"]:.6f} |')
    assert sum(m['actual_policy_calls'] for m in metrics.values())==entry['policy_rounds']
    assert sum(m['prescribed_prefix_turns'] for m in metrics.values())==entry['skipped_prefix_rounds']
    assert sum(m['timed_decision_wrapper_calls'] for m in metrics.values())==entry['policy_rounds']+entry['skipped_prefix_rounds']
    same_pairs=sum(p['same_complete_trajectory'] for p in strict['pairs'])
    nonvalid=[a for a in strict['attempts'] if a['status']!='valid']
    stamp=datetime.now(timezone.utc).isoformat()
    text=f'''# Final selected policy on reserved pool D

Published {stamp}.

The complete execution and replay audit is CONFIRMED for all 96 declared conditions. The selected candidate is `{declaration['candidate']}`, SHA256 `{declaration['candidate_sha256']}`. Its selection was recorded at {declaration['selection_time_utc']}, before the first D game, and the copied selection note is retained. This pool reports that fixed choice; it is not used to choose between candidates.

The sixteen opponent parameter settings and two prescribed histories were declared at {manifest['created_utc']}. They use known implementation families and were designed after earlier development results. Exact parameter and history separation is audited below; this is not a random sample from an opponent population.

W/D/L is from the candidate's perspective. Standard-start scores are separated from continuation tests, where neither policy is called during its prescribed prefix.

| Start | W/D/L | Seat0 | Seat1 | Worst HP difference | Ending rounds | Maximum timed wrapper call seconds |
|---|---|---|---|---:|---|---:|
'''+ '\n'.join(table)+f'''

All 96 conditions have an earliest valid result. The complete accounting retains {len(nonvalid)} nonvalid attempts; no selected result has a bot error, rejected submitted action or source drift. Each action history has been replayed through a fresh original Engine and every record compared. Fresh processes reproduce {entry['policy_rounds']} actual candidate decisions through the direct entry point and default factory, each agreeing with the recorded specification. The {entry['skipped_prefix_rounds']} prescribed prefix rounds are skipped. No candidate observation is mutated.

The timing wrapper is invoked on every game round, including prescribed turns that only copy prefix actions. Its call counts and aggregate seconds therefore include prefix turns. The receipt reports actual policy calls and prescribed turns separately. Aggregate timings cannot isolate policy-only time; the displayed maximum is a wrapper measurement.

The campaign began {freeze['started_utc']}, after the declared 23:00 UTC start restriction. The final primary game completed {strict['latest_completed_utc']}. Actual elapsed time to that completion was {strict['elapsed_to_latest_completion_seconds']:.6f}seconds; primary match runtimes sum to {strict['runtime_seconds_sum_of_primary_matches']:.6f}seconds. These shared-machine, low-priority timings do not estimate a portable time bound or the team's total work.

There are {strict['distinct_canonical_trajectories']} distinct complete canonical trajectories among 96 selected results. {same_pairs} of 48 physical-assignment pairs have identical canonical histories. Repeated deterministic trajectories are reproducibility checks and provide no additional independent strength evidence.

The recorded prior-use audit found {len(parameter['overlaps'])} exact normalized-parameter overlaps and {len(scenario['overlaps'])} exact prescribed-history overlaps. It records {len(parameter['skipped_unrecognized_inputs'])} unrecognized parameter inputs and {len(scenario['unresolved_inputs'])} unresolved scenario inputs. These counts describe the recognized archived streams and declarations only; they do not establish that an opponent behaves differently from every previous one or that no unrecorded evaluation occurred. The audit JSON retains coverage, inputs and every overlap.

Every selected condition follows. HP is candidate:opponent. No loss is omitted.

| Condition | W/D/L | HP | Ending round |
|---|---|---|---:|
'''
    for row in strict['cases']:
        hp=row['hp_candidate_first']
        text+=f'| {row["job"]} | {row["outcome"]} | {hp[0]}:{hp[1]} | {row["rounds"]} |\n'
    text+='''
Reproduce with terminal_validation using the candidate hash in terminal-candidate-declaration-001.json, followed by audit_terminal_campaign, replay_campaign_bounded, summarize_reserved_replays, both terminal separation audits, audit_best_entrypoints_bounded and summarize_entrypoint_audits. Bounded commands and their real timestamps are retained in the campaign pipeline log. Run from the project root with the supplied Python, bytecode disabled, the research temporary directory, an assigned low-priority core and one numerical thread. The complete receipt is verification/final_candidate.json. Protected-file integrity is checked separately against the initial inventory.

These are finite empirical findings on the unchanged bundled rules. They establish neither general superiority nor optimal play. Any later candidate revision must be identified separately and cannot inherit an untouched-validation claim from this pool.
'''
    output=A/'RESULTS.md'
    with output.open('x') as f:f.write(text)
    for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    result=dict(time_utc=stamp,all_passed=True,candidate=declaration['candidate'],candidate_sha256=declaration['candidate_sha256'],
        manifest_sha256=declaration['manifest_sha256'],conditions=96,source_archive_verified=True,metrics=metrics,
        nonvalid_attempts=nonvalid,fresh_calls_per_entrypoint=entry['policy_rounds'],skipped_prefix_rounds=entry['skipped_prefix_rounds'],
        distinct_canonical_trajectories=strict['distinct_canonical_trajectories'],identical_assignment_pairs=same_pairs,
        parameter_overlap_count=len(parameter['overlaps']),scenario_overlap_count=len(scenario['overlaps']),
        unresolved_parameter_inputs=parameter['skipped_unrecognized_inputs'],unresolved_scenario_inputs=scenario['unresolved_inputs'],
        cases=strict['cases'],input_sha256=inputs)
    with (A/'verification/final_candidate.json').open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Final reserved pool D complete\n\nClaim and verdict: CONFIRMED, all 96 declared games and complete source/replay/fresh-entry checks pass for selected SHA{declaration["candidate_sha256"]}. Per-start W/D/L: '+str({k:dict(v['outcomes']) for k,v in metrics.items()})+f'. {entry["policy_rounds"]} fresh decisions per entry point; {entry["skipped_prefix_rounds"]} skipped prefix rounds. {same_pairs}/48assignment pairs have identical histories, with {strict["distinct_canonical_trajectories"]} distinct overall. Parameter overlaps{len(parameter["overlaps"])}; prescribed-history overlaps{len(scenario["overlaps"])}. All conditions and limitations: {output}. Do not tune or select using D outcomes and then call them untouched final validation.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','input_sha256','nonvalid_attempts','unresolved_parameter_inputs','unresolved_scenario_inputs')}))


if __name__=='__main__':main()
