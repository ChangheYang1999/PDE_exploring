"""Exact-supplement manifest writer for g4_v1 (verifier 14:29Z: do not use the broad find roots of freeze_manifest_v3.sh for a two-entry supplement).
Copies the frozen g3_v1 manifest object, re-verifies every existing files[] and frozen_181_closure[] row against the live bytes, and appends EXACTLY two
new rows: outputs/campaign860/campaign_policy_v3.json and bin/supervise860_v4.sh (installed copies of the pending_g4 drafts, verified byte-equal to them).
Everything else (every old row, the closure, accepted278 and seed hashes, kappa entries) is preserved unchanged. Refuses if the target exists, if any old
row mismatches, if an added path is already listed, or if an installed file differs from its draft. Run ONLY on the lead's word after the bench read:
    env/bin/python outputs/dev_v9/pending_g4/freeze_g4_supplement.py [--dry-run]
Writes outputs/manifests/code_manifest_g4_v1.json and prints its sha256."""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, hashlib, os, sys, time
LANE = (_artifact_root); BASE_TAG = 'g3_v1'; TAG = 'g4_v1'
ADD = [('outputs/campaign860/campaign_policy_v3.json', 'outputs/dev_v9/pending_g4/campaign_policy_v3.json'), ('bin/supervise860_v4.sh', 'outputs/dev_v9/pending_g4/supervise860_v4.sh')]
DRY = '--dry-run' in sys.argv
def sha(p):
    with open(p, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()
base_path = os.path.join(LANE, 'outputs/manifests/code_manifest_%s.json' % BASE_TAG); out_path = os.path.join(LANE, 'outputs/manifests/code_manifest_%s.json' % TAG)
if os.path.exists(out_path): sys.exit('refuse: %s exists' % out_path)
m = json.load(open(base_path)); base_sha = sha(base_path)
if m.get('tag') != BASE_TAG: sys.exit('refuse: base tag %r' % m.get('tag'))
bad = []
for row in m['files'] + m['frozen_181_closure']:
    p = os.path.join(LANE, row['path'])
    if not os.path.exists(p) or sha(p) != row['sha256'] or ('bytes' in row and os.path.getsize(p) != row['bytes']): bad.append(row['path'])
if bad: sys.exit('refuse: %d base rows do not match the live bytes: %s' % (len(bad), bad[:5]))
listed = {row['path'] for row in m['files']}
new_rows = []
for path, draft in ADD:
    if path in listed: sys.exit('refuse: %s already listed in %s' % (path, BASE_TAG))
    live = os.path.join(LANE, path); dr = os.path.join(LANE, draft)
    if not os.path.exists(live): sys.exit('refuse: %s not installed (copy the draft %s first)' % (path, draft))
    if sha(live) != sha(dr): sys.exit('refuse: installed %s differs from the draft %s' % (path, draft))
    new_rows.append({'path': path, 'bytes': os.path.getsize(live), 'sha256': sha(live)})
out = dict(m); out['tag'] = TAG; out['utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()); out['base_manifest_tag'] = BASE_TAG; out['base_manifest_sha256'] = base_sha
out['files'] = list(m['files']) + new_rows
out['supplement_statement'] = 'exact supplement of %s (sha256 %s): every files[] row and the frozen_181_closure copied unchanged; exactly %d rows added: %s; written by outputs/dev_v9/pending_g4/freeze_g4_supplement.py (sha256 %s)' % (BASE_TAG, base_sha, len(new_rows), [r['path'] for r in new_rows], sha(os.path.abspath(__file__)))
assert len(out['files']) == len(m['files']) + 2 and out['frozen_181_closure'] == m['frozen_181_closure']
text = json.dumps(out, indent=1) + '\n'
if DRY: print('DRY RUN OK: base rows verified (%d files + %d closure); would add %s; would write %s' % (len(m['files']), len(m['frozen_181_closure']), new_rows, out_path)); sys.exit(0)
tmp = out_path + '.partial'
with open(tmp, 'w') as f: f.write(text); f.flush(); os.fsync(f.fileno())
os.replace(tmp, out_path); print('wrote', out_path, 'sha256', sha(out_path), 'files', len(out['files']), 'closure', len(out['frozen_181_closure']))
