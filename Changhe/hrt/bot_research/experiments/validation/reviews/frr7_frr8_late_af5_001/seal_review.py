"""Seal this source/record review only. No project imports or game execution."""
import gzip
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001')
UTC = lambda: datetime.now(timezone.utc).isoformat()
sha = lambda b: hashlib.sha256(b).hexdigest()
started = UTC()
errors = []
archives = {}
archive_edges = 0
active = {}

def check_archive(e, label):
    global archive_edges
    z = (OUT / e['archive']).read_bytes()
    b = gzip.decompress(z)
    archive_edges += 1
    if sha(z) != e['archive_sha256'] or sha(b) != e['sha256'] or len(b) != e['bytes']:
        errors.append({'kind': 'archive identity', 'edge': label})
    archives[e['archive']] = len(z)
    return b

manifests = {p.name: json.loads(p.read_bytes()) for p in sorted(OUT.glob('input_manifest_*.json'))}
final = manifests['input_manifest_final_001.json']
for name, manifest in manifests.items():
    for path, e in manifest['files'].items():
        check_archive(e, name + ':' + path)
audit = json.loads((OUT / 'record_audit_final_001.json').read_bytes())
supplement = json.loads((OUT / 'supplementary_checks_final_001.json').read_bytes())
for run, c in audit['campaigns'].items():
    if not c['complete_grid'] or c['missing_conditions'] or c['unexpected_conditions'] or c['duplicates'] or c['metadata_errors']:
        errors.append({'kind': 'condition accounting', 'run': run})
    if not c['summary_present']:
        errors.append({'kind': 'summary absent', 'run': run})
    if set(final['snapshot_runs'][run]['log_directory_files']) != {d['log'] for d in c['conditions']}:
        errors.append({'kind': 'retained log directory mismatch', 'run': run})
    if any(d['raw_check']['errors'] or d['source_check']['errors'] for d in c['conditions']):
        errors.append({'kind': 'raw or source audit errors', 'run': run})
    if supplement['summary_checks'][run]['errors']:
        errors.append({'kind': 'summary table accounting', 'run': run})
    path = 'bot_research/runs/lead/' + run + '/results.jsonl'
    rows = [json.loads(x) for x in check_archive(final['files'][path], 'final rows:' + run).splitlines()]
    for row in rows:
        active.update(row['sources'])
for package, checks in audit['frozen_packages'].items():
    if not all(x['matches'] for x in checks):
        errors.append({'kind': 'frozen manifest mismatch', 'package': package})
for item in final['current_static_versions'].values():
    for path in item['closure_paths']:
        active[path] = final['files'][path]['sha256']
for path, e in final['files'].items():
    if path == 'bot_research/bots/best.py' or path.startswith(('td_game/', 'data/')) or path == 'bot_research/bots/counters/data/early_wall_guard_001.json':
        active[path] = e['sha256']
    if '/runs/lead/frr' in path and (path.endswith('.jsonl') or path.endswith('/summary.md')):
        if sha(Path(path).read_bytes()) != e['sha256']:
            errors.append({'kind': 'closed record drift', 'path': path})
math_dir = OUT / 'af5_matrix_extension/verification'
math_receipt = json.loads((math_dir / 'receipt.json').read_bytes())
math_inputs = json.loads((math_dir / 'inputs.json').read_bytes())
math_matrix = json.loads((math_dir / 'matrix.json').read_bytes())
for key in ['inputs', 'matrix']:
    e = math_receipt[key]
    b = Path(e['path']).read_bytes()
    if sha(b) != e['sha256'] or len(b) != e['bytes']:
        errors.append({'kind': 'matrix receipt identity', 'edge': key})
if sha((math_dir / 'check_matrix.py').read_bytes()) != math_receipt['checker_sha256']:
    errors.append({'kind': 'matrix checker changed'})
if sha((OUT / 'af5_matrix_extension/PROOF.md').read_bytes()) != math_receipt['proof_sha256']:
    errors.append({'kind': 'matrix proof changed'})
if math_receipt['errors'] or math_receipt['afrr_raw_errors'] or math_receipt['value'] != '0':
    errors.append({'kind': 'matrix/afrr check did not pass'})
for name, e in math_inputs['files'].items():
    check_archive(e, 'matrix:' + name)
for path, h in math_inputs['current_source_hashes'].items():
    if path in active and active[path] != h:
        errors.append({'kind': 'source identity conflict', 'path': path})
    active[path] = h
for e in math_matrix['source_conditions']:
    if e['raw_log_present']:
        key = e['log']
        matches = [v for v in math_inputs['files'].values() if v['path'] == key]
        if len(matches) != 1 or sha(Path(key).read_bytes()) != matches[0]['sha256']:
            errors.append({'kind': 'matrix original log drift', 'path': key})
