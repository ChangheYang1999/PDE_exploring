#!/usr/bin/env python3
"""Verify or restore byte-preserved inputs in the compact publication bundle."""
from pathlib import Path
import argparse, gzip, hashlib, json, os
ROOT = Path(__file__).resolve().parent

def safe_path(name):
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT) or path == ROOT:
        raise ValueError('Invalid manifest path: ' + name)
    return path

def sha(data):
    return hashlib.sha256(data).hexdigest()

def verify(restore=False):
    manifest = json.loads((ROOT / 'MANIFEST.json').read_text())
    restored = 0
    for row in manifest['files']:
        stored = safe_path(row['stored_path'])
        data = stored.read_bytes()
        if len(data) != row['stored_bytes'] or sha(data) != row['stored_sha256']:
            raise ValueError('Stored-file checksum failed: ' + row['stored_path'])
        original = gzip.decompress(data) if row['encoding'] == 'gzip' else data
        if len(original) != row['bytes'] or sha(original) != row['sha256']:
            raise ValueError('Original-file checksum failed: ' + row['path'])
        if restore and row['encoding'] == 'gzip':
            target = safe_path(row['path'])
            if target.exists():
                if sha(target.read_bytes()) != row['sha256']:
                    raise ValueError('Refusing to overwrite changed file: ' + row['path'])
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open('xb') as f:
                    f.write(original)
                restored += 1
    return dict(file_count=len(manifest['files']), restored=restored,
                original_bytes=sum(x['bytes'] for x in manifest['files']),
                stored_bytes=sum({x['stored_path']:x['stored_bytes'] for x in manifest['files']}.values()),
                status='PASS')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['verify', 'restore'])
    args = parser.parse_args()
    print(json.dumps(verify(args.action == 'restore'), indent=2))
