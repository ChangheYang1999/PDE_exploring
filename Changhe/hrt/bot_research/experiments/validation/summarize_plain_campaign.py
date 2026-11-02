"""Summarize a campaign only after strict checks and original-engine replay.

Every valid attempt, including repeats, must occur in the replay audit. Primary
counts follow the strict audit's earliest-valid-completion rule. Raw trajectory
hashes are checked again at summary time.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', required=True)
    parser.add_argument('--replay', required=True)
    parser.add_argument('--heading', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    strict = json.loads(Path(args.strict).read_text())
    replay = json.loads(Path(args.replay).read_text())
    assert replay['all_passed'] and not replay['source_changed_during_run']
    replayed = {r['trajectory_sha256'] for r in replay['cases'] if r['passed']}
    sources = {p:digest(p) for p in (args.strict, args.replay)}
    for attempt in strict['attempts']:
        if attempt['status'] != 'valid':
            continue
        path = attempt['result_path']
        assert digest(path) == strict['input_sha256'][path]
        row = json.loads(Path(path).read_text())
        assert row['trajectory_sha256'] in replayed
        assert digest(row['replay_path']) == row['trajectory_sha256']
        sources[path] = digest(path)
        sources[row['replay_path']] = row['trajectory_sha256']
    grouped = defaultdict(list)
    for case in strict['cases']:
        condition = case['condition']
        grouped[(condition['candidate_id'], condition['opponent_id'])].append(dict(
            side=condition['candidate_side'], outcome=case['outcome'], hp=case['hp_candidate_first'],
            rounds=case['rounds'], runtime_seconds=case['runtime_seconds'],
            result_path=case['result_path']))
    rows = [dict(candidate=k[0], opponent=k[1], results=sorted(v,key=lambda r:r['side']))
            for k,v in grouped.items()]
    stamp = datetime.now(timezone.utc).isoformat()
    out = dict(time_utc=stamp, heading=args.heading, input_sha256=sources,
        checker_sha256=digest(__file__), valid_conditions=strict['valid_conditions'],
        expected_conditions=strict['expected_conditions'], attempt_counts=strict['attempt_counts'],
        unresolved_conditions=len(strict['unresolved']),
        outcomes=dict(Counter(c['outcome'] for c in strict['cases'])),
        complete_assignment_pairs=sum(p['exactly_two_assignments'] for p in strict['pairs']),
        identical_assignment_pairs=sum(p['same_complete_trajectory'] for p in strict['pairs']),
        repeat_disagreements=strict['repeat_disagreements'], rows=rows,
        scope='Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.')
    atomic_json(args.output,out,exclusive=True)
    lines = [f'# {args.heading}', '', f'Recorded: {stamp}', '',
        f"Completed {out['valid_conditions']} of {out['expected_conditions']} declared conditions. "
        f"Candidate outcomes: {out['outcomes']}. Attempts: {out['attempt_counts']}.", '',
        'Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.', '',
        f"Complete assignment pairs: {out['complete_assignment_pairs']}; identical normalized histories: {out['identical_assignment_pairs']}.", '',
        '| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |',
        '| --- | --- | --- | --- |']
    for row in rows:
        values = []
        for side in (0,1):
            r = next((r for r in row['results'] if r['side']==side),None)
            values.append('unresolved' if r is None else f"{r['outcome']}, {r['hp'][0]}:{r['hp'][1]}, {r['rounds']}")
        lines.append(f"| {row['candidate']} | {row['opponent']} | {values[0]} | {values[1]} |")
    lines += ['',out['scope'],'',f'Evidence: `{args.strict}`, `{args.replay}`.','']
    with Path(args.output).with_suffix('.md').open('x') as stream:
        stream.write('\n'.join(lines))
    print(json.dumps({k:out[k] for k in ('time_utc','valid_conditions','expected_conditions','outcomes','identical_assignment_pairs')}))


if __name__=='__main__':
    main()
