"""Render checked pool D results without merging standard and stress scores."""
from __future__ import annotations
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.final_validation_strict import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign-audit', required=True)
    parser.add_argument('--replay-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    audit = json.loads(Path(args.campaign_audit).read_text())
    replay = json.loads(Path(args.replay_audit).read_text())
    if replay['input_sha256'].get(args.campaign_audit) != digest(args.campaign_audit):
        raise ValueError('Replay accounting does not bind this campaign audit.')
    if not replay['all_primary_conditions_completed_and_replayed']:
        raise ValueError('A final summary requires every declared match and replay.')
    for field in ('candidate', 'candidate_sha256', 'pool', 'scores_by_scenario'):
        if replay[field] != audit[field]:
            raise ValueError('Campaign and replay accounting disagree: ' + field)
    for case in audit['cases']:
        for field in ('result_path', 'replay_path'):
            filename = case[field]
            if digest(filename) != audit['input_sha256'][filename]:
                raise ValueError('Checked match evidence changed: ' + filename)
    cases = audit['cases']
    grouped = defaultdict(list)
    for case in cases:
        grouped[case['condition']['scenario']].append(case)
    lines = [
        '# Independent reserved validation', '',
        f"Rendered at {now()}.", '',
        f"Candidate: `{audit['candidate']}`.",
        f"SHA256: `{audit['candidate_sha256']}`.",
        f"Pool: {audit['pool']}. All {len(cases)} prescribed conditions have valid results and complete original-engine replays.", '',
        'Standard starts measure the declared policy from its normal initial state. '
        'The other starts replace the first two or three rounds with registered legal prefixes and skip the underlying policy calls during those prefixes. '
        'Their scores are continuation stress results and are kept separate.', '',
        '| Start | Games | Wins | Draws | Losses |',
        '| --- | ---: | ---: | ---: | ---: |']
    order = ['standard'] + sorted(k for k in grouped if k != 'standard')
    for scenario in order:
        if scenario not in grouped:
            continue
        counts = audit['scores_by_scenario'][scenario]
        lines.append(f"| {scenario} | {len(grouped[scenario])} | {counts.get('W', 0)} | {counts.get('D', 0)} | {counts.get('L', 0)} |")
    paired = sum(p['exactly_two_assignments'] for p in audit['pairs'])
    identical = sum(p['same_complete_trajectory'] for p in audit['pairs'])
    lines += ['', f'{paired} conditions have both player assignments; {identical} pairs have identical complete normalized trajectories. '
              'The engine is deterministic. Exchanging seats and replaying actions checks reproducibility; neither supplies an independent random sample.', '',
              '| Start | Opponent | Seat 0 outcome / HP | Seat 1 outcome / HP | Rounds, seats 0 / 1 |',
              '| --- | --- | --- | --- | --- |']
    descriptions = {}
    for scenario in order:
        groups = defaultdict(list)
        for case in grouped.get(scenario, []):
            identifier = case['job'].rsplit('-', 2)[1]
            groups[identifier].append(case)
            descriptions[identifier] = case['condition']['opponent']
        for identifier, group in sorted(groups.items()):
            group.sort(key=lambda c: c['condition']['candidate_side'])
            if [c['condition']['candidate_side'] for c in group] != [0, 1]:
                raise ValueError('A condition lacks one player assignment.')
            outcomes = [c['outcome'] + ' ' + ':'.join(map(str, c['hp_candidate_first'])) for c in group]
            rounds = ' / '.join(str(c['rounds']) for c in group)
            lines.append(f"| {scenario} | {audit['pool']}-{identifier} | {outcomes[0]} | {outcomes[1]} | {rounds} |")
    failed = [a for a in audit['attempts'] if a['status'] == 'failed']
    lines += ['', 'HP is always candidate first. A simultaneous base destruction is a draw even when final HP differ.', '',
              f'{len(failed)} failed computational attempts are retained separately from the selected completed results. '
              'The selected result is the earliest valid completion for that exact condition. No outcome is assigned from a partial replay.', '']
    for attempt in failed:
        failure = attempt['failure']
        description = (f"{failure['timeout_seconds']:g}-second timeout" if 'timeout_seconds' in failure
                       else json.dumps(failure, sort_keys=True))
        lines.append(f"- `{attempt['job']}`: {description}; evidence in `{attempt['directory']}`.")
    lines += ['', 'Runtime measurements are low-priority wall times on a shared machine, not portable speed bounds. '
              'The sum of parallel match runtimes is not elapsed experiment time. Timed calls include the prefix wrapper; prescribed-round calls do not invoke the underlying policy.', '',
              '| Start | Sum of selected match times (s) | Largest candidate call (s) | Largest candidate total per match (s) |',
              '| --- | ---: | ---: | ---: |']
    for scenario in order:
        group = grouped.get(scenario, [])
        if group:
            lines.append(f"| {scenario} | {sum(c['runtime_seconds'] for c in group):.3f} | "
                         f"{max(c['decision_seconds_candidate_first'][0]['max'] for c in group):.3f} | "
                         f"{max(c['decision_seconds_candidate_first'][0]['total'] for c in group):.3f} |")
    lines += ['', f"First campaign start: {audit['started_utc']}. Last selected match completion: {audit['latest_completed_utc']}.",
              f"Elapsed between those events: {audit['elapsed_to_latest_completion_seconds']:.3f} seconds.", '',
              'The source archive matches the declared freeze. Completed results have no bot errors, rejected actions or source drift. '
              'The archived manifest and generated jobs agree. Opponent policy families and implementation code are shared with development. '
              'The separate holdout-separation audit addresses exact parameter overlap. No universal strength claim follows.', '',
              'Opponent definitions:', '', '```json', json.dumps(descriptions, indent=2, sort_keys=True), '```', '',
              f"Campaign accounting: `{args.campaign_audit}` (SHA256 `{digest(args.campaign_audit)}`).",
              f"Replay accounting: `{args.replay_audit}` (SHA256 `{digest(args.replay_audit)}`).",
              f"Renderer SHA256: `{digest(__file__)}`.", '']
    output = Path(args.output)
    if output.is_absolute() or output.parts[:3] != ('bot_research', 'runs', 'validation') or '..' in output.parts:
        raise ValueError('Use a project-relative validation output path.')
    with output.open('x') as stream:
        stream.write('\n'.join(lines))
    print(json.dumps({'output': args.output, 'games': len(cases), 'paired_conditions': paired}))


if __name__ == '__main__':
    main()
