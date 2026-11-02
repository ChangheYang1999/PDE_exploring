"""Read-only research inputs; write exact compressed copies only inside this review."""
import ast
import gzip
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('.')
OUT = Path('bot_research/experiments/validation/reviews/frr4_final_fortress_001')
UTC = lambda: datetime.now(timezone.utc).isoformat()
sha = lambda b: hashlib.sha256(b).hexdigest()
manifest = {'schema': 1, 'started_utc': UTC(), 'reviewer_model': 'GPT-6 Astra',
            'execution': 'stdlib source and record reads only; no project imports or policy/engine execution',
            'files': {}, 'absent': [], 'snapshot_runs': {}}

def retain(name):
    if name in manifest['files']:
        return gzip.decompress((OUT / manifest['files'][name]['archive']).read_bytes())
    p = Path(name)
    if not p.is_file():
        manifest['absent'].append({'path': name, 'observed_utc': UTC()})
        return None
    before = p.stat()
    b = p.read_bytes()
    after = p.stat()
    digest = sha(b)
    archived = f'inputs/{digest}.gz'
    q = OUT / archived
    q.parent.mkdir(exist_ok=True)
    if not q.exists():
        with q.open('xb') as f:
            f.write(gzip.compress(b, compresslevel=6, mtime=0))
    z = q.read_bytes()
    if gzip.decompress(z) != b:
        raise ValueError('archive mismatch: ' + name)
    manifest['files'][name] = {'sha256': digest, 'bytes': len(b), 'archive': archived,
                              'archive_sha256': sha(z), 'archive_bytes': len(z),
                              'read_utc': UTC(), 'source_mtime_utc': datetime.fromtimestamp(after.st_mtime, timezone.utc).isoformat(),
                              'stat_stable_during_read': (before.st_size, before.st_mtime_ns) == (after.st_size, after.st_mtime_ns)}
    return b

runs = ['bot_research/runs/lead/frr2', 'bot_research/runs/lead/frr3', 'bot_research/runs/lead/frr4',
        'bot_research/runs/lead/frr5', 'bot_research/runs/lead/frr6',
        'bot_research/runs/defense/x215_v46_lead', 'bot_research/runs/defense/x230_v48_lead']
all_rows = []
for run in runs:
    b = retain(run + '/results.jsonl')
    retain(run + '/summary.md')
    if b is None:
        manifest['snapshot_runs'][run] = {'rows': 0, 'results_exists': False}
        continue
    if b and not b.endswith(b'\n'):
        raise ValueError('incomplete final JSON line: ' + run)
    rows = [json.loads(line) for line in b.splitlines() if line.strip()]
    all_rows.extend(rows)
    manifest['snapshot_runs'][run] = {'rows': len(rows), 'results_exists': True}
    if run.endswith(('/frr4', '/frr5')):
        for row in rows:
            if row.get('log'):
                retain(row['log'])

for name in ['../hrt-lead/NOTES_FOR_TEAM.md', '../hrt-lead/RUN_STATUS.md',
             'bot_research/reports/REPORT.md', 'bot_research/notes/defense.md',
             'bot_research/experiments/lead/rr_specs.sh',
             'bot_research/experiments/lead/queue_h16.sh', 'bot_research/experiments/lead/queue_h17.sh',
             'bot_research/experiments/lead/queue_h18.sh', 'bot_research/experiments/lead/queue_h19.sh',
             'bot_research/runs/lead/queue_h16.log', 'bot_research/runs/lead/queue_h17.log',
             'bot_research/runs/lead/queue_h18.log', 'bot_research/runs/lead/queue_h19.log',
             'bot_research/runs/lead/frr4.out', 'bot_research/runs/lead/frr5.out', 'bot_research/runs/lead/frr6.out',
             'bot_research/bots/best.py', 'bot_research/bots/defense/fortress.py',
             'bot_research/experiments/validation/reviews/frr3-extension-review-001.md']:
    retain(name)
for directory, pattern in [('bot_research/harness','*.py'), ('data','*.json'),
                            ('bot_research/bots/defense/frozen/v46','*'), ('bot_research/bots/defense/frozen/v48','*')]:
    for p in sorted(Path(directory).glob(pattern)):
        if p.is_file(): retain(p.as_posix())
for row in all_rows:
    for name in row.get('sources', {}):
        retain(name)

def module_file(name):
    base = Path(*name.split('.'))
    for p in [base.with_suffix('.py'), base / '__init__.py']:
        if p.is_file(): return p.as_posix()
    return None

def closure(spec):
    seen, todo = {}, [spec.partition(':')[0]]
    while todo:
        name = todo.pop()
        if name in seen or not name.startswith('bot_research'): continue
        p = module_file(name)
        if p is None: continue
        seen[name] = p
        parts = name.split('.')
        todo.extend('.'.join(parts[:i]) for i in range(1,len(parts)))
        package = name if p.endswith('/__init__.py') else '.'.join(parts[:-1])
        for node in ast.walk(ast.parse(retain(p).decode())):
            if isinstance(node, ast.Import):
                todo.extend(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    pkg = package.split('.')
                    pkg = pkg[:len(pkg)-(node.level-1)]
                    target = '.'.join(pkg + ([node.module] if node.module else []))
                else: target = node.module or ''
                todo.append(target)
                todo.extend(f'{target}.{a.name}' for a in node.names)
    return sorted(set(seen.values()) | {p.as_posix() for p in Path('bot_research/harness').glob('*.py')})

manifest['current_static_versions'] = {}
for spec in sorted({row[key] for row in all_rows for key in ['spec_a','spec_b']}):
    paths = closure(spec)
    digest = hashlib.sha256()
    for p in paths:
        b = retain(p)
        digest.update(f'{p}\0{sha(b)}\n'.encode())
    manifest['current_static_versions'][spec] = {'version': digest.hexdigest(), 'closure_paths': paths}
manifest['finished_utc'] = UTC()
manifest['archive_unique_bytes'] = sum(p.stat().st_size for p in (OUT/'inputs').glob('*.gz'))
manifest['stat_unstable_inputs'] = [p for p,v in manifest['files'].items() if not v['stat_stable_during_read']]
with (OUT/'input_manifest_001.json').open('x') as f:
    json.dump(manifest,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps({k:manifest[k] for k in ['started_utc','finished_utc','snapshot_runs','archive_unique_bytes','stat_unstable_inputs']},indent=2))
print('input_count',len(manifest['files']))
print('manifest_sha256',sha((OUT/'input_manifest_001.json').read_bytes()))
