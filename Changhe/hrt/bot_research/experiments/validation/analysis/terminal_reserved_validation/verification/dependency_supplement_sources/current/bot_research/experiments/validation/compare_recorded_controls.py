"""Check exact trajectory equality for explicitly paired repeat controls.

The rows and their source attestations are checked afresh. Original-engine
replay validity is established separately by replay_audit; this check compares
the complete recorded histories after only player/name/order normalization.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now, read_result
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked_row(filename, inputs):
    path = Path(filename)
    directory = path.parent.parent
    freeze = directory / 'freeze.json'
    jobfile = directory / 'jobs' / (path.stem + '.json')
    metadata = json.loads(freeze.read_text())
    job = json.loads(jobfile.read_text())
    row = read_result(path, job, metadata['source_sha256'])
    assert not any(row['bot_errors']) and not any(row['rejected_actions'])
    assert not row['source_changed_during_match']
    replay = Path(row['replay_path'])
    assert digest(replay) == row['trajectory_sha256']
    for source in (path, freeze, jobfile, replay):
        inputs[str(source)] = digest(source)
    side = row['condition']['candidate_side']
    return {'result_path': filename, 'condition': row['condition'],
            'outcome': row['candidate_outcome'],
            'hp_candidate_first': row['hp'][::1 if side == 0 else -1],
            'rounds': row['rounds'],
            'decision_seconds_candidate_first': row['decision_seconds'][::1 if side == 0 else -1],
            'canonical_replay_sha256': canonical_replay(replay, side)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pairs', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    pairs = json.loads(Path(args.pairs).read_text())
    inputs = {args.pairs: digest(args.pairs)}
    checked = []
    for pair in pairs:
        a = checked_row(pair['a'], inputs)
        b = checked_row(pair['b'], inputs)
        equal = a['canonical_replay_sha256'] == b['canonical_replay_sha256']
        assert equal == pair.get('same', True), (pair['label'], equal)
        checked.append({'label': pair['label'], 'a': a, 'b': b,
                        'same_complete_trajectory': equal})
    output = {'time_utc': now(), 'all_passed': True, 'pairs': checked,
              'input_sha256': inputs, 'checker_sha256': digest(__file__),
              'scope': 'Explicit deterministic repeat controls. Equality includes every submitted action and recorded state; repeated games do not add independent evidence.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'all_passed': True, 'pairs': len(checked),
                      'same_complete_trajectory': sum(p['same_complete_trajectory'] for p in checked)}))


if __name__ == '__main__':
    main()
