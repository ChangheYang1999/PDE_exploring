"""Verify complete sharded development declarations and their archived inputs.

Unlike audit_data_archives, each folder contains its declared shard, and all
shards together must cover the complete Cartesian product exactly once.
"""
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import time
from bot_research.experiments.validation.artifact_io import atomic_json


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def expected_jobs(manifest, folder, shard, shards):
    jobs = []
    index = 0
    for candidate in manifest['candidates']:
        for opponent in manifest['opponents']:
            for side in (0, 1):
                if index % shards == shard:
                    identifier = f'case{index:04d}'
                    bots = [{'spec': candidate['spec']}, {'spec': opponent['spec']}]
                    names = [candidate['id'], opponent['id']]
                    if side:
                        bots.reverse()
                        names.reverse()
                    jobs.append(dict(id=identifier, names=names, bots=bots,
                        replay_path=str(folder / 'replays' / (identifier + '.jsonl')),
                        condition=dict(candidate_side=side, candidate_id=candidate['id'],
                            candidate_spec=candidate['spec'], opponent_id=opponent['id'],
                            opponent_spec=opponent['spec'], initial_state='standard',
                            engine_seed=None, purpose=manifest['purpose'],
                            strength_score_eligible=True, pool='development')))
                index += 1
    assert index == manifest['expected_conditions']
    return jobs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaigns', nargs='+', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    inputs, audits, groups = {}, [], defaultdict(list)
    for name in args.campaigns:
        folder = Path(name)
        assert not folder.is_absolute() and '..' not in folder.parts
        freeze_path = folder / 'freeze.json'
        freeze = json.loads(freeze_path.read_text())
        inputs[str(freeze_path)] = digest(freeze_path)
        manifest_files = [path for path in freeze['source_sha256']
                          if path.endswith('.json') and digest(path) == freeze['manifest_sha256']]
        assert len(manifest_files) == 1
        manifest_path = manifest_files[0]
        manifest = json.loads(Path(manifest_path).read_text())
        inputs[manifest_path] = digest(manifest_path)
        shards, shard = freeze['shards'], freeze['shard']
        assert type(shards) is int and shards > 0 and type(shard) is int and 0 <= shard < shards
        for path, sha in manifest['input_sha256'].items():
            assert freeze['source_sha256'].get(path) == sha
        for path, sha in freeze['source_sha256'].items():
            rel = Path(path)
            assert not rel.is_absolute() and '..' not in rel.parts
            assert digest(rel) == sha
            assert digest(folder / 'sources' / rel) == sha
        job_path = folder / 'jobs.json'
        inputs[str(job_path)] = digest(job_path)
        jobs = json.loads(job_path.read_text())
        assert jobs == expected_jobs(manifest, folder, shard, shards)
        for job in jobs:
            path = folder / 'results' / (job['id'] + '.json')
            assert not path.with_name(job['id'] + '.failure.json').exists()
            inputs[str(path)] = digest(path)
            row = json.loads(path.read_text())
            assert row['condition'] == job['condition']
            assert not row['source_changed_during_match']
            assert not any(row['bot_errors']) and not any(row['rejected_actions'])
            for field in ('source_sha256', 'source_sha256_at_end'):
                for source, sha in row[field].items():
                    assert freeze['source_sha256'].get(source) == sha
        audit = dict(campaign=name, shard=shard, shards=shards,
                     manifest_sha256=freeze['manifest_sha256'],
                     expected_total=manifest['expected_conditions'],
                     archived_inputs=len(freeze['source_sha256']), results=len(jobs),
                     explicit_data=[p for p in manifest['input_sha256'] if '/data/' in p and p.endswith('.json')],
                     all_passed=True)
        audits.append(audit)
        groups[freeze['manifest_sha256']].append(audit)
    coverage = []
    for sha, parts in groups.items():
        counts = {p['shards'] for p in parts}
        totals = {p['expected_total'] for p in parts}
        assert len(counts) == len(totals) == 1
        shards, total = next(iter(counts)), next(iter(totals))
        assert sorted(p['shard'] for p in parts) == list(range(shards))
        assert sum(p['results'] for p in parts) == total
        coverage.append(dict(manifest_sha256=sha, shards=shards, complete_conditions=total))
    assert all(digest(path) == sha for path, sha in inputs.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(),
        runtime_seconds=time.perf_counter()-started, checker_sha256=digest(__file__),
        input_sha256=inputs, campaigns=audits, complete_shard_groups=coverage, all_passed=True,
        scope='Exact declaration coverage and byte identity of live and archived inputs, with '
              'loaded-source receipts. Original-engine replay and policy reproduction are separate.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({key: output[key] for key in ('time_utc', 'runtime_seconds',
                                                   'campaigns', 'complete_shard_groups', 'all_passed')}))


if __name__ == '__main__':
    main()
