#!/usr/bin/env python3
"""Read-only, manifest-directed final source and research-copy identity check."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, time

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'certificates/source_manifest.json'
SOURCE = ROOT.parent / 'source'
COPY = ROOT / 'research_copy'

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        while chunk := stream.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()

def main():
    started = datetime.now(timezone.utc).isoformat()
    tick = time.monotonic()
    manifest = json.loads(MANIFEST.read_text())
    paths = [row['path'] for row in manifest['files']]
    assert len(paths) == len(set(paths)), 'Repeated input path'
    records = []
    for row in manifest['files']:
        rel = Path(row['path'])
        assert not rel.is_absolute() and '..' not in rel.parts
        assert rel.parts[0] in ('case1', 'analysis1')
        pair = {}
        for label, base in [('source', SOURCE), ('research_copy', COPY)]:
            file = base / rel
            assert file.is_file() and not file.is_symlink(), str(file)
            size = file.stat().st_size
            digest = sha(file)
            assert size == row['bytes'], f'Size mismatch: {file}'
            assert digest == row['sha256'], f'SHA256 mismatch: {file}'
            pair[label] = {'bytes': size, 'sha256': digest}
        records.append({'path': row['path'], **pair})
    elapsed = time.monotonic() - tick
    result = {
        'started_utc': started,
        'finished_utc': datetime.now(timezone.utc).isoformat(),
        'elapsed_seconds': elapsed,
        'method': 'Read exactly the files named in the initial manifest, each original and copy. No source traversal, write, import or execution.',
        'scope': 'Identity of the manifest-listed files, not mathematical validation and not a scan for extra files.',
        'source_commit_recorded': manifest['commit'],
        'source_commit_file': (SOURCE / 'REPO_COMMIT').read_text().strip(),
        'source_manifest_sha256': sha(MANIFEST),
        'code_sha256': sha(Path(__file__).resolve()),
        'file_count': len(records),
        'bytes_each_tree': sum(row['bytes'] for row in manifest['files']),
        'all_match': True,
        'files': records,
    }
    out = ROOT / 'certificates/source_integrity_final.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items() if key != 'files'}, indent=2))
    print('certificate_sha256', sha(out))

if __name__ == '__main__':
    main()
