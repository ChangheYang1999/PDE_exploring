"""Inspect prediction coverage separately from authoritative match validity."""
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--summary', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    summary_path = Path(args.summary)
    summary = json.loads(summary_path.read_text())
    hashes = {str(summary_path): hashlib.sha256(summary_path.read_bytes()).hexdigest()}
    rows = []
    for case in summary['cases']:
        path = Path(case['result_path'])
        hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        row = json.loads(path.read_text())
        trace = row['identification_trace']
        assert sorted(t['round'] for t in trace) == list(range(1, row['rounds'] + 1))
        rows.append({'condition': case['condition'], 'outcome': case['outcome'],
                     'hp_candidate_first': case['hp_candidate_first'],
                     **{k: row[k] for k in ('rounds', 'runtime_seconds', 'trace_missing_rounds',
                         'catalogue_reset_rounds', 'forecast_model_errors', 'declared_target_model',
                         'target_model_present_rounds', 'target_forecast_mismatch_rounds',
                         'no_matching_forecast_rounds')}})
    output = {'time_utc': now(), 'input_sha256': hashes,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'valid_games': len(rows),
              'games_with_resets': sum(bool(r['catalogue_reset_rounds']) for r in rows),
              'games_with_model_errors': sum(bool(r['forecast_model_errors']) for r in rows),
              'games_with_target_prediction_mismatches': sum(bool(r['target_forecast_mismatch_rounds']) for r in rows),
              'games_with_no_matching_forecast': sum(bool(r['no_matching_forecast_rounds']) for r in rows),
              'cases': rows,
              'scope': 'Prediction diagnostics do not replace outcome validation. Timed policy replicas need not agree.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: v for k, v in output.items() if k not in ('cases', 'input_sha256')}))


if __name__ == '__main__':
    main()