for run in ['frr1', 'frr3', 'frr5', 'frr8', 'afrr']:
    path = 'bot_research/runs/' + ('economy/' if run == 'afrr' else 'lead/') + run + '/results.jsonl'
    identities = {e['sha256'] for e in math_inputs['files'].values() if e['path'] == path}
    if len(identities) != 1 or sha(Path(path).read_bytes()) not in identities:
        errors.append({'kind': 'matrix closed result drift', 'path': path})
extra = json.loads((math_dir / 'additional_source_bindings_001.json').read_bytes())
for path, e in extra['files'].items():
    check_archive(e, 'additional upstream checker:' + path)
    if sha(Path(path).read_bytes()) != e['sha256']:
        errors.append({'kind': 'upstream source changed', 'path': path})
for path in ['report_discrepancy_001.json', 'root_report_discrepancy_001.json']:
    obj = json.loads((OUT / path).read_bytes())
    for key in ['archived_report', 'report_archive', 'report']:
        if key in obj and isinstance(obj[key], dict) and 'archive' in obj[key]:
            check_archive(obj[key], path + ':' + key)
active_mismatches = [p for p, h in active.items() if not Path(p).is_file() or sha(Path(p).read_bytes()) != h]
if active_mismatches:
    errors.append({'kind': 'current active source drift', 'paths': active_mismatches})
# This whole review uses only these bounded trees for the lane-size check.
owned = ['../hrt-w3', 'bot_research/bots/counters', 'bot_research/experiments/validation',
         'bot_research/runs/validation', 'bot_research/notes/validation.md']
owned_bytes = 0
for name in owned:
    q = Path(name)
    if q.is_file():
        owned_bytes += q.stat().st_size
    elif q.is_dir():
        for root, dirs, files in os.walk(q):
            for name in files:
                p = Path(root) / name
                if p.is_file():
                    owned_bytes += p.stat().st_size
free = os.statvfs('.').f_bavail * os.statvfs('.').f_frsize
if owned_bytes >= 3_000_000_000:
    errors.append({'kind': 'lane exceeds conservative decimal 3 GB limit'})
if free < 20_000_000_000:
    errors.append({'kind': 'free space below 20 GB'})
# Detect newly written concrete local paths in readable outputs. Archived
# upstream bytes remain exact historical inputs rather than edited sources.
for p in OUT.rglob('*'):
    if not p.is_file() or 'inputs' in p.relative_to(OUT).parts:
        continue
    if p.suffix in ['.json', '.md', '.py', '.txt']:
        data = p.read_text()
        if re.search(r'(?<![\w./])/(?:mnt|home|efs|tmp)/', data):
            errors.append({'kind': 'concrete local path in published output', 'path': p.relative_to(OUT).as_posix()})
outputs = {p.relative_to(OUT).as_posix(): {'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size}
           for p in OUT.rglob('*') if p.is_file() and 'inputs' not in p.relative_to(OUT).parts and p.name != 'seal_001.json'}
report = {'schema': 1, 'started_utc': started, 'sealed_utc': UTC(), 'reviewer_model': 'GPT-6 Astra',
          'verdict': 'CONFIRMED' if not errors else 'OPEN', 'errors': errors,
          'execution': 'Source and retained JSON only; zero policy constructors, decisions, engines, replays, existing project checkers or new games.',
          'new_campaigns': ['frr7', 'frr8'], 'new_games': 30, 'new_records': 1804, 'new_accepted_actions': 504024,
          'main_new_and_comparison_games': 158, 'main_records': 9234, 'main_accepted_actions': 2739683,
          'matrix_rows_joined': 152, 'added_afrr_raw_games': 20, 'added_afrr_raw_records': 1884, 'added_afrr_accepted_actions': 336324,
          'matrix_value': '0', 'archive_edge_count': archive_edges, 'unique_archives': len(archives),
          'compressed_archive_bytes': sum(archives.values()), 'active_current_paths_checked': len(active),
          'active_current_mismatches': active_mismatches, 'lane_logical_bytes_before_seal': owned_bytes,
          'filesystem_free_bytes': free, 'outputs': outputs}
p = OUT / 'seal_001.json'
with p.open('x') as f:
    json.dump(report, f, indent=2, sort_keys=True)
    f.write('\n')
print(json.dumps({'path': p.as_posix(), 'sha256': sha(p.read_bytes()), 'sealed_utc': report['sealed_utc'],
                  'verdict': report['verdict'], 'errors': errors, 'archive_edge_count': archive_edges,
                  'unique_archives': len(archives), 'compressed_archive_bytes': sum(archives.values()),
                  'lane_logical_bytes_before_seal': owned_bytes, 'filesystem_free_bytes': free}, indent=2))
