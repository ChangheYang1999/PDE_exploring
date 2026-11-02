"""Audit owned artifact paths, recognizing one frozen generic prefix guard."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
from bot_research.experiments.validation.artifact_io import atomic_json


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--guard-receipt', required=True)
    args = parser.parse_args()
    guard = json.loads(Path(args.guard_receipt).read_text())['generic_prefix_guard']
    roots = [Path('bot_research/bots/counters'), Path('bot_research/experiments/validation'),
             Path('bot_research/runs/validation'), Path('bot_research/notes/validation.md')]
    pattern = re.compile(r'(?<![A-Za-z0-9_.-])/(?:' + '|'.join(('mnt', 'home', 'efs', 'tmp')) + r')(?:/|\b)')
    matched, generic, inventory = [], [], {}
    checked = 0
    for root in roots:
        files = size = 0
        for path in ([root] if root.is_file() else root.rglob('*')):
            if not path.is_file():
                continue
            files += 1
            size += path.stat().st_size
            if path.suffix.lower() not in ('.py', '.json', '.jsonl', '.md', '.txt', '.log', '.out', '.csv'):
                continue
            checked += 1
            try:
                with path.open() as stream:
                    for number, line in enumerate(stream, 1):
                        if not pattern.search(line):
                            continue
                        row = dict(path=str(path), line=number)
                        if (str(path) == guard['path'] and number == guard['line']
                                and digest(line.encode()) == guard['line_sha256']
                                and digest(path.read_bytes()) == guard['source_sha256']):
                            generic.append(row)
                        else:
                            matched.append(row)
            except UnicodeError:
                matched.append(dict(path=str(path), issue='non-text content with text suffix'))
        inventory[str(root)] = dict(files=files, bytes=size)
    lane = Path.cwd().parent / 'hrt-w3'
    lane_bytes = sum(p.stat().st_size for p in lane.rglob('*') if p.is_file())
    free = shutil.disk_usage('.').free
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(),
                  checker_sha256=digest(Path(__file__).read_bytes()),
                  guard_receipt=dict(path=args.guard_receipt, sha256=digest(Path(args.guard_receipt).read_bytes())),
                  owned_project_files=inventory, lane_bytes=lane_bytes,
                  filesystem_free_bytes=free, scanned_text_files=checked,
                  absolute_path_matches=matched, generic_prefix_guard_matches=generic,
                  scope='Owned text artifacts. The sole allowed match is an exact frozen generic path-rejection guard, not a concrete local path. Active logs may grow after this scan.')
    atomic_json(Path(args.output), result, exclusive=True)
    print(json.dumps(result), flush=True)
    if (matched or len(generic) != 1 or free < 20_000_000_000
            or sum(v['bytes'] for v in inventory.values()) + lane_bytes >= 3_000_000_000):
        raise SystemExit(2)


if __name__ == '__main__':
    main()
