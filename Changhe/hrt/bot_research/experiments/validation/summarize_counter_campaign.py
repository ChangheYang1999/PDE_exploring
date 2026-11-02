"""Human-readable summary requiring matching strict, forecast and replay audits."""
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
    parser.add_argument('--forecasts', required=True)
    parser.add_argument('--replay', required=True)
    parser.add_argument('--heading', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    strict, forecasts, replay = [json.loads(Path(p).read_text()) for p in (args.strict, args.forecasts, args.replay)]
    assert forecasts['input_sha256'][args.strict] == digest(args.strict)
    assert forecasts['valid_conditions'] == strict['valid_conditions']
    assert forecasts['games_with_forecast_mismatch'] == 0
    assert replay['all_passed'] and not replay['source_changed_during_run']
    replayed = {c['trajectory_sha256'] for c in replay['cases'] if c['passed']}
    grouped = defaultdict(list)
    forecast_rounds = 0
    for case in strict['attempts']:
        if case['status'] != 'valid':
            continue
        path = case['result_path']
        assert digest(path) == strict['input_sha256'][path] == forecasts['input_sha256'][path]
        result = json.loads(Path(path).read_text())
        assert result['trajectory_sha256'] in replayed
    for case in strict['cases']:
        result = json.loads(Path(case['result_path']).read_text())
        forecast_rounds += len(result['forecast_trace'])
        grouped[(case['condition']['candidate_id'], case['condition']['opponent_id'])].append(dict(
            side=case['condition']['candidate_side'], outcome=case['outcome'], hp=case['hp_candidate_first'],
            rounds=case['rounds'], runtime_seconds=case['runtime_seconds'], result_path=case['result_path'],
            attacks=[{k:t[k] for k in ('round','attack_count','attack_tier','forecast_attack_gain','selected_sequence') if k in t}
                     for t in result['forecast_trace'] if t.get('attack_count')]))
    rows = [dict(candidate=k[0], opponent=k[1], results=sorted(v,key=lambda r:r['side'])) for k,v in grouped.items()]
    stamp = datetime.now(timezone.utc).isoformat()
    out = dict(time_utc=stamp, heading=args.heading,
        input_sha256={p:digest(p) for p in (args.strict,args.forecasts,args.replay)},
        checker_sha256=digest(__file__), valid_conditions=strict['valid_conditions'],
        expected_conditions=strict['expected_conditions'], attempt_counts=strict['attempt_counts'],
        unresolved_conditions=len(strict['unresolved']),
        outcomes=dict(Counter(c['outcome'] for c in strict['cases'])), primary_forecast_rounds=forecast_rounds,
        complete_assignment_pairs=sum(p['exactly_two_assignments'] for p in strict['pairs']),
        identical_assignment_pairs=sum(p['same_complete_trajectory'] for p in strict['pairs']),
        repeat_disagreements=strict['repeat_disagreements'], rows=rows,
        scope='Exact stated development conditions. Both assignments are controls, not independent random samples; known-prefix scenarios are excluded from standard-start strength totals.')
    atomic_json(args.output, out, exclusive=True)
    md = Path(args.output).with_suffix('.md')
    lines = [f'# {args.heading}', '', f'Recorded: {stamp}', '',
        f"Completed {out['valid_conditions']} of {out['expected_conditions']} declared conditions. "
        f"Outcomes from the counter side: {out['outcomes']}. Attempts: {out['attempt_counts']}.", '',
        'All selected completions pass strict source and legality checks, exact forecast checks, and full unchanged-engine replay. '
        'Unresolved attempts remain unresolved; timeouts are not losses.', '',
        f"Exact primary forecast rounds: {forecast_rounds}. Complete assignment pairs: {out['complete_assignment_pairs']}; "
        f"identical normalized histories: {out['identical_assignment_pairs']}. Asymmetric openings can legitimately differ.", '',
        '| Counter | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |', '| --- | --- | --- | --- |']
    for row in rows:
        values = []
        for side in (0,1):
            r = next((r for r in row['results'] if r['side']==side), None)
            values.append('unresolved' if r is None else f"{r['outcome']}, {r['hp'][0]}:{r['hp'][1]}, {r['rounds']}")
        lines.append(f"| {row['candidate']} | {row['opponent']} | {values[0]} | {values[1]} |")
    lines += ['', out['scope'], '', 'Evidence: '+', '.join(f'`{p}`' for p in out['input_sha256'])+'.', '']
    with md.open('x') as f:
        f.write('\n'.join(lines))
    print(json.dumps({k:out[k] for k in ('time_utc','valid_conditions','expected_conditions','outcomes','primary_forecast_rounds')}))


if __name__ == '__main__':
    main()
