"""Summarize the complete finite timing grid and prerecord paired finalists."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.search_forecast_timing import conditions


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--inputs', nargs='+', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    rows = [json.loads(line) for file in args.inputs for line in Path(file).read_text().splitlines()]
    expected = dict(conditions())
    indexed = {row['condition']['index']: row for row in rows}
    assert len(indexed) == len(rows), 'Duplicate condition index.'
    assert set(indexed) == set(expected), 'The requested finite grid is incomplete.'
    for index, row in indexed.items():
        assert row['condition']['parameters'] == expected[index]
    invalid = [row['condition']['index'] for row in rows if any(row['bot_errors'])
               or any(row['rejected_actions']) or row['source_changed_during_match']
               or row['forecast_mismatch_rounds']]
    clean = [row for row in rows if row['condition']['index'] not in invalid]
    by_lam = defaultdict(list)
    for row in clean:
        by_lam[row['condition']['parameters']['model_lam']].append(row)
    selected = {}
    def ranking(row):
        order = {'W': 2, 'D': 1, 'L': 0}[row['counter_outcome']]
        return (order, row['hp'][0] - row['hp'][1], row['hp'][0], -row['condition']['index'])
    for lam, group in sorted(by_lam.items()):
        for row in sorted(group, key=ranking, reverse=True)[:3]:
            index = row['condition']['index']
            selected.setdefault(index, set()).add(f'top three at lam={lam}')
        wins = [row for row in group if row['counter_outcome'] == 'W']
        if wins:
            row = min(wins, key=lambda r: (r['condition']['parameters']['attack_round'],
                                          r['condition']['index']))
            selected.setdefault(row['condition']['index'], set()).add(f'earliest successful attack at lam={lam}')
    summary = {
        'time_utc': datetime.now(timezone.utc).isoformat(),
        'purpose': 'development screen; deterministic parameter conditions, not independent random trials',
        'input_sha256': {file: hashlib.sha256(Path(file).read_bytes()).hexdigest() for file in args.inputs},
        'planned_and_completed': len(rows), 'invalid_condition_indices': invalid,
        'clean_outcomes': dict(Counter(row['counter_outcome'] for row in clean)),
        'unique_clean_trajectories': len({r['trajectory_sha256'] for r in clean}),
        'by_model_lam': {str(lam): {'conditions': len(group),
            'outcomes': dict(Counter(r['counter_outcome'] for r in group)),
            'unique_trajectories': len({r['trajectory_sha256'] for r in group})}
            for lam, group in sorted(by_lam.items())},
        'selection_rule': 'Top three by outcome then final HP margin then own HP at each lam; also earliest winning timing. Tie: lower condition index.',
        'paired_finalists': [{
            'screen_index': index, 'parameters': expected[index],
            'screen_outcome': indexed[index]['counter_outcome'], 'screen_hp': indexed[index]['hp'],
            'selected_because': sorted(reasons)} for index, reasons in sorted(selected.items())],
    }
    atomic_json(args.output, summary, exclusive=True)
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    main()
