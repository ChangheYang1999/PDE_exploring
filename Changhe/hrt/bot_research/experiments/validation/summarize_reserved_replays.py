"""Link each selected reserved result to a checked original-engine replay.

This consumes the independent campaign accounting and per-attempt replay
receipts. It does not rerun policies, create strength samples, or silently
replace a failed match with an outcome inferred from its partial replay.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def summarize(campaign_audit, audit_dirs):
    campaign = json.loads(Path(campaign_audit).read_text())
    inputs = {str(campaign_audit): digest(campaign_audit)}
    source_paths = set(static_closure({'td_game.engine'})) | {Path('td_game/balanced.json')}
    expected_engine = {str(path): digest(path) for path in source_paths}
    receipts, attempts, failed_computations = defaultdict(list), [], []
    for directory in audit_dirs:
        directory = Path(directory)
        for path in sorted((directory / 'failures').glob('*.json')):
            inputs[str(path)] = digest(path)
            failed_computations.append({'path': str(path), 'record': json.loads(path.read_text())})
        for path in sorted((directory / 'audits').glob('*.json')):
            inputs[str(path)] = digest(path)
            record = json.loads(path.read_text())
            attempt = {'audit_path': str(path), 'time_utc': record['time_utc']}
            try:
                if not record['all_passed'] or record['source_changed_during_run']:
                    raise ValueError('Replay receipt did not pass.')
                if record['count'] != len(record['cases']) or not record['cases']:
                    raise ValueError('Replay receipt has inconsistent case counts.')
                for name, value in expected_engine.items():
                    if record['source_sha256'].get(name) != value:
                        raise ValueError('Replay engine differs from the current protected engine: ' + name)
                for name, value in record['source_sha256'].items():
                    if digest(name) != value:
                        raise ValueError('Replay checker source has changed: ' + name)
                for name, value in record['input_sha256'].items():
                    if digest(name) != value:
                        raise ValueError('Replay input has changed: ' + name)
                    inputs[name] = value
                for case in record['cases']:
                    if not case['passed'] or case['row_index'] != 0:
                        raise ValueError('Only passing single-JSON result cases are accepted.')
                    row = json.loads(Path(case['input']).read_text())
                    for name in ('condition', 'hp', 'result', 'rounds', 'trajectory_sha256'):
                        if row[name] != case[name]:
                            raise ValueError('Replay receipt differs from result field: ' + name)
                attempt.update(valid=True, runtime_seconds=record['runtime_seconds'],
                               result_paths=[case['input'] for case in record['cases']])
                for case in record['cases']:
                    receipts[case['input']].append({'audit_path': str(path), 'time_utc': record['time_utc'],
                                                    'trajectory_sha256': case['trajectory_sha256']})
            except (ValueError, KeyError, TypeError, OSError) as error:
                attempt.update(valid=False, diagnostic=public_diagnostic(str(error)))
            attempts.append(attempt)
    selected, missing = [], []
    for case in campaign['cases']:
        result_path = case['result_path']
        replay_path = case['replay_path']
        for name in (result_path, replay_path):
            value = digest(name)
            if campaign['input_sha256'].get(name) != value:
                raise ValueError('Campaign input has changed: ' + name)
            inputs[name] = value
        valid = sorted(receipts[result_path], key=lambda value: value['time_utc'])
        if not valid:
            missing.append({'job': case['job'], 'result_path': result_path})
        else:
            if valid[0]['trajectory_sha256'] != inputs[replay_path]:
                raise ValueError('Selected replay digest differs from campaign evidence.')
            selected.append({'job': case['job'], 'result_path': result_path, **valid[0]})
    complete = (campaign['valid_conditions'] == campaign['expected_conditions']
                and not campaign['unresolved'] and not campaign['repeat_disagreements'] and not missing)
    return {'time_utc': now(), 'input_sha256': inputs,
            'checker_sha256': digest(__file__), 'protected_engine_sha256': expected_engine,
            'candidate': campaign['candidate'], 'candidate_sha256': campaign['candidate_sha256'],
            'pool': campaign['pool'], 'expected_conditions': campaign['expected_conditions'],
            'valid_matches': campaign['valid_conditions'], 'verified_primary_replays': len(selected),
            'all_primary_conditions_completed_and_replayed': complete,
            'missing_primary_replays': missing, 'unresolved_matches': campaign['unresolved'],
            'selected_replay_receipts': selected, 'replay_attempts': attempts,
            'replay_computational_failures': failed_computations,
            'match_attempt_counts': campaign['attempt_counts'],
            'scores_by_scenario': campaign['scores_by_scenario'],
            'paired_assignments_checked': len(campaign['pairs']),
            'all_pairs_have_both_assignments': all(p['exactly_two_assignments'] for p in campaign['pairs']),
            'all_paired_trajectories_identical': all(p['same_complete_trajectory'] for p in campaign['pairs']),
            'scope': campaign['scope']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign-audit', required=True)
    parser.add_argument('--audit-dirs', nargs='+', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--allow-incomplete', action='store_true')
    args = parser.parse_args()
    output = summarize(args.campaign_audit, args.audit_dirs)
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({key: output[key] for key in ('valid_matches', 'verified_primary_replays',
          'expected_conditions', 'all_primary_conditions_completed_and_replayed', 'missing_primary_replays')}))
    if not output['all_primary_conditions_completed_and_replayed'] and not args.allow_incomplete:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
