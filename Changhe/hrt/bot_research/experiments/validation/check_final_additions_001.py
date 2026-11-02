"""Check final owned additions after the last complete artifact scan."""
from pathlib import Path
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
import re
import shutil


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


start = now()
prior_path = Path('bot_research/runs/validation/final-checks-001.json')
prior_raw = prior_path.read_bytes()
assert sha(prior_raw) == '0cecd0f0558c560715ab7a036deee29094905b4d4fd965cff2bf4e1805bee33b'
prior = json.loads(prior_raw)
cutoff_text = next(x['started_utc'] for x in prior['steps'] if x['name'] == 'artifacts')
cutoff = datetime.fromisoformat(cutoff_text).timestamp()
roots = [Path('bot_research/bots/counters'), Path('bot_research/experiments/validation'),
         Path('bot_research/runs/validation'), Path('bot_research/notes/validation.md')]
pattern = re.compile(r'(?<![A-Za-z0-9_.-])/(?:' + '|'.join(('mnt', 'home', 'efs', 'tmp')) + r')(?:/|\b)')
suffixes = {'.py', '.json', '.jsonl', '.md', '.txt', '.log', '.out', '.csv', '.diff', '.sh'}
changed = []
issues = []
inventory = {}
for root in roots:
    count = total = 0
    paths = [root] if root.is_file() else root.rglob('*')
    for path in paths:
        if not path.is_file():
            continue
        st = path.stat()
        count += 1
        total += st.st_size
        if st.st_mtime < cutoff:
            continue
        raw = path.read_bytes()
        entry = {'path': str(path), 'bytes': len(raw), 'sha256': sha(raw),
                 'mtime_utc': datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat()}
        if path.suffix == '.gz':
            raw = gzip.decompress(raw)
            entry['decoded_bytes'] = len(raw)
            entry['decoded_sha256'] = sha(raw)
        if path.suffix in suffixes or path.suffix == '.gz':
            try:
                text = raw.decode()
            except UnicodeDecodeError:
                issues.append({'path': str(path), 'issue': 'Cannot decode text artifact'})
            else:
                for line_number, line in enumerate(text.splitlines(), 1):
                    if pattern.search(line):
                        issues.append({'path': str(path), 'line': line_number, 'issue': 'Absolute local path prefix'})
        changed.append(entry)
    inventory[str(root)] = {'files': count, 'bytes': total}
lane = Path('../hrt-w3')
lane_bytes = sum(p.stat().st_size for p in lane.rglob('*') if p.is_file())
free = shutil.disk_usage('.').free
owned = sum(x['bytes'] for x in inventory.values()) + lane_bytes
receipt = {
    'schema': 'final-additions-path-audit-001', 'started_utc': start, 'completed_utc': now(),
    'cutoff_utc': cutoff_text, 'prior_receipt_sha256': sha(prior_raw),
    'changed_files': changed, 'changed_files_count': len(changed), 'issues': issues,
    'owned_project_files': inventory, 'lane_bytes': lane_bytes, 'owned_bytes_including_lane': owned,
    'filesystem_free_bytes': free, 'all_passed': not issues and owned < 3_000_000_000 and free >= 20_000_000_000,
    'scope': 'Files modified since the start of the final full artifact scan, including decompressed new gzip archives. Protected files and original tests reuse the authenticated final-checks receipt. Later writes are outside this capture.',
    'script_sha256': sha(Path(__file__).read_bytes()),
}
out = Path('bot_research/runs/validation/artifacts-final-additions-001.json')
with out.open('x') as stream:
    stream.write(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
print(json.dumps({k: v for k, v in receipt.items() if k not in ('changed_files', 'owned_project_files')}, indent=2))
if not receipt['all_passed']:
    raise SystemExit(2)
