"""Publish fully audited finite pool C tables, keeping the selected bot fixed."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib, json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/final_reserved_validation'
ORDER=('standard','mirror_7493_3','asym_8669_2')
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('--candidate',choices=('best_v9e','P5TNUBM'),required=True);args=p.parse_args()
    inputs={}
    def read(path):
        inputs[str(path)]=digest(path)
        return json.loads(Path(path).read_text())
    declaration=read(E/'late-comparison-declaration-001.json');item=declaration['candidates'][args.candidate]
    name=item['campaign_name'];directory=R/name
    freeze=read(directory/'freeze.json');strict=read(R/(name+'-strict.json'));replay=read(R/(name+'-replay.json'))
    parameter=read(R/(name+'-parameter-separation.json'));scenario=read(R/(name+'-scenario-separation.json'))
    losses=read(R/(name+'-losses.json'))
    assert losses['candidate']==item['spec'] and losses['candidate_sha256']==item['sha256']
    for path,sha in losses['input_sha256'].items():assert digest(path)==sha
    assert freeze['candidate']==strict['candidate']==replay['candidate']==item['spec']
    assert freeze['candidate_sha256']==strict['candidate_sha256']==replay['candidate_sha256']==item['sha256']
    assert freeze['manifest_sha256']==declaration['manifest_sha256']==digest(declaration['manifest'])
    assert declaration['time_utc']<freeze['started_utc']
    assert strict['valid_conditions']==strict['expected_conditions']==72
    assert not strict['unresolved'] and not strict['repeat_disagreements'] and not strict['current_source_drift']
    assert strict['jobs_match_predeclared_manifest'] and strict['source_archive_verified']
    assert replay['all_primary_conditions_completed_and_replayed'] and replay['verified_primary_replays']==72
    assert replay['all_pairs_have_both_assignments']
    for path,sha in freeze['source_sha256'].items():
        assert digest(path)==sha and digest(directory/'sources'/path)==sha
    for path,sha in strict['input_sha256'].items():assert digest(path)==sha
    for path,sha in replay['input_sha256'].items():assert digest(path)==sha
    assert parameter['cutoff_utc']==scenario['cutoff_utc']==freeze['started_utc']
    assert scenario['candidate_or_opponent_calls']==0
    entry=None
    if args.candidate=='best_v9e':
        entry=read(R/(name+'-entrypoint-summary.json'))
        assert entry['all_passed'] and entry['count']==72 and entry['candidate_sha256']==item['sha256']
        for path,sha in entry['input_sha256'].items():assert digest(path)==sha
        for path,sha in entry['source_sha256'].items():assert digest(path)==sha
        assert parameter['no_exact_normalized_parameter_overlap_found'] and scenario['no_exact_complete_history_overlap_found']
    assert len(losses['losses'])==sum(c['outcome']=='L' for c in strict['cases'])
    groups=defaultdict(list)
    conditions=[]
    for c in strict['cases']:
        groups[c['condition']['scenario']].append(c)
        row=read(c['result_path'])
        assert not any(row['bot_errors']) and not any(row['rejected_actions']) and not row['source_changed_during_match']
        conditions.append(dict(job=c['job'],condition=c['condition'],outcome=c['outcome'],hp_candidate_first=c['hp_candidate_first'],hp_difference=c['hp_candidate_first'][0]-c['hp_candidate_first'][1],rounds=c['rounds'],candidate_decision_seconds=c['decision_seconds_candidate_first'][0],runtime_seconds=c['runtime_seconds'],result_path=c['result_path'],replay_path=c['replay_path']))
    table=[];metrics={}
    for start in ORDER:
        group=groups[start];assert len(group)==24
        count=Counter(c['outcome'] for c in group)
        margin=min(c['hp_candidate_first'][0]-c['hp_candidate_first'][1] for c in group)
        end=sorted(set(c['rounds'] for c in group))
        seats=[]
        for seat in (0,1):
            tally=Counter(c['outcome'] for c in group if c['condition']['candidate_side']==seat)
            assert sum(tally.values())==12
            seats.append(dict(tally))
        times=[c['decision_seconds_candidate_first'][0] for c in group]
        metrics[start]=dict(games=24,outcomes=dict(count),outcomes_by_seat=seats,worst_hp_difference=margin,ending_rounds=end,max_candidate_call_seconds=max(t['max'] for t in times),total_candidate_decision_seconds=sum(t['total'] for t in times),candidate_calls=sum(t['calls'] for t in times),sum_match_seconds=sum(c['runtime_seconds'] for c in group))
        fmt=lambda d:'/'.join(str(d.get(k,0)) for k in ('W','D','L'))
        table.append(f'| {start} | {fmt(count)} | {fmt(seats[0])} | {fmt(seats[1])} | {margin} | {", ".join(map(str,end))} | {metrics[start]["max_candidate_call_seconds"]:.6f} |')
    now=datetime.now(timezone.utc).isoformat()
    failures=[a for a in strict['attempts'] if a['status']!='valid']
    po=parameter['overlaps'];so=scenario['overlaps'];unresolved=scenario['unresolved_inputs']
    intro=('This is the independent final validation of the installed bot. Selection was fixed before these games.' if args.candidate=='best_v9e' else 'This is the comparison declared before the first pool C game. P5TNUBM remains unselected, regardless of this table. It uses the same fixed conditions as the primary validation and adds no independent sample of opponents.')
    text=f'''# Pool C: {args.candidate}\n\nPublished {now}.\n\n{intro}\n\nEntry point: `{item['spec']}`. Source SHA256: `{item['sha256']}`. The declaration and all source archives still match. Verdict: CONFIRMED for the exact finite table below, conditional on the stated environment and inputs. No claim of general optimality is made.\n\nWins/draws/losses are candidate outcomes from the original engine. HP difference is candidate minus opponent.\n\n| Start | W/D/L, both seats | Seat 0 W/D/L | Seat 1 W/D/L | Worst HP difference | Ending rounds | Largest candidate call, seconds |\n|---|---|---|---|---:|---|---:|\n'''+ '\n'.join(table)+f'''\n\nAll 72 prescribed conditions have complete results and independent original-engine replays. There are no bot errors, submitted rejected actions or source changes in the selected results. All 36 opponent/start combinations have both player assignments; {sum(c['same_complete_trajectory'] for c in strict['pairs'])} of their complete normalized trajectories agree. The engine is deterministic. The seat swaps test assignment effects and observed symmetry. They are not independent random samples.\n\nThe standard row begins from the normal game state. The two other rows prescribe legal initial histories from the unchanged manifest and skip policy calls for the first three or two rounds. Those rows test continuation from externally supplied positions, including the bot's foreign-map behavior. They are not merged into a single standard-start win rate.\n\nThe manifest was declared at 09:11:05Z. Both candidate specifications were registered at {declaration['time_utc']}, before either comparison campaign. This campaign began {freeze['started_utc']} and its last selected game completed {strict['latest_completed_utc']}; elapsed time was {strict['elapsed_to_latest_completion_seconds']:.6f} seconds. The selected games sum to {strict['runtime_seconds_sum_of_primary_matches']:.6f} seconds. Timing is low-priority wall time on shared hardware, not a portable speed bound; the sum of match times is not aggregate team runtime.\n\nThere are {len(failures)} failed or invalid attempts in the complete accounting, retained separately. The earliest valid completion is selected once per exact condition. All failures, if any, are listed in the linked strict receipt.\n\nThe separation audit found {len(po)} exact parameter overlaps and {len(so)} exact prescribed-history overlaps with records preceding this campaign. It leaves {len(unresolved)} recognized scenario inputs unresolved. The detailed receipts state coverage and every qualification. Implementations and families are shared with development, so these are held-out parameter settings and legal histories, not unseen policy families. For the comparison candidate, overlap with the earlier primary C campaign is expected by design.\n'''
    if entry is not None:
        text+=f'''\nFresh-process entry-point checks verify all 72 games and {entry['policy_rounds']} actual policy decisions per entry point. Direct `decide`, the default factory and the recorded candidate return exactly the same legal actions and leave observations unchanged. The {entry['skipped_prefix_rounds']} prescribed opening rounds are not counted as policy calls. These repeated checks add no strength sample.\n'''
    text+=f'''\nThe complete per-opponent HP, outcome and ending-round table is in `bot_research/runs/validation/{name}-summary.md`. The strict, replay, separation and loss receipts share this campaign prefix. No C-informed revision is permitted to reuse C as confirmatory evidence.\n\nReproduction uses `late_validation` with the exact declared candidate and hash, a new relative output directory, `--max-seconds 480 --match-timeout 300`, and `--resume` in later bounded invocations. Then run `audit_late_campaign`, `replay_campaign_bounded`, `summarize_reserved_replays` and `render_late_summary`. The pipeline log records every exact command. Use the supplied Python environment from the project root with bytecode disabled, the assigned low-priority affinity, single-thread numerical libraries and the required research temporary directory. No server or external compute is used.\n'''
    out=A/('RESULTS.md' if args.candidate=='best_v9e' else 'COMPARISON.md')
    with out.open('x') as f:f.write(text)
    inputs[str(out)]=digest(out);inputs[str(A/'PROOF.md')]=digest(A/'PROOF.md');inputs[str(Path(__file__).relative_to(Path.cwd()))]=digest(__file__)
    evidence=dict(time_utc=now,candidate=args.candidate,candidate_spec=item['spec'],candidate_sha256=item['sha256'],all_passed=True,conditions=72,metrics=metrics,cases=conditions,source_archive_verified=True,parameter_overlap_count=len(po),scenario_overlap_count=len(so),unresolved_scenario_inputs=len(unresolved),nonvalid_attempts=len(failures),input_sha256=inputs)
    atomic_json(A/'verification'/(args.candidate+'.json'),evidence,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {now}: Pool C {args.candidate} fully audited\n\nClaim and verdict: CONFIRMED for the exact 72-condition finite evaluation of SHA {item["sha256"]}. '+intro+'\n\n')
        for start in ORDER:
            m=metrics[start];f.write(f'{start}: '+ '/'.join(str(m['outcomes'].get(k,0)) for k in ('W','D','L'))+f' W/D/L, worst HP difference {m["worst_hp_difference"]}, rounds{m["ending_rounds"]}, largest candidate call {m["max_candidate_call_seconds"]:.6f}s.\n')
        f.write(f'\nAll 72 original-engine replays pass, no bot errors/rejections/source drift. Entry-point verification: '+(f'{entry["policy_rounds"]} policy calls per entry point over all 72 games.' if entry else 'The parameterized comparison uses its declared factory.')+f' Evidence: experiments/validation/analysis/final_reserved_validation/{out.name}. All per-seat/per-opponent tables: runs/validation/{name}-summary.md. Separation qualifications and all computational attempts are retained.\n')
    print(json.dumps(dict(time_utc=now,candidate=args.candidate,metrics=metrics)))
if __name__=='__main__':main()
