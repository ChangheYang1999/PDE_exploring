"""Publish a complete reused C comparison without rewriting prior validation."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import argparse
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E/'analysis/reused_c_validation'
ORDER = ('standard','mirror_7493_3','asym_8669_2')
RANK = {'L':0,'D':1,'W':2}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--declaration", default=str(E/"reused-c-declaration-001.json"))
    args = parser.parse_args()
    inputs = {}
    def digest(p):
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)] = digest(p)
        return json.loads(Path(p).read_text())
    def verify(mapping):
        for p, h in mapping.items():
            assert digest(p) == h, p
            inputs[p] = h
    declaration = read(Path(args.declaration))
    verify(declaration['source_sha256'])
    name = declaration['campaign_name']
    oldname = declaration['old_campaign_name']
    directory = R/name
    freeze = read(directory/'freeze.json')
    strict = read(R/(name+'-strict.json'))
    replay = read(R/(name+'-replay.json'))
    entry = read(R/(name+'-entrypoint-summary.json'))
    parameter = read(R/(name+'-parameter-separation.json'))
    scenario = read(R/(name+'-scenario-separation.json'))
    losses = read(R/(name+'-losses.json'))
    assert declaration['time_utc'] < freeze['started_utc']
    assert freeze['candidate'] == strict['candidate'] == replay['candidate'] == declaration['candidate']
    assert freeze['candidate_sha256'] == strict['candidate_sha256'] == replay['candidate_sha256'] == declaration['candidate_sha256']
    assert freeze['manifest_sha256'] == declaration['manifest_sha256'] == digest(declaration['manifest'])
    assert strict['valid_conditions'] == strict['expected_conditions'] == 72
    assert not strict['unresolved'] and not strict['repeat_disagreements'] and not strict['current_source_drift']
    assert strict['jobs_match_predeclared_manifest'] and strict['source_archive_verified']
    assert replay['all_primary_conditions_completed_and_replayed'] and replay['verified_primary_replays'] == 72
    assert replay['all_pairs_have_both_assignments']
    assert entry['all_passed'] and entry['count'] == 72 and entry['candidate_sha256'] == declaration['candidate_sha256']
    assert scenario['candidate_or_opponent_calls'] == 0
    for p, h in freeze['source_sha256'].items():
        assert digest(p) == digest(directory/'sources'/p) == h, p
    for item in (strict,replay,entry,losses):
        verify(item['input_sha256'])
    verify(entry['source_sha256'])
    oldproof = read(E/'analysis/final_reserved_validation/verification/best_v9e.json')
    assert oldproof['all_passed'] and oldproof['conditions'] == 72
    verify(oldproof['input_sha256'])
    oldstrict = read(R/(oldname+'-strict.json'))
    oldfreeze = read(R/oldname/'freeze.json')
    assert oldstrict['valid_conditions'] == 72 and not oldstrict['unresolved']
    assert oldfreeze['candidate_sha256'] == '70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87'
    for p, h in oldfreeze['source_sha256'].items():
        assert digest(R/oldname/'sources'/p) == h, p
    key = lambda row:json.dumps(row['condition'],sort_keys=True,separators=(',',':'))
    oldcases = {key(row):row for row in oldstrict['cases']}
    assert len(oldcases) == 72 and set(oldcases) == {key(row) for row in strict['cases']}
    comparisons = []
    groups = defaultdict(list)
    transitions = Counter()
    for c in strict['cases']:
        oldc = oldcases[key(c)]
        new = checked_row(c['result_path'],inputs)
        old = checked_row(oldc['result_path'],inputs)
        assert new['condition'] == old['condition'] == c['condition']
        assert new['outcome'] == c['outcome'] and old['outcome'] == oldc['outcome']
        transition = old['outcome']+'->'+new['outcome']
        transitions[transition] += 1
        row = dict(condition=new['condition'],job=c['job'],old_result=old['result_path'],new_result=new['result_path'],
            old_outcome=old['outcome'],new_outcome=new['outcome'],old_hp=old['hp_candidate_first'],new_hp=new['hp_candidate_first'],
            old_rounds=old['rounds'],new_rounds=new['rounds'],
            old_canonical_sha256=old['canonical_replay_sha256'],new_canonical_sha256=new['canonical_replay_sha256'],
            same_complete_trajectory=old['canonical_replay_sha256']==new['canonical_replay_sha256'],
            fallback_condition=new['outcome']=='L' and old['outcome']!='L')
        comparisons.append(row)
        groups[c['condition']['scenario']].append(c)
    assert len(losses['losses']) == sum(r['new_outcome']=='L' for r in comparisons)
    failures = [a for a in strict['attempts'] if a['status'] != 'valid']
    fallback = [r for r in comparisons if r['fallback_condition']]
    improved = [r for r in comparisons if RANK[r['new_outcome']] > RANK[r['old_outcome']]]
    regressed = [r for r in comparisons if RANK[r['new_outcome']] < RANK[r['old_outcome']]]
    metrics = {}
    table = []
    fmt = lambda c:'/'.join(str(c.get(k,0)) for k in ('W','D','L'))
    for start in ORDER:
        rows = groups[start]
        assert len(rows) == 24
        counts = Counter(r['outcome'] for r in rows)
        seats = [Counter(r['outcome'] for r in rows if r['condition']['candidate_side']==s) for s in (0,1)]
        assert all(sum(c.values()) == 12 for c in seats)
        times = [r['decision_seconds_candidate_first'][0] for r in rows]
        m = dict(games=24,outcomes=counts,outcomes_by_seat=seats,
            worst_hp_difference=min(r['hp_candidate_first'][0]-r['hp_candidate_first'][1] for r in rows),
            ending_rounds=sorted({r['rounds'] for r in rows}),candidate_calls=sum(t['calls'] for t in times),
            total_candidate_decision_seconds=sum(t['total'] for t in times),max_candidate_call_seconds=max(t['max'] for t in times))
        metrics[start] = m
        table.append(f'| {start} | {fmt(counts)} | {fmt(seats[0])} | {fmt(seats[1])} | {m["worst_hp_difference"]} | {m["ending_rounds"]} | {m["max_candidate_call_seconds"]:.6f} |')
    stamp = datetime.now(timezone.utc).isoformat()
    trigger = 'TRIGGERED' if fallback else 'NOT TRIGGERED'
    details = []
    for r in comparisons:
        details.append(f'| {r["job"]} | {r["old_outcome"]} {r["old_hp"][0]}:{r["old_hp"][1]} r{r["old_rounds"]} | {r["new_outcome"]} {r["new_hp"][0]}:{r["new_hp"][1]} r{r["new_rounds"]} | {r["fallback_condition"]} |')
    text = f'''# best_v9f on reused pool C

Published {stamp}.

The lead's predeclared fallback is **{trigger}**: {len(fallback)} new losses replace an old best_v9e win or draw. Across all seventy-two matched conditions, there are {len(improved)} W/D/L improvements and {len(regressed)} regressions. The finite table and the complete original-engine and entry-point checks are CONFIRMED. This worker reports the rule's result; the lead owns installation of the final bot.

This is a reused-pool independent execution audit. Pool C had already been evaluated and its aggregates disclosed before the lead selected this candidate. The fallback uses C to choose between candidates. These results therefore cannot be presented as untouched final validation of the selected winner. The earlier best_v9e validation is preserved with its original timestamps and source archives.

New candidate: `{declaration['candidate']}`, SHA256 `{declaration['candidate_sha256']}`. The twelve opposing configurations and three starts are exactly the original C manifest. Wins/draws/losses and HP differences below are from the candidate's perspective.

| Start | W/D/L | Seat0 | Seat1 | Worst HP difference | Ending rounds | Maximum call seconds |
|---|---|---|---|---:|---|---:|
'''+ '\n'.join(table)+f'''

All seventy-two new conditions are complete, with no bot errors, rejected submitted actions, or source drift. There are {len(failures)} nonvalid attempts in the complete retained accounting. Every selected result is replayed through the unchanged original engine. Fresh-process direct `decide` and default factory checks reproduce {entry['policy_rounds']} actual decisions per entry point across all seventy-two histories. The {entry['skipped_prefix_rounds']} prescribed prefix rounds are skipped rather than counted as policy calls. All observations remain unchanged and all fresh actions are legal.

The campaign started {freeze['started_utc']}; the last game completed {strict['latest_completed_utc']}. Elapsed time to that completion was {strict['elapsed_to_latest_completion_seconds']:.6f} seconds. Selected game runtimes sum to {strict['runtime_seconds_sum_of_primary_matches']:.6f} seconds. These are actual shared-machine low-priority timings, not an estimate of team runtime or a portable speed bound.

The refreshed separation audit records {len(parameter['overlaps'])} exact parameter overlaps, {len(scenario['overlaps'])} exact prescribed-history overlaps and {len(scenario['unresolved_inputs'])} unresolved recognized scenario inputs. Overlap with prior C runs is expected. Policy families and implementations are shared with development. {sum(r['same_complete_trajectory'] for r in comparisons)} old/new matched histories are exactly equal after canonical player/name normalization. {sum(p['same_complete_trajectory'] for p in strict['pairs'])} of thirty-six new physical-assignment pairs agree. Repeated deterministic trajectories add no independent strength evidence.

The following table includes every condition. A true final column activates the lead's fallback rule.

| Condition | best_v9e | best_v9f | Fallback |
|---|---|---|---|
'''+ '\n'.join(details)+'''

Reproduce with late_validation and the exact candidate hash in the active reused-c-declaration JSON, then audit_late_campaign, replay_campaign_bounded, summarize_reserved_replays, both separation audits, audit_best_entrypoints_bounded and summarize_entrypoint_audits. The pipeline log retains the bounded invocations. Use the supplied Python from the project root, disabled bytecode, the research temporary directory, one assigned low-priority core and one numerical thread. The complete machine-readable comparison and its input hashes are in verification/full_games.json.
'''
    output = A/'RESULTS.md'
    with output.open('x') as f:
        f.write(text)
    for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):
        inputs[str(p)] = digest(p)
    result = dict(time_utc=stamp,all_audits_passed=True,new_games=72,old_controls=72,
        candidate_sha256=declaration['candidate_sha256'],fallback_triggered=bool(fallback),fallback_conditions=fallback,
        improvements=len(improved),regressions=len(regressed),transitions=transitions,metrics=metrics,
        fresh_policy_calls_per_entrypoint=entry['policy_rounds'],skipped_prefix_rounds=entry['skipped_prefix_rounds'],
        comparisons=comparisons,input_sha256=inputs)
    with (A/'verification/full_games.json').open('x') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: best_v9f reused C audit complete\n\nClaim and verdict: CONFIRMED, all72conditions and original-engine/fresh-entry checks pass for SHA {declaration["candidate_sha256"]}. The predeclared fallback is {trigger}: {len(fallback)} new losses replace old wins/draws. Full W/D/L transitions: {dict(transitions)}. {entry["policy_rounds"]} fresh calls per direct/factory entry, {entry["skipped_prefix_rounds"]} correctly skipped prefix rounds; zero errors/rejections/source drift. C is now selection evidence, not untouched final validation. Complete conditions and metrics: {output}. The installed bytes can now be changed according to the lead\'s rule.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('comparisons','input_sha256','fallback_conditions')}))


if __name__ == '__main__':
    main()
