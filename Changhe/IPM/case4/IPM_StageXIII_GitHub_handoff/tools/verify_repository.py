#!/usr/bin/env python3
"""Verify the release inventory using only the Python standard library."""
import argparse
import hashlib
import json
from pathlib import Path


def sha256(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            value.update(block)
    return value.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.repo.resolve()
    manifest = json.loads((root/'metadata/repository_manifest.json').read_text())
    failures = []
    total = 0
    for row in manifest['files']:
        path = (root/row['path']).resolve()
        if root not in path.parents:
            raise ValueError('Inventory path escapes the repository')
        if not path.is_file() or path.stat().st_size != row['bytes'] or sha256(path) != row['sha256']:
            failures.append(row['path'])
        total += row['bytes']
    print(json.dumps({'passed': not failures, 'files': len(manifest['files']),
                      'bytes': total, 'failures': failures,
                      'manifest_self_hashed': False}, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
