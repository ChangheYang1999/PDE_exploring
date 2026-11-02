"""Verify all forecast diagnostics directly from the recorded submissions."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--inputs', nargs='+', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    cases, hashes = [], {}
    for name in args.inputs:
        path = Path(name)
        hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        for index, line in enumerate(path.read_text().splitlines()):
            row = json.loads(line)
            side = row['condition'].get('counter_side', row['condition'].get('candidate_side'))
            if side not in (0, 1):
                raise ValueError('Missing forecast perspective.')
            records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
            submissions = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
                           for r in records if r['round'] > 0 and r['player'] == 1 - side}
            trace = row['forecast_trace']
            if [t['round'] for t in trace] != list(range(1, row['rounds'] + 1)):
                raise ValueError('Incomplete, duplicate, or reordered forecast trace.')
            differing = [t['round'] for t in trace if t['predicted_actions'] != submissions[t['round']]]
            if differing != row['forecast_mismatch_rounds'] or row['forecast_trace_missing_rounds']:
                raise ValueError('Stored forecast diagnostics differ from the submissions.')
            source_changes = {name for name in row['source_sha256'] if row['source_sha256_at_end'].get(name) != row['source_sha256'][name]}
            if source_changes or row['source_changed_during_match']:
                raise ValueError('Source drift in a forecast game.')
            cases.append({'input': name, 'index': index, 'condition': row['condition'],
                          'rounds_checked': len(trace), 'forecast_mismatch_rounds': differing})
    output = {'time_utc': now(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256': hashes, 'cases': cases, 'count': len(cases),
              'rounds_checked': sum(c['rounds_checked'] for c in cases),
              'games_with_forecast_mismatch': sum(bool(c['forecast_mismatch_rounds']) for c in cases),
              'scope': 'Diagnostic audit against recorded target submissions. Full original-engine replay is a separate check.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('count', 'rounds_checked', 'games_with_forecast_mismatch')}))


if __name__ == '__main__':
    main()
