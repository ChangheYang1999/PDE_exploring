"""Compare explicit repeat controls with possibly opposite candidate labels."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pairs', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    pairs = json.loads(Path(args.pairs).read_text())
    inputs = {args.pairs: digest(args.pairs)}
    results = []
    for pair in pairs:
        views = {}
        for label in ('a','b'):
            checked = checked_row(pair[label],inputs)
            row = json.loads(Path(pair[label]).read_text())
            side = checked['condition']['candidate_side'] ^ bool(pair.get(label+'_flip',False))
            views[label] = {'checked_result':checked,'reference_side':side,
                           'reference_hp':row['hp'][::1 if side==0 else -1],
                           'reference_replay_sha256':canonical_replay(row['replay_path'],side)}
        equal = views['a']['reference_replay_sha256']==views['b']['reference_replay_sha256']
        assert equal == pair.get('same',True), (pair['label'],equal)
        results.append({'label':pair['label'],**views,'same_complete_trajectory':equal})
    result = {'time_utc':now(),'checker_sha256':digest(__file__),'input_sha256':inputs,
              'all_passed':True,'pairs':results,
              'scope':'Explicit deterministic repeat controls after declared player-orientation normalization. Original-engine replay is a separate check. Repeated conditions add no independent strength evidence.'}
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({'all_passed':True,'pairs':len(results),'identical':sum(r['same_complete_trajectory'] for r in results)}))


if __name__ == '__main__':
    main()
