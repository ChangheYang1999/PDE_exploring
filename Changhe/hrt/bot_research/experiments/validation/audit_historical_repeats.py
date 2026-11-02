"""Compare explicitly selected historical pairs from a fixed policy perspective."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_team_labels import invalid_reasons, replay
from bot_research.experiments.validation.summarize_identifying import canonical_replay
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    started = time.perf_counter()
    manifest = json.loads(Path(args.manifest).read_text())
    inputs = {args.manifest: digest(args.manifest)}
    sources = {str(p): digest(p) for p in static_closure(
        {'bot_research.experiments.validation.audit_historical_repeats'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    checked, comparisons = {}, []
    for pair in manifest['pairs']:
        cases = []
        for selected in pair['rows']:
            name, index = selected['stream'], selected['row_index']
            identity = (name, index)
            if identity not in checked:
                inputs[name] = digest(name)
                row = [json.loads(line) for line in Path(name).read_text().splitlines()][index]
                assert not invalid_reasons(row), (identity, invalid_reasons(row))
                specs = [row['spec_a'], row['spec_b']]
                assert specs.count(manifest['perspective_spec']) == 1
                side = specs.index(manifest['perspective_spec'])
                assert all(digest(p) == h for p, h in row['sources'].items())
                inputs.update(row['sources'])
                inputs[row['log']] = digest(row['log'])
                checked[identity] = dict(stream=name, row_index=index, perspective_side=side,
                    ordered_specs=specs[::1 if side == 0 else -1], scenario=row['scenario'],
                    ordered_versions=[row['version_a'],row['version_b']][::1 if side == 0 else -1],
                    outcome='D' if row['winner'] is None else 'W' if row['winner'] == side else 'L',
                    hp=[row['hp_a'],row['hp_b']][::1 if side == 0 else -1], rounds=row['rounds'],
                    replay_path=row['log'], canonical_sha256=canonical_replay(row['log'], side),
                    original_engine_replay=replay(row, inputs, sources) if args.replay else None)
            cases.append(checked[identity])
        assert len(cases) == 2
        left, right = cases
        assert all(left[k] == right[k] for k in ('ordered_specs','ordered_versions','scenario','perspective_side'))
        comparisons.append(dict(label=pair['label'], cases=cases,
            same_complete_trajectory=left['canonical_sha256'] == right['canonical_sha256'],
            same_outcome=(left['outcome'],left['hp'],left['rounds']) == (right['outcome'],right['hp'],right['rounds'])))
    assert all(digest(p) == h for p,h in {**inputs,**sources}.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-started,
        input_sha256=inputs, source_sha256=sources, comparisons=comparisons,
        original_engine_replay_performed=args.replay,
        scope='Explicit historical repeat comparisons with exact policy specifications, static closure versions, scenario and player assignment. All recorded errors and source drift are excluded. Canonical histories remove player names, match metadata and cross-player event-order indices only. No fresh policy execution or universal determinism conclusion.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps(dict(time_utc=result['time_utc'],runtime_seconds=result['runtime_seconds'],pairs=len(comparisons),same_trajectories=sum(p['same_complete_trajectory'] for p in comparisons),replayed=args.replay)),flush=True)

if __name__ == '__main__':
    main()
