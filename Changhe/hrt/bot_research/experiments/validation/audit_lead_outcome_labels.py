"""Check whether the lead matrix's W-D-L footer uses the game winner.

This audits reporting semantics, not bot strength or source provenance of
historical lead campaigns. A real independently replayed draw supplies the
small regression fixture. The lead's files are read and invoked unmodified.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
from bot_research.experiments.lead import matrix
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now, read_result
from bot_research.experiments.validation.replay_audit import audit_row


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def classify(row):
    side = row['candidate_side']
    winner = row['winner']
    true = 'D' if winner is None else ('W' if winner == side else 'L')
    margin = row['hp_diff_a'] * (1 if side == 0 else -1)
    sign = 'D' if margin == 0 else ('W' if margin > 0 else 'L')
    return true, sign, margin


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', nargs='+', required=True)
    parser.add_argument('--fixture-result', required=True)
    parser.add_argument('--fixture-output', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    inputs = {p: digest(p) for p in args.inputs}
    matrix_path = Path(matrix.__file__).relative_to(Path.cwd())
    inputs[str(matrix_path)] = digest(matrix_path)
    campaigns = []
    for filename in args.inputs:
        groups = defaultdict(lambda: {'winner_based': Counter(), 'margin_sign': Counter()})
        mismatches, errors = [], 0
        for index, line in enumerate(Path(filename).read_text().splitlines()):
            row = json.loads(line)
            if row.get('error'):
                errors += 1
                continue
            true, sign, margin = classify(row)
            candidate = row['spec_a'] if row['candidate_side'] == 0 else row['spec_b']
            groups[candidate]['winner_based'][true] += 1
            groups[candidate]['margin_sign'][sign] += 1
            if true != sign:
                mismatches.append({'row_index': index, 'candidate': candidate,
                    'scenario': row.get('scenario'), 'winner_based': true, 'margin_sign': sign,
                    'candidate_hp_margin': margin, 'hp': [row['hp_a'], row['hp_b']],
                    'winner': row['winner'], 'reason': row['reason'], 'log': row['log']})
        captured = io.StringIO()
        with redirect_stdout(captured):
            matrix.main([filename])
        campaigns.append({'input': filename, 'groups': groups, 'mismatches': mismatches,
                          'skipped_error_rows': errors,
                          'actual_matrix_footer': captured.getvalue().splitlines()[-1]})
    path = Path(args.fixture_result)
    directory = path.parent.parent
    freeze_path = directory/'freeze.json'
    job_path = directory/'jobs'/(path.stem+'.json')
    metadata = json.loads(freeze_path.read_text())
    job = json.loads(job_path.read_text())
    row = read_result(path, job, metadata['source_sha256'])
    assert not any(row['bot_errors']) and not any(row['rejected_actions'])
    assert not row['source_changed_during_match']
    replay = audit_row(row)
    assert row['result']['winner'] is None and row['hp'][0] != row['hp'][1]
    fixture = {'candidate_side': row['condition']['candidate_side'],
               'winner': row['result']['winner'], 'reason': row['result']['reason'],
               'spec_a': 'actual_draw:player0', 'spec_b': 'actual_draw:player1',
               'hp_a': row['hp'][0], 'hp_b': row['hp'][1],
               'hp_diff_a': row['hp'][0]-row['hp'][1]}
    fixture_path = Path(args.fixture_output)
    with fixture_path.open('x') as out:
        out.write(json.dumps(fixture, sort_keys=True)+'\n')
    captured = io.StringIO()
    with redirect_stdout(captured):
        matrix.main([str(fixture_path)])
    true, sign, margin = classify(fixture)
    assert true == 'D' and sign != 'D'
    for p in (path, freeze_path, job_path, Path(row['replay_path']), fixture_path):
        inputs[str(p)] = digest(p)
    changed = [p for p,h in inputs.items() if digest(p) != h]
    result = {'time_utc': now(), 'checker_sha256': digest(__file__),
              'input_sha256': inputs, 'source_changed_during_check': changed,
              'campaigns': campaigns, 'fixture': {'source_result': str(path),
              'source_engine_replay': replay, 'projection': fixture,
              'matrix_output': captured.getvalue(), 'correct_outcome': true,
              'incorrect_margin_sign_outcome': sign},
              'scope': 'Reporting-label audit only. Historical lead matches are not independently source-validated here; the projected draw fixture is source-checked and replayed. Both-base destruction is a draw regardless of residual negative HP.'}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({'fixture_correct': true, 'fixture_footer': captured.getvalue().splitlines()[-1],
        'campaign_mismatches': {c['input']: len(c['mismatches']) for c in campaigns},
        'source_changed': changed}))


if __name__ == '__main__':
    main()
