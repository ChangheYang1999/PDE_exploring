#!/usr/bin/env python3
"""Verify packed evidence, unpack outside Git, and replay existing IPM checks."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
import tarfile
import tempfile
import time
from pathlib import Path, PurePosixPath

BLOCK = 1024 * 1024


def relative(value):
    if not isinstance(value, str) or not value or '\\' in value or ':' in value:
        raise ValueError(f'Invalid relative path: {value!r}')
    path = PurePosixPath(value)
    if path.is_absolute() or '..' in path.parts or path.as_posix() != value:
        raise ValueError(f'Unsafe relative path: {value!r}')
    return path


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def digest(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(BLOCK), b''):
            value.update(chunk)
    return value.hexdigest()


def record(value):
    if (not isinstance(value, dict) or type(value.get('bytes')) is not int
            or value['bytes'] < 0 or not isinstance(value.get('sha256'), str)
            or re.fullmatch('[0-9a-f]{64}', value['sha256']) is None):
        raise ValueError('Invalid byte count or SHA-256 record')


def copy_checked(stream, destination, expected):
    destination.parent.mkdir(parents=True, exist_ok=True)
    value, count = hashlib.sha256(), 0
    with destination.open('xb') as output:
        for chunk in iter(lambda: stream.read(BLOCK), b''):
            count += len(chunk)
            if count > expected['bytes']:
                raise ValueError(f'Oversized payload: {destination}')
            output.write(chunk)
            value.update(chunk)
    if count != expected['bytes'] or value.hexdigest() != expected['sha256']:
        raise ValueError(f'Payload integrity failure: {destination}')


def output_root(requested, source):
    root = requested.expanduser().resolve() if requested else Path(
        tempfile.mkdtemp(prefix='ipm-combined3-evidence-')).resolve()
    forbidden = next((p for p in (source, *source.parents)
                      if (p / '.git').exists()), source)
    if root.is_relative_to(forbidden):
        raise ValueError('The extraction directory must be outside the Git working tree')
    if root.exists() and (not root.is_dir() or any(root.iterdir())):
        raise FileExistsError('The output directory must be empty or nonexistent')
    root.mkdir(parents=True, exist_ok=True)
    return root


def materialize(source, index_path, requested):
    index = json.loads(index_path.read_text(), object_pairs_hook=unique_keys)
    if index.get('format_version') != 1:
        raise ValueError('Unsupported evidence-index format')
    scope = relative(index['scope'])
    sources, evidence, packs = index['source_files'], index['evidence_files'], index['packs']
    if not isinstance(sources, dict) or not isinstance(evidence, dict) or not isinstance(packs, list):
        raise ValueError('Malformed evidence index')
    if set(sources) & set(evidence):
        raise ValueError('Source and evidence paths overlap')
    for name, value in {**sources, **evidence}.items():
        relative(name)
        record(value)
    source_paths = {name: source / Path(*relative(name).relative_to(scope).parts)
                    for name in sources}
    pack_paths, assigned = {}, set()
    for pack in packs:
        record(pack)
        name = pack['file']
        suffix = relative(name).relative_to('IPM.evidence')
        path = (index_path.parent / Path(*suffix.parts)).resolve()
        if name in pack_paths or not path.is_relative_to(index_path.parent.resolve()):
            raise ValueError(f'Duplicate or unsafe evidence pack: {name}')
        members = pack['members']
        if not isinstance(members, list) or len(set(members)) != len(members):
            raise ValueError(f'Invalid pack member list: {name}')
        for member in members:
            relative(member)
            if member in assigned or member not in evidence or evidence[member]['pack'] != name:
                raise ValueError(f'Invalid pack membership: {member}')
            assigned.add(member)
        if path.stat().st_size != pack['bytes'] or digest(path) != pack['sha256']:
            raise ValueError(f'Pack integrity failure: {path}')
        pack_paths[name] = path
    if assigned != set(evidence):
        raise ValueError('The pack lists do not cover the evidence index exactly')
    for name, path in source_paths.items():
        if path.stat().st_size != sources[name]['bytes'] or digest(path) != sources[name]['sha256']:
            raise ValueError(f'Source integrity failure: {path}')
    root = output_root(requested, source)
    for name, path in source_paths.items():
        with path.open('rb') as stream:
            copy_checked(stream, root / Path(*relative(name).parts), sources[name])
    extracted = set()
    for pack in packs:
        members = set(pack['members'])
        with tarfile.open(pack_paths[pack['file']], mode='r|xz') as archive:
            for entry in archive:
                name = entry.name
                relative(name)
                if (not entry.isfile() or name not in members or name in extracted
                        or entry.size != evidence[name]['bytes']):
                    raise ValueError(f'Unexpected archive member: {name}')
                destination = root / Path(*relative(name).parts)
                if not destination.resolve().is_relative_to(root):
                    raise ValueError(f'Archive path escapes output root: {name}')
                stream = archive.extractfile(entry)
                if stream is None:
                    raise ValueError(f'Unreadable archive member: {name}')
                with stream:
                    copy_checked(stream, destination, evidence[name])
                extracted.add(name)
    if extracted != set(evidence):
        raise ValueError('Evidence extraction is incomplete')
    result = {'status': 'MATERIALIZED_EVIDENCE_PASS', 'workspace': str(root),
              'source_files': len(sources), 'evidence_files': len(evidence),
              'packs': len(packs), 'index_sha256': digest(index_path)}
    (root / 'MATERIALIZATION.json').write_text(json.dumps(result, indent=2) + '\n')
    return root, scope, result


def validate(root, scope, python):
    here = root / Path(*scope.parts) / 'IPM.artifacts'
    checks = root / 'verification'
    checks.mkdir()
    residual = here / 'residual_recertification'
    threshold, join, independent = (checks / name for name in
                                    ('thresholds.json', 'join.json', 'independent.json'))
    commands = [
        [python, '-B', str(residual / 'verify_manifest.py'), '--repo-root', str(root), '--strict'],
        [python, '-B', str(residual / 'verify_final_thresholds.py'), '--output', str(threshold)],
        [python, '-B', str(here / 'operator_theory/assemble_fixed_parameter_closure_v01.py'),
         '--selected-M', '3/10', '--selected-Rb', '30000', '--output', str(join)],
        [python, '-B', str(here / 'verify_final_local_Q_closure.py'), '--consumer', str(join),
         '--out', str(independent)],
    ]
    expected = ['PASS', 'PASS_INDEPENDENT_EXACT_THRESHOLDS', 'FINAL_NUMERICAL_CLOSURE_PASS',
                'ROOT_INDEPENDENT_FINAL_LOCAL_Q_NUMERICAL_PASS']
    (checks / 'commands.json').write_text(json.dumps({'cwd': str(root), 'commands': commands}, indent=2) + '\n')
    records = []
    for number, command in enumerate(commands, 1):
        log = checks / f'command_{number}.log'
        started = time.monotonic()
        with log.open('x') as output:
            run = subprocess.run(command, cwd=root, stdout=output, stderr=subprocess.STDOUT)
        data_path = [log, threshold, join, independent][number - 1]
        actual = None
        if run.returncode == 0:
            actual = json.loads(data_path.read_text()).get('status')
        passed = run.returncode == 0 and actual == expected[number - 1]
        records.append({'command': command, 'returncode': run.returncode, 'status': actual,
                        'elapsed_seconds': time.monotonic() - started, 'log': str(log), 'passed': passed})
        (checks / 'status.json').write_text(json.dumps({'records': records,
            'all_completed': len(records) == len(commands),
            'all_passed_so_far': all(row['passed'] for row in records)}, indent=2) + '\n')
        if not passed:
            raise RuntimeError(f'Check {number} failed; inspect {log}')
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, default=Path(__file__).resolve().parent,
                        help='Source directory; normally the directory containing this script')
    parser.add_argument('--index', type=Path, help='Override the adjacent IPM.evidence/index.json')
    parser.add_argument('--output-dir', type=Path, help='Empty/nonexistent directory outside Git; default: fresh system temporary directory')
    parser.add_argument('--materialize-only', action='store_true', help='Verify and unpack without running numerical checks')
    parser.add_argument('--python', default=sys.executable, help='Python interpreter with the pinned research dependencies')
    args = parser.parse_args()
    source = args.source_dir.expanduser().resolve()
    index = (args.index or source / 'IPM.evidence/index.json').expanduser().resolve()
    root, scope, result = materialize(source, index, args.output_dir)
    if not args.materialize_only:
        result['checks'] = validate(root, scope, args.python)
        result['status'] = 'PACKED_EVIDENCE_REPRODUCTION_PASS'
    (root / 'REPRODUCTION.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError, RuntimeError, tarfile.TarError) as error:
        print(f'Packed reproduction failed: {error}', file=sys.stderr)
        sys.exit(1)
