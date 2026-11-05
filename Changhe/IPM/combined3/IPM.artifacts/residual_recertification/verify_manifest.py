#!/usr/bin/env python3
"""Verify a residual certificate archive and its preserved exact inputs.

Pure Python; no Arb installation is required.  Manifest schema:
  {
    "manifest_self_excluded": true,
    "files": {"archive/relative/path": "sha256-hex", ...},
    "source_files": {"repository/relative/path": "sha256-hex", ...}
  }
The two source paths and hashes are independently fixed below.  A manifest
is an integrity record, not by itself a proof of the numerical assertions.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import sys

EXPECTED_SOURCES = {
    'Changhe/IPM/combined1/combined1.artifacts/candidates/'
    'C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json':
        'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21',
    'Changhe/IPM/combined2/IPM.artifacts/exchange/candidate_snapshots/'
    'C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/phi_007_b18s2_phi_exact.json':
        'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a',
}
FIXED_C = Fraction(4076476460239181, 2251799813685248)
DIGEST_PATTERN = re.compile(r'^[0-9a-f]{64}$')


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key: ' + str(key))
        result[key] = value
    return result


def read_json(path):
    with path.open('r', encoding='utf-8') as stream:
        return json.load(stream, object_pairs_hook=no_duplicate_keys)


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def relative_target(root, relative):
    if not isinstance(relative, str) or not relative:
        raise ValueError('Every file key must be a nonempty relative path')
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts or '\\' in relative:
        raise ValueError('Unsafe or nonportable relative path: ' + relative)
    result = (root/path).resolve()
    try:
        result.relative_to(root)
    except ValueError:
        raise ValueError('Path resolves outside its declared root: ' + relative)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path,
                        default=Path(__file__).resolve().parent/'manifest.json')
    parser.add_argument('--repo-root', type=Path, required=True)
    parser.add_argument('--artifact-root', type=Path)
    parser.add_argument('--strict', action='store_true',
                        help='Also reject archive files absent from the manifest')
    args = parser.parse_args()
    manifest_path = args.manifest.resolve()
    root = (args.artifact_root or manifest_path.parent).resolve()
    repo = args.repo_root.resolve()
    problems = []
    count = 0
    try:
        manifest = read_json(manifest_path)
        records = manifest['files']
        sources = manifest['source_files']
        if not isinstance(records, dict) or not records:
            raise ValueError('files must be a nonempty dictionary')
        if sources != EXPECTED_SOURCES:
            raise ValueError('source_files must contain exactly the fixed Candidate 007/013 bindings')
        if manifest.get('manifest_self_excluded') is not True:
            raise ValueError('manifest_self_excluded must explicitly be true')
        listed_paths = set()
        for relative, expected in sorted(records.items()):
            target = relative_target(root, relative)
            if target == manifest_path:
                raise ValueError('The manifest itself must be excluded from files')
            if target in listed_paths:
                raise ValueError('Multiple manifest paths resolve to one file: ' + relative)
            listed_paths.add(target)
            if not isinstance(expected, str) or not DIGEST_PATTERN.fullmatch(expected):
                raise ValueError('Invalid SHA256 value for ' + relative)
            if not target.is_file():
                problems.append({'path': relative, 'error': 'missing'})
                continue
            actual = digest(target)
            count += 1
            if actual != expected:
                problems.append({'path': relative, 'error': 'sha256 mismatch',
                                 'expected': expected, 'actual': actual})
        for relative, expected in EXPECTED_SOURCES.items():
            target = relative_target(repo, relative)
            if not target.is_file():
                problems.append({'source': relative, 'error': 'missing'})
                continue
            actual = digest(target)
            if actual != expected:
                problems.append({'source': relative, 'error': 'sha256 mismatch',
                                 'expected': expected, 'actual': actual})
                continue
            value = read_json(target)
            c = value['cl_exact'] if 'cl_exact' in value else value['c_exact']
            if Fraction(c) != FIXED_C:
                problems.append({'source': relative, 'error': 'fixed c mismatch'})
            if 'reference_sha256' in value:
                expected_base = next(iter(EXPECTED_SOURCES.values()))
                if value['reference_sha256'] != expected_base:
                    problems.append({'source': relative, 'error': 'Candidate 007 reference mismatch'})
        if args.strict:
            actual_paths = {p.resolve() for p in root.rglob('*') if p.is_file()}
            extra = actual_paths-listed_paths-{manifest_path}
            for target in sorted(extra):
                problems.append({'path': str(target.relative_to(root)),
                                 'error': 'file absent from manifest'})
        result = {
            'status': 'PASS' if not problems else 'FAIL',
            'manifest': str(manifest_path),
            'manifest_sha256': digest(manifest_path),
            'archive_files_checked': count,
            'exact_sources_checked': len(EXPECTED_SOURCES),
            'fixed_c_exact': str(FIXED_C),
            'strict_archive_completeness': args.strict,
            'problems': problems,
            'scope': 'Byte integrity and exact source binding; numerical proof replay is a separate check.',
        }
    except (OSError, ValueError, KeyError, TypeError) as error:
        result = {'status': 'FAIL', 'error': str(error)}
    print(json.dumps(result, indent=2))
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
