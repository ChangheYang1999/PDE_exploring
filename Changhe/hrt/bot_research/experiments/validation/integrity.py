"""Read-only protected-tree inventory, including the pre-existing virtualenv."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def inventory(root: Path) -> dict:
    result = {}
    for directory, subdirs, files in os.walk(root, followlinks=False):
        if Path(directory) == root:
            subdirs[:] = [p for p in subdirs if p != 'bot_research']
        for name in files + [d for d in subdirs if (Path(directory) / d).is_symlink()]:
            path = Path(directory) / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                data = os.readlink(path).encode()
                result[relative] = {'kind': 'symlink', 'sha256': hashlib.sha256(data).hexdigest()}
            else:
                result[relative] = {'kind': 'file', 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}
    return dict(sorted(result.items()))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--baseline')
    args = parser.parse_args()
    root = Path.cwd()
    current = inventory(root)
    manifest = json.loads((root / 'bot_research/protected_files.sha256.json').read_text())
    missing = sorted(set(manifest) - set(current))
    changed = {p: {'manifest': h, 'actual': current[p]['sha256']} for p, h in manifest.items() if p in current and current[p]['sha256'] != h}
    result = {'time_utc': datetime.now(timezone.utc).isoformat(), 'inventory': current,
              'manifest_missing': missing, 'manifest_changed': changed,
              'outside_manifest': sorted(set(current) - set(manifest)),
              'virtualenv_existed_before_T0': True}
    if args.baseline:
        previous = json.loads(Path(args.baseline).read_text())['inventory']
        result['baseline_comparison'] = {'added': sorted(set(current) - set(previous)),
             'removed': sorted(set(previous) - set(current)),
             'changed': sorted(p for p in set(current) & set(previous) if current[p] != previous[p])}
    with Path(args.output).open('x') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({'time_utc': result['time_utc'], 'files_outside_research': len(current),
          'manifest_missing': len(missing), 'manifest_changed': sorted(changed),
          'baseline_comparison': result.get('baseline_comparison')}))


if __name__ == '__main__':
    main()
