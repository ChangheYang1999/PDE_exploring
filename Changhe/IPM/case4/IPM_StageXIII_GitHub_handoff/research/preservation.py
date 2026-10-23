#!/usr/bin/env python3
"""Exact SHA-256, link, permission and nanosecond-mtime preservation audit.

No protected tree is ever written. This absolute-loss workspace is outside all
six protected roots, which include the previous Stage XII campaign, so fresh
audit records cannot alter the preservation inventory itself.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import time

HERE = Path(__file__).resolve().parent
ROOTS = [Path('/Users/caltech/Changhe/IPM/IPM_R2'),
         Path('/Users/caltech/research/IPM_R2_macpro_reference_20261020'),
         Path('/Users/caltech/research/IPM_R2_macpro_runs/verification_20261020_01'),
         Path('/Users/caltech/research/IPM_R2_macpro_experiments/stage11_five_taylor'),
         Path('/Users/caltech/research/IPM_R2_macpro_experiments/stage12_large_scale'),
         Path('/Users/caltech/research/IPM_R2_macpro_experiments/stage12_absolute_loss')]


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def inventory():
    rows = {}
    for root in ROOTS:
        paths = [root]
        for directory, dirs, files in os.walk(root, followlinks=False):
            paths.extend(Path(directory) / name for name in dirs + files)
        for path in paths:
            observed = path.lstat()
            row = {'mode': stat.S_IMODE(observed.st_mode),
                   'mtime_ns': observed.st_mtime_ns}
            if path.is_symlink():
                row.update(type='symlink', target=os.readlink(path))
            elif path.is_dir():
                row['type'] = 'directory'
            elif path.is_file():
                row.update(type='file', bytes=observed.st_size, sha256=digest(path))
            else:
                raise ValueError('unexpected filesystem type: ' + str(path))
            rows[str(path)] = row
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['snapshot', 'verify'])
    args = parser.parse_args()
    baseline = HERE / 'provenance/preservation_before.json'
    if args.mode == 'snapshot':
        if baseline.exists():
            raise ValueError('initial preservation baseline already exists')
        record = {'epoch': time.time(), 'roots': list(map(str, ROOTS)),
                  'entries': inventory()}
        with baseline.open('x') as stream:
            json.dump(record, stream, indent=2)
            stream.write('\n')
        baseline.chmod(0o444)
        print(json.dumps({'protected_entries': len(record['entries']),
                          'files': sum(v['type'] == 'file' for v in record['entries'].values())}))
        return
    before = json.loads(baseline.read_text())['entries']
    after = inventory()
    errors = [{'path': path, 'before': before.get(path), 'after': after.get(path)}
              for path in sorted(set(before) | set(after)) if before.get(path) != after.get(path)]
    record = {'passed': not errors, 'checked_entries': len(before),
              'files': sum(v['type'] == 'file' for v in before.values()),
              'errors': errors, 'epoch': time.time(), 'roots': list(map(str, ROOTS))}
    dest = HERE / 'provenance' / ('preservation_check_' + str(time.time_ns()) + '.json')
    dest.write_text(json.dumps(record, indent=2) + '\n')
    (HERE / 'provenance/preservation_latest.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'passed': not errors, 'files': record['files'],
                      'errors': len(errors), 'record': str(dest)}))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
